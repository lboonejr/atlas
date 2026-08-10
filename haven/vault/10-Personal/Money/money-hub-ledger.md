---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-10T14:45:00-04:00
domain: personal
type: reference
status: active
tags: [personal-finance, budget, money-hub]
source: claude
area: money
---

# Money Hub — ledger (source of truth)

This note is the ONE structured source of truth for Lemar's personal budget: bills,
payment plans, goals, the two account pockets, the daily accrual, and reported cash. The **money-hub** skill (`.claude/skills/money-hub/SKILL.md`) reads and writes the
single fenced `yaml` block below; the Money Hub dashboard artifact and all calendar
reminder events (both per-bill due-date events and the daily "set aside today"
aggregate) are regenerated FROM it, never hand-edited (same doctrine as
[[on-button-reopen]]'s index).

Field rules (on-button-plan pattern):
- Amounts are plain numbers (USD). `null` = unknown/TBD — never invent a figure or a date.
- Dedupe by `id` (kebab-case, stable). Never delete a line: a settled bill goes
  `status: paid`; a dropped one `status: parked`.
- `day` = day-of-month for monthly bills; `due` = ISO date for one-time items and
  installments. A `calendar_event_id` marks the reminder event that projects the line
  onto the calendar (calendar is a one-way rendering; this note wins).
- `balance` / `balance_as_of` on a pocket = a figure LEMAR REPORTED, never fetched (the
  Era connector was retired 2026-08-10). `null` renders "not reported", never $0, and is
  never inferred from the income log. Older than 7 days renders stale with its true date.
  A reported balance is never adjusted to match what the ledger expected.
- `track` = `queue` (must carry a date; accrues daily and queues) or `spending` (paid
  as you go from the Spending pocket; no date, no accrual, not a defect). Added 2026-08-10.
- `daily_targets` = the daily accrual. ISO date key → `{operating_reserve, target,
  total_claim, gas_spent, swept_to_maintenance, funded, shortfall,
  calendar_event_id, contributions: [{line_id, amount, funded, status}]}`, `status` one
  of `pending` | `partial` | `funded` | `rolled` | `paid`. One aggregate calendar event
  per day, maintained on a rolling 7-day window. `operating_reserve` stays in Spending
  (gas); `target` moves to Set-Aside (bills); `total_claim` is the two added — what the
  day costs. `funded` = set aside; `paid` = the bill was actually settled. Never conflate
  the two. Past days are history — never rewritten.
- **The allocation SHAPE is DUE-DATE ORDER, locked 2026-08-10** — no priority tiers, no
  weekly floor, no waterfall. Do not redesign it here.
- **A `track: queue` line with no date is a defect, not a low priority.** It has no
  position in the queue, no calendar event, and accrues $0/day — it is invisible. Every
  one of them belongs in `open_questions` until Lemar supplies a date.
- Weekly runs append `## Update` sections below; the yaml holds state, the Updates hold
  history.

```yaml
config:
  week: mon-sun
  allocation: due-date-order         # LOCKED 2026-08-10 — replaces option-3-hybrid
                                     # (floor + waterfall, 2026-07-24, now RETIRED).
                                     # Sort every dated line by date; soonest funded
                                     # first. No tiers, no floor, no waterfall.
  income_target_weekly: 500          # UNVALIDATED — never a confirmed average. Lemar is
                                     # backfilling ~2 weeks of DoorDash earnings into
                                     # #personal-finance (2026-08-10); replace this with
                                     # the trailing 4-week average once entries land.
  overload_check: trailing-4wk-avg   # see the skill's OVERLOAD CHECK; skipped while the
                                     # income log holds fewer than 7 entries
  accrual: daily-drip                # LOCKED 2026-08-10 — every dated line spreads evenly
                                     # over [today .. due-1]; one combined daily number.
                                     # Replaces the 7-day-window RAMP (2026-08-09).
  funding_buffer_days: 0             # fully funded BY the due date (Lemar's framing:
                                     # "$100/month is $3.33/day"). Set 7 to be funded a
                                     # week early — raises every daily figure ~30%.
                                     # Separate from the 7-day calendar popup, which stays.
  daily_event_window: 7              # rolling: maintain aggregate calendar events for
                                     # today..+6 only; extend one day forward each scan
daily_allowances:                    # LOCKED 2026-08-10. FIRST claim on each day's
                                     # income — gas is the cost of earning it, not a bill
                                     # competing with bills. Stays in the Spending pocket
                                     # and is spent same-day; it never moves to Set-Aside.
  gas_maintenance:
    reserve: 30                      # held back daily (Lemar: "$25 to $30 max a day")
    soft_target: 25                  # what he aims to actually spend
    bucket: maintenance
    note: "Unspent remainder (reserve − actual spend) sweeps to the maintenance bucket
           ONLY when Lemar reports a figure. An unreported day is assumed spent — never
           credit the bucket from silence. A spend above the reserve is recorded as-is,
           never capped, and eats into that day's bill funding."
buckets:                             # accumulating balances, physically inside Set-Aside
  - {id: maintenance, name: "Car maintenance", balance: 0, pocket: set-aside,
     note: "Fed by the daily gas sweep. Funds repairs/maintenance. Money only leaves it
            on Lemar's explicit say-so — it never silently backfills a missed bill.
            FLAG 2026-08-10: `pocket: set-aside` now resolves to SoFi Checking, the
            bill-paying account, which is a poor home for a savings balance — it will sit
            mixed in with money earmarked for bills. Left as-is rather than moved to
            SoFi Savings, because that is Lemar's call. See open_questions."}
cash_on_hand:
  amount: null                       # Lemar reports: "I have $X cash"
  as_of: null
pockets:                             # TWO pockets. Account mapping CORRECTED 2026-08-10
                                     # by Lemar (see the Update below) — the roles are
                                     # unchanged, the accounts behind them swapped.
                                     # Lemar moves the money; nothing here transfers.
  - {id: spending, name: "Spending", account: doordash-crimson,
     balance: null, balance_as_of: null, status: active,
     role: "income lands here (DoorDash payouts); gas and day-to-day spending pay from here"}
  - {id: set-aside, name: "Set-Aside", account: sofi-checking,
     balance: null, balance_as_of: null, status: active,
     role: "the daily set-aside number moves here; every recurring bill is paid out of
            this account",
     note: "last known $128.78 as of 2026-07-11 came from the retired Era connector and
            is a month stale — deliberately NOT carried into `balance`, which only ever
            holds a figure Lemar reported."}
  # -- parked: still Lemar's accounts, not part of the model. Never resurrect without an
  #    explicit instruction.
  - {id: sofi-savings, status: parked, balance: null, balance_as_of: null,
     note: "was Set-Aside until the 2026-08-10 account correction. Now unassigned — the
            natural home for the maintenance bucket, but Lemar has not said so. UNRESOLVED,
            see open_questions; the bucket's pocket stays as written until he does."}
  - {id: cashapp-checking,  status: parked, balance: null, balance_as_of: null, note: "was p5 own-car pocket"}
  - {id: cashapp-savings,   status: parked, balance: null, balance_as_of: null, note: "was p6 side-projects pocket"}
bills:
  # -- monthly, queued (needs a billing day to be visible) --
  - {id: cuzzies-phone-workspace, name: "Cuzzie's phone + Google Workspace", amount: 550,
     cadence: monthly, day: null, track: queue, status: active, business_origin: true,
     note: "Lemar's own estimate 2026-07-22; actual recurring phone total unconfirmed.
            Business-origin cost he chose to carry personally (his stated #1 on
            2026-07-22), so it stays in this ledger — but it is the single largest line
            here and it is BOTH undated and unverified. Its reminder, once dated,
            belongs on the Cuzzie's (Owners) calendar per the business boundary."}
  - {id: student-loans, name: Student loans, amount: 500, cadence: monthly, day: null,
     track: queue, status: active, note: "~$8,000 remaining; billing day unknown — undated, invisible to the queue"}
  - {id: claude, name: Claude subscription, amount: 100, cadence: monthly, day: 4,
     track: queue, status: active, calendar_event_id: 7djf895pc8is0illrr8bcrra20,
     note: "card declined on the 4th May/Jun/Jul — Lemar to update payment method"}
  - {id: wispr-flow, name: Wispr Flow, amount: 15, cadence: monthly, day: 10,
     track: queue, status: active, calendar_event_id: e7d9muku31setk1b10le3bf3ak}
  - {id: moms-expenses, name: "Mom's expenses", amount: 200, cadence: monthly, day: null,
     track: queue, status: active, note: "billing day unknown — undated, invisible to the queue"}
  - {id: tidal, name: Tidal, amount: 14.92, cadence: monthly, day: null,
     track: queue, status: active, note: "billing day unknown — undated, invisible to the queue"}
  - {id: patreon, name: Patreon, amount: 25, cadence: monthly, day: 27,
     track: queue, status: active, calendar_event_id: lf7pne54rrtcnrvekhq0fecec4,
     note: "27th confirmed 2026-07-28 after a 10th-vs-27th conflict"}
  # -- day-to-day spending: paid as you go from the Spending pocket, never accrued --
  - {id: food, name: Food, amount: 600, cadence: monthly, day: null,
     track: spending, status: active, note: "~$20/day, spread across the month. Not a
            defect: this is Spending-pocket money, not a set-aside line."}
  - {id: transportation, name: "Transportation (Rahway → Newark)", amount: null,
     cadence: variable, day: null, track: spending, status: active,
     note: "$4.95/one-way NJ Transit (needs app spot-check); Spending-pocket money.
            Monthly total depends on Newark days/week."}
  # -- one-time, queued --
  - {id: cashapp-payback, name: "Cash App payback", amount: 187.22, cadence: once,
     due: null, track: queue, status: active, note: "'own pace, no fixed date' — under
            due-date order that means it never comes up. Needs a date or a parked status."}
  - {id: tmobile-split-1, name: "T-Mobile split payment 1 of 2", amount: 265, cadence: once,
     due: 2026-08-03, track: queue, status: active,
     calendar_event_id: pg0a92rgg01l09mg3tatcfb3mk,
     note: "due date has passed — confirm paid, then flip to paid and retire the event."}
  - {id: tmobile-split-2, name: "T-Mobile split payment 2 of 2", amount: null, cadence: once,
     due: null, track: queue, status: active, note: "amount and date not given yet"}
  - {id: gym-debt, name: "Personal gym debt", amount: 75, cadence: once, due: null,
     track: queue, status: active, note: "undated, invisible to the queue"}
  - {id: water-pump, name: "New water pump", amount: 184.79, cadence: once, due: null,
     track: queue, status: active,
     note: "unclear if inside or on top of the car goal's repairs figure — unreconciled"}
  - {id: metrc-fee, name: METRC, amount: 40, cadence: once, due: 2026-08-14,
     track: queue, status: active, calendar_event_id: q36k3ogoblpe3i5amktigav8ig,
     note: "reported in #personal-finance 2026-08-09. Priority field retired 2026-08-10 —
            its due date is now its whole position in the queue. Ramped: full $40 on 2026-08-10."}
  - {id: cleaning-supplies, name: "Cleaning supplies (house)", amount: 30, cadence: once,
     due: 2026-08-11, track: queue, status: active,
     calendar_event_id: ue8jtslgpl89qlmhdra710h13k,
     note: "reported in #personal-finance 2026-08-09. Ramped: full $30 on 2026-08-10."}
  - {id: comedy-show-tickets, name: "Comedy show tickets", amount: 50.28, cadence: once,
     due: 2026-08-12, track: queue, status: active,
     calendar_event_id: jfh8548cet84pcqo3o697fkbq8,
     note: "reported in #personal-finance 2026-08-09. Ramped: full $50.28 on 2026-08-10.
            The 'low priority' call from 8/9 no longer has anywhere to live under
            due-date order — if this should slip behind the rest, say so and it parks."}
  - {id: station-travel, name: "Travel to The Station", amount: 50, cadence: once,
     due: 2026-08-15, track: queue, status: active,
     calendar_event_id: ptacguksk2rsf3md3403gljtes,
     note: "reported in #personal-finance 2026-08-09. Ramped: full $50 on 2026-08-10.
            Lemar 8/9: likely becoming a recurring weekly expense (new weekend job at
            The Station) — rate TBD, he'll post it in #personal-finance."}
plans:
  - id: liquidibee-nomas-payment-plan
    creditor: "Nomas Recovery LLC (Amanda Ortiz, collections for LIQUIDIBEE 1 LLC)"
    total: 500
    note: "Good-faith payment plan, 4 weekly $125 installments (8/16, 8/23, 8/30, 9/06),
           re-spread 2026-08-09 at Lemar's request. Same saga as the missed July 15
           good-faith payment. Tracking/reminder only — nothing paid or contacted.
           2026-08-10: Lemar is handling the Nomas Recovery conversation DIRECTLY — no
           draft, no outreach, no #decisions card. The reminders stay; the relationship
           is his. The collector's stated deadline was Aug 15 and this schedule runs to
           Sept 6; that is Lemar's informed call, not an open question."
    installments:
      - {seq: 1, amount: 125, due: 2026-08-16, status: pending, calendar_event_id: tja7bjk9ri35n0bqb01c52j4es}
      - {seq: 2, amount: 125, due: 2026-08-23, status: pending, calendar_event_id: gt4knt3i2m6lpjhlrjf8n2jqn8}
      - {seq: 3, amount: 125, due: 2026-08-30, status: pending, calendar_event_id: locnmilchabhgq2o0kd8slf7r4}
      - {seq: 4, amount: 125, due: 2026-09-06, status: pending, calendar_event_id: ekpni2dt25f0fe5tjh51sbjj64}
daily_targets:                       # THE DAILY ACCRUAL (rebuilt 2026-08-10). Every
                                     # dated line drips a daily amount; target = the sum
                                     # of that day's drips = what today costs. `funded` is
                                     # what the day's logged income actually covered;
                                     # `shortfall` drags to tomorrow via ROLLOVER.
                                     # Computed 2026-08-10 from a zero start, so the first
                                     # days run hot (catch-up) and decay toward steady
                                     # state as the short-fuse lines clear.
  "2026-08-10":
    operating_reserve: 30.00
    target: 136.96
    total_claim: 166.96
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 136.96
    calendar_event_id: kli8jm1vlal3ntffr2lqdkpmuk
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: cleaning-supplies, amount: 30.00, funded: 0, status: pending}
      - {line_id: comedy-show-tickets, amount: 25.14, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 20.84, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 10.00, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.48, funded: 0, status: pending}
      - {line_id: station-travel, amount: 10.00, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 15.00, funded: 0, status: pending}
  "2026-08-11":
    operating_reserve: 30.00
    target: 92.44
    total_claim: 122.44
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 92.44
    calendar_event_id: vj19k5hjaq1krci59o1flcbj78
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: comedy-show-tickets, amount: 25.14, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 20.84, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 10.00, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: station-travel, amount: 10.00, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-12":
    operating_reserve: 30.00
    target: 67.29
    total_claim: 97.29
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 67.29
    calendar_event_id: hknnvpq91j5192c4ljvdskf9s4
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 20.83, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 10.00, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: station-travel, amount: 10.00, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-13":
    operating_reserve: 30.00
    target: 67.29
    total_claim: 97.29
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 67.29
    calendar_event_id: jho94o6sql4qjt6fdgjl0ej2oc
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 20.83, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 10.00, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: station-travel, amount: 10.00, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-14":
    operating_reserve: 30.00
    target: 57.29
    total_claim: 87.29
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 57.29
    calendar_event_id: d8ed3o469dh4r5j0c2qo73m6cs
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 20.83, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: station-travel, amount: 10.00, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-15":
    operating_reserve: 30.00
    target: 47.29
    total_claim: 77.29
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 47.29
    calendar_event_id: k9sog0mcpmisnn4p2hicernagk
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 20.83, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-16":
    operating_reserve: 30.00
    target: 26.46
    total_claim: 56.46
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 26.46
    calendar_event_id: i5aqp4u51gvj79113o7ls4ajqk
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-17":
    operating_reserve: 30.00
    target: 26.45
    total_claim: 56.45
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 26.45
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.61, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-18":
    operating_reserve: 30.00
    target: 26.45
    total_claim: 56.45
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 26.45
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.61, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-19":
    operating_reserve: 30.00
    target: 26.45
    total_claim: 56.45
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 26.45
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.61, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-20":
    operating_reserve: 30.00
    target: 26.45
    total_claim: 56.45
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 26.45
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.61, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-21":
    operating_reserve: 30.00
    target: 26.45
    total_claim: 56.45
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 26.45
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.61, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-22":
    operating_reserve: 30.00
    target: 26.45
    total_claim: 56.45
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 26.45
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 9.61, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: pending}
  "2026-08-23":
    operating_reserve: 30.00
    target: 16.83
    total_claim: 46.83
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.83
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-08-24":
    operating_reserve: 30.00
    target: 16.83
    total_claim: 46.83
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.83
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-08-25":
    operating_reserve: 30.00
    target: 16.83
    total_claim: 46.83
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.83
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-08-26":
    operating_reserve: 30.00
    target: 16.83
    total_claim: 46.83
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.83
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: patreon, amount: 1.47, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-08-27":
    operating_reserve: 30.00
    target: 15.36
    total_claim: 45.36
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 15.36
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-08-28":
    operating_reserve: 30.00
    target: 15.36
    total_claim: 45.36
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 15.36
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-08-29":
    operating_reserve: 30.00
    target: 15.36
    total_claim: 45.36
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 15.36
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-08-30":
    operating_reserve: 30.00
    target: 9.11
    total_claim: 39.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 9.11
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-08-31":
    operating_reserve: 30.00
    target: 9.11
    total_claim: 39.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 9.11
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-09-01":
    operating_reserve: 30.00
    target: 9.11
    total_claim: 39.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 9.11
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-09-02":
    operating_reserve: 30.00
    target: 9.11
    total_claim: 39.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 9.11
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-09-03":
    operating_reserve: 30.00
    target: 9.11
    total_claim: 39.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 9.11
    calendar_event_id: null
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-09-04":
    operating_reserve: 30.00
    target: 5.11
    total_claim: 35.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 5.11
    calendar_event_id: null
    contributions:
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-09-05":
    operating_reserve: 30.00
    target: 5.10
    total_claim: 35.10
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 5.10
    calendar_event_id: null
    contributions:
      - {line_id: liquidibee-4, amount: 4.62, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
  "2026-09-06":
    operating_reserve: 30.00
    target: 0.48
    total_claim: 30.48
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 0.48
    calendar_event_id: null
    contributions:
      - {line_id: wispr-flow, amount: 0.48, funded: 0, status: pending}
goals:                               # a goal is a bill Lemar owes himself: it needs a
                                     # target_date to enter the queue (locked 2026-08-10)
  - {id: own-car-running, name: "Get the car running", pocket: set-aside,
     target: 2800, saved: 0, target_date: null,
     note: "UNRESOLVED — target_date needed. ≈ $2,000 repairs + $1,000 taxes/tags/tires
            − $200 tires paid 7/25; car payment $500 also paid 7/25 (both pending Lemar
            confirming they landed); water-pump overlap unreconciled. Until a target
            date lands this generates no installments and stays out of the queue."}
  - {id: savings, name: "Savings", pocket: set-aside, target: null, saved: 0,
     target_date: null,
     note: "UNRESOLVED — target and target_date both needed. The retired model's '30% of
            income' framing died with the waterfall on 2026-08-10; under due-date order
            savings is funded by naming an amount and a date like anything else."}
open_questions:
  # -- the new #1 class of defect: undated queue lines are invisible --
  - "UNDATED (invisible to the queue — no event, no ramp, will never ring): student loans $500/mo · mom's $200/mo · Tidal $14.92/mo · Cuzzie's phone + Workspace ~$550/mo · Cash App payback $187.22 · gym debt $75 · water pump $184.79 · T-Mobile payment 2 (amount also unknown). Eight lines, ~$1,262/mo + $447 one-time, all silently outside the system until each gets a date."
  - "Car goal: what date do you want the car running by? Without it the goal generates nothing."
  - "Savings goal: how much, by when? Both fields are null."
  - "Cuzzie's phone + Workspace $550/mo is Lemar's estimate — actual total unconfirmed, and it is the largest line in the ledger."
  - "Confirm the 7/25 $1,000 allocation landed: $500 car payment, $200 tires, $50 mom"
  - "T-Mobile: confirm payment 1 ($265, was due 8/3) went through; payment 2 amount/date still needed"
  - "Water pump $184.79: inside or on top of the car goal's $2,000 repairs figure?"
  - "Comedy tickets $50.28 were called 'low priority' 8/9 — due-date order has no low tier. Park it or leave it queued on 8/12?"
  - "Claude card declines on the 4th three months running — payment method update is Lemar's own action with Anthropic"
  - "No balance has been reported for either pocket since the Era connector was retired 2026-08-10 — say 'Spending has $X' / 'Set-Aside has $X' whenever convenient; both currently render 'not reported'"
  - "Station travel $50/wk: Lemar started a weekend job at The Station 8/9 — pay rate not yet known, he'll report it in #personal-finance"
  - "Where should the maintenance bucket live? The 2026-08-10 account correction left it in Set-Aside, which is now SoFi Checking (the bill-paying account). SoFi Savings is free and is the obvious home, but Lemar has not said so — not moved."
  - "Gas/maintenance $30/day reserve is a rough cap Lemar named, not a measured figure — refine it once a few weeks of actual fill-ups are reported (it is now the largest single line in the ledger at ~$900/mo)"
  - "Income backlog: Lemar is posting ~2 weeks of DoorDash earnings to #personal-finance (2026-08-10). Until they land, income_target_weekly $500 is a guess and the overload check can't run."
```

## History

Everything before 2026-08-05 lives in
[[2026-07-11-personal-finance-dashboard-project]] — the project note that developed the
budget from the first rough sketch through the (now retired) Option 3 allocation
decision, the six-pocket mapping, and the calendar reminders. That note is closed; this
ledger carries the live state forward.

## Update 2026-08-10 (Era Context retired — every figure is now reported)

Lemar: "I think we should pull ERA out of the situation because it keeps disconnecting. I
was just thinking maybe reporting might be good for this."

**Era Context is out of the money system entirely.** It was the only component that
fetched rather than received, and it was carrying very little: earnings, cash, gas spend,
bills, payments, and plan terms were already reported by Lemar. Era supplied account
balances and a spending-by-category view, and it did both badly — the connector dropped
repeatedly, its last balance was **2026-07-11, a month stale**, and its 2-account plan
tier covered SoFi Checking plus SoFi Savings, the latter now parked. After the 2026-08-10
account correction it could not see DoorDash Crimson at all, which is where 100% of income
now lands. It was watching the wrong accounts, out of date, and unreliable.

**Balances are now reported, exactly like everything else.** Each pocket carries
`balance` + `balance_as_of`, set only when Lemar states a figure ("Spending has $240").
New skill mode 2b handles it. Three rules keep a self-reported balance honest:
- `null` renders **"not reported"** — never $0, and never inferred from the income log or
  by summing accruals. A number the system made up is worse than a blank.
- Every balance shows its age; **older than 7 days renders stale**, so a week-old figure
  can never pose as current.
- A reported balance is **never adjusted** to reconcile with what the ledger expected. If
  they disagree, both get shown and the gap gets named. The gap is information.

The stale $128.78 was deliberately NOT carried into `balance` — it came from the retired
connector, not from Lemar, so it stays in a note as history and both pockets start at
"not reported".

**Dropped, not replaced:** the dashboard's "Spending snapshot" section. It existed only to
render Era's category/cash-flow feed. With no transaction feed there is nothing to put
there, so the section is gone rather than left as a dead placeholder promising something
that will never arrive.

**Also cleaned up:** `pulse-dashboard` read Era for its money line and now reads the
ledger's `daily_targets` (today's claim, split into gas and set-aside); the Samira runbook
and anchors no longer list Era as a source.

**The honest tradeoff.** Nothing independently verifies Lemar's numbers now. That was
already true of every figure except balances, so the change is smaller than it sounds —
but it makes the staleness stamp load-bearing. A forgotten report should read as *stale*,
never as *current*, and the rules above are what enforce that.

Nothing paid, nothing contacted, no figure invented, no account disconnected by this
system — retiring the connector on Era's side is Lemar's own action if he wants it gone
there too.

## Update 2026-08-10 (account correction — which account plays which role)

Lemar corrected the account mapping: "The SoFi checking account is going to be where all
the recurring bills get paid. The account with the incoming money is gonna be the
DoorDash crimson card."

**The two roles are unchanged. Only the accounts behind them moved.**

| Role | Was | Now |
|---|---|---|
| Spending (income lands, gas + day-to-day paid from) | SoFi Checking | **DoorDash Crimson** |
| Set-Aside (daily bill number moves here, recurring bills paid from) | SoFi Savings | **SoFi Checking** |

Everything else about the model is untouched: due-date order, the daily accrual, the $30
gas reserve taking first claim, the one transfer a day. The instruction Lemar acts on each
morning is still "move today's set-aside number from Spending to Set-Aside" — it now means
DoorDash Crimson to SoFi Checking.

**Two consequences he did not specify, flagged rather than decided:**

1. **SoFi Savings is orphaned.** It was Set-Aside; now it has no role, so it is `parked`
   (never deleted). The maintenance bucket was defined as living "inside Set-Aside", which
   now resolves to SoFi Checking — the bill-paying account. That is a poor home for a
   savings balance, since it will sit mixed in with money earmarked for bills, and SoFi
   Savings is sitting free and already linked to Era. The obvious move is to point the
   bucket at SoFi Savings, but Lemar did not say that, so the bucket's `pocket` is left
   exactly as written and the question is open.

2. **Era is now watching the wrong accounts.** The plan links two: SoFi Checking and SoFi
   Savings. DoorDash Crimson, where 100% of income now lands, is not connected. So the
   account the whole system leans on hardest — the one that answers "did today's earnings
   cover today's number" — is the one it cannot see. SoFi Savings is parked and burning one
   of the two slots for nothing. Swapping Savings out for DoorDash Crimson would fix it
   inside the current plan tier. Not done: connecting an account is Lemar's own action at
   era.app, and the ledger never guesses at account plumbing.

`spending.era_account` is now `null`, recorded honestly rather than left pointing at an
account that no longer plays that role.

Nothing paid, nothing contacted, no money moved, no account connected or disconnected.

## Update 2026-08-10 (gas + maintenance — the operating reserve)

Lemar: "I also want to be able to factor in the gas. I really don't have a good number,
but I would say try to keep it around $25 to $30 max in gas/maintenance a day. If my tank
is full, I'll just put the rest of the money into a maintenance bucket."

**Modelled as an operating reserve, not a bill — and the distinction is load-bearing.**
A bill accrual moves money from Spending to Set-Aside and holds it there. Gas stays in
Spending and gets burned the same day; it never changes pockets. More importantly it is
the cost of *generating* the income, so it takes the **first claim on each day's
earnings** — fund the bills ahead of the gas and there is no next day's earnings. That is
a deliberate single-line exception to pure due-date order, made on that reasoning and not
on priority, and the skill forbids generalising it into a second tier.

`daily_allowances.gas_maintenance: {reserve: 30, soft_target: 25, bucket: maintenance}`.
Reserve is the $30 max he named; soft_target is the $25 he's aiming at.

**Every day now carries two figures, and no surface may show one without the other:**

| | today (8/10) | 8/12 | 8/16 |
|---|---|---|---|
| keep in Spending (gas) | $30.00 | $30.00 | $30.00 |
| move to Set-Aside (bills) | $136.96 | $67.29 | $26.46 |
| **total claim** | **$166.96** | **$97.29** | **$56.46** |

**The number that changed most.** The first seven days now claim **$705.02** — $495.02 of
bills plus $210 of gas — against a $500/week income target that was already a guess. Gas
alone runs **$900/month** at the $30 reserve, $750 at the $25 soft target. That is the
single largest line in the entire ledger, larger than the Cuzzie's phone estimate, and it
did not exist in the budget until today. Stated, not smoothed.

**The sweep.** When Lemar reports actual spend ("$22 on gas", "tank's full"), the
remainder sweeps into a new `maintenance` bucket (balance 0, living inside Set-Aside).
**An unreported day is assumed spent** — no sweep, no bucket credit, no nagging. Gas
genuinely does get spent, and inventing a maintenance balance he never confirmed would be
worse than missing one; the bucket only ever grows from a figure he gave. A spend above
the reserve is recorded as-is, never capped, and the overage is reported against the bill
line it reaches.

New skill sections: OPERATING RESERVE, mode 2b (report gas spend), and INCOME ALLOCATION
now funds the reserve before any bill — with an explicit callout when a day's income
doesn't even cover its own gas, which is the most important thing that can happen on a
given day.

Calendar: all seven rolling aggregate events retitled to show both figures
("Today costs $166.96 — $30 gas + $136.96 set aside").

Nothing paid, nothing contacted, no figure invented — the $30/$25 pair is Lemar's own.

## Update 2026-08-10 (daily accrual — every bill becomes its own payment plan)

Lemar's second call of the day, and it replaces the ramp added 2026-08-09: **every dated
line should spread evenly across the days until it's due, in one consistent format, so
there is a single daily number to hit.** His framing: "Claude is a hundred a month
($3.33 a day)... I want to make sure that all of these bills and expenses follow the same
format so that I can stay on track." Then Samira takes the day's DoorDash total, assigns
it against that number in due-date order, and drags any leftover into the next day.

**What changed in the mechanism.** The 8/9 RAMP only began saving 7 days before a due
date and dumped any shorter-fuse bill as a lump on day one — which is why all four
one-time bills landed as a single $170.28 spike on 8/10. The new ACCRUAL spreads every
line across its whole remaining window (`[today .. due − 1]`), so the number is smooth
and every line is treated identically. `config.accrual: daily-drip`.

**`funding_buffer_days: 0`.** Lemar's own arithmetic ($100/month = $3.33/day) funds a
bill *by* its due date, not a week early, so the buffer defaults to 0. Set it to 7 and
every window shrinks by a week and every daily figure rises ~30%. This is deliberately
NOT the same thing as the 7-day calendar popup, which is a notification and stays on
every bill event.

**Catch-up vs steady state.** The schedule below was computed from a zero start, so the
first days run hot and decay as short-fuse lines clear:

| | today (8/10) | 8/12 | 8/17 | 8/23 |
|---|---|---|---|---|
| daily number | **$136.96** | $67.29 | $26.45 | $16.83 |

Same effect per line: Claude is **$4.00/day** through this cycle (funding the full $100
in the 25 days left before Sep 4) and settles to **$3.22/day** once caught up. Both
figures get reported whenever a line is first accrued, so the opening number reads as a
transition rather than the new normal.

**The number that matters.** The first seven days (8/10–8/16) total **$495.02** — and
that is only the *dated* lines. The eight undated lines (~$1,265/mo + $447 one-time,
including Cuzzie's phone + Workspace and the student loans) accrue $0/day because they
have no date. The real daily cost of living is materially higher than $136.96 and cannot
be computed until those dates land. Stated, not estimated.

**New in the ledger:** `daily_targets` restructured to
`{target, funded, shortfall, calendar_event_id, contributions: [{line_id, amount, funded,
status}]}` and populated for 28 days (8/10 → 9/6), totalling $823.36 — reconciled
against the sum of the contributing lines to the cent. `funded` tracks what income
actually covered; `paid` still means a bill was settled. The two are never conflated.

**New in the skill:** an INCOME ALLOCATION step (pour the day's earnings into the day's
contributions in due-date order; partial funding is a first-class state), and ROLLOVER
now carries the *unfunded remainder* forward rather than a whole contribution — with a
line whose due date passes unfunded leaving the accrual entirely and surfacing as
overdue, instead of dripping forever against a date that has gone.

Nothing paid, nothing contacted, no figure or date invented.

## Update 2026-08-10 (model rebuild — due-date order, two pockets, one number)

Lemar reassessed the whole system and made four calls. This Update records them and what
each one changed. **No money moved, nothing paid, nobody contacted, no figure or date
invented.**

**1. Allocation shape: Option 3 hybrid floor + waterfall → RETIRED. Due-date order is
now locked.** The 7/24 model sorted spending into seven priority tiers, took a computed
weekly floor (~$463) off the top from tiers p1/p2/p4, then waterfalled leftovers through
p5 → p6 → p7. It never once ran on real data. Replaced with: every dated line goes in one
queue sorted by date, soonest funded first. `config.allocation: due-date-order`;
`floor_priorities` and `waterfall_order` deleted; the `priority` field removed from every
bill line (its historical values live in this Update and in the 7/11 project note).

*What this bought:* nothing to categorize, nothing to rank, no tier arguments. The four
bills that had sat with `priority: null` since 8/9 (METRC, cleaning supplies, comedy
tickets, station travel) are no longer stuck — their due dates are their position.

*What this cost, stated plainly:* the model now has no way to express "this one matters
less." The 8/9 "low priority" call on the comedy tickets has nowhere to live; it either
queues on 8/12 like everything else or it parks. Raised in `open_questions`.

**2. The undated-line problem got much worse, and that is the headline finding.** Under
the old floor, an undated monthly bill still contributed to the floor sum, so it was at
least *counted*. Under due-date order a line with no date has no position, no calendar
event, and no ramp — it is completely invisible. **Eight active lines are in that state
right now** (~$1,262/mo recurring + $447 one-time), including the two largest in the
whole ledger: Cuzzie's phone + Workspace (~$550/mo, also an unverified estimate) and
student loans ($500/mo). This is now the #1 open question and gets its own strip on the
dashboard. Nothing was dated to fix it — every one of those dates has to come from Lemar.

Introduced `track: queue | spending` to keep this honest: food ($600/mo) and
transportation are day-to-day Spending-pocket money, paid as you go, and were correctly
never going to have a due date. Marking them `spending` means they stop showing up as
defects while the eight genuinely-broken lines stand out.

**3. Six pockets → two.** Spending (SoFi Checking) and Set-Aside (SoFi Savings). The
four Option-3 pockets (Cash App checking/savings, DoorDash Crimson) are `status: parked`
— still Lemar's accounts, no longer part of the model, never deleted. The only transfer
instruction the system now produces is: *move today's set-aside number from Spending to
Set-Aside.* One move, once a day.

**4. Goals become dated lines.** A goal now needs a `target_date`; given one it generates
weekly installments that ramp and queue exactly like a payment plan. Both goals currently
have `target_date: null`, so **both generate nothing and are invisible** — same defect
class as the undated bills, listed as such. The old savings framing ("30% of income")
died with the waterfall; savings is now funded by naming an amount and a date.

**5. Business boundary drawn.** Cuzzie's / Station obligations no longer belong on the
personal reminder calendar or in `daily_targets`; they route to the **Cuzzie's (Owners)**
calendar (`c_5405960d...@group.calendar.google.com`) and to #on-button. One judgment call
recorded rather than guessed: `cuzzies-phone-workspace` STAYS in this personal ledger,
because Lemar explicitly chose on 2026-07-22 to carry it out of his own earnings — it is
business-origin money leaving a personal pocket. It carries `business_origin: true` so
the distinction is visible, and its reminder belongs on the business calendar once it
has a date.

**6. Nomas Recovery: Lemar is handling it directly.** The open question asking whether to
prepare a draft message about the delayed schedule is **closed, not deferred** — he took
it. The four weekly $125 reminders stay; no draft exists, nothing was sent, and the
system will not raise this again.

**7. Skill file repaired.** `.claude/skills/money-hub/SKILL.md` was stored base64-encoded
on disk (every other skill in the repo is plain text), so its own description surfaced as
`LS0tCm5hbWU6IG1vbmV5...` and nothing could match on it. Rewritten as plain text against
the new model, with two new guards that did not exist before:
- **OVERLOAD CHECK** — compares the coming week's set-aside total against the trailing
  4-week income average. It never shrinks or delays a line to make the number look
  achievable; it writes the true number and flags the gap. (Dormant until the income log
  has ≥7 entries.)
- **Rollover brake** — a contribution that rolls 3 days running gets named in #decisions
  instead of rolling silently forever. Three rolls means the plan is wrong, not that
  Lemar needs a fourth reminder.

**Unchanged and deliberately so:** the ramp math, the two-popup calendar convention
(7-day + day-of, locked 8/9), the daily aggregate event, capture-first discipline, and
every safety floor — never move money, never contact a creditor, never invent a number
or a date.

### Sources (this update)
- Lemar's direct answers, 2026-08-10 (this session): due-date order · goals get target
  dates · two pockets · separate business calendar · build now.
- Retired model: `## Update 2026-07-24T15:35:00-04:00` in
  `haven/vault/10-Personal/Money/2026-07-11-personal-finance-dashboard-project.md`
- Google Calendar `list_calendars` 2026-08-10 — confirmed "Cuzzie's (Owners)" exists.

## Update 2026-08-09 (bill-payment ramp + daily set-aside calendar — PART C)

Extended the money-hub skill per the staged #admin prompt: every bill/expense with a due
date now computes an even daily set-aside ramp, and the reminder calendar gets ONE
combined "set aside today" event across everything active. Applied the one-time backfill
to the four bills carrying a future `due` — `metrc-fee` ($40, due 8/14),
`cleaning-supplies` ($30, due 8/11), `comedy-show-tickets` ($50.28, due 8/12),
`station-travel` ($50, due 8/15). For all four, `end` (due − 7 days) fell before `start`,
so per the rule the FULL amount lands on day 1: all four on **2026-08-10**, one aggregate
entry, total **$170.28**, one calendar event (`kli8jm1vlal3ntffr2lqdkpmuk`).
`tmobile-split-1` was excluded (due date already passed); `tmobile-split-2`,
`cashapp-payback`, `gym-debt`, `water-pump` excluded (all `due: null`). Recurring
monthly-`day` bills were not auto-backfilled. Nothing paid, nothing contacted.

## Update 2026-08-09 (PART M sweep)

Swept #personal-finance. Four new one-time bills reported by Lemar as plain text drops —
`metrc-fee` $40 (8/14), `cleaning-supplies` $30 (8/11), `comedy-show-tickets` $50.28
(8/12), `station-travel` $50 (8/15) — added to the ledger and projected onto the reminder
calendar. Three had no obvious priority under the then-current model and were raised in
#decisions; that ambiguity was dissolved by the 2026-08-10 move to due-date order. No
earnings, cash-on-hand, or payment-plan drops this sweep.

## Update 2026-08-09 (Liquidibee/Nomas payment plan — set up, then re-spread)

Per Lemar's #decisions reply, set up the $500 good-faith payment owed to Amanda Ortiz at
Nomas Recovery LLC (collections for LIQUIDIBEE 1 LLC) as a savings plan — originally 6
daily $83.33 installments (8/10–8/15). Lemar then replied in #personal-finance that he
couldn't cover that pace and asked for four weeks, so it was reworked to **4 weekly $125
installments** (8/16, 8/23, 8/30, 9/06): the 8/10 aggregate event was updated in place
back to $170.28, the four Liquidibee-only daily events for 8/11–8/15 were cancelled, and
4 new weekly events created. Nothing paid, nothing contacted. (See the 2026-08-10 Update
above — Lemar has since taken the Nomas conversation directly.)

## Sources
- Prior project note: `haven/vault/10-Personal/Money/2026-07-11-personal-finance-dashboard-project.md` (full Slack ts provenance lives there)
- Staged prompt: #admin `C0BBLUA7JLX` ts `1786253312.218409`+`1786253312.241789`
  (`task:20260809_bill-payment-ramp-daily-calendar`)
- #decisions `C0BBXA96FFV` parent ts `1786194812.913559`, Lemar reply ts
  `1786241590.069229` (2026-08-09) — Liquidibee/Nomas payment-plan instruction
- #personal-finance `C0BGLEMH99T` thread ts `1786281440.216369`, Lemar reply ts
  `1786286215.944749` (2026-08-09) — 4-week re-spread instruction
