---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-09T08:10:00-04:00
domain: personal
type: reference
status: active
tags: [personal-finance, budget, money-hub]
source: claude
area: money
---

# Money Hub — ledger (source of truth)

This note is the ONE structured source of truth for Lemar's personal budget: bills,
account pockets, payment plans, goals, allocation config, and reported cash. The
**money-hub** skill (`.claude/skills/money-hub/SKILL.md`) reads and writes the single
fenced `yaml` block below; the Money Hub dashboard artifact and all calendar reminder
events are regenerated FROM it, never hand-edited (same doctrine as
[[on-button-reopen]]'s index).

Field rules (on-button-plan pattern):
- Amounts are plain numbers (USD). `null` = unknown/TBD — never invent a figure.
- Dedupe by `id` (kebab-case, stable). Never delete a line: a settled bill goes
  `status: paid`; a dropped one `status: parked`.
- `day` = day-of-month for monthly bills; `due` = ISO date for one-time items and
  installments. A `calendar_event_id` marks the reminder event that projects the line
  onto the reminder calendar (calendar is a one-way rendering; this note wins).
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
  amount: null                       # Lemar reports: "I have $X cash"
  as_of: null
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
     note: "due date has passed — confirm paid, then flip to paid and retire the event"}
  - {id: tmobile-split-2, name: "T-Mobile split payment 2 of 2", amount: null, cadence: once,
     due: null, priority: p2, status: active, note: "amount and date not given yet"}
  - {id: gym-debt, name: "Personal gym debt", amount: 75, cadence: once, due: null,
     priority: null, status: active, note: "priority unassigned — Lemar to slot it"}
  - {id: water-pump, name: "New water pump", amount: 184.79, cadence: once, due: null,
     priority: p5, status: active,
     note: "unclear if inside or on top of the $2,000 repairs lump — unreconciled"}
  - {id: metrc-fee, name: METRC, amount: 40, cadence: once, due: 2026-08-14,
     priority: null, status: active, calendar_event_id: q36k3ogoblpe3i5amktigav8ig,
     note: "reported in #personal-finance 2026-08-09; priority unassigned — flagged in #decisions 2026-08-09"}
  - {id: cleaning-supplies, name: "Cleaning supplies (house)", amount: 30, cadence: once,
     due: 2026-08-11, priority: null, status: active,
     calendar_event_id: ue8jtslgpl89qlmhdra710h13k,
     note: "reported in #personal-finance 2026-08-09; priority unassigned — flagged in #decisions 2026-08-09"}
  - {id: comedy-show-tickets, name: "Comedy show tickets", amount: 50.28, cadence: once,
     due: 2026-08-12, priority: null, status: active,
     calendar_event_id: jfh8548cet84pcqo3o697fkbq8,
     note: "reported in #personal-finance 2026-08-09; priority unassigned — flagged in #decisions 2026-08-09"}
  - {id: station-travel, name: "Travel to The Station", amount: 50, cadence: once,
     due: 2026-08-15, priority: p4, status: active,
     calendar_event_id: ptacguksk2rsf3md3403gljtes,
     note: "reported in #personal-finance 2026-08-09; priority p4 matches the existing Rahway→Newark commute pattern"}
plans: []                            # payment plans: {id, creditor, total, note, installments:
                                     #   [{seq, amount, due, status, calendar_event_id}]}
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
  - "METRC $40 (due 8/14): which priority does it belong to? (raised in #decisions 2026-08-09)"
  - "Cleaning supplies $30 (due 8/11): which priority does it belong to? (raised in #decisions 2026-08-09)"
  - "Comedy show tickets $50.28 (due 8/12): which priority does it belong to? (raised in #decisions 2026-08-09)"
```

## History

Everything before 2026-08-05 lives in
[[2026-07-11-personal-finance-dashboard-project]] — the project note that developed the
budget from the first rough sketch through the locked Option 3 allocation decision, the
pocket mapping, and the calendar reminders. That note is closed; this ledger carries the
live state forward. Weekly allocation runs and material changes append below.

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

## Sources
- Prior project note: `haven/vault/10-Personal/Money/2026-07-11-personal-finance-dashboard-project.md` (full Slack ts provenance lives there)
