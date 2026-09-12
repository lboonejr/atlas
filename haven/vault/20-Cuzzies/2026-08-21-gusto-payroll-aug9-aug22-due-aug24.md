---
created: 2026-08-21T08:17-04:00
updated: 2026-09-12T14:25:00-04:00
domain: cuzzies
type: task
status: awaiting-decision
tags: [gusto, payroll, funding, wind-down]
due: 2026-08-24T19:00-04:00
source: gmail
calendar_event_id: v5kjoasoqugfg34n10glv8834c
---

# Gusto payroll — Aug 9–22 period, due Monday 2026-08-24 7:00 PM ET

Gusto's 3-day heads-up notice: payroll for Cuzzie's Dispensary & Delivery LLC covering
**Aug 9, 2026 – Aug 22, 2026** must be run by **Monday, August 24, 2026, 7:00 PM EDT**.
Sent to admin@cuzziesnj.com, joshua@cuzziesnj.com, and lemar@cuzziesnj.com — an
action-required/critical notice, not a reply-worthy thread.

Every prior payroll cycle this vault has a record of hit a funding question before
running (see the string of `gusto-*-payroll-funding-shortfall` /
`*-payroll-shortfall-cancel` notes back through July). Flagging this cycle the same way
rather than assuming funding is in place — Samira has no visibility into account
balances to judge that herself (locked 2026-08-10: balances are reported, never
fetched).

Projected onto the **Cuzzie's (Owners)** calendar (business money — never the personal
reminder calendar, per the 2026-08-10 lock): event `s6fnevfjb1cilcak3cl4u5ke70`,
2026-08-24 7:00 PM ET, popups at 24h and day-of.

## Update 2026-08-21T10:15-04:00 — Lemar: the business has been closed since June 13, this shouldn't be running at all

Lemar replied in `#decisions`: "we've been closed since June 13th. I think we need to
figure out a way to stop this payroll from running every couple weeks since there is no
payroll to run."

This reframes every notice in this recurring string, not just this one. The vault
already has a record of a **"Gusto Final Payroll Deadline — Complete Employee Close-Out
(all 8 employees)"** run on 2026-07-31
([[2026-07-30-gusto-final-payroll-closeout]]) — but Gusto has kept firing a new
"time to run payroll" notice roughly every two weeks since (8/7, 8/11 late-notice, and
now this one), meaning that 7/31 event ran a final *off-cycle payroll*, not an actual
**termination of the Gusto company/account**. Those are different actions in Gusto —
running a last payroll leaves the account (and its recurring pay-schedule) active;
closing/terminating the company is a separate step.

**Samira has no Gusto login and cannot pause, cancel, or terminate the account or its
pay schedule herself** (no credential, and this is exactly the kind of account-state
change outside her authority even if she had one). The fix has to happen inside
app.gusto.com directly — likely under Settings → **company/account termination** (or
whatever Gusto calls ending the payroll subscription entirely, distinct from "run
payroll"), not another off-cycle run. Replied in-thread pointing this out rather than
either running/confirming this payroll (there's no payroll to run, per Lemar) or closing
this card outright — leaving it `awaiting-decision` until Lemar confirms the Gusto
account itself has been terminated, at which point this whole recurring note string can
close for good.

## Update 2026-08-21T12:04-04:00 (PART D) — Gusto: cash balance may not cover payroll 8/28

A second, separate Gusto task notice landed (`gustonoreply@gusto.com`, 2026-08-21
12:00 ET): "Review payroll funding — Based on known expenses, the current cash balance
from connected bank accounts may not fully cover payroll on Fri Aug 28," due Mon 8/24.
This is a distinct task from the "time to run payroll" notice already logged above, but
the same underlying pattern this note already flagged — a funding question surfacing
before a payroll run that, per Lemar's 10:15am reply, shouldn't be running at all since
the business closed 6/13. Not something Samira can review or fund (no Gusto login, no
bank visibility — balances are reported, never fetched, per the 2026-08-10 lock). Left
`awaiting-decision`, same as above; no new card opened, replied in-thread on the existing
one pointing to this as further evidence the Gusto account itself needs terminating, not
another off-cycle run. Gmail thread `1a0250d7b7efbc78` labeled seen.

## Update 2026-08-23T08:08-04:00 (calendar-sync) — deadline event was gone, recreated

This run found the Cuzzie's (Owners) calendar had no event with id
`s6fnevfjb1cilcak3cl4u5ke70` (deleted outside the vault — cause unknown). Recreated as
`v5kjoasoqugfg34n10glv8834c`, same 2026-08-24 7:00 PM ET slot, popups at 24h + day-of.
Still `awaiting-decision` — Lemar's 8/21 point that the Gusto account itself needs
terminating (not just another off-cycle run) stands.

## Update 2026-08-23T13:07-04:00 (calendar-sync) — the 08:08 "recreate" was a false positive; duplicate deleted

This run's calendar-sync found event `s6fnevfjb1cilcak3cl4u5ke70` — the one the
08:08 update above says was "deleted outside the vault" — still live on the Cuzzie's
(Owners) calendar, alongside the "recreated" `v5kjoasoqugfg34n10glv8834c`. It was never
actually deleted; the 08:08 pass's list query missed it and recreated a duplicate, so
Lemar has had two identical 8/24 7:00 PM ET reminders firing since this morning.

Cancelled the orphaned original (`s6fnevfjb1cilcak3cl4u5ke70`) — it was not referenced
by this note's `calendar_event_id` (which already pointed at the newer
`v5kjoasoqugfg34n10glv8834c`), so nothing this note tracks changed. One event remains:
`v5kjoasoqugfg34n10glv8834c`, 2026-08-24 7:00 PM ET, popups at 24h + day-of.

## Update 2026-09-12T14:25:00-04:00 — final-audit Chrome prompt, deletion moved to Thursday, restore question

Lemar asked (Convo 1 card ts `1789219701.620429`): for a Chrome prompt to do a final
audit of Gusto + double-check the 8/27 archive task, plus scour the rest of the account
for anything else worth saving, move the final deletion to Thursday, and whether a
deleted Gusto account can be restored.

**Archive check — done without Chrome, since Drive is a website these tools can
already read** (correcting an earlier answer in this thread that conflated "your
computer" with "the web," and that Chrome-in-your-browser reads live sites, not your
local machine, either): the "Cuzzie's Gusto Archive — 2026-09-06" Drive folder
(`1JC9VV9c3iVshwhpiaHpXMSk5ypjkK5Q6`) IS populated — W-2s/1099s (8 PDFs), Tax Filings
(9 federal/NJ PDFs + the NJ sales tax return added since), Payroll History (2 CSVs,
2025 + 2026 summaries). **Timesheets is empty** — consistent with no Gusto time
tracking having been used; worth a quick look in Gusto itself to confirm nothing's
missing there before archiving is called done.

Chrome-in-your-browser prompt for the final audit + wider scour (it can read
app.gusto.com's pages, not your local disk):

```
===CHROME RUN | task:gusto-final-audit | phase:pre-termination===
Site: app.gusto.com (Cuzzie's Dispensary & Delivery LLC)
Goal: final check before terminating the account.
Steps:
1. Taxes & compliance → Tax documents: confirm every W-2/1099 listed there is already
   in the "W-2s and 1099s" Drive folder (compare by employee name). Note anything not
   yet archived.
2. Taxes & compliance → Filings: same check against the "Tax Filings" Drive folder.
3. Reports → Payroll journal: confirm the exported CSVs cover the full active period.
4. Time tracking / Timesheets: check whether anything exists — the Drive archive's
   Timesheets folder is currently empty. If there's real data, export and note it here
   (don't upload it yourself — read only).
5. Scour company Documents / Files (if Gusto has a general document library beyond the
   four categories above) for anything else worth keeping — insurance certs, state
   registration numbers, benefits paperwork, anything not already covered.
6. Do NOT cancel, terminate, or change anything. Read-only.
Report: a plain list of what's confirmed archived, what's missing, and anything found
in step 5 that should be saved before termination.
===CHROME RUN END===
```

**Deletion moved to Thursday 9/17** — created a reminder on the Cuzzie's (Owners)
calendar for that morning to run the audit above, then terminate at Settings →
company/account termination.

**Restorability — genuinely don't know a specific number, so not asserting one.**
Gusto's own help content describes account cancellation as generally reversible for
some window after cancellation by contacting their support directly, but the exact
retention period isn't something this session has a reliable source for and it may
depend on your plan/contract. Recommend confirming directly with Gusto support (in-app
chat or their support line) before Thursday, so the decision to delete is made with the
real window in hand rather than an assumed one.

## Sources
- gmail: thread `1a024238c4662406` ("Time to run payroll for Cuzzie's Dispensary &
  Delivery LLC," automated@gusto.com, 2026-08-21 07:45 ET)
- gmail: thread `1a0250d7b7efbc78` ("Review payroll funding" task, gustonoreply@gusto.com,
  2026-08-21 12:00 ET — cash balance may not cover payroll 8/28)
- slack: #decisions ts `1787314219.825659` (card) / `1787315320.109899` (Lemar's reply)
  · Convo 1 card ts `1788718701.557769`, reply `1789219701.620429`
- haven: [[2026-07-30-gusto-final-payroll-closeout]] (the 7/31 "final payroll" run that
  did not stop these notices), [[2026-08-11-gusto-payroll-late]], the
  `gusto-*-payroll-funding-shortfall` string back through July
- drive: folder `1JC9VV9c3iVshwhpiaHpXMSk5ypjkK5Q6` ("Cuzzie's Gusto Archive —
  2026-09-06") — populated, Timesheets subfolder empty
- calendar: event `pe9u568iv0bv4uu0t5hivjc9bc`, "Terminate Gusto account (Cuzzie's) —
  after final audit", 2026-09-17 9:00-9:30am ET, Cuzzie's (Owners) calendar
