# eval (delta)

## ADDED Requirements

### Requirement: REQ-EVAL-004 Missing trailer
The scorer SHALL read a line that starts with `Missing:` after the text as a trailer, the same as `Kept as-is:`, `Cut candidates:`, and `Reader:`. The `trailers` check SHALL fail when a `Missing:` line appears and the fixture does not permit it.
Refs: REQ-EVAL-002, REQ-SKILL-018

#### Scenario: SCN-EVAL-004-1 Permitted
- **WHEN** an output ends with a `Missing:` line and the fixture lists `Missing:` in `trailers`
- **THEN** the `trailers` check passes, and the line is not part of the body that the scorer lints

#### Scenario: SCN-EVAL-004-2 Not permitted
- **WHEN** an output ends with a `Missing:` line and the fixture does not list it
- **THEN** the `trailers` check fails and names `Missing:`
