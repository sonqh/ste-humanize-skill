Subject: Your export problem (case CS-881)

Hi Maria,

You can export your data now if you do one month at a time. On the Export page, use the date filter to pick one month, then export. Repeat for each month.

The export fails because your account has 72,000 rows, and an export times out above 50,000 rows. Each single month is under 50,000 rows, so it works.

We have written a fix, and our team is checking it now. We hope it ships in the Friday release on 21 November, but our checks are running behind, so it may ship the week after. I cannot promise Friday.

Missing: the sender's name and sign-off. A date when the sender writes to Maria again.
