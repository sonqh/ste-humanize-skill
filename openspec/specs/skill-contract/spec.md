# skill-contract Specification

## Purpose
What `SKILL.md` promises an agent that loads it. Tests read the file and check the promise is still there.

## Requirements

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
`SKILL.md` SHALL require the rewritten text and nothing else as output, plus at most one `Kept as-is:` line when a longer phrase was kept on purpose. It SHALL forbid a preamble before the rewrite.

#### Scenario: SCN-SKILL-003-1 Format section
- **WHEN** the test reads the `## Output format` section
- **THEN** it contains `Kept as-is:` and the phrase `nothing else`

### Requirement: REQ-SKILL-004 Size, front page, and export
`SKILL.md` SHALL stay under 2000 words. `README.md` SHALL lint at baseline 0 with both scripts and with `lint.py`. It SHALL open with one sentence of value and SHALL hold no `## Develop` section. The full before and after table SHALL live in `examples/before-after.md`. `.gitattributes` SHALL mark the maintainer folders `export-ignore`. `git archive` of HEAD then holds no `openspec/`, `tests/`, `.ctx/`, or `.claude/`.

#### Scenario: SCN-SKILL-004-1 Word cap
- **WHEN** the test counts the words of `SKILL.md`
- **THEN** the count is under 2000

#### Scenario: SCN-SKILL-004-2 README lints clean
- **WHEN** `python3 scripts/lint.py README.md` runs
- **THEN** it exits 0

#### Scenario: SCN-SKILL-004-3 Clean archive
- **WHEN** `git archive HEAD | tar -t` runs
- **THEN** the list has `SKILL.md`, `references/`, `scripts/`, `examples/`, and no `openspec/`, `tests/`, `.claude/`

### Requirement: REQ-SKILL-005 Newcomer shape, captions, and numbers
`SKILL.md` SHALL hold a section `## Shape: a page for a newcomer` with a numbered list of five parts. The order: the base thing, the problem, what the tool does, proof, how to try it. The section SHALL give the caption rule. A caption for a clip or screenshot states what the reader sees, then why it matters. It does not repeat the command. `## Boundaries` SHALL say that a number needs a scale the reader has.

#### Scenario: SCN-SKILL-005-1 Section and order
- **WHEN** the test reads the `## Shape: a page for a newcomer` section
- **THEN** it holds a list of five numbered items and the first names the base thing and the fifth names how to try it

#### Scenario: SCN-SKILL-005-2 Caption rule
- **WHEN** the test reads that section
- **THEN** it contains `what the reader sees` and `does not repeat the command`

#### Scenario: SCN-SKILL-005-3 Numbers need a scale
- **WHEN** the test reads `## Boundaries`
- **THEN** it contains `scale the reader has`
