# skill-contract

## Purpose

What `SKILL.md` promises an agent that loads it. Tests read the file and check the promise is still there.

## ADDED Requirements

### Requirement: REQ-SKILL-001 Two modes
`SKILL.md` SHALL define exactly two modes under a `## Two modes` header: `Strict` for tool descriptions, error messages, and agent instructions, and `Human` for docs, READMEs, PR descriptions, and replies. Each mode SHALL say which rule set applies.

#### Scenario: SCN-SKILL-001-1 Header and names
- **WHEN** the test reads `SKILL.md`
- **THEN** the `## Two modes` section names `Strict` and `Human` and no third mode

### Requirement: REQ-SKILL-002 Precedence order
`SKILL.md` SHALL list the precedence when rules conflict, in this order: meaning, STE structure, voice, shape, brevity. The order SHALL appear as a numbered list under `## Order of precedence when rules conflict`.

#### Scenario: SCN-SKILL-002-1 Order
- **WHEN** the test extracts the numbered list under that header
- **THEN** the five items appear in that order

### Requirement: REQ-SKILL-003 Output format
`SKILL.md` SHALL require the rewrite alone as output, plus at most one `Kept as-is:` line when a longer phrase was kept on purpose. It SHALL forbid a preamble before the rewrite.

#### Scenario: SCN-SKILL-003-1 Format section
- **WHEN** the test reads the `## Output format` section
- **THEN** it contains `Kept as-is:` and the word `alone`
