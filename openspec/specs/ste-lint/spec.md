# ste-lint Specification

## Purpose
`scripts/ste-lint.py` checks the ASD-STE100 structural rules the skill applies. Levels: `advisory-free` rules count as hard findings, `advisory` rules print only.

## Requirements

### Requirement: REQ-STE-001 Rule table and levels
Every rule in `RULES` SHALL have an id, a level of `advisory-free` or `advisory`, a pattern, and a message that names the STE rule it comes from. The spec test SHALL assert the list of rule ids and levels in the script equals the list recorded in `tests/ste_rules.json`. A new rule SHALL fail that test until the list is updated.

#### Scenario: SCN-STE-001-1 Table matches
- **WHEN** the test reads `RULES` and `tests/ste_rules.json`
- **THEN** the id and level lists are equal

#### Scenario: SCN-STE-001-2 Message names the rule
- **WHEN** the test reads every message in `RULES`
- **THEN** each message is non-empty and under 160 characters

### Requirement: REQ-STE-002 Core structural checks
The linter SHALL report `long-sentence` when a sentence exceeds the word cap (25 words for descriptive text). It SHALL report `semicolon` on any `;` outside code. It SHALL report `passive-voice` and `present-perfect` as advisory, with modal perfect excluded. It SHALL also report `nominalization`, `phrasal-verb`, `marketing-adjective`, and `synonym-rotation`. Hedges (`may`, `might`, `could`) SHALL never be flagged.

#### Scenario: SCN-STE-002-1 Long sentence
- **WHEN** a sentence has 26 words
- **THEN** `long-sentence` fires with the word count in the message

#### Scenario: SCN-STE-002-2 Hedge is protected
- **WHEN** a line reads `The request may have failed.`
- **THEN** neither `present-perfect` nor any other rule fires

#### Scenario: SCN-STE-002-3 Code is skipped
- **WHEN** a semicolon sits inside a fenced code block
- **THEN** `semicolon` does not fire

### Requirement: REQ-STE-003 CLI contract
The script SHALL accept `FILE...` or stdin, `--baseline N`, `--disable <rules>`, `--json`, and `--selftest`. It SHALL exit 1 when hard findings exceed the baseline, else 0. The last two lines of human output SHALL be the violation summary and the hedge note. `--selftest` SHALL exit 0 and print `selftest OK`. An unknown rule in `--disable` SHALL exit 2 and list the known rules. `--json` SHALL print one object with `violations`, `count`, `hard_count`, `baseline`, `words`, `per_100_words`.

#### Scenario: SCN-STE-003-1 Disable
- **WHEN** `--disable synonym-rotation` is given on a file whose only hard finding is that rule
- **THEN** the run exits 0

#### Scenario: SCN-STE-003-3 JSON shape
- **WHEN** `--json` runs on any file
- **THEN** stdout parses as one object with the six keys above

#### Scenario: SCN-STE-003-2 Summary line
- **WHEN** the linter runs on any file
- **THEN** the output has a line that matches `N violations (M hard, baseline B)`

### Requirement: REQ-STE-004 Shape advisories
The linter SHALL report three advisory findings for each prose block. `long-paragraph` fires when a block has more than 6 sentences. `inline-list` fires when one sentence lists 5 or more items with commas and a last `and` or `or`. `buried-sequence` fires when a block holds 3 or more different sequence words. No shape finding SHALL fail the run. Each list item is its own block. Code is skipped.

#### Scenario: SCN-STE-004-1 Long paragraph
- **WHEN** a paragraph has 7 sentences
- **THEN** `long-paragraph` fires once with the sentence count in the match, and a paragraph of 6 sentences gets no finding

#### Scenario: SCN-STE-004-2 Inline list
- **WHEN** one sentence lists 5 items with commas and a last `and`
- **THEN** `inline-list` fires, and a sentence with 4 items gets no finding

#### Scenario: SCN-STE-004-3 Buried sequence
- **WHEN** a paragraph holds `first`, `then`, and `finally`
- **THEN** `buried-sequence` fires, and a numbered list with one sequence word in each item gets no finding

#### Scenario: SCN-STE-004-4 Advisory only
- **WHEN** a file holds only shape findings
- **THEN** the run exits 0, each finding has the level `advisory`, and `--disable long-paragraph` removes that finding
