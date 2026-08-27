---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-27T12:00:00-04:00
domain: personal
type: log
status: active
tags: [personal-finance, income, money-hub]
source: claude
area: money
---

# Income log — 2026

Every earning Lemar reports lands here as one line, appended by the **money-hub** skill
(never rewritten). Weeks run Monday–Sunday per [[money-hub-ledger]]. `source` is open:
`doordash` today; `station-shift`, `salary`, `business`, `trading-cards`, `other` as
they appear. One-off money that isn't work income (like the $1,000 received 2026-07-25)
still gets a line with `source: other` so weekly math sees everything.

Field rules: `date` ISO, `amount` plain number (USD), `note` free text or null.
Append-only; a wrong entry is corrected by a new line with a note, never by editing
history. New year → new file (`income-log-2027.md`).

```yaml
entries:
  - {date: 2026-07-20, source: doordash, amount: 153.94, note: "weekly total, week of Jul 20-26 — reported via #personal-finance screenshot (IMG_2079.png) + typed breakdown 2026-08-10"}
  - {date: 2026-07-27, source: doordash, amount: 327.70, note: "weekly total, week of Jul 27-Aug 2 — same #personal-finance drop, 2026-08-10"}
  - {date: 2026-08-03, source: doordash, amount: 457.40, note: "weekly total, week of Aug 3-9 — same #personal-finance drop, 2026-08-10"}
  - {date: 2026-08-10, source: doordash, amount: 61.43, note: "weekly total, week of Aug 10-16, PARTIAL/in-progress as of 2026-08-10 (will grow through the week) — same #personal-finance drop"}
  - {date: 2026-08-10, source: doordash, amount: 51.70, note: "reported #personal-finance 2026-08-10 ts 1786388799 as \"DoorDash Earnings : $51.70\", no date range given. Logged as its own line rather than merged into the $61.43 partial-week figure above — relationship between the two (additional earnings on top vs. a restated total) is unclear; raised as an open question, nothing merged/assumed."}
  - {date: 2026-08-10, source: doordash, amount: 0, note: "RECONCILIATION, no new money: Lemar's ✅ on Option 1 in #decisions (ts 1786393175, option ts 1786393179) confirmed the $51.70 line above is additional to the $61.43 partial-week line above it, not a restatement — running Aug 10-16 week-so-far total is $113.13 (61.43 + 51.70). Open question closed."}
  - {date: 2026-08-15, source: "the-station", amount: 144, note: "reported in #personal-finance"}
  - {date: 2026-08-23, source: "the-station", amount: 230, note: "Reported by Lemar 2026-08-25: 'I earned $230 from the station last weekend.' His Station shift is Sat+Sun, so this is the WEEKEND TOTAL (2026-08-22 + 2026-08-23); he gave no per-day split and none was invented. Dated to the Sunday, the day by which all of it had been earned, and logged as ONE line rather than split — same treatment as the 2026-08-15 $144 line above. NOT marked as funding any day: he reported spending most of it (see cash_on_hand $120 on 2026-08-25), never setting it aside."}
  - {date: 2026-08-24, source: doordash, amount: 30, note: "Reported by Lemar 2026-08-25: 'I made $30 doordashing yesterday.' Yesterday = 2026-08-24. Not marked as funding 2026-08-24 — nothing was reported as set aside."}
  - {date: 2026-08-26, source: doordash, amount: 70.78, note: "Reported by Lemar 2026-08-26 in #personal-finance (ts 1787751210.248719, ~9:33 ET): 'Got $70.78 from my last DoorDash shift.' Logged by Samira's PART M run on main; carried across in the 2026-08-26 merge. His words 'last shift' are noted but NOT interpreted as ending DoorDash work — no such conclusion was drawn."}
  - {date: 2026-08-27, source: doordash, amount: 50.60, note: "Reported by Lemar 2026-08-27 in #personal-finance (ts 1787786194.689369, ~08:36 ET): 'Made $50.60 just now on doordash.' Verified against the Slack message itself, not carried on trust from the main-branch run. Logged first by Samira's PART M run on main; her ALLOCATION of it was recomputed here against this branch's ledger (hers ran on a stale and truncated base)."}
# - {date: 2026-08-05, source: doordash, amount: 140, note: null}
```
