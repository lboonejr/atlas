---
created: 2026-07-24T12:20-04:00
updated: 2026-08-14T15:15:00-04:00
domain: cuzzies
type: task
status: active
tags: [gusto, payroll, pay-period]
source: gmail
due: 2026-07-29T19:00:00-04:00
calendar_event_id: r99cafdgphtqf15l6g54bq03s0
---

# Gusto — payroll due Mon Jul 27, pay period Jul 12–25

Automated Gusto email (2026-07-24 ~11:49am ET, thread `19f93f5e82ea20d4`, to
admin@cuzziesnj.com/joshua@cuzziesnj.com/lemar@cuzziesnj.com): payroll for Cuzzie's
Dispensary & Delivery LLC covering **Jul 12 – Jul 25, 2026** is due, deadline
**7:00 PM EDT Monday July 27**.

Same recurring question as the last several pay periods: run it (period was worked) or
skip it — Samira has no Gusto login/credential to act either way, this needs Lemar's
call in app.gusto.com. This is the sixth consecutive pay-period alert in this folder
(see the 2026-07-03, 2026-07-07, 2026-07-08 ×2, 2026-07-09, and 2026-07-10 sibling
notes) — several of the earlier ones were tied to a funding-shortfall warning. Worth
Lemar checking whether that underlying cause has actually been resolved, or whether
this is about to repeat the same late/skip pattern as the Jun 28–Jul 11 period.

## Update 2026-07-24T09:05-04:00
Lemar closed the #decisions card via 🫡 (saluting_face reaction, no thread reply). This
records that Lemar acknowledged/closed the alert — it does NOT record which way the
run/skip payroll call went; neither the card nor its thread stated that explicitly, and
Samira has no Gusto login to have run it herself. If a run/skip decision needs a
durable record, it should come from Lemar directly (in app.gusto.com or back on this
thread). Card closed, dropped from the #decisions queue.

## Update 2026-07-26 (~10:08 ET) — calendar reminder created
Gusto's reminder email repeated again this morning ("due tomorrow by 7pm EDT") with no
new information. No `calendar_event_id` had been written for this `due` yet, so
haven-calendar-sync created one — a popup reminder 10 minutes before the 7:00 PM EDT
Monday deadline — since whether payroll was actually run is still unconfirmed per the
update above.

## Update 2026-07-26 (~12:09 ET) — calendar-sync retired the reminder
Status is `done`; the 7/27 7:00 PM ET reminder event (`ka01o5f5f58iudnokou1s84810`) has
been cancelled and the id cleared per the calendar-sync RETIRE rule.

## Sources
- gmail: thread `19f93f5e82ea20d4`, automated@gusto.com, 2026-07-24 11:49 UTC; repeat
  reminder 2026-07-26 ~11:56am ET (thread `19f9e485e27aaac7`)
- slack: #decisions parent ts 1784895631.960559, 🫡 close reaction from U0BC5UTHYG4
- calendar: event `ka01o5f5f58iudnokou1s84810` cancelled 2026-07-26 (was 2026-07-27 7:00 PM ET)

## Update 2026-07-28T12:20:00-04:00 — Gusto confirms this payroll is now 1 day late; reopening

New Gusto email (thread `19fa88edcb8d38a0`, 2026-07-28 ~11:49am ET, "Action required:
Payroll is late for Cuzzie's Dispensary & Delivery LLC"): same pay period (Jul 12-25)
is now flagged **1 day late**, original payday Fri Jul 31. This resolves the
uncertainty flagged in the 2026-07-24 09:05 ET update — payroll for this period was
NOT run by the prior deadline, despite Lemar closing the #decisions card. Reopening
this note (`status: active`) since the underlying task is not actually done.

Gusto's email notes same-day/instant pay options may still be available to hit the
Jul 31 payday despite the late start. This is a payment action only Lemar can take
(no Gusto login available to Samira) — raised fresh in #decisions rather than
re-using the closed card, since the prior close didn't carry a run/skip signal.

## Sources (continued)
- gmail: thread `19fa88edcb8d38a0` (2026-07-28, "Action required: Payroll is late," 1
  day late, original payday Fri Jul 31)

## Update 2026-07-29T15:39:00-04:00 — off-cycle payroll confirmed, resolved

Gusto emailed a confirmation (gmail thread/message `19faf635faa00932`, "Off-cycle
payroll confirmed," 2026-07-29 ~3:39pm ET): the Jul 12–25 pay period was run as an
Off-Cycle payroll — Gusto will debit **$1,570.65** from Cuzzie's Dispensary & Delivery
LLC's bank account on **Wed Jul 29** ($1,209.36 employee net pay/donations + $361.29
taxes), employees paid **Tue Aug 4**. This was a Gusto-login action only Lemar could
take; Samira did not run it. Marking this note `done` — the run/skip question from the
2026-07-24 and 2026-07-28 updates is now settled (it was run, late but before the Aug 4
payday). No further action needed from Samira on this pay period.

## Sources (continued)
- gmail: message `19faf635faa00932` (gustonoreply@gusto.com, 2026-07-29 19:39 UTC,
  "Off-cycle payroll confirmed," $1,570.65 debit Jul 29, payday Aug 4)

## Update 2026-07-29T17:11:00-04:00 — CANCELED 38 minutes later; reopening, urgent

New Gusto email (thread `19faf86047552535`, "Payroll canceled," 2026-07-29 20:17 UTC =
4:17pm ET): "You canceled Cuzzie's Dispensary & Delivery LLC's payroll for $1,570.65 at
4:17pm EDT on Wed Jul 29." Gusto's own text attributes the cancel action to the account
holder (Lemar), not Samira — Samira has no Gusto login and did not touch this. Gusto:
"To pay your team on time, run payroll again by **7pm EDT on Wed Jul 29**" — same day,
same deadline.

This reverses the 15:39 ET "resolved" update above — the off-cycle run was confirmed,
then canceled 38 minutes later, before this note's calendar event could even retire
cleanly (it had just been cancelled by this run's calendar-sync pass moments before this
thread was found; a fresh reminder was created for the new 7pm deadline instead).
Reopening `status: active`, `due` moved to **2026-07-29T19:00:00-04:00** (today, 7pm ET).

Separately, an unrelated Gusto notice arrived 9 minutes later (thread `19faf8e474cf86f8`,
20:26 UTC, "You've added a past year non-Gusto payroll") about corrected W-2s (W-2Cs)
for a prior-year payroll entry — this is a distinct Gusto action from the same session,
not part of this Jul 12–25 pay-period thread; not chased further here, flagged for
Lemar to review directly in Gusto (legal responsibility to distribute W-2Cs sits with
him, not something Samira can act on).

Given the tight same-day window, posted a 🔴 urgent card to #decisions (not re-using the
already-closed prior card) and sent a direct phone notification — Samira has no Gusto
credential and cannot run or skip payroll herself; this needs Lemar in app.gusto.com
before 7pm ET.

## Sources (continued)
- gmail: message `19faf86047552535` (gustonoreply@gusto.com, 2026-07-29 20:17 UTC,
  "Payroll canceled," $1,570.65, re-run-by-7pm-ET-today deadline)
- gmail: thread `19faf8e474cf86f8` (2026-07-29 20:26 UTC, "past year non-Gusto payroll"
  — separate W-2C matter, unresolved, flagged for Lemar)
- calendar: event `7jjg70sv94gt6rk92r9glqrv2o` cancelled (stale, from the 15:39 ET
  "resolved" pass) → new event `474nemh5ki2hj3k81211pfouvo` created for the 7pm ET
  Jul 29 re-run deadline
