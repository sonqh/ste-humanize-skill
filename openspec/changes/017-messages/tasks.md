# Tasks

## 1. Scorer

- [ ] 1.1 Apply 017/D13 in `evals/eval.py`. Add a test for SCN-EVAL-006-1 and SCN-EVAL-006-2 in `tests/test_eval.py`. [REQ-EVAL-006] Verify: `python3 -m unittest tests.test_eval -v`

## 2. Skill text

- [ ] 2.1 Apply 017/D1 to 017/D10 in a new file `references/messages.md`, with the route row and the shorter `## Credits` of 017/D12 in `SKILL.md`. Add a test for SCN-SKILL-021-1, SCN-SKILL-021-2, and SCN-SKILL-021-3. [REQ-SKILL-021] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 1900`
- [ ] 2.2 Apply 017/D11 in `references/doc-shapes.md` and the trigger of 017/D12 in `SKILL.md`. Set the version to 0.10.0 in `SKILL.md` and `.claude-plugin/plugin.json`. Add a test for SCN-SKILL-021-4. Add messages to `README.md`. [REQ-SKILL-021] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 1900 && python3 scripts/lint.py README.md`

## 3. Record

- [ ] 3.1 Apply 017/D14. Add the six fixtures and run each one three times with version 0.9.0 and three times with version 0.10.0. Save the outputs in `evals/runs/`. Write the scores to `docs/verification/017.md` and the notes to `docs/releases/v0.10.0.md`. Full gate. [REQ-SKILL-021, REQ-EVAL-006] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- The README rewrite of 2026-11-17 is in the working tree, not committed. It goes in with task 2.2.
- The owner reviews the change before the archive.
- Archive with `bash scripts/openspec.sh archive 017-messages -y`, then `specctx build`.
