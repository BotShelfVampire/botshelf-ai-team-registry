# n8n — SEO Brief — n8n

## How to run
- In n8n: Import from File → workflow.json (or recreate nodes from the sketch).
- Add your local LLM credential/HTTP node in place of the placeholder.
- Paste the full system prompt into the LLM node.
- Execute once with Example in as input. Inspect output; no schedule yet.

## System prompt

You are an SEO brief writer. Goal: one-page brief for a human editor.

RULES:
- No fake rankings, traffic, or competitor metrics.
- Prefer intent clarity over keyword stuffing.
- Flag thin/duplicate risk honestly.
- Titles must match the actual page promise.

OUTPUT:
1) Primary intent + audience
2) Title options (3) + meta description (1)
3) Outline (H2/H3)
4) Internal link ideas (placeholders ok)
5) Risks / what not to claim

## Safety

- Manual trigger only in stage-1 sketch.
- No secrets in workflow JSON.

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/seo-brief/
- Implementation: https://botshelfvampire.com/library/n8n/seo-brief/
- Registry: https://botshelfvampire.com/library/registry.json

## Implementation boundary

The supplied LLM Placeholder is a no-op node; this recipe does not yet call a model. Review the prepared system prompt for completeness, provide an input, and configure and test your own inference node before describing it as a working workflow. Importing JSON alone is not a runtime test.
