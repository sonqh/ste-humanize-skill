# Tasks

## 1. Skill text

- [x] 1.1 Apply 004/D1 to D5 in `SKILL.md`. Raise the cap in `tests/test_skill_contract.py` to 2400 per 004/D6 and add tests for the five REQ-SKILL-006 scenarios, each tagged `# Covers:`. [REQ-SKILL-004] [REQ-SKILL-006] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 2400`
- [x] 1.2 Write `docs/verification/004.md`. Full gate. [REQ-SKILL-006] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- Archive with `npx -y @fission-ai/openspec@latest archive 004-audience-fit -y`, then `specctx build`.
