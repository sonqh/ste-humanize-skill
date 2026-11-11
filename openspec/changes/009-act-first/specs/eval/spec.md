# eval (delta)

## ADDED Requirements

### Requirement: REQ-EVAL-003 Early check
A fixture MAY hold a check `early`: a list of items with a `pattern` and a number `within_words`. The check SHALL pass when the pattern starts before that word of the output. The scorer SHALL count every word of the output, headings and code too. An absent pattern SHALL fail the check. The loader SHALL reject an item with a missing key or a bad pattern.

#### Scenario: SCN-EVAL-003-1 Position of the pattern
- **WHEN** the pattern starts in the first words, starts after the limit, or is absent
- **THEN** the check passes in the first case and fails by name in the other two

#### Scenario: SCN-EVAL-003-2 Bad early check
- **WHEN** an item has no `within_words`, has a bad pattern, or is not an object
- **THEN** the loader raises an error
