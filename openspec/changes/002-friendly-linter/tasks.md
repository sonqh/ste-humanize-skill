# Tasks

Every Verify runs from the repo root. Write `specctx` for `bash scripts/specctx.sh`.

## 1. Linter fixes

- [x] 1.1 In `scripts/tells-lint.py`: `not-x-its-y` matches across `,`, `.`, `:`, `;`, em dash, en dash, and ` - `. `stock-word` matches verb inflections (`s`, `es`, `d`, `ed`, `ing`) and noun plurals. Add one matching and one non-matching selftest case per fix. Add argparse help strings in Strict mode. No file and empty stdin exits 2 with `no input`. Add tests for SCN-TELLS-001-4, -5, SCN-TELLS-003-4, -5. The human and JSON output on real input does not change. [REQ-TELLS-001] [REQ-TELLS-003] Verify: `python3 scripts/tells-lint.py --selftest && python3 -m unittest tests.test_tells_lint -v`
- [x] 1.2 Write `scripts/lint.py` per 002/D1. Import both scripts as modules. One format, one JSON shape, `--only`, exit codes. Write `tests/test_lint_cli.py` with one test per scenario of REQ-LINT-001 and REQ-LINT-002. [REQ-LINT-001] [REQ-LINT-002] Verify: `python3 -m unittest tests.test_lint_cli -v && python3 scripts/lint.py --help > /dev/null`
- [x] 1.3 Add `LINT` to `caps` in `spec-ctx.toml`. [REQ-LINT-001] Verify: `bash scripts/specctx.sh check --strict`

## 2. Skill and README

- [x] 2.1 Trim `SKILL.md` under 1800 words per 002/D5. Move the numbered humanizer patterns into `references/ai-tells.md` and merge with what is there. Keep the table and one pointer sentence. [REQ-SKILL-004] Verify: `test $(wc -w < SKILL.md) -lt 1800 && python3 -m unittest tests.test_skill_contract -v`
- [x] 2.2 Rewrite `README.md` per 002/D4. Move the full table to `examples/before-after.md`. Keep one pair of at most 6 lines that lints clean. Install notes Node 22.20 for `npx skills add` and says what the git clone brings. Lint section shows `lint.py` only. Move `Develop` to `docs/CONTRIBUTING.md`. Drop the `--baseline 40` sentence. Remove the README exemption from `CLAUDE.md`. [REQ-SKILL-004] Verify: `python3 scripts/lint.py README.md docs/CONTRIBUTING.md && python3 scripts/tells-lint.py README.md && python3 scripts/ste-lint.py --disable synonym-rotation README.md && test $(grep -c "^## Develop" README.md) -eq 0 && ! grep -q "README.md. is exempt" CLAUDE.md`

## 3. Distribution

- [ ] 3.1 Write `.gitattributes` with `export-ignore` per 002/D6. Add a test for SCN-SKILL-004-3 in `tests/test_skill_contract.py`. [REQ-SKILL-004] Verify: `git archive HEAD | tar -t | grep -q "^SKILL.md" && ! git archive HEAD | tar -t | grep -q "^openspec/" && python3 -m unittest tests.test_skill_contract -v`
- [ ] 3.2 Write `.pre-commit-hooks.yaml` and `action.yml` per 002/D7. Add a `lint` job to `.github/workflows/ci.yml` that uses `./` with `files: "README.md docs/**/*.md"`. Add tests for SCN-LINT-003-1 and -2. [REQ-LINT-003] Verify: `python3 -m unittest tests.test_lint_cli -v && python3 -c "import yaml" 2>/dev/null || true; grep -q "id: ste-humanize-lint" .pre-commit-hooks.yaml && grep -q "using: composite" action.yml`
- [ ] 3.3 Write `docs/verification/002.md`. Note that spec-ctx must re-record its lint goldens against this commit. Full gate. [REQ-SKILL-004] Verify: `bash scripts/ci-local.sh`

## Workflow follow-up

- Run `specctx check --strict` and `npx -y @fission-ai/openspec@latest validate --all --strict` before archive, and validate again after.
- Archive with `/opsx:archive 002-friendly-linter`, then `specctx build`.
- Open a spec-ctx change to re-record `tests/fixtures/lint-golden/` with `SPECCTX_LINT_ORACLE` at the new commit and to port the two rule fixes.
