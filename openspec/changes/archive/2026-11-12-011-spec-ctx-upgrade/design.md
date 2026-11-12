# Design

## Context

The engine came in through plain commits, not through a change. The last one is `da102ad`, which pinned 0.1.1. The changelog of spec-ctx from 0.1.2 to 0.6.0 lists the changes that touch this repository. A first run of `bash scripts/ci-local.sh` with the pin at 0.6.0 passed with no fix.

## Goals / Non-Goals

**Goals:**
- Every spec-ctx command in this repository runs version 0.6.0.
- Each command that `.claude/CLAUDE.md` and `docs/CONTRIBUTING.md` name works as the text says.
- A test fails when a second pin or a second list of globs drifts.

**Non-Goals:**
- No change in the skill text, the linters, or the eval.
- No move from the local schema `spec-driven-ids` to the stock `spec-driven` schema.
- No baseline file.

## Decisions

- 011/D1 Pin 0.6.0, the latest version on npm on 2026-11-12, in one step. The gate passed on the first run, so a step through each minor version adds work and finds nothing. Refs: REQ-SKILL-013
- 011/D2 `specctx-run` is the entry point. The owner chose it on 2026-11-12. `specctx init --skills --force` writes it and the three aliases into `.claude/skills/` and `.agents/skills/`. The next upgrade is then one refresh. Refs: REQ-SKILL-013
- 011/D3 `[gate] markdown` in `spec-ctx.toml` holds the globs of `scripts/ci-local.sh`. Since 0.2.0 the default is an empty list. A plain `specctx gate --strict` then lints the same files as CI. The scripts keep their flag, and a test keeps the lists equal. Refs: REQ-SKILL-013
- 011/D4 `[cli] run` is `bash scripts/specctx.sh`. The `next:` line of `status` and `next` then prints a command that runs the pinned version in this repository. Refs: REQ-SKILL-013
- 011/D5 The pre-commit hook named `CLAUDE.md`. Change 005 moved that file to `.claude/CLAUDE.md`, so the hook linted no file there. The hook now uses the list of `scripts/ci-local.sh`. Refs: REQ-SKILL-013
- 011/D6 `.ctx/` keeps the evidence of changes 001 to 010. `check --strict` reads it with 0 findings. The first `handoff write` moves the resolved questions of `handoff.md` to `.ctx/questions.json`, which git tracks. `.ctx/current.json` goes into `.gitignore`. The run journal in `.ctx/local/` has its own `.gitignore`. Refs: REQ-SKILL-013
- 011/D7 `.github/workflows/ci.yml` stays. The action `sonqh/spec-ctx@v0` takes the same inputs and runs `bash scripts/specctx.sh`, so it uses the pin. Refs: REQ-SKILL-013

## Risks / Trade-offs

- `[gate] openspec` stays absent, so the gate runs `@fission-ai/openspec@latest`. A new OpenSpec release can break the gate with no change here.
- `openspec/config.yaml` names `spec-driven-ids`. Version 0.2.0 removed that schema from spec-ctx. The local copy in `openspec/schemas/` still works. Its rules are older than those of `specctx-run`.
- The gate prints `baseline: skipped`. A new finding on old content fails the gate with no baseline to absorb it.
