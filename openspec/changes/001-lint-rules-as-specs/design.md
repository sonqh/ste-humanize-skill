# Design

## Context

This repo is small: one SKILL.md, two Python scripts, two reference files. The value of specs here is traceability, not planning. So the specs mirror the code tables one to one and the tests read those tables.

## Goals / Non-Goals

**Goals:**
- Every rule ID in both `RULES` tables appears in exactly one requirement and one test.
- `specctx check --strict` passes with zero baseline entries. A fresh project should start clean.
- No behavior change in the scripts. Selftest counts are identical before and after.

**Non-Goals:**
- Documenting the regex text itself. The requirement names the rule and gives examples. The regex is the implementation.

## Decisions

- One requirement per rule group, not per rule. `tells-lint` has nine hard and six advisory rules, so two requirements plus one for the CLI. Each scenario names one rule with its example from the selftest. Alternative: one requirement per rule. Rejected because fifteen requirements with one sentence each add IDs without adding meaning. Creates no ADR.
- Tests read the `RULES` table from the script and assert the spec's rule list equals the code's rule list. A rule added to the code without a scenario fails the test, which is the traceability the specs exist for. Creates no ADR.
- Code tags go on the `RULES` table line and the `main()` line of each script. Python comments `# REQ-...` are what the spec-ctx scanner reads. Creates no ADR.
- SKILL.md section headers for the contract get no ID. The IDs live in the spec and the tests grep the header text. Changing SKILL.md headers would change what users see for no gain. Creates no ADR.
- `spec-ctx.toml` scans `scripts/**` as code and `tests/**` as tests. Capability codes: `TELLS`, `STE`, `SKILL`. Creates no ADR.

## Risks / Trade-offs

- A selftest example may not be a clean minimal case for a scenario. Mitigation: the scenario quotes the example as is. Readability of the example is a later concern.
- Python unittest adds no dependency but needs `python3`, which the scripts already need.
