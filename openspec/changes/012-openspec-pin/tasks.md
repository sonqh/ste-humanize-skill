# Tasks

## 1. Engine

- [x] 1.1 Write `scripts/openspec.sh` with the pin 2.0.0 per 012/D1 and 012/D2. Set `[gate] openspec` in `spec-ctx.toml` to `bash scripts/openspec.sh`. Name the script in the archive guidance of `openspec/config.yaml` per 012/D5. Add the tests for SCN-SKILL-014-1 and SCN-SKILL-014-2 to `tests/test_engine_pin.py`. [REQ-SKILL-014] Verify: `python3 -m unittest tests.test_engine_pin -v && test "$(bash scripts/openspec.sh --version)" = 2.0.0`
- [x] 1.2 Run `bash scripts/specctx.sh init --schema` per 012/D3. Set `schema: spec-driven` and remove the old apply item per 012/D4. Remove `openspec/schemas/spec-driven-ids/`. Add the test for SCN-SKILL-014-3. [REQ-SKILL-014] Verify: `python3 -m unittest tests.test_engine_pin -v && bash scripts/openspec.sh validate --all --strict && bash scripts/openspec.sh instructions tasks --change 012-openspec-pin | grep -q "REQ ID"`

## 2. Record

- [x] 2.1 Name `scripts/openspec.sh` in `.claude/CLAUDE.md` and `docs/CONTRIBUTING.md`. Run each command they name once. [REQ-SKILL-014] Verify: `python3 scripts/lint.py .claude/CLAUDE.md docs/CONTRIBUTING.md && grep -q scripts/openspec.sh .claude/CLAUDE.md && grep -q scripts/openspec.sh docs/CONTRIBUTING.md`
- [x] 2.2 Write `docs/verification/012.md`. Full gate. [REQ-SKILL-014] Verify: `bash scripts/ci-local.sh && bash scripts/openspec.sh validate --all --strict`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `bash scripts/openspec.sh archive 012-openspec-pin -y`, then `bash scripts/specctx.sh build`.
