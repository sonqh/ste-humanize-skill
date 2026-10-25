# Proposal

## Why

A product review on 2026-10-25 installed the skill and ran the linters as a stranger would. The skill itself scored well. The packaging did not.

- Two linters, two output formats, two `--json` shapes, two level vocabularies. A CI author writes two parsers. `tells-lint.py --help` has no help strings. `ste-lint.py --help` has full ones.
- The linter misses tells in the demo paragraph of the README. `not just a linter — it's a robust` passes, because the rule wants a comma or a period before `it's`. `leverages` passes, because the word list has no inflections.
- The README of this repo has 5 tells and 9 hard STE findings, because the before and after table quotes the patterns. CLAUDE.md exempts the README from the lint. So the tool fails its own front page.
- A `git clone` into `~/.claude/skills/` drags `openspec/`, `tests/`, `.ctx/`, and nine unrelated OpenSpec skills under `.claude/skills/` into the user's skills folder.
- `SKILL.md` is 2990 words and loads on every trigger. Its humanizer patterns duplicate `references/ai-tells.md`.
- No pre-commit hook, no GitHub Action, no demo. Half the README is maintainer content and stands before `Scope`.
- `tells-lint.py` with no file and empty stdin prints `0 hard finding(s)` and exits 0.

## What Changes

- One command, `scripts/lint.py`, runs both linters and prints one format: `file:line:col rule [level] match`. One `--json` shape. The two scripts stay as they are, because spec-ctx holds them as its parity oracle.
- `tells-lint.py` matches `not-x-its-y` across a dash or a colon, and `stock-word` matches the common inflections. The selftest grows with each fix. `--help` gets help strings. Empty input exits 2.
- The before and after table moves to `examples/before-after.md`, which already holds the long version. The README lints clean at baseline 0 and loses its exemption. Maintainer content moves to `docs/CONTRIBUTING.md`.
- `SKILL.md` drops the pattern list that `references/ai-tells.md` already holds and stays under 1800 words.
- `.gitattributes` marks the maintainer folders `export-ignore`, so a GitHub zip or `git archive` holds the skill only. A `.pre-commit-hooks.yaml` and an `action.yml` run `lint.py`.

Out of scope: new rules beyond the two fixes, a Vale style, an editor extension, a hosted playground, the TypeScript port in spec-ctx. That port re-records its goldens in its own change after this one lands.

## Capabilities

### New Capabilities
- `lint-cli`: the single `lint.py` entry, the hook, and the action.

### Modified Capabilities
- `tells-lint`: the two rule fixes, help strings, empty input.
- `skill-contract`: `SKILL.md` size, README order, clean lint, export-ignore.

## Impact

- `scripts/lint.py` (new), `scripts/tells-lint.py`, `SKILL.md`, `README.md`, `CLAUDE.md`, `references/ai-tells.md`, `docs/CONTRIBUTING.md`, `.gitattributes`, `.pre-commit-hooks.yaml`, `action.yml`, `tests/`.
- spec-ctx `tests/fixtures/lint-golden/` will differ for files that hold the new matches. spec-ctx handles that in a follow-up change with `SPECCTX_LINT_ORACLE`.
