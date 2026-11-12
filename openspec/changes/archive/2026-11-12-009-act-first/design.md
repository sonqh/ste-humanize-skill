# Design

## Context

Change 008 ran three long fixtures three times with versions 0.4.0 and 0.5.0. No run lost a fact. Every run failed the word limit of its fixture, and the limits were guesses.

## Goals / Non-Goals

**Goals:**
- A measure of length that follows what the reader does.
- A `Reader:` line only when it tells the owner something new.

**Non-Goals:**
- No rule that removes a fact to make a page short.
- No new rule in `SKILL.md` for the order of a page. The file must stay short.

## Decisions

- 009/D1 A page has no word limit. The reader of a README does two things: starts now, and looks up a detail later. A short page that drops the exit codes fails the second. A long page that hides the install command fails the first. So the test is the place of the first task, not the length. Refs: REQ-EVAL-003
- 009/D2 The six stored outputs of the README fixture already pass that test. The install command starts in the first 120 words and the first `pull` in the first 300. The rule goes into `references/doc-shapes.md`, where an agent reads it for a Write task. It does not go into `SKILL.md`, because the behavior is already there and each line in that file costs every task. Refs: REQ-SKILL-009
- 009/D3 The upper limit of a long fixture is the word count of its material. A rewrite or a page that is longer than its material added words and no facts. Refs: REQ-EVAL-003
- 009/D4 The `Reader:` line appears only when the request does not name the reader. The old text said "when you chose the reader yourself" and "if you cannot ask". A runner prompt that says the agent cannot ask reads as the trigger. The new text names the condition in the request. Refs: REQ-SKILL-003
- 009/D5 `## Two modes` said that the reader in Strict mode "cannot ask". The words are close to "if you cannot ask" in the reader rule. The sentence now says that the reader cannot ask what the writer meant. Refs: REQ-SKILL-003
- 009/D6 The check `early` takes a pattern and a number of words. It passes when the pattern starts before that word in the output. The scorer counts every word of the output, headings and code too, because the reader scrolls past them. Refs: REQ-EVAL-003

## Risks / Trade-offs

- A page can grow with no limit other than its material. The `Cut candidates:` line and the audience fit rules stay the guard against detail the reader does not need.
- The limits of `early` in the README fixture, 120 and 300 words, are choices of the fixture author. They sit well above the stored outputs, so they catch a page that buries the first task and not a page that adds one sentence.
- The six short fixtures keep their old word limits. One of them still fails by about 30 words.
