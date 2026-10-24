# tells-lint Specification

## Purpose
`scripts/tells-lint.py` finds signs of AI writing in markdown. Hard rules fail the run. Advisory rules print and do not fail.

## Requirements

### Requirement: REQ-TELLS-001 Hard rules
The `RULES` table SHALL hold exactly these hard rules: `dash`, `not-x-but-y`, `not-x-its-y`, `chat-residue`, `run-up`, `deep-saying`, `stock-word`, `bold-label`, `emoji-heading`. A hard finding SHALL count toward the baseline. Each rule SHALL have one matching and one non-matching example in the selftest.

#### Scenario: SCN-TELLS-001-1 Table matches
- **WHEN** the test reads `RULES` from the script
- **THEN** the set of rules with level `hard` equals the nine names above

#### Scenario: SCN-TELLS-001-2 Bold label with colon inside
- **WHEN** a line reads `- **Speed:** fast`
- **THEN** `bold-label` fires once

#### Scenario: SCN-TELLS-001-3 Dash as glue
- **WHEN** a line contains an em dash between two words
- **THEN** `dash` fires and the run exits 1 at baseline 0

### Requirement: REQ-TELLS-002 Advisory rules
The `RULES` table SHALL hold exactly these advisory rules: `sales-word`, `title-case-heading`, `stacked-qualifier`, `serves-as`, `closer`, `repeated-closer`. An advisory finding SHALL print with its rule name and SHALL not count toward the baseline.

#### Scenario: SCN-TELLS-002-1 Table matches
- **WHEN** the test reads `RULES` from the script
- **THEN** the set of rules with level `advisory` equals the six names above

#### Scenario: SCN-TELLS-002-2 Advisory does not fail
- **WHEN** a file has one `closer` finding and no hard finding
- **THEN** the run prints the finding and exits 0

### Requirement: REQ-TELLS-003 CLI contract
The script SHALL accept `FILE...` or stdin, `--baseline N` (default 0), `--disable <rule,rule>`, `--json`, and `--selftest`. It SHALL exit 1 when hard findings exceed the baseline, else 0. `--json` SHALL print a list with one object per file, each with `file` and `findings` (each finding with `rule`, `level`, `line`, `match`). `--selftest` SHALL exit 0 and print `selftest ok`. An unknown rule in `--disable` SHALL exit 2 and name it.

#### Scenario: SCN-TELLS-003-1 Baseline
- **WHEN** a file has 3 hard findings and `--baseline 3` is given
- **THEN** the run exits 0

#### Scenario: SCN-TELLS-003-2 JSON shape
- **WHEN** `--json` runs on a file with one finding
- **THEN** stdout parses as a JSON list with one object that has `file` and a `findings` list with one entry of `rule`, `level`, `line`, `match`

#### Scenario: SCN-TELLS-003-3 Unknown rule
- **WHEN** `--disable not-a-rule` is given
- **THEN** the run exits 2 and the message contains `not-a-rule`
