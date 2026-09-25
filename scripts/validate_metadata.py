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


directory_listing_path = ROOT / "docs" / "directory-listing.json"
directory_listing = load_json(directory_listing_path)
required_listing = {
    "schemaVersion",
    "lastUpdated",
    "product",
    "separateSurface",
    "descriptions",
    "categories",
    "tags",
    "verificationStates",
    "evidence",
    "claims",
    "license",
    "submissionControls",
}
if not isinstance(directory_listing, dict):
    fail("docs/directory-listing.json must be a JSON object")
missing = sorted(required_listing - directory_listing.keys())
if missing:
    fail(f"docs/directory-listing.json is missing required fields: {', '.join(missing)}")

product = directory_listing.get("product", {})
if product.get("surface") != "build-library":
    fail("docs/directory-listing.json product.surface must be 'build-library'")
if product.get("url") != "https://botshelfvampire.com/library/":
    fail("docs/directory-listing.json must use the canonical Build Library URL")

separate_surface = directory_listing.get("separateSurface", {})
if separate_surface.get("surface") != "marketplace":
    fail("docs/directory-listing.json separateSurface.surface must be 'marketplace'")
if separate_surface.get("separateFromBuildLibrary") is not True:
    fail("docs/directory-listing.json must keep Marketplace separate from Build Library")

expected_states = ["Verified", "Untested", "Partial", "Blocked", "Unverified"]
if directory_listing.get("verificationStates") != expected_states:
    fail("docs/directory-listing.json verificationStates must preserve the canonical ordered states")

evidence = directory_listing.get("evidence", {})
failed_evidence_url = (
    "https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/"
    "examples/evidence-record.research-desk-2026-09-10.json"
)
if evidence.get("failedEvaluation") != failed_evidence_url:
    fail("docs/directory-listing.json must link the canonical failed-evaluation record")

claims = directory_listing.get("claims", {})
if not claims.get("supported") or not claims.get("prohibited"):
    fail("docs/directory-listing.json must contain supported and prohibited claims")
prohibited_text = " ".join(claims["prohibited"]).lower()
if "open source" not in prohibited_text or "osi-approved" not in prohibited_text:
    fail("docs/directory-listing.json must prohibit open-source and OSI-approved claims")

license_metadata = directory_listing.get("license", {})
if license_metadata.get("label") != "custom free-use-at-own-risk license":
    fail("docs/directory-listing.json must use the repository's custom license wording")
if license_metadata.get("osiApproved") is not False:
    fail("docs/directory-listing.json must not claim OSI approval")
if license_metadata.get("openSourceClaimAllowed") is not False:
    fail("docs/directory-listing.json must not allow an open-source claim")

controls = directory_listing.get("submissionControls", {})
for field in ("useOnlyOfficialVerifiedAssets", "requireOfficialRouteCheck", "requireDuplicateCheck", "requireFeeCheck"):
    if controls.get(field) is not True:
        fail(f"docs/directory-listing.json submissionControls.{field} must be true")
if controls.get("externalAcceptanceImplied") is not False:
    fail("docs/directory-listing.json must not imply external acceptance")

citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
if "license: MIT" in citation:
    fail("CITATION.cff must not claim MIT; the repository uses custom license terms")

print(f"Validated {schema_path.relative_to(ROOT)}")
for example_path in example_paths:
    print(f"Validated {example_path.relative_to(ROOT)}")
print("Validated codemeta.json project invariants")
print("Validated docs/directory-listing.json submission invariants")
print("Validated CITATION.cff license invariant")
