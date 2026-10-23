---
name: ste-humanize
description: "Rewrite English so a reader cannot misread it and still hears a person behind it. Combines the sentence discipline of ASD-STE100 (one meaning per word, active voice, short sentences, one instruction per sentence) with the AI-tell removal of the humanizer skill (no not-X-but-Y, no one-line closers, no dashes everywhere, no stock AI words). Use for docs, READMEs, PR descriptions, design notes, replies, tool descriptions, error messages, and any prose Claude writes for a person. Triggers: humanize, make this clear, plain rewrite, STE rewrite, remove AI tells, write this for a human, rewrite so nobody misreads it. Not for fiction, marketing, or copy where voice is the point."
version: 0.2.0
license: MIT
---

# ste-humanize: clear enough for a machine, written for a person

This skill does two jobs in one pass. First it applies the structural rules of ASD-STE100, the controlled English the aerospace industry built so a maintenance step cannot be misread. Then it removes the habits that make text read as machine-written: staged contrasts, one-line closers, dashes as glue, stock words, decorative bold. The result is text a non-native reader, a downstream agent, and a tired colleague all read the same way.

Keep what the text says. Do not add a fact, a number, a cause, or a name the source did not give. Do not drop a condition, a scope limit, or a hedge that carries real doubt.

## When to use this skill

- You write a document, README, design note, PR description, changelog, or reply for a person who did not write the source.
- You write a tool description, error message, or instruction that another agent must parse with no human to ask.
- A draft reads dense, hedged, over-formatted, or sounds like a chatbot.

Do not use it for fiction, poetry, marketing, or any text where voice and persuasion are the point.

## Two modes

Pick the mode from the text type. Do not announce it unless the user asks for the rule table.

**Strict.** Tool and function descriptions, error messages, agent-to-agent instructions, procedures, safety text. Apply every STE rule below, including the word-use rules. From the humanizer side apply only the leftovers (section C, patterns 1 and 2): a tool description must not open with "Great question!" and must not re-explain what the caller knows. Voice does not matter here. A wrong reading does.

**Human.** READMEs, docs, design notes, PR descriptions, chat replies, status updates, anything a person reads. Apply the STE structural rules in full, treat the STE word-use rules as a direction, and apply the full humanizer pass. The reader should not notice a standard was applied. They should notice they understood it on the first read.

## Order of precedence when rules conflict

1. Meaning. Every fact, condition, qualifier, and hedge in the source survives.
2. Structure (STE). Short sentences, active voice, one instruction per sentence, no semicolons, no dropped words.
3. Voice (humanizer). No staging, no inflation, no decoration, no chatbot residue. Keep the writer's specific details and real asides.
4. Shape. Parallel parts become bullets. Technical terms stay as the field uses them.
5. Brevity. Shorter only when it does not cost 1 to 4.

The two sources agree more than they disagree. Where they do disagree, this is how to read them together:

| Topic | STE says | Humanizer says | This skill does |
|---|---|---|---|
| Hedges | Keep "may", "could", "sometimes". Confidence is content. | Cut stacked qualifiers added by nervous editing. | Keep one hedge that carries real doubt. Cut the stack around it. "It could potentially possibly affect" becomes "It may affect". "May have failed" stays "may have failed". |
| Lists | Use a list for 3 or more steps or conditions. | Do not give every item a bold label and a colon. | Use lists for sequences and conditions. Write items as plain sentences or phrases without bold labels. |
| Flat tone | Be literal and flat. | Keep the writer's opinions, asides, and specific details. | In Strict mode be flat. In Human mode keep an aside or an opinion when it adds information, and still write it in a short active sentence. |
| Punctuation | No semicolons. Em dash permitted. | No em or en dashes unless the writer's sample uses them. | No semicolons and no dashes. Use a period, a comma, a colon, or parentheses. |
| Synonyms | One word, one meaning, used the same way every time. | No rule, but stock AI words are out. | Pick one plain word per idea and reuse it. Do not reach for "leverage", "robust", "delve", or "landscape" to vary it. |
| Passive voice | Active voice for instructions. Passive only when the actor is unknown or irrelevant. | Prefer active when it names the actor. | Active voice. Allow passive only in descriptive text where the actor truly does not matter, and say who acts whenever it matters. |

## STE structural rules

Apply these in both modes. Each one is mechanical: you can point at the word or mark that breaks it.

| Rule | Do | Do not |
|---|---|---|
| Active voice | "The agent deletes the file." | "The file is deleted." unless the actor is unknown or irrelevant |
| No phrasal verbs | "Remove the panel." "Start the job." "Contact the team." | "Take off the panel." "Spin up the job." "Reach out to the team." |
| One instruction per sentence | "Open the file. Read line 3." | "Open the file and read line 3, then check if it matches." |
| Sentence length | 20 words or fewer for instructions. 25 or fewer for description. | Long sentences with stacked clauses |
| No semicolons | Split into two sentences. | Any semicolon |
| Noun clusters | 3 words or fewer stacked as one noun phrase | "high pressure fuel pump inlet valve assembly" |
| No dropped words | Keep subject, verb, and article explicit. | "Files not backed up will be lost." (which files?) |
| Keep modality | "The request may have failed." | "The request failed." when the source said "may" |
| Simple tenses | "We received the report." | "We have received the report." unless the compound form carries meaning the simple form cannot (see below) |
| Verb, not noun | "Analyze the log." | "Perform an analysis of the log." |
| One topic per paragraph | 6 sentences or fewer | Paragraphs that change subject halfway |
| Lists for sequences | A numbered list for 3 or more steps | A sequence buried in one prose sentence |

One exception on tenses. "The job has completed" (and its output is ready now) and "the job completed" (at some past time) are different statements. Where the compound form carries current relevance or a hedge, keep it and note the departure.

STE word-use rules (one word, one meaning, one part of speech) depend on ASD's 900-word dictionary, which this skill does not reproduce. Apply the principle: choose the plainest common word and use it the same way every time. Do not claim dictionary compliance.

## Humanizer patterns

Apply section A and B on one sighting. Patterns marked *weak alone* need company. In Strict mode apply only section C.

### A. Staging instead of stating

1. **Not X but Y.** "It's not just a song, it's a statement." The negative half names something no one claimed. State the point. Keep a contrast only when the negative half corrects a belief the reader holds.
2. **One-line closers.** "That is the real win." "Read that again." A row of fragments. A sentence after an example that names what the example showed. Cut it unless it adds a fact or a consequence.
3. **Sayings that sound deep.** "At its core", "the real question is", "X is the language of Y". Replace with the specific claim.
4. **Staged run-up.** "Let's dive in", "Here's the thing", "Honestly?". Delete the run-up and make the point.
5. **Arguing with no one.** "I'm not saying", "To be clear", "One might be tempted to". Remove the defense. Keep an objection only when the text attributes it or a reader would raise it.
6. **Forced triads.** Three items because three sounds complete. Keep three when the meaning has three parts. Otherwise merge or develop one.
7. **Dashes as the universal connector.** No em dashes or en dashes in the final text. Replace each with a period, comma, colon, or parentheses. Leave dashes inside code, paths, and URLs alone.
8. **Stacked qualifiers.** "Could potentially possibly". Keep the one hedge the source supports. *Weak alone.*

### B. Inflation and decoration

9. **Stock AI words.** actually, additionally, align with, crucial, deep dive, delve, enhance, garner, highlight (verb), interplay, intricate, key (adjective), landscape (abstract), leverage, meticulous, pivotal, robust (figurative), seamless, showcase, tapestry, testament, underscore (verb), vibrant. Replace with the plain word or cut.
10. **Inflated significance.** "marks a pivotal moment", "plays a key role", "the future looks bright". Keep the fact. Drop the significance. End on the last concrete fact.
11. **Vague connection.** "associated with", "linked to". Name the relationship the source gives. If the source does not say, keep the vague word rather than invent a role.
12. **Shallow -ing riders.** "..., highlighting the importance of", "..., ensuring reliability". Keep the fact. Keep the rider only when the source supports it.
13. **Sales language.** rich (figurative), profound, nestled, renowned, breathtaking, diverse array. State what the thing is.
14. **Borrowed authority.** "experts argue", "industry reports", a list of prestige outlets. Use the real source and what it said, or cut.
15. **Avoiding is, are, has.** "serves as", "boasts", "features", "represents". Use is, are, has.
16. **Bold as decoration.** Bold on every list item with a colon after it. Remove the bold. Turn a labeled list into prose when the labels carry no information.
17. **Decorative headings.** Title Case, emojis, arrows, a rule between every section. Use sentence case. Let the heading name what the section holds.
18. **Repeated sentence openings.** Three sentences in a row starting with the same subject. Merge or vary. *Weak alone.*

### C. Leftovers from the chat

19. **Chatbot residue.** "Great question!", "I hope this helps", "Would you like me to...". Remove the wrapper. Keep the content.
20. **Re-explaining what the reader knows.** A reply that rebuilds the background before it reaches the decision. Lead with the decision. Keep only the one fact the reader lacks.
21. **Writing about the document.** "This section outlines", "the table below shows". Describe the subject, not the page.
22. **A heading repeated in the first sentence.** Remove the repeated sentence.

## Process

1. Pick the mode from the text type.
2. Read the whole text once for meaning. Write down, for yourself, every hedge and every condition. These must survive.
3. Run the linters for a mechanical first pass. `scripts/ste-lint.py FILE` checks semicolons, sentence length, phrasal verbs, nominalization, marketing adjectives, synonym rotation, passive voice, and compound tenses. `scripts/tells-lint.py FILE` checks dashes, not-X-but-Y, stock AI words, bold labels on list items, chatbot residue, and Title Case headings. Neither linter flags hedges, and neither one checks meaning.
4. Mark every finding, strongest first: section A tells and STE structure first, then section B, then word choice.
5. Rewrite paragraph by paragraph. State each point in a short active sentence. Split parallel ideas into bullets. Keep technical terms as the field uses them. If a rewrite would drop a condition or upgrade a hedge to a fact, keep the longer phrasing and flag it.
6. Read the result aloud. Ask two questions. Can a reader with no back-channel misread any sentence? Does any sentence still sound like a chatbot? Fix both.
7. Run both linters again. Advisory findings do not fail. Hard findings do, unless you can name the precision they protect.
8. If the input already complies, say so. Do not force edits onto clean text.

## Output format

**Default: the rewritten text and nothing else.** No preamble, no mode announcement, no count of changes, no closing offer.

One permitted addition. When step 5 kept a longer phrasing on purpose, add one line after the text, prefixed `Kept as-is:`, naming the phrase and the precision it protects. Omit the line when there is nothing to report.

**On request: the rule table.** When the user asks to "show the diff", "explain the changes", or "which rules did it break", output this instead:

```markdown
| Rule | Original | Rewrite |
|---|---|---|
| Not X but Y | "It's not a tool, it's a mirror." | "The tool shows you your own habits." |
| Present perfect | "We have received your request." | "We received your request." |
| Dash as connector | "The policy — announced today — applies." | "The policy, announced today, applies." |

Mode: Human. 9 findings.
```

Follow the table with one line on anything you did not change on purpose, and why.

**File mode.** When the user names a file, write only the final text to the file. Change prose only. Keep code blocks, inline code, commands, paths, YAML front matter, data, and link targets unchanged. Then give the user a short summary.

**Embedded mode.** When another task uses this skill for a document, PR, or commit message, return only the final text.

## Voice

When the user gives a writing sample, read it first and match its sentence length, word choice, punctuation, and openings. The sample overrides the dash rule: if the sample uses dashes, keep them at the same rate.

Without a sample, take the voice from the kind of text. A design note or a reply keeps the writer's opinion and the odd specific detail. A reference page or an error message stays neutral. In both cases the sentences stay short and active.

Keep what carries the writer's voice unless it hurts the meaning: a specific unusual detail, mixed feelings stated plainly, a real aside, a first-person choice the writer can explain.

## Shape: bullets first

Prefer a bullet list over a paragraph whenever the content has parallel parts: options, steps, findings, risks, decisions, rules. A reader scans a list faster than prose, and a list forces one idea per line.

- One idea per bullet. One or two short sentences. No bold label and no colon at the start.
- Lead each bullet with the point. Put the reason or the example after it.
- Use a numbered list only when order matters.
- Keep prose for one connected argument, a lead sentence, or a transition. Two or three sentences per paragraph.
- Do not nest more than one level. If a bullet needs sub-bullets, it is probably a section.
- Do not turn a table into bullets. A table is better when items share the same attributes.

When the source is a long paragraph with three or more parallel ideas, split it into bullets. When the source is a list of fragments with no claim in them, merge them into sentences.

## Technical terms and other languages

Keep established technical terms as they are. Do not translate them word by word, and do not swap them for a plainer word that loses the meaning. "Source of truth", "idempotent", "pure function", "lockfile", "managed block", "adapter", "schema", "diff", "hook", "MCP server" stay in English in any language. The same holds for product names, file names, commands, flags, and config keys.

- A term the reader may not know gets a short definition once, on first use. After that, use the term alone.
- Pick one term per concept and reuse it. Do not alternate between the English term and a translation.
- When the text is not in English, apply every structural rule (short sentences, active voice, one instruction per sentence, no semicolons, no dashes, no bold labels) in that language. The humanizer patterns apply in that language too: "không phải X mà là Y" is the same tell as "not X but Y".
- Translate only ordinary words. "Thư mục" for directory is fine. "Nguồn chân lý" for source of truth is not, because readers in the field use the English term.
- In Strict mode, keep the exact identifier, error code, or API name the system uses, even when a plainer word exists.

## Boundaries

Will:

- Rewrite dense, hedged, or machine-sounding English into short, active, single-meaning sentences that still read like a person wrote them.
- Preserve every fact, condition, scope qualifier, and real hedge.
- Return the rewrite alone by default, and name the rules on request.
- Suggest a one-line glossary entry for a domain term that must stay.

Will not:

- Add a fact, cause, frequency, mechanism, name, or number the source did not give.
- Turn "may have failed" into "failed", or "could be caused by X" into "X is the cause".
- Drop a safety condition or exception to shorten a sentence. It flags the trade-off instead.
- Reproduce ASD's dictionary or guarantee certified STE compliance. For aircraft documentation, use the real standard.
- Rewrite fiction, marketing, or persuasive copy.
- Make empty content useful. A hollow paragraph comes out short, clean, and still hollow. Say so.
- Shorten past the point of clarity. Stop when the sentence is unambiguous, not when it is shortest.

## Resources

- `references/ste-rules.md`: the ASD-STE100 rule categories with citations.
- `references/ai-tells.md`: the full humanizer pattern list with before and after examples.
- `examples/before-after.md`: worked examples for this combined skill.
- `examples/ste-before-after.md`: the original STE examples, including official ones.
- `scripts/ste-lint.py`: deterministic STE structural linter (stdlib only).
- `scripts/tells-lint.py`: deterministic AI-tell linter (stdlib only).

## Credits

- STE rules, linter, and STE examples: [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill), MIT, by Dustin Yuchen Teng.
- AI-tell patterns: the `humanizer` skill, MIT, based on Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- ASD-STE100: [asd-ste100.org](https://www.asd-ste100.org/). This skill paraphrases rule categories. It does not reproduce the standard.
