# Handoff
change: 001-lint-rules-as-specs
current: 001/2.1
base: none
as_of: 2026-10-24T03:51:35.925Z
done:
- 001/1.1
reopened:
- 001/3.1 tests edited after review (at 2026-10-24T03:55:29.199Z)
open_questions:
- Task 5.2 Verify runs 'gate --strict' with the default markdown globs. The defaults include *.md, so the linters read SKILL.md (10 hard findings, it quotes forbidden patterns) and README.md (8 hard, before/after examples). CLAUDE.md says to skip SKILL.md and references/. Proposed fix: change the Verify to add --markdown "CLAUDE.md AGENTS.md decisions/*.md openspec/**/*.md docs/**/*.md" (what ci-local.sh and the hooks use). Edit tasks.md Verify of 5.2 yourself, or tell me to. (task none, 2026-10-24)
resolved:
- REQ-TELLS-003 and SCN-TELLS-003-2 say --json prints one object with file, findings, and the hard count. The script prints a JSON list of {file, findings} objects and no hard count. Fixing the script is a behavior change. Fix the spec to match the script, or approve a script change? (task 001/2.1, 2026-10-24) answer: spec changed in 89ffb68
- SCN-SKILL-003-1 needs the word 'alone' in the SKILL.md Output format section. The section says 'the rewritten text and nothing else' and has no 'alone'. SKILL.md must not change. Change the scenario to require 'nothing else' (and Kept as-is:), or approve a SKILL.md edit? (task 001/4.1, 2026-10-24) answer: spec changed in acd94a4
next: 001/2.1  Tag `RULES` and `main()` in `scripts/tells-lint.py`. Write `tests/test_tells_lint.py` with one test per scenario of REQ-TELLS-001 to 003, each marked `# Covers:` and naming its SCN.
evidence: 1 task(s), 1 command, 0 manual
