# Media brief: inspectable evidence for AI Teams

**Updated:** 2026-09-18  
**Product:** [BotShelf Vampire](https://botshelfvampire.com/)  
**Public source:** [AI Team Registry](https://github.com/BotShelfVampire/botshelf-ai-team-registry)

## One-sentence angle

AI-agent directories usually summarize capability claims; BotShelf Vampire is building a public implementation and evidence layer that lets a reader inspect the job, runtime, exact implementation, verification state, human approval boundary, failures, and known limits.

## What is distinct

BotShelf Vampire keeps two surfaces separate:

- The [Marketplace](https://botshelfvampire.com/) contains ready-to-use AI Team product listings.
- The [Build Library](https://botshelfvampire.com/library/) contains local and self-hosted foundations organized by job and runtime.

A runtime variant is not counted as a new team, a prompt is not automatically a multi-agent system, and source availability is not treated as proof that a workflow works.

## What a reviewer can inspect

1. **Job and implementation:** the intended outcome and the concrete runtime path, source files, prerequisites, and revision.
2. **Verification state:** an implementation remains **Untested** unless evidence identifies the exact runtime, model, version, input scope, checks, and observed result.
3. **Human approval boundary:** actions such as sending, spending, publishing, pushing, merging, or deploying stay behind an explicit approval boundary.
4. **Failures and unrun checks:** rejected outputs, blocked seats, and checks that did not run remain visible.
5. **Known limits:** deterministic checks are not promoted into claims about semantic accuracy, safety, or production reliability.

## Primary evidence

- [Machine-readable evidence schema](evidence-record.schema.json): a public format for recording the job, implementation, pinned revision, runtime and model identity, checks, approval boundary, failures, limits, and artifacts.
- [Conservative evidence-record example](../examples/evidence-record.artifact-gate.json): marked **Partial** because a deterministic 12-test checker ran, while AI-model execution and live publisher integration did not.
- [Software Team evidence](https://botshelfvampire.com/cross-ai/software-desk.html): preserves unavailable seats and a `WAITING_ON_HUMAN` stop before push, merge, or deploy.
- [Research Desk evaluation](https://botshelfvampire.com/cross-ai/proof/research-desk-2026-09-10.html): preserves a failed evaluation for the tested configuration instead of generalizing it to every model or runtime.
- [Canonical machine-readable registry](https://botshelfvampire.com/library/registry.json): current Build Library inventory and status.

## Claims this project does not make

- Schema validity does not verify task accuracy or safety.
- A JSON parse, syntax check, or file-presence check is not a successful AI workflow run.
- One passing run does not verify other models, runtimes, inputs, or revisions.
- A visible failure is evidence about the tested configuration, not proof that every configuration fails.
- Public source does not mean a workflow may act on accounts, money, or production systems without permission.

## Editorial questions worth testing

- Can an independent reviewer reproduce the stated result from the pinned revision?
- Does the evidence distinguish structural checks from semantic evaluation?
- Are failed, blocked, and unrun checks as visible as passing checks?
- Does the documented approval boundary match what the runtime actually enforces?
- Can the same job move between runtimes without changing the acceptance criteria?
- Does the Marketplace remain distinct from the implementation-focused Build Library?

## Suggested verification path

1. Open the [canonical Build Library](https://botshelfvampire.com/library/) and choose one job.
2. Inspect its source directory and runtime prerequisites.
3. Read the canonical status in the [registry JSON](https://botshelfvampire.com/library/registry.json).
4. Compare the claim with a revision-specific evidence record.
5. Check whether failures, unrun checks, limits, and approval boundaries are explicit.
6. Re-run only with non-sensitive test input and record the exact environment.

## Availability

The public repository is available for independent inspection and reproducibility review. BotShelf Vampire should be described as an implementation/evidence-layer project in progress, not as proof that every listed AI Team is verified.
