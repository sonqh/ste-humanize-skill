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
`SKILL.md` SHALL require the text and nothing else as output. It SHALL permit three lines after the text, each only when there is something to report. `Kept as-is:` names a longer phrase kept on purpose. `Cut candidates:` names a part of a Rewrite that does not serve the reader. `Reader:` names a reader that the writer chose, and SHALL appear only when the request does not name the reader. It SHALL forbid a preamble before the text.

#### Scenario: SCN-SKILL-003-1 Format section
- **WHEN** the test reads the `## Output format` section
- **THEN** it contains `Kept as-is:`, `Cut candidates:`, `Reader:`, and the phrase `nothing else`

#### Scenario: SCN-SKILL-003-2 Reader line
- **WHEN** the test reads `## Output format` and `## Reader first`
- **THEN** the first contains `only when the request does not name the reader`, and the second tells the writer to add no `Reader:` line when the request names the reader

### Requirement: REQ-SKILL-004 Size, front page, and export
`SKILL.md` SHALL stay under 1900 words. `README.md` SHALL lint at baseline 0 with both scripts and with `lint.py`. It SHALL open with one sentence of value and SHALL hold no `## Develop` section. The full before and after table SHALL live in `examples/before-after.md`. `.gitattributes` SHALL mark the maintainer folders `export-ignore`. `git archive` of HEAD then holds no `openspec/`, `tests/`, `evals/`, `.ctx/`, or `.claude/`.

#### Scenario: SCN-SKILL-004-1 Word cap
- **WHEN** the test counts the words of `SKILL.md`
- **THEN** the count is under 1900

#### Scenario: SCN-SKILL-004-2 README lints clean
- **WHEN** `python3 scripts/lint.py README.md` runs
- **THEN** it exits 0

#### Scenario: SCN-SKILL-004-3 Clean archive
- **WHEN** `git archive HEAD | tar -t` runs
- **THEN** the list has `SKILL.md`, `references/`, `scripts/`, `examples/`, and no `openspec/`, `tests/`, `evals/`, `.claude/`

### Requirement: REQ-SKILL-005 Newcomer shape, captions, and numbers
`references/doc-shapes.md` SHALL hold a section `## A page for a newcomer` with a numbered list of five parts. The order: the base thing, the problem, what the tool does, proof, how to try it. The section SHALL give the caption rule. A caption for a clip or screenshot states what the reader sees, then why it matters. It does not repeat the command. `SKILL.md` SHALL name that file. `## Boundaries` in `SKILL.md` SHALL say that a number needs a scale the reader has.

#### Scenario: SCN-SKILL-005-1 Section and order
- **WHEN** the test reads the `## A page for a newcomer` section of `references/doc-shapes.md`
- **THEN** it holds a list of five numbered items and the first names the base thing and the fifth names how to try it

#### Scenario: SCN-SKILL-005-2 Caption rule
- **WHEN** the test reads that section
- **THEN** it contains `what the reader sees` and `does not repeat the command`

#### Scenario: SCN-SKILL-005-3 Numbers need a scale
- **WHEN** the test reads `## Boundaries` in `SKILL.md`
- **THEN** it contains `scale the reader has`

### Requirement: REQ-SKILL-006 Audience fit
`references/human.md` SHALL hold a section `## Audience fit` for Human mode. The writer SHALL find what the reader already knows first. The writer SHALL keep an identifier only when the reader needs it for a task, and SHALL apply this test to appendices. The writer SHALL verify claims against source code and SHALL use meaningful links. Precedence item 1 in `SKILL.md` SHALL keep every condition and exception. Bullets SHALL group the sentences of one event.

#### Scenario: SCN-SKILL-006-1 Reader first
- **WHEN** the test reads `## Audience fit` in `references/human.md`
- **THEN** it contains `Human mode`, `already know`, and `complete a task`

#### Scenario: SCN-SKILL-006-2 Appendices
- **WHEN** the test reads `## Audience fit` in `references/human.md`
- **THEN** it contains `appendices` and `collapsed sections`

#### Scenario: SCN-SKILL-006-3 Source and links
- **WHEN** the test reads `## Audience fit` in `references/human.md`
- **THEN** it contains `against the source code` and `link text`

#### Scenario: SCN-SKILL-006-4 Conditions survive and identifiers stay exact
- **WHEN** the test reads item 1 of the precedence list in `SKILL.md` and `## Technical terms and other languages` in `references/terms.md`
- **THEN** item 1 contains `condition` and `exception`, and the terms section contains `Audience fit` and `Strict mode`

#### Scenario: SCN-SKILL-006-5 One event per bullet
- **WHEN** the test reads `## Shape: fit the content` in `SKILL.md`
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

### Requirement: REQ-SKILL-008 Two tasks
`SKILL.md` SHALL define exactly two tasks under a `## Two tasks` header: `Rewrite` and `Write`. In a Rewrite the source is the truth. The writer SHALL report a part the reader does not need as a cut candidate and SHALL NOT remove it. In a Write the reader brief decides the content. A Write SHALL still include every condition, exception, and limit of a behavior it describes, and every safety condition. Precedence item 1 SHALL name the Write task.

#### Scenario: SCN-SKILL-008-1 Header and names
- **WHEN** the test reads the `## Two tasks` section
- **THEN** the bold labels are `Rewrite` and `Write` and no third label

#### Scenario: SCN-SKILL-008-2 Rewrite keeps the source
- **WHEN** the test reads the `## Two tasks` section
- **THEN** it contains `Cut candidates:` and `source is the truth`

#### Scenario: SCN-SKILL-008-3 Limits of a Write
- **WHEN** the test reads the `## Two tasks` section and item 1 of the precedence list
- **THEN** the section contains `safety condition` and `exception`, and item 1 contains `Write task`

### Requirement: REQ-SKILL-009 Reader first
`SKILL.md` SHALL hold a section `## Reader first`. It SHALL give a reader brief as a numbered list of three questions. They ask who reads, what the reader knows, and what the reader does next. It SHALL require the answer in the first sentence. It SHALL tell the writer to stop when the reader can act. It SHALL name `references/doc-shapes.md` for the usual reader of each kind of page. That file SHALL put the first task before the reference. Process step 1 SHALL name the reader brief.

#### Scenario: SCN-SKILL-009-1 Brief of three questions
- **WHEN** the test reads the `## Reader first` section
- **THEN** it holds a numbered list of three items and contains `reader brief`

#### Scenario: SCN-SKILL-009-2 Answer first and stop rule
- **WHEN** the test reads the `## Reader first` section
- **THEN** it contains `Answer first` and `reader can act`

#### Scenario: SCN-SKILL-009-3 Kinds of page
- **WHEN** the test reads the `## Reader first` section and `references/doc-shapes.md`
- **THEN** the section names the file. The file has a table row for each of these: README, how-to guide, reference page, design note, PR description, runbook

#### Scenario: SCN-SKILL-009-4 Process names the brief
- **WHEN** the test reads step 1 of `## Process`
- **THEN** it contains `reader brief` and `task`

#### Scenario: SCN-SKILL-009-5 First task before the reference
- **WHEN** the test reads `references/doc-shapes.md`
- **THEN** it contains `The first task comes before the reference`

### Requirement: REQ-SKILL-010 Shape fits the content
`SKILL.md` SHALL hold a section `## Shape: fit the content` and no section `## Shape: bullets first`. The section SHALL hold a table from a kind of content to a shape. The table SHALL cover bullets, a numbered list, a table, and prose. The section SHALL name three signs of a wrong shape. They are a paragraph of more than 6 sentences, a sentence that lists 5 or more items, and a sentence that walks through steps. It SHALL tell the writer to keep reasoning in prose.

#### Scenario: SCN-SKILL-010-1 Table of shapes
- **WHEN** the test reads the `## Shape: fit the content` section
- **THEN** it holds a table with the cells `Bullets`, `Numbered list`, `Table`, and a cell that starts with `Prose`

#### Scenario: SCN-SKILL-010-2 Signs
- **WHEN** the test reads that section
- **THEN** it contains `more than 6 sentences` and `5 or more items`

#### Scenario: SCN-SKILL-010-3 Reasoning stays prose
- **WHEN** the test reads that section and the list of `## ` headers
- **THEN** the section contains `Do not cut reasoning into bullets`, and no header reads `Shape: bullets first`

### Requirement: REQ-SKILL-011 Route table
`SKILL.md` SHALL hold a section `## What to read` with a table from a case to a file in `references/`. The table SHALL name every file in `references/` and no other file. Process step 1 SHALL name that section. `references/human.md`, `references/terms.md`, and `references/doc-shapes.md` SHALL say in their first lines when to read them. A rule that moved to a reference file SHALL have no section of its own in `SKILL.md`.

#### Scenario: SCN-SKILL-011-1 Every reference is routed
- **WHEN** the test reads the table in `## What to read` and lists `references/`
- **THEN** the two sets of file names are equal

#### Scenario: SCN-SKILL-011-2 No dead reference
- **WHEN** the test reads each path under `references/` or `scripts/` that `SKILL.md` or a reference file names in a code span
- **THEN** each path exists

#### Scenario: SCN-SKILL-011-3 Each file says when to read it
- **WHEN** the test reads the first four lines of `references/human.md`, `references/terms.md`, and `references/doc-shapes.md`
- **THEN** each holds `Read this file when`

#### Scenario: SCN-SKILL-011-4 One home for each rule
- **WHEN** the test reads the `## ` headers of `SKILL.md` and step 1 of `## Process`
- **THEN** no header reads `Voice`, `Audience fit`, `Humanizer patterns`, or `Technical terms and other languages`, no header appears two times, and step 1 contains `What to read`

### Requirement: REQ-SKILL-012 Page guides
`references/doc-shapes.md` SHALL hold a section `## Reader questions` with a method of six numbered steps and a test of the title, the first paragraph, and the headings. `references/page-guides.md` SHALL hold a guide for a README, an ADR, and a technical proposal. Each guide SHALL name its readers, list their questions in order, and end with a test. `SKILL.md` SHALL let a Rewrite move a part and remove none.

#### Scenario: SCN-SKILL-012-1 Reader questions
- **WHEN** the test reads `## Reader questions` in `references/doc-shapes.md`
- **THEN** it holds six numbered steps and contains `cut candidate` and `first paragraph, and the headings`

#### Scenario: SCN-SKILL-012-2 Three guides
- **WHEN** the test reads `## README`, `## ADR`, and `## Technical proposal` in `references/page-guides.md`
- **THEN** each one contains `Readers:`, six or more numbered questions, and a line that starts with `Test:`

#### Scenario: SCN-SKILL-012-3 Table rows and the template rule
- **WHEN** the test reads `references/doc-shapes.md`
- **THEN** the table has a row `ADR` and a row `Technical proposal`, and the file contains `keep its headings and their order`

#### Scenario: SCN-SKILL-012-4 The skill names the questions
- **WHEN** the test reads `## Reader first`, `## Two tasks`, and `## What to read` in `SKILL.md`
- **THEN** the first contains `questions the reader brings`. The second contains `A Rewrite may move a part` and `removes none`. The third names a Rewrite of a whole page and the three kinds of page

### Requirement: REQ-SKILL-013 One pin of the spec engine
`scripts/specctx.sh` SHALL name the spec-ctx version in one line `SPECCTX_VERSION=<semver>` and SHALL run `npx -y spec-ctx@$SPECCTX_VERSION`. The hooks, `scripts/ci-local.sh`, and the CI workflow SHALL run spec-ctx through that script. No other tracked file outside the history folders SHALL name a spec-ctx version. Every gate SHALL lint one list of markdown globs.

#### Scenario: SCN-SKILL-013-1 One pin
- **WHEN** the test reads `scripts/specctx.sh`
- **THEN** it holds one `SPECCTX_VERSION` line with a semver value, and the `exec` line names `spec-ctx@$SPECCTX_VERSION`

#### Scenario: SCN-SKILL-013-2 No second pin
- **WHEN** the test reads the tracked files outside `openspec/changes/archive/`, `.ctx/evidence/`, `docs/verification/`, `docs/releases/`, and `evals/runs/`
- **THEN** only `scripts/specctx.sh` holds `spec-ctx@` and a digit, and each spec-ctx call in `.githooks/`, `scripts/ci-local.sh`, and `.github/workflows/ci.yml` goes through `scripts/specctx.sh`

#### Scenario: SCN-SKILL-013-3 One markdown list
- **WHEN** the test reads `[gate] markdown` in `spec-ctx.toml` and the markdown globs in `.githooks/pre-commit`, `scripts/ci-local.sh`, and `.github/workflows/ci.yml`
- **THEN** the four lists are equal

### Requirement: REQ-SKILL-014 One pin of OpenSpec and the stock schema
`scripts/openspec.sh` SHALL name the OpenSpec version in one line `OPENSPEC_VERSION=<semver>` and SHALL run `npx -y @fission-ai/openspec@$OPENSPEC_VERSION`. `[gate] openspec` in `spec-ctx.toml` SHALL run that script. No other tracked file outside the history folders SHALL name an OpenSpec version. `openspec/config.yaml` SHALL name the stock schema `spec-driven`.

#### Scenario: SCN-SKILL-014-1 One OpenSpec pin
- **WHEN** the test reads `scripts/openspec.sh` and `[gate] openspec` in `spec-ctx.toml`
- **THEN** the script holds one `OPENSPEC_VERSION` line with a semver value, its `exec` line names `@fission-ai/openspec@$OPENSPEC_VERSION`, and `[gate] openspec` is `bash scripts/openspec.sh`

#### Scenario: SCN-SKILL-014-2 No second OpenSpec pin
- **WHEN** the test reads the tracked files outside the history folders of SCN-SKILL-013-2 and outside the spec-ctx skill copies `.claude/skills/specctx-*` and `.agents/skills/specctx-*`
- **THEN** no file holds `@fission-ai/openspec@` followed by a digit or by `latest`

#### Scenario: SCN-SKILL-014-3 Stock schema
- **WHEN** the test reads `openspec/config.yaml` and the list of tracked files
- **THEN** the schema is `spec-driven`, no tracked file is under `openspec/schemas/`, and `openspec/templates/spec-driven-ids/` holds `spec.md` and `tasks.md`
