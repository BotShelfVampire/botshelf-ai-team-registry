# BotShelf Vampire — AI Team Registry

[![Evidence metadata validation](https://github.com/BotShelfVampire/botshelf-ai-team-registry/actions/workflows/evidence-metadata.yml/badge.svg)](https://github.com/BotShelfVampire/botshelf-ai-team-registry/actions/workflows/evidence-metadata.yml)

Public source for the **BotShelf Vampire Build Library** and its AI Team implementation/evidence layer: prompt packs, workflow recipes, code sketches, and MCP-oriented tool guidance for local and self-hosted AI workflows. Each evidence record is designed to make the job, runtime, exact implementation, verification state, human approval boundary, failures, and known limits inspectable.

[Browse the canonical Build Library](https://botshelfvampire.com/library/) · [Canonical team pages](https://botshelfvampire.com/library/teams/) · [Machine-readable registry](https://botshelfvampire.com/library/registry.json) · [AI-readable project map](llms.txt) · [CodeMeta 4.0](codemeta.json)

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

[Ollama walkthrough](docs/ollama-source-research.md) · [Run-evidence template](docs/run-evidence-template.md)

For workflows split across writer and reviewer agents, use the [exact-artifact review gate](docs/cross-agent-artifact-gate.md): copyable prompts, a dependency-free Python checker, and failure-case tests. It catches a draft changed after review; it does not authenticate reviewers or authorize publication.

## Verification status

Treat an implementation as **Untested unless evidence identifies the exact runtime, model, version, input, and result**. Source files and website status can differ between revisions. A website's verification badge does not automatically verify this GitHub snapshot.

A JSON parse, Python syntax check, or file-presence check is structural validation. It is not proof that a model or workflow executed correctly. Prompt instructions also do not replace permissions enforced by the runtime.

## What the evidence layer records

Canonical BotShelf pages are designed to make implementation claims inspectable before adoption. The [machine-readable evidence-record schema](docs/evidence-record.schema.json) defines the fields needed to pin a claim to a job, implementation, source revision, runtime, model, checks, approval boundary, failures, limits, and supporting artifacts. Schema validity makes a record easier to inspect; it does not by itself prove accuracy or safety.

The [artifact-gate evidence record](examples/evidence-record.artifact-gate.json) is a conservative machine-readable example: it is marked **Partial**, records the checks that ran, keeps unrun model and publisher checks visible, and does not promote a deterministic unit test to a verified AI workflow.

The [Research Desk failure record](examples/evidence-record.research-desk-2026-09-10.json) preserves the September 2026 result as **Blocked**: 0 of 9 answers were accepted, the observed attribution and numerical failures remain visible, and unexecuted external actions are not presented as successful.

For an evidence-first overview designed for independent editorial review, see the [public media brief](docs/media-brief.md).

For consistent directory submissions, use the [public listing kit](docs/listing-kit.md) and its [machine-readable directory manifest](docs/directory-listing.json).

For the current free Launching Next route, use the [verified submission package](docs/launching-next-submission.md). It remains **Prepared / Not Submitted** until a final duplicate, contact, fee, and approval check is completed.

For Microlaunch, use the [route audit](docs/microlaunch-route-audit.md). Paid options are verified, but the current public pages do not explicitly confirm that the Regular route is free, so the status remains **Audited / Not Submitted**.

For AlternativeTo, use the [free-queue submission package](docs/alternativeto-submission.md). The Marketplace is the listing target, the Build Library remains separate evidence, and the status is **Prepared / Not Submitted**.

For Dev Hunt, use the [free-slot route audit](docs/devhunt-route-audit.md). Weeks below the platform's capacity threshold are free, full weeks are $49, and the status is **Audited / Not Submitted**.

For SaaSHub, use the [route audit](docs/saashub-route-audit.md). The normal submission tool is officially described as free, the featured placement is $99/month, and the status is **Audited / Not Submitted**.

For StartupBase, use the [route audit](docs/startupbase-route-audit.md). The standard no-badge community queue is free with an estimated 10+ week wait; badge verification and paid tiers remain excluded, and the status is **Audited / Not Submitted**.

- **Job:** the outcome the AI Team is meant to produce.
- **Runtime and implementation:** the actual model/runtime path, required setup, and whether the material is a prompt, workflow recipe, code sketch, or tool integration.
- **Status:** **Verified** only for the exact run evidenced; otherwise **Untested**, **Partial**, **Blocked**, or **Unverified** as applicable.
- **Human approval boundary:** actions such as publishing, sending, spending, pushing, merging, or deploying remain behind an explicit human gate.
- **Failure evidence:** rejected outputs and unavailable seats remain visible instead of being converted into success claims.

Two public examples show the difference between a claim and evidence:

- [Software Team evidence](https://botshelfvampire.com/cross-ai/software-desk.html) records a partial local run, unavailable seats, and a `WAITING_ON_HUMAN` stop before push, merge, or deploy.
- [Research Desk evaluation](https://botshelfvampire.com/cross-ai/proof/research-desk-2026-09-10.html) preserves the tested configuration's failed evaluation rather than generalizing it to every model or runtime.

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
