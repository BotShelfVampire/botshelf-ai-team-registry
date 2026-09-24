# BotShelf Vampire Build Library — Directory Listing Kit

Updated: 2026-09-25

Use this kit for free directory and editorial submissions that describe the **Build Library / AI Team Registry**. The **Marketplace is a separate product surface** and must not be merged into the same listing unless a directory explicitly supports multiple product surfaces.

## Canonical identity

- **Product name:** BotShelf Vampire Build Library
- **Primary product URL:** https://botshelfvampire.com/library/
- **Public evidence repository:** https://github.com/BotShelfVampire/botshelf-ai-team-registry
- **Suggested categories:** Developer tools; AI workflow library; local/self-hosted AI; agent evaluation; evidence tooling
- **Suggested tags:** AI workflows, AI teams, agent evaluation, developer tools, local AI, self-hosted AI, evidence
- **Availability:** Publicly inspectable Build Library, subject to the repository's custom free-use-at-own-risk license. Marketplace availability and pricing are separate.
- **License wording:** Use “custom free-use-at-own-risk license.” Do not label the repository “open source” or “OSI-approved.”

## Reusable descriptions

### One line

Inspect and adapt AI Team workflows by job, runtime, verification state, approval boundary, and failure evidence.

### Short

A public Build Library for inspecting AI Team workflows by job, runtime, implementation, verification state, human approval boundary, and failure evidence.

### Medium

BotShelf Vampire Build Library organizes AI Team implementations by the job performed and the runtime used. Each evidence record can expose the implementation, verification state, human approval boundary, visible failures, known limitations, and produced artifacts. Marketplace listings remain separate from this inspectable Build Library.

### Full

BotShelf Vampire Build Library is an implementation and evidence layer for AI Teams. It helps developers inspect and adapt workflows by the job performed and the runtime used, while keeping implementation details and evaluation state visible.

Evidence records can distinguish Verified, Untested, Partial, Blocked, and Unverified states; record human approval boundaries; preserve failed or unexecuted checks; state known limitations; and link to produced artifacts. A public JSON Schema and CI validate record structure, but structural validity does not prove that an AI result is correct, safe, or production-ready.

The Build Library is distinct from the BotShelf Vampire Marketplace. Marketplace listings are ready-to-use product offers; the Build Library contains inspectable local or self-hosted foundations and evidence organized by job and runtime.

## Key distinctions

- **Job first:** records begin with the work performed, not a generic agent label.
- **Runtime-specific:** implementations identify the actual runtime or execution context when known.
- **Verification is explicit:** Verified, Untested, Partial, Blocked, and Unverified are not interchangeable.
- **Human approval boundaries are visible:** records state where a person must review or approve.
- **Failure evidence is retained:** failed and unexecuted checks remain part of the evidence.
- **Marketplace stays separate:** do not present Build Library records as Marketplace products.

## Primary evidence links

- Evidence-record JSON Schema: https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/docs/evidence-record.schema.json
- Partial artifact-gate example: https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/examples/evidence-record.artifact-gate.json
- Blocked Research Desk evaluation (0 / 9 accepted): https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/examples/evidence-record.research-desk-2026-09-10.json
- Original public Research Desk evaluation: https://botshelfvampire.com/cross-ai/proof/research-desk-2026-09-10.html
- Public validation workflow: https://github.com/BotShelfVampire/botshelf-ai-team-registry/actions/workflows/validate-evidence.yml
- Machine-readable CodeMeta: https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/codemeta.json
- AI-readable index: https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/llms.txt
- Editorial media brief: https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/docs/media-brief.md

## Claims that are supported

- The public repository contains inspectable implementation and evidence materials.
- A machine-readable evidence-record schema is public.
- The repository retains a visible failed evaluation rather than presenting it as a success.
- Public CI checks the structure of the schema, evidence records, CodeMeta, and license references.
- Marketplace and Build Library are separate product surfaces.

## Claims not to make

- Do not say every team or implementation is verified.
- Do not say schema or CI validity proves accuracy, safety, or production readiness.
- Do not generalize one “0 / 9 accepted” evaluation to every BSV workflow.
- Do not call a prompt or single workflow “multi-agent” without implementation evidence.
- Do not call the repository open source or OSI-approved.
- Do not describe the registry as an MCP server, hosted deployment, or autonomous service unless that exact capability is independently verified.
- Do not claim a directory accepted, published, or endorsed BSV until a public listing or observable confirmation exists.
- Do not invent user counts, revenue, performance metrics, integrations, or customer claims.

## Route-specific link selection

- **Product directory:** use the Build Library URL, then link the repository as evidence.
- **Developer or GitHub directory:** use the repository URL and the JSON Schema.
- **Editorial submission:** use the media brief and at least one evidence record, including failure evidence when relevant.
- **AI or machine-readable directory:** use the CodeMeta file, llms.txt, and JSON Schema.
- **Marketplace directory:** submit Marketplace items separately; do not reuse this listing as a Marketplace offer.

## Asset and submission controls

Use only official, verified BSV logos, screenshots, and URLs. Do not fabricate product screens or metrics. Confirm each directory’s current free official submission route, duplication history, and fee status before submitting. This kit is a reusable source of accurate copy; its publication does **not** mean that any external directory has accepted or published BSV.
