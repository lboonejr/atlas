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
  - {date: 2026-08-26, source: doordash, amount: 70.78, note: "last DoorDash shift"}
  - {date: 2026-08-27, source: doordash, amount: 50.60, note: "reported via #personal-finance"}
# - {date: 2026-08-05, source: doordash, amount: 140, note: null}
```
