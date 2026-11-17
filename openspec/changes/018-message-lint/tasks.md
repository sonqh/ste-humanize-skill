# Tasks

## 1. Linters

- [ ] 1.1 Apply 018/D8 in `scripts/ste-lint.py`. Add selftest examples, and a test for SCN-STE-005-1, SCN-STE-005-2, and SCN-STE-005-3 in `tests/test_ste_lint.py`. [REQ-STE-005] Verify: `python3 scripts/ste-lint.py --selftest && python3 -m unittest tests.test_ste_lint -v`
- [ ] 1.2 Apply 018/D1 to 018/D7 in `scripts/tells-lint.py`. Add selftest examples. Add a test for each scenario of REQ-TELLS-005 and for SCN-TELLS-001-6 in `tests/test_tells_lint.py`, and change the sets of SCN-TELLS-001-1 and SCN-TELLS-002-1. [REQ-TELLS-001, REQ-TELLS-002, REQ-TELLS-005] Verify: `python3 scripts/tells-lint.py --selftest && python3 -m unittest tests.test_tells_lint -v`

## 2. Record

- [ ] 2.1 Apply 018/D9. Name the new rules in `references/messages.md` and `README.md`. Set the version to 0.11.0 in `SKILL.md` and `.claude-plugin/plugin.json`. Score the 017 run again. Write `docs/verification/018.md` and `docs/releases/v0.11.0.md`. Full gate. [REQ-TELLS-005, REQ-STE-005] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- This change is stacked on change 017. Merge and archive 017 first.
- The owner reviews the change before the archive.
- Archive with `bash scripts/openspec.sh archive 018-message-lint -y`, then `specctx build`.
