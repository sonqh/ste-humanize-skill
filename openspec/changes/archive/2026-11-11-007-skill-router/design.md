# Design

## Context

Change 006 added the reader rules and raised `SKILL.md` to 2795 words. The file mixes three kinds of rule. Some apply to every text. Some apply in Human mode only. Some apply only when the agent writes a new page or meets a term in another language.

## Goals / Non-Goals

**Goals:**
- An agent reads only the rules that apply to its mode and task.
- Each rule has one home. A rule for one mode does not hide in a section for all modes.
- The owner can measure what an agent writes before and after a change in the skill.

**Non-Goals:**
- No rule is removed or changed in meaning, except the one in 007/D5.
- No model call in the tests or in the CI gate.
- No judge model in the scorer. The checks are mechanical.

## Decisions

- 007/D1 `SKILL.md` holds the rules for every text. They are the modes, the tasks, the reader brief, the precedence, the sentence rules, the shape, the process, the output, and the boundaries. The alternative was a thin index with every rule in `references/`. An agent that skips one read would then lose a core rule. Refs: REQ-SKILL-011
- 007/D2 A table `## What to read` maps a case to one file. Process step 1 sends the agent to that table. Each reference file says in its first lines when to read it. Refs: REQ-SKILL-011
- 007/D3 Strict mode needs no extra file for most texts. `## Two modes` states all of its exceptions in one paragraph: keep every identifier, keep the tone flat, and remove only two kinds of AI tell. Refs: REQ-SKILL-011
- 007/D4 `references/human.md` owns the voice rules, the audience fit rules, the AI tell groups, and the table of conflicts between STE and the humanizer. Audience fit changed three rules in other sections of `SKILL.md`. The file now lists those three changes in one place. Refs: REQ-SKILL-006, REQ-SKILL-011
- 007/D5 `references/ai-tells.md` has 2217 words. Before, the skill told the agent to read it for every rewrite in Human mode. Now the agent reads it when the source sounds like a chatbot, or when it cannot tell whether a phrase is a tell. The groups in `references/human.md` name every pattern. This is the one change in behavior. Refs: REQ-SKILL-011
- 007/D6 The STE rules in `SKILL.md` are one line each, under `## Sentence rules`. The lines with examples move to `references/ste-rules.md`. The linter reports most of these rules, so the agent gets a second signal. Refs: REQ-SKILL-011
- 007/D7 The cap falls to 1900 words. `SKILL.md` has 1807. The plan was 1000 to 1200. The rules for every text need about 1800 words. A lower number means a removed rule, and the eval must show first that the removal is safe. Refs: REQ-SKILL-004
- 007/D8 The eval has two parts. A fixture is a JSON file with a request, the material, and the checks. The scorer reads one output file for each fixture and applies the checks. It calls no model. A runner makes the outputs: an agent with the skill, or a person. Refs: REQ-EVAL-001, REQ-EVAL-002
- 007/D9 The checks are mechanical. They test that a fact stays, that a source-level name goes, and that the first sentence holds the answer. They also test the shape, a word limit, and the hard findings of the linter. A judge model would see more, but its score changes between runs. Refs: REQ-EVAL-002
- 007/D10 The runner prompt names the skill folder, the request, and the material. It names no check, so the agent cannot write to the test. Refs: REQ-EVAL-002
- 007/D11 `evals/` stays out of the release archive, as `tests/` does. Refs: REQ-SKILL-004

## Risks / Trade-offs

- An agent can skip the read of a reference file. The core rules stay in `SKILL.md`, so the loss is the voice rules or the audience fit rules, not the meaning rules.
- 007/D5 can let a weak AI tell pass. The linter still reports the hard ones.
- A mechanical check can pass a bad text and fail a good one. A check for a fact uses a pattern, and a writer can state the fact in other words. Read the output when a check fails.
- One run per fixture is a small sample. A difference of one check between two versions is noise.
- The scorer does not test meaning. A text can keep each fact and still state a wrong relation between them.
