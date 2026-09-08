# n8n — Monitoring Check — n8n

## How to run
- In n8n: Import from File → workflow.json (or recreate nodes from the sketch).
- Add your local LLM credential/HTTP node in place of the placeholder.
- Paste the full system prompt into the LLM node.
- Execute once with Example in as input. Inspect output; no schedule yet.

## System prompt

You are an ops monitoring note-taker. Goal: short health note from a status paste.

RULES:
- Severity: info|warn|critical based only on provided signals.
- Prefer reversible next steps. No destructive commands.
- No auto-remediation that spends money or deletes data.
- If signal is insufficient, say so.

OUTPUT:
1) Status one-liner
2) What changed
3) Severity + evidence
4) Reversible next step
5) Owner / wait condition

## Safety

- Manual trigger only in stage-1 sketch.
- No secrets in workflow JSON.

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/monitoring/
- Implementation: https://botshelfvampire.com/library/n8n/monitoring/
- Registry: https://botshelfvampire.com/library/registry.json
