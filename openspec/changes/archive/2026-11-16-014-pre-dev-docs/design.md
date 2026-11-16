# Design

## Context

Change 010 added `references/page-guides.md` with a guide for a README, an ADR, and a technical proposal. The ADR fixture is a thread where the team agreed. `SKILL.md` has 1892 words, 8 under the cap. `evals/eval.py` knows three trailers.

## Goals / Non-Goals

**Goals:**
- A page about work not built yet tells the reader which claims are facts and which are not.
- A gap in the material shows in the page and after it. It never turns into an invented number.
- A design doc and an ADR with the status Proposed get the questions of their readers in order.

**Non-Goals:**
- No task Review. That is a later change.
- No new tells for decision pages, and no change in the linters.
- No template files. The template rule of 010/D6 stays.

## Decisions

- 014/D1 The rules for work not built yet live in one section, `## Work not built yet`, in `references/page-guides.md`. The design doc, the Proposed ADR, and the proposal all read it. One copy keeps the three guides the same. Refs: REQ-SKILL-016
- 014/D2 A claim has one of four kinds: measured, estimate, target, or assumption. A measured claim gives the source and the date. An estimate gives who made it and from what. The writer marks the kind in the sentence: "We measured", "We estimate", "The target is", "We assume". A label column was the alternative. A sentence keeps the kind next to the number when someone copies it. Refs: REQ-SKILL-016
- 014/D3 A gap gets `TBD`, an owner, and a date in the page, for example "Cost: TBD (Lan, by 2026-12-01)". When the material gives no owner, the mark is `TBD (owner unknown)`. Each gap also goes to the section of open questions. Refs: REQ-SKILL-016
- 014/D4 The trailer `Missing:` names each gap in one line after the text, in a Write task only. In a Rewrite the source is the truth, so a gap there is the choice of the owner. The trailer tells the user what to find before the page goes out. Refs: REQ-SKILL-018
- 014/D5 The design doc guide is a new guide, not a change to `## Technical proposal`. A proposal asks an approver for time or money. A design doc asks reviewers and builders to agree on what to build. The first reader differs, so the first question differs. Refs: REQ-SKILL-017
- 014/D6 The design doc asks eight questions in this order:
  1. The problem and the proof of it.
  2. Goals and non-goals.
  3. The proposed design.
  4. The options, with "do nothing".
  5. The unknowns, and how to learn them.
  6. The measure of success.
  7. The rollout and the way back.
  8. The open questions.

  Refs: REQ-SKILL-017
- 014/D7 An ADR with the status Proposed still says "We will". The status carries the doubt, so the decision sentence needs no hedge. The ADR names its criteria before the options, and a table scores each option on the same criteria. Refs: REQ-SKILL-017
- 014/D8 `SKILL.md` loses `## Resources`. Step 3 of `## Process` already names `scripts/lint.py`. The room pays for one route row and the `Missing:` bullet. Refs: REQ-SKILL-018
- 014/D9 `evals/eval.py` adds `Missing:` to its tuple of trailers. Without it, the scorer lints the line as part of the body. Refs: REQ-EVAL-004
- 014/D10 `## Resources` freed too few words. `SKILL.md` also loses the Boundaries line on STE compliance, and the route row stays short. The rule on the STE dictionary in `## Sentence rules` now says "Do not claim STE compliance". The advice to use the real standard for aircraft documentation goes. The file has 1896 words. Refs: REQ-SKILL-018

## Risks / Trade-offs

- A page with many `TBD` marks can look unfinished to an approver. That is true of the page, and the reader must see it.
- A writer can mark a guess as an estimate to make it look firmer. The rule asks for who made the estimate and from what, so the reader can judge it.
- `page-guides.md` grows by about 450 words. An agent reads it only for the pages that the route row names.
- `SKILL.md` stays near the cap. The next rule must go to `references/`.
