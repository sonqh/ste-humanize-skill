# Contributing

Specs live in `openspec/`. The engine is spec-ctx. `scripts/specctx.sh` names its install source.

```bash
git config core.hooksPath .githooks    # turn on the hooks
python3 -m unittest discover -s tests  # run the tests
bash scripts/ci-local.sh               # run the CI steps on this machine
```

- The `pre-commit` hook runs `specctx gate --strict` and the tests.
- The `pre-push` hook runs `scripts/ci-local.sh`. `SPECCTX_SKIP_PUSH_GATE=1` skips it and says so.
- CI skips the spec-ctx job while the spec-ctx repository is private. It prints a notice. Run `scripts/ci-local.sh` instead.
- Tests use `unittest` only. They add no dependency.
- Every markdown file follows the skill itself, Human mode. Lint it with `python3 scripts/lint.py FILE`. `SKILL.md` and `references/` quote the patterns they forbid, so they are exempt.

## Eval

The eval measures what an agent writes with the skill. The scorer calls no model.

```bash
python3 evals/eval.py list                             # the fixtures
python3 evals/eval.py prompt ID --skill PATH_TO_SKILL  # the prompt for one run
python3 evals/eval.py score OUTPUTS_DIR                # read OUTPUTS_DIR/<id>.md
```

- Give each prompt to a new agent. Save its reply as `<id>.md` in one folder for each version of the skill.
- Run the eval before and after a change in `SKILL.md` or `references/`. Compare the two scores.
- `evals/runs/` holds the outputs of earlier runs.
- CI does not run the eval. It runs the tests of the scorer.

## Release

- The plugin version lives in two places: `version` in the front matter of `SKILL.md` and `version` in `.claude-plugin/plugin.json`. A test fails when they differ.
- Plugin users get an update only when this version changes. Raise it in both files when the skill text or a linter changes.
- Run `claude plugin validate --strict .` before you push a release. It checks both manifests.

