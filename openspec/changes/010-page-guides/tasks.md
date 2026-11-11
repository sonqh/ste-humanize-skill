# Tasks

## 1. Skill text

- [x] 1.1 Apply 010/D1 to 010/D8 in `references/doc-shapes.md`, `references/page-guides.md`, and `SKILL.md`. Set the version to 0.6.0 in `SKILL.md` and `.claude-plugin/plugin.json`. Add one test for each REQ-SKILL-012 scenario. Name the three kinds of page in `README.md`. [REQ-SKILL-012] Verify: `python3 -m unittest tests.test_skill_contract -v && test $(wc -w < SKILL.md) -lt 1900 && python3 scripts/lint.py README.md`

## 2. Record

- [x] 2.1 Add the fixtures `write-adr-from-thread` and `long-proposal`. Run each one three times with version 0.5.1 and three times with version 0.6.0. Save the outputs in `evals/runs/`. Write the scores to `docs/verification/010.md` and the notes to `docs/releases/v0.6.0.md`. Full gate. [REQ-SKILL-012] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- This change is stacked on change 009. Merge and archive 009 first.
- The owner reviews the change before the archive.
- Archive with `npx -y @fission-ai/openspec@latest archive 010-page-guides -y`, then `specctx build`.
