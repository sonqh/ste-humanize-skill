# ste-humanize

A skill for Claude Code that makes your AI agent write text you understand on the first read, in the voice of a person.

A skill is a folder of instructions that Claude Code loads when a task needs it. This one holds writing rules. Claude reads them when you ask for a document, a reply, or a rewrite.

## The problem

- An AI agent puts the background first and the answer last.
- It packs four options into one long paragraph.
- It sounds like a chatbot. The before text in the example below shows the habits.
- When you ask it to shorten a text, it can drop a condition or change "may fail" into "fails".

## What the skill changes

| Without the skill | With the skill |
|---|---|
| The answer is in the last paragraph. | The first sentence gives the answer, the decision, or the action. |
| One paragraph holds every option. | A list appears where the content has parallel parts or steps. Reasoning stays a paragraph. |
| Long sentences in passive voice. | Sentences of 25 words or fewer, in active voice, with one instruction each. |
| Chatbot phrases and filler. | The skill removes them. Your details and opinions stay. |
| A rewrite loses a condition. | Each condition, exception, and "may" stays. |

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

1. Install the plugin in Claude Code 2.1.275 or newer.

   ```
   /plugin install ste-humanize --marketplace sonqh/ste-humanize-skill
   ```

2. Ask for a text. Say who reads it.

   ```
   /ste-humanize:ste-humanize write a how-to guide for new users from these notes
   ```

You get the text back and nothing else.

## What you can ask for

```
Write a how-to guide for new users from these notes
Write an ADR from this thread
Rewrite this proposal for the director who approves the budget
Rewrite this README section
Humanize this PR description
Rewrite this error message so an agent cannot misread it
Show the diff
```

- The plugin namespaces the skill, so the command is `/ste-humanize:ste-humanize`. Claude also picks the skill up from a plain request such as "humanize this".
- For a README, an ADR, or a technical proposal, the skill orders the page by the questions of its readers. The request or the cost of a proposal comes first. The title of an ADR states the decision.
- For a new page, the skill starts from the reader. It works out who reads the page, what they already know, and what they do next. Name the reader in your request when you can. If the skill cannot tell who the reader is, it asks you.
- In a rewrite, the skill removes no idea of yours. It names a part the reader may not need on a `Cut candidates:` line. You decide.
- Add "show the diff" or "which rules did it break" to see each change in a table, with the rule behind it.
- The skill picks one of two modes. Strict is for text that a program or an agent parses: tool descriptions, error messages, and agent instructions. Human is for text that a person reads: docs, READMEs, PR descriptions, and replies.

## What it is not for

- It is not for fiction, marketing, persuasive copy, or text where voice is the point.
- It is built for these texts: documentation, READMEs, design notes, PR descriptions, and changelogs. It is also built for replies in threads, tool descriptions, error messages, and agent-to-agent instructions.
- It does not certify a text as ASD-STE100. It does not hold the 900-word dictionary of that standard. It applies the principle: the plainest common word, used the same way every time. For certified STE documentation, use the real standard.

## Other ways to install

On an older Claude Code, add the marketplace first.

```
/plugin marketplace add sonqh/ste-humanize-skill
/plugin install ste-humanize@sonqh
```

`/plugin update ste-humanize@sonqh` gets a new version. The update applies after a restart.

With the [skills CLI](https://skills.sh/). It needs Node 22.20 or newer.

```bash
npx skills add sonqh/ste-humanize-skill
```

Or clone it into your skills folder.

```bash
git clone https://github.com/sonqh/ste-humanize-skill ~/.claude/skills/ste-humanize
```

- The clone brings the whole repository: the skill, the tests, the specs in `openspec/`, and the maintainer hooks.
- The zip on the GitHub release page holds the skill only.
- Codex and other agents that read `~/.agents/skills` use the same clone, with that path.

## Check a file without the agent

The repository holds a linter. It finds the rule breaks that a pattern can find, and it needs only Python 3.

```bash
python3 scripts/lint.py FILE
```

- Each finding prints as `file:line:col rule [level] match`.
- Hard findings fail the run when they exceed `--baseline N` (default 0). Advisory findings never fail it.
- `--only tells` or `--only ste` runs one rule set: the chatbot habits or the sentence rules.
- `--disable rule,rule` turns rules off.
- `--json` prints the findings as JSON.
- Three advisory rules look at the shape: `long-paragraph`, `inline-list`, and `buried-sequence`.
- The linter flags no hedges and checks no meaning. A clean run means the regex checks found nothing.

## Credits

- STE rules, `ste-lint.py`, and the STE examples come from [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) by Dustin Yuchen Teng, MIT.
- The AI-tell patterns come from the `humanizer` skill, MIT, which adapts Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## License

MIT. See [LICENSE](LICENSE).
