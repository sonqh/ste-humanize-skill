# skill-contract (delta)

## ADDED Requirements

### Requirement: REQ-SKILL-020 Tells of decision pages
`references/ai-tells.md` SHALL hold `## G. Decision pages` with the patterns 27 to 32. Each pattern SHALL have a line that starts with `Watch for:`, a line that starts with `Problem:`, and a before and after. `references/human.md`, `references/page-guides.md`, and `references/review.md` SHALL name `## G. Decision pages`. The route row in `SKILL.md` SHALL say 32 patterns.
Refs: REQ-SKILL-012, REQ-SKILL-019, REQ-TELLS-004

#### Scenario: SCN-SKILL-020-1 Six patterns
- **WHEN** the test reads `## G. Decision pages` in `references/ai-tells.md`
- **THEN** it holds the headings `### 27.` to `### 32.`, and each pattern has `Watch for:`, `Problem:`, `Before:`, and `After:`

#### Scenario: SCN-SKILL-020-2 Pointers
- **WHEN** the test reads `references/human.md`, `references/page-guides.md`, and `references/review.md`
- **THEN** each one contains `G. Decision pages`

#### Scenario: SCN-SKILL-020-3 Route row
- **WHEN** the test reads `## What to read` in `SKILL.md`
- **THEN** the row of `references/ai-tells.md` says `32 patterns`, and `SKILL.md` has fewer than 1900 words
