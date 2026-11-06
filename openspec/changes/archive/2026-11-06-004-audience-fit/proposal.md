# Proposal

## Why

The owner rewrote a feature document with ste-humanize for readers who do not know the codebase. The result kept file names, function names, and a code map. Those details made the page harder to read and did not help the reader understand the feature. The owner asked for an audience fit rule on 2026-11-06.

- Human mode has no rule that asks who reads the text before it decides which details to keep.
- The technical terms section lists file names among the terms that always stay. A rewrite then keeps every source-level name.
- Precedence item 1 says every fact survives. So the skill cannot drop a file name the reader does not need.
- "One idea per bullet" splits one event over several bullets.

## What Changes

- A section `## Audience fit` for Human mode, after `## Voice`.
- Precedence item 1 keeps every fact the reader needs and every condition, exception, qualifier, and hedge. It allows audience fit to drop a source-level detail.
- The technical terms rule protects an identifier that stays from translation and paraphrase. Audience fit decides whether it stays. Strict mode keeps every identifier.
- Bullets group the sentences of one event. Independent rules get separate bullets.
- Process step 1 names the reader. File mode allows audience fit removals and lists them.
- Boundaries allow an explanation of behavior verified in the source code, with a link to it.
- The word cap of `SKILL.md` rises from 2000 to 2400.

## Capabilities

### Modified Capabilities
- `skill-contract`: the word cap and the audience fit rule.

## Impact

- `SKILL.md`, `openspec/specs/skill-contract/spec.md`, `tests/test_skill_contract.py`.
