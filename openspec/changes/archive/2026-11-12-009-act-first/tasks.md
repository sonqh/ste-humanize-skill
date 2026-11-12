# Tasks

## 1. Skill text and eval

- [x] 1.1 Apply 009/D4 and 009/D5 in `SKILL.md` and 009/D2 in `references/doc-shapes.md`. Set the version to 0.5.1 in `SKILL.md` and `.claude-plugin/plugin.json`. Add the tests for SCN-SKILL-003-2 and SCN-SKILL-009-5. [REQ-SKILL-003] [REQ-SKILL-009] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 1900`
- [x] 1.2 Add `early` to `evals/eval.py` per 009/D6. Set the limits of the three long fixtures per 009/D1 and 009/D3. Add one test for each REQ-EVAL-003 scenario. [REQ-EVAL-003] Verify: `python3 -m unittest tests.test_eval -v`

## 2. Record

- [x] 2.1 Run the README fixture and the Strict fixture three times with version 0.5.1. Save the outputs in `evals/runs/`. Write the scores to `docs/verification/009.md`. Full gate. [REQ-EVAL-003] [REQ-SKILL-003] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `npx -y @fission-ai/openspec@latest archive 009-act-first -y`, then `specctx build`.
