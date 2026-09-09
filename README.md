# BotShelf Vampire — AI Team Registry

Public source for the **BotShelf Vampire Build Library**: prompt packs, workflow recipes, code sketches, and MCP-oriented tool guidance for local and self-hosted AI workflows.

[Browse the canonical Build Library](https://botshelfvampire.com/library/) · [Canonical team pages](https://botshelfvampire.com/library/teams/) · [Machine-readable registry](https://botshelfvampire.com/library/registry.json)

## Choose a job

| Job | Source directory | Typical input |
| --- | --- | --- |
| Research a question from sources | [Deep Research](teams/deep-research/) | Question and labeled sources |
| Review a code change | [Coding Review](teams/coding-review/) | Diff and expected behavior |
| Review documentation | [Doc Review](teams/doc-review/) | Draft and prerequisites |
| Analyze pasted data | [Data Analysis](teams/data-analysis/) | Table or CSV excerpt |
| Draft from notes | [Writing](teams/writing-draft/) | Notes and intended audience |
| Prepare a search-focused brief | [SEO Brief](teams/seo-brief/) | Keyword and page context |
| Triage a support request | [Support Triage](teams/support-triage/) | Message and escalation rules |
| Review a status update | [Monitoring](teams/monitoring/) | Status or log excerpt |
| Build a lead brief from public facts | [Lead Research](teams/lead-research/) | Public facts you provide |
| Prioritize a day | [Personal Assistant](teams/personal-assistant/) | Tasks and constraints |

## Choose an implementation

Open the team's directory, then choose the runtime you already use:

| Runtime | Materials | What to expect |
| --- | --- | --- |
| Ollama | Modelfile and prompt | Local model instructions |
| LM Studio | System prompt and local-server example | Local prompt workflow |
| Open WebUI | System prompt and knowledge notes | Instructions to adapt in your UI |
| n8n | Workflow JSON and setup notes | Recipe requiring configuration |
| CrewAI | Python sketch | Multi-agent starting point to adapt |
| LangGraph | Python graph sketch | Stateful workflow starting point |
| MCP | Prompt/tool guidance and server hints | Integration guidance; inspect the files for what is implemented |

Runtime directories are **variants of a job**, not additional distinct teams. A prompt pack is not automatically a multi-agent system, and an MCP-oriented pack is not necessarily a deployable MCP server. Current inventory and status belong in the [canonical registry](https://botshelfvampire.com/library/registry.json), rather than a fixed marketing count here.

## First run

1. Pick one job and inspect its `team.yaml`, README, and runtime files.
2. Check the prerequisites and replace example settings for your environment.
3. Start with a small, non-sensitive input whose expected result you can inspect.
4. Compare the output with that input. Record the model, runtime version, source revision, output, and any failure.
5. Keep actions that affect other people, accounts, money, or production behind the job's human approval boundary.

For a concrete local starting point, open [Deep Research for Ollama](teams/deep-research/ollama/). Its Modelfile contains the build and run commands. The system prompt asks for findings, open questions, and next checks without inventing citations.

## Verification status

Treat an implementation as **Untested unless evidence identifies the exact runtime, model, version, input, and result**. Source files and website status can differ between revisions. A website's verification badge does not automatically verify this GitHub snapshot.

A JSON parse, Python syntax check, or file-presence check is structural validation. It is not proof that a model or workflow executed correctly. Prompt instructions also do not replace permissions enforced by the runtime.

## How this fits BotShelf Vampire

| Surface | Role |
| --- | --- |
| **This GitHub repository** | Copyable source and distribution for Build Library materials |
| **[Build Library](https://botshelfvampire.com/library/)** | Canonical job and implementation pages |
| **[Ready-to-use Marketplace](https://botshelfvampire.com/)** | Separate free and paid AI team product listings |
| **[Marketplace prompt source](https://github.com/BotShelfVampire/botshelf)** | Free packs for Grok Bot, Claude Code, and ChatGPT |

Use a Library workflow, adapt it to a specific job, and document a real run before considering a Marketplace submission. Copying a runtime variant does not automatically create or publish a product.

## Layout

```text
teams/<team_id>/
  team.yaml
  README.md
  ollama/
  lm-studio/
  open-webui/
  n8n/
  crewai/
  langgraph/
  mcp/
```

## License and links

The registry uses **free-use-at-own-risk**; read the [LICENSE](LICENSE). It is not labeled MIT, Apache-2.0, or OSI-approved.

[BotShelf Vampire](https://botshelfvampire.com/) · [Build Library](https://botshelfvampire.com/library/) · [X: @botshelfvampire](https://x.com/botshelfvampire)

BotShelf Vampire is independent of the AI runtime vendors named here.
