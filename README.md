# botshelf-ai-team-registry

Public source/distribution mirror of the BotShelf Build Library **canonical AI Team Registry**.

BotShelf Vampire publishes a public AI Team registry covering AI agent teams, multi-agent systems, multi-agent workflows, MCP integrations, and runnable implementations across multiple AI runtimes — with BotShelf as the canonical identity and this repo as copyable source.

- **Canonical registry (BotShelf):** https://botshelfvampire.com/library/ and https://botshelfvampire.com/library/teams/
- **What is an AI Team?** https://botshelfvampire.com/library/teams/#what-is-an-ai-team
- **Machine-readable:** https://botshelfvampire.com/library/registry.json
- **This GitHub repo:** copyable implementation files for local runtimes
- **Bot Shelf marketplace source:** [botshelf](https://github.com/BotShelfVampire/botshelf)

## Terminology (short)

- **Primary term:** AI Team / AI Teams
- **Close related labels** (when the architecture fits): AI agent team, Agent Team, Multi-Agent System, Multi-Agent Workflow
- **Broader discovery concepts** (not automatic synonyms): AI Agents, Multi-Agent Orchestration, Agent Orchestration, Agentic Workflow, AI Workflow
- One canonical Team entity per job — not a landing page per synonym. No swarm terms here (these packs are not swarm architectures).

## Model (honest)

- **10 Teams** (job concepts: deep-research, coding-review, …)
- **70 implementations** (7 runtimes × 10 jobs)

Not “70 AI Teams”. Marketplace ready-to-use Team product pages on BotShelf are separate commercial entities.

## Entity note

| Surface | Role |
|--------|------|
| GitHub (`botshelf-ai-team-registry`) | Source / distribution |
| BotShelf Library | Canonical registry |
| BotShelf marketplace Teams | Commercial product pages (separate) |

## Layout

```
teams/
  <team_id>/
    team.yaml
    README.md
    ollama/ …
    lm-studio/
    open-webui/
    n8n/
    crewai/
    langgraph/
    mcp/
```

## License

`free-use-at-own-risk` — see [LICENSE](./LICENSE). Not claiming MIT/Apache SPDX.

## Status

Library implementation status is **Untested** unless a page explicitly records runtime verification. Structural checks (JSON parse, file present) are not the same as Verified runtime execution.
