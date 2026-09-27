# Dev Resources route audit

**Audited:** 2026-09-27 JST  
**Destination:** [Dev Resources](https://devresourc.es/)  
**Status:** **Audited / Prepared / Not Submitted**  
**Cost incurred:** **$0**

## Route verified

Dev Resources describes itself in its current terms as a free, curated directory of developer resources. Its public submission path redirects to an account sign-in. The directory also links to the public `marcelscruz/dev-resources` repository, whose current contribution guide accepts resource additions in the `resources` folder through a pull request. When a contributor cannot prepare the TypeScript entry, the guide permits an issue containing the resource information.

The official free contribution route is therefore:

1. search the website, repository, open issues, and pull requests for duplicates;
2. use the signed-in submission form, or add the resource to the correct alphabetical file under `resources/`;
3. keep the description under 160 characters;
4. select no more than three existing categories;
5. use a clean HTTPS product-homepage URL with no query parameters;
6. wait for automated review and the maintainer's final decision.

No form, issue, or pull request was submitted in this audit.

## Duplicate check

Public checks found no indexed Dev Resources listing, repository entry, open issue, or pull request for either:

- `BotShelf Vampire`
- `botshelfvampire.com`

This does not prove that the account-gated submission system has no unpublished draft. A signed-in history check remains required immediately before any submission.

## Proposed listing

The proposed subject is the **Build Library**, not a Marketplace product listing.

```ts
{
    name: 'BotShelf Vampire',
    description:
        'Copyable AI-team build resources with inspectable runtime, verification status, human approval boundaries, and visible failed evaluations.',
    categories: ['AI', 'Library', 'Tooling'],
    url: 'https://botshelfvampire.com',
    keywords: [
        'ai teams',
        'ollama',
        'n8n',
        'crewai',
        'langgraph',
        'mcp',
        'prompts',
        'workflows',
        'evidence',
        'human approval',
    ],
}
```

The clean homepage URL is required by the contribution guide and currently labels the **Ready-to-use Marketplace** and **Build Library** as separate layers. The description above names only the Build Library role. Before submission, re-check that this separation remains visible and that the entry still meets the directory's “main product” rule.

## Product-fit check

The contribution guide currently requires a resource that developers use to build software, a custom domain, a clean HTTPS URL, immediate availability, and sufficient quality. The Build Library is a plausible fit because it publishes prompt packs, workflow recipes, code sketches, and runtime guidance for developer-operated AI systems.

This is a proposed fit, not acceptance. Dev Resources retains final editorial discretion.

## Paid branch excluded

The separate advertising page currently lists:

- Bronze: **$59/month**
- Silver: **$99/month**
- Gold: **$179/month**

Advertising is not required for organic acceptance and was not purchased. “Skip the queue” is also a paid service under the current terms and is excluded.

## Evidence and boundaries

A submitted description must not imply that:

- the Build Library and Marketplace are the same product surface;
- every implementation is verified;
- structural CI proves AI-output quality or safety;
- this repository is MIT-licensed or OSI-approved;
- the visible failed evaluation is a successful run.

Use these public evidence links during review:

- [Build Library](https://botshelfvampire.com/library/)
- [AI Team registry source](https://github.com/BotShelfVampire/botshelf-ai-team-registry)
- [Verification states and evidence model](https://github.com/BotShelfVampire/botshelf-ai-team-registry#verification-status)
- [Visible failed evaluation: 0 / 9 accepted](https://botshelfvampire.com/cross-ai/proof/research-desk-2026-09-10.html)

## Risk, blocker, and next action

**Risk:** The directory requires the clean product homepage, while the proposed subject is specifically the Build Library. The homepage currently separates the Build Library from the Marketplace, but an editorial reviewer may still treat the broader BotShelf Vampire site as the listed product.

**Blocker:** The official web form requires sign-in, so unpublished account drafts and exact live form fields were not observable in this run. A direct GitHub contribution would also create an external PR before that account-history check.

**Next action:** Re-open the signed-in submission history, repeat the public duplicate search, confirm the route is still free, then submit exactly once through the official form or a rule-compliant GitHub PR. Do not buy advertising or skip-the-queue placement.
