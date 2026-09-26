# Dev Hunt route audit

**Status:** Audited / Not Submitted  
**Checked:** 2026-09-26 12:05 JST  
**Cost incurred:** $0

## Decision

Do not submit or pay in the current session. Dev Hunt is not an unconditional free listing route.

The current Dev Hunt source code labels a launch week as free only while that week has fewer than 15 tools. Weeks at or above that threshold are displayed as $49. If a selected free week fills before submission, the form moves the product to the nearest available free slot. Dev Hunt's pricing source describes the average wait for a free launch as six months.

A live account is required to inspect the current week inventory, existing drafts, and exact form state. No account was created, no login was completed, no form was submitted, and no checkout was opened.

## Official routes and source evidence

- Public site: https://devhunt.org/
- Login: https://devhunt.org/login
- Authenticated submission route: https://devhunt.org/account/tools/new
- Official source repository: https://github.com/MarsX-dev/devhunt
- Free-versus-paid week selector: https://github.com/MarsX-dev/devhunt/blob/main/components/ui/SelectLaunchDate/index.tsx
- Submission logic: https://github.com/MarsX-dev/devhunt/blob/main/app/account/tools/new/page.tsx
- Pricing source: https://github.com/MarsX-dev/devhunt/blob/main/app/the-story/pricing.jsx

## Terms encountered

- Launch week with fewer than 15 tools: Free
- Launch week with 15 or more tools: $49
- Queue-skip plan: $49
- Newsletter advertisement: $397
- Home-page advertisement: $497
- Home page plus newsletter: $797

The paid packages are outside the authorized no-spend scope. No purchase or negotiation was initiated.

## Duplicate and eligibility check

Indexed public search found no BotShelf Vampire listing on Dev Hunt. This does not prove that no unpublished draft exists inside an authenticated account.

If a verified free slot is later available, the proposed listing surface is the BotShelf Vampire Build Library because it provides developer-facing implementation material, runtime variants, evidence records, and public source. The Marketplace remains a separate product surface and must not be merged into the Dev Hunt listing.

## Prepared positioning

- **Name:** BotShelf Vampire Build Library
- **Website:** https://botshelfvampire.com/library/
- **Repository:** https://github.com/BotShelfVampire/botshelf-ai-team-registry
- **Slogan:** Inspectable AI team implementations for real jobs
- **Description:** BotShelf Vampire's Build Library provides prompt packs, workflow recipes, code sketches, runtime variants, and machine-readable evidence for job-focused AI teams. Evidence records distinguish Verified, Untested, Partial, and Blocked states, retain failed evaluations, and keep publishing, spending, deployment, and other consequential actions behind human approval.
- **Pricing type:** Free
- **Marketplace boundary:** The ready-to-use Marketplace at https://botshelfvampire.com/ is separate and is not the submitted developer tool.

## Claims guardrail

Allowed:

- The Build Library contains public implementation and evidence material.
- Status labels apply only to the exact implementation or run they reference.
- Failed evaluations and unexecuted checks remain visible.

Do not claim:

- The repository is OSI-approved open source.
- Every implementation is verified.
- Dev Hunt has accepted, scheduled, featured, or endorsed the project.
- A free week is currently available until confirmed in the authenticated selector.

## Submission gate

Before any submission:

1. Confirm the authorized account has no existing draft or prior submission.
2. Recheck the public catalog for a duplicate.
3. Confirm that the selected week is explicitly labeled Free in the live authenticated form.
4. Stop immediately if the week changes to $49 or any other paid path appears.
5. Verify the live categories, pricing type, images, logo, URLs, and contact identity.
6. Obtain action-time owner approval before submitting or transmitting contact details.
7. Retain the confirmation page or submission identifier.
8. Count publication only after a public Dev Hunt listing is live.
