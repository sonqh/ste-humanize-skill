---
name: ste-humanize
description: "Write or rewrite English so a reader cannot misread it and still hears a person behind it. Starts from the reader: what they know and what they do next. Combines ASD-STE100 sentence discipline with AI-tell removal (no not-X-but-Y, no one-line closers, no dash glue, no stock AI words). Use to write or rewrite docs, READMEs, PR descriptions, replies, tool descriptions, error messages, and any prose written for a person. Triggers: write a doc, humanize, make this clear, plain rewrite, STE rewrite, remove AI tells. Not for fiction, marketing, or copy where voice is the point."
version: 0.4.0
license: MIT
---

# ste-humanize: clear enough for a machine, written for a person

This skill starts from the reader. Then it does two jobs in one pass. First it applies the structural rules of ASD-STE100, the controlled English that aerospace built so a maintenance step cannot be misread. Then it removes the habits that make text read as machine-written.

Keep what the source says. Do not drop a condition, a scope limit, or a hedge that carries real doubt.

## When to use this skill

Use it when you write or rewrite a document, README, design note, PR description, or reply for a person, or a tool description, error message, or instruction that another agent must parse. Use it when a draft reads dense, hedged, over-formatted, or like a chatbot. Do not use it for fiction, marketing, or any text where voice and persuasion are the point.

## Two modes

Pick the mode from the text type. Do not announce it unless the user asks for the rule table.

**Strict.** Tool descriptions, error messages, agent-to-agent instructions, procedures, safety text. Apply every STE rule below, including the word-use rules. From the humanizer side apply only chatbot residue and re-explaining what the reader knows. Voice does not matter here. A wrong reading does.

**Human.** READMEs, docs, design notes, PR descriptions, chat replies, status updates, anything a person reads. Apply the STE structural rules in full, treat the STE word-use rules as a direction, and apply the full humanizer pass. The reader should notice they understood it on the first read, not that a standard was applied.

## Two tasks

The mode sets the rules. The task sets what you may leave out. Pick the task from the request.

**Rewrite.** The user gives a text. The source is the truth. Keep every fact per precedence item 1. When the reader may not need an idea, do not remove it. Name it on a `Cut candidates:` line. The owner of the text decides.

**Write.** The user asks for a new text from notes, code, a diff, or the conversation. That material is input. The reader brief decides which parts go in. Three limits stay:

- A condition, exception, or limit of a behavior you describe always goes in.
- A safety condition always goes in.
- No fact goes in that the material does not give and that you did not verify.

In Strict mode the reader is a tool or an agent, and it cannot ask. When in doubt, keep the detail.

## Reader first

Before the first sentence, answer a reader brief. Do not print it.

1. Who reads this? Take the reader from the request, then from the kind of page. `references/doc-shapes.md` lists the usual reader and the opening of each kind of page. Read it for a Write task.
2. What does the reader already know?
3. What does the reader do or decide after reading?

Then apply the brief:

- Answer first. The first sentence gives the conclusion, the decision, or the action the reader must take. Reasons and background come after it. Each section opens with its own point.
- Each part must help the reader with item 3. If it does not, leave it out of a Write. In a Rewrite it stays and becomes a cut candidate.
- Background the reader already has gets one clause or none.
- Stop when the reader can act. Leave out a template section that has nothing to say.
- If neither the request nor the kind of page tells you the reader, ask. If you cannot ask, choose the most likely reader and report it on a `Reader:` line.

## Order of precedence when rules conflict

1. Meaning. Every fact the reader needs survives, and so does every condition, exception, qualifier, and hedge in the source. Audience fit may drop a source-level detail the reader does not need, such as a file name. In a Write task, the reader brief decides which facts the reader needs.
2. Structure (STE). Short sentences, active voice, one instruction per sentence, no semicolons, no dropped words.
3. Voice (humanizer). No staging, no inflation, no decoration, no chatbot residue. Keep the writer's specific details and real asides.
4. Shape. The content picks the shape. Technical terms the reader needs stay as the field uses them.
5. Brevity. Shorter only when it does not cost 1 to 4.

Where the two sources disagree:

| Topic | STE says | Humanizer says | This skill does |
|---|---|---|---|
| Hedges | Keep "may", "could". | Cut stacked qualifiers. | Keep one real hedge. "It could potentially possibly affect" becomes "It may affect". "May have failed" stays. |
| Flat tone | Literal and flat. | Keep opinions and specifics. | Strict: flat. Human: keep an aside that adds information. |
| Punctuation | No semicolons. Em dash permitted. | No em or en dashes. | No semicolons, no dashes. Use a period, comma, colon, or parentheses. |

## STE structural rules

Apply these in both modes. Each one is mechanical: you can point at the word or mark that breaks it.

- Active voice. "The agent deletes the file." Not "The file is deleted.", unless the actor is unknown or irrelevant.
- No phrasal verbs. "Remove the panel." "Start the job." Not "Take off", "Spin up".
- One instruction per sentence. "Open the file. Read line 3." Not "Open the file and read line 3, then check if it matches."
- Sentence length. 20 words or fewer for instructions, 25 for description.
- No semicolons. Split into two sentences.
- Noun clusters. 3 words or fewer in one noun phrase.
- No dropped words. Keep subject, verb, and article. "Files not backed up will be lost" does not say which files.
- Keep modality. "The request may have failed." Not "The request failed." when the source said "may".
- Simple tenses. "We received the report." Not "We have received the report.", unless the compound form carries meaning. "The job has completed" (output is ready now) differs from "the job completed" (at some past time). Keep the compound form where it carries current relevance, and note the departure.
- Verb, not noun. "Analyze the log." Not "Perform an analysis of the log."
- One topic per paragraph, 6 sentences or fewer.
- Numbered list for 3 or more steps. Do not bury a sequence in one sentence.

STE word-use rules (one word, one meaning, one part of speech) depend on ASD's 900-word dictionary, which this skill does not reproduce. Choose the plainest common word and use it the same way every time. Do not claim dictionary compliance.

## Humanizer patterns

`references/ai-tells.md` holds the 26 patterns with before and after examples. Read it for a Human mode rewrite. Patterns 1 to 5 justify an edit on one sighting. A pattern marked *weak alone* needs company. In Strict mode apply only patterns 22 and 26. The groups:

- Staging: not X but Y, one-line closers, deep-sounding sayings, run-ups, forced triads, dashes as glue.
- Inflation: stock AI words, inflated significance, shallow -ing riders, sales language, borrowed authority.
- Decoration: bold labels, decorative headings.
- Chat leftovers: chatbot residue, writing about the document, re-explaining what the reader knows.

## Process

1. Pick the mode and the task. Answer the reader brief. For a Rewrite, read the whole text once and note every hedge, condition, and exception. These must survive. For a Write, list the points the reader needs, the answer first.
2. Run `python3 scripts/lint.py FILE` on the source or the draft for a mechanical first pass. It flags no hedges and checks no meaning.
3. Mark every finding, strongest first: staging and STE structure, then inflation, then word choice.
4. Write or rewrite paragraph by paragraph in short active sentences. Pick the shape per `## Shape: fit the content`. If a rewrite would drop a condition or upgrade a hedge to a fact, keep the longer phrasing and flag it.
5. Read the result aloud. Fix any sentence a reader could misread and any that still sounds like a chatbot.
6. Run the linter again. Advisory findings do not fail. Hard findings do, unless you can name the precision they protect.
7. If the input already complies, say so. Do not force edits onto clean text.

## Output format

**Default: the text and nothing else.** No preamble, no mode announcement, no count of changes, no closing offer.

Three permitted additions, each one line after the text. Omit a line when there is nothing to report.

- `Kept as-is:` when step 4 kept a longer phrasing on purpose. Name the phrase and the precision it protects.
- `Cut candidates:` in a Rewrite task, when a part does not help the reader. Name each part in a few words. Do not remove it.
- `Reader:` when you chose the reader yourself. Name the reader in one clause.

**On request: the rule table.** When the user asks to "show the diff", "explain the changes", or "which rules did it break", output this instead:

```markdown
| Rule | Original | Rewrite |
|---|---|---|
| Not X but Y | "It's not a tool, it's a mirror." | "The tool shows you your own habits." |
| Present perfect | "We have received your request." | "We received your request." |

Mode: Human. 9 findings.
```

Follow the table with one line on anything you did not change on purpose, and why.

**File mode.** When the user names a file, write only the final text to the file. Change prose only. In Human mode, you may also remove an identifier or a code map from the prose when it fails audience fit. Do not change a code block, command, YAML front matter, data, or link target. Then give a short summary that lists each identifier you removed, each cut candidate, and the reader you chose.

**Embedded mode.** When another task uses this skill for a document, PR, or commit message, return only the final text.

## Voice

When the user gives a writing sample, match its sentence length, word choice, punctuation, and openings. The sample overrides the dash rule: if it uses dashes, keep them at the same rate.

Without a sample, take the voice from the text type. A design note or a reply keeps the writer's opinion and specific details. A reference page or an error message stays neutral. Keep what carries the writer's voice unless it hurts the meaning: an unusual detail, mixed feelings stated plainly, a real aside, a first-person choice the writer can explain.

## Audience fit

Apply this section in Human mode only. The reader brief says who reads the text and what they already know. Choose the technical details from it. If you cannot tell who reads it, keep the identifiers. A contributor who changes the code, a user of the feature, and a reviewer of a decision need different details.

- Explain behavior, examples, conditions, and limits in terms the reader already has. Say what the feature does, when it does it, and where it stops.
- Keep a file name, function name, or internal identifier only when the reader needs it to complete a task. Examples of such a task: run a command, set a config key, open the code to change it, or search a log.
- Always keep a command, flag, config key, or error string that the reader must type or match. Keep it exact.
- Apply the same test to appendices and collapsed sections. A reader who opens one reads every line in it. A code map for readers who never open the code serves no reader need.
- When you have the code, verify each claim against the source code. Then explain the behavior in plain language. Add a source link for traceability. The link text names what the reader finds there, for example "where retries stop". Do not use the file path as link text. Do not invent a link or a claim that you cannot verify.
- Simplify the explanation. Keep the behavior exact. Every condition and exception in the source survives the rewrite.

## Shape: fit the content

The content picks the shape. A long paragraph is the first sign of a wrong shape.

| Content | Shape |
|---|---|
| 3 or more parallel parts: options, findings, risks, decisions, rules | Bullets |
| Steps in an order | Numbered list |
| Items that share the same attributes | Table |
| Conditions with different results | Bullets, one condition each |
| One line of reasoning, where each sentence needs the one before it | Prose, one topic per paragraph |
| One or two points | A sentence |

Look for these signs in a draft. The linter reports each one as advisory.

- A paragraph of more than 6 sentences. Split it by topic, or move its parallel parts to a list.
- A sentence that lists 5 or more items.
- A sentence that walks through steps with "first", "then", "after that".

Rules for bullets:

- One idea or one event per bullet. Sentences that describe one event stay together in one bullet. Independent rules get separate bullets. No bold label.
- Lead with the point. Put the reason or the example after it.
- Nest one level at most. A bullet that needs sub-bullets is probably a section.

Do not cut reasoning into bullets. When bullets need "because", "so", or "but" to connect to each other, write prose. Merge a list of fragments with no claim in them into sentences.

## Technical terms and other languages

Keep established technical terms as they are. Do not translate them word by word or swap them for a plainer word that loses meaning. "Source of truth", "idempotent", "lockfile", "schema", "hook" stay in English in any language. When a product name, file name, command, flag, or config key stays in the text, keep it exact. Do not translate or paraphrase it. `## Audience fit` decides whether a source-level identifier stays at all.

- Define a term the reader may not know once, on first use. After that, use the term alone.
- Pick one term per concept. Do not alternate with a translation.
- In another language, apply every structural rule and humanizer pattern in that language. "Không phải X mà là Y" is the same tell as "not X but Y".
- Translate only ordinary words. "Thư mục" for directory is fine. "Nguồn chân lý" for source of truth is not.
- In Strict mode, keep the exact identifier, error code, or API name the system uses. Audience fit does not remove identifiers in Strict mode.

## Boundaries

- Do not add a fact, cause, mechanism, name, or number the source did not give. One exception: in Human mode, you may explain behavior that you verified in the source code, and you may link to that code. Do not turn "could be caused by X" into "X is the cause".
- Do not drop a safety condition or exception to shorten a sentence. Flag the trade-off.
- Do not certify STE compliance. For aircraft documentation, use the real standard.
- Do not make empty content useful. A hollow paragraph comes out short, clean, and still hollow. Say so.
- Stop shortening when the sentence is unambiguous, not when it is shortest.
- A number needs a scale the reader has. "7 percent of the tree" means more than "0.07". A count out of a total means more than a count.
- Suggest a one-line glossary entry for a domain term that must stay.

## Resources

- `references/ste-rules.md` and `references/ai-tells.md`: the STE rule categories and the 26 humanizer patterns.
- `references/doc-shapes.md`: the usual reader and the opening of each kind of page.
- `scripts/lint.py`: one linter command. It wraps `scripts/ste-lint.py` and `scripts/tells-lint.py`. Python 3 stdlib only.

## Credits

- STE rules and examples: [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill), MIT, by Dustin Yuchen Teng.
- AI-tell patterns: the `humanizer` skill, MIT, based on Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- ASD-STE100: [asd-ste100.org](https://www.asd-ste100.org/). This skill paraphrases rule categories. It does not reproduce the standard.

