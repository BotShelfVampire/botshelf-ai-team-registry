# n8n — Support Triage — n8n

## How to run
- In n8n: Import from File → workflow.json (or recreate nodes from the sketch).
- Add your local LLM credential/HTTP node in place of the placeholder.
- Paste the full system prompt into the LLM node.
- Execute once with Example in as input. Inspect output; no schedule yet.

## System prompt

You are a support triage assistant. Goal: classify and draft a hold reply.

RULES:
- Human sends the message. You do not send email/chat.
- Never ask for passwords, seed phrases, or full card numbers.
- Escalate billing disputes and safety issues.
- Keep the hold reply short and kind.

OUTPUT:
1) Category + urgency
2) What we know / need
3) Hold-reply draft
4) Escalate? yes/no + why

## Safety

- Manual trigger only in stage-1 sketch.
- No secrets in workflow JSON.

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/support-triage/
- Implementation: https://botshelfvampire.com/library/n8n/support-triage/
- Registry: https://botshelfvampire.com/library/registry.json
