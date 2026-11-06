# Proposal

## Why

The owner asked on 2026-11-06 to make ste-humanize installable from a Claude Code plugin marketplace. Today a user needs the skills CLI or a git clone.

- Claude Code installs plugins from a marketplace with one command. A repo becomes a marketplace when it holds `.claude-plugin/marketplace.json`.
- A plugin with `SKILL.md` at its root and no `skills/` folder loads as one skill. So the repo needs no file moves, and `npx skills add` keeps working.

## What Changes

- `.claude-plugin/plugin.json` names the plugin `ste-humanize` with version 0.3.0.
- `.claude-plugin/marketplace.json` names the marketplace `sonqh` and lists the plugin with source `./`.
- The `SKILL.md` front matter version moves from 0.2.0 to 0.3.0, because change 004 changed the skill text.
- `CLAUDE.md` moves to `.claude/CLAUDE.md`. At the plugin root it fails `claude plugin validate --strict`.
- README gets the plugin install lines. CONTRIBUTING gets the release rule.

## Capabilities

### Modified Capabilities
- `skill-contract`: the plugin manifests and the version rule.

## Impact

- `.claude-plugin/`, `SKILL.md`, `.claude/CLAUDE.md`, `AGENTS.md`, `README.md`, `docs/CONTRIBUTING.md`, `.gitattributes`, `scripts/ci-local.sh`, `.github/workflows/ci.yml`, `tests/test_skill_contract.py`.
