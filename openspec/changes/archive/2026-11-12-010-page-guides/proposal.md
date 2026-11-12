# Proposal

## Why

The owner asked on 2026-11-11 for more help with whole documents: a document, an ADR, a README, a technical proposal. The skill must write and rewrite them from the view of the reader.

- `references/doc-shapes.md` gives one table row for each kind of page. A row names the reader and the opening. It does not say what the reader asks next, or in which order.
- The table has no row for an ADR or a technical proposal.
- A Rewrite keeps the order of the source. A proposal that states its request in the last paragraph keeps it there.
- The skill has no rule for a page with two kinds of reader, or for a repository that has its own template.

## What Changes

- `references/doc-shapes.md` gains `## Reader questions`: a method of six steps that orders any document by the questions of its reader.
- `references/page-guides.md` is new. It holds a guide for a README, an ADR, and a technical proposal. Each guide lists the readers, their questions in order, and one test.
- The table gains a row for an ADR and a row for a technical proposal.
- A rule for templates: keep the headings and the order of a template of the repository.
- A Rewrite may move a part. It moves facts and removes none.
- Two eval fixtures: an ADR from a chat thread, and a long proposal.
- The version rises to 0.6.0.

## Capabilities

### Modified Capabilities
- `skill-contract`: the reader questions, the three page guides, and the rule that a Rewrite may move a part.

## Impact

- `SKILL.md`, `references/doc-shapes.md`, `references/page-guides.md`, `README.md`, `.claude-plugin/plugin.json`.
- `evals/fixtures/`, `evals/runs/`, `tests/test_skill_contract.py`.
- No change in the linters or in `evals/eval.py`.
