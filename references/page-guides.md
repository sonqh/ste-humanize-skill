# Page guides: README, ADR, technical proposal

Read this file when the page is a README, an ADR, or a technical proposal. Each guide lists the readers, the questions they bring in order, and one test. `## Reader questions` in `references/doc-shapes.md` holds the method for every other page.

## README

Readers: first, a person who decides whether to use the project. Second, a user who comes back to look up one thing.

1. What is this, and is it for me? One sentence, then one more on who it is for.
2. How do I install it? The command, and what it needs.
3. How do I run one thing that works? One example with its result.
4. What else can it do? The main commands or features, in a list or a table.
5. What does it not do? The limits and the cases it is not built for.
6. Where is the detail? The reference: every flag, the config keys, the exit codes.
7. Where do I get help, and what is the license?

Test: a new reader can run the first example from the top of the page, and does not need to read below it.

## ADR

An ADR is an architecture decision record. Readers: first, a maintainer who meets the result later and cannot ask the authors. Second, a reviewer who must accept the decision now.

1. What did we decide? The title states the decision as a sentence. "Use Redis for user sessions" tells more than "Session storage".
2. Is it still in force? The status and the date. A replaced ADR names the ADR that replaced it.
3. What forced a decision? The context: the problem, the limits, and the facts of that date, with numbers.
4. What exactly did we choose? The decision in active voice: "We will". State the scope and each exception.
5. What else did we look at, and why not? One bullet for each option, with the reason against it.
6. What follows? The consequences, good and bad. Say what becomes harder, and what event must make the team decide again.

An ADR records one decision. Leave out the steps of the implementation and the history of the meetings.

Test: a maintainer who reads it a year later can say what the team decided, why, and what would make the decision wrong.

## Technical proposal

Readers: first, the person who approves, with about two minutes. Second, the reviewers who test the design and the risk. Third, the people who build it.

1. What do you want from me, and by when? The request and the date, in the first paragraph.
2. What do we get, and what does it cost? The gain as a number with a scale. The cost in time, money, and people.
3. What happens if we do nothing?
4. Which options are there, and why this one? A table when the options share attributes.
5. What can go wrong, and how do we go back? Keep each "may" and "not tested". Name the way back.
6. What is not known yet? The open questions.
7. How will the work run? The plan and the phases, for the people who build it.
8. The detail of the design comes last, for the reviewers.

Test: an approver who reads only the first paragraph can say yes, say no, or name the one question that stops them.
