# skill-contract (delta)

## ADDED Requirements

### Requirement: REQ-SKILL-012 Page guides
`references/doc-shapes.md` SHALL hold a section `## Reader questions` with a method of six numbered steps and a test of the title, the first paragraph, and the headings. `references/page-guides.md` SHALL hold a guide for a README, an ADR, and a technical proposal. Each guide SHALL name its readers, list their questions in order, and end with a test. `SKILL.md` SHALL let a Rewrite move a part and remove none.

#### Scenario: SCN-SKILL-012-1 Reader questions
- **WHEN** the test reads `## Reader questions` in `references/doc-shapes.md`
- **THEN** it holds six numbered steps and contains `cut candidate` and `first paragraph, and the headings`

#### Scenario: SCN-SKILL-012-2 Three guides
- **WHEN** the test reads `## README`, `## ADR`, and `## Technical proposal` in `references/page-guides.md`
- **THEN** each one contains `Readers:`, six or more numbered questions, and a line that starts with `Test:`

#### Scenario: SCN-SKILL-012-3 Table rows and the template rule
- **WHEN** the test reads `references/doc-shapes.md`
- **THEN** the table has a row `ADR` and a row `Technical proposal`, and the file contains `keep its headings and their order`

#### Scenario: SCN-SKILL-012-4 The skill names the questions
- **WHEN** the test reads `## Reader first`, `## Two tasks`, and `## What to read` in `SKILL.md`
- **THEN** the first contains `questions the reader brings`. The second contains `A Rewrite may move a part` and `removes none`. The third names a Rewrite of a whole page and the three kinds of page
