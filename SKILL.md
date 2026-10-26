---
name: ste-humanize
description: "Rewrite English so a reader cannot misread it and still hears a person behind it. Combines ASD-STE100 sentence discipline with AI-tell removal (no not-X-but-Y, no one-line closers, no dash glue, no stock AI words). Use for docs, READMEs, PR descriptions, replies, tool descriptions, error messages, and any prose written for a person. Triggers: humanize, make this clear, plain rewrite, STE rewrite, remove AI tells. Not for fiction, marketing, or copy where voice is the point."
version: 0.2.0
license: MIT
---

# ste-humanize: clear enough for a machine, written for a person

This skill does two jobs in one pass. First it applies the structural rules of ASD-STE100, the controlled English that aerospace built so a maintenance step cannot be misread. Then it removes the habits that make text read as machine-written.

Keep what the text says. Do not drop a condition, a scope limit, or a hedge that carries real doubt.

## When to use this skill

Use it when you write a document, README, design note, PR description, or reply for a person, or a tool description, error message, or instruction that another agent must parse. Use it when a draft reads dense, hedged, over-formatted, or like a chatbot. Do not use it for fiction, marketing, or any text where voice and persuasion are the point.

## Two modes

Pick the mode from the text type. Do not announce it unless the user asks for the rule table.

**Strict.** Tool descriptions, error messages, agent-to-agent instructions, procedures, safety text. Apply every STE rule below, including the word-use rules. From the humanizer side apply only chatbot residue and re-explaining what the reader knows. Voice does not matter here. A wrong reading does.

**Human.** READMEs, docs, design notes, PR descriptions, chat replies, status updates, anything a person reads. Apply the STE structural rules in full, treat the STE word-use rules as a direction, and apply the full humanizer pass. The reader should notice they understood it on the first read, not that a standard was applied.

## Order of precedence when rules conflict

1. Meaning. Every fact, condition, qualifier, and hedge in the source survives.
2. Structure (STE). Short sentences, active voice, one instruction per sentence, no semicolons, no dropped words.
3. Voice (humanizer). No staging, no inflation, no decoration, no chatbot residue. Keep the writer's specific details and real asides.
4. Shape. Parallel parts become bullets. Technical terms stay as the field uses them.
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

1. Pick the mode. Read the whole text once for meaning. Note every hedge and condition. These must survive.
2. Run `python3 scripts/lint.py FILE` for a mechanical first pass. It flags no hedges and checks no meaning.
3. Mark every finding, strongest first: staging and STE structure, then inflation, then word choice.
4. Rewrite paragraph by paragraph in short active sentences. Split parallel ideas into bullets. If a rewrite would drop a condition or upgrade a hedge to a fact, keep the longer phrasing and flag it.
5. Read the result aloud. Fix any sentence a reader could misread and any that still sounds like a chatbot.
6. Run the linter again. Advisory findings do not fail. Hard findings do, unless you can name the precision they protect.
7. If the input already complies, say so. Do not force edits onto clean text.

## Output format

**Default: the rewritten text and nothing else.** No preamble, no mode announcement, no count of changes, no closing offer.

One permitted addition. When step 4 kept a longer phrasing on purpose, add one line after the text, prefixed `Kept as-is:`, naming the phrase and the precision it protects. Omit the line when there is nothing to report.

**On request: the rule table.** When the user asks to "show the diff", "explain the changes", or "which rules did it break", output this instead:

```markdown
| Rule | Original | Rewrite |
|---|---|---|
| Not X but Y | "It's not a tool, it's a mirror." | "The tool shows you your own habits." |
| Present perfect | "We have received your request." | "We received your request." |

Mode: Human. 9 findings.
```

Follow the table with one line on anything you did not change on purpose, and why.

**File mode.** When the user names a file, write only the final text to the file. Change prose only. Keep code, commands, paths, YAML front matter, data, and link targets unchanged. Then give a short summary.

**Embedded mode.** When another task uses this skill for a document, PR, or commit message, return only the final text.

## Voice

When the user gives a writing sample, match its sentence length, word choice, punctuation, and openings. The sample overrides the dash rule: if it uses dashes, keep them at the same rate.

Without a sample, take the voice from the text type. A design note or a reply keeps the writer's opinion and specific details. A reference page or an error message stays neutral. Keep what carries the writer's voice unless it hurts the meaning: an unusual detail, mixed feelings stated plainly, a real aside, a first-person choice the writer can explain.

## Shape: bullets first

Prefer a bullet list over a paragraph when the content has parallel parts: options, steps, findings, risks, decisions, rules.

- One idea per bullet, in one or two short sentences. No bold label. Numbered only when order matters.
- Lead with the point. Put the reason or the example after it.
- Keep prose for one connected argument or a transition.
- Nest one level at most. A bullet that needs sub-bullets is probably a section.
- Keep a table as a table when items share the same attributes.

Split a long paragraph with three or more parallel ideas into bullets. Merge a list of fragments with no claim in them into sentences.

## Shape: a page for a newcomer

When the reader may not know the domain, order the page so each part needs only the one before it.

1. What the base thing is, in one paragraph. Name it, say where it lives, say what it holds.
2. The problem, in two or three bullets, in words the reader already has.
3. What the tool does about it. A table of before and after works when the rows are parallel.
4. Proof. A clip, a transcript, or a number with a scale the reader has.
5. How to try it. Three commands or fewer.

Explain each term on first use, inside the sentence that uses it. A caption for a clip or a screenshot says what the reader sees, then why it matters. It does not repeat the command.

## Technical terms and other languages

Keep established technical terms as they are. Do not translate them word by word or swap them for a plainer word that loses meaning. "Source of truth", "idempotent", "lockfile", "schema", "hook" stay in English in any language. So do product names, file names, commands, flags, and config keys.

- Define a term the reader may not know once, on first use. After that, use the term alone.
- Pick one term per concept. Do not alternate with a translation.
- In another language, apply every structural rule and humanizer pattern in that language. "Không phải X mà là Y" is the same tell as "not X but Y".
- Translate only ordinary words. "Thư mục" for directory is fine. "Nguồn chân lý" for source of truth is not.
- In Strict mode, keep the exact identifier, error code, or API name the system uses.

## Boundaries

- Do not add a fact, cause, mechanism, name, or number the source did not give. Do not turn "could be caused by X" into "X is the cause".
- Do not drop a safety condition or exception to shorten a sentence. Flag the trade-off.
- Do not certify STE compliance. For aircraft documentation, use the real standard.
- Do not make empty content useful. A hollow paragraph comes out short, clean, and still hollow. Say so.
- Stop shortening when the sentence is unambiguous, not when it is shortest.
- A number needs a scale the reader has. "7 percent of the tree" means more than "0.07". A count out of a total means more than a count.
- Suggest a one-line glossary entry for a domain term that must stay.

## Resources

- `references/ste-rules.md` and `references/ai-tells.md`: the STE rule categories and the 26 humanizer patterns.
- `scripts/lint.py`: one linter command. It wraps `scripts/ste-lint.py` and `scripts/tells-lint.py`. Python 3 stdlib only.

## Credits

- STE rules and examples: [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill), MIT, by Dustin Yuchen Teng.
- AI-tell patterns: the `humanizer` skill, MIT, based on Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- ASD-STE100: [asd-ste100.org](https://www.asd-ste100.org/). This skill paraphrases rule categories. It does not reproduce the standard.

