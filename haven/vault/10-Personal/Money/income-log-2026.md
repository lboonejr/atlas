---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-29T14:30:00-04:00
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
  - {date: 2026-08-28, source: doordash, amount: 51.39, note: "Lemar's DoorDash 'Dashes' breakdown, posted as a screenshot plus his own typed transcription in #personal-finance 2026-08-29 (ts 1788011757.485089, ~11:35 ET). Verified against the Slack message itself. Dash 1 of 4 on Fri 8/28. 8/28 had NO prior income entry, so all four are unambiguously new money — logged. NOT marked as funding any day: he reported EARNINGS, not that he set anything aside."}
  - {date: 2026-08-28, source: doordash, amount: 21.95, note: "Lemar's DoorDash 'Dashes' breakdown, posted as a screenshot plus his own typed transcription in #personal-finance 2026-08-29 (ts 1788011757.485089, ~11:35 ET). Verified against the Slack message itself. Dash 2 of 4 on Fri 8/28."}
  - {date: 2026-08-28, source: doordash, amount: 28.10, note: "Lemar's DoorDash 'Dashes' breakdown, posted as a screenshot plus his own typed transcription in #personal-finance 2026-08-29 (ts 1788011757.485089, ~11:35 ET). Verified against the Slack message itself. Dash 3 of 4 on Fri 8/28."}
  - {date: 2026-08-28, source: doordash, amount: 32.55, note: "Lemar's DoorDash 'Dashes' breakdown, posted as a screenshot plus his own typed transcription in #personal-finance 2026-08-29 (ts 1788011757.485089, ~11:35 ET). Verified against the Slack message itself. Dash 4 of 4 on Fri 8/28. Day total $133.99."}
  - {date: 2026-08-29, source: doordash, amount: 46.00, note: "Lemar's DoorDash 'Dashes' breakdown, posted as a screenshot plus his own typed transcription in #personal-finance 2026-08-29 (ts 1788011757.485089, ~11:35 ET). Verified against the Slack message itself. Sat 8/29. No prior entry for 8/29 — unambiguously new. NOT marked as funding."}
  - {date: 2026-08-29, source: doordash, amount: 0, note: "NO NEW MONEY — RECONCILIATION HELD OPEN. The same 8/29 breakdown ALSO lists Mon 8/24 $38.80, Wed 8/26 $53.25 + $50.60, and Thu 8/27 $57.25 + $57.80. Those three days already carry entries from his earlier verbal reports: 8/24 $30.00, 8/26 $70.78, 8/27 $50.60. The app figures and the verbal figures CONFLICT and were NOT both logged — logging both would double-count roughly $151 and inflate the trailing 4-week income average that OVERLOAD CHECK divides by, making the week look more affordable than it is. Most likely reading, NOT applied: the breakdown is the app's authoritative record and the three verbal lines are approximate recollections of dashes already inside it — note $50.60 appears in the breakdown on Wed 8/26 while he reported it 8/27 as 'just now', consistent with a dash that ran past midnight. Against that: the screenshot may be a scrolled/partial list, and $70.78 matches no breakdown row or pair. Needs Lemar: replace the three verbal entries with the app rows, or keep both as separate money. Until he answers, 8/24, 8/26 and 8/27 keep ONLY their original verbal entries."}
  - {date: 2026-08-26, source: doordash, amount: 53.25, note: "Lemar's DoorDash 'Dashes' breakdown (ts 1788011757.485089), unblocked by his two #decisions replies of 2026-08-29, both verified against the Slack thread itself (thread ts 1788011652.830719). Now loggable: the competing 8/26 entry ($70.78) is voided on his instruction, so nothing conflicts with this row."}
  - {date: 2026-08-27, source: doordash, amount: 57.25, note: "Lemar's DoorDash 'Dashes' breakdown (ts 1788011757.485089), unblocked by his two #decisions replies of 2026-08-29, both verified against the Slack thread itself (thread ts 1788011652.830719). Dash 1 of 2 on Thu 8/27. Now loggable: the competing 8/27 entry ($50.60) is the Wed 8/26 dash per his own confirmation, so 8/27 had no valid entry of its own."}
  - {date: 2026-08-27, source: doordash, amount: 57.80, note: "Lemar's DoorDash 'Dashes' breakdown (ts 1788011757.485089), unblocked by his two #decisions replies of 2026-08-29, both verified against the Slack thread itself (thread ts 1788011652.830719). Dash 2 of 2 on Thu 8/27. Day total $115.05."}
  - {date: 2026-08-29, source: doordash, amount: 0, note: "RECONCILIATION, no new money — VOID. Lemar 2026-08-29 (#decisions ts 1788017291.486109, verified at the source): 'You can remove the manual $70.78 entry.' The 2026-08-26 $70.78 'last DoorDash shift' line above is VOIDED — it corresponds to no dash in his itemized breakdown and he confirmed it should not count. History is not edited (append-only): the line stays, this note voids it. Do NOT sum $70.78 into any total."}
  - {date: 2026-08-29, source: doordash, amount: 0, note: "RECONCILIATION, no new money — DATE CLARIFIED, NOT a void. Lemar 2026-08-29 (#decisions ts 1788017130.025569, verified at the source): 'Same dash was accidentally logged under 2 dates.' The 2026-08-27 $50.60 line above and the Wed 8/26 $50.60 row in his app breakdown are ONE dash; the app dates it 8/26, which fits a dash running past midnight (he reported it 8/27 as 'just now'). This ledger only ever held ONE $50.60 entry, so unlike main there is no duplicate here to void — the existing 8/27 line IS that single dash and it stands as the record. Its calendar date is the only thing off. Counted exactly once."}
  - {date: 2026-08-29, source: doordash, amount: 0, note: "RECONCILIATION, no new money — ONE ROW STILL OPEN. His breakdown lists Mon 8/24 $38.80; the log holds $30.00 for 8/24 from his 8/25 verbal report. He did NOT address this pair in either reply, so it is NOT resolved by them and $38.80 is NOT logged — logging both would double-count ~$30 into the trailing 4-week average OVERLOAD CHECK divides by. Arithmetic check that isolates it: the valid entries now total $428.89 for 8/24-8/29, versus $437.69 for his breakdown — a difference of exactly $8.80, which is $38.80 - $30.00. So 8/24 is the ONLY remaining discrepancy, and the likely reading (same dash, $30 was his estimate, $38.80 is the app) would close the two records exactly. Still his call."}
# - {date: 2026-08-05, source: doordash, amount: 140, note: null}
```
