# Handoff
change: 009-act-first
current: none
base: 2026-11-11T16:00:27.227Z
as_of: 2026-11-11T16:02:33.292Z
done:
- 009/1.1
- 009/2.1
- 010/2.1
reopened:
- 009/1.1 change 010 added tests to tests/test_skill_contract.py, so the file hash changed (at 2026-11-11T16:02:18.619Z)
- 009/2.1 change 010 added tests to tests/test_skill_contract.py, so the file hash changed (at 2026-11-11T16:02:19.213Z)
open_questions:
resolved:
- REQ-TELLS-003 and SCN-TELLS-003-2 say --json prints one object with file, findings, and the hard count. The script prints a JSON list of {file, findings} objects and no hard count. Fixing the script is a behavior change. Fix the spec to match the script, or approve a script change? (task 001/2.1, 2026-10-24) answer: spec changed in 89ffb68
- SCN-SKILL-003-1 needs the word 'alone' in the SKILL.md Output format section. The section says 'the rewritten text and nothing else' and has no 'alone'. SKILL.md must not change. Change the scenario to require 'nothing else' (and Kept as-is:), or approve a SKILL.md edit? (task 001/4.1, 2026-10-24) answer: spec changed in acd94a4
- Task 5.2 Verify runs 'gate --strict' with the default markdown globs. The defaults include *.md, so the linters read SKILL.md (10 hard findings, it quotes forbidden patterns) and README.md (8 hard, before/after examples). CLAUDE.md says to skip SKILL.md and references/. Proposed fix: change the Verify to add --markdown "CLAUDE.md AGENTS.md decisions/*.md openspec/**/*.md docs/**/*.md" (what ci-local.sh and the hooks use). Edit tasks.md Verify of 5.2 yourself, or tell me to. (task none, 2026-10-24) answer: Verify edited, README exempt
next: no open task
evidence: 5 task(s), 5 command, 0 manual
