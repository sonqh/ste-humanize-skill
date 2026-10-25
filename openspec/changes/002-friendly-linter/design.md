# Design

## Context

The two Python scripts are the oracle for the TypeScript port in spec-ctx. Their output format must not change here, or the port breaks for every user of spec-ctx before it can follow. So the single format lives in a wrapper, and the rule fixes are the only change inside the scripts.

## Goals / Non-Goals

**Goals:**
- One command, one output format, one JSON shape, one exit code rule.
- The demo paragraph in the README lints as the README claims.
- The README lints clean with the same rules it sells.
- A clone or a zip of the repo holds the skill, not our process.

**Non-Goals:**
- Changing the output of `tells-lint.py` or `ste-lint.py`. Only their matches change.
- Porting rules to Vale. A later decision.

## Decisions

- D1 Wrapper, not merge. `scripts/lint.py FILE... [--baseline N] [--disable rules] [--only tells|ste] [--json]` imports both scripts as modules and runs their rule tables on the same text. It prints `file:line:col rule [level] match`, sorted by file, line, column. Levels are `hard` and `advisory` for both sources. The ste-lint levels `advisory-free` and the like map to `advisory`. It exits 1 when hard findings exceed the baseline, 2 on a usage error or empty input, else 0. `--json` prints a list with one object per file: `file`, `findings`, where each finding has `rule`, `level`, `line`, `col`, `match`, `source` (`tells` or `ste`). Python 3 stdlib only.
- D2 Rule fixes in `tells-lint.py`. `not-x-its-y` accepts `,`, `.`, `:`, `;`, an em dash, an en dash, or ` - ` before `it's` or `it is`. `stock-word` matches the inflections `s`, `es`, `d`, `ed`, `ing` of each verb in the list, and the plural of each noun. Each fix adds one matching and one non-matching selftest case. Modifies REQ-TELLS-001.
- D3 `tells-lint.py` gets argparse help strings in Strict mode. Empty stdin with no file exits 2 with `no input`. Modifies REQ-TELLS-003. The human and JSON output on real input do not change.
- D4 README. The order is fixed. Title. One sentence of value. Install, with the Node 22.20 note for `npx skills add`. Use. One before and after pair of at most 6 lines that lints clean. Lint, with `lint.py` only. Scope. Credits. License. The full table moves to `examples/before-after.md`. `Develop` moves to `docs/CONTRIBUTING.md`. The `--baseline 40` sentence goes away. The README lints at baseline 0 with both scripts and `lint.py`. CLAUDE.md drops the README exemption. `SKILL.md` and `references/` keep theirs.
- D5 `SKILL.md` under 1800 words. The `## Humanizer patterns` section keeps the table and one sentence that points at `references/ai-tells.md`. The numbered patterns move there and merge with what is already there. The tests of REQ-SKILL-001 to 003 still pass.
- D6 Clean export. `.gitattributes` marks the maintainer paths as `export-ignore`. The list: `openspec/`, `tests/`, `.ctx/`, `.claude/`, `.agents/`, `.github/`, `.githooks/`, `decisions/`, `docs/`, `spec-ctx.toml`, `AGENTS.md`, `CLAUDE.md`. The README tells users that the zip from the GitHub release page holds the skill only. The git clone install stays and the README says what it brings.
- D7 Hook and action. `.pre-commit-hooks.yaml` with one hook `ste-humanize-lint` that runs `scripts/lint.py` on staged markdown. `action.yml`, composite, inputs `files` (globs) and `baseline`, runs `lint.py`. Both are thin. The repo's own CI calls the action on its markdown.

## Risks / Trade-offs

- The stock word inflections may add false positives on words like `leverage` as a noun in finance text. Accepted. The skill is for prose about software.
- spec-ctx's lint goldens drift until its follow-up change. Its CI stays green, because the goldens are recorded, not computed. The follow-up re-records with `SPECCTX_LINT_ORACLE` pointed at this repo.
- Moving the table out of the README weakens the first screen. The 6 line pair keeps one example on it.

## Open Questions

None.
