# skill-contract (delta)

## MODIFIED Requirements

### Requirement: REQ-SKILL-003 Output format
`SKILL.md` SHALL require the text and nothing else as output. It SHALL permit three lines after the text, each only when there is something to report. `Kept as-is:` names a longer phrase kept on purpose. `Cut candidates:` names a part of a Rewrite that does not serve the reader. `Reader:` names a reader that the writer chose. It SHALL forbid a preamble before the text.

#### Scenario: SCN-SKILL-003-1 Format section
- **WHEN** the test reads the `## Output format` section
- **THEN** it contains `Kept as-is:`, `Cut candidates:`, `Reader:`, and the phrase `nothing else`

### Requirement: REQ-SKILL-004 Size, front page, and export
`SKILL.md` SHALL stay under 2800 words. `README.md` SHALL lint at baseline 0 with both scripts and with `lint.py`. It SHALL open with one sentence of value and SHALL hold no `## Develop` section. The full before and after table SHALL live in `examples/before-after.md`. `.gitattributes` SHALL mark the maintainer folders `export-ignore`. `git archive` of HEAD then holds no `openspec/`, `tests/`, `.ctx/`, or `.claude/`.

#### Scenario: SCN-SKILL-004-1 Word cap
- **WHEN** the test counts the words of `SKILL.md`
- **THEN** the count is under 2800

#### Scenario: SCN-SKILL-004-2 README lints clean
- **WHEN** `python3 scripts/lint.py README.md` runs
- **THEN** it exits 0

#### Scenario: SCN-SKILL-004-3 Clean archive
- **WHEN** `git archive HEAD | tar -t` runs
- **THEN** the list has `SKILL.md`, `references/`, `scripts/`, `examples/`, and no `openspec/`, `tests/`, `.claude/`

### Requirement: REQ-SKILL-005 Newcomer shape, captions, and numbers
`references/doc-shapes.md` SHALL hold a section `## A page for a newcomer` with a numbered list of five parts. The order: the base thing, the problem, what the tool does, proof, how to try it. The section SHALL give the caption rule. A caption for a clip or screenshot states what the reader sees, then why it matters. It does not repeat the command. `SKILL.md` SHALL name that file. `## Boundaries` in `SKILL.md` SHALL say that a number needs a scale the reader has.

#### Scenario: SCN-SKILL-005-1 Section and order
- **WHEN** the test reads the `## A page for a newcomer` section of `references/doc-shapes.md`
- **THEN** it holds a list of five numbered items and the first names the base thing and the fifth names how to try it

#### Scenario: SCN-SKILL-005-2 Caption rule
- **WHEN** the test reads that section
- **THEN** it contains `what the reader sees` and `does not repeat the command`

#### Scenario: SCN-SKILL-005-3 Numbers need a scale
- **WHEN** the test reads `## Boundaries` in `SKILL.md`
- **THEN** it contains `scale the reader has`

### Requirement: REQ-SKILL-006 Audience fit
`SKILL.md` SHALL hold a section `## Audience fit` for Human mode. The writer SHALL find what the reader already knows first. The writer SHALL keep an identifier only when the reader needs it for a task, and SHALL apply this test to appendices. The writer SHALL verify claims against source code and SHALL use meaningful links. Precedence item 1 SHALL keep every condition and exception. Bullets SHALL group the sentences of one event.

#### Scenario: SCN-SKILL-006-1 Reader first
- **WHEN** the test reads `## Audience fit`
- **THEN** it contains `Human mode`, `already know`, and `complete a task`

#### Scenario: SCN-SKILL-006-2 Appendices
- **WHEN** the test reads `## Audience fit`
- **THEN** it contains `appendices` and `collapsed sections`

#### Scenario: SCN-SKILL-006-3 Source and links
- **WHEN** the test reads `## Audience fit`
- **THEN** it contains `against the source code` and `link text`

#### Scenario: SCN-SKILL-006-4 Conditions survive and identifiers stay exact
- **WHEN** the test reads item 1 of `## Order of precedence when rules conflict` and `## Technical terms and other languages`
- **THEN** item 1 contains `condition` and `exception`, and the terms section contains `Audience fit` and `Strict mode`

#### Scenario: SCN-SKILL-006-5 One event per bullet
- **WHEN** the test reads `## Shape: fit the content`
- **THEN** it contains `one event` and `Independent rules`

## ADDED Requirements

### Requirement: REQ-SKILL-008 Two tasks
`SKILL.md` SHALL define exactly two tasks under a `## Two tasks` header: `Rewrite` and `Write`. In a Rewrite the source is the truth. The writer SHALL report a part the reader does not need as a cut candidate and SHALL NOT remove it. In a Write the reader brief decides the content. A Write SHALL still include every condition, exception, and limit of a behavior it describes, and every safety condition. Precedence item 1 SHALL name the Write task.

#### Scenario: SCN-SKILL-008-1 Header and names
- **WHEN** the test reads the `## Two tasks` section
- **THEN** the bold labels are `Rewrite` and `Write` and no third label

#### Scenario: SCN-SKILL-008-2 Rewrite keeps the source
- **WHEN** the test reads the `## Two tasks` section
- **THEN** it contains `Cut candidates:` and `source is the truth`

#### Scenario: SCN-SKILL-008-3 Limits of a Write
- **WHEN** the test reads the `## Two tasks` section and item 1 of the precedence list
- **THEN** the section contains `safety condition` and `exception`, and item 1 contains `Write task`

### Requirement: REQ-SKILL-009 Reader first
`SKILL.md` SHALL hold a section `## Reader first`. It SHALL give a reader brief as a numbered list of three questions. They ask who reads, what the reader already knows, and what the reader does after reading. It SHALL require the answer in the first sentence. It SHALL tell the writer to stop when the reader can act. It SHALL name `references/doc-shapes.md` as the place that lists the usual reader of each kind of page. Process step 1 SHALL name the reader brief.

#### Scenario: SCN-SKILL-009-1 Brief of three questions
- **WHEN** the test reads the `## Reader first` section
- **THEN** it holds a numbered list of three items and contains `reader brief`

#### Scenario: SCN-SKILL-009-2 Answer first and stop rule
- **WHEN** the test reads the `## Reader first` section
- **THEN** it contains `Answer first` and `reader can act`

#### Scenario: SCN-SKILL-009-3 Kinds of page
- **WHEN** the test reads the `## Reader first` section and `references/doc-shapes.md`
- **THEN** the section names the file. The file has a table row for each of these: README, how-to guide, reference page, design note, PR description, runbook

#### Scenario: SCN-SKILL-009-4 Process names the brief
- **WHEN** the test reads step 1 of `## Process`
- **THEN** it contains `reader brief` and `task`

### Requirement: REQ-SKILL-010 Shape fits the content
`SKILL.md` SHALL hold a section `## Shape: fit the content` and no section `## Shape: bullets first`. The section SHALL hold a table from a kind of content to a shape. The table SHALL cover bullets, a numbered list, a table, and prose. The section SHALL name three signs of a wrong shape. They are a paragraph of more than 6 sentences, a sentence that lists 5 or more items, and a sentence that walks through steps. It SHALL tell the writer to keep reasoning in prose.

#### Scenario: SCN-SKILL-010-1 Table of shapes
- **WHEN** the test reads the `## Shape: fit the content` section
- **THEN** it holds a table with the cells `Bullets`, `Numbered list`, `Table`, and a cell that starts with `Prose`

#### Scenario: SCN-SKILL-010-2 Signs
- **WHEN** the test reads that section
- **THEN** it contains `more than 6 sentences` and `5 or more items`

#### Scenario: SCN-SKILL-010-3 Reasoning stays prose
- **WHEN** the test reads that section and the list of `## ` headers
- **THEN** the section contains `Do not cut reasoning into bullets`, and no header reads `Shape: bullets first`
