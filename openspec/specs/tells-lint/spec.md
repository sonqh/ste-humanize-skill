# tells-lint Specification

## Purpose
`scripts/tells-lint.py` finds signs of AI writing in markdown. Hard rules fail the run. Advisory rules print and do not fail.

## Requirements

### Requirement: REQ-TELLS-001 Hard rules
The `RULES` table SHALL hold exactly these hard rules: `dash`, `not-x-but-y`, `not-x-its-y`, `chat-residue`, `run-up`, `deep-saying`, `stock-word`, `bold-label`, `emoji-heading`. A hard finding SHALL count toward the baseline. `not-x-its-y` SHALL match across a comma, period, colon, semicolon, em dash, en dash, or spaced hyphen. `stock-word` SHALL match the inflections of each verb and the plural of each noun in its list. Each rule SHALL have one matching and one non-matching selftest example.

#### Scenario: SCN-TELLS-001-1 Table matches
- **WHEN** the test reads `RULES` from the script
- **THEN** the set of rules with level `hard` equals the nine names above

#### Scenario: SCN-TELLS-001-2 Bold label with colon inside
- **WHEN** a line reads `- **Speed:** fast`
- **THEN** `bold-label` fires once

#### Scenario: SCN-TELLS-001-3 Dash as glue
- **WHEN** a line contains an em dash between two words
- **THEN** `dash` fires and the run exits 1 at baseline 0

#### Scenario: SCN-TELLS-001-4 Contrast across a dash
- **WHEN** a line reads `It's not just a linter — it's a gate.`
- **THEN** `not-x-its-y` fires once

#### Scenario: SCN-TELLS-001-5 Inflected stock word
- **WHEN** a line reads `The team leverages the cache.`
- **THEN** `stock-word` fires once with the match `leverages`

### Requirement: REQ-TELLS-002 Advisory rules
The `RULES` table SHALL hold exactly these advisory rules: `sales-word`, `title-case-heading`, `stacked-qualifier`, `serves-as`, `closer`, `repeated-closer`, `false-balance`, `actorless-decision`, `empty-mitigation`, `unmeasured-quality`. An advisory finding SHALL print with its rule name and SHALL not count toward the baseline.

#### Scenario: SCN-TELLS-002-1 Table matches
- **WHEN** the test reads `RULES` from the script
- **THEN** the set of rules with level `advisory` equals the ten names above

#### Scenario: SCN-TELLS-002-2 Advisory does not fail
- **WHEN** a file has one `closer` finding and no hard finding
- **THEN** the run prints the finding and exits 0

### Requirement: REQ-TELLS-003 CLI contract
The script SHALL accept `FILE...` or stdin, `--baseline N` (default 0), `--disable <rule,rule>`, `--json`, and `--selftest`, each with a help string. It SHALL exit 1 when hard findings exceed the baseline, else 0. `--json` SHALL print a list of `{file, findings}` with `rule`, `level`, `line`, `match` per finding. `--selftest` SHALL exit 0 and print `selftest ok`. An unknown rule in `--disable` SHALL exit 2 and name it. No file and empty stdin SHALL exit 2 with `no input`.

#### Scenario: SCN-TELLS-003-1 Baseline
- **WHEN** a file has 3 hard findings and `--baseline 3` is given
- **THEN** the run exits 0

#### Scenario: SCN-TELLS-003-2 JSON shape
- **WHEN** `--json` runs on a file with one finding
- **THEN** stdout parses as a JSON list with one object that has `file` and a `findings` list with one entry of `rule`, `level`, `line`, `match`

#### Scenario: SCN-TELLS-003-3 Unknown rule
- **WHEN** `--disable not-a-rule` is given
- **THEN** the run exits 2 and the message contains `not-a-rule`

#### Scenario: SCN-TELLS-003-4 Help strings
- **WHEN** `--help` runs
- **THEN** every flag line has a description after it

#### Scenario: SCN-TELLS-003-5 Empty input
- **WHEN** the script runs with no file and empty stdin
- **THEN** it exits 2 and prints `no input`

### Requirement: REQ-TELLS-004 Decision tells
`false-balance` SHALL match a phrase that avoids a choice. `actorless-decision` SHALL match a decision with no actor. `empty-mitigation` SHALL match a mitigation that names no action. `unmeasured-quality` SHALL match a quality word in a sentence with no digit, and SHALL not match when the sentence has a digit. Each rule SHALL have one matching and one non-matching selftest example.
Refs: REQ-TELLS-002, REQ-SKILL-020

#### Scenario: SCN-TELLS-004-1 False balance
- **WHEN** a line reads `Both options have their merits.`
- **THEN** `false-balance` fires once

#### Scenario: SCN-TELLS-004-2 Actorless decision
- **WHEN** a line reads `It was decided that the team uses pg-boss.`
- **THEN** `actorless-decision` fires once, and `The team decided to use pg-boss.` gives no finding

#### Scenario: SCN-TELLS-004-3 Empty mitigation
- **WHEN** a line reads `Mitigation: we will monitor closely.`
- **THEN** `empty-mitigation` fires once

#### Scenario: SCN-TELLS-004-4 Quality word with no number
- **WHEN** a line reads `Option B is more scalable.`
- **THEN** `unmeasured-quality` fires once, and `Option B scales to 350 jobs per second.` gives no finding

#### Scenario: SCN-TELLS-004-5 Advisory only
- **WHEN** a file holds one example of each of the four rules and nothing else
- **THEN** the run prints four findings and exits 0 at baseline 0
