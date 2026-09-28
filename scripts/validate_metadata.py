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

route_status_schema_path = ROOT / "docs" / "directory-route-status.schema.json"
route_status_path = ROOT / "docs" / "directory-route-status.json"
route_status_schema = load_json(route_status_schema_path)
route_status = load_json(route_status_path)

try:
    Draft202012Validator.check_schema(route_status_schema)
except Exception as exc:
    fail(
        f"{route_status_schema_path.relative_to(ROOT)} is not a valid "
        f"Draft 2020-12 schema: {exc}"
    )

route_status_validator = Draft202012Validator(
    route_status_schema,
    format_checker=FormatChecker(),
)
route_status_errors = sorted(
    route_status_validator.iter_errors(route_status),
    key=lambda error: list(error.absolute_path),
)
if route_status_errors:
    for error in route_status_errors:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        print(
            f"ERROR: {route_status_path.relative_to(ROOT)}:{location}: {error.message}",
            file=sys.stderr,
        )
    raise SystemExit(1)

routes = route_status["routes"]
if route_status["routeCount"] != len(routes):
    fail("docs/directory-route-status.json routeCount must equal the number of routes")

route_ids = [route["id"] for route in routes]
route_names = [route["name"] for route in routes]
if len(route_ids) != len(set(route_ids)):
    fail("docs/directory-route-status.json route ids must be unique")
if len(route_names) != len(set(route_names)):
    fail("docs/directory-route-status.json route names must be unique")

classification_counts = {
    "verified-free": 0,
    "conditional-free": 0,
    "unverified": 0,
    "temporarily-unavailable": 0,
    "paid-only": 0,
}
lifecycle_counts = {"submitted": 0, "accepted": 0, "published": 0}

for route in routes:
    classification = route["zeroCostPath"]["classification"]
    classification_counts[classification] += 1

    lifecycle = route["lifecycle"]
    for state in lifecycle_counts:
        lifecycle_counts[state] += int(lifecycle[state])

    if lifecycle["accepted"] and not lifecycle["submitted"]:
        fail(f"directory route {route['id']!r} cannot be accepted before submission")
    if lifecycle["published"] and not lifecycle["accepted"]:
        fail(f"directory route {route['id']!r} cannot be published before acceptance")

    evidence = route["externalEvidence"]
    if lifecycle["submitted"] and not evidence["confirmationReceipt"]:
        fail(f"directory route {route['id']!r} needs a confirmationReceipt when submitted")
    if lifecycle["published"] and not evidence["liveUrl"]:
        fail(f"directory route {route['id']!r} needs a liveUrl when published")

    if classification in {"paid-only", "temporarily-unavailable", "unverified"}:
        if route["zeroCostPath"]["currentlyActionable"]:
            fail(
                f"directory route {route['id']!r} cannot be currently actionable "
                f"with classification {classification!r}"
            )

    automation = route["automation"]
    if not automation["automatedSubmissionPermitted"] and not automation["manualOwnerActionRequired"]:
        fail(
            f"directory route {route['id']!r} must preserve a manual owner gate "
            "when automated submission is not permitted"
        )

    audit_path = ROOT / route["audit"]["path"]
    if not audit_path.is_file():
        fail(
            f"directory route {route['id']!r} references missing audit file "
            f"{route['audit']['path']!r}"
        )

summary = route_status["summary"]
if summary["byZeroCostClassification"] != classification_counts:
    fail(
        "docs/directory-route-status.json classification summary must match "
        "the route records"
    )
for state, count in lifecycle_counts.items():
    if summary[state] != count:
        fail(
            f"docs/directory-route-status.json summary.{state} must match "
            "the route records"
        )


citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
if "license: MIT" in citation:
    fail("CITATION.cff must not claim MIT; the repository uses custom license terms")

print(f"Validated {schema_path.relative_to(ROOT)}")
for example_path in example_paths:
    print(f"Validated {example_path.relative_to(ROOT)}")
print("Validated codemeta.json project invariants")
print("Validated docs/directory-listing.json submission invariants")\nprint("Validated docs/directory-route-status.json against its schema and lifecycle invariants")
print("Validated CITATION.cff license invariant")
