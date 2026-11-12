# Contributing

Specs live in `openspec/`. The engine is spec-ctx. `scripts/specctx.sh` names its install source.

```bash
git config core.hooksPath .githooks    # turn on the hooks
python3 -m unittest discover -s tests  # run the tests
bash scripts/ci-local.sh               # run the CI steps on this machine
```

- The `pre-commit` hook runs `specctx gate --strict` and the tests.
- The `pre-push` hook runs `scripts/ci-local.sh`. `SPECCTX_SKIP_PUSH_GATE=1` skips it and says so.
- `[gate] markdown` in `spec-ctx.toml` names the files that the gate lints. The hooks, `scripts/ci-local.sh`, and CI pass the same list. A test fails when the lists differ.
- The CI job `specs` runs the action `sonqh/spec-ctx@v0` with `bash scripts/specctx.sh`, so it uses the same version.
- Tests use `unittest` only. They add no dependency.
- Every markdown file follows the skill itself, Human mode. Lint it with `python3 scripts/lint.py FILE`. `SKILL.md` and `references/` quote the patterns they forbid, so they are exempt.

## Eval

The eval measures what an agent writes with the skill. The scorer calls no model.

```bash
python3 evals/eval.py list                             # the fixtures
python3 evals/eval.py prompt ID --skill PATH_TO_SKILL  # the prompt for one run
python3 evals/eval.py score OUTPUTS_DIR                # read OUTPUTS_DIR/<id>.md
python3 evals/eval.py score RUN1 RUN2 RUN3 --only IDS  # several runs, some fixtures
```

- Give each prompt to a new agent. Save its reply as `<id>.md` in one folder for each version of the skill.
- Run the eval before and after a change in `SKILL.md` or `references/`. Compare the two scores.
- Run a fixture three times or more. With several run folders, the report shows each failed check with the count of runs where it failed.
- `evals/runs/` holds the outputs of earlier runs.
- CI does not run the eval. It runs the tests of the scorer.

## Upgrade spec-ctx

Do the upgrade in an OpenSpec change. Change 011 is the model.

1. Read the spec-ctx changelog from your version to the new one.
2. Set `SPECCTX_VERSION` in `scripts/specctx.sh`. No other file names the version.
3. Run `bash scripts/ci-local.sh`. Record each failure and each new warning before you fix one.
4. Run `bash scripts/specctx.sh init --skills --force`. It writes the skills into `.claude/skills/` and `.agents/skills/` and keeps `spec-ctx.toml`.
5. Run `bash scripts/specctx.sh status` and `bash scripts/specctx.sh next`.

To roll back, set `SPECCTX_VERSION` to the old version.

## Release

- The plugin version lives in two places: `version` in the front matter of `SKILL.md` and `version` in `.claude-plugin/plugin.json`. A test fails when they differ.
- Plugin users get an update only when this version changes. Raise it in both files when the skill text or a linter changes.
- Run `claude plugin validate --strict .` before you push a release. It checks both manifests.

