# Tiny Startups route audit

Audited: 2026-09-27 01:59 JST  
Status: **Audited / Not Submitted / Not Approved / Not Listed**  
Cost incurred: **$0 / £0**

## Decision

Use only Tiny Startups' official **Submit a Startup — Free** route if a future submission is completed. Do not select an upgrade, paid backlink, paid promotion, membership, or checkout.

For Tiny Startups, the proposed listing target is the **BotShelf Vampire Marketplace** at https://botshelfvampire.com/. The **Build Library** at https://botshelfvampire.com/library/ remains a separate implementation and evidence layer and must not be presented as the same product surface.

No account was created, no sign-in or OAuth flow was started, no form was submitted, no contact detail was transmitted, no upgrade was selected, and no payment action was taken during this audit.

## Official route

- Free submission form: https://www.tinystartups.com/submit
- Terms: https://www.tinystartups.com/terms
- Membership: https://www.tinystartups.com/membership
- Homepage: https://www.tinystartups.com/

The official form currently labels the route **Launch your startup — free** and shows a six-step flow:

1. Your URL
2. Your startup
3. Revenue
4. Traffic
5. About you
6. Upgrades

The form says it reads initial product data from the submitted URL and allows corrections before completion.

## Free-route conditions

Tiny Startups' current Terms state that:

- free submissions enter a review queue;
- approval and a specific launch date are not guaranteed;
- the submitter must own the product or be authorised to promote it;
- the submission must be a real, working product rather than a placeholder, concept, or service;
- every listing is subject to discretionary review;
- rankings may not be manipulated with bots, purchased votes, or coordinated campaigns.

The homepage describes listings as hand-approved. A public search performed before this audit did not surface an existing Tiny Startups listing for “BotShelf Vampire” or “BotShelf Vampire Build Library.” This does not rule out an unpublished draft inside an account.

## Paid branches — excluded

Tiny Startups' Terms list the following paid items:

- Skip the queue: **$99**
- DR 70+ do-follow backlink: **$99**
- Four partner backlinks: **$199**
- Newsletter feature: **$199**
- SEO review article: **$99**
- Boost purchases: **$29 / $129 / $199**
- Membership: **$299/year**

The membership page separately advertises a founding price of **$299/year** and says submissions are expedited. Its public copy is internally inconsistent about renewal: one section says the 12-month payment does not renew automatically, while the FAQ says membership renews annually. The current Terms also say membership renews annually unless cancelled, that Stripe processes payments, and that purchases are final and non-refundable; rejected paid listings receive account credit rather than a cash refund.

These branches were not opened or selected. If a future free submission reaches an upgrade or checkout choice, it must remain on the zero-cost route.

## Proposed listing scope

### Listing target — Marketplace

- **Name:** BotShelf Vampire
- **URL:** https://botshelfvampire.com/
- **Category:** AI & ML or Developer Tools, whichever the live form offers and best matches the official category labels
- **One-line description:** Ready-to-use AI Teams for real jobs, with a separate Build Library that exposes implementation and evidence.
- **Core distinction:** the Marketplace contains ready-to-use product listings; the Build Library is a separate inspectable layer.

### Evidence layer — not a second listing

- Build Library: https://botshelfvampire.com/library/
- Public evidence repository: https://github.com/BotShelfVampire/botshelf-ai-team-registry
- Evidence schema: https://github.com/BotShelfVampire/botshelf-ai-team-registry/blob/main/docs/evidence-record.schema.json
- Visible failed evaluation: https://botshelfvampire.com/cross-ai/proof/research-desk-2026-09-10.html

Evidence should describe the job performed, runtime or implementation, verification state, human approval boundary, failed or unexecuted checks, and known limits. Cross-AI is one part of the product, not the entire positioning.

## Accuracy controls

Do not claim that:

- every Marketplace item or Build Library implementation is verified;
- structural CI proves AI accuracy, safety, or production readiness;
- the repository is MIT, Apache-2.0, OSI-approved, or generally “open source”;
- the Build Library is a hosted MCP server;
- one failed evaluation applies to every workflow or runtime;
- Tiny Startups has approved, published, endorsed, or scheduled BSV before an observable confirmation exists;
- Tiny Startups' public audience, newsletter, backlink, or traffic claims are independently verified.

Use **Verified**, **Untested**, **Partial**, **Blocked**, and **Unverified** only when the underlying evidence supports the exact state.

## Risk and blocker

- The final form includes an **Upgrades** step, so a nominally free route can branch into paid placement.
- Submission requires product, revenue, traffic, and founder information. Those values must be confirmed from authoritative owner records; they must not be guessed.
- Completing the form is an external representational action and may also require account authentication.
- Public search cannot detect an unpublished account draft, so the account state must be checked immediately before any future submission.

## Next safe action

If a future run has authorised account access and can verify that no unpublished duplicate exists, prepare the free form through the final review screen using the Marketplace as the product and the Build Library only as separate evidence. Stop before any paid option or checkout. Record the confirmation, listing URL, status, timestamp, and observable result only after the site returns them.
