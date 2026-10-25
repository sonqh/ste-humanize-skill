# ste-humanize

A Claude Code skill that rewrites English so nobody misreads it and it still sounds like a person wrote it.

## Install

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

## Use

```
/ste-humanize rewrite this README section
Humanize this PR description
Rewrite this error message so an agent cannot misread it
Show the diff
```

- You get the rewritten text back.
- Add "show the diff" or "which rules did it break" to see the rule table.
- The skill picks a mode. Strict is for tool descriptions, error messages, and agent instructions. Human is for docs, READMEs, PR descriptions, and replies.

One example:

```text
Before: It's not just a sync tool, it's a robust, seamless layer. That is the real win.
After:  The tool writes your setup to each agent. Each agent then reads the same rules.
```

More pairs are in [`examples/before-after.md`](examples/before-after.md).

## Lint

One command checks both rule sets: the structural STE rules and the AI tells.

```bash
python3 scripts/lint.py FILE
```

- Each finding prints as `file:line:col rule [level] match`.
- Hard findings fail the run when they exceed `--baseline N` (default 0). Advisory findings never fail it.
- `--only tells` or `--only ste` runs one rule set.
- `--disable rule,rule` turns rules off.
- `--json` prints the findings as JSON.
- The linter flags no hedges and checks no meaning. A clean run means the regex checks found nothing.

## Scope

- Built for documentation, READMEs, design notes, PR descriptions, changelogs, replies in threads, tool descriptions, error messages, and agent-to-agent instructions.
- Not built for fiction, marketing, persuasive copy, or text where voice is the point.
- It does not reproduce ASD's 900-word dictionary. It applies the principle: the plainest common word, used the same way every time. For certified STE documentation, use the real standard.

## Credits

- STE rules, `ste-lint.py`, and the STE examples come from [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) by Dustin Yuchen Teng, MIT.
- The AI-tell patterns come from the `humanizer` skill, MIT, which adapts Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## License

MIT. See [LICENSE](LICENSE).
