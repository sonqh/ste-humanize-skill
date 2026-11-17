# Design

## Context

`SKILL.md` has two modes and two tasks. A reply is Human mode. The table in `references/doc-shapes.md` has one row for a status update or a reply, for a reader who has the context. `references/terms.md` says that the sentence rules and the AI tells apply in any language. `SKILL.md` has 1894 words, 6 under the cap of 1900. `evals/eval.py` lints each output and fails it on a hard finding. On Vietnamese text, `long-sentence` counts syllables, so a sentence of 20 Vietnamese words fails.

The sources of this design:

- The draft-response skill in `anthropics/knowledge-work-plugins`: the order of a reply, the length for each channel, the check of promises, "I" and "we".
- Mailchimp, voice and tone: the state of the reader sets the tone, and the voice stays.
- GOV.UK writing guidelines: plain words, contractions.
- Nielsen Norman Group, four dimensions of tone.
- Zendesk, guidelines for AI replies: phrases to avoid.

## Goals / Non-Goals

**Goals:**
- A reply to an upset user that is not technical opens with the answer, in plain words, with one sentence for the problem at most.
- A message made from an internal note keeps every hedge and adds no promise.
- A refusal says the no first.
- The same rules hold in English and in Vietnamese.

**Non-Goals:**
- No change in the linters. Change 018 can add the phrase lists and a Vietnamese sentence length.
- No templates with blanks, no emoji, no humor.
- No process of many turns with the user. The output stays the text.
- No language other than English and Vietnamese in the message rules.

## Decisions

- 017/D1 A message is not a third mode or a third task. It is Human mode. Its rules go in a new file, `references/messages.md`, with one route row: "The text is a reply or a message to a user or a customer". The alternative was a third mode. It breaks REQ-SKILL-001 and costs words that `SKILL.md` does not have. Refs: REQ-SKILL-021
- 017/D2 A message made from an internal note, a ticket, or a thread is a Write. The material is input, and the reader is someone else. A message the user wrote and wants better is a Rewrite. The limits of a Write stay: every condition goes in, and no fact enters that the material does not give. Refs: REQ-SKILL-021, REQ-SKILL-008
- 017/D3 Before the first sentence, the writer decides the state of the reader: calm, confused, or upset. The tone follows the state. The voice and the facts stay. Refs: REQ-SKILL-021
- 017/D4 A reply has this order:
  1. When something went wrong or the reader is upset, one sentence that names the problem. No more than one.
  2. The answer, or the action the reader takes.
  3. The next step: who does it and when, with a date.
  4. One closing sentence, or none.

   Item 1 does not break "answer first", because it is one sentence that the reader needs before the answer. Refs: REQ-SKILL-021
- 017/D5 The channel sets the length. A chat reply has 1 to 4 sentences. A ticket reply has 1 to 3 short paragraphs. An email has 5 paragraphs at most. Refs: REQ-SKILL-021
- 017/D6 For a reader who is not technical, say what the reader sees and what they do, not how the system works. Use the common word: "buy", not "purchase". Explain a term inside the sentence that first uses it. Keep an error text or a button name exact, because the reader must find it. Refs: REQ-SKILL-021, REQ-SKILL-006
- 017/D7 A message adds no promise, date, refund, price, or plan that the material does not give. A hedge stays. "We expect a fix on Friday" stays, and it does not become "We will fix it on Friday". When the reader needs a date that the material does not give, the writer names it on a `Missing:` line. Use "I" for a promise of one person and "we" for a promise of the team. Refs: REQ-SKILL-021, REQ-SKILL-018
- 017/D8 Bad news and a refusal start with the no. Then the reason in plain words. Then the closest option, when the material gives one. Do not blame the reader. Refs: REQ-SKILL-021
- 017/D9 English messages allow a positive contraction such as "you'll" or "we're". They do not use a negative contraction such as "can't" or "don't", because a reader can miss the "not". Documents keep no contractions. Do not use these phrases:
  - "unfortunately", "please note"
  - "we apologize for any inconvenience", "rest assured"
  - the stock offer to answer more questions, "hope this helps"
  - a vague date such as "soon" or "shortly"

  Refs: REQ-SKILL-021
- 017/D10 A Vietnamese message keeps one pair of pronouns from start to end. Examples are "em" and "anh/chị", "chúng tôi" and "quý khách", or "mình" and "bạn". The pair comes from the message of the customer, or from a sample of the user. Other rules:
  - "Dạ" and "ạ" appear once at most.
  - Do not use the stock phrases of Vietnamese support text. Examples are "rất tiếc vì sự bất tiện này" and "trong thời gian sớm nhất". `references/messages.md` holds the list.
  - Do not copy English structure. Write "Bạn kiểm tra lại mật khẩu", not "Vui lòng thực hiện việc kiểm tra mật khẩu".
  - Terms follow `references/terms.md`.

  Refs: REQ-SKILL-021
- 017/D11 `references/doc-shapes.md` gains two rows. A support reply has a reader with one problem who may not know the product well. A notice to customers has a reader who must learn of an outage, a change, or a refusal, and what it means for them. Refs: REQ-SKILL-021
- 017/D12 `SKILL.md` gains the route row and the trigger "reply to a customer". `## Credits` becomes one line that names `LICENSE` and keeps the note on ASD-STE100. `LICENSE` already names both sources. Refs: REQ-SKILL-021
- 017/D13 A fixture may list rules in `lint_disable`. The scorer drops their findings before the check `lint-hard`. The Vietnamese fixtures list `long-sentence`, because the linter counts syllables. The scorer also reads "Dưới đây là" and "Chắc chắn rồi" as a preamble. Refs: REQ-EVAL-006
- 017/D14 Six fixtures, three cases in English and in Vietnamese:
  - a reply to an upset user who is not technical
  - a message to a customer from an engineering note that holds a hedged date
  - a refusal of a feature request.

   Each version runs three times. One agent runs all six fixtures for one version, so six agents run in all. Refs: REQ-EVAL-006, REQ-SKILL-021
- 017/D15 The first run changed the check of the two refusal fixtures. Each email opened with a subject line, and the scorer reads "Subject:" as the first sentence, so `answer-first` failed in every run of both versions. The fixtures now use `early`. The no must start in the first 16 words in English and the first 18 in Vietnamese. That leaves room for a subject line and a greeting. The limits were set after the author read the outputs. Refs: REQ-EVAL-006

## Risks / Trade-offs

- A message reads `references/messages.md` and `references/human.md`, about 1500 words more than now.
- The author of the fixtures also wrote the rules. The record says so.
- One agent runs six fixtures, so a fixture can see the one before it. The fixtures run in the same order for both versions.
- The Vietnamese outputs get no check of sentence length until change 018.
