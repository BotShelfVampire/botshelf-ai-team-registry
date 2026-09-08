# botshelf-ai-team-registry

Public source/distribution mirror of the BotShelf Build Library **canonical AI Team Registry**.

- **Canonical registry (BotShelf):** https://botshelfvampire.com/library/ and https://botshelfvampire.com/library/teams/
- **Machine-readable:** https://botshelfvampire.com/library/registry.json
- **This GitHub repo:** copyable implementation files for local runtimes

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
