# Proposal

## Why

Change 012 pinned OpenSpec 2.0.0. The OpenSpec skills in this repository came from OpenSpec 1.15.0. The owner chose on 2026-11-12 to refresh them with the pinned version.

- Each skill records `generatedBy: "1.15.0"`. No test finds a skill that is older than the pin.
- OpenSpec 2.0 installs skills only. The six `/opsx` commands are from 1.15.0.

## What Changes

- `bash scripts/openspec.sh update` writes the six OpenSpec skills into `.agents/skills/` with `generatedBy: "2.0.0"`.
- Each folder `.claude/skills/openspec-*` becomes a symlink to the same folder in `.agents/skills/`. One copy of each skill stays.
- The six commands in `.claude/commands/opsx/` go.
- `docs/CONTRIBUTING.md` names `bash scripts/openspec.sh update` in the upgrade of OpenSpec.
- A new requirement, REQ-SKILL-015, ties the skills to the pin.

## Capabilities

### Modified Capabilities
- `skill-contract`: the OpenSpec skills come from the pinned version.

## Impact

- `.agents/skills/openspec-*`, `.agents/skills/.openspec-target`, `.claude/skills/openspec-*`, `.claude/commands/opsx/`.
- `docs/CONTRIBUTING.md`, `tests/test_engine_pin.py`.
- No change in `SKILL.md`, `references/`, the linters, `evals/`, or `README.md`. The release archive leaves out `.claude/` and `.agents/`.
