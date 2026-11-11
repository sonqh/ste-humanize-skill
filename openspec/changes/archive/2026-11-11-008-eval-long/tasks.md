# Tasks

## 1. Scorer and fixtures

- [x] 1.1 Add three long fixtures to `evals/fixtures/` per 008/D1 to 008/D3. Let `score` take several folders and `--only` per 008/D4 to 008/D6. Add one test for SCN-EVAL-001-3 and one for SCN-EVAL-002-5. [REQ-EVAL-001] [REQ-EVAL-002] Verify: `python3 -m unittest tests.test_eval -v && python3 evals/eval.py list`

## 2. Record

- [x] 2.1 Run the three long fixtures three times with version 0.4.0 and three times with version 0.5.0. Save the outputs in `evals/runs/`. Write the scores and the limits of the run to `docs/verification/008.md`. Write `docs/releases/v0.5.0.md`. Full gate. [REQ-EVAL-002] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- The owner reviews the change before the archive.
- Archive with `npx -y @fission-ai/openspec@latest archive 008-eval-long -y`, then `specctx build`.
