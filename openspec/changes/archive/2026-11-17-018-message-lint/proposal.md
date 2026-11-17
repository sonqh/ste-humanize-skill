# Proposal

## Why

Change 017 gave the skill rules for messages to users and customers, in English and in Vietnamese. The linter does not check them yet:

- It finds none of the stock phrases of support text, such as "we apologize for any inconvenience" or "trong thời gian sớm nhất".
- It finds no vague date, such as "soon" or "sắp tới".
- It does not see "Không phải X mà là Y", the Vietnamese form of a hard tell.
- It counts each Vietnamese syllable as a word. A Vietnamese sentence of 20 words fails the cap of 25. The fixtures of change 017 turn off `long-sentence` for this reason.

## What Changes

- `scripts/tells-lint.py` gains five advisory rules: `support-cliche`, `vague-date`, `blame-phrase`, `negative-contraction`, and `particle-repeat`. Each one has a list in English and, where it applies, in Vietnamese.
- `not-x-but-y` also matches "không phải ... mà là". It stays a hard rule.
- `scripts/ste-lint.py` counts a Vietnamese sentence by syllables, with a cap of 35.
- The Vietnamese fixtures of change 017 drop `lint_disable`. The outputs of the 017 run are scored again with the new linter.
- `references/messages.md` and `README.md` name the new rules. The version rises to 0.11.0.

## Capabilities

### Modified Capabilities
- `tells-lint`: rules for messages, and the Vietnamese contrast.
- `ste-lint`: the length of a Vietnamese sentence.

## Impact

- `scripts/tells-lint.py`, `scripts/ste-lint.py`, `tests/test_tells_lint.py`, `tests/test_ste_lint.py`.
- `references/messages.md`, `README.md`, `SKILL.md`, `.claude-plugin/plugin.json`, `evals/fixtures/`.
- This change is stacked on change 017, which is not merged.
