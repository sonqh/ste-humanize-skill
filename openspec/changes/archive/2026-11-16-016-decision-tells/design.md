# Design

## Context

`references/ai-tells.md` holds 26 patterns in groups A to F. `scripts/tells-lint.py` checks nine hard rules and six advisory rules. REQ-TELLS-002 names the six advisory rules. `SKILL.md` has 1894 words and routes to `references/ai-tells.md` with "the 26 patterns with examples". The page guides and `references/review.md` say what a decision page must answer. They do not name the habits of a model that writes one.

## Goals / Non-Goals

**Goals:**
- A writer and a reviewer can name the tells of a decision page and fix them.
- The linter points at the tells that a phrase can show.
- No file that passes the gate today fails it after this change.

**Non-Goals:**
- No hard rule. The phrases also occur in honest text.
- No check of the structure of the argument, such as the count of pros and cons for each option.
- No change in `scripts/ste-lint.py`.

## Decisions

- 016/D1 `references/ai-tells.md` gains `## G. Decision pages` with six patterns. The patterns are:
  - 27 false balance
  - 28 matched pros and cons
  - 29 straw options
  - 30 quality words with no number
  - 31 empty mitigation
  - 32 a decision with no actor

  Each pattern has the same form as patterns 1 to 26. Refs: REQ-SKILL-020
- 016/D2 Pattern 28 is *weak alone*. Two options can have three pros each by chance. Pattern 29 names an option that the material does not give. The option to do nothing is never a straw option. Refs: REQ-SKILL-020
- 016/D3 The linter checks patterns 27, 30, 31, and 32 with four advisory rules. Patterns 28 and 29 need judgement and stay in the reference. A hard rule was the alternative. "It depends on your needs" is fine in a how-to guide, and "reliable" is fine in a sentence that gives the uptime. A hard rule would fail such text. Refs: REQ-TELLS-002, REQ-TELLS-004
- 016/D4 `false-balance` matches phrases that avoid a choice. Examples are "both options have their merits", "each approach has its trade-offs", and "it depends on your needs". Others are "there is no one-size-fits-all", "no silver bullet", and "the right choice depends on". Refs: REQ-TELLS-004
- 016/D5 `actorless-decision` matches "it was decided", "it has been decided", "a decision was made", and "it is recommended that" with its forms "proposed", "suggested", and "advised". Refs: REQ-TELLS-004
- 016/D6 `empty-mitigation` matches "monitor closely", "closely monitor", "careful planning", "carefully consider", "ensure proper", "thorough testing", and "follow best practices". Each one names care and no action. Refs: REQ-TELLS-004
- 016/D7 `unmeasured-quality` matches scalable, scalability, performant, future-proof, flexible, maintainable, reliable, efficient, battle-tested, enterprise-grade, production-ready, and best-in-class. It fires only when the sentence has no digit. A sentence ends at a period, a question mark, an exclamation mark, or a new line. Two words of pattern 12 that also describe quality stay with `stock-word`, a hard rule. Refs: REQ-TELLS-004
- 016/D8 `references/human.md` adds the group to its list of tells. `references/page-guides.md` tells the writer of an ADR, a proposal, or a design doc to read the group. Step 7 of `references/review.md` tells the reviewer to check it. `SKILL.md` changes "26" to "32" and gains no word. Refs: REQ-SKILL-020
- 016/D9 One eval fixture, `rewrite-decision-tells`, gives a proposal with all six tells. A Rewrite must keep each fact and remove each tell. It runs three times with version 0.8.0 and three times with version 0.9.0. Refs: REQ-SKILL-020
- 016/D10 In the first run, 1 run of 0.9.0 quoted "monitor closely" in the text to say that it names no action. Pattern 31 now says what a Rewrite does when the source names no action. It writes `TBD` with the owner and names the phrase on the `Cut candidates:` line. The 3 runs of 0.9.0 ran again. Refs: REQ-SKILL-020

## Risks / Trade-offs

- `unmeasured-quality` can fire on a sentence that gives its number in the next sentence. It is advisory, so the writer decides.
- A Write of a decision page reads about 600 words more in `references/ai-tells.md`, when the agent opens that file.
- The phrase lists cover English only. `references/terms.md` already says that a tell in another language is the same tell.
