# skill-contract (delta)

## ADDED Requirements

### Requirement: REQ-SKILL-016 Work not built yet
`references/page-guides.md` SHALL hold `## Work not built yet`. It SHALL name four kinds of claim: measured, estimate, target, and assumption. It SHALL mark a gap with `TBD`, an owner, and a date, and SHALL forbid a number that the material does not give. `SKILL.md` SHALL route a page about work not built yet to `references/page-guides.md`.
Refs: REQ-SKILL-012

#### Scenario: SCN-SKILL-016-1 Four kinds of claim
- **WHEN** the test reads `## Work not built yet` in `references/page-guides.md`
- **THEN** it contains `measured`, `estimate`, `target`, `assumption`, and `TBD`

#### Scenario: SCN-SKILL-016-2 No invented number
- **WHEN** the test reads `## Work not built yet`
- **THEN** it contains `Do not invent a number` and `Open questions`

#### Scenario: SCN-SKILL-016-3 Route
- **WHEN** the test reads `## What to read` in `SKILL.md`
- **THEN** a row contains `not built yet` and names `references/page-guides.md`

### Requirement: REQ-SKILL-017 Design doc and Proposed ADR
`references/page-guides.md` SHALL hold `## Design doc` with `Readers:`, six or more numbered questions, and a `Test:` line. The questions SHALL cover non-goals, the option to do nothing, and open questions. The ADR guide SHALL cover the status Proposed and SHALL name the criteria before the options. `references/doc-shapes.md` SHALL have a row `Design doc`.
Refs: REQ-SKILL-012

#### Scenario: SCN-SKILL-017-1 Design doc guide
- **WHEN** the test reads `## Design doc` in `references/page-guides.md`
- **THEN** it contains `Readers:`, six or more numbered questions, a line that starts with `Test:`, `Non-goals`, `do nothing`, and `open questions`

#### Scenario: SCN-SKILL-017-2 Proposed ADR
- **WHEN** the test reads `## ADR` in `references/page-guides.md`
- **THEN** it contains `Proposed` and `criteria`, and `criteria` comes before `What else did we look at`

#### Scenario: SCN-SKILL-017-3 Table row
- **WHEN** the test reads the table in `references/doc-shapes.md`
- **THEN** a row starts with `Design doc`

### Requirement: REQ-SKILL-018 Missing trailer
`## Output format` in `SKILL.md` SHALL permit a fourth line, `Missing:`, in a Write task. The line SHALL name each input that the reader needs and the material does not give. `SKILL.md` SHALL stay under 1900 words.
Refs: REQ-SKILL-003, REQ-SKILL-004

#### Scenario: SCN-SKILL-018-1 Four trailers
- **WHEN** the test reads `## Output format` in `SKILL.md`
- **THEN** it contains `Kept as-is:`, `Cut candidates:`, `Reader:`, and `Missing:`

#### Scenario: SCN-SKILL-018-2 Write only
- **WHEN** the test reads the `Missing:` bullet
- **THEN** it contains `Write task` and `does not give`

#### Scenario: SCN-SKILL-018-3 Cap
- **WHEN** the test counts the words of `SKILL.md`
- **THEN** the count is under 1900
