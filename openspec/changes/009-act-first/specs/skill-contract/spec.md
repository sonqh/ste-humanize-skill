# skill-contract (delta)

## MODIFIED Requirements

### Requirement: REQ-SKILL-003 Output format
`SKILL.md` SHALL require the text and nothing else as output. It SHALL permit three lines after the text, each only when there is something to report. `Kept as-is:` names a longer phrase kept on purpose. `Cut candidates:` names a part of a Rewrite that does not serve the reader. `Reader:` names a reader that the writer chose, and SHALL appear only when the request does not name the reader. It SHALL forbid a preamble before the text.

#### Scenario: SCN-SKILL-003-1 Format section
- **WHEN** the test reads the `## Output format` section
- **THEN** it contains `Kept as-is:`, `Cut candidates:`, `Reader:`, and the phrase `nothing else`

#### Scenario: SCN-SKILL-003-2 Reader line
- **WHEN** the test reads `## Output format` and `## Reader first`
- **THEN** the first contains `only when the request does not name the reader`, and the second tells the writer to add no `Reader:` line when the request names the reader

### Requirement: REQ-SKILL-009 Reader first
`SKILL.md` SHALL hold a section `## Reader first`. It SHALL give a reader brief as a numbered list of three questions. They ask who reads, what the reader knows, and what the reader does next. It SHALL require the answer in the first sentence. It SHALL tell the writer to stop when the reader can act. It SHALL name `references/doc-shapes.md` for the usual reader of each kind of page. That file SHALL put the first task before the reference. Process step 1 SHALL name the reader brief.

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

#### Scenario: SCN-SKILL-009-5 First task before the reference
- **WHEN** the test reads `references/doc-shapes.md`
- **THEN** it contains `The first task comes before the reference`
