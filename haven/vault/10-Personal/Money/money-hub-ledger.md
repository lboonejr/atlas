---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-27T12:00:00-04:00
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
- `non_negotiable: true` (optional, added 2026-08-15) — Lemar's explicit flag on a bill,
  plan, or goal line meaning REBALANCE (see SKILL.md) may never propose stretching,
  re-tiering, or otherwise touching it, no matter how tight a week gets. Absent =
  negotiable by default. Only Lemar sets or clears this flag; never infer it from a
  line looking important.
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
     balance: 70, balance_as_of: 2026-08-26, status: active,
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
            due-date reminder lives on the Cuzzie's (Owners) calendar.
            PAYMENT ATTEMPTED 2026-08-17 per Lemar in #personal-finance (ts
            1786999318.129009): 'I paid for google workspace but the transaction didn't
            process yet.' CONFIRMED NOT CLEARED 2026-08-18 (#decisions ts 1787001107.337499,
            reply 1787009888.775939): 'The charge did not clear.' Stays `status: active`/
            unpaid, still accruing toward the 8/19 due date and still suspension-risk if
            not resolved by 8/20 — Lemar carries the actual re-attempt himself, Samira
            cannot retry billing."}
  - {id: student-loans, name: Student loans, amount: 500, cadence: monthly, day: 16,
     track: queue, status: active, calendar_event_id: eo3u9f3dm97hc987tvvkcblaig,
     note: "~$8,000 remaining. DATED 2026-08-15 per Lemar in #personal-finance
            (ts 1786754410.308129): 'The student loans get paid on the 16th of every
            month (this month was taken care of).' Since August's 8/16 due date is
            already funded/handled outside the system, the catch-up window skips it —
            accrual starts fresh toward the NEXT cycle, due 2026-09-16, rather than
            back-loading a catch-up onto a date that's already covered. Steady-state
            cycle (Sep16→Oct16, 30 days) will be ~$16.67/day once caught up."}
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
     due: 2026-11-30, track: queue, status: active, calendar_event_id: 8dh069la1a8jkorijs38fbo33s,
     note: "DATED 2026-08-15 per Lemar in #personal-finance (ts 1786754410.308129):
            'The cash app payback will just be for the end of November but let's just
            make sure that we account for the accruing interest. I think it's like 2%
            each day or something like that.' Accruing here against the STATED $187.22
            only — Lemar's own words flag the rate as uncertain ('I think it's like'),
            so no compounding was invented on top of it; see open_questions for the ask
            to confirm the actual balance or rate closer to the due date."}
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
     track: queue, status: paid, calendar_event_id: null,
     note: "PAID 2026-08-15 per Lemar in #personal-finance (ts 1786754410.308129):
            'The personal gym debt has been paid.' Mode 7 — no calendar event existed
            to retire (was never dated) and no daily_targets contribution existed to
            clear (was undated, so it never accrued)."}
  - {id: water-pump, name: "New water pump", amount: 184.79, cadence: once,
     due: 2026-09-15, track: queue, status: active, calendar_event_id: hgt0094c7sif12li39o46bfs7g,
     note: "DATED 2026-08-15 per Lemar in #personal-finance (ts 1786754410.308129):
            'Let's have the new water pump in hand by September 15th.' Overlap with the
            car goal's ≈$2,000 repairs estimate is STILL unreconciled — see
            open_questions; dating this line doesn't resolve whether it's inside or on
            top of that figure."}
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
  - {id: station-travel, name: "Travel to The Station", amount: 80, cadence: once,
     due: 2026-08-15, track: queue, status: paid,
     calendar_event_id: null,
     note: "reported in #personal-finance 2026-08-09. Ramped: full $50 on 2026-08-10.
            RATE CORRECTED 2026-08-15 per Lemar in #personal-finance: 'Round Trip
            (Saturday & Sunday total): $80 per week' — this was the TBD rate flagged
            8/9. Amount raised 50→80 for this week's already-open occurrence (today's
            due date); future weeks tracked as the new recurring line
            station-travel-weekly below, not as repeats of this one-time id.
            PAID 2026-08-16 per Lemar in #personal-finance ('made it to The Station
            today, so the travel cost has officially been fully covered') — funded in
            full 2026-08-15 via income allocation, now confirmed settled. Reminder
            event ptacguksk2rsf3md3403gljtes cancelled/cleared."}
  - {id: station-travel-weekly, name: "Travel to The Station — weekly", amount: 80,
     cadence: weekly, weekday: saturday, first_due: 2026-08-22, track: queue,
     status: active, calendar_event_id: 7ppstt92j8m4ben3u0v8iepink,
     note: "Added 2026-08-15: recurring weekly round-trip travel cost for the new
            weekend Station security-desk job (Sat+Sun combined, $80/week total),
            confirmed rate per Lemar in #personal-finance. Starts the Saturday AFTER
            this week's one-time station-travel occurrence (2026-08-15) so the two
            never double-count. Same weekly-cadence accrual pattern as moms-weekly.
            CLARIFIED 2026-08-16 per Lemar in #personal-finance: this $80/weekend is
            train fare, not gas — he won't be driving to weekend shifts for now. No
            figure changes: this line was already tracked as its own $80 accrual
            separate from daily_allowances.gas_maintenance, so nothing double-counted
            and nothing to remove. Noted for the record only."}
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
     amount: 500, cadence: once, due: 2026-09-30, track: queue, status: active,
     calendar_event_id: 8mg783n6eujr2mk4990eub0p7s,
     note: "Added 2026-08-14. Confirmed via #decisions (ts 1786709976.054069 /
            1786712349.341559): the mechanic did the repair for free up front; Lemar
            will pay him back $500 'down the road once my expenses stabilize a little
            bit more'. Separate debt from tow-truck-repay (the $500 friend loan for the
            tow itself) — same breakdown episode, two distinct $500 obligations.
            DATED 2026-08-15 per Lemar in #personal-finance (ts 1786754410.308129):
            'The mechanic repayment, I want it to be for the end of September.'"}
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
  - {id: fantasy-football-buyin, name: "Fantasy football league buy-in", amount: 300,
     cadence: once, due: 2026-09-07, track: queue, status: active,
     calendar_event_id: hg1jv9it638bi0b74sffckq0lg,
     note: "Reported directly by Lemar in #personal-finance 2026-08-14 (ts
            1786740958.338029): '$300 buy in, due 9/7, can we put this one in the loop?'
            Personal, one-time — not recurring. ACCRUAL window [2026-08-15..2026-09-06],
            23 days ($13.05/day for the first 8 days, $13.04/day the remaining 15,
            cent-exact)."}
  - {id: dil-christmas-gift, name: "Dil's Christmas gift (custom book embosser)",
     amount: 100, cadence: once, due: 2026-11-15, track: queue, status: active,
     calendar_event_id: 1n1p68pda0pfooi3g10l8o2rd0,
     note: "Reported directly by Lemar in #personal-finance 2026-08-14 (ts
            1786741216.632109): custom book embosser as a Christmas gift for 'Dil', due
            2026-11-15. Personal, one-time. ACCRUAL window [2026-08-15..2026-11-14],
            92 days ($1.09/day for the first 64 days, $1.08/day the remaining 28,
            cent-exact)."}
  - {id: self-account-balance-repay, name: "Self-account balance repay", amount: 242,
     cadence: once, due: 2026-11-30, track: queue, pocket: set-aside, status: active,
     calendar_event_id: tivvj427c9ukh53863qkvt1bh0,
     note: "Reported directly by Lemar in #personal-finance 2026-08-14 (ts
            1786742686.895999): 'I also wanna add in $242 by the last day of
            November to repay my self-account open balance. This is a personal that
            I opened a self-account and left the balance on the card.' His own card
            balance, not Cuzzie's/Station business. Personal, one-time. ACCRUAL
            window [2026-08-15..2026-11-29], 107 days ($2.27/day for the first 18
            days (8/15-9/1), $2.26/day for the remaining 89 (9/2-11/29),
            cent-exact)."}
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
      - {seq: 1, amount: 125, due: 2026-08-17, status: pending, calendar_event_id: tja7bjk9ri35n0bqb01c52j4es}
      - {seq: 2, amount: 125, due: 2026-08-23, status: pending, calendar_event_id: gt4knt3i2m6lpjhlrjf8n2jqn8}
      - {seq: 3, amount: 125, due: 2026-08-30, status: pending, calendar_event_id: locnmilchabhgq2o0kd8slf7r4}
      - {seq: 4, amount: 125, due: 2026-09-06, status: pending, calendar_event_id: ekpni2dt25f0fe5tjh51sbjj64}
  - id: hillview-med-payment-plan
    creditor: "Hillview Med (David Alston, CAO; Beverly Willekes) — collections on an
               outstanding balance, no payment received since May 19, 2026"
    total: 2532.00
    note: "Personal, not business — Cuzzie's closed 2026-06-13 and Lemar is handling this
           balance personally rather than through the business (haven note
           haven/vault/20-Cuzzies/2026-08-19-hillview-med-outstanding-balance.md). David
           proposed $200 every other week until paid in full (email 2026-08-25 07:59am
           ET, gmail thread 1a01aeb6b8dd7c71); Lemar accepted directly by email
           (2026-08-25 10:10am ET) and David confirmed back (2026-08-25 10:50am ET,
           agreeing to a first-payment start ~2 weeks out). $2,532.00 ÷ $200/installment
           = 12.66, so 13 installments: 12 of $200.00 (12 x $200 = $2,400.00) and a
           final 13th installment of $132.00 (the true remainder of a fixed-payment
           plan, not a cents-split remainder) — same convention as every other
           split-total line in this ledger (remainder on the LAST installment, see the
           own-car-running goal). Biweekly cadence, first due 2026-09-07, +14 days each
           through 2027-02-22. Tracking/reminder only — nothing paid or contacted by
           this skill; Lemar's payment-account follow-up to David (personal vs. business
           account) is still open, see haven/vault/20-Cuzzies/2026-08-19-hillview-med-outstanding-balance.md."
    installments:
      - {seq: 1, amount: 200.00, due: 2026-09-07, status: pending, calendar_event_id: 3623o178cin0k8ur1kpn2pdvns}
      - {seq: 2, amount: 200.00, due: 2026-09-21, status: pending, calendar_event_id: 8tqp1f82emre4su8snpt7jkbm8}
      - {seq: 3, amount: 200.00, due: 2026-10-05, status: pending, calendar_event_id: 7eu40ni98rujmqkk06v056cvbk}
      - {seq: 4, amount: 200.00, due: 2026-10-19, status: pending, calendar_event_id: ers50di8vp5n9hgce2c93j2gbo}
      - {seq: 5, amount: 200.00, due: 2026-11-02, status: pending, calendar_event_id: 2r5l52mctslahsm46kt8v7jmr8}
      - {seq: 6, amount: 200.00, due: 2026-11-16, status: pending, calendar_event_id: jd8hhpom6630vcl7qngrb55mtc}
      - {seq: 7, amount: 200.00, due: 2026-11-30, status: pending, calendar_event_id: e97nucos0mevd25dtd027bppcs}
      - {seq: 8, amount: 200.00, due: 2026-12-14, status: pending, calendar_event_id: vtfhu3puaenc59dq1aferal2t8}
      - {seq: 9, amount: 200.00, due: 2026-12-28, status: pending, calendar_event_id: oeimlffdpuqsghv76hblnr1n30}
      - {seq: 10, amount: 200.00, due: 2027-01-11, status: pending, calendar_event_id: upuaup2c73s4ovo8133bm97c5g}
      - {seq: 11, amount: 200.00, due: 2027-01-25, status: pending, calendar_event_id: hnl66ogi3cbc604k4glred6jko}
      - {seq: 12, amount: 200.00, due: 2027-02-08, status: pending, calendar_event_id: v9tr3e2rvqa6l6s5clk1qh3uoo}
      - {seq: 13, amount: 132.00, due: 2027-02-22, status: pending, calendar_event_id: ntds0kc1kch49u6srj57ho1n4c}
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
    target: 594.81
    total_claim: 624.81
    gas_spent: null
    swept_to_maintenance: 0
    funded: 114.00
    shortfall: 480.81
    calendar_event_id: k9sog0mcpmisnn4p2hicernagk
    recompute_note: "2026-08-15 PART M: station-travel corrected $50.00 -> $80.00 per
      Lemar's rate confirmation (+$30.00 to target/total_claim/shortfall). Every other
      contribution/day unchanged; the new station-travel-weekly line (first_due
      2026-08-22) is not yet hand-spread into daily_targets -- deferred to the next
      dedicated recompute pass per this ledger's established practice for multi-day
      additions (same treatment as tmobile-split-2 / moms-car-oil-change / am-botte).
      2026-08-15 PART M (2), INCOME ALLOCATION: $144 the-station earnings logged;
      gas_maintenance.reserve $30.00 held in Spending first, $114.00 poured into
      today's contributions in due-date order -- station-travel (due today) funded in
      full ($80.00), liquidibee-1 (due 2026-08-16) partially funded ($34.00 of
      $125.00), the rest of the queue untouched. Surplus: $0 (money ran out mid-line).
      OVERLOAD CHECK ran for the first time this pass (income log crossed the 7-entry
      floor) -- see Update below and the #decisions card raised for it."
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: cuzzies-google-voice, amount: 12.67, funded: 0, status: pending}
      - {line_id: cuzzies-google-workspace, amount: 21.25, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.05, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 125.00, funded: 34.00, status: partial}
      - {line_id: liquidibee-2, amount: 15.63, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.69, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.67, funded: 0, status: pending}
      - {line_id: moms-car-oil-change, amount: 100.00, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.34, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: own-car-running-1, amount: 36.37, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.19, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.13, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.10, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.07, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.05, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.09, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: station-travel, amount: 80.00, funded: 80.00, status: paid}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.97, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-16":
    operating_reserve: 30.00
    target: 289.81
    total_claim: 319.81
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 289.81
    calendar_event_id: i5aqp4u51gvj79113o7ls4ajqk
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: cuzzies-google-voice, amount: 12.67, funded: 0, status: pending}
      - {line_id: cuzzies-google-workspace, amount: 21.25, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.05, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.63, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.69, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.67, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.34, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: own-car-running-1, amount: 36.37, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.19, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.13, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.10, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.07, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.05, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.09, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.97, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-17":
    operating_reserve: 30.00
    target: 380.75
    total_claim: 410.75
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 380.75
    calendar_event_id: 2f3r9682t2emqdu76snes086b8
    recompute_note: "2026-08-16 PART M: liquidibee-1's due date moved 8/16->8/17 (Lemar's
      Monday-call renegotiation plan). Its $91.00 remaining balance ($125.00 total minus
      the $34.00 already funded 2026-08-15, historical/untouched) added here as a new
      contribution; target/total_claim/shortfall raised by the same $91.00. 2026-08-16's
      daily_targets had NO existing liquidibee-1 contribution to remove -- the automatic
      ROLLOVER that should have carried the $91.00 shortfall from 2026-08-15 into
      2026-08-16 was explicitly deferred in that pass (see Update 2026-08-15 (3):
      'ROLLOVER is reserved for the day's LAST hourly scan') and no later pass ran it, so
      2026-08-16 never actually held the contribution this change was expected to move.
      Discrepancy flagged; nothing else on 2026-08-16 touched."
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: cuzzies-google-voice, amount: 12.66, funded: 0, status: pending}
      - {line_id: cuzzies-google-workspace, amount: 21.25, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.05, funded: 0, status: pending}
      - {line_id: liquidibee-1, amount: 91.00, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.63, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.69, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.67, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.33, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: own-car-running-1, amount: 36.36, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.07, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.05, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.09, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.97, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-18":
    operating_reserve: 30.00
    target: 277.06
    total_claim: 307.06
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 277.06
    calendar_event_id: i2k3vo0025kbt3lbseppnf690s
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: cuzzies-google-workspace, amount: 21.25, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.05, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.63, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.69, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.67, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.33, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: own-car-running-1, amount: 36.36, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.09, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-19":
    operating_reserve: 30.00
    target: 255.77
    total_claim: 285.77
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 255.77
    calendar_event_id: j6imqfltarucop954b1dkdvkq4
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.05, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.34, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.66, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.33, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: own-car-running-1, amount: 36.36, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-20":
    operating_reserve: 30.00
    target: 255.76
    total_claim: 285.76
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 255.76
    calendar_event_id: 7eg9gi4dqvae72l33nh0smr8c8
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.05, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: metrc-fee, amount: 6.66, funded: 0, status: pending}
      - {line_id: moms-lump-0821, amount: 18.33, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: own-car-running-1, amount: 36.36, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-21":
    operating_reserve: 30.00
    target: 230.77
    total_claim: 260.77
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 230.77
    calendar_event_id: 6q6rn0gp6umdaus4vil752rn78
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.05, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: own-car-running-1, amount: 36.36, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-22":
    operating_reserve: 30.00
    target: 194.41
    total_claim: 224.41
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 194.41
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.05, funded: 0, status: pending}
      - {line_id: liquidibee-2, amount: 15.62, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.85, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-23":
    operating_reserve: 30.00
    target: 178.77
    total_claim: 208.77
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 178.77
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.28, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-24":
    operating_reserve: 30.00
    target: 178.76
    total_claim: 208.76
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 178.76
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-25":
    operating_reserve: 30.00
    target: 194.15
    total_claim: 224.15
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 194.15
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.39, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-26":
    operating_reserve: 30.00
    target: 194.15
    total_claim: 224.15
    gas_spent: null
    swept_to_maintenance: 0
    funded: 40.78
    shortfall: 153.37
    calendar_event_id: null
    resolution: "INCOME ALLOCATION 2026-08-26 (PART M): $70.78 DoorDash earned today.
                 $30.00 held as the operating reserve (Spending, for gas — gas_spent
                 not yet reported today). Remaining $40.78 poured into today's
                 contributions in due-date order (soonest due first, ties by smallest
                 amount): patreon (due 8/27) funded in full $2.08; moms-weekly (due
                 8/28) funded in full $3.84; own-car-running-2 (due 8/29) funded in
                 full $18.18; liquidibee-3 (due 8/30) funded in full $8.33; claude (due
                 9/4) funded in full $5.00; own-car-running-3 (due 9/5) partially
                 funded $3.35 of $12.12 — money ran out here. Every later-due
                 contribution (liquidibee-4 through wispr-flow) stays pending,
                 untouched. No surplus — the money landed mid-line on
                 own-car-running-3."
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 5.00, status: funded}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.39, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 8.33, status: funded}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 3.84, status: funded}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 18.18, status: funded}
      - {line_id: own-car-running-3, amount: 12.12, funded: 3.35, status: partial}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: patreon, amount: 2.08, funded: 2.08, status: funded}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-27":
    operating_reserve: 30.00
    target: 192.07
    total_claim: 222.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 20.60
    shortfall: 171.47
    calendar_event_id: null
    resolution: "INCOME ALLOCATION 2026-08-27 (PART M): $50.60 DoorDash earned today,
                 reported in #personal-finance (ts 1787786194.689369). $30.00 held as
                 the operating reserve (Spending, for gas — gas_spent not yet reported
                 today). Remaining $20.60 poured into today's contributions in
                 due-date order (soonest due first, ties by smallest amount):
                 moms-weekly (due 8/28) funded in full $3.84; own-car-running-2 (due
                 8/29) partially funded $16.76 of $18.18 — money ran out here. Every
                 later-due contribution (liquidibee-3 through cashapp-payback) stays
                 pending, untouched. No surplus — the money landed mid-line on
                 own-car-running-2."
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.39, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 3.84, funded: 3.84, status: funded}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 16.76, status: partial}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-28":
    operating_reserve: 30.00
    target: 188.23
    total_claim: 218.23
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 188.23
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.39, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-2, amount: 18.18, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-29":
    operating_reserve: 30.00
    target: 178.39
    total_claim: 208.39
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 178.39
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.39, funded: 0, status: pending}
      - {line_id: liquidibee-3, amount: 8.33, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-30":
    operating_reserve: 30.00
    target: 170.06
    total_claim: 200.06
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 170.06
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.05, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.39, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.63, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-08-31":
    operating_reserve: 30.00
    target: 170.02
    total_claim: 200.02
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 170.02
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.38, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-09-01":
    operating_reserve: 30.00
    target: 170.02
    total_claim: 200.02
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 170.02
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.38, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.27, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.58, funded: 0, status: pending}
  "2026-09-02":
    operating_reserve: 30.00
    target: 170.00
    total_claim: 200.00
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 170.00
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.38, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-03":
    operating_reserve: 30.00
    target: 170.00
    total_claim: 200.00
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 170.00
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: claude, amount: 5.00, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.38, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-04":
    operating_reserve: 30.00
    target: 156.67
    total_claim: 186.67
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 156.67
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.38, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-3, amount: 12.12, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-05":
    operating_reserve: 30.00
    target: 152.89
    total_claim: 182.89
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 152.89
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.38, funded: 0, status: pending}
      - {line_id: liquidibee-4, amount: 5.68, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-06":
    operating_reserve: 30.00
    target: 147.21
    total_claim: 177.21
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 147.21
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: fantasy-football-buyin, amount: 13.04, funded: 0, status: pending}
      - {line_id: hillview-med-1, amount: 15.38, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-07":
    operating_reserve: 30.00
    target: 118.78
    total_claim: 148.78
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 118.78
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.20, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-08":
    operating_reserve: 30.00
    target: 118.77
    total_claim: 148.77
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 118.77
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-09":
    operating_reserve: 30.00
    target: 118.77
    total_claim: 148.77
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 118.77
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
      - {line_id: wispr-flow, amount: 0.57, funded: 0, status: pending}
  "2026-09-10":
    operating_reserve: 30.00
    target: 118.20
    total_claim: 148.20
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 118.20
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
  "2026-09-11":
    operating_reserve: 30.00
    target: 109.87
    total_claim: 139.87
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 109.87
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-4, amount: 9.09, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.13, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
  "2026-09-12":
    operating_reserve: 30.00
    target: 109.11
    total_claim: 139.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 109.11
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.12, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
  "2026-09-13":
    operating_reserve: 30.00
    target: 109.11
    total_claim: 139.11
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 109.11
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.12, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
  "2026-09-14":
    operating_reserve: 30.00
    target: 109.10
    total_claim: 139.10
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 109.10
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.55, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
      - {line_id: tow-truck-repay, amount: 16.12, funded: 0, status: pending}
      - {line_id: water-pump, amount: 5.96, funded: 0, status: pending}
  "2026-09-15":
    operating_reserve: 30.00
    target: 87.01
    total_claim: 117.01
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 87.01
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
      - {line_id: student-loans, amount: 15.62, funded: 0, status: pending}
  "2026-09-16":
    operating_reserve: 30.00
    target: 71.39
    total_claim: 101.39
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 71.39
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-17":
    operating_reserve: 30.00
    target: 71.39
    total_claim: 101.39
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 71.39
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-18":
    operating_reserve: 30.00
    target: 63.06
    total_claim: 93.06
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 63.06
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-5, amount: 7.27, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-19":
    operating_reserve: 30.00
    target: 64.13
    total_claim: 94.13
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 64.13
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-20":
    operating_reserve: 30.00
    target: 64.13
    total_claim: 94.13
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 64.13
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-21":
    operating_reserve: 30.00
    target: 64.12
    total_claim: 94.12
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 64.12
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-22":
    operating_reserve: 30.00
    target: 64.12
    total_claim: 94.12
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 64.12
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-23":
    operating_reserve: 30.00
    target: 64.12
    total_claim: 94.12
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 64.12
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-24":
    operating_reserve: 30.00
    target: 64.12
    total_claim: 94.12
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 64.12
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-25":
    operating_reserve: 30.00
    target: 55.79
    total_claim: 85.79
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 55.79
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-6, amount: 6.06, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-26":
    operating_reserve: 30.00
    target: 58.07
    total_claim: 88.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 58.07
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-27":
    operating_reserve: 30.00
    target: 58.07
    total_claim: 88.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 58.07
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.87, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.34, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-28":
    operating_reserve: 30.00
    target: 58.05
    total_claim: 88.05
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 58.05
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.86, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.64, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.31, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-29":
    operating_reserve: 30.00
    target: 58.03
    total_claim: 88.03
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 58.03
    calendar_event_id: null
    contributions:
      - {line_id: car-repair-payment, amount: 13.04, funded: 0, status: pending}
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: mechanic-repair-repay, amount: 10.86, funded: 0, status: pending}
      - {line_id: moms-weekly, amount: 8.33, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-09-30":
    operating_reserve: 30.00
    target: 25.80
    total_claim: 55.80
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 25.80
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-01":
    operating_reserve: 30.00
    target: 25.80
    total_claim: 55.80
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 25.80
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-02":
    operating_reserve: 30.00
    target: 25.80
    total_claim: 55.80
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 25.80
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-7, amount: 5.19, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-03":
    operating_reserve: 30.00
    target: 20.61
    total_claim: 50.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 20.61
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-04":
    operating_reserve: 30.00
    target: 20.61
    total_claim: 50.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 20.61
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-05":
    operating_reserve: 30.00
    target: 20.61
    total_claim: 50.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 20.61
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-06":
    operating_reserve: 30.00
    target: 20.61
    total_claim: 50.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 20.61
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-07":
    operating_reserve: 30.00
    target: 20.61
    total_claim: 50.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 20.61
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-08":
    operating_reserve: 30.00
    target: 20.61
    total_claim: 50.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 20.61
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-09":
    operating_reserve: 30.00
    target: 20.61
    total_claim: 50.61
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 20.61
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-8, amount: 4.54, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-10":
    operating_reserve: 30.00
    target: 16.07
    total_claim: 46.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.07
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-11":
    operating_reserve: 30.00
    target: 16.07
    total_claim: 46.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.07
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-12":
    operating_reserve: 30.00
    target: 16.07
    total_claim: 46.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.07
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-13":
    operating_reserve: 30.00
    target: 16.07
    total_claim: 46.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.07
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}
  "2026-10-14":
    operating_reserve: 30.00
    target: 16.07
    total_claim: 46.07
    gas_spent: null
    swept_to_maintenance: 0
    funded: 0
    shortfall: 16.07
    calendar_event_id: null
    contributions:
      - {line_id: cashapp-payback, amount: 1.75, funded: 0, status: pending}
      - {line_id: dil-christmas-gift, amount: 1.09, funded: 0, status: pending}
      - {line_id: own-car-running-10, amount: 3.63, funded: 0, status: pending}
      - {line_id: own-car-running-11, amount: 3.30, funded: 0, status: pending}
      - {line_id: own-car-running-9, amount: 4.04, funded: 0, status: pending}
      - {line_id: self-account-balance-repay, amount: 2.26, funded: 0, status: pending}