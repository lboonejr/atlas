---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-11T17:19:00-04:00
domain: personal
type: reference
status: active
tags: [personal-finance, budget, money-hub]
source: claude
area: money
---

# Money Hub — ledger (source of truth)

This note is the ONE structured source of truth for Lemar's personal budget: bills,
account pockets, payment plans, goals, allocation config, the daily set-aside ramp, and
reported cash. The **money-hub** skill (`.claude/skills/money-hub/SKILL.md`) reads and
writes the single fenced `yaml` block below; the Money Hub dashboard artifact and all
calendar reminder events (both per-bill due-date events and the daily "set aside today"
aggregate) are regenerated FROM it, never hand-edited (same doctrine as
[[on-button-reopen]]'s index).

Field rules (on-button-plan pattern):
- Amounts are plain numbers (USD). `null` = unknown/TBD — never invent a figure.
- Dedupe by `id` (kebab-case, stable). Never delete a line: a settled bill goes
  `status: paid`; a dropped one `status: parked`.
- `day` = day-of-month for monthly bills; `due` = ISO date for one-time items and
  installments. A `calendar_event_id` marks the reminder event that projects the line
  onto the reminder calendar (calendar is a one-way rendering; this note wins).
- `daily_targets` = the even daily set-aside ramp (added 2026-08-09, see the
  money-hub skill's RAMP/DAILY CALENDAR/ROLLOVER sections). ISO date key →
  `{total, calendar_event_id, contributions: [{bill_id, amount, status}]}`, `status`
  one of `pending` | `rolled` | `paid`. One aggregate calendar event per day; never a
  duplicate for the same date.
- The allocation SHAPE is a locked decision (Option 3 hybrid floor + waterfall,
  2026-07-24) — do not redesign it here. The floor DOLLAR figure is computed, not
  stored: sum active monthly bills with priority p1/p2/p4, ÷ 4.33.
- `reported_balances` = manually-reported account balances (added 2026-08-10, per
  Lemar's #decisions call to use manual entry for SoFi checking instead of Era Context
  until it reconnects). ISO date key per report; latest entry per `pocket` is current.
  Never a substitute for `cash_on_hand` (physical cash only).
- Weekly allocation runs append `## Update` sections below; the yaml holds state, the
  Updates hold history.

```yaml
config:
  week: mon-sun
  income_target_weekly: 500          # a target, never a confirmed average (2026-07-22)
  allocation: option-3-hybrid        # LOCKED 2026-07-24 — floor off the top, then waterfall
  floor_priorities: [p1, p2, p4]     # floor = sum of their active monthly bills / 4.33
                                     # ~ $463/wk as of 2026-08-05 (the 7/24 worked example
                                     # said ~$454, before Tidal + Patreon were folded in)
  waterfall_order: [p5, p6, p7]      # p3 (ex-employee back pay $11,579) removed from the
                                     # personal waterfall 2026-07-24 — moving to a
                                     # Cuzzie's-side deal, not structured yet
cash_on_hand:
  amount: 20                           # reported #personal-finance 2026-08-11 ("Cash on hand today - $20")
  as_of: 2026-08-11
reported_balances:                   # manually-reported account balances (2026-08-10, see field rules above)
  - {pocket: sofi-checking, amount: 2.54, as_of: 2026-08-10,
     note: "Lemar #decisions 2026-08-10: 'SoFi checking and we will use manual entry instead of Era.' Manual tracking starts here — update this entry whenever a new SoFi checking balance is reported in #personal-finance."}
pockets:                             # where delegated money goes (draft mapping 2026-07-24,
                                     # confirmed names 2026-07-25; no transfers made by anyone
                                     # but Lemar)
  - {id: sofi-checking,    role: operating — income lands here, floor pays from here, era_account: "Checking - 4102"}
  - {id: sofi-savings,     role: p7 savings,        era_account: "Savings - 6970"}
  - {id: cashapp-checking, role: p5 own car,        era_account: null}
  - {id: cashapp-savings,  role: p6 side projects,  era_account: null}
  - {id: doordash-crimson, role: p1 Cuzzie's buffer (checking + savings), era_account: null}
bills:
  # -- monthly --
  - {id: cuzzies-phone-workspace, name: "Cuzzie's phone + Google Workspace", amount: 550,
     cadence: monthly, day: null, priority: p1, status: active,
     note: "Lemar's own estimate 2026-07-22; actual recurring phone total unconfirmed"}
  - {id: student-loans, name: Student loans, amount: 500, cadence: monthly, day: null,
     priority: p2, status: active, note: "~$8,000 remaining; billing day unknown"}
  - {id: claude, name: Claude subscription, amount: 100, cadence: monthly, day: 4,
     priority: p2, status: active, calendar_event_id: 7djf895pc8is0illrr8bcrra20,
     note: "card declined on the 4th May/Jun/Jul — Lemar to update payment method"}
  - {id: wispr-flow, name: Wispr Flow, amount: 15, cadence: monthly, day: 10,
     priority: p2, status: active, calendar_event_id: e7d9muku31setk1b10le3bf3ak}
  - {id: moms-expenses, name: "Mom's expenses", amount: 200, cadence: monthly, day: null,
     priority: p2, status: active, note: "billing day unknown"}
  - {id: tidal, name: Tidal, amount: 14.92, cadence: monthly, day: null,
     priority: p2, status: active, note: "billing day unknown"}
  - {id: patreon, name: Patreon, amount: 25, cadence: monthly, day: 27,
     priority: p2, status: active, calendar_event_id: lf7pne54rrtcnrvekhq0fecec4,
     note: "27th confirmed 2026-07-28 after a 10th-vs-27th conflict"}
  - {id: food, name: Food, amount: 600, cadence: monthly, day: null,
     priority: p4, status: active, note: "~$20/day, spread across the month, no due day"}
  - {id: transportation, name: "Transportation (Rahway → Newark)", amount: null,
     cadence: variable, day: null, priority: p4, status: active,
     note: "$4.95/one-way NJ Transit (needs app spot-check); monthly total depends on Newark days/week"}
  # -- one-time --
  - {id: cashapp-payback, name: "Cash App payback", amount: 187.22, cadence: once,
     due: null, priority: p2, status: active, note: "own pace, no fixed date"}
  - {id: tmobile-split-1, name: "T-Mobile split payment 1 of 2", amount: 265, cadence: once,
     due: 2026-08-03, priority: p2, status: active,
     calendar_event_id: pg0a92rgg01l09mg3tatcfb3mk,
     note: "due date has passed — confirm paid, then flip to paid and retire the event. No ramp: due date already passed when the ramp feature was added 2026-08-09."}
  - {id: tmobile-split-2, name: "T-Mobile split payment 2 of 2", amount: null, cadence: once,
     due: null, priority: p2, status: active, note: "amount and date not given yet"}
  - {id: gym-debt, name: "Personal gym debt", amount: 75, cadence: once, due: null,
     priority: null, status: active, note: "priority unassigned — Lemar to slot it"}
  - {id: water-pump, name: "New water pump", amount: 184.79, cadence: once, due: null,
     priority: p5, status: active,
     note: "unclear if inside or on top of the $2,000 repairs lump — unreconciled"}
  - {id: metrc-fee, name: METRC, amount: 40, cadence: once, due: 2026-08-14,
     priority: null, status: active, calendar_event_id: q36k3ogoblpe3i5amktigav8ig,
     note: "reported in #personal-finance 2026-08-09; priority unassigned — flagged in #decisions 2026-08-09 (Lemar said 'high priority' 8/9, exact p1-vs-p2 bucket still unconfirmed). Ramped 2026-08-09: due date under 8 days out when logged, so full $40 lands on 2026-08-10; ROLLED to 2026-08-11 by end-of-day ROLLOVER, then ROLLED again to 2026-08-12 by end-of-day ROLLOVER (still pending/unpaid, see daily_targets)."}
  - {id: cleaning-supplies, name: "Cleaning supplies (house)", amount: 30, cadence: once,
     due: 2026-08-11, priority: null, status: paid,
     note: "PAID 2026-08-10 at $29.95 — confirmed by Lemar in #decisions (ts 1786395169, 'Yes the 29.95 is for the tract[ked] cleaning supplies. I paid it early'), picking Option 3 (the $29.95 purchase IS this bill). $0.05 under the tracked $30, not reconciled further. Due-date calendar event (ue8jtslgpl89qlhdra710h13k) retired; its $30 daily-set-aside contribution on 2026-08-10 flipped to paid and removed from that day's aggregate total (now $140.28). Prior note: reported in #personal-finance 2026-08-09, ramped 2026-08-09 (due date under 8 days out when logged)."}
  - {id: comedy-show-tickets, name: "Comedy show tickets", amount: 50.28, cadence: once,
     due: 2026-08-12, priority: null, status: active,
     calendar_event_id: jfh8548cet84pcqo3o697fkbq8,
     note: "reported in #personal-finance 2026-08-09; priority unassigned — flagged in #decisions 2026-08-09 (Lemar said 'low priority' 8/9; p5/p6/p7 are each tied to a specific pocket (own-car/side-projects/savings) so the bucket still needs confirming). Ramped 2026-08-09: due date under 8 days out when logged, so full $50.28 lands on 2026-08-10; ROLLED to 2026-08-11 by end-of-day ROLLOVER, then ROLLED again to 2026-08-12 by end-of-day ROLLOVER — note the due date is also 2026-08-12, so this is the last day it can roll (still pending/unpaid, see daily_targets)."}
  - {id: station-travel, name: "Travel to The Station", amount: 50, cadence: once,
     due: 2026-08-15, priority: p4, status: active,
     calendar_event_id: ptacguksk2rsf3md3403gljtes,
     note: "reported in #personal-finance 2026-08-09; priority p4 matches the existing Rahway→Newark commute pattern, confirmed by Lemar 8/9 ('median priority'). Ramped 2026-08-09: due date under 8 days out when logged, so full $50 lands on 2026-08-10; ROLLED to 2026-08-11 by end-of-day ROLLOVER, then ROLLED again to 2026-08-12 by end-of-day ROLLOVER (still pending/unpaid, see daily_targets). Lemar 8/9: likely becoming a recurring weekly expense (new weekend job at The Station) — rate TBD, he'll post it in #personal-finance."}
  - {id: moms-car-oil-change, name: "Mom's car oil change", amount: null, cadence: once,
     due: null, priority: null, status: active,
     note: "reported in #personal-finance 2026-08-11: 'It'll be about $100' due 'by the end of next week' — both amount and due date are hedged/unconfirmed, left null per the never-guess rule. Lemar asked for this to be worked into the payment plan, daily totals, and Google Calendar — that scheduling needs a confirmed dollar figure and exact ISO due date first; raised in #decisions."}
  - {id: moms-car-repair-breakdown, name: "Mom's car repair (breakdown)", amount: null,
     cadence: once, due: null, priority: null, status: active,
     note: "reported in #personal-finance 2026-08-11: mom's car broke down, blocking Lemar from DoorDashing until it's fixed. Lemar estimated 'I think we're looking at a $500 repair' — unconfirmed figure, left null; no due date given. Raised in #decisions."}
plans:                               # payment plans: {id, creditor, total, note, installments:
                                     #   [{seq, amount, due, status, calendar_event_id}]}
  - id: liquidibee-nomas-payment-plan
    creditor: "Nomas Recovery LLC (Amanda Ortiz, collections for LIQUIDIBEE 1 LLC)"
    total: 500
    note: "Good-faith payment plan. Originally split evenly across 6 days (2026-08-10
           through the Aug 15 due date) per Lemar's 2026-08-09 #decisions reply; Lemar
           said 2026-08-09 in #personal-finance he can't cover that pace and asked to
           re-spread it across 4 weeks from today instead — RE-SPREAD 2026-08-09 to 4
           weekly $125 installments (8/16, 8/23, 8/30, 9/06). Lemar corrected 2026-08-10
           in #decisions ('I wanted 8 payments not 4') — Samira asked whether that means
           twice-weekly $62.50 within the same 8/16–9/06 window or 8 weekly $62.50
           installments running through ~10/25; UNANSWERED, installments below still
           reflect the old 4-payment schedule pending that reply. Same saga as the
           missed July 15 good-faith payment. Tracking/reminder only — nothing paid or
           contacted. FLAG: the collector's actual stated deadline was Aug 15 —
           this schedule already runs past that and has NOT been communicated to Nomas
           Recovery/Amanda Ortiz; a general extension-request draft was saved to Gmail
           Drafts (not sent) per Lemar's earlier option pick, but doesn't commit to an
           exact payment count since that's still open."
    installments:
      - {seq: 1, amount: 125, due: 2026-08-16, status: pending, calendar_event_id: tja7bjk9ri35n0bqb01c52j4es}
      - {seq: 2, amount: 125, due: 2026-08-23, status: pending, calendar_event_id: gt4knt3i2m6lpjhlrjf8n2jqn8}
      - {seq: 3, amount: 125, due: 2026-08-30, status: pending, calendar_event_id: locnmilchabhgq2o0kd8slf7r4}
      - {seq: 4, amount: 125, due: 2026-09-06, status: pending, calendar_event_id: ekpni2dt25f0fe5tjh51sbjj64}
daily_targets:                       # even daily set-aside ramp (added 2026-08-09)
  "2026-08-10":
    total: 0
    contributions:
      - {bill_id: metrc-fee, amount: 40, status: rolled}
      - {bill_id: cleaning-supplies, amount: 30, status: paid}
      - {bill_id: comedy-show-tickets, amount: 50.28, status: rolled}
      - {bill_id: station-travel, amount: 50, status: rolled}
  "2026-08-11":
    total: 0
    contributions:
      - {bill_id: metrc-fee, amount: 40, status: rolled}
      - {bill_id: comedy-show-tickets, amount: 50.28, status: rolled}
      - {bill_id: station-travel, amount: 50, status: rolled}
  "2026-08-12":
    total: 140.28
    calendar_event_id: p4nlnh093ub4pgap2asi190kl0
    contributions:
      - {bill_id: metrc-fee, amount: 40, status: pending}
      - {bill_id: comedy-show-tickets, amount: 50.28, status: pending}
      - {bill_id: station-travel, amount: 50, status: pending}
goals:
  - {id: own-car-running, name: "Get the car running", pocket: cashapp-checking,
     target: 2800, saved: 0,
     note: "≈ $2,000 repairs + $1,000 taxes/tags/tires − $200 tires paid 7/25; car payment
            $500 also paid 7/25 (both pending Lemar confirming they landed); water-pump
            overlap unreconciled"}
  - {id: savings, name: "Savings (p7)", pocket: sofi-savings, target: null, saved: 0,
     note: "the '30% of income' framing doesn't fit the current waterfall room — needs a
            real number or a shape change (open question)"}
open_questions:
  - "Billing days unknown: student loans, mom's $200, Tidal (asked in the 2026-07-25 #decisions card)"
  - "Cuzzie's phone + Workspace $550/mo is Lemar's estimate — actual phone plan total unconfirmed"
  - "Confirm the 7/25 $1,000 allocation landed: $500 car payment, $200 tires, $50 mom"
  - "T-Mobile: confirm payment 1 ($265, was due 8/3) went through; payment 2 amount/date still needed"
  - "P7 savings '30% of income' vs ~$37/wk waterfall room — pick a number or change the shape"
  - "Water pump $184.79: inside or on top of the $2,000 repairs lump?"
  - "Gym debt $75: which priority does it belong to?"
  - "Claude card declines on the 4th three months running — payment method update is Lemar's own action with Anthropic"
  - "Era Context: SoFi connection needs a reconnect at era.app; Cash App still syncing; plan tier caps at 2 linked accounts. SoFi checking balance now tracked manually instead per Lemar's 2026-08-10 #decisions call (see reported_balances) — Era reconnect still open for SoFi savings + everything else."
  - "METRC $40 (due 8/14): p1 or p2? (Lemar said 'high priority' 8/9, exact bucket unconfirmed — raised in #decisions 2026-08-09)"
  - "Comedy show tickets $50.28 (due 8/12): p5/p6/p7, or no floor/waterfall bucket at all? (Lemar said 'low priority' 8/9, but the waterfall buckets are each tied to a specific pocket — raised in #decisions 2026-08-09)"
  - "Liquidibee/Nomas: does Lemar want the extension-request draft in Gmail Drafts edited/sent now that the payment count is being corrected to 8? Nothing sent yet."
  - "Liquidibee/Nomas: 8 payments — twice-weekly $62.50 within 8/16–9/06, or 8 weekly $62.50 through ~10/25? Raised in #decisions 2026-08-10, ledger/calendar not yet rebuilt pending this answer."
  - "Station travel $50/wk: Lemar started a weekend job at The Station 8/9 — pay rate not yet known, he'll report it in #personal-finance"
  - "'Gas $10' dropped in #personal-finance 2026-08-10 with a receipt photo (IMG_2080.jpeg) — doesn't match any existing bill line (no recurring gas bill, no due date) and isn't income or cash-on-hand. Lemar said in #decisions 2026-08-10 he wants to 'add in receipts for everything I paid for so that it comes off of the total amount I need to make today' — reads as a request for a broader receipts-offset feature, not a direct answer for this specific $10 item. Left OUT of the ledger; flagging for a follow-up #decisions clarification instead of guessing the feature shape or category."
  - "SoFi checking manual balance ($2.54, reported 2026-08-10): now tracked in `reported_balances` per Lemar's #decisions call — no further open question, just noting for the dashboard's Cash position section."
  - "Mom's car oil change (reported 2026-08-11): Lemar said 'about $100' due 'by the end of next week' — need an exact dollar figure and ISO due date before this can be ramped and put on the calendar/payment plan as he asked."
  - "Mom's car repair/breakdown (reported 2026-08-11): Lemar estimated 'I think we're looking at a $500 repair,' and it's blocking DoorDash income until fixed — need a confirmed amount and due date before this becomes a proper bill line."
```

## History

Everything before 2026-08-05 lives in
[[2026-07-11-personal-finance-dashboard-project]] — the project note that developed the
budget from the first rough sketch through the locked Option 3 allocation decision, the
pocket mapping, and the calendar reminders. That note is closed; this ledger carries the
live state forward. Weekly allocation runs and material changes append below.

## Update 2026-08-09 (bill-payment ramp + daily set-aside calendar — PART C, task:20260809_bill-payment-ramp-daily-calendar)

Extended the money-hub skill (`.claude/skills/money-hub/SKILL.md`) per the staged
#admin prompt: every bill/expense with a due date now computes an even daily
set-aside ramp, and the reminder calendar gets ONE combined "set aside today" event
across everything active, instead of Lemar tracking each bill separately. Full spec
(RAMP window math, DAILY CALENDAR aggregate-event rules, end-of-day ROLLOVER) now lives
in the skill; this note adds the new `daily_targets` ledger block and applies the
one-time backfill to the four bills already carrying a future `due` (added earlier this
same run by PART M):

- `metrc-fee` ($40, due 8/14), `cleaning-supplies` ($30, due 8/11),
  `comedy-show-tickets` ($50.28, due 8/12), `station-travel` ($50, due 8/15) — for all
  four, `end` (due − 7 days) fell before `start` (today, since the ramp window can't
  reach into the past for a backfill), so per the rule the FULL amount lands on day 1.
  All four independently land on **2026-08-10** (tomorrow) → one aggregate
  `daily_targets["2026-08-10"]` entry, total **$170.28**, one calendar event
  (`kli8jm1vlal3ntffr2lqdkpmuk`, "Set aside today: $170.28", all-day, popup reminder —
  same convention as the existing per-bill due-date events).
- `tmobile-split-1` ($265, due 2026-08-03) was excluded — its due date has already
  passed, so no ramp window exists for it (not guessed, not back-dated).
- `tmobile-split-2`, `cashapp-payback`, `gym-debt`, `water-pump` — all `due: null`,
  excluded per the guardrail (never guess a date to force a ramp).
- Recurring monthly-`day` bills (Claude, Wispr Flow, Patreon, etc.) were **not**
  auto-backfilled this pass — per the skill's own guard, backfilling would require
  inventing a "logged" date for bills that have existed for weeks; only a freshly
  added/chained recurring cycle gets ramped going forward.
- Each of the four bills' own note field now records the ramp outcome; their existing
  per-bill due-date calendar events are unchanged (the daily aggregate is an ADDITIONAL
  layer, not a replacement).
- ROLLOVER (end-of-day, ≥5pm ET) did not fire this run (run time ≈ 8:53am ET) — it is
  now specified in the skill for the day's last hourly scan going forward.

Nothing paid, nothing contacted, no figure or date guessed. Dashboard re-render:
deferred to the next mode-7/PART M render that touches this ledger (no live artifact
session this pass — page fields for "Today's set-aside" already specified in the
skill's DASHBOARD section for the next render to pick up).

## Update 2026-08-09 (PART M sweep)

Swept #personal-finance (oldest 24h). Four new one-time bills reported by Lemar as
plain text drops — added to the ledger, each projected onto the reminder calendar:

- `metrc-fee` — METRC $40, due 2026-08-14. Priority left `null` (no clear ledger
  pattern to match) — raised in #decisions.
- `cleaning-supplies` — Cleaning supplies (house) $30, due 2026-08-11. Priority left
  `null` — raised in #decisions.
- `comedy-show-tickets` — Comedy show tickets $50.28, due 2026-08-12. Priority left
  `null` — raised in #decisions.
- `station-travel` — Travel to The Station $50, due 2026-08-15. Priority set `p4` —
  matches the existing `transportation` (Rahway → Newark commute) line's priority, a
  direct pattern match, not a guess.

No earnings, cash-on-hand, or payment-plan drops this sweep. No payments marked paid.
Dashboard re-rendered (4 new upcoming-bills rows). One #decisions parent posted
bundling the 3 unassigned priorities.

## Update 2026-08-09 (Liquidibee/Nomas payment-plan setup — PART A)

Per Lemar's reply in the #decisions thread (channel `C0BBXA96FFV`, parent ts
`1786194812.913559`, his reply ts `1786241590.069229`, 2026-08-09): "Can we make sure
that you put this in the #personal-finance channel and we're going to create a series
of Google Calendar events that will serve as a payment plan for this amount. so split
the full amount evenly from tomorrow to August 15th so that I will know how much I need
to earn on Door Dash to be able to pay it on the 15th" — referring to the $500
good-faith payment owed to Amanda Ortiz at Nomas Recovery LLC (collections for
LIQUIDIBEE 1 LLC), due Saturday 2026-08-15, 9:00-9:30am ET (see
[[2026-07-31-liquidibee-forbearance-ends]] for the full history of that saga, including
the missed July 15 good-faith payment).

Added a new `plans` entry, `liquidibee-nomas-payment-plan` ($500 total), split evenly
across the 6 days from tomorrow (2026-08-10) through the due date (2026-08-15):
$83.33/day for 2026-08-10 through 2026-08-14, $83.35 on 2026-08-15 (the extra $0.02
lands on the last day so the six installments sum to exactly $500.00). Each installment
now carries its own reminder-calendar event id.

Calendar: the existing 2026-08-10 aggregate "Set aside today" event
(`kli8jm1vlal3ntffr2lqdkpmuk`) was UPDATED in place — total moved from $170.28 to
$253.61 to fold in this plan's first $83.33 installment alongside the four existing
contributions (METRC, cleaning supplies, comedy tickets, Station travel); the four
existing contributions were left untouched. Five NEW all-day aggregate events were
created, one per remaining day (2026-08-11 through 2026-08-15), each titled "Set aside
today: $83.33" ($83.35 on the 15th), all-day with a popup reminder, on the same
reminder calendar, no attendees. `daily_targets` gained a 5th contribution on
2026-08-10 and five brand-new date entries for 2026-08-11 through 2026-08-15.

Posted a summary to #personal-finance (`C0BGLEMH99T`) and replied in the #decisions
thread so Lemar can close it out. Nothing paid, nothing contacted — Nomas Recovery /
Amanda Ortiz were not reached; this is a tracking/budgeting plan only, per the safety
floor.

## Update 2026-08-09 (Liquidibee/Nomas plan re-spread to 4 weeks — PART C)

Lemar replied in #personal-finance (thread ts `1786281440.216369`, reply ts
`1786286215.944749`): "I'm not going to be able to cover this payment plan right now.
I need like four more weeks to take care of this so let's spread it out between four
weeks from today."

Reworked the plan from 6 daily $83.33 installments (8/10–8/15) to **4 weekly $125
installments** (8/16, 8/23, 8/30, 9/06 — exactly 4 weeks from today, 8/9, with no
rounding remainder since 500/4 is exact):

- Calendar: the 2026-08-10 aggregate event (`kli8jm1vlal3ntffr2lqdkpmuk`) was UPDATED
  in place — Liquidibee's $83.33 contribution removed, total reverted to $170.28
  (METRC + cleaning supplies + comedy tickets + station travel only). The 4 pure
  Liquidibee-only aggregate events for 8/11–8/15 were CANCELLED (not left stale) since
  their sole purpose was this plan. 4 NEW standalone events created for the new weekly
  installments (8/16, 8/23, 8/30, 9/06), each "$125" with day-of + 7-day-before popups.
- `daily_targets` for 8/11–8/15 removed (no more contributions on those days);
  8/10 total corrected to $170.28.
- `plans.liquidibee-nomas-payment-plan.installments` replaced with the 4 new rows.

**Flag, not decided:** the collector's (Nomas Recovery/Amanda Ortiz) stated deadline
was Aug 15 — this new internal savings schedule runs through Sept 6, past that date.
This is purely a change to Lemar's own savings pacing; nothing has been communicated to
Nomas Recovery about paying later, and Samira has not and will not contact them without
Lemar's explicit go-ahead (external-contact safety floor). Raised as an open question
above and as a #decisions card asking whether he wants a draft message prepared (never
sent) explaining a delayed payment.

Nothing paid, nothing contacted, no event deleted-without-replacement (the 4 retired
daily events were purpose-built solely for the old schedule; their function is fully
replaced by the 4 new weekly events). Replied to #personal-finance thread confirming
the rebuild.

## Update 2026-08-10 (PART M sweep)

Swept #personal-finance since the last run (2026-08-09 re-spread). Three new messages,
all from Lemar today, 2026-08-10:

- **Earnings** — a "DoorDash Earnings" screenshot (`IMG_2079.png`, ts `1786369136`)
  followed 8 minutes later by a typed breakdown (ts `1786369598`) giving four weekly
  totals: Jul 20-26 $153.94, Jul 27-Aug 2 $327.70, Aug 3-9 $457.40, Aug 10-16 $61.43
  (partial/in-progress week). Treated as one drop — the typed text supplies the exact
  figures so no image read/confirm was needed. Logged as four entries to
  `income-log-2026.md` (Monday-anchored per the mon-sun week convention), each noted as
  a weekly total and the in-progress one flagged as partial. This is the FIRST income
  logged since the log was created 2026-08-05 (it had sat empty).
- **"Gas $10"** (ts `1786371101`) with a receipt photo (`IMG_2080.jpeg`) — doesn't match
  any existing bill line, isn't income/cash-on-hand, and isn't a payment against a
  tracked plan. Left OUT of the ledger rather than guessing a category; added to
  `open_questions` and raised in #decisions 2026-08-10.
- No cash-on-hand report, no new bills, no payment-plan terms, no "mark paid" this
  sweep. No `daily_targets`/calendar changes (nothing new carries a `due`). ROLLOVER not
  yet due this run.

Dashboard re-rendered (income + this-week numbers now reflect the four logged weeks).
Nothing paid, nothing contacted, no figure guessed.

## Update 2026-08-10 (PART M sweep, 2nd pass)

Swept #personal-finance since the last run (2026-08-10 first pass, which ended at the
"Gas $10" drop, ts `1786371101.191659`). Two new messages, both from Lemar today,
2026-08-10:

- **Cash on hand** (ts `1786373460.228489`, "Cash on hand today: $25") — Mode 2. Set
  `cash_on_hand: {amount: 25, as_of: 2026-08-10}`.
- **"SoFi balance today: $2.54"** (ts `1786373508.071459`) — a reported bank balance,
  not physical cash on hand and not tied to a specific pocket (`sofi-checking` vs.
  `sofi-savings` both map to SoFi; Era Context is the intended live-balance layer, and
  SoFi still needs reconnecting there per the existing open question). No ledger field
  fits this cleanly, so left OUT rather than guess; added to `open_questions` and raised
  in #decisions.

No earnings, bills, payment-plan terms, or "mark paid" this pass. No `daily_targets`/
calendar changes (nothing new carries a `due`). ROLLOVER not yet due (run time ≈2:09pm
ET, gate is ≥5pm ET).

Also found in #decisions (ts `1786307410.388389`, an earlier run today): the
`.claude/skills/money-hub/SKILL.md` file itself is stored as a single base64 blob on
disk (traced to commit `01e027a`) — decodes losslessly to the complete, correct skill
text, and this run read it the same way (in-memory decode, nothing on disk touched).
Still awaiting Lemar's call on that card; not duplicated here, and no skill-file write
made by this pass (outside PART M's scope).

Dashboard re-rendered (cash-on-hand figure now reflects the $25 report). Nothing paid,
nothing contacted, no figure guessed.

## Update 2026-08-10 (PART M sweep, 3rd pass)

Swept #personal-finance since the last run (2nd pass, ended at the SoFi balance drop,
ts `1786373508.071459`). Two new messages, both from Lemar today, 2026-08-10:

- **"$29.95 spent on cleaning supplies"** (ts `1786386505.063809`, receipt photo
  `IMG_2081.jpeg`) — doesn't cleanly match the existing "Cleaning supplies $30" bill
  (due 8/11; unclear if this purchase IS that bill being paid early/differently, or a
  separate expense) and isn't income or cash-on-hand. Left OUT of the ledger rather than
  guess; added to `open_questions`.
- **"DoorDash Earnings : $51.70"** (ts `1786388799.564249`) — Mode 1 (log earnings), no
  date range given so treated as today (2026-08-10). Appended to `income-log-2026.md` as
  its own line rather than merged into the already-logged $61.43 partial-week figure —
  whether it's additional earnings on top or a restated total is unclear. Added to
  `open_questions`.

No cash-on-hand report, no new/updated bills with a `due`, no payment-plan terms, no
"mark paid" this pass. No `daily_targets`/calendar changes needed (nothing carries a new
`due`). ROLLOVER not yet due (run time ≈4:1x pm ET, gate is ≥5pm ET).

Dashboard re-render deferred to the next PART M pass — no material change to the
headline numbers this pass beyond the new income line (which the "This week" section
will pick up next render). Nothing paid, nothing contacted, no figure guessed.

## Update 2026-08-10 (PART A follow-through — #decisions answers processed)

Two #decisions cards Lemar answered this pass, processed directly (not a #personal-
finance sweep — that's PART M, separate):

- **SoFi checking manual tracking** (#decisions ts `1786385477.411649`, Lemar's reply
  ts `1786388173.527179`: "SoFi checking and we will use manual entry instead of Era").
  Added `reported_balances` block to the ledger, first entry `sofi-checking: $2.54,
  as_of: 2026-08-10`. Resolved the open question; Era reconnect for everything else
  (SoFi savings, Cash App) stays open. Replied "Done ✅" in the #decisions thread.
- **Cleaning-supplies bill marked paid** (#decisions ts `1786393175.511769`, Lemar'
  reply ts `1786395169.639189`: "Yes the 29.95 is for the tract[ked] cleaning supplies.
  I paid it early") — Mode 6. Flipped `cleaning-supplies` to `status: paid`
  ($29.95 actual, $0.05 under the tracked $30). Cancelled its due-date calendar event
  (`ue8jtslgpl89qlhdra710h13k`). Flipped its `daily_targets["2026-08-10"]` contribution
  to `paid` and reduced that day's aggregate "Set aside today" event
  (`kli8jm1vlal3ntffr2lqdkpmuk`) from $170.28 to $140.28 (METRC + comedy tickets +
  station travel only now). The DoorDash $51.70 half of that same card is still
  UNANSWERED — left open, nothing guessed. Replied "Done ✅" in the #decisions thread.

Separately, Lemar's Liquidibee/Nomas correction ("I wanted 8 payments not 4," #decisions
ts `1786288639.033759`, reply ts `1786289675.222939`) was already surfaced by Samira
with a follow-up clarifying question (twice-weekly vs. 8-weekly cadence) — still
unanswered, plan/calendar left as the old 4-payment schedule pending that reply (noted
in the `plans` block above; not re-litigated here).

Also noted: Lemar's reply to the "Gas $10" card ("I want to be able to add in receipts
for everything that I paid for so that it comes off of the total amount that I need to
make today") reads as a request for a new receipts-offset feature/design, not a direct
answer to the two specific options originally posed. Left the $10 gas item OUT of the
ledger rather than guess the feature shape; flagged for a follow-up #decisions
clarification instead.

No calendar changes beyond the two described above. Nothing paid, nothing contacted, no
figure guessed. Dashboard re-render deferred to the next pass that also picks up PART
M's sweep (avoids rendering twice in one hourly cycle).

## Update 2026-08-10 (PART M sweep, 4th pass — end-of-day ROLLOVER)

Swept #personal-finance since the last run (3rd pass, ended at the DoorDash $51.70
drop, ts `1786388799.564249`, followed by this bot's own 🌐 summary post at ts
`1786393173.886619`). **No new money drops** — the channel's newest message is still
that same 🌐 summary post; nothing from Lemar has landed since. (The two #decisions
answers processed in between were handled by the separate PART A follow-through above,
not a #personal-finance sweep.)

Run time ≈5:26pm ET — the day's LAST hourly scan (gate ≥5pm ET) — so ROLLOVER fired per
the money-hub skill's ROLLOVER section:

- `daily_targets["2026-08-10"]` had three contributions still `status: pending`
  (`metrc-fee` $40, `comedy-show-tickets` $50.28, `station-travel` $50 — total $140.28)
  and one already `paid` (`cleaning-supplies` $30, untouched — a payment always wins
  over a rollover). All three pending contributions flipped to `status: rolled` and
  their amounts carried into a brand-new `daily_targets["2026-08-11"]` entry (that date
  had no prior entry).
- 2026-08-10's total recomputed to **$0** (every contribution now paid or rolled) — per
  the DAILY CALENDAR rule, a day reaching $0 gets its aggregate event RETIRED: cancelled
  `kli8jm1vlal3ntffr2lqdkpmuk` and cleared its `calendar_event_id` from the ledger.
- 2026-08-11's total is **$140.28** — created a new all-day aggregate event
  (`1fjsh976g0p9ni4ud7urr3jivs`, "Set aside today: $140.28", popup reminders at 0 and
  10080 minutes matching the existing convention, no attendees, description flags all
  three contributions as "rolled from 2026-08-10").
- Each rolled bill's own note field updated to record the rollover (metrc-fee,
  comedy-show-tickets, station-travel).

This is a mechanical daily-housekeeping step, not a payment — nothing was assumed paid,
nothing contacted. Dashboard re-rendered (Today's set-aside now $0, 2026-08-11 carries
the $140.28 rolled target).

## Sources
- Prior project note: `haven/vault/10-Personal/Money/2026-07-11-personal-finance-dashboard-project.md` (full Slack ts provenance lives there)
- Staged prompt: #admin `C0BBLUA7JLX` ts `1786253312.218409`+1786253312.241789`
  (`task:20260809_bill-payment-ramp-daily-calendar`)
- #decisions `C0BBXA96FFV` parent ts `1786194812.913559`, Lemar reply ts
  `1786241590.069229` (2026-08-09) — Liquidibee/Nomas payment-plan instruction
- #personal-finance `C0BGLEMH99T` thread ts `1786281440.216369`, Lemar reply ts
  `1786286215.944749` (2026-08-09) — 4-week re-spread instruction
- #personal-finance `C0BGLEMH99T` ts `1786369136.576589` (DoorDash Earnings screenshot),
  `1786369598.347299` (typed weekly breakdown), `1786371101.191659` ("Gas $10" photo) —
  2026-08-10 PART M sweep
- #personal-finance `C0BGLEMH99T` ts `1786373460.228489` ("Cash on hand today: $25"),
  `1786373508.071459` ("SoFi balance today: $2.54") — 2026-08-10 PART M sweep, 2nd pass
- #personal-finance `C0BGLEMH99T` ts `1786386505.063809` ("$29.95 spent on cleaning
  supplies", photo), `1786388799.564249` ("DoorDash Earnings : $51.70") — 2026-08-10
  PART M sweep, 3rd pass
- #decisions `C0BBXA96FFV` ts `1786385477.411649` (SoFi manual-tracking answer, reply ts
  `1786388173.527179`), ts `1786393175.511769` (cleaning-supplies answer, reply ts
  `1786395169.639189`) — 2026-08-10 PART A follow-through
- #personal-finance `C0BGLEMH99T` ts `1786393173.886619` (this bot's own 🌐 3rd-pass
  summary, the channel's newest message as of this sweep) — 2026-08-10 PART M sweep,
  4th pass / end-of-day ROLLOVER

## Update 2026-08-10 (PART A — DoorDash $51.70 clarification resolved)

Lemar reacted ✅ on Option 1 in the "Money hub — 2 quick clarifications" card
(#decisions ts `1786393175.511769`, option reply ts `1786393179.543229`): the
$51.70 DoorDash drop is **additional** earnings on top of the already-logged $61.43
partial-week (Aug 10-16) figure, not a restatement. Running week-so-far total is
**$113.13**. Nothing re-summed here — `income-log-2026.md` is append-only, so the
reconciliation is recorded there as a new zero-amount note line rather than editing
the two existing entries. Removed the now-resolved DoorDash line from
`open_questions` above. Replied "Done ✅" in-thread.

## Sources (cont.)
- #decisions `C0BBXA96FFV` ts `1786393175.511769`, option reply ts
  `1786393179.543229`, Lemar ✅ — 2026-08-10 PART A follow-through

## Update 2026-08-11 (PART M sweep)

Swept #personal-finance since the last run (4th pass, 2026-08-10, ended at this bot's
own 🌐 3rd-pass summary post ts `1786393173.886619`). Two new messages, both from Lemar
today, 2026-08-11:

- **"Okay notice that my mom's car is probably going to need an oil change by the end
  of next week. It'll be about $100 so can we put that on the payment plan, make sure
  that it's worked into our daily totals and on the Google event calendar?"**
  (ts `1786402207.550489`). This reads as a genuine money drop (a bill being reported),
  but both figures are hedged/unconfirmed — "about $100" and "by the end of next week"
  is not an ISO date. Per the never-guess-a-number/date rule, added a new bill line
  `moms-car-oil-change` with `amount: null, due: null, priority: null` rather than
  inventing a figure or date. Because `due: null`, **no** ramp was computed and **no**
  calendar event was created (per the skill's CALENDAR section: `day: null`/`due: null`
  → no event, the gap rides in `open_questions` until Lemar supplies the date). His
  explicit ask to wire this into "the payment plan," "daily totals," and "the Google
  event calendar" is exactly what will happen once he confirms the amount and exact
  date — nothing was executed instruction-style ahead of that confirmation.
- **"My mom's car just broke down, meaning that I can't DoorDash until it's fixed. I
  think we're looking at a $500 repair"** (ts `1786413446.708309`) — a second, separate
  money drop (the routine oil-change need vs. an urgent breakdown are different
  issues). "I think we're looking at a $500 repair" is an estimate, not a confirmed
  figure, and no due date was given at all. Added a second new bill line
  `moms-car-repair-breakdown` with `amount: null, due: null, priority: null` for the
  same reason — left null rather than guessed. No ramp, no calendar event (no `due`).

Both figures/dates raised together in ONE #decisions parent (bundling both items into a
single card rather than two separate pings) asking Lemar to confirm: (1) the oil
change's exact dollar amount and exact due date, and (2) the repair's exact dollar
amount and due date. No earnings, cash-on-hand, or payment-plan-terms drops this sweep;
no "mark paid". ROLLOVER not due this run (not the day's last hourly scan).

Dashboard re-rendered: two new "no date yet" bills reflected in the Upcoming Bills
section's "no date yet" strip, and the two new open questions appended to the Open
Questions section — no other section changed (no amounts, no calendar events, no
income). Nothing paid, nothing contacted, no figure or date guessed.

## Sources (cont. 2)
- #personal-finance `C0BGLEMH99T` ts `1786402207.550489` (mom's car oil change, "about
  $100," due "end of next week"), ts `1786413446.708309` (mom's car breakdown, "I think
  ... $500 repair") — 2026-08-11 PART M sweep

## Update 2026-08-11 (PART M sweep, 2nd pass)

Swept #personal-finance since the last run (1st pass 2026-08-11, ended at the mom's-car
breakdown drop, ts `1786413446.708309`, followed by this bot's own 🌐 summary post ts
`1786451044.122119`). One new message, from Lemar today, 2026-08-11:

- **"Cash on hand today - $20"** (ts `1786464148.853639`) — Mode 2, unambiguous figure.
  Set `cash_on_hand: {amount: 20, as_of: 2026-08-11}` (was $25 as of 2026-08-10).

No earnings, bills, payment-plan terms, or "mark paid" this pass. No `daily_targets`/
calendar changes (nothing new carries a `due`). ROLLOVER not due this run. The two
mom's-car open questions from the prior pass remain unanswered — not re-pinged this
pass (already surfaced in the bundled #decisions card).

Dashboard re-render deferred — no live artifact session available this pass; the new
cash-on-hand figure is captured here in the ledger (source of truth) and will render on
the next PART P/M pass that touches the artifact.

## Sources (cont. 3)
- #personal-finance `C0BGLEMH99T` ts `1786464148.853639` ("Cash on hand today - $20") —
  2026-08-11 PART M sweep, 2nd pass

## Update 2026-08-11 (PART M sweep, 3rd pass — end-of-day ROLLOVER + deferred render)

Swept #personal-finance since the last run (2nd pass, ended at the cash-on-hand drop,
ts `1786464148.853639`). **No new money drops** — that message is still the channel's
newest as of this pass; the cash-on-hand $20 figure it reported was already committed
to the ledger by the prior pass (commit `4d304e5`), so nothing new to log here.

Run time ≈5:19pm ET — at/after the ROLLOVER gate (≥5pm ET) — so ROLLOVER fired per the
money-hub skill's ROLLOVER section:

- `daily_targets["2026-08-11"]` had three contributions still `status: pending`
  (`metrc-fee` $40, `comedy-show-tickets` $50.28, `station-travel` $50 — total $140.28).
  All three flipped to `status: rolled` and their amounts carried into a brand-new
  `daily_targets["2026-08-12"]` entry (that date had no prior entry).
- 2026-08-11's total recomputed to **$0** — per the DAILY CALENDAR rule, cancelled its
  aggregate event (`1fjsh976g0p9ni4ud7urr3jivs`) and cleared the id from the ledger.
- 2026-08-12's total is **140.28** — created a new all-day aggregate event
  (`p4nlnh093ub4pgap2asi190kl0`, "Set aside today: $140.28", popup reminders at 0 and
  10080 minutes, no attendees, description flags all three contributions as "rolled
  from 2026-08-11"). Note: `comedy-show-tickets` is also DUE 2026-08-12 — its own
  per-bill due-date event (`jfh8548cet84pcqo3o697fkbq8`) is untouched and separate from
  this daily aggregate layer, per the skill's DAILY CALENDAR doctrine (both are
  expected, not a duplicate).
- Each rolled bill's own note field updated to record the second rollover (metrc-fee,
  comedy-show-tickets, station-travel).

This is a mechanical daily-housekeeping step, not a payment — nothing was assumed paid,
nothing contacted. Dashboard re-rendered this pass as well, picking up the deferred
cash-on-hand $20 figure from the prior pass together with this ROLLOVER (avoids two
renders in one cycle).

## Sources (cont. 4)
- Google Calendar `c_205bab62b8bb2c4fe12eec38bbc6725abaf6f5f11b767fe99a542112cf5695d3@group.calendar.google.com` — cancelled `1fjsh976g0p9ni4ud7urr3jivs` (2026-08-11 aggregate, $0), created `p4nlnh093ub4pgap2asi190kl0` (2026-08-12 aggregate, $140.28) — 2026-08-11 PART M sweep, 3rd pass / end-of-day ROLLOVER
