# Handoff
change: 015-review-task
current: none
base: 2026-11-16T15:11:19.404Z
as_of: none
done:
reopened:
open_questions:
resolved:
- Q3 Task 5.2 Verify runs 'gate --strict' with the default markdown globs. The defaults include *.md, so the linters read SKILL.md (10 hard findings, it quotes forbidden patterns) and README.md (8 hard, before/after examples). CLAUDE.md says to skip SKILL.md and references/. Proposed fix: change the Verify to add --markdown "CLAUDE.md AGENTS.md decisions/*.md openspec/**/*.md docs/**/*.md" (what ci-local.sh and the hooks use). Edit tasks.md Verify of 5.2 yourself, or tell me to. (task none, 2026-10-24) answer: Verify edited, README exempt
- Q4 plan ready for 011-spec-ctx-upgrade. Approve to start the tasks? (task 011-spec-ctx-upgrade, 2026-11-12) answer: Approved by the owner on 2026-11-12 in the session
- Q5 archive 011-spec-ctx-upgrade? (task 011-spec-ctx-upgrade, 2026-11-12) answer: Owner merged PR #11 and asked to run the archive on 2026-11-12
- Q6 plan ready for 012-openspec-pin. Approve to start the tasks? (task 012-openspec-pin, 2026-11-12) answer: Owner approved the fix plan for the risks of 011 on 2026-11-12: ok dong y tat ca
- Q7 archive 012-openspec-pin? (task 012-openspec-pin, 2026-11-12) answer: Owner merged PR #13 and asked to continue with the archive on 2026-11-12
- Q8 plan ready for 013-openspec-skills. Approve to start the tasks? (task 013-openspec-skills, 2026-11-12) answer: Owner chose 'Do 013 as tested' on 2026-11-12
- Q9 archive 013-openspec-skills? (task 013-openspec-skills, 2026-11-12) answer: Owner approved archive of 013 on 2026-11-16.
- Q10 plan ready for 014-pre-dev-docs. Approve to start the tasks? (task 014-pre-dev-docs, 2026-11-16) answer: Owner approved plan 014 on 2026-11-16.
- Q11 archive 014-pre-dev-docs? (task 014-pre-dev-docs, 2026-11-16) answer: Owner approved archive of 014 on 2026-11-16.
- Q12 plan ready for 015-review-task. Approve to start the tasks? (task 015-review-task, 2026-11-16) answer: Owner approved plan 015 on 2026-11-16.
- and 2 more in .ctx/questions.json
next: 015/1.1  Apply 015/D9 in `evals/eval.py`. Add a test for SCN-EVAL-005-1 in `tests/test_eval.py`.
evidence: 0 task(s), 0 command, 0 manual
