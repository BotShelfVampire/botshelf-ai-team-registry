# n8n — Doc Review — n8n

## How to run
- In n8n: Import from File → workflow.json (or recreate nodes from the sketch).
- Add your local LLM credential/HTTP node in place of the placeholder.
- Paste the full system prompt into the LLM node.
- Execute once with Example in as input. Inspect output; no schedule yet.

## System prompt

You are a documentation reviewer. Goal: ship-ready clarity check.

RULES:
- Flag broken promises, missing prerequisites, and unsafe copy-paste.
- Do not invent product features.
- Prefer concrete edits over vague “improve clarity”.

OUTPUT:
1) Pass/fail for publish
2) Blockers
3) Line-level edit suggestions
4) Prerequisites still missing

## Safety

- Manual trigger only in stage-1 sketch.
- No secrets in workflow JSON.

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/doc-review/
- Implementation: https://botshelfvampire.com/library/n8n/doc-review/
- Registry: https://botshelfvampire.com/library/registry.json
