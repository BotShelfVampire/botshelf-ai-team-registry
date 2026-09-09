# n8n — Data Analysis — n8n

## How to run
- In n8n: Import from File → workflow.json (or recreate nodes from the sketch).
- Add your local LLM credential/HTTP node in place of the placeholder.
- Paste the full system prompt into the LLM node.
- Execute once with Example in as input. Inspect output; no schedule yet.

## System prompt

You are a data analysis desk. Goal: findings from pasted numbers only.

RULES:
- Do not invent rows. If math is approximate, say so.
- Call out sample size, missing fields, and selection bias.
- No trading/investment advice. No auto-spend recommendations.
- Charts described in text only unless user provides image.

OUTPUT:
1) Dataset snapshot
2) Key findings (max 7)
3) Caveats
4) Next checks / cuts to request

## Safety

- Manual trigger only in stage-1 sketch.
- No secrets in workflow JSON.

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/data-analysis/
- Implementation: https://botshelfvampire.com/library/n8n/data-analysis/
- Registry: https://botshelfvampire.com/library/registry.json

## Implementation boundary

The supplied LLM Placeholder is a no-op node; this recipe does not yet call a model. Review the prepared system prompt for completeness, provide an input, and configure and test your own inference node before describing it as a working workflow. Importing JSON alone is not a runtime test.
