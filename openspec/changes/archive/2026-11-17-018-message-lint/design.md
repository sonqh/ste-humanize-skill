# Design

## Context

`scripts/tells-lint.py` holds its rules in one table, `RULES`. REQ-TELLS-001 names the 9 hard rules and REQ-TELLS-002 the 10 advisory rules. `scripts/ste-lint.py` reports `long-sentence` above 25 words. It counts whitespace tokens, so in Vietnamese it counts syllables. `references/messages.md` holds the phrase lists of change 017. The 18 Vietnamese outputs of the 017 run hold 202 sentences of 3 syllables or more. The longest has 29 syllables, and 95 percent have 22 or fewer.

## Goals / Non-Goals

**Goals:**
- The linter finds the phrases that `references/messages.md` forbids, in both languages.
- A Vietnamese sentence gets a length check that a good sentence passes.
- No hard finding is new on a markdown file of the repository.

**Non-Goals:**
- No check of the pair of pronouns. A regex cannot tell which pair the writer chose.
- No new hard rule except the Vietnamese form of `not-x-but-y`.
- No language other than English and Vietnamese.

## Decisions

- 018/D1 The five new rules are advisory. A document can use "soon" or "unfortunately" with good reason, and an advisory finding does not fail the run. The alternative was hard rules. They would fail the docs of the repository that quote the phrases. Refs: REQ-TELLS-005, REQ-TELLS-002
- 018/D2 `support-cliche` holds the stock phrases of `## English` and `## Vietnamese` in `references/messages.md`. Examples are "please note", "rest assured", "bất tiện này", and "mong quý khách thông cảm". "hope this helps" stays in the hard rule `chat-residue`. Refs: REQ-TELLS-005
- 018/D3 `vague-date` holds a time with no date:
  - English: "soon", "shortly", "in the coming days", "as soon as possible", "ASAP"
  - Vietnamese: "thời gian sớm nhất", "sớm nhất có thể", "trong vài ngày tới", "sắp tới"

  Refs: REQ-TELLS-005
- 018/D4 `blame-phrase` holds a phrase that says what the reader did wrong:
  - English: "you failed to", "you forgot to", "you neglected to", "you should have", "due to your error"
  - Vietnamese: "anh", "chị", "bạn", or "quý khách", then "đã quên" or "nhập sai"

  Refs: REQ-TELLS-005
- 018/D5 `negative-contraction` matches "can't", "don't", "won't", and the other negative forms, with a straight or a curly apostrophe. Refs: REQ-TELLS-005
- 018/D6 `particle-repeat` fires once per file when "dạ" or "ạ" occurs more than once as a whole word. It reports the second occurrence. Refs: REQ-TELLS-005
- 018/D7 `not-x-but-y` also matches "không phải" and then "mà là" or "mà" within 60 characters of one sentence. Refs: REQ-TELLS-001
- 018/D8 A sentence is Vietnamese when 30 percent or more of its words hold a letter that English does not use. Examples are "đ", "ư", and a tone mark. The cap of a Vietnamese sentence is 35 syllables. No sentence of the 017 run goes over it. The sentence of 43 syllables that change 017 tested fails it. The message says "syllables". Refs: REQ-STE-005
- 018/D9 The six fixtures of change 017 keep their checks. The three Vietnamese fixtures drop `lint_disable`. The scorer still reads the key, so REQ-EVAL-006 does not change. The outputs of the 017 run are scored again, and no agent runs. Refs: REQ-STE-005, REQ-EVAL-006

## Risks / Trade-offs

- `vague-date` can fire on "soon" in a document that has no date to give. It is advisory.
- The cap of 35 comes from 18 outputs of one run. A longer sentence that is still clear fails it. The author can name the reason, or split it.
- A text that mixes English and Vietnamese in one sentence can fall on either side of the 30 percent line.
- This change is stacked on change 017. Merge and archive 017 first.
