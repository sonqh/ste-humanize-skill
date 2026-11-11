# Page shapes: who reads each kind of page

Read this file for a Write task, or when a Rewrite must change the order of a page. It fills the reader brief when the request names no reader. A reader that the user names overrides the table.

## The usual reader of each page

| Page | Usual reader | What the reader does next | Open with | Leave out |
|---|---|---|---|---|
| README | A person who does not know the project and must decide whether to use it | Decide, install, run one example | One sentence that says what the project does, then the install command | Internal design, history |
| How-to guide | A user with one goal, who knows the product basics | Complete one task | The result, and what the reader needs before the first step. Then numbered steps | Theory, other ways to do it |
| Reference page | A user who looks up one item | Find one fact and leave | What the item is. Then entries in one fixed form, in a table or a list | Narrative, lessons |
| Concept page | A reader who wants to know why the thing works this way | Build a model, then choose | The idea in one or two sentences | Step lists |
| Design note | A reviewer who must approve or challenge a decision | Decide | The decision and the recommendation. Then the options and the trade-offs | Detail the decision does not depend on |
| PR description | A reviewer who knows the codebase and not this change | Review, test, merge | What changes and why. Then how to verify it | A tour of each file. The diff shows it |
| Runbook | An on-call person with little time | Stop an incident | The symptom and the first action | Background. Link it |
| Release note | A user who must decide whether to upgrade | Upgrade, or wait | What changes for the user, breaking changes first | Internal refactors |
| Status update or reply | A person who has the context | Act or decide | The decision or the request | The problem, restated |

Rules that apply to every row:

- One page serves one reader. When two readers need different things, write two pages or two sections, and say at the top of each who it is for.
- A page that mixes two rows fails both readers. A how-to guide that stops to explain theory loses the user in the middle of the task. Link the concept page.
- A template is a list of possible sections. Leave out a section that has nothing to say.
- The title says what the page gives the reader. "Rotate an API key" tells more than "API keys".

## A page for a newcomer

When the reader may not know the domain, order the page so each part needs only the one before it.

1. What the base thing is, in one paragraph. Name it, say where it lives, say what it holds.
2. The problem, in two or three bullets, in words the reader already has.
3. What the tool does about it. A table of before and after works when the rows are parallel.
4. Proof. A clip, a transcript, or a number with a scale the reader has.
5. How to try it. Three commands or fewer.

Explain each term on first use, inside the sentence that uses it. A caption for a clip or a screenshot says what the reader sees, then why it matters. It does not repeat the command.
