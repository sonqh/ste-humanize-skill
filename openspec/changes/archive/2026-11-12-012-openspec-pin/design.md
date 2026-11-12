# Design

## Context

Change 011 moved spec-ctx to 0.6.0 and listed two risks. A trial on a worktree of `main` ran `specctx init --schema` and OpenSpec 2.0.0 with the schema `spec-driven`. Validate passed. `openspec instructions tasks` gave the rules for REQ citations and `Verify:` from `openspec/config.yaml`.

## Goals / Non-Goals

**Goals:**
- The gate, the hooks, and CI run one known OpenSpec version.
- OpenSpec reads the stock schema and the rules of spec-ctx 0.6.0.

**Non-Goals:**
- No refresh of the OpenSpec skills in `.claude/skills/openspec-*` and the commands in `.claude/commands/opsx/`. OpenSpec writes them with `openspec update`.
- No change in an archived change or in its evidence.

## Decisions

- 012/D1 A wrapper script pins OpenSpec, as `scripts/specctx.sh` pins spec-ctx. `[gate] openspec` runs it, so the gate, `next`, and the CI action use the same version. The alternative was the npx command in `spec-ctx.toml`. Then a person who runs OpenSpec by hand needs a second place to read the version. Refs: REQ-SKILL-014
- 012/D2 The pin is 2.0.0, the version that `@latest` gave on 2026-11-12. Change 011 passed on it. Refs: REQ-SKILL-014
- 012/D3 `specctx init --schema` writes the templates and merges two rule items. Its templates are equal to the templates of the old schema folder. The schema folder then goes. Refs: REQ-SKILL-014
- 012/D4 The old apply item `Close each task with specctx task done <id>. Never tick a checkbox by hand.` goes. The merged item says the same and adds `specctx-run`. A later `init --schema` adds the merged item again if it is absent, so the old item is the one to remove. Refs: REQ-SKILL-014
- 012/D5 The archive guidance keeps the two items of spec-ctx that name `openspec`. A first item says that `openspec` means `bash scripts/openspec.sh`, as the `specctx-run` skill reads it. An edit of an item of spec-ctx makes the next `init --schema` add the item again, so the note goes in a new item. A second run of `init --schema` added nothing. Refs: REQ-SKILL-014
- 012/D6 The evidence of task 001/1.1 keeps its command `grep -q spec-driven-ids openspec/config.yaml`. The evidence lists no file, so it does not go stale. The merged rule item names `openspec/templates/spec-driven-ids/`, so the command still passes. Refs: REQ-SKILL-014

## Risks / Trade-offs

- A new OpenSpec release does not reach this repository until a person raises the pin.
- The OpenSpec skills and the `opsx` commands call a bare `openspec`. An agent that follows them runs the version on its path.
- The `specctx-run` skill names the latest OpenSpec for a project with no `[gate] openspec`. This repository sets the key, so the line does not apply. The test skips the spec-ctx skill copies, because `init --skills` writes them.
- The `.openspec.yaml` of each change records its schema. Seven archived changes name `spec-driven-ids`. Validate does not read them, so they stay. The file of change 012 now names `spec-driven`, because `openspec status` failed on the old name.
- `init --schema` adds `adopt-report.md` to `.gitignore`. The line does no harm.
