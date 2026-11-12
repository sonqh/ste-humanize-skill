# Tasks

## 1. Engine

- [x] 1.1 Set the pin to 0.6.0 in `scripts/specctx.sh` per 011/D1. Add `[gate] markdown` and `[cli] run` to `spec-ctx.toml` per 011/D3 and 011/D4, and keep every custom value. Fix the globs of `.githooks/pre-commit` per 011/D5. Add `.ctx/current.json` to `.gitignore`. Write `tests/test_engine_pin.py` with one test for each REQ-SKILL-013 scenario. [REQ-SKILL-013] Verify: `python3 -m unittest tests.test_engine_pin -v && test "$(bash scripts/specctx.sh --version)" = 0.6.0`
- [x] 1.2 Run `bash scripts/specctx.sh init --skills --force` per 011/D2. Both skill folders then hold `specctx-run` and the three aliases. [REQ-SKILL-013] Verify: `test -f .claude/skills/specctx-run/SKILL.md && diff -r .claude/skills/specctx-run .agents/skills/specctx-run && grep -q specctx-run .claude/skills/specctx-bootstrap/SKILL.md`

## 2. Record

- [x] 2.1 Change the workflow text of `.claude/CLAUDE.md` and `docs/CONTRIBUTING.md` per 011/D2. Run each command they name once. [REQ-SKILL-013] Verify: `python3 scripts/lint.py .claude/CLAUDE.md docs/CONTRIBUTING.md && grep -q specctx-run .claude/CLAUDE.md && ! grep -q "repository is private" docs/CONTRIBUTING.md`
- [x] 2.2 Write `docs/verification/011.md`. Full gate. [REQ-SKILL-013] Verify: `bash scripts/ci-local.sh && npx -y @fission-ai/openspec@latest validate --all --strict`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `npx -y @fission-ai/openspec@latest archive 011-spec-ctx-upgrade -y`, then `bash scripts/specctx.sh build`.
