# Handoff
change: 001-lint-rules-as-specs
current: 001/2.1
base: none
as_of: 2026-10-24T03:51:35.925Z
done:
- 001/1.1
reopened:
open_questions:
resolved:
- REQ-TELLS-003 and SCN-TELLS-003-2 say --json prints one object with file, findings, and the hard count. The script prints a JSON list of {file, findings} objects and no hard count. Fixing the script is a behavior change. Fix the spec to match the script, or approve a script change? (task 001/2.1, 2026-10-24) answer: spec changed in 89ffb68
next: 001/2.1  Tag `RULES` and `main()` in `scripts/tells-lint.py`. Write `tests/test_tells_lint.py` with one test per scenario of REQ-TELLS-001 to 003, each marked `# Covers:` and naming its SCN.
evidence: 1 task(s), 1 command, 0 manual
