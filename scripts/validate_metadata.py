#!/usr/bin/env python3
"""Validate public evidence and discovery metadata without executing an AI workflow."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


schema_path = ROOT / "docs" / "evidence-record.schema.json"
schema = load_json(schema_path)

try:
    Draft202012Validator.check_schema(schema)
except Exception as exc:
    fail(f"{schema_path.relative_to(ROOT)} is not a valid Draft 2020-12 schema: {exc}")

validator = Draft202012Validator(schema, format_checker=FormatChecker())
example_paths = sorted((ROOT / "examples").glob("evidence-record*.json"))

if not example_paths:
    fail("No examples/evidence-record*.json files were found")

for example_path in example_paths:
    instance = load_json(example_path)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
    if errors:
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            print(
                f"ERROR: {example_path.relative_to(ROOT)}:{location}: {error.message}",
                file=sys.stderr,
            )
        raise SystemExit(1)

codemeta_path = ROOT / "codemeta.json"
codemeta = load_json(codemeta_path)
required_codemeta = {
    "@context",
    "@type",
    "@id",
    "name",
    "description",
    "codeRepository",
    "issueTracker",
    "url",
    "license",
    "dateModified",
    "author",
    "keywords",
}
missing = sorted(required_codemeta - codemeta.keys())
if missing:
    fail(f"codemeta.json is missing required project fields: {', '.join(missing)}")

expected = {
    "@context": "https://w3id.org/codemeta/4.0",
    "@type": "SoftwareSourceCode",
    "@id": "https://github.com/BotShelfVampire/botshelf-ai-team-registry",
    "codeRepository": "https://github.com/BotShelfVampire/botshelf-ai-team-registry",
    "issueTracker": "https://github.com/BotShelfVampire/botshelf-ai-team-registry/issues",
    "license": "https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/LICENSE",
}
for key, value in expected.items():
    if codemeta.get(key) != value:
        fail(f"codemeta.json {key!r} must be {value!r}")

citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
if "license: MIT" in citation:
    fail("CITATION.cff must not claim MIT; the repository uses custom license terms")

print(f"Validated {schema_path.relative_to(ROOT)}")
for example_path in example_paths:
    print(f"Validated {example_path.relative_to(ROOT)}")
print("Validated codemeta.json project invariants")
print("Validated CITATION.cff license invariant")
