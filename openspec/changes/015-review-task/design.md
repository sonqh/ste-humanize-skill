# Design

## Context

`SKILL.md` defines two tasks, Rewrite and Write, under `## Two tasks`. REQ-SKILL-008 says there are exactly two. `SKILL.md` has 1896 words, 4 under the cap. The page guides of change 010 and change 014 hold the reader questions of a README, an ADR, a technical proposal, and a design doc. `## Reader questions` in `references/doc-shapes.md` holds the method for every other page. `evals/eval.py` accepts the tasks Rewrite and Write.

## Goals / Non-Goals

**Goals:**
- A request to review a page gets a fixed form: a verdict, the reader questions in a table, the other findings, and the lint count.
- The review uses the same reader questions that a Write uses, so a review and a Write agree.
- The author keeps the text. The review only points.

**Non-Goals:**
- No review of one sentence or one error message. The rule table in `## Output format` covers that.
- No new tells for decision pages, and no change in the linters.
- No check of facts that the reviewer cannot see.

## Decisions

- 015/D1 A review is not a third task under `## Two tasks`. The two tasks decide what a text may leave out. A review writes no text. It gets a route row and its own file, `references/review.md`. The alternative was a third task in `SKILL.md`. It costs about 50 words that the file does not have, and it changes REQ-SKILL-008 and REQ-SKILL-012. Refs: REQ-SKILL-019
- 015/D2 The reviewer takes the reader from the request, then from the table in `references/doc-shapes.md`. The questions come from the guide in `references/page-guides.md` when the page has one. Otherwise the reviewer writes them with `## Reader questions`. A page about work not built yet also gets the checks of `## Work not built yet`. Refs: REQ-SKILL-019
- 015/D3 The first sentence is the verdict. It names the reader and says whether the page is ready for that reader. When the page is not ready, it names the one gap that stops the reader most. Refs: REQ-SKILL-019
- 015/D4 The table has one row for each reader question, in the order of the guide. The column Answered holds Yes, Partly, or No. Where names the heading of the page. Gap says in a few words what the reader does not get. Refs: REQ-SKILL-019
- 015/D5 Other findings come after the table, 7 or fewer, the most severe first. The order of severity is:
  1. A number with no source, or a claim that may be wrong.
  2. A missing condition, risk, or way back.
  3. A wrong order.
  4. A claim with no kind, or a `TBD` with no owner.
  5. A part that answers no question.

   Each finding names the place, the problem, and a fix in one clause. Refs: REQ-SKILL-019
- 015/D6 The reviewer runs `scripts/lint.py` on the page and reports one line: the count of hard findings and the three rules that occur most. The author can run the linter for each finding. Refs: REQ-SKILL-019
- 015/D7 A review does not rewrite the page and does not add a fact. A fix may quote one short phrase. When the reviewer cannot check a fact, the finding says so. When the page is ready, the review says so and adds no finding to fill the space. Refs: REQ-SKILL-019
- 015/D8 `SKILL.md` gains one route row and the word "review" in its triggers. Its second paragraph repeats the description in the front matter, and gets shorter to pay for both. Refs: REQ-SKILL-019
- 015/D9 `evals/eval.py` adds `Review` to its tasks. A review is text for a person, so the scorer applies the same checks to it. These are the preamble, the first sentence, the word limit, and the lint. Refs: REQ-EVAL-005
- 015/D10 The route row and the shorter second paragraph land in task 2.1, with `references/review.md`. A test asks that each file in `references/` has a route row, so the file cannot come first alone. Task 2.2 keeps the version, the triggers, and the README. Refs: REQ-SKILL-019
- 015/D11 The test of SCN-EVAL-001-1 asked that the fixtures hold exactly the tasks Rewrite and Write. REQ-EVAL-001 asks only that they cover both. The test now asks that the set holds both, so a fixture with the task Review passes. Refs: REQ-EVAL-001, REQ-EVAL-005
- 015/D12 The first eval run changed 015/D3 and a fixture. A verdict in one sentence ran to 30 to 48 words, and some runs wrote "nearly ready". The verdict now takes one or two short sentences. The first says "ready" or "not ready". The first ADR of `review-ready-adr` was not ready. The reviewers found a claim that may be wrong, numbers with no kind, and no option to do nothing. The fixture now gives an ADR that answers each of those. The ADR runs of both versions ran again. Refs: REQ-SKILL-019

## Risks / Trade-offs

- A review that follows a guide can miss a problem that the guide does not name. The other findings leave room for it, 7 at most.
- An agent that reviews a page reads `references/review.md`, the guide, and `references/doc-shapes.md`. That is about 2600 words more than a review without the skill.
- `SKILL.md` stays near the cap. The next rule must go to `references/`.
- This change is stacked on change 014. Merge and archive 014 first.
