# Proposal

## Why

`SKILL.md` has 2795 words after change 006. An agent reads all of it for every task. The owner asked on 2026-11-11 for a shorter file, because a long file can make an agent miss a rule.

- An agent that rewrites one error message in Strict mode reads the voice rules, the audience fit rules, and the page shapes. None of them apply.
- The exceptions for Strict mode sit in six sections. An agent must join them.
- The STE rules appear two times: in `SKILL.md` and in `references/ste-rules.md`.
- No test shows what an agent writes with the skill. Change 006 left that open.

## What Changes

- `SKILL.md` keeps the rules for every text. A table `## What to read` names the file for each case.
- `references/human.md` is new. It holds the voice rules, the audience fit rules, the AI tell groups, and the table of conflicts.
- `references/terms.md` is new. It holds the rules for technical terms and other languages.
- The STE rules in `SKILL.md` become one line each. The examples move to `references/ste-rules.md`.
- The word cap of `SKILL.md` falls from 2800 to 1900. The version rises to 0.5.0.
- `evals/` is new. It holds six fixtures and a scorer with no model call. A runner writes one output for each fixture, and the scorer checks it.

## Capabilities

### New Capabilities
- `eval`: the fixtures and the scorer for text that an agent wrote with the skill.

### Modified Capabilities
- `skill-contract`: the word cap, the place of the audience fit rules and the terms rules, and the route table.

## Impact

- `SKILL.md`, `references/human.md`, `references/terms.md`, `references/ste-rules.md`, `references/doc-shapes.md`.
- `evals/eval.py`, `evals/fixtures/`, `tests/test_eval.py`, `tests/test_skill_contract.py`.
- `.claude-plugin/plugin.json`, `.gitattributes`, `spec-ctx.toml`.
- No linter changes.
