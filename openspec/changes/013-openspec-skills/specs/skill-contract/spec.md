## ADDED Requirements

### Requirement: REQ-SKILL-015 OpenSpec skills from the pinned version
Each OpenSpec skill in `.agents/skills/openspec-*` SHALL record `generatedBy` equal to `OPENSPEC_VERSION` of `scripts/openspec.sh`. Each `.claude/skills/openspec-*` entry SHALL be a symlink to the folder of the same name in `.agents/skills/`. The repository SHALL hold no `.claude/commands/opsx/` folder, because OpenSpec 2.0 installs skills only.
Refs: REQ-SKILL-014

#### Scenario: SCN-SKILL-015-1 Skills match the pin
- **WHEN** the test reads each `.agents/skills/openspec-*/SKILL.md` and `scripts/openspec.sh`
- **THEN** at least one skill exists, and each skill records `generatedBy` equal to `OPENSPEC_VERSION`

#### Scenario: SCN-SKILL-015-2 One copy of each skill
- **WHEN** the test reads each `.claude/skills/openspec-*` entry
- **THEN** each entry is a symlink to `../../.agents/skills/` and the folder of the same name, and each `.agents/skills/openspec-*` folder has such an entry

#### Scenario: SCN-SKILL-015-3 No opsx commands
- **WHEN** the test reads the list of tracked files
- **THEN** no tracked file is under `.claude/commands/opsx/`
