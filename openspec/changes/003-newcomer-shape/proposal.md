# Proposal

## Why

Writing the spec-ctx README for a reader who knew neither OpenSpec nor spec-ctx showed three gaps in the skill. The owner approved all three on 2026-10-26.

- The skill rules sentences and words. It says nothing about the order of a page for a reader who does not know the domain. Two README drafts put the problem before the reader knew what the base product was.
- The skill has no rule for the caption of a clip or screenshot. Two demo captions repeated the command and said nothing about what the reader sees.
- A number without a scale the reader has is noise. "0.0502" and "72 of 88" went into a README for strangers. The skill does not name this.

## What Changes

- A section `## Shape: a page for a newcomer` with the order: what the base thing is, the problem, what the tool does, proof, how to try it.
- One bullet for captions under the same section.
- One line under `## Boundaries` on numbers and scale.
- The word cap of `SKILL.md` rises from 1800 to 2000.

## Capabilities

### Modified Capabilities
- `skill-contract`: the word cap and the two new rules.

## Impact

- `SKILL.md`, `openspec/specs/skill-contract/spec.md`, `tests/test_skill_contract.py`.
