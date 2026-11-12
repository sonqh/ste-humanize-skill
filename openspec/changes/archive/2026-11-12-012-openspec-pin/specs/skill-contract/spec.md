## ADDED Requirements

### Requirement: REQ-SKILL-014 One pin of OpenSpec and the stock schema
`scripts/openspec.sh` SHALL name the OpenSpec version in one line `OPENSPEC_VERSION=<semver>` and SHALL run `npx -y @fission-ai/openspec@$OPENSPEC_VERSION`. `[gate] openspec` in `spec-ctx.toml` SHALL run that script. No other tracked file outside the history folders SHALL name an OpenSpec version. `openspec/config.yaml` SHALL name the stock schema `spec-driven`.

#### Scenario: SCN-SKILL-014-1 One OpenSpec pin
- **WHEN** the test reads `scripts/openspec.sh` and `[gate] openspec` in `spec-ctx.toml`
- **THEN** the script holds one `OPENSPEC_VERSION` line with a semver value, its `exec` line names `@fission-ai/openspec@$OPENSPEC_VERSION`, and `[gate] openspec` is `bash scripts/openspec.sh`

#### Scenario: SCN-SKILL-014-2 No second OpenSpec pin
- **WHEN** the test reads the tracked files outside the history folders of SCN-SKILL-013-2 and outside the spec-ctx skill copies `.claude/skills/specctx-*` and `.agents/skills/specctx-*`
- **THEN** no file holds `@fission-ai/openspec@` followed by a digit or by `latest`

#### Scenario: SCN-SKILL-014-3 Stock schema
- **WHEN** the test reads `openspec/config.yaml` and the list of tracked files
- **THEN** the schema is `spec-driven`, no tracked file is under `openspec/schemas/`, and `openspec/templates/spec-driven-ids/` holds `spec.md` and `tasks.md`
