Subject: Your export problem (case CS-881)

Hi Maria,

The export fails for Acme because your account has too much data for it. The export stops before it finishes when an account has more than 50,000 rows. Acme has 72,000.

You can export one month at a time instead. Each month is under 50,000 rows, so it works.

1. Open the Export page.
2. Set the date filter to one month.
3. Export. Repeat for each month you need.

We built a fix, and it is in review now. If it passes testing, it should ship in the release on Friday, 21 November. Testing has a backlog, so it may ship the week after. I cannot promise Friday.

Missing: the name of the sender, and a date when the sender will write again.
