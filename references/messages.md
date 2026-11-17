# Messages to users and customers

Read this file when the text is a reply or a message to a user or a customer. Examples are a chat reply, a ticket reply, an email, and a notice. It adds to `SKILL.md` and `references/human.md`. A message is Human mode.

## Before you write

- Pick the task. A message made from an internal note, a ticket, or a thread is a Write. The material is input, and the reader is someone else. A message that the user wrote and wants better is a Rewrite.
- Decide the state of the reader: calm, confused, or upset. Take it from the message of the reader, then from the request. The state sets the tone. The voice and the facts stay the same.
- An upset reader wants the problem named once and the fix next. A confused reader wants one step at a time. A calm reader wants the answer and nothing more.

## Order of a reply

1. When something went wrong, or the reader is upset, write one sentence that names the problem. Write no more than one.
2. The answer, or the action the reader takes.
3. The next step: who does it and when, with a date. "Minh sends the new invoice on 3 March."
4. One closing sentence, or none.

The sentence of item 1 does not break "answer first". The reader needs to know that you understood the problem before they read the fix. Leave out item 1 when nothing went wrong.

## Length by channel

| Channel | Length |
|---|---|
| Chat | 1 to 4 sentences |
| Ticket reply | 1 to 3 short paragraphs |
| Email | 5 paragraphs at most |
| Notice to many customers | What happened, what it means for the reader, what they do. Then the detail |

A reader of a chat reads on a phone. Put a step list in a chat only when the reader must do 3 steps or more.

## A reader who is not technical

- Say what the reader sees and what they do. Do not say how the system works. "Your payment did not go through" tells more than "The gateway returned a 502".
- Use the common word: "buy", not "purchase", "help", not "assist", "about", not "approximately".
- Explain a term inside the sentence that first uses it. Then use the same term each time.
- Keep an error text, a button name, or a menu name exact. The reader must find it on the screen.
- Leave out an internal name: a service, a ticket number of the team, or the name of a database. Keep a reference number that the reader must quote to you.

## Promises

A message adds no promise, date, refund, price, or plan that the material does not give. This is the rule that a message breaks most, because a promise makes a reply sound kind.

- A hedge stays. "We expect a fix on Friday" stays. It does not become "We will fix it on Friday".
- An engineer who writes "probably" gives an estimate. The customer gets an estimate, in plain words.
- When the reader needs a date or an answer that the material does not give, do not write it. Name it on a `Missing:` line in a Write task. The sender finds it before they send.
- Use "I" for a promise that one person makes, and "we" for a promise of the team.
- Do not promise an outcome that another team decides, such as a refund or a feature.

## Bad news and refusals

1. Say the no, or the bad news, in the first sentence.
2. Give the reason in plain words, in one or two sentences.
3. Give the closest option the reader has, when the material gives one.

- Do not blame the reader. "The file was larger than 10 MB" tells the fact. A sentence that says what the reader did wrong only tells them they failed.
- Do not hide the no in the middle of thanks and regrets.
- Write positively only when it changes no fact. "You can export up to 10 MB" is fine. A reply that never says "no" to a refusal is not.

## English

- Use a positive contraction such as "you'll", "we're", or "it's". It sounds like a person.
- Do not use a negative contraction such as "can't", "don't", or "won't". Write "cannot", "do not", "will not". A reader can miss the "not" in a contraction. Documents keep no contractions at all.
- Do not use these phrases. Each one says nothing or delays the point:
  - "unfortunately", "please note"
  - "we apologize for any inconvenience", "sorry for any inconvenience"
  - "rest assured", "we value your feedback", "we understand your frustration"
  - "don't hesitate to reach out", "feel free to contact us", "hope this helps"
- Write a date, not "soon", "shortly", or "in the coming days". When no date exists, say that, and say when you will write again.
- One apology at most, for a real fault. "I'm sorry the export failed twice" names the fault.
- One exclamation mark at most in a message, and none in bad news.

## Vietnamese

Apply every sentence rule and every AI tell in Vietnamese. `references/terms.md` decides which terms stay in English.

- Keep one pair of pronouns from start to end. Examples are "em" and "anh/chị", "chúng tôi" and "quý khách", or "mình" and "bạn". Take the pair from the message of the customer, or from a sample of the user. When neither gives one, use "chúng tôi" and "anh/chị" in an email, and "mình" and "bạn" in a chat.
- "Dạ" and "ạ" appear once at most in a message. In each sentence they read as a template.
- Do not use these phrases. Each one says nothing or delays the point:
  - "rất tiếc vì sự bất tiện này", "xin lỗi vì sự bất tiện"
  - "trong thời gian sớm nhất", "trong thời gian sớm nhất có thể"
  - "mong anh/chị thông cảm", "mong quý khách thông cảm"
  - "hy vọng thông tin trên hữu ích", "đừng ngần ngại liên hệ"
  - "chúng tôi luôn lắng nghe", "chúng tôi trân trọng ý kiến"
- Do not copy English structure. Write a verb, not "thực hiện việc" or "tiến hành" in front of a noun. "Bạn kiểm tra lại mật khẩu" tells more than "Vui lòng thực hiện việc kiểm tra mật khẩu".
- Use "vui lòng" once at most, for a request the reader must do.
- "Không phải X mà là Y" is the same tell as in English. State Y.
- Write a date as "thứ Sáu, 3/3" or "3/3/2027", not "sắp tới" or "trong vài ngày tới".
- One sentence holds one idea. The linter counts a Vietnamese sentence by syllables, with a cap of 35.

## What the linter finds

`python3 scripts/lint.py FILE` reports five advisory rules for messages, in both languages: `support-cliche`, `vague-date`, `blame-phrase`, `negative-contraction`, and `particle-repeat`. It reports "Không phải X mà là Y" as the hard rule `not-x-but-y`. It cannot tell if the pronouns stay the same from start to end. Check that yourself.
