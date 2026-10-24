# Proposal

## Why

The two linters in `scripts/` are the only machine checkable part of this skill, and their rules live in code alone. A rule that changes, or a false positive that gets fixed, leaves no record beyond a commit message. The skill's own contract (two modes, the precedence order, the output format) lives in prose that nothing tests. This change writes both down as requirements with IDs. It adds a small test suite. Every rule and every contract line gets one test that names it.

This is also the first fresh install of spec-ctx on a project that never had OpenSpec. The install itself is part of what this change verifies.

## What Changes

- One requirement per linter rule class. Each names the rule IDs and their level (hard or advisory). Each scenario has one matching and one non-matching example from the selftests.
- Requirements for the CLI contract of both scripts: flags, exit codes, JSON shape, selftest.
- Requirements for the skill contract: the two modes, the precedence order, the output format.
- `tests/` with Python unittest files. Each test carries `# Covers: REQ-...` and names its scenario.
- Code tags `# REQ-...` in the two scripts next to the rule tables and the CLI entry points.

Out of scope: new rules, rule wording changes, the TypeScript port (that happens in spec-ctx 006). SKILL.md does not change.

## Capabilities

### New Capabilities
- `tells-lint`: the AI tell rules and their CLI.
- `ste-lint`: the STE rules and their CLI.
- `skill-contract`: modes, precedence, output format.

### Modified Capabilities
None.

## Impact

- New: `tests/`, `spec-ctx.toml`, `openspec/`, `decisions/retired-ids.md`, three skills under `.claude/skills` and `.agents/skills`.
- `scripts/*.py`: comment tags only. No behavior change. The selftests must pass before and after with the same counts.
