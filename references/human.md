# Human mode: voice, audience fit, and the AI tells

Read this file when the mode is Human. It adds to the rules in `SKILL.md`. It does not apply in Strict mode.

## Voice

When the user gives a writing sample, match its sentence length, word choice, punctuation, and openings. The sample overrides the dash rule: if it uses dashes, keep them at the same rate.

Without a sample, take the voice from the text type. A design note or a reply keeps the writer's opinion and specific details. A reference page stays neutral. Keep what carries the writer's voice unless it hurts the meaning: an unusual detail, mixed feelings stated plainly, a real aside, a first-person choice the writer can explain.

## Audience fit

Apply this section in Human mode only. The reader brief says who reads the text and what they already know. Choose the technical details from it. If you cannot tell who reads it, keep the identifiers. A contributor who changes the code, a user of the feature, and a reviewer of a decision need different details.

- Explain behavior, examples, conditions, and limits in terms the reader already has. Say what the feature does, when it does it, and where it stops.
- Keep a file name, function name, or internal identifier only when the reader needs it to complete a task. Examples of such a task: run a command, set a config key, open the code to change it, or search a log.
- Always keep a command, flag, config key, or error string that the reader must type or match. Keep it exact.
- Apply the same test to appendices and collapsed sections. A reader who opens one reads every line in it. A code map for readers who never open the code serves no reader need.
- When you have the code, verify each claim against the source code. Then explain the behavior in plain language. Add a source link for traceability. The link text names what the reader finds there, for example "where retries stop". Do not use the file path as link text. Do not invent a link or a claim that you cannot verify.
- Simplify the explanation. Keep the behavior exact. Every condition and exception in the source survives the rewrite.

Audience fit changes three rules of `SKILL.md`:

- Precedence item 1. Audience fit may drop a source-level detail the reader does not need, such as a file name.
- File mode. You may remove an identifier or a code map from the prose when it fails audience fit.
- Boundaries. You may explain behavior that you verified in the source code, and you may link to that code.

## The AI tells

Remove these habits. Patterns 1 to 5 in `references/ai-tells.md` justify an edit on one sighting. A pattern marked *weak alone* there needs company.

- Staging: not X but Y, one-line closers, deep-sounding sayings, run-ups, forced triads, dashes as glue.
- Inflation: stock AI words, inflated significance, shallow -ing riders, sales language, borrowed authority.
- Decoration: bold labels, decorative headings.
- Chat leftovers: chatbot residue, writing about the document, text that explains again what the reader knows.

Read `references/ai-tells.md` when the source sounds like a chatbot, or when you cannot tell whether a phrase is a tell.

## Where STE and the humanizer disagree

| Topic | STE says | Humanizer says | This skill does |
|---|---|---|---|
| Hedges | Keep "may", "could". | Cut stacked qualifiers. | Keep one real hedge. "It could potentially possibly affect" becomes "It may affect". "May have failed" stays. |
| Flat tone | Literal and flat. | Keep opinions and specifics. | Keep an aside that adds information. |
| Punctuation | No semicolons. Em dash permitted. | No em or en dashes. | No semicolons, no dashes. Use a period, comma, colon, or parentheses. |
| Word use | One word, one meaning, from a dictionary of 900 words. | No rule. | Treat the STE word rule as a direction: the plainest common word, used the same way every time. |
