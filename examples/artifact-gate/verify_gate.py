"""Check a review against exact artifact bytes. This does not authorize publication."""

import argparse
import hashlib
import json
from pathlib import Path
import re


class GateError(ValueError):
    pass


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise GateError("Duplicate JSON key: " + key)
        result[key] = value
    return result


def verify(artifact, review):
    """Return the checked digest or raise; no network, writes, or model calls."""
    record = json.loads(Path(review).read_text(encoding="utf-8"),
                        object_pairs_hook=unique_keys)
    required = {"artifact_sha256", "decision", "checks"}
    if not isinstance(record, dict) or set(record) != required:
        raise GateError("Review must contain exactly artifact_sha256, decision, checks")
    expected = record["artifact_sha256"]
    if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
        raise GateError("Expected a lowercase SHA-256 hex digest")
    if record["decision"] != "approve":
        raise GateError("Review decision is not approve")
    gates = {"source_support": "pass", "scope": "pass", "no_private_data": "pass"}
    if record["checks"] != gates:
        raise GateError("Every required check must be present and pass")
    actual = hashlib.sha256(Path(artifact).read_bytes()).hexdigest()
    if actual != expected:
        raise GateError("Artifact changed or the review belongs to another artifact")
    return actual


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path)
    parser.add_argument("review", type=Path)
    args = parser.parse_args(argv)
    try:
        digest = verify(args.artifact, args.review)
    except (OSError, ValueError, UnicodeError) as error:
        print("FAIL: " + str(error))
        return 2
    print("PASS: exact artifact matches approved review: " + digest)
    print("Publication is NOT authorized by this check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
