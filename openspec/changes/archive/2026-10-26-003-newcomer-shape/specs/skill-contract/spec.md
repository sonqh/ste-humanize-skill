# skill-contract (delta)

## MODIFIED Requirements

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

## ADDED Requirements

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
