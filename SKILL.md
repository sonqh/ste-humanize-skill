---
name: ste-humanize
description: "Write or rewrite English so a reader cannot misread it and still hears a person behind it. Starts from the reader: what they know and what they do next. Combines ASD-STE100 sentence discipline with AI-tell removal (no not-X-but-Y, no one-line closers, no dash glue, no stock AI words). Use to write or rewrite docs, READMEs, PR descriptions, replies, tool descriptions, error messages, and any prose written for a person. Triggers: write a doc, humanize, make this clear, plain rewrite, STE rewrite, remove AI tells. Not for fiction, marketing, or copy where voice is the point."
version: 0.5.0
license: MIT
---

# ste-humanize: clear enough for a machine, written for a person

This skill starts from the reader. Then it applies the sentence rules of ASD-STE100, the controlled English that aerospace built so a maintenance step cannot be misread. Last, it removes the habits that make text read as machine-written.

Use it to write or rewrite a document, README, design note, PR description, or reply for a person. Use it also for a tool description, error message, or instruction that an agent must parse. Do not use it for fiction, marketing, or any text where voice and persuasion are the point.

## What to read

This file holds the rules for every text. Read one more file only when its row applies. Read it before you write.

| When | Read |
|---|---|
| The mode is Human | `references/human.md`: voice, audience fit, and the AI tells |
| The task is Write | `references/doc-shapes.md`: the usual reader and the opening of each kind of page |
| The text is not in English, or it holds domain terms or identifiers | `references/terms.md` |
| A sentence rule is unclear | `references/ste-rules.md`: each rule with an example |
| An AI tell is unclear | `references/ai-tells.md`: the 26 patterns with examples |

## Two modes

Pick the mode from the text type. Do not announce it.

**Strict.** Tool descriptions, error messages, agent-to-agent instructions, procedures, safety text. The reader is a tool or an agent, and it cannot ask. Apply every rule in this file. Keep every identifier and every detail. Keep the tone flat. From the AI tells, remove only chatbot residue and text that explains again what the reader knows.

**Human.** READMEs, docs, design notes, PR descriptions, chat replies, status updates, anything a person reads. Apply every rule in this file and in `references/human.md`. The reader should notice that they understood the text on the first read, not that a standard was applied.

## Two tasks

The mode sets the rules. The task sets what you may leave out. Pick the task from the request.

**Rewrite.** The user gives a text. The source is the truth. Keep every fact per precedence item 1. When the reader may not need an idea, do not remove it. Name it on a `Cut candidates:` line. The owner of the text decides.

**Write.** The user asks for a new text from notes, code, a diff, or the conversation. That material is input. The reader brief decides which parts go in. Three limits stay:

- A condition, exception, or limit of a behavior you describe always goes in.
- A safety condition always goes in.
- No fact goes in that the material does not give and that you did not verify.

## Reader first

Before the first sentence, answer a reader brief. Do not print it.

1. Who reads this? Take the reader from the request, then from the kind of page in `references/doc-shapes.md`.
2. What does the reader already know?
3. What does the reader do or decide after reading?

Then apply the brief:

- Answer first. The first sentence gives the conclusion, the decision, or the action the reader must take. Reasons and background come after it. Each section opens with its own point.
- Each part must help the reader with item 3. If it does not, leave it out of a Write. In a Rewrite it stays and becomes a cut candidate.
- Background the reader already has gets one clause or none.
- Stop when the reader can act. Leave out a template section that has nothing to say.
- If neither the request nor the kind of page tells you the reader, ask. If you cannot ask, choose the most likely reader and report it on a `Reader:` line.

## Order of precedence when rules conflict

1. Meaning. Every fact the reader needs survives, and so does every condition, exception, qualifier, and hedge in the source. In a Write task, the reader brief decides which facts the reader needs.
2. Structure (STE). Short sentences, active voice, one instruction per sentence, no semicolons, no dropped words.
3. Voice (humanizer). No staging, no inflation, no decoration, no chatbot residue.
4. Shape. The content picks the shape.
5. Brevity. Shorter only when it does not cost 1 to 4.

## Sentence rules

Apply these in both modes. Each one is mechanical: you can point at the word or mark that breaks it.

- Active voice, unless the actor is unknown or irrelevant.
- One plain verb, not a phrasal verb. "Start the job." Not "Spin up the job."
- One instruction per sentence.
- 20 words or fewer for an instruction, 25 for a description.
- No semicolons and no dashes. Use a period, comma, colon, or parentheses.
- 3 words or fewer in one noun phrase.
- Keep the subject, the verb, and the article.
- Keep modality. "The request may have failed" does not become "The request failed". Keep one real hedge and cut stacked qualifiers.
- Simple tenses, unless the compound form carries meaning. "The job has completed" says that the output is ready now.
- A verb, not a noun. "Analyze the log." Not "Perform an analysis of the log."
- One topic per paragraph, 6 sentences or fewer.
- The plainest common word, used the same way every time. This skill does not hold the STE dictionary. Do not claim compliance with it.

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
- Nest one level at most.

Do not cut reasoning into bullets. When bullets need "because", "so", or "but" to connect to each other, write prose. Merge a list of fragments with no claim in them into sentences.

## Process

1. Pick the mode and the task. Read the files that `## What to read` names. Answer the reader brief.
2. For a Rewrite, read the whole text once and note every hedge, condition, and exception. These must survive. For a Write, list the points the reader needs, the answer first.
3. Run `python3 scripts/lint.py FILE` on the source or the draft. It flags no hedges and checks no meaning.
4. Write or rewrite paragraph by paragraph. If a rewrite would drop a condition or change a hedge into a fact, keep the longer phrasing and flag it.
5. Read the result aloud. Fix any sentence a reader could misread and any that still sounds like a chatbot.
6. Run the linter again. Advisory findings do not fail. Hard findings do, unless you can name the precision they protect.
7. If the input already complies, say so. Do not force edits onto clean text.

## Output format

**Default: the text and nothing else.** No preamble, no mode announcement, no count of changes, no closing offer.

Three permitted additions, each one line after the text. Omit a line when there is nothing to report.

- `Kept as-is:` when step 4 kept a longer phrasing on purpose. Name the phrase and the precision it protects.
- `Cut candidates:` in a Rewrite task, when a part does not help the reader. Name each part in a few words. Do not remove it.
- `Reader:` when you chose the reader yourself. Name the reader in one clause.

**On request: the rule table.** When the user asks to "show the diff", "explain the changes", or "which rules did it break", output a table with the columns Rule, Original, and Rewrite. Add one line with the mode and the count of findings. Add one line on anything you did not change on purpose, and why.

**File mode.** When the user names a file, write only the final text to the file. Change prose only. Do not change a code block, command, YAML front matter, data, or link target. Then give a short summary that lists each identifier you removed, each cut candidate, and the reader you chose.

**Embedded mode.** When another task uses this skill for a document, PR, or commit message, return only the final text.

## Boundaries

- Do not add a fact, cause, mechanism, name, or number the source did not give. Do not turn "could be caused by X" into "X is the cause".
- Do not drop a safety condition or exception to shorten a sentence. Flag the trade-off.
- Do not certify STE compliance. For aircraft documentation, use the real standard.
- Do not make empty content useful. A hollow paragraph comes out short, clean, and still hollow. Say so.
- Stop shortening when the sentence is unambiguous, not when it is shortest.
- A number needs a scale the reader has. "7 percent of the tree" means more than "0.07". A count out of a total means more than a count.

## Resources

- `scripts/lint.py`: one linter command. It wraps `scripts/ste-lint.py` and `scripts/tells-lint.py`. Python 3 stdlib only.

## Credits

- STE rules and examples: [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill), MIT, by Dustin Yuchen Teng.
- AI-tell patterns: the `humanizer` skill, MIT, based on Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- ASD-STE100: [asd-ste100.org](https://www.asd-ste100.org/). This skill paraphrases rule categories. It does not reproduce the standard.
