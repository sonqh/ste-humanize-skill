# tells-lint (delta)

## MODIFIED Requirements

### Requirement: REQ-TELLS-002 Advisory rules
The `RULES` table SHALL hold exactly these advisory rules: `sales-word`, `title-case-heading`, `stacked-qualifier`, `serves-as`, `closer`, `repeated-closer`, `false-balance`, `actorless-decision`, `empty-mitigation`, `unmeasured-quality`. An advisory finding SHALL print with its rule name and SHALL not count toward the baseline.

#### Scenario: SCN-TELLS-002-1 Table matches
- **WHEN** the test reads `RULES` from the script
- **THEN** the set of rules with level `advisory` equals the ten names above

#### Scenario: SCN-TELLS-002-2 Advisory does not fail
- **WHEN** a file has one `closer` finding and no hard finding
- **THEN** the run prints the finding and exits 0

## ADDED Requirements

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
