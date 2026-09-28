# Hacker News / Show HN route audit

**Audit timestamp:** 2026-09-29 06:58:09 JST  
**Status:** Audited / Prepared / Not Submitted  
**Cost incurred:** $0  
**Proposed subject:** BotShelf Vampire Build Library  
**Separate surface:** BotShelf Vampire Marketplace

## Decision

Prepare the Build Library for a possible **Show HN** submission, but do not post, create an account, log in, solicit votes, or publish AI-generated comments.

The Build Library is the better fit for Show HN because it is a technical artifact that people can inspect and try. The Marketplace remains a separate product surface and must not be presented as the same thing.

## Official route and eligibility

- Official route: [Show HN submission guidelines](https://news.ycombinator.com/showhn.html)
- General rules: [Hacker News Guidelines](https://news.ycombinator.com/newsguidelines.html)
- Submission page: [Hacker News submit](https://news.ycombinator.com/submit)

The official Show HN rules say the submission must be something the maker personally worked on, that people can try, and that the maker is available to discuss. A title must begin with `Show HN`. Landing pages, signup-only pages, newsletters, lists, and work that is not ready to try are excluded. The rules also prohibit asking friends to upvote or comment.

The general Hacker News rules say not to use the site primarily for promotion, not to solicit votes or comments, not to delete and repost, and not to post generated or AI-edited comments. The submit page requires a logged-in Hacker News account. No fee, checkout, trial, contract, reservation, or paid placement is shown for an ordinary submission.

## Zero-cost classification

**Verified free for an ordinary user submission.** The official submit route presents only login or account creation and no payment step. This classification does not mean the route is ready for automated use: it requires an authorized human account and genuine maker participation.

## Duplicate check

Public web searches for the exact phrases `"BotShelf Vampire"` and `"botshelfvampire.com"` did not surface an existing Hacker News submission on 2026-09-29. This is not proof that no prior, deleted, renamed, or account-internal submission exists. Authorized account history and a final site search must be checked immediately before any post.

## Prepared title

`Show HN: BotShelf Vampire – Evidence-first AI team workflows by job and runtime`

## Prepared submission URL

`https://botshelfvampire.com/library/`

This URL should remain directly inspectable without forcing email capture or account creation.

## Prepared maker comment

I built BotShelf Vampire's Build Library to make AI-team implementations inspectable before adoption.

It organizes workflows by the job performed and by runtime or implementation. Each evidence record can show the exact status (Verified, Untested, Partial, Blocked, or Unverified), the human approval boundary, the runtime and model used, and failures that remain unresolved.

The public repository includes an evidence-record schema, CI validation, and a blocked research-desk evaluation in which 0 of 9 answers were accepted. That failure is kept visible rather than rewritten as a success claim.

The Marketplace is a separate surface; this Show HN candidate is the Build Library and evidence layer. I would value feedback on which evidence fields are most useful before trying an AI-team workflow in a real environment.

## Required pre-post checks

1. Confirm the exact artifact still works without signup and is substantial enough for Show HN.
2. Check Hacker News public search and the authorized account's submissions for duplicates, deletions, or prior failures.
3. Confirm the poster personally worked on the project and can participate in the thread.
4. Human-review the exact title and comment; do not paste generated or AI-edited comments.
5. Confirm the route remains free and has no checkout, contract, trial, reservation, or paid promotion.
6. Do not ask anyone to vote, comment, submit, or coordinate visibility.
7. Preserve the live item URL and separately record submitted, accepted, published, declined, removed, and no-response states.

## Blocker and next action

**Blocker:** No authorized Hacker News account history, maker identity, or human availability for authentic discussion has been verified. The draft comment also cannot be posted as-is because Hacker News prohibits generated or AI-edited comments.

**Next action:** Keep the package prepared. Only an owner-authorized maker should independently rewrite the comment in their own words, perform the final duplicate and fee checks, post once through the official route, and converse without AI-generated text or vote solicitation.
