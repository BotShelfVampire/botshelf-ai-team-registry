# Indie Hackers product route audit

**Audit timestamp:** 2026-09-29 11:56:58 JST  
**Status:** Audited / Prepared / Not Submitted  
**Cost incurred:** $0  
**Proposed subject:** BotShelf Vampire Marketplace  
**Separate supporting surface:** BotShelf Vampire Build Library

## Decision

Prepare a Marketplace product record for Indie Hackers' Products Database, but do not create an account, sign in, submit a product, publish a community post, contact the operator, or enter any payment path.

The public product database exposes an **Add Your Product** route, but that route redirects signed-out users to sign in. The signed-out pages do not state that adding a product costs exactly $0 and do not expose the complete submission form. Therefore the route remains **unverified**, not verified-free.

## Official route

- [Indie Hackers Products Database](https://www.indiehackers.com/products)
- [Add Your Product](https://www.indiehackers.com/products/new)
- [Indie Hackers Terms of Service](https://www.indiehackers.com/terms)

The Products Database describes products and side projects, includes categories such as AI, Marketplaces, Programming, Productivity, and Open Source, and exposes an Add Your Product action. The product-add URL redirects to sign-in when logged out.

The Terms require accurate account information, prohibit account sharing, prohibit crawling or scraping by manual or automated means, and prohibit background processes that interfere with the service. Any future account or submission action must therefore be performed manually by an authorized owner through the normal interface.

## Zero-cost classification

**Unverified.** The public site describes creation of a free account and shows no checkout on the signed-out product pages, but it does not explicitly confirm that adding a product costs $0. No authenticated page, trial, paid placement, contract, reservation, or checkout was opened.

## Duplicate check

Public exact-name and domain searches for `"BotShelf Vampire"` and `"botshelfvampire.com"` did not surface an Indie Hackers product or post on 2026-09-29. This is not proof that no private draft, deleted post, renamed record, or account-level history exists.

## Product separation

- **Listing subject:** BotShelf Vampire Marketplace — ready-to-use AI teams.
- **Supporting evidence:** Build Library — job-based implementation materials, runtime paths, verification states, approval boundaries, and visible failed evaluations.
- The Marketplace and Build Library must not be merged into one product record.

## Prepared fields

**Name:** BotShelf Vampire

**Tagline:** Ready-to-use AI teams with inspectable implementation evidence

**Primary URL:** https://botshelfvampire.com/

**Suggested categories:** AI; Marketplaces; Productivity

**Business model:** Free and subscription-based

**Description:**

BotShelf Vampire is a marketplace for ready-to-use AI teams organized around a specific job. Each listing is kept separate from the public Build Library, which records implementation and runtime details, verification states such as Verified or Untested, human approval boundaries, known limits, and failed evaluations. Cross-AI is one part of the product rather than the whole product.

**Supporting evidence URL:** https://botshelfvampire.com/library/

## Required pre-submission checks

1. Use only an owner-authorized account; do not share credentials or automate account creation.
2. Inspect the authenticated product form and stop immediately if any fee, trial, upgrade, contract, reservation, or negotiation appears.
3. Check authorized account history for existing products, drafts, pending reviews, deletions, or final failures.
4. Search the live public Products Database again for the exact product name and root domain.
5. Confirm the final category, business model, owner identity, revenue disclosure, and assets from current facts; do not invent metrics.
6. Keep Marketplace as the product and Build Library as separate supporting evidence.
7. Preserve a confirmation receipt or live URL and record submitted, accepted, published, declined, removed, paid-only, and no-response separately.

## Blocker and next action

**Blocker:** The authenticated form, exact $0 status, account history, owner identity, and final product fields remain unverified.

**Next action:** Keep the package prepared and unsubmitted. Reconsider only in an owner-operated manual session that confirms the live form costs exactly $0, no duplicate exists, no paid option is selected by default, and the Marketplace/Build Library separation is preserved.
