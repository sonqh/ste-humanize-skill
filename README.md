# ste-humanize

A skill for Claude Code that makes your AI agent write text you understand on the first read, in the voice of a person.

It is for people who ask an agent to write documentation, design docs, ADRs, PR descriptions, replies, or error messages. It writes new pages from your notes, rewrites text you already have, and reviews a page before you share it. It also writes replies to users and messages to customers, in English and in Vietnamese.

A skill is a folder of instructions that Claude Code loads when a task needs it. This one holds writing rules. Claude reads them when you ask for a document, a reply, a rewrite, or a review. You ask in plain words, as you do now.

## The problem

- An AI agent puts the background first and the answer last.
- It packs four options into one long paragraph.
- It sounds like a chatbot. The before text in the example below shows the habits.
- When you ask it to shorten a text, it can drop a condition or change "may fail" into "fails".
- On a design page, it weighs each option and picks none. It promises a fast system with no number and answers a risk with a promise to watch it.

## What the skill changes

| Without the skill | With the skill |
|---|---|
| The answer is in the last paragraph. | The first sentence gives the answer, the decision, or the action. |
| One paragraph holds every option. | A list appears where the content has parallel parts or steps. Reasoning stays a paragraph. |
| Long sentences in passive voice. | Sentences of 25 words or fewer, in active voice, with one instruction each. |
| Chatbot phrases and filler. | The skill removes them. Your details and opinions stay. |
| A rewrite loses a condition. | Each condition, exception, and "may" stays. |
| A design doc invents a number for work not built yet. | Each number says if it is measured, an estimate, a target, or an assumption. An unknown value is `TBD`, with an owner. |

The sentence rules come from ASD-STE100. It is the controlled English that aerospace uses so that nobody misreads a maintenance step. The list of chatbot habits comes from Wikipedia's "Signs of AI writing".

## An example

```text
Before: Oops! An error may have occurred while processing your request due to a
        possible mismatch in the expected data format, which could be caused by
        an outdated client version. Please try again or reach out to support.

After:  Your request may have failed. The cause may be a data format that does
        not match what the server expects. An outdated client can cause this
        mismatch. Check your client version. If the error continues, contact
        support.
```

The after text has five short sentences, and each one says one thing. "May" stays on both claims, because the source was not sure. "Oops!" and "Please try again" go, because they tell the reader nothing to do.

More pairs are in [`examples/before-after.md`](examples/before-after.md).

## Try it

1. Install the plugin. In Claude Code 2.1.275 or newer, one command does it.

   ```
   /plugin install ste-humanize --marketplace sonqh/ste-humanize-skill
   ```

   On an older Claude Code, add the marketplace first.

   ```
   /plugin marketplace add sonqh/ste-humanize-skill
   /plugin install ste-humanize@sonqh
   ```

2. Ask for a text. Say who reads it.

   ```
   /ste-humanize:ste-humanize write a how-to guide for new users from these notes
   ```

You get the text back with no introduction. A short line after the text can name a part to cut or an input that is missing.

You do not need the command. Claude also picks the skill up from a plain request such as "humanize this" or "review this doc". The plugin namespaces the skill, so the command is `/ste-humanize:ste-humanize`.

To get a new version later, run `/plugin update ste-humanize@sonqh`. The update applies after a restart.

## What you can ask for

```
Write a how-to guide for new users from these notes
Write an ADR from this thread
Write a design doc for this feature from my notes
Review this design doc for the backend team
Rewrite this proposal for the director who approves the budget
Rewrite this README section
Humanize this PR description
Rewrite this error message so an agent cannot misread it
Reply to this customer. She is upset and not technical
Turn this engineering note into a message for the customer, in Vietnamese
Show the diff
```

Name the reader in your request when you can. Each section below says what the skill does with one kind of request.

## What the skill does

### Write a new page

You give notes, code, a diff, or a conversation. The skill writes the page from them.

- Before the first sentence, the skill works out who reads the page, what they already know, and what they do next. If it cannot tell who the reader is, it asks you. If it cannot ask, it picks the most likely reader and names that reader on a `Reader:` line.
- The page opens with the answer, the decision, or the request. Background comes after it.
- Each section answers one question of the reader, the most urgent first. A template section with nothing to say stays out.
- Every condition, exception, and safety limit in your material goes in. No fact goes in that your material does not give.
- When the reader needs something that your notes do not give, the skill names it on a `Missing:` line. It does not fill the gap with a guess.

### Rewrite a text you have

You give a text. The skill keeps every fact in it and changes how it says them.

- It keeps every condition, exception, and hedge. "May fail" stays "may fail".
- It removes no idea of yours. It names a part that the reader may not need on a `Cut candidates:` line. You decide.
- It can move a part, so that the page follows the questions of its reader. It moves facts and removes none.
- When it keeps a long phrase on purpose, it says why on a `Kept as-is:` line.
- When the text is already clear, it says so and changes nothing.
- Add "show the diff" or "which rules did it break" to see each change in a table, with the rule behind it.
- When you name a file, the skill writes the result to the file. It changes prose only. Code blocks, commands, front matter, data, and link targets stay as they are.

### Review a page

You give a page and ask if it is ready. The skill does not rewrite it. You keep the text and make the changes. The review has four parts:

1. A verdict that names the reader and says "ready" or "not ready". When the page is not ready, it names the gap that stops the reader most.
2. A table with one row for each question of the reader. Each row says if the page answers it, under which heading, and what is missing.
3. Up to seven other problems, the most serious first. A number with no source or a missing risk comes before a problem of order or style.
4. The result of the linter in one line.

### Reply to a user or write to a customer

You give the message of a user, an internal note, or a draft. The skill writes a message for a person who may not know the technology. It works in English and in Vietnamese.

- It decides if the reader is calm, confused, or upset, and sets the tone from that. The facts stay the same.
- A reply names the problem in one sentence when something went wrong. Then it gives the answer, then the next step with a person and a date.
- The channel sets the length: up to 4 sentences in a chat, up to 5 paragraphs in an email.
- It says what the reader sees and does, not how the system works. It keeps an error text or a button name exact, so the reader can find it.
- It adds no promise, date, or refund that your material does not give. When an engineer writes "probably Friday", the customer reads an estimate, not a promise. When the customer needs a date that you did not give, the skill names it on a `Missing:` line.
- Bad news starts with the no, then the reason, then the closest option.
- It removes the stock phrases of support text in both languages. One example is a vague promise to reply as soon as possible.
- In Vietnamese, it keeps one pair of pronouns from start to end, such as "em" and "anh/chị". It uses "dạ" and "ạ" once at most.

### Pages it knows

The skill knows the usual reader of each kind of page and what that reader does next. It uses this when your request names no reader.

| Page | What the skill puts first |
|---|---|
| README | What the project does, then the install command and one example |
| How-to guide | The result, what you need before you start, then numbered steps |
| Reference page | What the item is, then entries in one fixed form |
| Concept page | The idea in one or two sentences |
| Design note | The decision and the recommendation, then the options |
| Design doc | The problem, the goals, and the non-goals, then the proposed design |
| ADR | A title that states the decision, then the status and the date |
| Technical proposal | The request, the cost, and the date of the decision |
| PR description | What changes and why, then how to test it |
| Runbook | The symptom and the first action |
| Release note | What changes for the user, breaking changes first |
| Status update or reply | The decision or the request |
| Support reply | The answer or the fix, after one sentence for the problem |
| Notice to customers | What happened and what it means for the reader |

For a README, an ADR, a technical proposal, and a design doc, the skill has a full guide. Each guide lists the questions of the reader in order, and the page follows that order. An ADR names the options, the criteria that decide between them, and who decides. A design doc names its non-goals, the option to do nothing, and the questions still open. When your repository has a template for the page, the skill keeps its headings and their order.

### Work that is not built yet

A design doc or a proposal describes a feature before its code exists. The skill keeps facts and guesses apart on these pages.

- Each number says what kind it is: measured, an estimate, a target, or an assumption.
- The skill does not invent a number. A value that nobody knows yet becomes `TBD`, with the person who finds it and a date. An example is "Cost: TBD (Lan, by 2026-12-01)".
- Questions with no answer yet go in a section of open questions.
- Plans use "will". A real "may" stays.

### Decision pages

The skill looks for six habits of a model that writes an ADR, a design doc, or a proposal:

- A page that weighs each option and picks none.
- Pros and cons with the same count for each option, as if by rule.
- Options that nobody would choose, put there to make the favorite look good.
- A quality word with no number behind it.
- A risk answered with a promise to watch it, and no action.
- A decision that names nobody who made it.

### The habits it removes

The skill knows 32 habits that make text read as machine-written. Each one has an example and a rewrite in [`references/ai-tells.md`](references/ai-tells.md). They fall into seven groups:

| Group | Examples |
|---|---|
| Staging instead of stating | A contrast with a claim nobody made, one-line closers, a long run-up before the point |
| Rhythm by rule | Groups of three, the same opening on each sentence, dashes everywhere |
| Inflation and borrowed authority | Big claims, sales words, "experts agree" with no source |
| Formatting by rule | Bold as decoration, decorative headings, curly quotes |
| Leftovers from the chat | Praise of the question, an offer to help more, knowledge-limit disclaimers |
| Writing for the wrong reader | Text about the document instead of its subject, a repeat of what the reader knows |
| Decision pages | The six habits in the section above |

### Two modes

The skill picks the mode from the kind of text. You do not choose it.

| Mode | For | What changes |
|---|---|---|
| Strict | Text that a program or an agent reads: tool descriptions, error messages, agent instructions, procedures | Every identifier and detail stays. The tone stays flat. |
| Human | Text that a person reads: docs, READMEs, PR descriptions, replies | The voice of the writer stays. Details the reader does not need, such as an internal file name, can go. |

In Human mode, give a sample of your writing and the skill matches its sentence length, words, and punctuation.

### Other languages and technical terms

- The skill applies its rules in the language of the text. A chatbot habit in Vietnamese is the same habit as its English form.
- Established terms such as "idempotent", "schema", and "lockfile" stay as they are. The skill does not translate them word by word.
- Product names, file names, commands, flags, and config keys stay exact.
- The skill defines a term the reader may not know once, on first use.

## What it is not for

- It is not for fiction, marketing, persuasive copy, or text where voice is the point.
- It does not certify a text as ASD-STE100. It does not hold the 900-word dictionary of that standard. It applies the principle: the plainest common word, used the same way every time. For certified STE documentation, use the real standard.
- It does not tell you if a fact is true. It keeps the facts you give and adds none.
- It does not make an empty paragraph useful. A paragraph with no content comes out short and clean, and the skill says that it has no content.

## Install without the plugin

Codex and other agents read skills from `~/.agents/skills`. Use one of these ways for them.

With the [skills CLI](https://skills.sh/). It needs Node 22.20 or newer.

```bash
npx skills add sonqh/ste-humanize-skill
```

Or clone it into your skills folder.

```bash
git clone https://github.com/sonqh/ste-humanize-skill ~/.claude/skills/ste-humanize
```

- The clone brings the whole repository: the skill, the tests, the specs in `openspec/`, and the maintainer hooks.
- Codex and other agents that read `~/.agents/skills` use the same clone, with that path.
- The zip on the GitHub release page holds the skill only.

## Check a file without the agent

The skill comes with a linter. It finds the rule breaks that a pattern can find, and it needs only Python 3. Run it in the folder of the skill: a clone of this repository, or the folder where you installed the skill.

```bash
python3 scripts/lint.py FILE
```

- Each finding prints as `file:line:col rule [level] match`.
- Hard findings fail the run when they exceed `--baseline N` (default 0). Advisory findings never fail it.
- `--only tells` or `--only ste` runs one rule set: the chatbot habits or the sentence rules.
- `--disable rule,rule` turns rules off.
- `--json` prints the findings as JSON.
- Three advisory rules look at the shape: `long-paragraph`, `inline-list`, and `buried-sequence`.
- Four advisory rules look at decision pages: `false-balance`, `actorless-decision`, `empty-mitigation`, and `unmeasured-quality`.
- Five advisory rules look at messages, in English and Vietnamese: `support-cliche`, `vague-date`, `blame-phrase`, `negative-contraction`, and `particle-repeat`.
- In Vietnamese, the linter counts a sentence by syllables, with a cap of 35.
- The linter flags no hedges and checks no meaning. A clean run means the regex checks found nothing.

## What is in the repository

| Path | What it holds |
|---|---|
| [`SKILL.md`](SKILL.md) | The rules for every text. Claude reads this file first. |
| [`references/`](references/) | Detail that Claude reads only when a task needs it: page guides, messages, the review steps, the 32 habits, the sentence rules, and terms. |
| [`examples/`](examples/) | Pairs of before and after text. |
| [`scripts/`](scripts/) | The linter. |
| [`evals/`](evals/) | Test requests and the outputs of each run, to compare two versions of the skill. |
| [`openspec/`](openspec/) | The specs. Each change to the skill starts here. |

To change the skill, read [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md). The notes of each version are in [`docs/releases/`](docs/releases/).

## Credits

- STE rules, `ste-lint.py`, and the STE examples come from [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) by Dustin Yuchen Teng, MIT.
- The AI-tell patterns come from the `humanizer` skill, MIT, which adapts Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## License

MIT. See [LICENSE](LICENSE).
