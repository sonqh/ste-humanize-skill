# Tasks

## 1. Scorer

- [ ] 1.1 Apply 015/D9 in `evals/eval.py`. Add a test for SCN-EVAL-005-1 in `tests/test_eval.py`. [REQ-EVAL-005] Verify: `python3 -m unittest tests.test_eval -v`

## 2. Skill text

- [ ] 2.1 Apply 015/D2 to 015/D7 in a new file `references/review.md`. Lint it at baseline 0. Add a test for SCN-SKILL-019-1, SCN-SKILL-019-2, and SCN-SKILL-019-3. [REQ-SKILL-019] Verify: `python3 -m unittest tests.test_skill_contract -v`
- [ ] 2.2 Apply 015/D1 and 015/D8 in `SKILL.md`. Set the version to 0.8.0 in `SKILL.md` and `.claude-plugin/plugin.json`. Add a test for SCN-SKILL-019-4. Add a review request to `README.md`. [REQ-SKILL-019] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 1900 && python3 scripts/lint.py README.md`

## 3. Record

- [ ] 3.1 Add the fixtures `review-design-doc-gaps` and `review-ready-adr`, and a test for SCN-EVAL-005-2. The first gives a design doc with no non-goals, no way back, and a cost with no source. The second gives an ADR that answers each question. Run each one three times with version 0.7.0 and three times with version 0.8.0. Save the outputs in `evals/runs/`. Write the scores to `docs/verification/015.md` and the notes to `docs/releases/v0.8.0.md`. Full gate. [REQ-SKILL-019, REQ-EVAL-005] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- This change is stacked on change 014. Merge and archive 014 first.
- The owner reviews the change before the archive.
- Archive with `bash scripts/openspec.sh archive 015-review-task -y`, then `specctx build`.
