# Tasks

## 1. Install check

- [x] 1.1 Confirm the fresh install: `spec-ctx.toml` with the three codes, the three skills in both skill folders, `openspec/config.yaml` with schema `spec-driven-ids`. Record the exact commands in `docs/verification/001.md`. [REQ-SKILL-001] Verify: `test -d .claude/skills/specctx-bootstrap && test -d .agents/skills/specctx-done && grep -q spec-driven-ids openspec/config.yaml`

## 2. tells-lint

- [x] 2.1 Tag `RULES` and `main()` in `scripts/tells-lint.py`. Write `tests/test_tells_lint.py` with one test per scenario of REQ-TELLS-001 to 003, each marked `# Covers:` and naming its SCN. [REQ-TELLS-001, REQ-TELLS-002, REQ-TELLS-003] Verify: `python3 -m unittest tests.test_tells_lint -v`

## 3. ste-lint

- [x] 3.1 Write `tests/ste_rules.json` from the current `RULES` table. Tag `RULES` and `main()` in `scripts/ste-lint.py`. Write `tests/test_ste_lint.py` for REQ-STE-001 to 003. [REQ-STE-001, REQ-STE-002, REQ-STE-003] Verify: `python3 -m unittest tests.test_ste_lint -v`

## 4. Skill contract

- [ ] 4.1 Write `tests/test_skill_contract.py` for REQ-SKILL-001 to 003. Tag nothing in SKILL.md. [REQ-SKILL-001, REQ-SKILL-002, REQ-SKILL-003] Verify: `python3 -m unittest tests.test_skill_contract -v`

## 5. Close

- [ ] 5.1 Add `.githooks/pre-commit` and `.githooks/pre-push` that run `specctx gate --strict` and the unittest suite, a `scripts/ci-local.sh`, and a CI workflow that calls the spec-ctx action when the repo is reachable. README gains a `Develop` section. Both selftests print the same counts as before this change. [REQ-TELLS-003, REQ-STE-003] Verify: `bash scripts/ci-local.sh`
- [ ] 5.2 Write `docs/verification/001.md`. Run the gate. [REQ-SKILL-001] Verify: `npx -y github:sonqh/spec-ctx#997ea1979506 gate --strict && npx -y @fission-ai/openspec@latest validate --all --strict`

## Workflow follow-up

- Archive with `/opsx:archive 001-lint-rules-as-specs`, then `specctx build`.
