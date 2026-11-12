# ste-humanize-skill

A Claude Code skill that rewrites English with ASD-STE100 structure and no AI tells. The skill is `SKILL.md`. The two linters are `scripts/tells-lint.py` and `scripts/ste-lint.py`. Specs live in `openspec/`.

## First thing in every session

Run the `specctx-run` skill. The engine is [spec-ctx](https://www.npmjs.com/package/spec-ctx), called through `bash scripts/specctx.sh`, the one place that names its version. Write it as `specctx` below. The skills `specctx-bootstrap`, `specctx-next`, and `specctx-done` are aliases of `specctx-run`.

```bash
specctx next               # the next action and the command for it
specctx status             # the active change, the current task, the open questions
specctx task start <task>  # the context of the task
# work
specctx task done <task>   # runs Verify, writes the evidence, sets the checkbox
specctx handoff write
```

`specctx next` stops at the plan and at the archive. Only the owner approves a stop. Tick no checkbox by hand. Do not open `openspec/specs/` by hand. Use `context`, `bundle`, or `task start`.

## Rules

- Every markdown file in this repo follows the skill itself, Human mode. Lint with both scripts at baseline 0, except `SKILL.md` and `references/`, which quote the patterns they forbid.
- No behavior change in the scripts without a change in `openspec/`. The selftests must pass with the same counts.
- Tag code with its REQ: `# REQ-TELLS-001`. Tag tests: `# Covers: REQ-TELLS-001`.
- Run `bash scripts/ci-local.sh` before every push.
- Python 3 stdlib only. No dependency.
