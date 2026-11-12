# Proposal

## Why

Change 011 left two risks. The owner approved a fix for both on 2026-11-12.

- `spec-ctx.toml` has no `[gate] openspec`. The gate runs the latest OpenSpec, so a new OpenSpec release can turn the gate red with no change in this repository.
- `openspec/config.yaml` names the schema `spec-driven-ids`. spec-ctx 0.2.0 removed that schema. This repository keeps an old copy in `openspec/schemas/`, and the newer spec-ctx rules do not reach it.

## What Changes

- `scripts/openspec.sh` is new. It pins OpenSpec 2.0.0, the way `scripts/specctx.sh` pins spec-ctx.
- `[gate] openspec` in `spec-ctx.toml` runs that script.
- `openspec/config.yaml` names the stock schema `spec-driven`. `specctx init --schema` installs the ID templates into `openspec/templates/spec-driven-ids/` and merges its rules.
- The old schema folder `openspec/schemas/spec-driven-ids/` goes.
- `.claude/CLAUDE.md` and `docs/CONTRIBUTING.md` name the script.
- A new requirement, REQ-SKILL-014, keeps one pin of OpenSpec and the stock schema.

## Capabilities

### Modified Capabilities
- `skill-contract`: one pin of OpenSpec and the stock schema.

## Impact

- `scripts/openspec.sh`, `spec-ctx.toml`, `openspec/config.yaml`, `openspec/schemas/`, `openspec/templates/`, `.gitignore`.
- `.claude/CLAUDE.md`, `docs/CONTRIBUTING.md`, `tests/test_engine_pin.py`.
- No change in `SKILL.md`, `references/`, the linters, `evals/`, `README.md`, or the archived changes.
