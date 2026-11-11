# Design

## Context

`SKILL.md` has two modes, Strict and Human. Both describe a rewrite of a text that exists. The rules work at the level of the sentence. The owner also uses the skill to write a new document. In that case no source text exists, so "keep what the text says" has nothing to keep.

## Goals / Non-Goals

**Goals:**
- An agent that writes a new page selects the content from the reader, not from the material.
- A reader gets the answer in the first sentence.
- A long paragraph becomes a list only when the content is parallel.
- A rewrite never removes an idea of the owner without a report.

**Non-Goals:**
- No third mode. REQ-SKILL-001 stays as it is.
- No change in the order of precedence. REQ-SKILL-002 stays as it is.
- No eval that calls a model.
- No hard lint rule for shape. A regex cannot tell reasoning from a list.

## Decisions

- 006/D1 The skill gets a second axis, the task, with two values: `Rewrite` and `Write`. The mode sets the rules. The task sets what the writer may leave out. The alternative was a third mode. It would mix two questions and break REQ-SKILL-001. Refs: REQ-SKILL-008
- 006/D2 In a Rewrite the source is the truth. A part that does not serve the reader stays in the text. The writer names it on a `Cut candidates:` line. The alternative was to cut it. The owner of the text may want that part, and a silent cut loses it. Refs: REQ-SKILL-003, REQ-SKILL-008
- 006/D3 In a Write the material is input: notes, code, a diff, or the conversation. The reader brief decides what goes on the page. Three limits stay. A condition, exception, or limit of a described behavior goes in, and so does a safety condition. No fact enters that the material does not give. Refs: REQ-SKILL-008
- 006/D4 The reader brief has three questions: who reads, what they already know, and what they do after reading. The third question is the test for each part of the page. The writer does not print the brief. Refs: REQ-SKILL-009
- 006/D5 A request to write a page often names no reader. The writer then takes the reader from the kind of page. `references/doc-shapes.md` holds that table, so `SKILL.md` stays short. When the kind of page does not tell either, the writer asks. A writer that cannot ask chooses the most likely reader and reports it on a `Reader:` line, so the owner sees a wrong guess at once. Refs: REQ-SKILL-003, REQ-SKILL-009
- 006/D6 "Answer first" applies to every page and to each section. Pattern 26 keeps its narrower rule for a reply. Refs: REQ-SKILL-009
- 006/D7 Length gets a stop rule and no number: stop when the reader can act. A word budget would be wrong for a reference page and for a reply at the same time. Refs: REQ-SKILL-009
- 006/D8 `## Shape: bullets first` becomes `## Shape: fit the content`. A table maps content to shape. Reasoning stays prose. The old title told an agent to prefer bullets, and the owner wants bullets only where they help. Refs: REQ-SKILL-010, REQ-SKILL-006
- 006/D9 The paragraph limit is 6 sentences in the skill and in the linter. It is the STE limit, and `SKILL.md` already states it. One number in both places is easier to keep true than two. Refs: REQ-SKILL-010, REQ-STE-004
- 006/D10 The three shape checks live in `scripts/ste-lint.py`, outside the `RULES` table. They need a prose block, and the table holds one regex for each line. All three are advisory, so no file in this repo can fail on them. Refs: REQ-STE-004
- 006/D11 The newcomer page rules move from `SKILL.md` to `references/doc-shapes.md`. They apply to one kind of page. An agent reads them only when it writes that page. Refs: REQ-SKILL-005
- 006/D12 The word cap rises from 2400 to 2800. The move in 006/D11 frees about 150 words. The new sections need about 600. Refs: REQ-SKILL-004
- 006/D13 The precedence list keeps its five items and its order. Item 1 gains one sentence: in a Write task, the reader brief decides which facts the reader needs. Refs: REQ-SKILL-008

## Risks / Trade-offs

- A Write can leave out a part that the reader needs. The three limits in 006/D3 hold the parts that cause harm when they are missing. The `Reader:` line shows a wrong guess.
- A `Cut candidates:` line adds text after a rewrite. It appears only when there is a candidate, and Embedded mode still returns the final text only.
- The shape checks use a regex and will give false findings. They are advisory and each one can be turned off with `--disable`.
- The contract tests still read `SKILL.md` for strings. They prove that the rule is written, not that an agent follows it. The eval in a later change covers that.
- The cap rises a second time. The next rule should move detail into `references/` before it raises the cap again.
