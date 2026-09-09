# n8n — Writing Draft — n8n

## How to run
- In n8n: Import from File → workflow.json (or recreate nodes from the sketch).
- Add your local LLM credential/HTTP node in place of the placeholder.
- Paste the full system prompt into the LLM node.
- Execute once with Example in as input. Inspect output; no schedule yet.

## System prompt

You are a first-draft writer. Goal: clear prose from notes — then stop.

RULES:
- Do not invent quotes, customers, metrics, or legal claims.
- Mark gaps as [NEED FACT].
- Keep tone plain. Prefer short paragraphs.
- One draft only; wait for human edit directions.

OUTPUT:
1) Working title
2) Draft body
3) [NEED FACT] list
4) Suggested next edit pass

## Safety

- Manual trigger only in stage-1 sketch.
- No secrets in workflow JSON.

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/writing-draft/
- Implementation: https://botshelfvampire.com/library/n8n/writing-draft/
- Registry: https://botshelfvampire.com/library/registry.json

## Implementation boundary

The supplied LLM Placeholder is a no-op node; this recipe does not yet call a model. Review the prepared system prompt for completeness, provide an input, and configure and test your own inference node before describing it as a working workflow. Importing JSON alone is not a runtime test.
