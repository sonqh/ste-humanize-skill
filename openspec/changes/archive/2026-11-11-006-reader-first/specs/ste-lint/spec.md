# ste-lint (delta)

## ADDED Requirements

### Requirement: REQ-STE-004 Shape advisories
The linter SHALL report three advisory findings for each prose block. `long-paragraph` fires when a block has more than 6 sentences. `inline-list` fires when one sentence lists 5 or more items with commas and a last `and` or `or`. `buried-sequence` fires when a block holds 3 or more different sequence words. No shape finding SHALL fail the run. Each list item is its own block. Code is skipped.

#### Scenario: SCN-STE-004-1 Long paragraph
- **WHEN** a paragraph has 7 sentences
- **THEN** `long-paragraph` fires once with the sentence count in the match, and a paragraph of 6 sentences gets no finding

#### Scenario: SCN-STE-004-2 Inline list
- **WHEN** one sentence lists 5 items with commas and a last `and`
- **THEN** `inline-list` fires, and a sentence with 4 items gets no finding

#### Scenario: SCN-STE-004-3 Buried sequence
- **WHEN** a paragraph holds `first`, `then`, and `finally`
- **THEN** `buried-sequence` fires, and a numbered list with one sequence word in each item gets no finding

#### Scenario: SCN-STE-004-4 Advisory only
- **WHEN** a file holds only shape findings
- **THEN** the run exits 0, each finding has the level `advisory`, and `--disable long-paragraph` removes that finding
