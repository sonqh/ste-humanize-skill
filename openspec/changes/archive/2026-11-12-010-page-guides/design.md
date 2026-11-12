# Design

## Context

Change 006 added the reader brief. Change 007 moved the page table to `references/doc-shapes.md`. The table answers who reads a page and how the page opens. This change is stacked on change 009, which is not archived.

## Goals / Non-Goals

**Goals:**
- An agent orders a whole document by what its reader asks, first question first.
- The three kinds of page that the owner named get a guide: README, ADR, technical proposal.
- A rewrite of a whole page can fix a wrong order.

**Non-Goals:**
- No template with fixed headings. A team has its own template, and the skill keeps it.
- No guide for every kind of page. The method covers the others.
- No change in `evals/eval.py`.

## Decisions

- 010/D1 The method is a list of reader questions. The writer lists the questions, orders them by urgency, and gives each one a section. The alternative was a fixed outline for each kind of page. An outline tells the writer what to fill in. A question tells the writer what the reader needs, so it also shows what to leave out. Refs: REQ-SKILL-012
- 010/D2 The method ends with a test. The writer reads only the title, the first paragraph, and the headings. A reader scans a document that way before they read it. Refs: REQ-SKILL-012
- 010/D3 The three guides live in a new file, `references/page-guides.md`, with 570 words. An agent that writes a how-to guide or a runbook does not read them. `references/doc-shapes.md` keeps the table and the method. Refs: REQ-SKILL-012
- 010/D4 Each guide names more than one reader and says who comes first. An ADR serves a maintainer a year later before it serves the reviewer of today. A proposal serves the approver before the people who build. Refs: REQ-SKILL-012
- 010/D5 The ADR guide states the decision in the title and gives the status next. The common ADR form puts the context first. The reader of an old ADR asks what the team decided before they ask why. Refs: REQ-SKILL-012
- 010/D6 A template of the repository wins over the order of a guide. The writer keeps its headings and their order, and applies the reader rules to the title, to the summary, and inside each section. Readers and tools find a part by its heading. Refs: REQ-SKILL-012
- 010/D7 A Rewrite may move a part. Precedence item 1 protects each fact, not its place. The rule sits in `## Two tasks`, next to the rule that a Rewrite removes nothing. Refs: REQ-SKILL-012
- 010/D8 `SKILL.md` gains one route row, one bullet, and two sentences. It has 1892 words, 8 under the cap. Refs: REQ-SKILL-012

## Risks / Trade-offs

- A Write of a README, an ADR, or a proposal reads 570 words more than before.
- A Rewrite that moves parts is harder to compare with its source. The `Cut candidates:` line and the rule that no fact goes stay the guard.
- The guides give one order. A team can want another. The template rule in 010/D6 covers a team that wrote its order down.
- `SKILL.md` has 8 words of room. The next rule must go to `references/`.
