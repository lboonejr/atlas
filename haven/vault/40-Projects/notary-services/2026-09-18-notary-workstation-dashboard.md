---
created: 2026-09-18T09:40:00-04:00
updated: 2026-09-18T09:40:00-04:00
domain: project
type: decision
status: active
tags: [notary, dashboard, workstation, surfaces]
source: claude
---

# The notary workstation — what it is, and the rules it runs under

The notary business now has one place to be run from: a dashboard called **The Workstation**,
published at https://claude.ai/artifact/5q3G772uieaQFrubGhfqek. The page source lives in this
repo at `apps/notary-workstation/index.html`.

Related: [[2026-09-15-notary-business-backend-systems]] (the locked plan),
[[2026-09-20-notary-exam-day-checkpoint]] (the open items it loaded from),
[[2026-09-16-notary-b2b-acquisition-tracks]].

## What it is

One surface that changes shape as the business changes phase, not two dashboards.

Right now it is in **pre-commission** mode: nothing operational exists, so the top of the page
leads with the next deadline, how many launch steps are done, how many items are open, and an
honest `$0` for money. The moment the first job is entered it flips to **operating** mode, and
the same four tiles become jobs on the book, alarms, money owed to Lemar, and what he keeps.
Nothing is faked to fill space in the meantime.

Six tabs: **Today** (what's going on, the next seven days, and a running log of what got done)
· **Jobs** · **Money** · **Marketing** · **Launch** · **Open items**.

## Three decisions, recorded

**1. It is its own surface, not a panel inside Pulse.** Pulse is Lemar's personal command
center across everything. This is one business, run end to end, with its own money and its own
alarms. Putting it inside Pulse would bury it.

**2. It absorbed the Given Word Runway tracker.** All 43 steps from the five-phase runway
(https://claude.ai/artifact/YFaq1Kcgh9xUzk2EZvDC4e) are now the Launch tab, with their costs,
their deadline and queue and gate markers, and their tick state. The old tracker still opens,
but it is no longer the place to work from. Two trackers competing over the same checklist is
exactly the failure this avoids.

**3. It is writable, and the vault is still the record.** The page carries a small shared
database so Lemar — and Samira, and any automation — can add a job, close an item, tick a
launch step, or drop a line in the log without opening a repo. That makes it usable on a phone,
which is the whole point.

The rule that keeps this honest: **anything typed into the page is a capture, not the record.**
Haven stays the source of truth, and what lands in the page gets swept back into the vault the
same way a Convo 2 drop does. If the two ever disagree, the vault wins.

## What it computes, rather than asks for

- **The four alarms** from `notary-journal-mirror` — no journal entry, invoice unpaid on its own
  terms, act logged with no fee, scan-back overdue — are derived from the job board and shown in
  a red band at the top of every tab. An appointment that has passed with the job still open is
  flagged too.
- **The money picture** is computed from completed jobs only: billed, minus what the printing
  actually cost (`pages × 2 × $0.055` when no receipt exists), minus the set-aside at 20% on
  the statutory line and 35% on everything else, leaving what Lemar keeps. The exempt-versus-
  taxable split for Schedule SE is a row, not a reconstruction job in April.
- **Payment chasing** runs on each channel's own terms — 7 days for consumer and agent-referral
  work, day 16 for a brokerage, day 31 or 46 for a signing service. A loan signing is not late
  at one week.
- **Marketing** scores each channel on jobs and billed revenue from the job board itself, beside
  its current state and what is blocking it. No second place to key an attribution.

## What it deliberately does not hold

No signer full names, addresses, dates of birth, or credential details — same PII-poor rule as
the job record. The journal of record holds that, under its own access controls and a ten-year
duty, and a copy in a shared page could never be fully deleted. First name and a town is all
the board needs.

It also does not decide anything legal. It never says whether an act may be performed, never
prices outside the published card, and the RESPA line — never pay an agent for a referral — is
printed on the Marketing tab where the temptation actually lives.

## What it was loaded with, on 2026-09-18

43 launch steps across the five phases · 15 open items (the four DORES questions, the three
BlueNotary questions, the three county-counter questions, the Monday exam, the county clerk
call, the platform research, and the CPA and RESPA-attorney calls) · 5 marketing channels,
each with what is blocking it · 0 jobs, which is correct until the commission exists.

## Sources
- claude: Claude Code session, 2026-09-18
