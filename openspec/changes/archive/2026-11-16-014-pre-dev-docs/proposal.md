# Proposal

## Why

The owner asked on 2026-11-16 for help with documents that come before the code. These are a design doc, an ADR that is not accepted yet, and a proposal for a feature in planning. The guides of change 010 assume that the team already decided and has the numbers.

- The proposal guide asks for the gain as a number and for the cost. A Write task must not add a fact that the material does not give. When the notes have no number, the agent can invent one or skip the question without a word.
- A page before the code mixes facts of four kinds: a measured number, an estimate, a target, and an assumption. The skill does not tell the writer to mark which is which.
- The ADR guide has no rule for the status Proposed, and no rule that names the criteria before the options.
- No guide covers a design doc: goals, non-goals, the options, and the open questions of a feature that is not built.

## What Changes

- `references/page-guides.md` gains `## Work not built yet`: the four kinds of claim, the `TBD` mark for a gap, and the section of open questions.
- `references/page-guides.md` gains `## Design doc`: its readers, their questions in order, and a test.
- The ADR guide gains the status Proposed and a table that scores each option on the same criteria.
- `SKILL.md` gains one route row and the trailer `Missing:`. The section `## Resources` goes, to keep the file under the cap of 1900 words.
- `evals/eval.py` reads `Missing:` as a trailer.
- Two eval fixtures: a design doc from notes with no cost, and an ADR from a thread that did not decide.
- The version rises to 0.7.0.

## Capabilities

### Modified Capabilities
- `skill-contract`: the guide for work not built yet, the design doc guide, the Proposed ADR, and the `Missing:` trailer.
- `eval`: the scorer reads `Missing:` as a trailer.

## Impact

- `SKILL.md`, `references/doc-shapes.md`, `references/page-guides.md`, `README.md`, `.claude-plugin/plugin.json`.
- `evals/eval.py`, `evals/fixtures/`, `evals/runs/`, `tests/test_skill_contract.py`, `tests/test_eval.py`.
- No change in the linters.
