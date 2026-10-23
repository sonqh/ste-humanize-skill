# AI writing tells: the full pattern list

This file holds the patterns the humanizer side of `ste-humanize` checks, with a before and after for each. SKILL.md carries the short form. The patterns come from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup, as adapted in the MIT-licensed `humanizer` skill.

Why these patterns exist: a language model writes what is most likely to come next, so by default it makes the choice that fits the widest range of readers. A person chooses for one reader and one subject, so their choices are uneven and specific. Every pattern below is one form of the default choice.

Two rules follow. Every sentence you keep must add something the reader did not already have. A tell counts in proportion to how rarely a careful writer would make it on purpose. Patterns 1 to 5 justify an edit on one sighting. A pattern marked *weak alone* needs company before you act.

## A. Staging instead of stating

### 1. Not X but Y

Watch for: not X but Y; not just, not only, not merely X, but Y; it's not X, it's Y; X rather than Y; the same contrast split across sentences ("This does not mean X. It means Y."); a clipped negative tail ("..., no guessing").

Problem: the negative half names something no one claimed, so the positive half sounds larger. State the point. Keep a contrast only when the negative half corrects a belief the reader holds.

Before: It's not just about the beat under the vocals; it's part of the aggression. It's not merely a song, it's a statement.
After: The heavy beat adds to the aggressive tone.

Before (split): This does not mean every choice is equal. It means there is no external system that confirms which choice is right.
After: No external system confirms which choice is right, although the choices still have different consequences.

### 2. One-line closers and dramatic fragments

Watch for: a one-sentence paragraph that restates the paragraph before it; "That is the real win."; "Read that again."; the same closer after several sections; a sentence after an example that names what it showed; a row of fragments; one word in ALL CAPS or with periods between words.

Problem: the line asks the reader to pause on a claim instead of adding to it. Cut a closer that repeats. Keep it when it adds a fact or a consequence the example does not show.

Before: Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.
After: AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

### 3. Sayings that sound deep

Watch for: the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter, X is the Y of Z, X becomes a trap, the language of, the currency of, the architecture of.

Problem: an ordinary point is dressed as a hidden truth. Replace the saying with the specific claim.

Before: The real question is whether teams can adapt. At its core, what really matters is organizational readiness.
After: The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.

### 4. Staged run-up before the point

Watch for: Let's dive in, let's explore, let's break this down, here's what you need to know, without further ado, heads up, quick note, Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk.

Problem: the writer announces the point instead of making it. Remove the run-up.

Before: Let's dive into how caching works in Next.js. Here's what you need to know.
After: Next.js caches data at several layers: request memoization, the data cache, and the router cache.

### 5. Arguing with no one

Watch for: This isn't (mainly) about, I'm not saying, To be clear, Don't get me wrong, This is not to say, Some might say... but, A tempting approach would be, One might be tempted to, You might think... but.

Problem: the text answers an objection that appears nowhere else. Remove the defense. Keep an objection the text attributes or answers in full.

Before: Session tokens rotate every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place.
After: Session tokens rotate every 24 hours, in place, and clients refresh without a restart.

## B. Rhythm by rule

### 6. Forced triads

Problem: ideas arrive in threes to sound complete. Check that each item adds a distinct idea. Keep three real items when the meaning needs three.

Before: The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.
After: The event includes talks and panels. There is also time for informal networking between sessions.

### 7. Repeated sentence openings

Problem: several sentences in a row start with the same subject. Merge or vary. Do not ban the word. *Weak alone.*

Before: She noted the door. She noted the lock on it. She filed both away.
After: She noted the door and its lock, then filed both away.

### 8. Dashes as the universal connector

Rule: the final text must not contain em dashes or en dashes unless the writer's sample uses them. Replace each with a period, comma, colon, or parentheses. Leave dashes inside code, paths, and URLs alone.

Before: The new policy, announced without warning, affects thousands of workers. (The original had two dashes around "announced without warning".)

### 9. Stacked qualifiers

Watch for: to be fair, it's also possible, could potentially, might arguably, in some cases it may.

Problem: repeated editing adds qualifiers until every claim sounds uncertain. Keep a qualifier only when the source supports it. Keep scope statements, safety notices, and real corrections. Ordinary hedges such as "perhaps" or "tends to" are human habits, not tells. *Weak alone.*

Before: It could potentially possibly be argued that the policy might have some effect on outcomes.
After: The policy may affect outcomes.

### 10. Hyphenated pairs everywhere

Problem: compound modifiers keep their hyphen after the noun. Keep it before a noun ("a high-quality report"), drop it after ("the report is high quality"). *Weak alone.*

### 11. Passive voice and missing subjects

Problem: the text hides who acts. Use active voice when it makes the actor clearer. *Weak alone* here, but a hard STE rule for instructions.

Before: No configuration file needed. The results are preserved automatically.
After: You do not need a configuration file. The system preserves the results automatically.

## C. Inflation and borrowed authority

### 12. Overused AI words

Watch for: actually, additionally, align with, bolstered, crucial, deep dive, delve, enduring, enhance, garner, gate (figurative), highlight (verb), interplay, intricate, key (adjective), landscape (abstract), leverage, meticulous, pivotal, quietly, robust (figurative), seamless, showcase, tapestry, testament, underscore (verb), valuable, vibrant.

Problem: models use these far more often than people do, especially in groups. A formal word outside this list is not a tell by itself.

Before: Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape.
After: Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common.

### 13. Inflated significance

Watch for: stands as a testament, a pivotal moment, plays a key role, marking the, reflects a broader, lasting legacy, setting the stage for, evolving landscape; "Despite these challenges... continues to thrive"; "the future looks bright".

Problem: an ordinary detail is said to mark a change or promise a future. Keep the fact, drop the significance. End on the last concrete fact.

Before: The institute was established in 1989, marking a pivotal moment in the evolution of regional statistics.
After: The institute was established in 1989, part of a wider decentralization of administrative functions.

### 14. Vague connection

Watch for: associated with, connected to, linked to, tied to.

Problem: the text says two things are connected without saying how. Name the relationship the source gives. If the source does not say, keep the vague wording rather than invent a role.

Before: He is associated with the Rajhans Orchestra, which he founded and conducts.
After: He founded and conducts the Rajhans Orchestra.

### 15. Shallow -ing riders

Watch for: highlighting, underscoring, emphasizing, ensuring, reflecting, symbolizing, contributing to, fostering, showcasing.

Problem: an -ing phrase is bolted onto a fact to make it sound deeper. Keep the fact. Keep the rider only when the source supports it.

Before: The temple's palette of blue, green, and gold resonates with the region's natural beauty, reflecting the community's deep connection to the land.
After: The temple is painted blue, green, and gold, colors meant to evoke Texas bluebonnets and the Gulf of Mexico.

### 16. Sales language

Watch for: rich (figurative), profound, exemplifies, commitment to, natural beauty, nestled, in the heart of, renowned, featuring, diverse array, breathtaking, must-visit, stunning.

Problem: the text reads like an advertisement. State what the thing is.

Before: Nestled within the breathtaking region of Gonder, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage.
After: Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

### 17. Borrowed authority

Watch for: experts argue, observers have cited, industry reports, some critics; cited in [a list of outlets]; over N followers.

Problem: an unnamed authority stands in for what was said. Use the real source and what it said, or cut.

Before: Experts believe the river plays a crucial role in the regional ecosystem.
After: Researchers and conservationists study the river for its unusual characteristics.

### 18. Avoiding is, are, and has

Watch for: serves as, stands as, functions as, operates as, marks, represents [a]; boasts, features, offers, maintains [a]; refers to.

Before: Gallery 825 serves as LAAA's exhibition space. The gallery features four spaces and boasts over 3,000 square feet.
After: Gallery 825 is LAAA's exhibition space. The gallery has four rooms totaling 3,000 square feet.

## D. Formatting by rule

### 19. Bold as decoration

Problem: words are bolded without reason, and every list item gets a bold label and a colon. Remove the bold. Turn a labeled list into prose when the labels carry no information.

Before:
- **User Experience:** The interface was improved.
- **Performance:** Algorithms were optimized.
- **Security:** End-to-end encryption was added.

After: The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

### 20. Decorative headings

Problem: Title Case on every heading, emojis or arrows as decoration, a horizontal rule between every section, a heading written for effect. Use sentence case. Let the heading name what the section holds.

### 21. Curly quotation marks

Problem: curly quotes where the target format uses straight quotes. Most editors auto-curl. *Weak alone.*

## E. Leftovers from the chat and the draft

### 22. Chatbot residue

Watch for: I hope this helps, Of course!, Certainly!, Great question!, You're absolutely right, Would you like..., Want me to...?, let me know.

Problem: a chatbot's greeting, praise, or offer remains in text that should stand on its own. Remove the wrapper. Keep the content.

### 23. Knowledge-limit disclaimers and guesses

Watch for: as of [date], up to my last training update, while specific details are limited, based on available information, likely [grew up, studied], it is believed that.

Problem: the text admits it found no source and fills the gap with a guess. State what the source does not show, or remove the sentence.

### 24. A heading repeated in the first sentence

Problem: a heading is followed by a one-line paragraph that restates it. Remove the repeated sentence.

### 25. Writing about the document instead of its subject

Watch for: "was added to replace", "generated from", "compiled from", "the table below compares", "this section is organized by".

Problem: the text describes itself instead of its subject. Keep a source credit the reader can follow. Cut the account of how you worked. *Weak alone.*

## F. Writing for the wrong reader

### 26. Re-explaining what the reader knows

Watch for: a reply that restates the problem, walks through the diagnosis, and lays out the evidence before it reaches the decision; the answer sitting in the last line.

Problem: in a reply the reader already has the context. Lead with the decision. Keep only the reasoning that would change whether the reader agrees.

## When not to act

Leave a watched phrase alone inside a quotation, a title, a proper name, or a passage that discusses the phrase rather than uses it. Salutations on a letter predate chatbots. Keep the details that carry the writer's voice: a specific unusual detail, mixed feelings stated plainly, a real aside, a first-person choice the writer can explain.
