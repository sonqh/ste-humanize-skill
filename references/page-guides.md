# Page guides: README, ADR, technical proposal, design doc

Read this file when the page is a README, an ADR, a technical proposal, or a design doc. Read it also when the page is about work that is not built yet. Each guide lists the readers, the questions they bring in order, and one test. For an ADR, a technical proposal, or a design doc, read `## G. Decision pages` in `references/ai-tells.md` too. `## Reader questions` in `references/doc-shapes.md` holds the method for every other page.

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
2. Is it still in force? The status and the date. The status is Proposed, Accepted, or Superseded. A replaced ADR names the ADR that replaced it. A Proposed ADR names who decides, and by when.
3. What forced a decision? The context: the problem, the limits, and the facts of that date, with numbers.
4. What exactly did we choose? The decision in active voice: "We will". A Proposed ADR also says "We will", because the status carries the doubt. State the scope and each exception.
5. What decides between the options? Name the criteria before the options: for example the cost, the load on the team, or a limit of time.
6. What else did we look at, and why not? One bullet for each option, with the reason against it. When the options share the criteria, use a table with one row for each option and one column for each criterion.
7. What follows? The consequences, good and bad. Say what becomes harder, and what event must make the team decide again.

An ADR records one decision. Leave out the steps of the implementation and the history of the meetings. For a Proposed ADR, read `## Work not built yet` too.

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

## Design doc

A design doc says what the team will build and why, before the code exists. Read `## Work not built yet` too.

Readers: first, the reviewers who must agree on the design before the work starts. Second, the people who build it. Third, a person who reads it later to learn why the feature works this way.

1. What problem do we solve, and for whom? The problem in one paragraph, with the proof: a measured number, a ticket, or the words of a user.
2. What must the feature do, and what not? Goals and Non-goals, one bullet each. A non-goal stops a request for it later.
3. What do we propose? The design at the level that the reviewers decide on: the parts, the data, and the interfaces.
4. What else did we look at? Each option, with "do nothing" first. Score each option on the same criteria, in a table. Say why each option loses.
5. What do we not know yet? Each unknown, and the spike or the test that answers it before the work depends on it.
6. How do we know that it works? The measure of success: a target with a number, and how the team measures it.
7. How does it go out, and how do we go back? The phases of the rollout, the flag or the switch, and the way back.
8. What is still open? The open questions, each with an owner and a date.

The steps of the build and the estimate of each task go in the plan of the work. Leave them out of the design doc.

Test: a reviewer reads only the title, the goals, and the proposed design. The reviewer can then say what the team will build, what it will not build, and what is still open.

## Work not built yet

Read this section for a design doc, for an ADR with the status Proposed, and for a proposal of a feature in planning. Before the code exists, the material has gaps, and its numbers are of different kinds.

Mark each claim as measured, estimate, target, or assumption, in the sentence that holds it:

- A measured number comes from a test or from production. Give the source and the date. "We measured 350 jobs per second on staging on 2026-10-10."
- An estimate is a number that a person worked out. Give who made it, and from what. "Lan estimates three weeks, from the size of the export job."
- A target is a number that the work must reach. "The target is a p95 below 200 ms."
- An assumption is a statement that the plan depends on and that nobody checked. "We assume that the vendor API stays at version 2."

Rules for a gap:

- Do not invent a number, a date, a name, or a cost. A gap stays a gap.
- Mark a gap in the page with `TBD`, an owner, and a date: "Cost: TBD (Lan, by 2026-12-01)". When the material names no owner, write `TBD (owner unknown)`.
- Put each gap in the section Open questions too, as one question with its owner.
- In a Write task, name each gap on the `Missing:` line after the text.
- Use "will" for the plan and for a decision. Use the present tense only for what is true today. Keep "may" on a risk and on an estimate.
