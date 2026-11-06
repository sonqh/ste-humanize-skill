# skill-contract (delta)

## MODIFIED Requirements

### Requirement: REQ-SKILL-004 Size, front page, and export
`SKILL.md` SHALL stay under 2400 words. `README.md` SHALL lint at baseline 0 with both scripts and with `lint.py`. It SHALL open with one sentence of value and SHALL hold no `## Develop` section. The full before and after table SHALL live in `examples/before-after.md`. `.gitattributes` SHALL mark the maintainer folders `export-ignore`. `git archive` of HEAD then holds no `openspec/`, `tests/`, `.ctx/`, or `.claude/`.

#### Scenario: SCN-SKILL-004-1 Word cap
- **WHEN** the test counts the words of `SKILL.md`
- **THEN** the count is under 2400

#### Scenario: SCN-SKILL-004-2 README lints clean
- **WHEN** `python3 scripts/lint.py README.md` runs
- **THEN** it exits 0

#### Scenario: SCN-SKILL-004-3 Clean archive
- **WHEN** `git archive HEAD | tar -t` runs
- **THEN** the list has `SKILL.md`, `references/`, `scripts/`, `examples/`, and no `openspec/`, `tests/`, `.claude/`

## ADDED Requirements

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
- **WHEN** the test reads `## Shape: bullets first`
- **THEN** it contains `one event` and `Independent rules`
