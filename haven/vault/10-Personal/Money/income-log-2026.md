---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-05T07:47:00-04:00
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
entries: []
# - {date: 2026-08-05, source: doordash, amount: 140, note: null}
```
