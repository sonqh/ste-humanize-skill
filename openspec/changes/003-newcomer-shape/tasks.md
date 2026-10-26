# Tasks

## 1. Skill text

- [ ] 1.1 Add the section and the Boundaries line to `SKILL.md` per 003/D1 and D2. Raise the cap in `tests/test_skill_contract.py` to 2000 and add tests for the three REQ-SKILL-005 scenarios, each tagged `# Covers:`. [REQ-SKILL-004] [REQ-SKILL-005] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 2000`
- [ ] 1.2 Write `docs/verification/003.md`. Full gate. [REQ-SKILL-004] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- Archive with `npx -y @fission-ai/openspec@latest archive 003-newcomer-shape -y`, then `specctx build`.
