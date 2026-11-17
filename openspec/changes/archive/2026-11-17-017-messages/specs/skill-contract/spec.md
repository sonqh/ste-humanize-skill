# skill-contract (delta)

## ADDED Requirements

### Requirement: REQ-SKILL-021 Messages to users and customers
`references/messages.md` SHALL hold the rules for a message to a user or a customer. The rules SHALL cover the state of the reader, the order of a reply, the length by channel, promises, and bad news. It SHALL have a section for English and one for Vietnamese. `SKILL.md` SHALL route a message to it and SHALL stay under 1900 words.
Refs: REQ-SKILL-008, REQ-SKILL-011, REQ-SKILL-018

#### Scenario: SCN-SKILL-021-1 Order and promises
- **WHEN** the test reads `references/messages.md`
- **THEN** it contains `upset`, a numbered order of a reply, `chat`, `email`, `Missing:`, and `promise`

#### Scenario: SCN-SKILL-021-2 English
- **WHEN** the test reads `## English` in `references/messages.md`
- **THEN** it contains `you'll`, `can't`, and `unfortunately`

#### Scenario: SCN-SKILL-021-3 Vietnamese
- **WHEN** the test reads `## Vietnamese` in `references/messages.md`
- **THEN** it contains `anh/chị`, `quý khách`, `Dạ`, and `rất tiếc vì sự bất tiện này`

#### Scenario: SCN-SKILL-021-4 Route, shapes, and cap
- **WHEN** the test reads `## What to read` in `SKILL.md`, the table in `references/doc-shapes.md`, and counts the words of `SKILL.md`
- **THEN** a row names `references/messages.md`, the table has the rows `Support reply` and `Notice to customers`, and the count is under 1900
