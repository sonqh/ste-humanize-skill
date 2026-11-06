# Design

## Decisions

- 005/D1 The marketplace lives in this repo, with the plugin at source `./`. The marketplace name is `sonqh`, so the install line reads `ste-humanize@sonqh`. A later skill in another repo can join the same marketplace through a `github` source entry.
- 005/D2 No `skills` key and no `skills/` folder. The Claude Code docs say a plugin with `SKILL.md` at its root loads as one skill. The test install shows 1 skill, 0 agents, and 0 hooks. The maintainer skills and commands under `.claude/` do not load.
- 005/D3 The version is set, not taken from the commit. With no version, every commit counts as an update, and maintainer commits would push updates to users. The version lives in the `SKILL.md` front matter and in `plugin.json`. A test keeps the two equal.
- 005/D4 `CLAUDE.md` moves to `.claude/CLAUDE.md`, where Claude Code also reads project instructions. `AGENTS.md` imports the new path. The CI and `ci-local.sh` gate lists change with it.
- 005/D5 `.claude-plugin/` is export-ignored. The release zip holds the skill for a manual install and needs no manifest. The old `/CLAUDE.md` line is gone, because `.claude/` is already ignored.
- 005/D6 No icon. The directory takes the icon once, at the first submission, so the owner picks it.

## Risks / Trade-offs

- A version that nobody raises leaves plugin users on old text. CONTRIBUTING states the rule.
- The skill gets the namespaced name `/ste-humanize:ste-humanize`. README says so.
