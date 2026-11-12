# Tasks

## 1. Skills

- [x] 1.1 Run `bash scripts/openspec.sh update` per 013/D1 and 013/D2. Add one test for each REQ-SKILL-015 scenario to `tests/test_engine_pin.py` per 013/D3. [REQ-SKILL-015] Verify: `python3 -m unittest tests.test_engine_pin -v && test -L .claude/skills/openspec-propose && test ! -e .claude/commands/opsx`

## 2. Record

- [x] 2.1 Name `bash scripts/openspec.sh update` in the upgrade section of `docs/CONTRIBUTING.md`. Write `docs/verification/013.md`. Full gate. [REQ-SKILL-015] Verify: `python3 scripts/lint.py docs/CONTRIBUTING.md docs/verification/013.md && grep -q "openspec.sh update" docs/CONTRIBUTING.md && bash scripts/ci-local.sh && bash scripts/openspec.sh validate --all --strict`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `bash scripts/openspec.sh archive 013-openspec-skills -y`, then `bash scripts/specctx.sh build`.
