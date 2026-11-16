# Review of a page

Read this file when the user asks you to review a page, check whether it is ready, or say what is missing. A review points at problems. The author keeps the text and makes the changes.

## Steps

1. Find the reader. Take the reader from the request. If the request names none, take the usual reader of this kind of page from the table in `references/doc-shapes.md`.
2. Find the questions of that reader. When `references/page-guides.md` has a guide for this kind of page, use its questions in their order. Otherwise write them with `## Reader questions` in `references/doc-shapes.md`.
3. For each question, find the part of the page that answers it. Note the heading. Decide whether the answer is complete, partial, or absent.
4. When the page is about work not built yet, apply `## Work not built yet` in `references/page-guides.md`. Look for a number with no kind, a gap with no `TBD`, a `TBD` with no owner, and a missing option to do nothing.
5. Read the title, the first paragraph, and the headings only. Check that the reader can say what the page gives them or asks of them.
6. Run `python3 scripts/lint.py FILE` on the page. Count the hard findings and note the three rules that occur most.
7. Choose the other findings, up to 7, the most severe first.

## Output

The review has four parts, in this order:

1. The verdict, in one or two short sentences. The first sentence names the reader and says "ready" or "not ready". Do not write "nearly ready": the reader must know whether to act. When the page is not ready, the second sentence names the one gap that stops the reader most.
2. A table with one row for each reader question, in the order of step 2.
3. The other findings, 7 or fewer, as bullets.
4. One line with the result of `scripts/lint.py`.

The table has this form:

| Question | Answered | Where | Gap |
|---|---|---|---|
| What do we propose? | Partly | Design | No interface for the export job |

- Answered is Yes, Partly, or No.
- Where names the heading of the page, or "nowhere".
- Gap says in a few words what the reader does not get. Leave it empty when the answer is Yes.

Order the other findings by this list, the most severe first:

1. A number with no source, or a claim that may be wrong.
2. A missing condition, risk, or way back.
3. A part in the wrong order, such as a request in the last paragraph.
4. A claim with no kind, or a `TBD` with no owner.
5. A part that answers no question of the reader.

Each finding names the place, the problem, and a fix in one clause. "Rollout: no way back. Name the flag or the switch that turns the export off."

The lint line gives the count and the rules: "Lint: 4 hard findings, mostly long-sentence and phrasal-verb." When there are none, write "Lint: no hard findings."

## Limits

- Do not rewrite the page. A fix may quote one short phrase. When the user asks for the rewrite after the review, that is a Rewrite task.
- Do not add a fact. Name what is missing, and do not supply the value.
- When you cannot check a fact, say so in the finding: "not checked".
- When the page is ready, say so in the verdict. Do not add findings to fill the space.
- Apply the sentence rules and the AI tells to the review itself.
