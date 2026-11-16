# Proposal

## Why

The owner asked on 2026-11-16 for a review of a document as a task of its own. A team reviews a design doc, an ADR, or a proposal before the work starts, and the author must keep the text. Today the skill can only write or rewrite. A request such as "review this RFC" gets a rewritten page, or a list of opinions in no fixed form.

- The page guides already hold the questions of each reader. Nothing uses them to check a page that exists.
- Change 014 added the rules for work not built yet. A review must find a gap, a claim with no kind, and an option that is missing.
- The author needs each finding next to the place in the page, and the most important one first.

## What Changes

- `references/review.md` is new. It holds the steps of a review and its output. The output starts with a verdict in one sentence. Then a table checks each reader question: answered, partly, or not, where, and what is missing. Then up to seven other findings, the most severe first. Then one line with the lint count.
- A review changes no text and adds no fact. It names what is missing.
- `SKILL.md` gains one route row to `references/review.md`, and "review" in its triggers. Its second paragraph gets shorter, to stay under the cap of 1900 words.
- `evals/eval.py` accepts the task `Review`. Two fixtures: a review of a design doc with gaps, and a review of a page that is ready.
- The version rises to 0.8.0.

## Capabilities

### Modified Capabilities
- `skill-contract`: the review of a page.
- `eval`: fixtures for the task Review.

## Impact

- `SKILL.md`, `references/review.md`, `README.md`, `.claude-plugin/plugin.json`.
- `evals/eval.py`, `evals/fixtures/`, `evals/runs/`, `tests/test_skill_contract.py`, `tests/test_eval.py`.
- No change in the linters.
- This change is stacked on change 014, which is not merged.
