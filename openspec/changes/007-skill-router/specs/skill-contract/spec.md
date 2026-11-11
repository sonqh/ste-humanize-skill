# skill-contract (delta)

## MODIFIED Requirements

### Requirement: REQ-SKILL-004 Size, front page, and export
`SKILL.md` SHALL stay under 1900 words. `README.md` SHALL lint at baseline 0 with both scripts and with `lint.py`. It SHALL open with one sentence of value and SHALL hold no `## Develop` section. The full before and after table SHALL live in `examples/before-after.md`. `.gitattributes` SHALL mark the maintainer folders `export-ignore`. `git archive` of HEAD then holds no `openspec/`, `tests/`, `evals/`, `.ctx/`, or `.claude/`.

#### Scenario: SCN-SKILL-004-1 Word cap
- **WHEN** the test counts the words of `SKILL.md`
- **THEN** the count is under 1900

#### Scenario: SCN-SKILL-004-2 README lints clean
- **WHEN** `python3 scripts/lint.py README.md` runs
- **THEN** it exits 0

#### Scenario: SCN-SKILL-004-3 Clean archive
- **WHEN** `git archive HEAD | tar -t` runs
- **THEN** the list has `SKILL.md`, `references/`, `scripts/`, `examples/`, and no `openspec/`, `tests/`, `evals/`, `.claude/`

### Requirement: REQ-SKILL-006 Audience fit
`references/human.md` SHALL hold a section `## Audience fit` for Human mode. The writer SHALL find what the reader already knows first. The writer SHALL keep an identifier only when the reader needs it for a task, and SHALL apply this test to appendices. The writer SHALL verify claims against source code and SHALL use meaningful links. Precedence item 1 in `SKILL.md` SHALL keep every condition and exception. Bullets SHALL group the sentences of one event.

#### Scenario: SCN-SKILL-006-1 Reader first
- **WHEN** the test reads `## Audience fit` in `references/human.md`
- **THEN** it contains `Human mode`, `already know`, and `complete a task`

#### Scenario: SCN-SKILL-006-2 Appendices
- **WHEN** the test reads `## Audience fit` in `references/human.md`
- **THEN** it contains `appendices` and `collapsed sections`

#### Scenario: SCN-SKILL-006-3 Source and links
- **WHEN** the test reads `## Audience fit` in `references/human.md`
- **THEN** it contains `against the source code` and `link text`

#### Scenario: SCN-SKILL-006-4 Conditions survive and identifiers stay exact
- **WHEN** the test reads item 1 of the precedence list in `SKILL.md` and `## Technical terms and other languages` in `references/terms.md`
- **THEN** item 1 contains `condition` and `exception`, and the terms section contains `Audience fit` and `Strict mode`

#### Scenario: SCN-SKILL-006-5 One event per bullet
- **WHEN** the test reads `## Shape: fit the content` in `SKILL.md`
- **THEN** it contains `one event` and `Independent rules`

## ADDED Requirements

### Requirement: REQ-SKILL-011 Route table
`SKILL.md` SHALL hold a section `## What to read` with a table from a case to a file in `references/`. The table SHALL name every file in `references/` and no other file. Process step 1 SHALL name that section. `references/human.md`, `references/terms.md`, and `references/doc-shapes.md` SHALL say in their first lines when to read them. A rule that moved to a reference file SHALL have no section of its own in `SKILL.md`.

#### Scenario: SCN-SKILL-011-1 Every reference is routed
- **WHEN** the test reads the table in `## What to read` and lists `references/`
- **THEN** the two sets of file names are equal

#### Scenario: SCN-SKILL-011-2 No dead reference
- **WHEN** the test reads each path under `references/` or `scripts/` that `SKILL.md` or a reference file names in a code span
- **THEN** each path exists

#### Scenario: SCN-SKILL-011-3 Each file says when to read it
- **WHEN** the test reads the first four lines of `references/human.md`, `references/terms.md`, and `references/doc-shapes.md`
- **THEN** each holds `Read this file when`

#### Scenario: SCN-SKILL-011-4 One home for each rule
- **WHEN** the test reads the `## ` headers of `SKILL.md` and step 1 of `## Process`
- **THEN** no header reads `Voice`, `Audience fit`, `Humanizer patterns`, or `Technical terms and other languages`, no header appears two times, and step 1 contains `What to read`
