# Before and after: the combined pass

Each example shows the input, what STE alone would produce, what the humanizer alone would produce, and what this skill produces. The last column is the target. The STE-only examples in `ste-before-after.md` show the official rules on their own.

## 1. A README paragraph (Human mode)

Input:

> Let's dive into what this tool does. It's not just a sync utility — it's a robust, seamless configuration layer that has been designed to leverage your existing setup across the various agents that have been configured, ensuring consistency and reducing friction. That is the real win.

STE only:

> This tool is a configuration layer. It uses your existing setup across the configured agents. It keeps the agents consistent. It reduces friction.

Readable, but "robust", "seamless", and "That is the real win" went away only because STE cut adjectives, and "reduces friction" is still a claim with no fact behind it.

Humanizer only:

> This tool is a configuration layer that reuses the setup you already have across the agents you configured, so they stay consistent.

Better voice, but one 25-word sentence with a subordinate clause, and "stay consistent" is still vague.

This skill:

> This tool is a configuration layer. It reads the setup you already have and writes it to each agent you configured. Each agent then reads the same rules.

Kept as-is: nothing. "Reducing friction" was dropped because the source gave no fact behind it.

## 2. An error message (Strict mode)

Input:

> Oops! An error may have occurred while processing your request due to a possible mismatch in the expected data format, which could be caused by an outdated client version. Please try again or reach out to support.

This skill:

> Your request may have failed. The cause may be a data format that does not match what the server expects. An outdated client can cause this mismatch. Check your client version. If the error continues, contact support.

Notes: "may have" stays on both claims. "Oops!" is chat residue. "Reach out to" is a phrasal verb. "Please try again" was dropped because it told the user nothing about what to change, and the source gave no reason a retry would help.

## 3. A PR description (Human mode)

Input:

> ## 🚀 Overview
>
> This PR introduces a pivotal change to the caching layer — it's not merely a refactor, it's a rethinking of how we handle invalidation. Key highlights:
>
> - **Performance:** Cache hits are significantly faster
> - **Reliability:** Stale entries are now properly handled
> - **Maintainability:** The code is cleaner and more modular
>
> Let me know if you have any questions!

This skill:

> ## Caching: invalidate by key instead of by timestamp
>
> This PR changes how the cache layer invalidates entries. Before, the layer compared a timestamp on every read. Now it drops an entry when its key changes.
>
> Cache hits no longer compare timestamps. Stale entries are removed when the key changes instead of on the next read. The invalidation logic now lives in one module, `cache/invalidate.ts`.

Kept as-is: the heading names the mechanism the author described in the diff. If the diff is not available, keep the heading "Caching changes" and ask the author what the mechanism is.

Notes: "significantly faster" was replaced with the mechanism, not a number, because the source gave no number. The bold labels carried no information. The emoji and "Let me know" are decoration and residue.

## 4. A tool description for an agent (Strict mode)

Input:

> This tool will attempt to synchronize state across the various backends that have been configured, and if a conflict is detected it may resolve it automatically depending on the strategy that has been set, or otherwise it will surface the conflict for manual review.

This skill:

> The tool tries to synchronize state across the configured backends. If it finds a conflict, it reads the configured strategy. If the strategy allows automatic resolution, the tool may resolve the conflict without a user. If the tool does not resolve the conflict, it reports the conflict for manual review.

Notes: one instruction per sentence. "May resolve" stays a hedge. No humanizer pass beyond residue, because the reader is a model.

## 5. A reply in a review thread (Human mode, pattern 26)

Input:

> Yeah, you're right, this works around the issue rather than fixing it. The real fix is in `MergeService`: when we move a child under a new parent, it should update `pipeline_id` along with `parent_id`. We can backfill the bad rows from the audit log. I checked QA: 123 past merges, only 6 rows wrong now, so the cleanup is small. Since `MergeService` is shared and not specific to this account, I'd rather open a separate ticket than widen this PR.

This skill:

> Agreed, this is a workaround. A proper fix in `MergeService` would widen this PR past its scope. It is shared code, so it needs a check of the merge flow for every account and a backfill for the 6 rows already wrong in QA.
>
> I will keep this PR account specific and open a separate ticket for the `MergeService` fix and the backfill.

Notes: the reader already knows the problem. The decision leads. The one fact they lacked (6 rows) stays. The diagnosis moves to the ticket.

## 6. Text that already complies

Input:

> Run `make test` before you push. The job takes about 4 minutes. If a test fails, read the log in `reports/`.

This skill:

> The text already complies. No changes.
