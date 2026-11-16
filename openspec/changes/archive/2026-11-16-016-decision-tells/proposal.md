# Proposal

## Why

The owner asked on 2026-11-16 for the AI tells of decision pages: an ADR, a design doc, a proposal. The 26 patterns in `references/ai-tells.md` describe the sentence. A decision page has tells of its own, at the level of the argument, and the skill does not name them.

- A model avoids a choice. It writes "Both options have their merits" or "It depends on your needs" on a page whose reader must decide.
- It gives each option the same number of pros and cons, so the comparison looks fair and says nothing.
- It adds an option that nobody proposed, only to reject it.
- It calls an option scalable, reliable, or flexible with no number.
- It answers a risk with "We will monitor closely".
- It hides who decided: "It was decided that".

The review of change 015 found some of these in eval runs by hand. Nothing in the skill or the linter names them.

## What Changes

- `references/ai-tells.md` gains `## G. Decision pages` with six patterns, 27 to 32. Each has a list to watch for, the problem, and a before and after.
- `scripts/tells-lint.py` gains four advisory rules for the patterns that a phrase can show: `false-balance`, `actorless-decision`, `empty-mitigation`, and `unmeasured-quality`. The other two patterns need judgement and stay in the reference.
- `references/human.md` names the new group. `references/page-guides.md` and `references/review.md` point to it.
- The route row in `SKILL.md` says 32 patterns.
- One eval fixture: a Rewrite of a proposal full of these tells.
- The version rises to 0.9.0.

## Capabilities

### Modified Capabilities
- `tells-lint`: four new advisory rules.
- `skill-contract`: the tells of decision pages.

## Impact

- `references/ai-tells.md`, `references/human.md`, `references/page-guides.md`, `references/review.md`, `SKILL.md`, `README.md`, `.claude-plugin/plugin.json`.
- `scripts/tells-lint.py`, `tests/test_tells_lint.py`, `tests/test_skill_contract.py`.
- `evals/fixtures/`, `evals/runs/`.
- The new rules are advisory. No file in the repository fails the gate because of them.
