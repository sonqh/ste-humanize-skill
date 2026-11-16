# eval (delta)

## ADDED Requirements

### Requirement: REQ-EVAL-005 Review fixtures
The loader SHALL accept the task `Review` next to `Rewrite` and `Write`. The set SHALL hold 2 or more fixtures with the task `Review`. The scorer SHALL apply the same checks to a review as to a text.
Refs: REQ-EVAL-001, REQ-SKILL-019

#### Scenario: SCN-EVAL-005-1 Task accepted
- **WHEN** a fixture has the task `Review`
- **THEN** the loader accepts it, and still rejects an unknown task

#### Scenario: SCN-EVAL-005-2 Set holds reviews
- **WHEN** the test loads every fixture
- **THEN** 2 or more have the task `Review`
