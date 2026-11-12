# Proposal

## Why

The long eval of change 008 left two questions for the owner. The owner asked on 2026-11-11 for the answer that serves the reader best.

- How long may a page be? The README from notes had 695 to 755 words, and its fixture allowed 560.
- When does the `Reader:` line appear? Version 0.5.0 added it in 2 of 3 Strict runs, and the request named the reader.

## What Changes

- No word limit for a page. A reader does not count words. A reader wants to act soon and to find a detail later. The stored outputs already put the install command and the first command near the top, and the reference detail at the end. The measure changes, and the skill text does not get a length rule.
- `references/doc-shapes.md` states the order as a rule: the first task comes before the reference.
- The `Reader:` line appears only when the request does not name the reader. `## Reader first` and `## Output format` both say so.
- The eval gets a check `early`: a pattern must start in the first N words of the output.
- The word limit of each long fixture becomes the word count of its material. A text must not be longer than what it was made from.
- The version rises to 0.5.1.

## Capabilities

### Modified Capabilities
- `skill-contract`: the rule for the `Reader:` line, and the order of a page.
- `eval`: the `early` check.

## Impact

- `SKILL.md`, `references/doc-shapes.md`, `.claude-plugin/plugin.json`.
- `evals/eval.py`, three fixtures, `tests/test_eval.py`, `tests/test_skill_contract.py`.
