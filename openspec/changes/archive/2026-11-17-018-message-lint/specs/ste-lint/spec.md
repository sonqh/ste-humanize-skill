# ste-lint (delta)

## ADDED Requirements

### Requirement: REQ-STE-005 Length of a Vietnamese sentence
A sentence SHALL count as Vietnamese when 30 percent or more of its words hold a letter that English does not use. The linter SHALL report `long-sentence` on a Vietnamese sentence of more than 35 syllables, and the message SHALL say "syllables". Other sentences SHALL keep the cap of REQ-STE-002.
Refs: REQ-STE-002, REQ-EVAL-006

#### Scenario: SCN-STE-005-1 Vietnamese sentence under the cap
- **WHEN** a Vietnamese sentence has 30 syllables
- **THEN** `long-sentence` does not fire

#### Scenario: SCN-STE-005-2 Vietnamese sentence over the cap
- **WHEN** a Vietnamese sentence has 43 syllables
- **THEN** `long-sentence` fires and the message contains `syllables`

#### Scenario: SCN-STE-005-3 English keeps its cap
- **WHEN** an English sentence has 26 words and one Vietnamese name
- **THEN** `long-sentence` fires with the cap of 25
