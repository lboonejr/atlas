---
created: 2026-08-15T18:45-04:00
updated: 2026-08-15T19:10-04:00
domain: project
type: brief
status: active
tags: [stormy, money-hub]
source: claude
---

# Money Hub rebalance steward

## The idea

A "budget rebalance steward" capability for Money Hub. Instead of building a wholly
separate steward agent, extend the `money-hub` skill itself with a **rebalance step**
that fires alongside the OVERLOAD CHECK. When accrual overload is detected, it should
reason about the current money situation and propose concrete rework options — e.g.
delay/stretch a goal's drip rate, re-tier a payment plan, flag business-origin-but-
personally-carried bills for business reimbursement instead of personal accrual — and
surface those as a decision in #decisions for Lemar to approve, mirroring how Chase and
the email loop already stage decisions rather than act unilaterally.

## The trigger

Money Hub's OVERLOAD CHECK fired on 2026-08-15 (first time it has fired) —
[[2026-08-15-money-hub-overload-check|Slack: #decisions, 6:14pm ET]]:

- 7-day need (8/15–8/21): **$2,193.73**
- Trailing 4-week logged-income average: **$299.04/week** — the need is ~7.3x normal.
- Genuinely due-dated bills in that window — **$478.00 total**:
  - `station-travel` — $80.00, due 8/15
  - `liquidibee-1` (Nomas plan) — $125.00, due 8/16
  - `cuzzies-google-voice` — $38.00, due 8/18 *(business-origin, carried personally)*
  - `cuzzies-google-workspace` — $85.00, due 8/19 *(business-origin, carried personally)*
  - `metrc-fee` — $40.00, due 8/21
  - `moms-lump-0821` — $110.00, due 8/21
- The remaining **~$1,715.73** is simultaneous catch-up drip from longer-horizon goals
  all accruing from today at once: the $2,800 car-running goal, $500 tow-truck-repay,
  $500 mechanic-repair-repay, $242 self-account-balance-repay, and others.

Money Hub's current behavior: report the number and stop — *"Nothing shrunk or delayed
— the accrual is written exactly as computed. This is your call on what moves, not
mine."* No rework is proposed.

## What Stormy is baking

What rework moves the steward is allowed to propose, how aggressive/conservative it
defaults to, what data it needs beyond what Money Hub already tracks, where the hard
line is before it must stop and ask instead of just proposing, and whether this lives
as a new step inside `money-hub` or something adjacent to it.

## Update 2026-08-15: pressure test — Q1-Q3

- **Q1 (core problem):** Operational efficiency — save Lemar from manually untangling
  an overload every time it fires.
- **Q2 (primary beneficiary):** Lemar, personal finances.
- **Q3 (scope & hardest constraint):** In scope — personal-side moves (goal drip rates,
  payment-plan re-tiering, timing shuffles within the personal ledger) **plus** flagging
  business-origin-but-personally-carried bills for business reimbursement. Hardest
  constraint: flagging is advisory only — the steward never touches a business ledger
  or accounting entry automatically; it surfaces the flag and stops.

## Update 2026-08-15: pressure test — Q4-Q6

- **Q4 (success metric):** Operational metric — a clean, accurate proposal every time
  overload fires.
- **Q5 (minimum viable success):** It proposes at least one real move Lemar would
  actually take, instead of just re-reporting the number with no rework attached.
- **Q6 (early warning sign):** It proposes a move Lemar wouldn't actually take (e.g.
  stretching a goal he considers non-negotiable) — a sign its judgment is off and needs
  retuning or killing.

## Update 2026-08-15: pressure test — Q7-Q10

- **Q7 (most likely blocker):** Tech/tools — getting the rework-reasoning logic right
  inside `money-hub`.
- **Q8 (sign-off / involvement):** Lemar only. No other role needed — everything in
  scope is personal-ledger; business-origin bills are only *flagged*, never touched.
- **Q9 (activation timing):** ASAP — within 1 week.
- **Q10 (preconditions):** None. Ship it for the next overload event.

## Update 2026-08-15: pressure test — Q11-Q15

- **Q11 (compliance):** None — no regulated area, no external party needs to approve
  anything. Reggie stays uninvolved.
- **Q12 (automated workflows):** Overload detection (already exists in `money-hub`) plus
  drafting the rework proposals both run automatically, triggered off the same overload
  event.
- **Q13 (data/status flow):** No new source of truth. The `money-hub-ledger.md` stays
  the one ledger; proposals surface as a #decisions card, same pattern as today's
  overload report and the same surface Chase/email-loop already use.
- **Q14 (delegation):** No — Lemar leads. Nobody else owns any part of this.
- **Q15 (what comes back / cadence):** N/A — nothing delegated. Every proposal is a
  decision that comes back to Lemar directly, every time it fires (not batched).

## Pressure test complete — all 15 answered.

## Locked plan

### Mission
Give `money-hub` a rebalance step: the moment its overload check fires, it doesn't just
report the gap — it drafts real rework moves within Lemar's own personal ledger and
puts them in front of him as a single #decisions card, so he approves or edits instead
of doing the untangling math himself.

### Success criteria
Every overload event produces at least one proposal Lemar would actually act on (MVP:
one real move, not just the number restated). Fails if it ever proposes moving a goal
Lemar considers non-negotiable — that is the signal to retune or kill it, not iterate
past it.

### Timing & preconditions
Activate ASAP, within the week. No preconditions — ships ahead of the next overload
event, whenever that fires next.

### Phases

1. **Define the move types** — goal: lock the exact set of rework moves the steward is
   allowed to draft (stretch/delay a goal's drip rate, re-tier a payment plan's
   installment size or start date, flag a business-origin-but-personally-carried bill
   for business reimbursement). Owner: Lemar + this session. Duration: same session.
   Output: a short "allowed moves" list written into the `money-hub` skill file.
   Dependency: none.
2. **Add the non-negotiable guard** — goal: give goals in `money-hub-ledger.md` an
   optional flag (e.g. `non-negotiable: true`) so the steward knows what it must never
   propose stretching. Owner: this session. Duration: same session. Output: ledger
   schema note + one field added to existing goal entries Lemar marks. Dependency:
   phase 1 (need the move types defined to know what the guard blocks).
3. **Wire the rebalance step into `money-hub`** — goal: the skill drafts proposals
   immediately after an overload fires, using only ledger data + the move types +
   the guard, and posts ONE #decisions card (proposal, not the plain report) instead of
   today's report-only message. Owner: this session (implementation). Duration: same
   session. Output: updated `money-hub` skill instructions. Dependency: phases 1-2.
4. **Dry-run against today's real overload** — goal: before shipping, run the new logic
   against the actual 2026-08-15 numbers ($2,193.73 need, $478 genuinely due, the goal
   catch-up drip) and show Lemar what it would have proposed, as a sanity check with no
   live posting. Owner: Lemar review. Duration: same session. Output: a sample proposal
   Lemar confirms looks right (or doesn't). Dependency: phase 3.
5. **Ship** — goal: live for the next real overload event. Owner: `money-hub` /
   Samira's PART M. Duration: ongoing. Output: every future overload event posts a
   rebalance proposal instead of a bare report. Dependency: phase 4 sign-off.

### Risks & sign-offs
Biggest risk is getting the reasoning logic wrong (Q7) — mitigated by phase 4's dry run
against real numbers before it ever posts live. Sign-off is Lemar only (Q8); no other
role is involved since everything in scope stays inside the personal ledger.

### Compliance flags
None. No regulated area, no external approval needed (Q11). Reggie stays uninvolved.

### Automation map
Runs autonomously: overload detection (already exists) + drafting the proposal (Q12).
Needs a human gate: every proposal is a #decisions card Lemar must approve before
anything is considered decided — the steward never edits the ledger itself (Q13, Q15).
No new source of truth: `money-hub-ledger.md` stays the one ledger, #decisions stays
the one surface (Q13).

### Delegation brief
No delegation — Lemar leads end-to-end, nobody else owns any part of this (Q14). Every
proposal comes back to Lemar directly and individually, not batched (Q15).

## Skill specs

No new skill needed. `money-hub` already exists on the roster — this project is a
modification to it (phases 1-3 above), not a new build. Nothing routes to
`skill-creator`.

## Sources
- slack: https://newworkspace-zlb6313.slack.com/archives/C0BBXA96FFV/p1786832078131649 (OVERLOAD CHECK message, Samira/Money Hub, 2026-08-15 6:14pm ET)
