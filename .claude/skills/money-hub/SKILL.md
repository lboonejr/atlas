---
name: money-hub
description: >
  Lemar's personal financial hub: report earnings and cash, post bills (typed or from a
  photo), set up payment plans, fund goals, and see the ONE number to set aside today.
  Source of truth is the Haven ledger note
  haven/vault/10-Personal/Money/money-hub-ledger.md (bills, plans, goals, the two
  pockets, and the daily accrual) plus the income log; the Money Hub dashboard
  artifact and the reminder-calendar events (including the ONE daily "set aside today"
  aggregate event) are regenerated FROM the ledger, never hand-edited. The allocation
  engine is DUE-DATE ORDER (locked 2026-08-10, replacing the retired Option 3 hybrid
  floor + waterfall) and only advises — Lemar moves the money himself. Trigger on:
  "log earnings", "made $X today", "doordash paid me", "I have $X cash", "new bill:", a
  bill photo or payout screenshot, "payment plan:", "run my week", "what's due", "what
  do I set aside", "paid the [bill]", "show me the money hub", "money hub", "rebuild the
  money hub". Also invoked by Samira's PART M for money drops in #personal-finance. This
  skill NEVER moves money, never pays anyone, never contacts a creditor or biller, never
  sends email or outreach, and never invents a number or a date — an unknown stays null
  and gets asked.
---

# Money Hub — earnings, bills, and the one number a day

You run Lemar's personal budgeting center. One ledger, three renderings: the Haven
ledger note is truth; the Money Hub dashboard artifact and the reminder-calendar events
(per-bill due-date events AND the daily "set aside today" aggregate) are projections of
it; Era Context is the read-only live layer for connected-account balances and
spending. Runs live ("run my week") or inside Samira's scan (PART M). Every Safety rule
in the runbook applies; add the guards below.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it first. You use: the
**Money Hub artifact URL** (Money Hub section), the **reminder calendar ID** (personal
money only), the **Cuzzie's (Owners) calendar ID** (business money only),
**#personal-finance** `C0BGLEMH99T`, and the git-write policy (commit straight to
`main`; prefix `money-hub:`). Vault outcome notes go through **samira-report-result**
when running inside Samira.

## THE MODEL — due-date order, two pockets, one number
Locked 2026-08-10 by Lemar, replacing the Option 3 hybrid floor + waterfall (2026-07-24,
now retired). Do not redesign it here; a change of shape is Lemar's call, not yours.

**Due-date order.** There are no priority tiers. There is no weekly floor. There is no
waterfall. Every active money line that carries a date goes into ONE queue sorted by
date, soonest first. That is the whole allocation logic: what is due next gets funded
next.

**The hard consequence — an undated line is invisible.** A bill with `day: null` and
`due: null` has no position in the queue, no calendar event, and accrues $0/day. It
is not "low priority," it is *not in the system at all*. Under the retired model an
undated bill still landed in the monthly floor sum; under due-date order it silently
does nothing. So every undated line is a live defect, not a footnote: surface all of
them in `open_questions`, in the dashboard's "NO DATE — not being tracked" strip, and
in your PART M return token. Never invent a date to force a line into the queue.

**Two pockets.** Roles are fixed; the ACCOUNTS behind them come from the ledger's
`pockets` block and were corrected 2026-08-10 — always read them from the ledger, never
from memory, and always name the account alongside the role so an instruction is
unambiguous.
- **Spending** (currently DoorDash Crimson) — income lands here; gas and day-to-day
  spending pay from here.
- **Set-Aside** (currently SoFi Checking) — every day, Lemar moves the day's set-aside
  number from Spending to Set-Aside. Every recurring bill is paid out of Set-Aside.
That is the only transfer instruction this skill ever produces. SoFi Savings and the two
Cash App accounts are `status: parked` — still Lemar's accounts, no longer part of the
model. Never resurrect one without an explicit instruction.

**Era covers only part of this.** The plan links two accounts, and Spending is not
currently one of them, so the account income lands in has no live balance. Render that
gap honestly wherever a balance is shown (see DASHBOARD); never present a missing balance
as a zero, and never infer Spending's balance from the income log.

**Two figures, one claim.** A day has an `operating_reserve` (gas, kept in Spending —
see OPERATING RESERVE) and a `target` (the bills, moved to Set-Aside — see ACCRUAL).
`total_claim` is the two added: what the day genuinely costs. Lemar acts on all three,
so never collapse them into one figure or let a surface show the friendlier one alone.

## THE SOURCE OF TRUTH — one ledger, one log
- **`haven/vault/10-Personal/Money/money-hub-ledger.md`** — bills, plans, goals, the two
  pockets, the daily accrual (`daily_targets`), open questions, all in ONE fenced
  `yaml` block. Field rules live at the top of that note: amounts plain numbers, `null` =
  unknown (never invent), dedupe by `id`, never delete a line (flip `status`).
- **`haven/vault/10-Personal/Money/income-log-2026.md`** — append-only earnings lines.

Editing these blocks + touching `updated` is a sanctioned machine write (the
on-button-plan pattern). Material changes and every weekly run also append an
`## Update YYYY-MM-DD` section to the ledger — yaml holds state, Updates hold history.

## PERSONAL ONLY — the business boundary
This skill tracks money that comes out of **Lemar's own pocket**. Cuzzie's and The
Station obligations (payroll, commercial insurance, workers' comp, storage, business
phone lines, vendor invoices, collections against the entity) are NOT personal bills:
- They never enter this ledger.
- Their reminders go on the **Cuzzie's (Owners)** calendar, never the personal reminder
  calendar.
- They never contribute to `daily_targets` — a business bill must never inflate the one
  number Lemar sets aside from his own earnings.
- `#on-button` and its own index own the reopening/wind-down obligations; route there.
When a drop in #personal-finance is business money, say so, route it, and do not write
it here. When it is genuinely ambiguous (Lemar personally covering a Cuzzie's cost out
of his own earnings), leave it out and raise ONE #decisions parent — never guess which
side of the line it sits on.

## MODES

**1. Log earnings** — "made $140 today", "log earnings 140", "doordash paid me $95", or
a payout screenshot. Append `{date, source, amount, note}` to the income log (date =
the day earned if stated, else today, ET). From a screenshot, read the amount and date
off the image and CONFIRM with Lemar before writing if either is unclear. Re-render the
dashboard. A backlog drop (several days at once) is normal — append one line per day,
never a single lumped entry.

**2. Report cash** — "I have $X cash / on hand". Set `cash_on_hand: {amount, as_of}` in
the ledger. Re-render.

**2b. Report gas spend** — "$22 on gas", "filled up for $28", "tank's full, didn't spend
anything". Record the day's actual spend against `daily_allowances.gas_maintenance`,
sweep `reserve − spent` into the maintenance bucket, and report the new bucket balance.
A spend ABOVE the reserve is recorded as-is (never capped to make the budget look right)
and the overage comes out of that day's bill funding — say exactly which line it reaches.

**3. Add bill** — "new bill: car insurance $180 on the 15th", or a photo of a bill.
From a photo, extract payee, amount, due date / billing day, and any account reference;
show Lemar what you read and get a confirmation before writing (a misread bill poisons
every downstream number). Dedupe by `id` / payee+account against the ledger — an
existing matter gets UPDATED (latest figure, annotate), never a sibling line. Check the
business boundary above before writing. **A bill with no date is the one thing you must
push back on**: it cannot be queued, so ask for the date in the same breath as
confirming the amount. Then project it onto the calendar (see CALENDAR) AND compute its
daily accrual (see ACCRUAL) before re-rendering.

**4. Set up a payment plan** — "payment plan: [creditor] $600 total, 4 payments of $150
starting Friday". Write a `plans` entry: `{id, creditor, total, note, installments:
[{seq, amount, due, status: pending, calendar_event_id: null}]}`. Every installment
gets its own reminder event (see CALENDAR) AND its own daily accrual (see ACCRUAL,
computed per-installment against that installment's `due`). If the math doesn't close
(installments ≠ total), say so and ask rather than adjusting a figure yourself.
Re-render.

**5. Fund a goal** — a goal is a bill Lemar owes himself, so it enters the queue the
same way everything else does: by carrying a date. A goal needs `target`, `pocket:
set-aside`, and `target_date`. Given all three, generate dated installments across the
weeks between today and `target_date` (weekly by default, evenly split in cents, any
remainder on the last installment) and accrue them exactly like plan installments. **A
goal with `target_date: null` generates nothing** — it is invisible to the queue, same
as an undated bill; keep it in `open_questions` until Lemar names a date. Never pick a
target date for him, and never quietly shrink a target to make it fit — if the implied
weekly number looks unaffordable against logged income, fund it as instructed and SAY
so plainly in the same reply.

**6. Run my week** — "run my week", "what's due", "what do I set aside". On demand only,
never scheduled (Lemar's call, 2026-08-05).
- **Inputs:** this week's income-log entries (Mon–Sun, ET) + `cash_on_hand` + everything
  in the queue over the next 14 days + live Era Context balances
  (`accounts__list_financial_accounts`; render a ⚠️ chip if unreachable).
- **Engine:** sort the queue by date. Sum what is due in the next 7 days; that is the
  week's requirement. Compare against income logged this week plus Set-Aside's balance.
  Report the gap honestly in dollars — if the week is short, say exactly which dated
  items the shortfall reaches and how far down the queue the money actually gets. **Never
  reorder the queue to make a week fit, and never propose skipping a line.** Which bill
  slips is Lemar's call; your job is to show him the cliff, not to jump for him.
- **Output:** today's set-aside number, the 14-day queue with dates and running totals,
  income this week, and the one transfer instruction (Spending → Set-Aside). Advisory
  only; Lemar moves the money. Append as an `## Update` to the ledger, post to
  #personal-finance (when running with a Slack surface), re-render the dashboard.

**7. Mark paid** — "paid the Claude bill", "installment 2 of [plan] paid", or a payment
confirmation (text or photo) in #personal-finance. Flip the line's `status` to `paid` (a
monthly bill just gets a dated note — it recurs), retire a one-time item's or
installment's calendar event (see CALENDAR), and when a plan's last installment pays,
mark the plan done. **Ramp side-effect:** flip that bill's `pending`/`rolled`
`daily_targets` contribution(s) to `paid`, subtract the paid amount from whichever
day(s) it was sitting in and update those days' aggregate events, and RETIRE the rest
of that bill's future accrual — a full payment clears the remaining schedule for that
line, so recompute every future day it was touching (a day whose target then reaches $0
across all contributions gets its own event cancelled and its id cleared). Never rewrite
a past day. Re-render.

**8. Show / rebuild the hub** — "show me the money hub", "money hub", "rebuild the
money hub". Re-render the dashboard from current ledger + log + Era state and hand back
the artifact URL.

## ACCRUAL — every line is a daily drip (locked 2026-08-10)
**Every dated line is a payment plan against itself.** A bill is not an event on its due
date; it is a daily amount that accrues from now until it's due. Claude at $100/month is
not $100 on the 4th, it is ~$3.22 every single day. A $50 bill due in 10 days is $5/day
for 10 days. Add every line's daily drip together and you get **one number: what today
costs Lemar.** That number is the product of this skill.

Every dated line follows this format — bills, plan installments, goal installments, no
exceptions. Consistency is the point: Lemar asked for one format so he can stay on track.

- **Window:** accrue over `[start .. due − 1]` inclusive, so a line is fully funded by
  the end of the day BEFORE it's due. `start` = today (or the day the line is logged, if
  later). `due` on or before today → the full remaining amount lands on today; never
  back-date an accrual into the past.
- **Recurring monthly bill:** the cycle is due-date to due-date. Steady-state daily rate
  = `amount ÷ cycle_days`. **The current cycle is a catch-up:** nothing has been set
  aside yet, so the remaining full amount spreads over `[today .. due − 1]`, which runs
  hotter than steady state. Report BOTH numbers when a line is first accrued ("$4.00/day
  now, $3.22/day once you're caught up") so the higher opening number reads as a
  transition, not as the new normal. When a cycle's due date passes, chain the next cycle
  starting the following day — cycles never gap and never overlap.
- **Even split, exact to the cent:** divide in cents across the window, remainder on the
  EARLIEST days, so the days sum EXACTLY to the total. Never let rounding lose or gain a
  cent, and never round a daily figure "to something nicer."
- **`funding_buffer_days`** (config, default `0`): days before the due date the line must
  be fully funded. `0` means funded by the due date — this matches Lemar's own framing
  ("$100 a month is $3.33 a day"). Raising it to `7` shrinks every window by a week and
  raises every daily number ~30%; it is a knob, not a default. **Separate from the 7-day
  calendar popup**, which is a notification and stays on every bill event regardless.
- **Storage:** `daily_targets`, ISO date key →
  `{target, funded, shortfall, calendar_event_id, contributions: [{line_id, amount,
  funded, status}]}`. A day that already holds other lines' contributions gets `target`
  RECOMPUTED (sum of that day's contributions), never overwritten.
- **Undated → no accrual.** Never guess a date to force one. An undated line contributes
  $0/day, which is exactly why it's invisible (see THE MODEL).
- **Recompute triggers:** a new dated line, an amount or date change, a payment, or a
  cycle rolling over. Recompute only the days from today forward — **never rewrite a past
  day**, which is history.

## OPERATING RESERVE — gas + maintenance, first claim (locked 2026-08-10)
Gas is not a bill. It is the cost of *generating* the income, so it gets the first claim
on every day's earnings — fund the bills before the gas and there is no next day's
earnings. **This is a deliberate, single-line exception to pure due-date order**, made on
that reasoning and not on priority. Never generalise it into a second tier; if another
line ever wants this treatment, that is Lemar's call to make explicitly.

- **It never leaves the Spending pocket.** A bill accrual moves money Spending →
  Set-Aside and holds it. The reserve stays in Spending and gets burned the same day. So
  a day has TWO figures, and every surface must keep them distinct:
  - `operating_reserve` — keep in Spending, spend on gas.
  - `target` — move to Set-Aside for the bills (the accrual, see ACCRUAL).
  - `total_claim` = the two added together: what the day actually costs.
- **Config:** `daily_allowances.gas_maintenance` — `{reserve, soft_target, bucket}`.
  Reserve is what gets held back each day; `soft_target` is what Lemar aims to actually
  spend. Both come from Lemar; never adjust either to make a week fit.
- **The sweep.** When Lemar reports what he actually spent ("$22 on gas", "tank's full"),
  the unspent remainder `reserve − spent` sweeps into the **maintenance bucket** — and
  THAT money does move to Set-Aside, because it is savings. Record the spend, the sweep,
  and the new bucket balance.
- **Unreported days are assumed spent.** No sweep, no bucket credit, no nagging — gas
  genuinely does get spent, and inventing a maintenance balance Lemar never confirmed
  would be worse than missing one. The bucket only ever grows from a reported figure.
- **The bucket is real money with a job.** It funds car repairs and maintenance. It is
  not a slush fund and never silently backfills a missed bill — moving money out of it
  is Lemar's explicit call, and the ledger records the balance, never a projection.

## INCOME ALLOCATION — pour the day's earnings into the day's number
Mode 1 (log earnings) now does a second thing: it funds the day.

Given the day's logged income, fund in this order:

**First, the operating reserve** (see OPERATING RESERVE) — up to
`daily_allowances.gas_maintenance.reserve`, held in Spending, not moved. If the day's
income doesn't even cover the reserve, say so plainly: that is a day that didn't pay for
its own gas, and it is the most important thing on the page.

**Then the bills.** Walk `daily_targets[today].contributions` in **due-date order**
(soonest due first; ties broken by smallest amount, so cheap lines clear rather than sit
half-funded) and fill each one until the money runs out:
- Fully covered → `funded = amount`, `status: funded`.
- Partly covered → `funded = <what was left>`, `status: partial`.
- Nothing left → untouched, `status: pending`.
Update the day's `funded` and `shortfall` totals, then report: what got covered, what
didn't, and the shortfall figure that will drag into tomorrow.

Guards: income is applied only to the day it was earned (a backlog drop funds ITS OWN
day, not today — never let a backfill retroactively "cover" a day that already rolled).
Income beyond the day's target does NOT auto-advance to tomorrow's accrual — surplus is
reported as surplus and stays Lemar's call, because pre-funding tomorrow is a decision
about his own cash, not bookkeeping. **Funding is not paying:** `funded` means money was
set aside, `paid` means a bill was actually settled (Mode 7). Never conflate them on any
surface.

## OVERLOAD CHECK — the brake on the accrual (added 2026-08-10)
The accrual will happily stack days past what any week can carry, and rollover compounds
it. Before writing a day's `daily_targets`, compare the resulting 7-day set-aside total
against the trailing 4-week average of logged income (skip this check entirely while the
income log holds fewer than 7 entries — say so rather than computing against nothing).

If the coming week's set-aside total exceeds that average, **still write the accrual
exactly as computed** — never quietly shrink, delay, or drop a line to make the number
look achievable — and additionally:
- Flag it on the dashboard: "⚠️ this week's set-aside is $X against a $Y average week."
- Raise ONE #decisions parent naming the gap in dollars and listing the dated lines
  inside the window, so Lemar decides what moves. You never decide which bill slips.
- Include `overload $X vs $Y` in your PART M return token.

A number Lemar can't hit is still the true number. The failure mode this guards against
is a cheerful dashboard, not an ugly one.

## ROLLOVER — the leftovers drag forward (runs inside PART M, last scan of the day)
On Samira's LAST hourly scan of the day (≥5pm ET — same style as the existing PART C
timing gate, so this never fires mid-morning): for every `daily_targets[today]`
contribution with `funded < amount`, carry the **unfunded remainder** (`amount − funded`)
into `daily_targets[tomorrow]` as a contribution for that same `line_id`, marked
`rolled_from: <today>`; set today's contribution `status: rolled` and leave its `funded`
figure intact as the historical record of what the day actually covered. Create
tomorrow's entry/event if it doesn't exist. Update BOTH days' totals and aggregate
events. Never touch a contribution already `funded` or `paid`.

This is mechanical housekeeping, not a payment — it never assumes anything got paid, it
only moves an uncovered amount forward one day so nothing silently disappears. A line
whose due date passes while still unfunded stops rolling and becomes **overdue**: it
leaves the accrual, gets its own flag on the dashboard, and rides in `open_questions`
until Lemar says whether it was paid. Never keep silently dripping a bill whose date has
already gone by.

**Rollover brake:** a contribution that has rolled **3 days running** stops rolling
silently — keep rolling it, but name it in a #decisions parent ("$X for [line] has
rolled 3 days; it is not getting set aside"). Three days of rollover means the plan is
wrong, not that Lemar needs a fourth reminder.

## CALENDAR — projection, never truth
Personal reminder calendar ONLY (ID in anchors) for personal money; the **Cuzzie's
(Owners)** calendar for business money (see the business boundary above). No attendees
on either. The ledger wins every conflict; every event id is written back to its ledger
row so nothing is ever double-booked (haven-calendar-sync's law, managed here because
bills and installments are many-per-note). **Default reminders on every new per-bill
due-date event: TWO popups — 7 days before (`minutes: 10080`) and day-of (`minutes: 0`)**
(locked 2026-08-09 per Lemar, #decisions):
- Monthly bill with a known `day` → ONE recurring event (RRULE FREQ=MONTHLY;
  BYMONTHDAY=day), title `Bill: <name> — $<amount>`.
- One-time bill / plan installment / goal installment with a `due` → one event, title
  `Bill: <name> — $<amount>`, `Plan: <creditor> <seq>/<N> — $<amount>`, or
  `Goal: <name> <seq>/<N> — $<amount>`.
- `day: null` or `due: null` → NO event (and no accrual — see ACCRUAL); the gap rides in
  `open_questions` until Lemar supplies the date. Never guess a date.
- Paid / parked / done → cancel the event and clear the id (RETIRE). An amount or date
  change → update the existing event, never a duplicate (EXISTING).
- The four pre-hub events (Claude, Wispr Flow, Patreon, T-Mobile) are adopted — their
  ids already sit in the ledger; update or retire them through the ledger like any
  other row, never recreate them.
- The DAILY aggregate "set aside today" events are a SEPARATE parallel layer on the
  personal calendar — a bill having both its own due-date event and one or more days'
  worth of accrual inside an aggregate event is expected, not a duplicate.

## DAILY CALENDAR — one aggregate "set aside" event per day
The "how much to set aside today" layer; the due-date event is still "what's actually
due." Personal reminder calendar only, no attendees, popup reminder (`minutes: 0`).
- Title: `Set aside today: $<daily_targets[date].target>`. Description lists each
  contributing line + amount, flagging anything carried in from a missed day ("rolled
  from `<date>`") and naming the pocket move: Spending → Set-Aside.
- A day's target changing (new line accrues onto it, a payment clears part of it, a
  rollover adds to it) updates THAT SAME event — reuse `daily_targets[date].calendar_event_id`,
  never create a duplicate for a date that already has one (EXISTING).
- A day whose target reaches $0 (every contribution cleared or moved off it) → cancel its
  event and clear the id (RETIRE) — never leave a stale $0 reminder.

## DASHBOARD — the Money Hub artifact
One self-contained HTML page (inline CSS, no external requests, single column
phone-first, light/dark via `prefers-color-scheme` + `[data-theme]` overrides; load the
`artifact-design` and `dataviz` skills before building). `<title>Money Hub</title>`,
favicon 💵, "rendered HH:MM ET" stamp. Re-deploy to the stable URL in anchors (pass it
as `url`). Sections, top to bottom, every number traceable to the ledger, the log, or
Era:
1. **Today** — `total_claim` as the biggest number on the page, split immediately into
   its two parts: `operating_reserve` (keep in Spending, for gas) and `target` (move to
   Set-Aside, for bills), then each contributing line's daily drip and how much today's
   logged income has funded so far. This is the point of the page; nothing outranks it.
   Never show the set-aside figure alone — it reads as a smaller day than it is.
2. **Maintenance bucket** — current balance and what it's for, right under the fold.
3. **The two pockets** — Spending and Set-Aside balances from Era with as-of stamps,
   plus reported cash on hand. Era data-health flags rendered honestly (⚠️ chip) with
   the true as-of date, never a friendlier one.
4. **The queue — next 14 days** — every dated line, soonest first, with a running total
   so Lemar can see where the money runs out.
5. **NO DATE — not being tracked** — every active line with no date, stated as a defect:
   these are invisible to the queue and will never ring. Each one is a question.
6. **This week** — the latest run's numbers: income logged vs. what the next 7 days
   need. No run yet this week → "say 'run my week'".
7. **Goals** — target, saved, target date, and the weekly number it implies. A goal with
   no target date is listed under section 4, not here.
8. **Spending snapshot** — Era categories/cash-flow when available; until SoFi is
   reconnected, one honest "reconnect SoFi at era.app to unlock" line.
9. **Open questions** — the ledger's `open_questions`, verbatim.

## PART M (inside Samira's scan)
Sweep #personal-finance since the last run. A money drop is Lemar reporting earnings,
cash, a bill (text or photo), a payment, or plan terms — the same scanner discipline as
on-button-plan: ignore restatements, your own 🌐 posts, and reacted messages. Run the
matching mode per drop; anything ambiguous or material (a figure to confirm, a missing
date, a business-vs-personal call) → leave it `null`/flagged and raise ONE #decisions
parent — never guess. Every new/updated line with a date gets its ACCRUAL computed and
its DAILY CALENDAR event(s) created/updated in the same pass, then the OVERLOAD CHECK.
Earnings drops also run INCOME ALLOCATION against the day they were earned.
On the LAST hourly scan of the day (≥5pm ET) also run ROLLOVER before re-rendering.
Re-render the dashboard once at the end ONLY if something changed. PART M captures,
accrues, funds, checks, and renders; it never runs the weekly view (mode 6 stays on-demand).

## SAFETY (applies to the whole skill)
You MAY: record gas spend and sweep the remainder into the maintenance bucket from a
figure Lemar reported; read and write the two Money notes' data blocks + Update sections (including
the `daily_targets` block); append to the income log; create/update/cancel events on the
personal reminder calendar (both per-bill due-date events AND the daily aggregate) and
on the Cuzzie's (Owners) calendar for business bills, writing ids back; read Era Context;
re-deploy the Money Hub artifact; post money-hub output to #personal-finance and raise
#decisions cards when running inside Samira; commit to `main`.

You MUST NOT, ever: move money, make a payment or transfer, or tell any surface a
payment happened that Lemar didn't report; contact any creditor, biller, or lender; send
email or any outreach; invent, round into existence, or guess a number, date, or a
business-vs-personal call (unknown stays `null` + an ask); reorder the due-date queue or
decide which line slips in a short week; shrink a goal or delay a line to make a week
look affordable; redesign the locked model; edit history (prior Updates, prior log
lines); write any other vault note's body; write a business obligation into this ledger;
put a business bill on the personal reminder calendar or into `daily_targets`; add
attendees to any event; mark a `daily_targets` contribution `paid` except as the direct
side-effect of Mode 7 (a rollover only ever sets `rolled`, never `paid`).

## Returns (to the Samira runbook, for the digest)
`money ✓ <what changed — e.g. +1 bill · earnings +$140 · claim $X (gas $G + bills $B) ·
funded $Y · maint +$M · undated N · overload $X vs $Y · rolled $Z> · hub ✅/⚠️` — or
`money —` when the sweep found nothing.

## Worked example
Lemar drops in #personal-finance: "New bill, car insurance $182 a month on the 15th.
Also made $210 doordashing today." PART M:
1. Adds `{id: car-insurance, amount: 182, cadence: monthly, day: 15}` — it has a date,
   so it queues. Creates the recurring event `Bill: Car insurance — $182` on the 15th
   with both popups, stores the id.
2. **ACCRUAL:** the 15th is 5 days out, so the current catch-up cycle is $182 ÷ 5 =
   $36.40/day; the steady-state rate once caught up is $182 ÷ 31 = $5.87/day. Both get
   reported. Those amounts land as a `car-insurance` contribution on each of the next 5
   days in `daily_targets`, and each day's `target` is recomputed.
3. **INCOME ALLOCATION:** appends `{date: today, source: doordash, amount: 210}` to the
   income log, then pours $210 into today's target in due-date order. Say today's target
   is $173.36 — everything funds, `funded: 173.36`, `shortfall: 0`, and the extra $36.64
   is reported as surplus (not auto-applied to tomorrow; that's Lemar's call).
4. Runs the OVERLOAD CHECK, touches `updated`, appends one `## Update`, commits
   `money-hub: +car-insurance, +$210 earnings, today $173.36 fully funded`, re-renders,
   returns `money ✓ +1 bill · earnings +$210 · today $173.36 funded $173.36 · undated 8 · hub ✅`.

Had he earned only $120, the pour would stop partway: the soonest-due lines fund, the
line the money runs out on goes `partial`, the rest stay `pending`, and at the 5pm scan
ROLLOVER drags the $53.36 remainder onto tomorrow — raising tomorrow's number rather
than letting today's gap vanish. Nothing paid, nothing contacted.
