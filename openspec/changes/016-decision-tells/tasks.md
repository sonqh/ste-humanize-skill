# Tasks

## 1. Linter

- [ ] 1.1 Apply 016/D3 to 016/D7 in `scripts/tells-lint.py`. Add one selftest example that matches and one that does not for each new rule. Update the test of SCN-TELLS-002-1, and add one test for each REQ-TELLS-004 scenario in `tests/test_tells_lint.py`. Lint every markdown file of the repository at baseline 0. [REQ-TELLS-002, REQ-TELLS-004] Verify: `python3 scripts/tells-lint.py --selftest && python3 -m unittest tests.test_tells_lint -v`

## 2. Skill text

- [ ] 2.1 Apply 016/D1, 016/D2, and 016/D8 in `references/ai-tells.md`, `references/human.md`, `references/page-guides.md`, `references/review.md`, and `SKILL.md`. Set the version to 0.9.0 in `SKILL.md` and `.claude-plugin/plugin.json`. Add one test for each REQ-SKILL-020 scenario. Name the tells of decision pages in `README.md`. [REQ-SKILL-020] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 1900 && python3 scripts/lint.py README.md`

## 3. Record

- [ ] 3.1 Apply 016/D9. Add the fixture `rewrite-decision-tells`. Run it three times with version 0.8.0 and three times with version 0.9.0. Save the outputs in `evals/runs/`. Write the scores to `docs/verification/016.md` and the notes to `docs/releases/v0.9.0.md`. Full gate. [REQ-SKILL-020, REQ-TELLS-004] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `bash scripts/openspec.sh archive 016-decision-tells -y`, then `specctx build`.
