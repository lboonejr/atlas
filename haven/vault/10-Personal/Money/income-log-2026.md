---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-29T13:15:00-04:00
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
  - {date: 2026-08-24, source: doordash, amount: 38.80, note: "from a full 'Dashes' breakdown Lemar posted as text in #personal-finance 2026-08-29 ~11:35am ET (ts 1788011757), per-dash amounts with dates. One of 10 lines in that post; see the other 8 below plus the flagged possible-duplicate note on the 2026-08-26 $50.60 line."}
  - {date: 2026-08-26, source: doordash, amount: 53.25, note: "from the same 2026-08-29 Dashes breakdown."}
  - {date: 2026-08-26, source: doordash, amount: 50.60, note: "from the same 2026-08-29 Dashes breakdown. POSSIBLE DUPLICATE of the 2026-08-27 $50.60 line above (identical amount) — that line was logged with no date-range confirmation and may be this same dash misattributed to Aug 27 instead of Aug 26. Logged as its own line rather than silently merged or dropped; raised in #decisions rather than guessed. Do NOT sum both into weekly totals until resolved."}
  - {date: 2026-08-27, source: doordash, amount: 57.25, note: "from the same 2026-08-29 Dashes breakdown."}
  - {date: 2026-08-27, source: doordash, amount: 57.80, note: "from the same 2026-08-29 Dashes breakdown."}
  - {date: 2026-08-28, source: doordash, amount: 51.39, note: "from the same 2026-08-29 Dashes breakdown."}
  - {date: 2026-08-28, source: doordash, amount: 21.95, note: "from the same 2026-08-29 Dashes breakdown."}
  - {date: 2026-08-28, source: doordash, amount: 28.10, note: "from the same 2026-08-29 Dashes breakdown."}
  - {date: 2026-08-28, source: doordash, amount: 32.55, note: "from the same 2026-08-29 Dashes breakdown."}
  - {date: 2026-08-29, source: doordash, amount: 46.00, note: "from the same 2026-08-29 Dashes breakdown."}
  - {date: 2026-08-29, source: doordash, amount: 0, note: "OPEN QUESTION, no new money: does the 2026-08-26 $70.78 'last DoorDash shift' line above correspond to ANY dash in the 2026-08-29 breakdown, or is it a separate/estimated figure not reflected there? None of the 10 breakdown amounts match $70.78. Also unresolved: is the 2026-08-27 $50.60 line the same dash as the 2026-08-26 $50.60 line above (see that line's note)? Raised in #decisions 2026-08-29 rather than guessed — do not sum overlapping candidates into any weekly total until Lemar answers."}
  - {date: 2026-08-29, source: doordash, amount: 0, note: "RECONCILIATION, no new money: Lemar confirmed in #decisions (ts 1788011652, reply ts 1788017130) 'Same dash was accidentally logged under 2 dates.' The 2026-08-27 $50.60 line above (reported standalone, no date-range detail) and the 2026-08-26 $50.60 line above (from the itemized 2026-08-29 breakdown, full date+amount provenance) are the same dash. Voiding the less-detailed 2026-08-27 $50.60 line from weekly totals going forward — the 2026-08-26 breakdown line is kept as the record of record. History not edited per append-only doctrine; do not sum both into any weekly total."}
  - {date: 2026-08-29, source: doordash, amount: 0, note: "RECONCILIATION, no new money: Lemar confirmed in #decisions (ts 1788011652, reply ts 1788017291) 'You can remove the manual $70.78 entry.' VOIDING the 2026-08-26 $70.78 'last DoorDash shift' line above — it does not correspond to any dash in the 2026-08-29 itemized breakdown and Lemar confirmed it should not be counted. History not edited per append-only doctrine (a wrong entry is corrected by a note, never by deletion); do not sum the $70.78 line into any weekly total going forward."}
# - {date: 2026-08-05, source: doordash, amount: 140, note: null}
```
