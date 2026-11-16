# Tasks

## 1. Scorer

- [ ] 1.1 Apply 014/D9 in `evals/eval.py`. Add one test for each REQ-EVAL-004 scenario in `tests/test_eval.py`. [REQ-EVAL-004] Verify: `python3 -m unittest tests.test_eval -v`

## 2. Skill text

- [ ] 2.1 Apply 014/D1 to 014/D3 and 014/D5 to 014/D7 in `references/page-guides.md` and `references/doc-shapes.md`. Add one test for each REQ-SKILL-016 and REQ-SKILL-017 scenario. Lint both files at baseline 0. [REQ-SKILL-016, REQ-SKILL-017] Verify: `python3 -m unittest tests.test_skill_contract -v`
- [ ] 2.2 Apply 014/D4 and 014/D8 in `SKILL.md`, and add the route row of REQ-SKILL-016. Set the version to 0.7.0 in `SKILL.md` and `.claude-plugin/plugin.json`. Add one test for each REQ-SKILL-018 scenario. Name the design doc in `README.md`. [REQ-SKILL-016, REQ-SKILL-018] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 1900 && python3 scripts/lint.py README.md`

## 3. Record

- [ ] 3.1 Add the fixtures `write-design-doc-no-cost` and `write-proposed-adr`. The first permits `Missing:` and forbids a cost in dollars. The second requires `Proposed` and the word `criteria`. Run each one three times with version 0.6.0 and three times with version 0.7.0. Save the outputs in `evals/runs/`. Write the scores to `docs/verification/014.md` and the notes to `docs/releases/v0.7.0.md`. Full gate. [REQ-SKILL-016, REQ-SKILL-017, REQ-SKILL-018, REQ-EVAL-004] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `bash scripts/openspec.sh archive 014-pre-dev-docs -y`, then `specctx build`.
