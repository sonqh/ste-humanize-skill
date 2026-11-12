# Design

## Context

A trial of `openspec update` with 2.0.0 ran on a worktree of `main` on 2026-11-12. It changed 19 files. The skills got small text edits and `generatedBy: "2.0.0"`. The six `/opsx` commands went. The six folders `.claude/skills/openspec-*` became symlinks. The skills still call a bare `openspec`. The owner saw these results and chose to apply them as they are.

## Goals / Non-Goals

**Goals:**
- The OpenSpec skills come from the pinned version.
- A test fails when the skills and the pin differ.

**Non-Goals:**
- No edit of a file that OpenSpec writes. The next `openspec update` would undo it.
- No new workflow from `openspec config profile`.

## Decisions

- 013/D1 Apply the output of `openspec update` with no edit. Refs: REQ-SKILL-015
- 013/D2 Keep the symlinks. OpenSpec 2.0 keeps one copy of a skill in `.agents/skills/` and links the tool folders to it. A copy in place of a link would differ from what the next `openspec update` writes. Refs: REQ-SKILL-015
- 013/D3 A test compares `generatedBy` of each OpenSpec skill with `OPENSPEC_VERSION`. A rise of the pin with no `openspec update` then fails the tests. Refs: REQ-SKILL-015
- 013/D4 The text that forbids `/opsx:apply` stays in `openspec/config.yaml` and in the `specctx-run` skill. spec-ctx writes both. The rule is still true with no command. Refs: REQ-SKILL-015

## Risks / Trade-offs

- `/opsx:apply` and the five other commands are gone. A person who typed them uses the skills by name.
- A clone with `core.symlinks=false`, the default of Git for Windows, gets a text file in place of each link. Claude Code on that clone does not find the six OpenSpec skills in `.claude/skills/`. The copies in `.agents/skills/` stay.
- The skills still call a bare `openspec`. The line in `.claude/CLAUDE.md` says that `openspec` means `bash scripts/openspec.sh`.
