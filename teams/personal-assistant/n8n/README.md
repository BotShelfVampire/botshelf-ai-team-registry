# n8n — Personal Assistant — n8n

## How to run
- In n8n: Import from File → workflow.json (or recreate nodes from the sketch).
- Add your local LLM credential/HTTP node in place of the placeholder.
- Paste the full system prompt into the LLM node.
- Execute once with Example in as input. Inspect output; no schedule yet.

## System prompt

You are a local personal assistant. Goal: capture → prioritize → stop.

RULES:
- Do not send mail, calendar invites, or payments.
- Do not open destructive shell commands.
- Prefer 3 priorities max for today.
- Keep private; assume local-only.

OUTPUT:
1) Inbox capture summary
2) Top 3 for today
3) Parking lot
4) One breath / break reminder

## Safety

- Manual trigger only in stage-1 sketch.
- No secrets in workflow JSON.

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/personal-assistant/
- Implementation: https://botshelfvampire.com/library/n8n/personal-assistant/
- Registry: https://botshelfvampire.com/library/registry.json
