# Tasks

## 1. Linter

- [x] 1.1 Add `long-paragraph`, `inline-list`, and `buried-sequence` to `scripts/ste-lint.py` per 006/D9 and 006/D10. Add the three ids to `RULE_IDS` and to the selftest. Add one test for each REQ-STE-004 scenario in `tests/test_ste_lint.py`, each tagged `# Covers:`. [REQ-STE-004] Verify: `python3 -m unittest tests.test_ste_lint tests.test_lint_cli -v && python3 scripts/ste-lint.py --selftest`

## 2. Skill text

- [x] 2.1 Write `references/doc-shapes.md` per 006/D5 and 006/D11. Apply 006/D1 to 006/D8 and 006/D13 in `SKILL.md`. Set the version to 0.4.0 in `SKILL.md` and `.claude-plugin/plugin.json`. Change the tests in `tests/test_skill_contract.py` for REQ-SKILL-003 to 006 and add one test for each scenario of REQ-SKILL-008 to 010. [REQ-SKILL-003] [REQ-SKILL-004] [REQ-SKILL-005] [REQ-SKILL-006] [REQ-SKILL-008] [REQ-SKILL-009] [REQ-SKILL-010] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 2800`
- [x] 2.2 Add the Write task to `README.md` and one Write example to `examples/before-after.md`. [REQ-SKILL-004] [REQ-SKILL-008] Verify: `python3 scripts/lint.py README.md && python3 -m unittest tests.test_skill_contract -v`

## 3. Record

- [x] 3.1 Write `docs/verification/006.md`. Full gate. [REQ-SKILL-009] [REQ-STE-004] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `npx -y @fission-ai/openspec@latest archive 006-reader-first -y`, then `specctx build`.
