# eval Specification

## Purpose
How the project measures a text that an agent wrote with the skill. Fixtures hold the task and the checks. A scorer with no model call applies the checks.

## Requirements

### Requirement: REQ-EVAL-001 Fixtures
Each file in `evals/fixtures/` SHALL be one JSON object with the keys `id`, `mode`, `task`, `request`, `input`, and `checks`. The `id` SHALL equal the file name without `.json`. The loader SHALL reject an unknown mode, an unknown task, an unknown check, and a bad pattern. The set SHALL hold 6 or more fixtures. It SHALL cover both modes and both tasks. It SHALL hold one fixture that expects bullets and one that expects prose.

#### Scenario: SCN-EVAL-001-1 Set loads and covers the cases
- **WHEN** the test loads every fixture
- **THEN** it gets 6 or more, with both modes, both tasks, a `bullets` shape, and a `prose` shape

#### Scenario: SCN-EVAL-001-2 Bad fixture
- **WHEN** a fixture holds an unknown check, an unknown mode, or an `id` that differs from its file name
- **THEN** the loader raises an error

### Requirement: REQ-EVAL-002 Scorer
`evals/eval.py score DIR` SHALL read `DIR/<id>.md` for each fixture and apply its checks. The checks SHALL cover kept facts, omitted names, the answer in the first sentence, a word limit, the shape, and hard lint findings. The scorer SHALL call no model and no network. The same output SHALL get the same score. The run SHALL exit 0 when all checks pass, 1 when a check fails, and 2 on a usage error. `eval.py prompt` SHALL print a runner prompt that names no check.

#### Scenario: SCN-EVAL-002-1 Good output
- **WHEN** an output meets each check of its fixture
- **THEN** no check fails

#### Scenario: SCN-EVAL-002-2 Bad output
- **WHEN** an output opens with a preamble, drops a fact, keeps a forbidden name, and has the wrong shape
- **THEN** each of those checks fails by name

#### Scenario: SCN-EVAL-002-3 Same score
- **WHEN** the scorer reads the same output two times
- **THEN** both results are equal

#### Scenario: SCN-EVAL-002-4 Commands and exit codes
- **WHEN** the test runs `list`, `prompt`, and `score`
- **THEN** `list` exits 0, and `prompt` prints the path of `SKILL.md` and no check. An unknown fixture or a missing folder exits 2. An empty folder exits 1 with `missing output`
