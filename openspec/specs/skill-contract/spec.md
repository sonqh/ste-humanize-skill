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
`SKILL.md` SHALL stay under 2400 words. `README.md` SHALL lint at baseline 0 with both scripts and with `lint.py`. It SHALL open with one sentence of value and SHALL hold no `## Develop` section. The full before and after table SHALL live in `examples/before-after.md`. `.gitattributes` SHALL mark the maintainer folders `export-ignore`. `git archive` of HEAD then holds no `openspec/`, `tests/`, `.ctx/`, or `.claude/`.

#### Scenario: SCN-SKILL-004-1 Word cap
- **WHEN** the test counts the words of `SKILL.md`
- **THEN** the count is under 2400

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

### Requirement: REQ-SKILL-006 Audience fit
`SKILL.md` SHALL hold a section `## Audience fit` for Human mode. The writer SHALL find what the reader already knows first. The writer SHALL keep an identifier only when the reader needs it for a task, and SHALL apply this test to appendices. The writer SHALL verify claims against source code and SHALL use meaningful links. Precedence item 1 SHALL keep every condition and exception. Bullets SHALL group the sentences of one event.

#### Scenario: SCN-SKILL-006-1 Reader first
- **WHEN** the test reads `## Audience fit`
- **THEN** it contains `Human mode`, `already know`, and `complete a task`

#### Scenario: SCN-SKILL-006-2 Appendices
- **WHEN** the test reads `## Audience fit`
- **THEN** it contains `appendices` and `collapsed sections`

#### Scenario: SCN-SKILL-006-3 Source and links
- **WHEN** the test reads `## Audience fit`
- **THEN** it contains `against the source code` and `link text`

#### Scenario: SCN-SKILL-006-4 Conditions survive and identifiers stay exact
- **WHEN** the test reads item 1 of `## Order of precedence when rules conflict` and `## Technical terms and other languages`
- **THEN** item 1 contains `condition` and `exception`, and the terms section contains `Audience fit` and `Strict mode`

#### Scenario: SCN-SKILL-006-5 One event per bullet
- **WHEN** the test reads `## Shape: bullets first`
- **THEN** it contains `one event` and `Independent rules`

### Requirement: REQ-SKILL-007 Plugin marketplace
The repo SHALL hold `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`. The plugin name SHALL equal the `name` in the `SKILL.md` front matter. The marketplace SHALL list that plugin with source `./`. The plugin version SHALL equal the `version` in the `SKILL.md` front matter. `claude plugin validate --strict .` SHALL pass when the CLI is present.

#### Scenario: SCN-SKILL-007-1 Names match
- **WHEN** the test reads both manifests and the `SKILL.md` front matter
- **THEN** the plugin name, the marketplace entry name, and the skill name are equal, and the entry source is `./`

#### Scenario: SCN-SKILL-007-2 Versions match
- **WHEN** the test reads `plugin.json` and the `SKILL.md` front matter
- **THEN** both versions are equal and follow semver

#### Scenario: SCN-SKILL-007-3 Validate passes
- **WHEN** the `claude` CLI is on the path and the test runs `claude plugin validate --strict .`
- **THEN** it exits 0
