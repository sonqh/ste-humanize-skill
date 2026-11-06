# ste-humanize-skill

A Claude Code skill that rewrites English with ASD-STE100 structure and no AI tells. The skill is `SKILL.md`. The two linters are `scripts/tells-lint.py` and `scripts/ste-lint.py`. Specs live in `openspec/`.

## First thing in every session

Run the `specctx-bootstrap` skill. The engine is [spec-ctx](https://www.npmjs.com/package/spec-ctx), called through `bash scripts/specctx.sh`, the one place that names its version. Write it as `specctx` below.

```bash
specctx status
specctx task next
specctx task start <task>
# work
specctx task done <task>
specctx handoff write
```

Tick no checkbox by hand. Do not open `openspec/specs/` by hand. Use `bundle` or `task start`.

## Rules

- Every markdown file in this repo follows the skill itself, Human mode. Lint with both scripts at baseline 0, except `SKILL.md` and `references/`, which quote the patterns they forbid.
- No behavior change in the scripts without a change in `openspec/`. The selftests must pass with the same counts.
- Tag code with its REQ: `# REQ-TELLS-001`. Tag tests: `# Covers: REQ-TELLS-001`.
- Run `bash scripts/ci-local.sh` before every push.
- Python 3 stdlib only. No dependency.
