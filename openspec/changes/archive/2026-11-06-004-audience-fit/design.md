# Design

## Decisions

- 004/D1 The new section `## Audience fit` sits after `## Voice` and before `## Shape: bullets first`. The reader decides the content before the shape decides the layout. The section applies in Human mode only. When the writer cannot tell who reads the text, the identifiers stay. Six bullets follow. They cover terms the reader has, the task test for identifiers, and commands and error strings that always stay. They also cover appendices, source verification with meaningful link text, and conditions that survive.
- 004/D2 Precedence item 1 changes from "every fact survives" to "every fact the reader needs survives, and so does every condition, exception, qualifier, and hedge". Without this change, item 1 outranks audience fit and keeps every file name. The order of the five items stays.
- 004/D3 The technical terms rule keeps two jobs apart. It protects an identifier that stays: no translation, no paraphrase. `## Audience fit` decides whether a source-level identifier stays. Strict mode keeps every identifier, because its reader is a tool or an agent that needs the exact name.
- 004/D4 "One idea per bullet" becomes "one idea or one event per bullet". Sentences of one event stay in one bullet. Independent rules get separate bullets.
- 004/D5 Process step 1 names the reader in Human mode and adds exceptions to what must survive. File mode allows the removal of an identifier or a code map from prose. It never changes a code block, command, YAML front matter, data, or link target. Its summary lists each removed identifier.
- 004/D6 The cap moves to 2400 words. The new text is about 400 words. The file has 2347 words after the change.
- 004/D7 `## Boundaries` gets one exception. In Human mode, the writer may explain behavior verified in the source code and link to it. Without it, the rule against an added mechanism or name blocks the verification bullet.
- 004/D8 An independent review found the Boundaries and File mode conflicts, a contrast tell, and a loose "relevant". This design holds the fixes. A `Removed:` output line was out of scope, because it changes REQ-SKILL-003.

## Risks / Trade-offs

- A writer can now drop a detail that a reader needs. The task test and the "every relevant condition and exception" line limit this. The writer must name the reader first.
- File mode can now remove a path from a user file. It removes only a detail that fails the task test, and it never edits one that stays.
- The cap has 53 words of room left. The next rule needs a trim or another raise.
- "Every condition and exception in the source" is stricter than the owner's "all relevant conditions". It matches precedence item 1 and leaves no room to drop a condition.
