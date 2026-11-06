# Tasks

## 1. Plugin

- [x] 1.1 Add both manifests, move `CLAUDE.md`, raise the versions, and update the gate lists per 005/D1 to D5. Add tests for the three REQ-SKILL-007 scenarios, each tagged `# Covers:`. [REQ-SKILL-007] Verify: `python3 -m unittest tests.test_skill_contract -v`
- [x] 1.2 Add the install lines to `README.md` and the release rule to `docs/CONTRIBUTING.md`. Write `docs/verification/005.md`. Full gate. [REQ-SKILL-007] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- Archive with `npx -y @fission-ai/openspec@latest archive 005-plugin-marketplace -y`, then `specctx build`.
