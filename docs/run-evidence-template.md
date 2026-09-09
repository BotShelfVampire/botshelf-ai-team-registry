# Record a real AI workflow run

A useful run record lets another person understand what was executed and where it failed. Keep this separate from a sample expected answer.

```text
Status: Untested / executed with failures / executed and checked
Date:
Team and runtime directory:
Git commit or source revision:
Runtime and dependency versions:
Model name, tag, and digest if available:
Hardware / relevant environment:
Settings:
Input (redacted):
Actual output or artifact:
How the output was captured:
Checks performed:
Observed failures:
Unexpected actions:
Known limits:
Reviewer:
```

Use non-sensitive or permissioned inputs. Redact secrets and private records before publishing evidence. Do not replace failed output with an ideal answer.

A syntax check proves parsing. A JSON import proves that specific import. A completed model call proves that a call returned. None alone proves task accuracy, tool safety, or reliability across other models and inputs.

Publish a verification claim only as narrowly as the record supports. If a website badge refers to another revision, retain the distinction.
