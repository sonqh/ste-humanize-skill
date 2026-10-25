# lint-cli Specification

## Purpose
`scripts/lint.py` runs the tells linter and the STE linter in one command. It prints one format and one JSON shape. The pre-commit hook and the GitHub action call it.

## Requirements

### Requirement: REQ-LINT-001 One command and one format
`scripts/lint.py FILE...` SHALL run both rule sets and print one line per finding as `file:line:col rule [level] match`, sorted by file, line, column. Levels SHALL be `hard` or `advisory`. It SHALL accept `--baseline N`, `--disable <rules>`, `--only tells|ste`, and `--json`. It SHALL exit 1 when hard findings exceed the baseline, 2 on a usage error or empty input, else 0. Python 3 stdlib only.

#### Scenario: SCN-LINT-001-1 Both sources in one list
- **WHEN** a file has one `stock-word` tell and one `semicolon` STE finding
- **THEN** stdout has two lines in the one format, ordered by line, and the exit code is 1

#### Scenario: SCN-LINT-001-2 Only one source
- **WHEN** `--only ste` is given on that file
- **THEN** stdout has the `semicolon` line only

#### Scenario: SCN-LINT-001-3 Empty input
- **WHEN** `lint.py` runs with no file and empty stdin
- **THEN** it exits 2 and prints `no input`

### Requirement: REQ-LINT-002 JSON shape
`lint.py --json` SHALL print a list with one object per file. Each object SHALL have `file` and `findings`. Each finding SHALL have `rule`, `level`, `line`, `col`, `match`, and `source` with the value `tells` or `ste`. Nothing else SHALL go to stdout.

#### Scenario: SCN-LINT-002-1 Shape
- **WHEN** `--json` runs on a file with one finding from each source
- **THEN** stdout parses as a list with one object whose `findings` has two entries with the six keys, and `source` differs between them

### Requirement: REQ-LINT-003 Hook and action
`.pre-commit-hooks.yaml` SHALL define one hook `ste-humanize-lint` that runs `scripts/lint.py` on the staged markdown files. `action.yml` SHALL be a composite action with inputs `files` and `baseline` that runs `lint.py` on the matched files. The repository CI SHALL call the action on its own markdown.

#### Scenario: SCN-LINT-003-1 Hook id
- **WHEN** the test reads `.pre-commit-hooks.yaml`
- **THEN** it holds one hook with `id: ste-humanize-lint` and an `entry` that names `scripts/lint.py`

#### Scenario: SCN-LINT-003-2 Action inputs
- **WHEN** the test reads `action.yml`
- **THEN** `inputs` has `files` and `baseline` and `runs.using` is `composite`
