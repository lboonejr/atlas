---
created: 2026-08-05T07:47:00-04:00
updated: 2026-08-10T10:05:00-04:00
domain: personal
type: reference
status: active
tags: [personal-finance, budget, money-hub]
source: claude
area: money
---

# Money Hub — ledger (source of truth)

This note is the ONE structured source of truth for Lemar's personal budget: bills,
payment plans, goals, the two account pockets, the daily set-aside ramp, and reported
cash. The **money-hub** skill (`.claude/skills/money-hub/SKILL.md`) reads and writes the
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
- `track` = `queue` (must carry a date; gets ramped and queued) or `spending` (paid as
  you go from the Spending pocket; no date, no ramp, not a defect). Added 2026-08-10.
- `daily_targets` = the even daily set-aside ramp. ISO date key →
  `{total, calendar_event_id, contributions: [{bill_id, amount, status}]}`, `status`
  one of `pending` | `rolled` | `paid`. One aggregate calendar event per day.
- **The allocation SHAPE is DUE-DATE ORDER, locked 2026-08-10** — no priority tiers, no
  weekly floor, no waterfall. Do not redesign it here.
- **A `track: queue` line with no date is a defect, not a low priority.** It has no
  position in the queue, no calendar event, and no ramp — it is invisible. Every one of
  them belongs in `open_questions` until Lemar supplies a date.
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
cash_on_hand:
  amount: null                       # Lemar reports: "I have $X cash"
  as_of: null
pockets:                             # TWO pockets (locked 2026-08-10). Lemar moves the
                                     # money; nothing here transfers anything.
  - {id: spending, name: "Spending",  account: sofi-checking, era_account: "Checking - 4102",
     status: active, role: "income lands here; day-to-day spending pays from here"}
  - {id: set-aside, name: "Set-Aside", account: sofi-savings, era_account: "Savings - 6970",
     status: active, role: "the daily set-aside number moves here; queued bills pay from here"}
  # -- retired with the Option 3 model 2026-08-10; still Lemar's accounts, no longer
  #    part of the model. Never resurrect without an explicit instruction.
  - {id: cashapp-checking,  status: parked, note: "was p5 own-car pocket"}
  - {id: cashapp-savings,   status: parked, note: "was p6 side-projects pocket"}
  - {id: doordash-crimson,  status: parked, note: "was p1 Cuzzie's buffer (checking + savings)"}
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
  # -- day-to-day spending: paid as you go from the Spending pocket, never ramped --
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
daily_targets:
  "2026-08-10":
    total: 170.28
    calendar_event_id: kli8jm1vlal3ntffr2lqdkpmuk
    contributions:
      - {bill_id: metrc-fee, amount: 40, status: pending}
      - {bill_id: cleaning-supplies, amount: 30, status: pending}
      - {bill_id: comedy-show-tickets, amount: 50.28, status: pending}
      - {bill_id: station-travel, amount: 50, status: pending}
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
  - "Era Context: SoFi connection needs a reconnect at era.app (balances are stale to 2026-07-11); Cash App still syncing; plan tier caps at 2 linked accounts"
  - "Station travel $50/wk: Lemar started a weekend job at The Station 8/9 — pay rate not yet known, he'll report it in #personal-finance"
  - "Income backlog: Lemar is posting ~2 weeks of DoorDash earnings to #personal-finance (2026-08-10). Until they land, income_target_weekly $500 is a guess and the overload check can't run."
```

## History

Everything before 2026-08-05 lives in
[[2026-07-11-personal-finance-dashboard-project]] — the project note that developed the
budget from the first rough sketch through the (now retired) Option 3 allocation
decision, the six-pocket mapping, and the calendar reminders. That note is closed; this
ledger carries the live state forward.

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
