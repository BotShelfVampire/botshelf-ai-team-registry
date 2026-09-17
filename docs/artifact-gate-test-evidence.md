# Artifact-gate test evidence

Status: deterministic checker executed and checked; no AI model or live publisher run.

- Date: 2026-09-17, approximately 08:04 JST.
- Runtime: Python 3.12.14, local macOS environment.
- Dependencies: Python standard library only; no package installation.
- Input: temporary fictional UTF-8 text (including Japanese) and synthetic review JSON.
- Scope: the verifier and tests distributed with this record, not a deployed multi-agent service.

From examples/artifact-gate, the command was:

~~~sh
python3 -m unittest -v test_verify_gate.py
~~~

Result:

~~~text
Ran 12 tests in 0.007s

OK
~~~

Covered cases:

1. Exact matching artifact and approved review.
2. One extra byte after review.
3. A change from LF to CRLF line endings.
4. Rejected, unknown, uppercase, boolean, and null decisions.
5. Missing, unresolved, failed, wrong-type checks.
6. Extra top-level field.
7. Missing digest field.
8. Wrong, malformed, and non-string digests.
9. Duplicate JSON key.
10. Malformed JSON and non-object JSON values.
11. Successful CLI function return plus explicit non-authorization message.
12. Missing review file returning failure.

The CLI-function tests invoke main directly with arguments and capture its output. They do not test a publisher integration. No model calls, network calls, external writes, or purchases are part of these tests. The tests create and clean up their own temporary fixtures.

Known limits: no reviewer authentication, storage-permission enforcement, signature validation, semantic fact checking, live platform verification, concurrent-file mutation protection, or performance benchmark. A digest match is not a trustworthy approval if the review record can be forged. Other Python versions and operating systems were not run.

Record your own run against a pinned repository commit; do not transfer this result to modified code or treat it as a Verified badge for unrelated Library recipes.
