# eval (delta)

## ADDED Requirements

### Requirement: REQ-EVAL-006 Fixtures in Vietnamese
A fixture MAY list rule names in `lint_disable`. The scorer SHALL drop the findings of those rules before the check `lint-hard`. The scorer SHALL read an output that opens with "Dưới đây là" or "Chắc chắn rồi" as a preamble.
Refs: REQ-EVAL-002, REQ-SKILL-021

#### Scenario: SCN-EVAL-006-1 Disabled rule
- **WHEN** a body holds a sentence of 30 words and the fixture lists `long-sentence` in `lint_disable`
- **THEN** the check `lint-hard` passes, and it fails for the same body when the fixture lists no rule

#### Scenario: SCN-EVAL-006-2 Vietnamese preamble
- **WHEN** an output opens with "Dưới đây là tin nhắn"
- **THEN** the check `no-preamble` fails
