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
