# Page shapes: who reads each kind of page

Read this file when the task is Write, or when a Rewrite covers a whole page. It fills the reader brief when the request names no reader. A reader that the user names overrides the table. After the table, read `## Reader questions`. For a README, an ADR, or a technical proposal, read `references/page-guides.md` too.

## The usual reader of each page

| Page | Usual reader | What the reader does next | Open with | Leave out |
|---|---|---|---|---|
| README | A person who does not know the project and must decide whether to use it | Decide, install, run one example | One sentence that says what the project does, then the install command | Internal design, history |
| How-to guide | A user with one goal, who knows the product basics | Complete one task | The result, and what the reader needs before the first step. Then numbered steps | Theory, other ways to do it |
| Reference page | A user who looks up one item | Find one fact and leave | What the item is. Then entries in one fixed form, in a table or a list | Narrative, lessons |
| Concept page | A reader who wants to know why the thing works this way | Build a model, then choose | The idea in one or two sentences | Step lists |
| Design note | A reviewer who must approve or challenge a decision | Decide | The decision and the recommendation. Then the options and the trade-offs | Detail the decision does not depend on |
| ADR | A maintainer who meets the result of the decision later and asks why | Keep the decision, or replace it with a new one | A title that states the decision, then the status and the date | Steps of the implementation, the history of the meetings |
| Technical proposal | A person who approves time or money and has little time | Say yes, say no, or ask one question | The request, the cost, and the date of the decision | Detail the approver does not need. Put it after the plan |
| PR description | A reviewer who knows the codebase and not this change | Review, test, merge | What changes and why. Then how to verify it | A tour of each file. The diff shows it |
| Runbook | An on-call person with little time | Stop an incident | The symptom and the first action | Background. Link it |
| Release note | A user who must decide whether to upgrade | Upgrade, or wait | What changes for the user, breaking changes first | Internal refactors |
| Status update or reply | A person who has the context | Act or decide | The decision or the request | The problem, restated |

Rules that apply to every row:

- One page serves one reader. When two readers need different things, write two pages or two sections, and say at the top of each who it is for.
- A page that mixes two rows fails both readers. A how-to guide that stops to explain theory loses the user in the middle of the task. Link the concept page.
- The first task comes before the reference. A README lets the reader install the tool and run one example near the top. The exit codes, the full list of flags, and the limits go after that part, under a heading such as Reference. A reader who only wants to start can stop there.
- A template is a list of possible sections. Leave out a section that has nothing to say.
- When the repository has a template for this kind of page, keep its headings and their order. Readers and tools find a part by its heading. Apply the reader rules to the title, to the summary, and inside each section.
- The title says what the page gives the reader. "Rotate an API key" tells more than "API keys".

## Reader questions

A reader comes to a page with questions. Use them to order any document, and to rewrite one that has the wrong order.

1. Write the questions the reader brings, in the words of the reader. Three to seven are enough.
2. Put first the question that the reader must answer to act. Put last the questions that only some readers have.
3. Give each question one section. The heading names what the reader looks for. "How to go back" tells more than "Considerations".
4. The first sentence of a section answers its question. The detail comes after it.
5. A part that answers no question on the list has no place. Leave it out of a Write. Name it as a cut candidate in a Rewrite.
6. Test the page. Read only the title, the first paragraph, and the headings. The reader must be able to say what the page gives them or asks of them.

A page can have two kinds of reader. The first reader is the one who acts or decides first. The questions of the first reader come first. The other reader gets sections with clear labels after them.

## A page for a newcomer

When the reader may not know the domain, order the page so each part needs only the one before it.

1. What the base thing is, in one paragraph. Name it, say where it lives, say what it holds.
2. The problem, in two or three bullets, in words the reader already has.
3. What the tool does about it. A table of before and after works when the rows are parallel.
4. Proof. A clip, a transcript, or a number with a scale the reader has.
5. How to try it. Three commands or fewer.

Explain each term on first use, inside the sentence that uses it. A caption for a clip or a screenshot says what the reader sees, then why it matters. It does not repeat the command.
