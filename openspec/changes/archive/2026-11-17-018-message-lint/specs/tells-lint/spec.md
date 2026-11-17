# tells-lint (delta)

## ADDED Requirements

### Requirement: REQ-TELLS-005 Tells of messages
The `RULES` table SHALL hold the advisory rules `support-cliche`, `vague-date`, `blame-phrase`, `negative-contraction`, and `particle-repeat`. The first three SHALL match English and Vietnamese phrases. `particle-repeat` SHALL fire once per file when "dạ" or "ạ" occurs more than once. Each rule SHALL have one matching and one non-matching selftest example.
Refs: REQ-TELLS-002, REQ-SKILL-021

#### Scenario: SCN-TELLS-005-1 Stock phrase in both languages
- **WHEN** one line reads `We apologize for any inconvenience.` and another reads `Mong quý khách thông cảm.`
- **THEN** `support-cliche` fires twice

#### Scenario: SCN-TELLS-005-2 Vague date
- **WHEN** a line reads `We will fix it soon.` or `Bên em sẽ xử lý trong thời gian sớm nhất.`
- **THEN** `vague-date` fires, and it does not fire on `We will fix it on 3 March.`

#### Scenario: SCN-TELLS-005-3 Blame and contraction
- **WHEN** a line reads `You forgot to save, so we can't restore it.`
- **THEN** `blame-phrase` and `negative-contraction` each fire once

#### Scenario: SCN-TELLS-005-4 Particle once per file
- **WHEN** a file holds `Dạ` once and `ạ` twice
- **THEN** `particle-repeat` fires once, and it does not fire on a file with one `ạ`

## MODIFIED Requirements

### Requirement: REQ-TELLS-001 Hard rules
The `RULES` table SHALL hold exactly these hard rules: `dash`, `not-x-but-y`, `not-x-its-y`, `chat-residue`, `run-up`, `deep-saying`, `stock-word`, `bold-label`, `emoji-heading`. A hard finding SHALL count toward the baseline. `not-x-its-y` SHALL match across a comma, period, colon, semicolon, em dash, en dash, or spaced hyphen. `not-x-but-y` SHALL match "không phải ... mà". `stock-word` SHALL match inflections and plurals. Each rule SHALL have one matching and one non-matching selftest example.

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

#### Scenario: SCN-TELLS-001-6 Vietnamese contrast
- **WHEN** a line reads `Không phải lỗi hệ thống mà là do cấu hình.`
- **THEN** `not-x-but-y` fires once

### Requirement: REQ-TELLS-002 Advisory rules
The `RULES` table SHALL hold exactly these advisory rules: `sales-word`, `title-case-heading`, `stacked-qualifier`, `serves-as`, `closer`, `repeated-closer`, `false-balance`, `actorless-decision`, `empty-mitigation`, `unmeasured-quality`, `support-cliche`, `vague-date`, `blame-phrase`, `negative-contraction`, `particle-repeat`. An advisory finding SHALL print with its rule name and SHALL not count toward the baseline.

#### Scenario: SCN-TELLS-002-1 Table matches
- **WHEN** the test reads `RULES` from the script
- **THEN** the set of rules with level `advisory` equals the fifteen names above

#### Scenario: SCN-TELLS-002-2 Advisory does not fail
- **WHEN** a file has one `closer` finding and no hard finding
- **THEN** the run prints the finding and exits 0
