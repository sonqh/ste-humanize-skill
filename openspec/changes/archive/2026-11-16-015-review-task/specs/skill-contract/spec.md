# skill-contract (delta)

## ADDED Requirements

### Requirement: REQ-SKILL-019 Review of a page
`references/review.md` SHALL hold the steps and the output of a review. The output SHALL open with a verdict. A table of the reader questions SHALL follow, with the columns Question, Answered, Where, and Gap. Then 7 or fewer other findings, and a lint line. A review SHALL change no text and add no fact. `SKILL.md` SHALL route a review to `references/review.md` and SHALL stay under 1900 words.
Refs: REQ-SKILL-008, REQ-SKILL-012, REQ-SKILL-016

#### Scenario: SCN-SKILL-019-1 Steps
- **WHEN** the test reads `## Steps` in `references/review.md`
- **THEN** it holds numbered steps and names `references/page-guides.md`, `## Reader questions`, and `## Work not built yet`

#### Scenario: SCN-SKILL-019-2 Output
- **WHEN** the test reads `## Output` in `references/review.md`
- **THEN** it contains `| Question | Answered | Where | Gap |`, `verdict`, `7 or fewer`, and `scripts/lint.py`

#### Scenario: SCN-SKILL-019-3 No rewrite
- **WHEN** the test reads `## Limits` in `references/review.md`
- **THEN** it contains `Do not rewrite` and `Do not add a fact`

#### Scenario: SCN-SKILL-019-4 Route and cap
- **WHEN** the test reads `## What to read` and counts the words of `SKILL.md`
- **THEN** a row names `review` and `references/review.md`, and the count is under 1900
