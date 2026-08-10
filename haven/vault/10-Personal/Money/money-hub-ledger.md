---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-10T14:09:00-04:00
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
  amount: 25                         # reported #personal-finance 2026-08-10 ("Cash on hand today: $25")
  as_of: 2026-08-10
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
     note: "reported in #personal-finance 2026-08-09; priority unassigned — flagged in #decisions 2026-08-09 (Lemar said 'high priority' 8/9, exact p1-vs-p2 bucket still unconfirmed). Ramped 2026-08-09: due date under 8 days out when logged, so full $40 lands on 2026-08-10 (see daily_targets)."}
  - {id: cleaning-supplies, name: "Cleaning supplies (house)", amount: 30, cadence: once,
     due: 2026-08-11, priority: null, status: active,
     calendar_event_id: ue8jtslgpl89qlmhdra710h13k,
     note: "reported in #personal-finance 2026-08-09; priority unassigned — flagged in #decisions 2026-08-09 (Lemar said 'high priority' 8/9, exact p1-vs-p2 bucket still unconfirmed). Ramped 2026-08-09: due date under 8 days out when logged, so full $30 lands on 2026-08-10 (see daily_targets)."}
  - {id: comedy-show-tickets, name: "Comedy show tickets", amount: 50.28, cadence: once,
     due: 2026-08-12, priority: null, status: active,
     calendar_event_id: jfh8548cet84pcqo3o697fkbq8,
     note: "reported in #personal-finance 2026-08-09; priority unassigned — flagged in #decisions 2026-08-09 (Lemar said 'low priority' 8/9; p5/p6/p7 are each tied to a specific pocket (own-car/side-projects/savings) so the bucket still needs confirming). Ramped 2026-08-09: due date under 8 days out when logged, so full $50.28 lands on 2026-08-10 (see daily_targets)."}
  - {id: station-travel, name: "Travel to The Station", amount: 50, cadence: once,
     due: 2026-08-15, priority: p4, status: active,
     calendar_event_id: ptacguksk2rsf3md3403gljtes,
     note: "reported in #personal-finance 2026-08-09; priority p4 matches the existing Rahway→Newark commute pattern, confirmed by Lemar 8/9 ('median priority'). Ramped 2026-08-09: due date under 8 days out when logged, so full $50 lands on 2026-08-10 (see daily_targets). Lemar 8/9: likely becoming a recurring weekly expense (new weekend job at The Station) — rate TBD, he'll post it in #personal-finance."}
plans:                                # payment plans: {id, creditor, total, note, installments:
                                     #   [{seq, amount, due, status, calendar_event_id}]}
  - id: liquidibee-nomas-payment-plan
    creditor: "Nomas Recovery LLC (Amanda Ortiz, collections for LIQUIDIBEE 1 LLC)"
    total: 500
    note: "Good-faith payment plan. Originally split evenly across 6 days (2026-08-10
           through the Aug 15 due date) per Lemar's 2026-08-09 #decisions reply; Lemar
           said 2026-08-09 in #personal-finance he can't cover that pace and asked to
           re-spread it across 4 weeks from today instead — RE-SPREAD 2026-08-09 to 4
           weekly $125 installments (8/16, 8/23, 8/30, 9/06). Same saga as the missed
           July 15 good-faith payment. Tracking/reminder only — nothing paid or
           contacted. FLAG: the collector's actual stated deadline was Aug 15 —
           this new schedule runs past that and has NOT been communicated to Nomas
           Recovery/Amanda Ortiz; raised in #decisions since contacting them to
           renegotiate is outside what Samira can do unattended."
    installments:
      - {seq: 1, amount: 125, due: 2026-08-16, status: pending, calendar_event_id: tja7bjk9ri35n0bqb01c52j4es}
      - {seq: 2, amount: 125, due: 2026-08-23, status: pending, calendar_event_id: gt4knt3i2m6lpjhlrjf8n2jqn8}
      - {seq: 3, amount: 125, due: 2026-08-30, status: pending, calendar_event_id: locnmilchabhgq2o0kd8slf7r4}
      - {seq: 4, amount: 125, due: 2026-09-06, status: pending, calendar_event_id: ekpni2dt25f0fe5tjh51sbjj64}
daily_targets:                       # even daily set-aside ramp (added 2026-08-09)
  "2026-08-10":
    total: 170.28
    calendar_event_id: kli8jm1vlal3ntffr2lqdkpmuk
    contributions:
      - {bill_id: metrc-fee, amount: 40, status: pending}
      - {bill_id: cleaning-supplies, amount: 30, status: pending}
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
  - "Era Context: SoFi connection needs a reconnect at era.app; Cash App still syncing; plan tier caps at 2 linked accounts"
  - "METRC $40 (due 8/14): p1 or p2? (Lemar said 'high priority' 8/9, exact bucket unconfirmed — raised in #decisions 2026-08-09)"
  - "Cleaning supplies $30 (due 8/11): p1 or p2? (Lemar said 'high priority' 8/9, exact bucket unconfirmed — raised in #decisions 2026-08-09)"
  - "Comedy show tickets $50.28 (due 8/12): p5/p6/p7, or no floor/waterfall bucket at all? (Lemar said 'low priority' 8/9, but the waterfall buckets are each tied to a specific pocket — raised in #decisions 2026-08-09)"
  - "Liquidibee/Nomas: the re-spread 4-week savings schedule (through 9/06) runs past the collector's stated Aug 15 deadline — does Lemar want a draft message prepared for Nomas Recovery explaining the delay? Raised in #decisions 2026-08-09, nothing drafted or sent yet."
  - "Station travel $50/wk: Lemar started a weekend job at The Station 8/9 — pay rate not yet known, he'll report it in #personal-finance"
  - "'Gas $10' dropped in #personal-finance 2026-08-10 with a receipt photo (IMG_2080.jpeg) — doesn't match any existing bill line (no recurring gas bill, no due date) and isn't income or cash-on-hand. Unclear if Lemar wants this tracked as a new recurring/one-time expense line (and if so what cadence/pocket) or if it's just an FYI needing no ledger action. Raised in #decisions 2026-08-10, nothing added to the ledger."
  - "'SoFi balance today: $2.54' dropped in #personal-finance 2026-08-10 — a reported bank balance, not cash on hand (the `cash_on_hand` field is for physical cash) and not tied to a specific pocket (both `sofi-checking` and `sofi-savings` map to SoFi). No ledger field exists for a manually-reported account balance (that's Era Context's job, and SoFi still needs reconnecting per the open question above). Left OUT of the ledger rather than guess which pocket/field it belongs in; raised in #decisions 2026-08-10."
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

## Sources
- Prior project note: `haven/vault/10-Personal/Money/2026-07-11-personal-finance-dashboard-project.md` (full Slack ts provenance lives there)
- Staged prompt: #admin `C0BBLUA7JLX` ts `1786253312.218409`+`1786253312.241789`
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
