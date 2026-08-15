---
created: 2026-08-15T18:45-04:00
updated: 2026-08-15T18:45-04:00
domain: project
type: brief
status: awaiting-decision
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

## Sources
- slack: https://newworkspace-zlb6313.slack.com/archives/C0BBXA96FFV/p1786832078131649 (OVERLOAD CHECK message, Samira/Money Hub, 2026-08-15 6:14pm ET)
