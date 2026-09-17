import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from verify_gate import GateError, main, verify


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="bsv-artifact-gate-")
        self.addCleanup(self.temp.cleanup)
        self.artifact = Path(self.temp.name) / "draft.txt"
        self.review = Path(self.temp.name) / "review.json"
        self.artifact.write_bytes("Demo only: export CSV. 日本語\n".encode("utf-8"))
        self.record = {
            "artifact_sha256": hashlib.sha256(self.artifact.read_bytes()).hexdigest(),
            "decision": "approve",
            "checks": {"source_support": "pass", "scope": "pass", "no_private_data": "pass"},
        }
        self.save()

    def save(self):
        self.review.write_text(json.dumps(self.record), encoding="utf-8")

    def test_matching_artifact_passes(self):
        self.assertEqual(verify(self.artifact, self.review), self.record["artifact_sha256"])

    def test_one_extra_byte_fails(self):
        self.artifact.write_bytes(self.artifact.read_bytes() + b" ")
        with self.assertRaises(GateError):
            verify(self.artifact, self.review)

    def test_different_line_endings_fail(self):
        self.artifact.write_bytes(self.artifact.read_bytes().replace(b"\n", b"\r\n"))
        with self.assertRaises(GateError):
            verify(self.artifact, self.review)

    def test_reject_and_unknown_decisions_fail(self):
        for decision in ("reject", "unknown", "APPROVE", True, None):
            with self.subTest(decision=decision):
                self.record["decision"] = decision
                self.save()
                with self.assertRaises(GateError):
                    verify(self.artifact, self.review)

    def test_failed_unknown_or_missing_check_fails(self):
        valid = dict(self.record["checks"])
        for checks in ({"scope": "pass"}, {**valid, "scope": "unknown"},
                       {**valid, "source_support": "fail"}, {**valid, "scope": True}, []):
            with self.subTest(checks=checks):
                self.record["checks"] = checks
                self.save()
                with self.assertRaises(GateError):
                    verify(self.artifact, self.review)

    def test_extra_field_fails(self):
        self.record["publish_now"] = True
        self.save()
        with self.assertRaises(GateError):
            verify(self.artifact, self.review)

    def test_missing_field_fails(self):
        del self.record["artifact_sha256"]
        self.save()
        with self.assertRaises(GateError):
            verify(self.artifact, self.review)

    def test_bad_digest_fails(self):
        for digest in ("0" * 64, "z" * 64, "abc", None, 123):
            with self.subTest(digest=digest):
                self.record["artifact_sha256"] = digest
                self.save()
                with self.assertRaises(GateError):
                    verify(self.artifact, self.review)

    def test_duplicate_key_fails(self):
        self.review.write_text('{"decision":"reject","decision":"approve"}', encoding="utf-8")
        with self.assertRaises(GateError):
            verify(self.artifact, self.review)

    def test_invalid_or_non_object_json_fails(self):
        for value in ("{", "[]", "null", '"approve"'):
            with self.subTest(value=value):
                self.review.write_text(value, encoding="utf-8")
                with self.assertRaises(ValueError):
                    verify(self.artifact, self.review)

    def test_cli_success_does_not_grant_publication(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main([str(self.artifact), str(self.review)])
        self.assertEqual(code, 0)
        self.assertIn("Publication is NOT authorized", output.getvalue())

    def test_cli_missing_file_returns_failure(self):
        with contextlib.redirect_stdout(io.StringIO()):
            code = main([str(self.artifact), str(self.review) + ".missing"])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
