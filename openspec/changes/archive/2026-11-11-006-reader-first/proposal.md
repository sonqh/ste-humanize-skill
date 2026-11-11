# Proposal

## Why

The owner wants text from this skill to serve the reader: clear, easy to understand, and short. He asked for this on 2026-11-11. He also uses the skill to write a new document, and the skill has no rule for that case.

- `SKILL.md` describes a rewrite only. `## Process` starts from a text that exists. An agent that writes a new page gets no step that selects the content.
- The reader decides which identifiers stay. The reader does not decide which ideas stay, or where the answer goes.
- Brevity is last in the precedence and has no rule of its own. The STE split makes a text longer.
- "Lead with the decision" applies to a reply only (pattern 26). A document or a PR description has no such rule.
- `## Shape: bullets first` relies on the agent to see parallel parts. The linter has no check for a long paragraph. The title also pushes an agent to cut reasoning into bullets.

## What Changes

- A section `## Two tasks` with `Rewrite` and `Write`. The task sets what the writer may leave out. The two modes stay.
- A section `## Reader first` with a reader brief of three questions, the answer first rule, and a stop rule for length.
- `## Shape: bullets first` becomes `## Shape: fit the content`, with a table from content to shape and three signs to check.
- Two new output lines: `Cut candidates:` for a Rewrite and `Reader:` when the writer chose the reader.
- A new file `references/doc-shapes.md`. It lists the usual reader and the opening of each kind of page. The newcomer page rules move there.
- Three advisory checks in `scripts/ste-lint.py`: `long-paragraph`, `inline-list`, and `buried-sequence`.
- The word cap of `SKILL.md` rises from 2400 to 2800. The version rises to 0.4.0.

## Capabilities

### Modified Capabilities
- `skill-contract`: the output lines, the word cap, and the place of the newcomer rules. Also the two tasks, the reader brief, and the shape section with its table.
- `ste-lint`: three advisory shape checks.

## Impact

- `SKILL.md`, `references/doc-shapes.md`, `README.md`, `examples/before-after.md`.
- `scripts/ste-lint.py`, `tests/test_ste_lint.py`, `tests/test_skill_contract.py`.
- `.claude-plugin/plugin.json`.
- Out of scope: an eval that measures what an agent writes with the skill. It needs a model call, so it gets its own change.
