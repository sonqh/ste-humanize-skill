# Proposal

## Why

The first eval run gave the same score for versions 0.4.0 and 0.5.0 of the skill: 84 of 85 checks. The run could not tell the two versions apart, for three reasons.

- The longest material had 119 words. A long text is where an agent loses a condition.
- Each fixture ran one time for each version. A difference of one check is noise.
- The checks were near their upper limit.

The owner asked on 2026-11-11 for long fixtures and three runs for each cell.

## What Changes

- Three long fixtures: a design note, the notes for a README, and a tool description. The material has 637 to 849 words. Each fixture checks 19 or more facts.
- `evals/eval.py score` takes one folder for each run. It reports each failed check as a count of runs.
- `--only IDS` scores a part of the fixtures.
- `docs/releases/v0.5.0.md` holds the notes for the first release.

## Capabilities

### Modified Capabilities
- `eval`: the long fixtures, and a score over several runs.

## Impact

- `evals/eval.py`, `evals/fixtures/`, `evals/runs/`, `tests/test_eval.py`.
- `docs/CONTRIBUTING.md`, `docs/releases/v0.5.0.md`.
- No change in `SKILL.md`, `references/`, or the linters.
