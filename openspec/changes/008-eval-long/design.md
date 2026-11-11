# Design

## Context

`evals/` holds six short fixtures and a scorer for one folder of outputs. The scorer calls no model. A runner writes the outputs.

## Goals / Non-Goals

**Goals:**
- A fixture long enough that an agent can lose a fact in the middle.
- A score over several runs, so that one unlucky run does not decide the result.

**Non-Goals:**
- No change in the skill text. This change measures. It does not tune.
- No judge model.
- No statistics beyond a count of runs. Three runs are too few for more.

## Decisions

- 008/D1 A long fixture has 600 words or more of material. The set holds three: one Rewrite in Human mode, one Write in Human mode, and one Rewrite in Strict mode. Refs: REQ-EVAL-001
- 008/D2 Each long fixture holds 15 or more `must_contain` patterns. The facts sit in the middle of the material, inside long paragraphs: a condition, an exception, a limit, a hedge. Those are the facts that precedence item 1 of the skill protects. Refs: REQ-EVAL-001
- 008/D3 The Write fixture also lists names that must not appear: a codename, an internal service, a ticket number. They test audience fit. Refs: REQ-EVAL-001
- 008/D4 `score` takes one folder for each run. The alternative was one folder with a file name for each run. A folder for each run keeps the old layout valid, so the outputs of the first eval still score. Refs: REQ-EVAL-002
- 008/D5 With more than one run, the report shows each failed check with the count of runs where it failed. A check that fails in 3 of 3 runs is a finding. A check that fails in 1 of 3 runs is a hint. Refs: REQ-EVAL-002
- 008/D6 `--only` limits the score to named fixtures. A runner can then repeat the long fixtures and leave the short ones out, and no line says that an output is missing. Refs: REQ-EVAL-002

## Risks / Trade-offs

- The material is about 800 words, at the low end of the plan of 800 to 1500. The tool description has 637, which is already long for a tool description.
- The word limits of the long fixtures are guesses of the fixture author. A failed `max-words` check needs a person to read the output.
- A pattern can miss a fact that the writer stated in other words. The report gives the pattern, so a person can read the output and decide.
- The same author wrote the skill text and the fixtures.
