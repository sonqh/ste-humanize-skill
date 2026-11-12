# Proposal

## Why

This repository runs spec-ctx 0.1.1. The latest version on npm is 0.6.0. Six releases came out between them.

- The skills `specctx-bootstrap`, `specctx-next`, and `specctx-done` are copies from 0.1.1. Version 0.6.0 ships `specctx-run` as the one skill and keeps the three names as aliases.
- Since 0.2.0, a plain `specctx gate --strict` lints no markdown unless `spec-ctx.toml` names the globs. `docs/CONTRIBUTING.md` names that command.
- No requirement names the one file that holds the version. A second pin can drift from the first and nothing fails.

## What Changes

- `scripts/specctx.sh` pins 0.6.0.
- `spec-ctx.toml` gains `[gate] markdown` and `[cli] run`. Every custom value stays.
- `specctx-run` is the entry point of the workflow. The three old skills become the aliases that 0.6.0 ships.
- The pre-commit hook lints `.claude/CLAUDE.md`, the path since change 005.
- `.claude/CLAUDE.md` and `docs/CONTRIBUTING.md` name the new workflow.
- A new requirement, REQ-SKILL-013, keeps one pin and one list of markdown globs.

## Capabilities

### Modified Capabilities
- `skill-contract`: one pin of the spec engine and one list of markdown globs.

## Impact

- `scripts/specctx.sh`, `spec-ctx.toml`, `.githooks/pre-commit`, `.gitignore`.
- `.claude/skills/specctx-*`, `.agents/skills/specctx-*`.
- `.claude/CLAUDE.md`, `docs/CONTRIBUTING.md`, `tests/test_engine_pin.py`.
- `.ctx/`: a new `questions.json`. The evidence of changes 001 to 010 stays.
- No change in `SKILL.md`, `references/`, the linters, `evals/`, or `README.md`.
