---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-14T14:12:00-04:00
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
  amount: 20                        # reported #personal-finance 2026-08-11 ts 1786464148
                                     # ("Cash on hand today - $20"). Backfilled 2026-08-14
                                     # PART M — a prior pass (2026-08-13) claimed this was
                                     # "already logged" but it was never actually written.
  as_of: 2026-08-11
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
  - {id: cuzzies-google-voice, name: "Cuzzie's Google Voice (reseller billing lapse)",
     amount: 38, cadence: once, due: 2026-08-18, track: queue, status: active,
     business_origin: true, calendar_event_id: e0cc8cm48q6p7j9h14h61tdp5o,
     note: "Added 2026-08-13. The cuzziesnj.com Workspace reseller relationship lapsed
            (see haven/vault/00-Inbox/2026-08-12-google-voice-subscription-cancellation.md,
            customer ID C00hppi2w) — this and cuzzies-google-workspace below are the
            direct-billing catch-up charges Lemar found to fix it. Distinct from the
            existing cuzzies-phone-workspace $550/mo estimate above, not a replacement
            for it. Business-origin, carried personally per the same 2026-07-22 call —
            accrues here, but its due-date reminder lives on the Cuzzie's (Owners)
            calendar, not the personal one, per the business boundary."}
  - {id: cuzzies-google-workspace, name: "Cuzzie's Google Workspace (direct billing setup)",
     amount: 85, cadence: once, due: 2026-08-19, track: queue, status: active,
     business_origin: true, calendar_event_id: u45glcg7992eg9q79nnb6brlco,
     note: "Added 2026-08-13. Same reseller billing lapse as cuzzies-google-voice above —
            all Workspace services for cuzziesnj.com (including lemar@cuzziesnj.com email
            itself) suspend 2026-08-20 without this. Business-origin, carried personally;
            due-date reminder lives on the Cuzzie's (Owners) calendar."}
  - {id: student-loans, name: Student loans, amount: 500, cadence: monthly, day: null,
     track: queue, status: active, note: "~$8,000 remaining; billing day unknown — undated, invisible to the queue"}
  - {id: claude, name: Claude subscription, amount: 100, cadence: monthly, day: 4,
     track: queue, status: active, calendar_event_id: 7djf895pc8is0illrr8bcrra20,
     note: "card declined on the 4th May/Jun/Jul — Lemar to update payment method"}
  - {id: wispr-flow, name: Wispr Flow, amount: 15, cadence: monthly, day: 10,
     track: queue, status: active, calendar_event_id: e7d9muku31setk1b10le3bf3ak,
     note: "2026-08-10 cycle ($15) PAID outside the system over the weekend, per
            Lemar 2026-08-13 — confirmed in the recompute session. Next cycle due
            2026-09-10 accrues normally from 2026-08-13 (recompute baseline)."}
  - {id: moms-expenses, name: "Mom's expenses", amount: 200, cadence: monthly, day: null,
     track: queue, status: parked, note: "SUPERSEDED 2026-08-13 by moms-lump-0821 and
            moms-weekly below, once Lemar gave concrete figures and dates. Parked, not
            deleted, per field rules."}
  - {id: moms-lump-0821, name: "Mom — one-time", amount: 110, cadence: once,
     due: 2026-08-21, track: queue, status: active, calendar_event_id: 99shu89b5clms6up7c7ud8hk98,
     note: "Added 2026-08-13, reported directly by Lemar."}
  - {id: moms-weekly, name: "Mom's expenses — weekly", amount: 50, cadence: weekly,
     weekday: friday, first_due: 2026-08-28, track: queue, status: active,
     calendar_event_id: vf835hks1jb44drqroo9221of0,
     note: "Added 2026-08-13: '$50 a week every Friday from then on', starting the Friday
            after the 8/21 one-time payment. `cadence: weekly` is new to this ledger's
            schema — accrues the same way a monthly bill does (spread over
            [cycle_start..due-1], chain starts the day AFTER each due date so cycles
            never gap or overlap), just on a 7-day period instead of a calendar month.
            No end date given — chains for as long as daily_targets projects forward,
            same as every other recurring line."}
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
  - {id: tmobile-split-2, name: "T-Mobile split payment 2 of 2", amount: 278, cadence: once,
     due: 2026-08-28, track: queue, status: active, calendar_event_id: vkp5r31n2du2u9ubk0o3vof7go,
     note: "Confirmed 2026-08-14 in #personal-finance: 'majority or at least half' of the
            July T-Mobile payment plan already paid outside the system; this $278 is the
            second half, due 8/28. daily_targets recompute for this new dated line
            deferred to the next dedicated recompute pass — not hand-spread here to avoid
            an arithmetic error across ~15 open days."}
  - {id: gym-debt, name: "Personal gym debt", amount: 75, cadence: once, due: null,
     track: queue, status: active, note: "undated, invisible to the queue"}
  - {id: water-pump, name: "New water pump", amount: 184.79, cadence: once, due: null,
     track: queue, status: active,
     note: "unclear if inside or on top of the car goal's repairs figure — unreconciled"}
  - {id: metrc-fee, name: METRC, amount: 40, cadence: once, due: 2026-08-21,
     track: queue, status: active, calendar_event_id: q36k3ogoblpe3i5amktigav8ig,
     note: "reported in #personal-finance 2026-08-09. Priority field retired 2026-08-10 —
            its due date is now its whole position in the queue. Due date pushed
            2026-08-13 from 8/14 to 8/21 at Lemar's request — too many bills were
            piling up on top of each other; this buys a week of breathing room. Now
            spreads over 7 days instead of landing as a same-day lump."}
  - {id: cleaning-supplies, name: "Cleaning supplies (house)", amount: 30, cadence: once,
     due: 2026-08-11, track: queue, status: paid, calendar_event_id: null,
     note: "reported in #personal-finance 2026-08-09. PAID outside the system over the
            weekend, per Lemar 2026-08-13 — confirmed in the recompute session. Due-date
            event ue8jtslgpl89qlmhdra710h13k already fired 8/11 before the payment was
            confirmed; retired here rather than cancelled retroactively. Out of the
            accrual — no daily_targets contribution from 2026-08-13 forward."}
  - {id: comedy-show-tickets, name: "Comedy show tickets", amount: 50.28, cadence: once,
     due: 2026-08-12, track: queue, status: parked, overdue: true,
     calendar_event_id: null,
     note: "reported in #personal-finance 2026-08-09. NOT paid — confirmed by Lemar
            2026-08-13, the only one of the three original past-due lines still owed at
            that point. Due date already passed as of the 2026-08-13 recompute baseline,
            so per Lemar's Option A ('roll it forward') and the ACCRUAL rule ('due on or
            before today lands fully today'), the full $50.28 was folded into 8/13's
            target, then rolled to 8/14 when the car stayed down.
            CANCELLED 2026-08-13 (same day, later): Lemar isn't going — 'not needed right
            now, too many bills are piling up' — so it's dropped from the accrual
            entirely rather than parked-but-still-owed. Its due-date event
            jfh8548cet84pcqo3o697fkbq8 already fired 8/12; cleared, not cancelled
            retroactively. Parked per field rules, never deleted."}
  - {id: station-travel, name: "Travel to The Station", amount: 50, cadence: once,
     due: 2026-08-15, track: queue, status: active,
     calendar_event_id: ptacguksk2rsf3md3403gljtes,
     note: "reported in #personal-finance 2026-08-09. Ramped: full $50 on 2026-08-10.
            Lemar 8/9: likely becoming a recurring weekly expense (new weekend job at
            The Station) — rate TBD, he'll post it in #personal-finance."}
  - {id: tow-truck-repay, name: "Tow truck advance repayment", amount: 500, cadence: once,
     due: 2026-09-15, track: queue, status: active, calendar_event_id: 160350dborpf6c2cllcmbkr07o,
     note: "Added 2026-08-13, funding source corrected 2026-08-14. Lemar borrowed $500
            from a friend to cover the tow truck when the car broke down; this repays
            that friend (not the car-purchase fund, as first recorded — corrected per
            Lemar's 2026-08-14 #decisions reply, ts 1786712349.341559). CONFIRMED
            2026-08-14: this is a SEPARATE debt from mechanic-repair-repay below — one
            $500 loan for the tow, a second $500 owed to the mechanic for the repair
            itself. Car-fix status not reconfirmed since 8/13."}
  - {id: mechanic-repair-repay, name: "Mechanic repair repayment (mom's car breakdown)",
     amount: 500, cadence: once, due: null, track: queue, status: active,
     calendar_event_id: null,
     note: "Added 2026-08-14. Confirmed via #decisions (ts 1786709976.054069 /
            1786712349.341559): the mechanic did the repair for free up front; Lemar
            will pay him back $500 'down the road once my expenses stabilize a little
            bit more' — no date given, explicitly open-ended. Separate debt from
            tow-truck-repay (the $500 friend loan for the tow itself) — same breakdown
            episode, two distinct $500 obligations. UNDATED — invisible to the queue
            (no event, no ramp) until Lemar names a date; see open_questions."}
  - {id: moms-car-oil-change, name: "Mom's car — oil change", amount: 100, cadence: once,
     due: 2026-08-23, track: queue, status: active, calendar_event_id: 1ia5n73c169uckbr0o8s5bakbk,
     note: "Pushed back 7 days 2026-08-14 per Lemar (#personal-finance: car wasn't driven
            for a few days, so lighten the load on the next few days) — was 8/16, now
            8/23. Calendar event moved to match. daily_targets recompute deferred to the
            next dedicated recompute pass.
            Reported 2026-08-09 in #personal-finance ('about $100, by end of next week'),
            confirmed 2026-08-11 in a #decisions thread reply: 'Oil Change - $100 by
            8/16'. Personal — mom's car, not a Cuzzie's/Station cost. Backfilled
            2026-08-14 PART M: the 2026-08-11 PART M pass raised this as an open question
            in #decisions and Lemar answered it the same day, but the answer sat
            unprocessed — a later pass (2026-08-13) incorrectly reported 'no new drops'
            without checking the thread reply. Now added, accrued, and on the calendar."}
  - {id: car-repair-payment, name: "Car repair payment", amount: 600, cadence: once,
     due: 2026-09-30, track: queue, status: active, calendar_event_id: ef8fdfuovosp9imro92oj5ifn0,
     note: "Added 2026-08-13. Lemar said 'Sept 31st', which doesn't exist (September has
            30 days) — interpreted as 2026-09-30, the last day of the month. FLAG if a
            different date was meant (e.g. Oct 1). Overlaps conceptually with the
            'own-car-running' goal's ≈$2,000 repairs estimate below, but Lemar named it
            as a separate near-term dated target rather than folding it into that
            undated goal, so it's tracked here as its own line — worth reconciling once
            the car goal gets a target_date."}
  - {id: am-botte-mechanical-past-due, name: "Am Botte Mechanical — past due balance",
     amount: 431.83, cadence: once, due: 2026-10-31, track: queue, status: active,
     calendar_event_id: pdvbut91vu3uuvrb8t3p1m8bu8,
     note: "Reported 2026-08-14 in #decisions (ts 1786727804.674749): 'log the Am Botte
            mechanical Past Due Balance ($431.83) to the cal and make a payment plan
            spread evenly from tomorrow to October 31st.' Interpreted as a single dated
            bill (due 2026-10-31) rather than a fixed-installment plan — the ACCRUAL
            engine already spreads any dated line evenly, cent-exact, across every day
            between now and its due date, which is exactly 'spread evenly' — so no
            separate installment schedule was invented. FLAG if Lemar actually wanted
            fixed weekly/monthly installments with their own individual due-date events
            instead. daily_targets recompute for this new line deferred to the next
            dedicated recompute pass (window runs ~78 days to 10/30, same reasoning as
            tmobile-split-2/moms-car-oil-change above — not hand-spread here to avoid an
            arithmetic error across that many open days)."}
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
daily_targets:                       # Revised 2026-08-13 (fourth revision, same
                                     # day): car part didn't come in, 8/14's target
                                     # pushed to 8/15 (possibly Saturday, not
                                     # confirmed). See Update 2026-08-13 (FOURTH
                                     # REVISION) below. 8/10-8/14 entries are closed
                                     # history, never rewritten -- see each day's
                                     # `resolution` key.
  "2026-08-10":
    operating_reserve: 30.00
    target: 136.96
    total_claim: 166.96
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 136.96
    calendar_event_id: kli8jm1vlal3ntffr2lqdkpmuk
    resolution: "CLOSED 2026-08-13 — this day already fired with nothing funded (income
                 log was empty). wispr-flow and cleaning-supplies were paid outside the
                 system that weekend (flipped to paid below); every other contribution's
                 dollar obligation is superseded by the fresh 2026-08-13 recompute, not
                 added a second time — see Update 2026-08-13 (RECOMPUTE)."
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: rolled}
      - {line_id: cleaning-supplies, amount: 30.00, funded: 0, status: paid}
      - {line_id: comedy-show-tickets, amount: 25.14, funded: 0, status: rolled}
      - {line_id: liquidibee-1, amount: 20.84, funded: 0, status: rolled}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: rolled}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: rolled}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: rolled}
      - {line_id: metrc-fee, amount: 10.00, funded: 0, status: rolled}
      - {line_id: patreon, amount: 1.48, funded: 0, status: rolled}
      - {line_id: station-travel, amount: 10.00, funded: 0, status: rolled}
      - {line_id: wispr-flow, amount: 15.00, funded: 0, status: paid}
  "2026-08-11":
    operating_reserve: 30.00
    target: 92.44
    total_claim: 122.44
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 92.44
    calendar_event_id: vj19k5hjaq1krci59o1flcbj78
    resolution: "CLOSED 2026-08-13 — already fired with nothing funded. Superseded by the
                 fresh 2026-08-13 recompute, not added a second time — see Update
                 2026-08-13 (RECOMPUTE)."
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: rolled}
      - {line_id: comedy-show-tickets, amount: 25.14, funded: 0, status: rolled}
      - {line_id: liquidibee-1, amount: 20.84, funded: 0, status: rolled}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: rolled}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: rolled}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: rolled}
      - {line_id: metrc-fee, amount: 10.00, funded: 0, status: rolled}
      - {line_id: patreon, amount: 1.47, funded: 0, status: rolled}
      - {line_id: station-travel, amount: 10.00, funded: 0, status: rolled}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: rolled}
  "2026-08-12":
    operating_reserve: 30.00
    target: 67.29
    total_claim: 97.29
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 67.29
    calendar_event_id: hknnvpq91j5192c4ljvdskf9s4
    resolution: "CLOSED 2026-08-13 — already fired with nothing funded. comedy-show-tickets
                 became due today and was NOT paid (Lemar confirmed 2026-08-13); it is
                 folded whole into the 2026-08-13 recompute rather than continuing to
                 drip. Every other contribution is superseded by the fresh recompute, not
                 added a second time — see Update 2026-08-13 (RECOMPUTE)."
    contributions:
      - {line_id: claude, amount: 4.00, funded: 0, status: rolled}
      - {line_id: liquidibee-1, amount: 20.83, funded: 0, status: rolled}
      - {line_id: liquidibee-2, amount: 9.62, funded: 0, status: rolled}
      - {line_id: liquidibee-3, amount: 6.25, funded: 0, status: rolled}
      - {line_id: liquidibee-4, amount: 4.63, funded: 0, status: rolled}
      - {line_id: metrc-fee, amount: 10.00, funded: 0, status: rolled}
      - {line_id: patreon, amount: 1.47, funded: 0, status: rolled}
      - {line_id: station-travel, amount: 10.00, funded: 0, status: rolled}
      - {line_id: wispr-flow, amount: 0.49, funded: 0, status: rolled}
  "2026-08-13":
    operating_reserve: 30.00
    target: 216.56
    total_claim: 246.56
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 216.56
    calendar_event_id: jho94o6sql4qjt6fdgjl0ej2oc
    resolution: "CLOSED same day, 2026-08-13 — Lemar proactively pushed today's target to
                 tomorrow: the car is down and he can't earn without it, so nothing could
                 be funded today regardless of the schedule. This is the same rollover
                 mechanic as any other day's shortfall, just invoked directly by Lemar
                 instead of waiting for the automatic end-of-day scan. Every line below is
                 superseded by the fresh 2026-08-14 recompute, not added a second time —
                 see Update 2026-08-13 (SECOND REVISION). Contingent on the car actually
                 being back tomorrow; if not, this may need pushing again."
    contributions:
      - {line_id: car-repair-payment, amount: 12.50, funded: 0, status: rolled}
      - {line_id: claude, amount: 4.55, funded: 0, status: rolled}
      - {line_id: comedy-show-tickets, amount: 50.28, funded: 0, status: rolled}
      - {line_id: liquidibee-1, amount: 41.67, funded: 0, status: rolled}
      - {line_id: liquidibee-2, amount: 12.50, funded: 0, status: rolled}
      - {line_id: liquidibee-3, amount: 7.36, funded: 0, status: rolled}
      - {line_id: liquidibee-4, amount: 5.21, funded: 0, status: rolled}
      - {line_id: metrc-fee, amount: 40.00, funded: 0, status: rolled}
      - {line_id: patreon, amount: 1.79, funded: 0, status: rolled}
      - {line_id: station-travel, amount: 25.00, funded: 0, status: rolled}
      - {line_id: tow-truck-repay, amount: 15.16, funded: 0, status: rolled}
      - {line_id: wispr-flow, amount: 0.54, funded: 0, status: rolled}
  "2026-08-14":
    operating_reserve: 30.00
    target: 200.33
    total_claim: 230.33
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 200.33
    calendar_event_id: d8ed3o469dh4r5j0c2qo73m6cs
    resolution: "CLOSED same day, 2026-08-13 → 8/14 — the part for the car repair didn't
                 come in, so it's still down. Lemar proactively pushed 8/14's target to
                 8/15 (same move as 8/13 → 8/14): possibly running again by Saturday,
                 not confirmed. Every line below is superseded by the fresh 2026-08-15
                 recompute, not added a second time — see Update 2026-08-13 (FOURTH
                 REVISION). If Saturday doesn't pan out either, this may need pushing
                 again."
    contributions:
      - {line_id: car-repair-payment, amount: 12.77, funded: 0, status: rolled}
      - {line_id: claude, amount: 4.77, funded: 0, status: rolled}
      - {line_id: liquidibee-1, amount: 62.50, funded: 0, status: rolled}
      - {line_id: liquidibee-2, amount: 13.89, funded: 0, status: rolled}
      - {line_id: liquidibee-3, amount: 7.82, funded: 0, status: rolled}
      - {line_id: liquidibee-4, amount: 5.44, funded: 0, status: rolled}
      - {line_id: metrc-fee, amount: 5.72, funded: 0, status: rolled}
      - {line_id: moms-lump-0821, amount: 15.72, funded: 0, status: rolled}
      - {line_id: moms-weekly, amount: 3.58, funded: 0, status: rolled}
      - {line_id: patreon, amount: 1.93, funded: 0, status: rolled}
      - {line_id: station-travel, amount: 50.00, funded: 0, status: rolled}
      - {line_id: tow-truck-repay, amount: 15.63, funded: 0, status: rolled}
      - {line_id: wispr-flow, amount: 0.56, funded: 0, status: rolled}
                                     # `resolution` key.
  "2026-08-15":
    operating_reserve: 30.00
    target: 404.29
    total_claim: 434.29
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 404.29
    calendar_event_id: k9sog0mcpmisnn4p2hicernagk
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: cuzzies-google-voice, amount: 12.67, funded: 0, status: pending}
      - {line_id: cuzzies-google-workspace, amount: 21.25, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 125.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.63, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.69, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.67, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.34, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.09, funded: 0, status: pending}
      - {line_id: station-travel, amount: 50.00, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
      - {line_id: moms-car-oil-change, amount: 100.00, funded: 0, status: pending}
  "2026-08-16":
    operating_reserve: 30.00
    target: 129.29
    total_claim: 159.29
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 129.29
    calendar_event_id: i5aqp4u51gvj79113o7ls4ajqk
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: cuzzies-google-voice, amount: 12.67, funded: 0, status: pending}
      - {line_id: cuzzies-google-workspace, amount: 21.25, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.63, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.69, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.67, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.34, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.09, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-17":
    operating_reserve: 30.00
    target: 129.27
    total_claim: 159.27
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 129.27
    calendar_event_id: 2f3r9682t2emqdu76snes086b8
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: cuzzies-google-voice, amount: 12.66, funded: 0, status: pending}
      - {line_id: cuzzies-google-workspace, amount: 21.25, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.63, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.69, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.67, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.33, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.09, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-18":
    operating_reserve: 30.00
    target: 116.61
    total_claim: 146.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 116.61
    calendar_event_id: i2k3vo0025kbt3lbseppnf690s
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: cuzzies-google-workspace, amount: 21.25, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.63, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.69, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.67, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.33, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.09, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-19":
    operating_reserve: 30.00
    target: 95.32
    total_claim: 125.32
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 95.32
    calendar_event_id: j6imqfltarucop954b1dkdvkq4
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.66, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.33, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-20":
    operating_reserve: 30.00
    target: 95.31
    total_claim: 125.31
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 95.31
    calendar_event_id: 7eg9gi4dqvae72l33nh0smr8c8
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.66, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.33, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-21":
    operating_reserve: 30.00
    target: 70.32
    total_claim: 100.32
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 70.32
    calendar_event_id: 6q6rn0gp6umdaus4vil752rn78
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-22":
    operating_reserve: 30.00
    target: 70.32
    total_claim: 100.32
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 70.32
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-23":
    operating_reserve: 30.00
    target: 54.69
    total_claim: 84.69
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 54.69
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-24":
    operating_reserve: 30.00
    target: 54.69
    total_claim: 84.69
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 54.69
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-25":
    operating_reserve: 30.00
    target: 54.69
    total_claim: 84.69
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 54.69
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-26":
    operating_reserve: 30.00
    target: 54.69
    total_claim: 84.69
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 54.69
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-27":
    operating_reserve: 30.00
    target: 52.61
    total_claim: 82.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 52.61
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-28":
    operating_reserve: 30.00
    target: 48.77
    total_claim: 78.77
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 48.77
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-29":
    operating_reserve: 30.00
    target: 57.11
    total_claim: 87.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 57.11
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-30":
    operating_reserve: 30.00
    target: 48.78
    total_claim: 78.78
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 48.78
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-31":
    operating_reserve: 30.00
    target: 48.76
    total_claim: 78.76
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 48.76
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-09-01":
    operating_reserve: 30.00
    target: 48.76
    total_claim: 78.76
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 48.76
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-09-02":
    operating_reserve: 30.00
    target: 48.75
    total_claim: 78.75
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 48.75
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-03":
    operating_reserve: 30.00
    target: 48.75
    total_claim: 78.75
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 48.75
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-04":
    operating_reserve: 30.00
    target: 35.42
    total_claim: 65.42
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 35.42
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-05":
    operating_reserve: 30.00
    target: 43.76
    total_claim: 73.76
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 43.76
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-06":
    operating_reserve: 30.00
    target: 38.08
    total_claim: 68.08
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 38.08
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-07":
    operating_reserve: 30.00
    target: 38.07
    total_claim: 68.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 38.07
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-08":
    operating_reserve: 30.00
    target: 38.07
    total_claim: 68.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 38.07
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-09":
    operating_reserve: 30.00
    target: 38.07
    total_claim: 68.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 38.07
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-10":
    operating_reserve: 30.00
    target: 37.50
    total_claim: 67.50
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 37.50
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
  "2026-09-11":
    operating_reserve: 30.00
    target: 29.17
    total_claim: 59.17
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 29.17
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
  "2026-09-12":
    operating_reserve: 30.00
    target: 37.50
    total_claim: 67.50
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 37.50
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.12, funded: 0, status: pending}
  "2026-09-13":
    operating_reserve: 30.00
    target: 37.50
    total_claim: 67.50
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 37.50
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.12, funded: 0, status: pending}
  "2026-09-14":
    operating_reserve: 30.00
    target: 37.49
    total_claim: 67.49
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 37.49
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.12, funded: 0, status: pending}
  "2026-09-15":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
  "2026-09-16":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
  "2026-09-17":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
  "2026-09-18":
    operating_reserve: 30.00
    target: 13.04
    total_claim: 43.04
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 13.04
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
  "2026-09-19":
    operating_reserve: 30.00
    target: 21.38
    total_claim: 51.38
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.38
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
  "2026-09-20":
    operating_reserve: 30.00
    target: 21.38
    total_claim: 51.38
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.38
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
  "2026-09-21":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
  "2026-09-22":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
  "2026-09-23":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
  "2026-09-24":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
  "2026-09-25":
    operating_reserve: 30.00
    target: 13.04
    total_claim: 43.04
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 13.04
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
  "2026-09-26":
    operating_reserve: 30.00
    target: 21.38
    total_claim: 51.38
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.38
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
  "2026-09-27":
    operating_reserve: 30.00
    target: 21.38
    total_claim: 51.38
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.38
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
  "2026-09-28":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
  "2026-09-29":
    operating_reserve: 30.00
    target: 21.37
    total_claim: 51.37
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 21.37
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
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
  - "UNDATED (invisible to the queue — no event, no ramp, will never ring): student loans $500/mo · Tidal $14.92/mo · Cuzzie's phone + Workspace ~$550/mo · Cash App payback $187.22 · gym debt $75 · water pump $184.79 · T-Mobile payment 2 (amount also unknown) · mechanic repair repayment $500 (added 2026-08-14, see mechanic-repair-repay — 'down the road once expenses stabilize', no date given). Eight lines, ~$1,065/mo + $947 one-time, all silently outside the system until each gets a date. (Mom's expenses is no longer on this list — dated 2026-08-13, see moms-lump-0821 and moms-weekly.)"
  - "Car goal: what date do you want the car running by? Without it the goal generates nothing."
  - "Savings goal: how much, by when? Both fields are null."
  - "Cuzzie's phone + Workspace $550/mo is Lemar's estimate — actual total unconfirmed, and it is the largest line in the ledger."
  - "Confirm the 7/25 $1,000 allocation landed: $500 car payment, $200 tires, $50 mom"
  - "T-Mobile: confirm payment 1 ($265, was due 8/3) went through; payment 2 amount/date still needed"
  - "Water pump $184.79: inside or on top of the car goal's $2,000 repairs figure?"
  - "RESOLVED 2026-08-13 (recompute session, updated same day): comedy tickets $50.28 confirmed unpaid and briefly folded into the accrual, then CANCELLED later the same day — Lemar isn't going, too many bills were piling up. Parked, out of the queue entirely, not owed. See Update 2026-08-13 (THIRD REVISION)."
  - "Claude card declines on the 4th three months running — payment method update is Lemar's own action with Anthropic"
  - "No balance has been reported for either pocket since the Era connector was retired 2026-08-10 — say 'Spending has $X' / 'Set-Aside has $X' whenever convenient; both currently render 'not reported'"
  - "Station travel $50/wk: Lemar started a weekend job at The Station 8/9 — pay rate not yet known, he'll report it in #personal-finance"
  - "Where should the maintenance bucket live? The 2026-08-10 account correction left it in Set-Aside, which is now SoFi Checking (the bill-paying account). SoFi Savings is free and is the obvious home, but Lemar has not said so — not moved."
  - "Gas/maintenance $30/day reserve is a rough cap Lemar named, not a measured figure — refine it once a few weeks of actual fill-ups are reported (it is now the largest single line in the ledger at ~$900/mo)"
  - "Income backlog: Lemar is posting ~2 weeks of DoorDash earnings to #personal-finance (2026-08-10). Until they land, income_target_weekly $500 is a guess and the overload check can't run."
  - "RESOLVED 2026-08-14: Lemar confirmed (#decisions ts 1786712349.341559) these ARE two separate $500 obligations from the same breakdown — a friend-funded tow ($500, tow-truck-repay, due 9/15) and a mechanic repair he'll repay 'down the road' with no date yet (mechanic-repair-repay, undated). Both now carry their own line; see the UNDATED bullet above for the second."
  - "NEW 2026-08-14: Lemar confirmed his new Station weekend job (#decisions ts 1786710731.810909) — $12/hour, ~23 hrs/week, security desk. No paycheck/earnings figure reported yet under this job; log actual pay via #personal-finance once it starts landing, same as DoorDash. Not the same thing as the 'Station travel $50/wk' expense line above (that's his travel cost, not this income)."
```

## Update 2026-08-14 (PART M — T-Mobile amount/date + oil-change reschedule)

Two new drops in #personal-finance this pass:
- **T-Mobile split payment 2 of 2** — Lemar confirmed the amount/date that were
  previously `null`: $278, due 2026-08-28 (the second half of the July bill's
  payment plan; the first half is "already paid, majority or at least half").
  Calendar event created (`vkp5r31n2du2u9ubk0o3vof7go`, both 7-day + day-of
  popups).
- **Mom's car oil change** — pushed back 7 days at Lemar's own request ("since
  I didn't drive the car for a few days... lighten the load on the next few
  days"): due moved from 2026-08-16 to 2026-08-23. Calendar event
  `1ia5n73c169uckbr0o8s5bakbk` moved to match (caught a tool side-effect along
  the way — the first update call silently converted it to an all-day event;
  re-issued with an explicit timezone and confirmed it's a timed 9am event
  again before moving on).

Both lines updated in the yaml above. **daily_targets recompute NOT run this
pass** for either change — spreading two new dated lines across ~15 open days
by hand risks an arithmetic slip in a real financial number; deferring to the
next dedicated recompute pass (same doctrine as other same-day drops earlier
this week) rather than guess at the day-by-day split. Dashboard re-render also
deferred to PART P.

## Update 2026-08-14 (PART M — mom's-car $500 debt split, resolved)

Lemar answered the open question directly in #decisions (ts 1786712349.341559,
replying to the card posted by the earlier interrupted pass this morning):
"I borrowed 500 from my friend to get the tow truck. I have to pay that back
separately. The repair cost is 500 and the mechanic did it for free so I'm going
to pay him back 500 down the road once my expenses stabilize a little bit more."

Confirmed: **two separate $500 debts**, not one described two ways.
- `tow-truck-repay` ($500, due 2026-09-15) — funding source corrected to "a friend"
  (was mis-recorded as "the car-purchase fund" on 2026-08-13). Amount/date/calendar
  event unchanged.
- `mechanic-repair-repay` ($500, **no date** — "down the road") — new line, `track:
  queue`, `status: active`, no calendar event (nothing to ring against). Added to
  the UNDATED open-questions bullet; total undated one-time exposure moves from
  $447 to $947.

Nothing paid, nothing invented — the no-date debt stays invisible-by-design until
Lemar names one, per the skill's own rule. Also logged Lemar's new Station
weekend-job pay rate ($12/hr, ~23 hrs/week, security desk — #decisions ts
1786710731.810909) as a forward-looking open question; no earnings yet reported
under it, so no income-log entry created. Replied "Done ✅" in both #decisions
threads. Dashboard re-render deferred to PART P later this pass.

## Update 2026-08-14 (PART M — backfilled two stranded confirmations)

Samira's hourly PART M sweep of #personal-finance (72h window, back to 2026-08-11).
The channel itself held no NEW drops this pass — the only post in-window was "Cash on
hand today - $20" (2026-08-11), which a later automated pass (2026-08-13, ts
1786638103) claimed was "already logged." **It wasn't** — `cash_on_hand` was still
`null`/`null` going into this pass. Fixed now: `cash_on_hand.amount: 20`,
`as_of: 2026-08-11`.

While tracing that gap, found a second one: on 2026-08-11 Samira raised a #decisions
card asking Lemar to confirm two hedged mom's-car figures (oil change ~$100, breakdown
repair ~$500). Lemar replied the same day with real numbers — "Oil Change - $100 by
8/16" and "Repair (Friend Loaned me money to pay for it now) - $500 by 9/15" — but no
subsequent pass ever read that thread reply, so nothing was written.

**Oil change — added as a new bill, `moms-car-oil-change`, $100 due 2026-08-16.**
Personal (mom's car maintenance Lemar is covering), not Cuzzie's/Station. 8/14 is
already closed history (Lemar pushed it to 8/15 on 2026-08-13, car still down), so this
accrues onto the earliest open day: the full $100 lands on **2026-08-15** (window is
just the one day, `[8/15..8/15]`, due date 8/16). 8/15's target moves from $304.29 to
**$404.29** ($30 gas + $404.29 set-aside = $434.29 total claim). Its own due-date
reminder event was created on 8/16 (both popups); 8/15's aggregate "set aside today"
event was updated in place with the new total and the added line.

**Repair ($500 by 9/15) — NOT added as a new line.** Amount and due date are identical
to the existing `tow-truck-repay` line (added 2026-08-13, described then as "borrowed
from the car-purchase fund" rather than "a friend"), both tracing back to the same car
breakdown. Treated as the same $500 obligation rather than a sibling line, to avoid
silently doubling Lemar's daily number on a guess. Flagged in `open_questions` for
Lemar to confirm it's one debt, not two.

Nothing paid, nothing contacted. No earnings drop this pass (income log still under 7
entries — OVERLOAD CHECK stays dormant). Not confirmed to be the day's last scan
(≥5pm ET), so ROLLOVER was not run. Dashboard re-rendered.

## History

Everything before 2026-08-05 lives in
[[2026-07-11-personal-finance-dashboard-project]] — the project note that developed the
budget from the first rough sketch through the (now retired) Option 3 allocation
decision, the six-pocket mapping, and the calendar reminders. That note is closed; this
ledger carries the live state forward.

## Update 2026-08-13 (FIFTH REVISION — two Cuzzie's billing-lapse bills added)

Lemar: "I need $85 by the 19th so that I can pay for the Google Workspace before it gets
suspended on the 20th. But before that earlier in the week, I gotta pay $38 for the
Google Voice."

**These are not new personal expenses — they're the fix for an already-tracked business
issue.** `haven/vault/00-Inbox/2026-08-12-google-voice-subscription-cancellation.md`
already documents that the cuzziesnj.com Workspace reseller relationship lapsed: without
direct billing set up in the Google Admin console (customer ID `C00hppi2w`), **all**
Workspace services — including `lemar@cuzziesnj.com` email itself — suspend 2026-08-20.
That note was raised as a `#decisions` card and explicitly left as "outside Samira's
authority" (a payment-method decision). Lemar's numbers here match that exact deadline.

**Confirmed rather than assumed which side of the boundary this sits on.** Asked
directly: personal ledger (matching the existing `cuzzies-phone-workspace` precedent
from 2026-07-22) or route to Cuzzie's and stay out of this ledger entirely? Lemar chose
personal — consistent with his standing call to carry Cuzzie's phone + Workspace costs
from his own earnings. Two new one-time bills, `business_origin: true`, distinct from
the existing undated $550/mo `cuzzies-phone-workspace` estimate (not a replacement for
it — these are one-time catch-up charges, that's an ongoing monthly line):
- **`cuzzies-google-voice`, $38, due 2026-08-18.** Date also asked rather than assumed —
  "earlier in the week" was ambiguous between Monday and Tuesday; Lemar picked Tuesday.
- **`cuzzies-google-workspace`, $85, due 2026-08-19.**

**Accrue in the personal ledger (contributing to `daily_targets`), but their calendar
reminders live on the Cuzzie's (Owners) calendar**, per the existing note on
`cuzzies-phone-workspace` ("its reminder... belongs on the Cuzzie's (Owners) calendar
per the business boundary") — the money comes from Lemar's own earnings, but the
service being paid for is Cuzzie's, so the reminder sits where the business context is.
Layered onto the already-computed 8/15-8/18 window rather than a full rebuild, since
these two new lines don't change any other line's schedule.

**8/15's number moves from $300.37 to $334.29.** The four affected personal aggregate
calendar events (8/15-8/18) were updated with the new totals; two new due-date reminder
events were created on the Cuzzie's (Owners) calendar.

Nothing paid, nothing contacted, no admin console login — this records what Lemar
reported and confirmed.

## Update 2026-08-13 (FOURTH REVISION — 8/14's target pushed to 8/15; car part delayed)

**The car part didn't come in today.** Lemar: "looks like the car part didn't come in
today so the car possibly won't be functional until Saturday." Not confirmed — just the
best information he has right now.

Asked directly rather than assumed: should 8/14's target ($230.33) push to 8/15 now, or
wait until Friday actually passes to decide? Lemar chose to push it now.

**Same mechanism as the 8/13 → 8/14 push** (Update below): 8/14 closes as history —
target/total_claim preserved, every contribution flipped to `status: rolled`, nothing
rewritten — and every dated line's window is rebuilt fresh with `today = 2026-08-15`.
Station travel (due 8/15) is the one line whose due date lands exactly on the new
baseline, so per the accrual rule it goes from a $50.00/day-shared figure to landing in
full today. Liquidibee 1 of 4 (due 8/16) now has only one day left in its window, so its
full $125 lands on 8/15 too — the same "fewer days, higher rate" effect the original
recompute produced, just compounding a second time.

**Today's number (now 8/15) is $300.37** — $30.00 gas + $270.37 set-aside. This is the
second consecutive day pushed for the same reason; the ledger already anticipated this
exact scenario ("if not, this may need pushing again," 8/13 → 8/14 resolution note). If
Saturday doesn't pan out either, the pattern repeats a third time. The rolling calendar
events (8/15-8/21) were updated; 8/14's event now reads $0/rolled.

Nothing paid, nothing contacted — this records what Lemar reported and asked for.

## Update 2026-08-13 (THIRD REVISION — comedy tickets cancelled, METRC pushed a week)

**Too many bills were piling up on the near-term days**, so Lemar cut one and deferred
another rather than let the daily number keep climbing.

- **Comedy show tickets ($50.28) — cancelled.** He's not going. This is different from
  the earlier "past due, unpaid" state (Update below): that was still an open debt
  waiting on a payment decision; this is Lemar deciding there's no debt at all. Flipped
  to `status: parked` per field rules (never deleted), `overdue: true` and the historical
  `rolled` contributions on 8/10-8/13 stay exactly as they were — they correctly recorded
  what the plan looked like at the time, and a decision made today doesn't rewrite that.
  Simply drops out of every day from 8/14 forward.
- **METRC ($40) — due date pushed one week, 8/14 to 8/21.** Lemar's explicit ask, scoped
  to METRC alone (confirmed — not the whole schedule). It no longer lands as a same-day
  lump; it spreads over the new 7-day window like everything else.

**Today's number drops from $314.89 to $230.33** ($30.00 gas + $200.33 set-aside) — the
two changes together remove $84.56 from 8/14 alone (comedy's full $50.28 plus $34.28 of
METRC's former lump, since $5.72/day of METRC's $40 still lands on 8/14 under its new
spread). The rolling aggregate calendar events (8/14-8/20) were updated with the new
figures; METRC's own due-date reminder event was moved to 8/21 rather than duplicated.
Dashboard re-rendered again.

Nothing paid, nothing contacted — this records what Lemar decided.

## Update 2026-08-13 (SECOND REVISION — 8/13's target pushed to 8/14; mom's payments added)

**The car is still down as of this revision** — Lemar isn't certain it'll be fixed by
tomorrow (8/14) either, just hopeful. Given that, he asked to push today's (8/13) target
to tomorrow rather than let it sit there unfundable: he can't DoorDash without the car,
so nothing was going to get earned today regardless of what the schedule said.

**Mechanically, this is the ROLLOVER rule invoked directly by Lemar instead of waiting
for the automatic end-of-day scan.** 8/13 closes as history exactly like 8/10-8/12 did
in the recompute above — target/total_claim preserved as the historical record, every
contribution flipped to `status: rolled`, nothing rewritten. Rather than literally
duplicating each of 8/13's line items onto 8/14 (which risks double-listing a line that
already has its own natural 8/14 drip), every dated line's window was rebuilt fresh with
`today = 2026-08-14` — the same technique as the original recompute, scaled down from
three days to one. Comedy tickets and METRC (due 8/12 and 8/14 respectively, both on or
before the new baseline) land in full on 8/14 per the accrual rule itself.

**Two new obligations, both reported by Lemar in this same conversation:**
- **$110 to his mom by 2026-08-21** — new one-time bill `moms-lump-0821`.
- **$50/week to his mom, every Friday starting 2026-08-28** (the Friday after the above)
  — new bill `moms-weekly`, `cadence: weekly`. This is a new cadence type for this
  ledger; it accrues the same way a monthly bill does (spread over
  `[cycle_start..due-1]`, next cycle starts the day AFTER each due date so cycles never
  gap or overlap — same rule that already governs Wispr Flow's monthly chain), just on
  a 7-day period. The old undated `moms-expenses` ($200/mo estimate) is superseded and
  parked — this is Lemar giving it real structure, not a separate obligation on top.

**Today's effective number (now 8/14) is $314.89** — $30.00 gas + $284.89 set-aside,
covering everything that would have been due today (8/13, rolled) plus 8/14's own
lines plus both new mom's payments starting to accrue. The 7-day rolling calendar
events were updated a third time; 8/13's own event now reads $0/rolled rather than being
deleted, since the day itself still exists on the calendar. Two new due-date reminder
events were created for the mom's lines (`moms-lump-0821` due 8/21, and the first
`moms-weekly` cycle due 8/28). Dashboard re-rendered again.

Nothing paid, nothing contacted — this records what Lemar reported and asked for.

## Update 2026-08-13 (REVISION — two new car obligations added same day)

**The car is currently down.** Lemar is hoping it's fixed and back on the road tomorrow
(8/14) but isn't certain yet — logged for context, no ledger field tracks car status
directly.

Two new one-time bills, both added to the queue and accrued from today like everything
else:
- **`tow-truck-repay`, $500, due 2026-09-15.** Lemar borrowed $500 from the car-purchase
  fund to cover the tow truck; this repays that fund.
- **`car-repair-payment`, $600, due 2026-09-30.** Lemar said "Sept 31st" — September has
  30 days, so this was interpreted as the last day of the month. **Flag if a different
  date was meant** (e.g. Oct 1). This overlaps conceptually with the `own-car-running`
  goal's ≈$2,000 repairs estimate (still `target_date: null`, so not in the queue) —
  left as two separate lines rather than merged, since Lemar named this one with its own
  near-term date; worth reconciling once the goal itself gets a target date.

Both extend `daily_targets` out to **2026-09-29** (car-repair-payment's window) — 22 days
further than the 2026-09-06 endpoint the recompute below had just established. Every day
from 8/13 forward was rebuilt again to include these two new drips; the 8/10-8/12
historical entries and the recompute methodology below are unaffected.

**Today's number moves from $218.90 to $246.56** ($30.00 gas + $216.56 set-aside; the
two new lines add $15.16 + $12.50 = $27.66). The rolling 7-day calendar events (8/13-
8/19) were updated again with the new totals, and two new due-date reminder events were
created for the two bills themselves (both popups, per the calendar's standard). The
dashboard was re-rendered a second time.

Nothing paid, nothing contacted — this records what Lemar reported.

## Update 2026-08-13 (RECOMPUTE — daily_targets rebuilt against the real date)

**This closes the blocking recompute from the v4 handoff doc and Update 2026-08-10
(DATE ERROR) below.** Lemar answered both open questions in this recompute session:

1. Of the three past-due bills, he paid **Wispr Flow ($15, was due 8/10)** and
   **cleaning supplies ($30, was due 8/11)** outside the system over the weekend.
   **Comedy show tickets ($50.28, was due 8/12) were NOT paid** — still owed.
2. For the three elapsed unfunded days: **Option A — roll it forward.** The unfunded
   set-aside drags onto today rather than being pulled out and tracked separately.

**Bills block:** wispr-flow's 8/10 cycle and cleaning-supplies both flip to reflect the
payment (cleaning-supplies fully `status: paid` and retired from the queue; wispr-flow's
`status` stays `active` since it's monthly and recurs — only the paid cycle is done, the
next cycle due 9/10 continues). comedy-show-tickets stays `active`, flagged `overdue: true`.

**How Option A was actually applied — mechanically equivalent to a rollover, not a
second lump on top of one.** The naive reading of "roll the $296.69 forward" would sum
the old 8/10-8/12 targets and add them on top of a freshly recomputed 8/13. That
double-counts: the total dollars owed on every still-future line (Claude, METRC, Patreon,
Station travel, all four Liquidibee installments) hasn't changed, only the number of days
left to spread it over has shrunk by three. So each line's accrual window was rebuilt
fresh from `today = 2026-08-13` against its **true remaining balance** (nothing was ever
funded 8/10-8/12 — the income log is empty, so nothing was actually lost, only the
schedule was wrong). This produces the identical dollar result rolling forward would
have, without compounding rounding error across three mechanical rollover passes. Comedy
tickets — the one bill whose due date has now actually passed unpaid — needed no special
rollover math at all: the ACCRUAL rule already says a line "due on or before today lands
fully today," so its full $50.28 simply lands on 8/13 as a single-day contribution. The
old 8/10-8/12 `daily_targets` entries are kept as closed history (never rewritten — see
each day's new `resolution` key), not deleted or recomputed after the fact.

**The gas operating reserve was deliberately NOT rolled forward.** The doc's "$90 of gas
reserve elapsed unfunded" was flagged as a fact, not a debt to recoup — gas is a same-day
allowance for actual driving, not an accrual with a carried balance (see OPERATING
RESERVE in the skill). Each day from 8/13 forward still gets its own flat $30 reserve.
Flagging this explicitly rather than silently deciding it, per the same rule that governs
every other unknown here.

**The result: today (2026-08-13) costs $218.90 — $30.00 gas + $188.90 set-aside**,
materially below the doc's rough $460 estimate, because (a) two of the three past-due
bills are now settled and (b) a from-scratch recompute doesn't stack a rollover lump on
top of a fresh calculation of the same money. `daily_targets` rebuilt through 2026-09-06
(the last Liquidibee/Nomas installment). The rolling 7-day aggregate calendar events for
8/13-8/19 were updated/created and their ids written back (8/13-8/16 existing events
updated in place; 8/17-8/19 newly created — 8/10-8/12's events already fired and were not
retroactively cancelled). The Money Hub dashboard was re-rendered dropping the stale-date
banner (see below).

Nothing paid, nothing contacted — Wispr Flow and cleaning supplies were paid by Lemar
himself outside this system; this session only recorded that.

## Update 2026-08-10 (DATE ERROR — schedule computed against the wrong day)

**Everything dated in this ledger was computed against today = 2026-08-10. The real date
is 2026-08-13** (verified directly from the system clock: Thursday 2026-08-13 13:29 ET).
Three days of real time passed inside the session that built this.

How it happened, for the record: Era's `as_of` stamp read 2026-08-10T13:33, the newest
Slack messages in #personal-finance were 2026-08-09, the calendar events had been created
2026-08-09/10, and the first two handoff docs came back from Drive stamped 2026-08-10.
Every available signal agreed on Aug 10, so the accrual was anchored there. The third
handoff doc came back stamped 2026-08-13, which surfaced the conflict.

**What is wrong:** only the dated schedule. `daily_targets` (all 28 days), the seven
rolling calendar events, and the dashboard's date header. Consequences as of 2026-08-13:
- `2026-08-10` ($136.96), `2026-08-11` ($92.44), `2026-08-12` ($67.29) have ELAPSED
  UNFUNDED — $296.69 of set-aside, plus 3 × $30 = $90 of gas reserve.
- Their calendar events have already fired.
- Wispr Flow ($15, due 8/10), cleaning supplies ($30, 8/11) and comedy show tickets
  ($50.28, 8/12) are PAST DUE unless Lemar paid them outside the system.
- METRC ($40) is due TOMORROW with one day left to fund it, not four.

**What is NOT wrong:** every structural decision holds — due-date order, the accrual
mechanism itself, the gas operating reserve and its first claim, the two pockets and
their corrected accounts, reported balances and the three honesty rules, the overload
check, the rollover brake, the base64 skill repair, the business boundary. All five
commits stand. Only the arithmetic's starting day is off.

**Deliberately NOT auto-corrected.** Rolling all $296.69 onto today would push today's
number to roughly $460 and cascade from there; the rollover rule was written for a day
ending, not for three days vanishing at once. The alternative is to treat those three
bills as plainly overdue, lift them out of the accrual, and restart clean from 2026-08-13.
Which is right depends on whether Lemar actually paid them over the weekend, which this
system has no way to know. Raised as a blocking open question rather than guessed —
the same rule that governs every other unknown here.

Lemar's call 2026-08-13: the recompute happens in a separate chat. This Update, the
warning block on `daily_targets`, the dashboard banner, and the v4 handoff all carry the
correction so the next session cannot act on Monday's numbers by accident.

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

## Update 2026-08-14 (2) — Am Botte Mechanical past-due balance added

Per Lemar's #decisions message (ts `1786727804.674749`): "Can we log the Am Botte
mechanical Past Due Balance ($431.83) to the cal and make a payment plan spread evenly
from tomorrow to October 31st?" Added `am-botte-mechanical-past-due` as a single dated
bill, `due: 2026-10-31`, calendar event `pdvbut91vu3uuvrb8t3p1m8bu8` created with both
popups (7-day + day-of). Read "spread evenly from tomorrow to October 31st" as a
description of the standard daily-accrual behavior (every dated line spreads cent-exact
across every day between now and its due date) rather than a request for a fixed
installment schedule with its own separate events — flagged in the line's note in case
Lemar actually wants discrete installments instead. `daily_targets` recompute for this
line deferred to the next dedicated recompute pass (the window runs ~78 days, matching
the same reasoning already used for `tmobile-split-2` and `moms-car-oil-change` above).
Nothing paid, nothing contacted.

## Sources
- Prior project note: `haven/vault/10-Personal/Money/2026-07-11-personal-finance-dashboard-project.md` (full Slack ts provenance lives there)
- Staged prompt: #admin `C0BBLUA7JLX` ts `1786253312.218409`+`1786253312.241789`
  (`task:20260809_bill-payment-ramp-daily-calendar`)
- #decisions `C0BBXA96FFV` parent ts `1786194812.913559`, Lemar reply ts
  `1786241590.069229` (2026-08-09) — Liquidibee/Nomas payment-plan instruction
- #personal-finance `C0BGLEMH99T` thread ts `1786281440.216369`, Lemar reply ts
  `1786286215.944749` (2026-08-09) — 4-week re-spread instruction
