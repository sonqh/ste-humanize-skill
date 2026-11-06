# skill-contract (delta)

## ADDED Requirements

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
