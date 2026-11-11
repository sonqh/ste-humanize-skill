# Tasks

## 1. Skill text

- [x] 1.1 Apply 007/D1 to 007/D7 in `SKILL.md`. Write `references/human.md` and `references/terms.md`. Move the rule examples to `references/ste-rules.md`. Set the version to 0.5.0 in `SKILL.md` and `.claude-plugin/plugin.json`. Change the tests for REQ-SKILL-004 and REQ-SKILL-006 and add one test for each REQ-SKILL-011 scenario. [REQ-SKILL-004] [REQ-SKILL-006] [REQ-SKILL-011] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 1900`

## 2. Eval

- [x] 2.1 Write `evals/eval.py` and six fixtures in `evals/fixtures/` per 007/D8 to 007/D10. Add `evals/` to `.gitattributes` per 007/D11. Add the `EVAL` code to `spec-ctx.toml`. Write `tests/test_eval.py` with one test for each scenario of REQ-EVAL-001 and REQ-EVAL-002. [REQ-EVAL-001] [REQ-EVAL-002] Verify: `python3 -m unittest tests.test_eval tests.test_skill_contract -v && python3 evals/eval.py list`

## 3. Record

- [x] 3.1 Run the six fixtures with version 0.4.0 and with version 0.5.0 of the skill. Write the scores and the limits of the run to `docs/verification/007.md`. Full gate. [REQ-EVAL-002] [REQ-SKILL-011] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `npx -y @fission-ai/openspec@latest archive 007-skill-router -y`, then `specctx build`.
