## ADDED Requirements

### Requirement: REQ-SKILL-013 One pin of the spec engine
`scripts/specctx.sh` SHALL name the spec-ctx version in one line `SPECCTX_VERSION=<semver>` and SHALL run `npx -y spec-ctx@$SPECCTX_VERSION`. The hooks, `scripts/ci-local.sh`, and the CI workflow SHALL run spec-ctx through that script. No other tracked file outside the history folders SHALL name a spec-ctx version. Every gate SHALL lint one list of markdown globs.

#### Scenario: SCN-SKILL-013-1 One pin
- **WHEN** the test reads `scripts/specctx.sh`
- **THEN** it holds one `SPECCTX_VERSION` line with a semver value, and the `exec` line names `spec-ctx@$SPECCTX_VERSION`

#### Scenario: SCN-SKILL-013-2 No second pin
- **WHEN** the test reads the tracked files outside `openspec/changes/archive/`, `.ctx/evidence/`, `docs/verification/`, `docs/releases/`, and `evals/runs/`
- **THEN** only `scripts/specctx.sh` holds `spec-ctx@` and a digit, and each spec-ctx call in `.githooks/`, `scripts/ci-local.sh`, and `.github/workflows/ci.yml` goes through `scripts/specctx.sh`

#### Scenario: SCN-SKILL-013-3 One markdown list
- **WHEN** the test reads `[gate] markdown` in `spec-ctx.toml` and the markdown globs in `.githooks/pre-commit`, `scripts/ci-local.sh`, and `.github/workflows/ci.yml`
- **THEN** the four lists are equal
