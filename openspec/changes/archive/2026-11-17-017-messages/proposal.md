# Proposal

## Why

The owner asked on 2026-11-17 for messages as well as documents. The skill must reply to a user who does not know the technology, and turn a text into a message for a customer. Both in English and in Vietnamese.

The skill reads a message as a page. It has no rules for the parts that make a message fail:

- It does not ask if the reader is upset, confused, or calm. A reply to an upset customer gets the same tone as a reply to a teammate.
- It has no order for a reply: what to say first when something went wrong, and where the next step goes.
- It does not stop a promise. A note that says "probably fixed by Friday" can become "fixed by Friday" in the message to the customer.
- It has no list of the stock phrases of support text, in English or in Vietnamese.
- In Vietnamese it has no rule for the pronouns of address, and the linter counts each syllable as a word.

Skills on the market and five style guides show what works. The sources are the draft-response skill of Anthropic, Mailchimp, GOV.UK, Nielsen Norman Group, and Zendesk. The design names what this change takes from each.

## What Changes

- `references/messages.md` is new. It holds the rules for a reply or a message to a user or a customer:
  - the state of the reader
  - the order of a reply
  - the length for each channel
  - plain words for a reader who is not technical
  - promises and bad news
  - a section for English and a section for Vietnamese.
- `SKILL.md` gains one route row and a trigger. `## Credits` gets shorter to pay for them, because `LICENSE` names both sources.
- `references/doc-shapes.md` gains two rows: a support reply and a notice to customers.
- `evals/eval.py` gains the fixture key `lint_disable` and the Vietnamese openers of a preamble. Six fixtures cover three cases, each in English and in Vietnamese.
- The version rises to 0.10.0.

## Capabilities

### Modified Capabilities
- `skill-contract`: messages to users and customers.
- `eval`: fixtures in Vietnamese.

## Impact

- `SKILL.md`, `references/messages.md`, `references/doc-shapes.md`, `README.md`, `.claude-plugin/plugin.json`.
- `evals/eval.py`, `evals/fixtures/`, `evals/runs/`, `tests/test_skill_contract.py`, `tests/test_eval.py`.
- No change in the linters. Change 018 can add the rules for stock phrases, vague dates, and Vietnamese sentence length.
