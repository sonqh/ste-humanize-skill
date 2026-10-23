# ste-humanize

A Claude Code skill that rewrites English so nobody misreads it and it still sounds like a person wrote it.

It combines two disciplines:

- The sentence rules of [ASD-STE100](https://www.asd-ste100.org/) (Simplified Technical English), the controlled language the aerospace industry built so a maintenance step cannot be misread. Short sentences, active voice, one instruction per sentence, one meaning per word, no dropped words.
- The AI-tell removal of the `humanizer` skill, based on Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). No "not X but Y", no one-line closers, no dashes as glue, no stock AI words, no bold labels on every list item, no chatbot residue.

STE alone makes text flat. The humanizer alone leaves long sentences. Together they produce text a non-native reader, a downstream agent, and a tired colleague all read the same way.

## Before and after

| Before | After |
|---|---|
| "Let's dive into what this tool does. It's not just a sync utility, it's a robust, seamless configuration layer that has been designed to leverage your existing setup across the various agents that have been configured, ensuring consistency. That is the real win." | "This tool is a configuration layer. It reads the setup you already have and writes it to each agent you configured. Each agent then reads the same rules." |
| "Oops! An error may have occurred while processing your request due to a possible mismatch in the expected data format, which could be caused by an outdated client version. Please reach out to support." | "Your request may have failed. The cause may be a data format that does not match what the server expects. An outdated client can cause this mismatch. Check your client version. If the error continues, contact support." |

More in [`examples/before-after.md`](examples/before-after.md).

## What it does

1. Picks a mode. **Strict** for tool descriptions, error messages, and agent instructions: full STE, no voice. **Human** for docs, READMEs, PR descriptions, and replies: STE structure plus the full humanizer pass.
2. Reads the text for meaning and lists every hedge and condition that must survive.
3. Runs two linters for a mechanical first pass.
4. Rewrites paragraph by paragraph in short active sentences, with the writer's specific details kept.
5. Returns the rewrite alone, plus one `Kept as-is:` line when it left a longer phrase on purpose.

When the two sources disagree, SKILL.md has a precedence table. The short version: meaning first, then STE structure, then voice, then brevity.

## Install

With the [skills CLI](https://skills.sh/):

```bash
npx skills add sonqh/ste-humanize-skill
```

Or clone into your global skills folder:

```bash
git clone https://github.com/sonqh/ste-humanize-skill ~/.claude/skills/ste-humanize
```

Codex and other agents that read `~/.agents/skills`:

```bash
git clone https://github.com/sonqh/ste-humanize-skill ~/.agents/skills/ste-humanize
```

## Use

```
/ste-humanize rewrite this README section
Humanize this PR description
Rewrite this error message so an agent cannot misread it
Show the diff
```

You get the rewritten text back. Add "show the diff" or "which rules did it break" to see the rule table.

## Linters

Both scripts are stdlib-only Python and exit 1 when hard findings exceed `--baseline` (default 0).

```bash
python scripts/ste-lint.py FILE        # semicolons, length, phrasal verbs, nominalization, passive, tenses
python scripts/tells-lint.py FILE      # dashes, not-X-but-Y, stock words, bold labels, chat residue
python scripts/tells-lint.py --selftest
```

Neither linter flags hedges. Neither one checks that a rewrite kept the original meaning. A clean run means the regex checks found nothing.

The repo's own SKILL.md does not lint clean, because it quotes the patterns it forbids. Lint it with `--baseline 40` and read the findings as examples.

## Scope

Built for: documentation, READMEs, design notes, PR descriptions, changelogs, replies in threads, tool descriptions, error messages, agent-to-agent instructions.

Not built for: fiction, marketing, persuasive copy, or text where voice is the point.

This skill does not reproduce ASD's 900-word dictionary. The standard is free to obtain but not free to redistribute. It applies the principle (plainest common word, used the same way every time). For certified STE documentation, use the real standard.

## Credits

- STE rules, `ste-lint.py`, and the STE examples come from [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) by Dustin Yuchen Teng, MIT.
- The AI-tell patterns come from the `humanizer` skill, MIT, which adapts Wikipedia's "Signs of AI writing".

## License

MIT. See [LICENSE](LICENSE).
