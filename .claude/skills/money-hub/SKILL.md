---
name: money-hub
description: >
  Lemar's personal financial hub: report earnings and cash, post bills (typed or from a
  photo), set up payment plans, fund goals, and see the ONE number to set aside today.
  Source of truth is the Haven ledger note
  haven/vault/10-Personal/Money/money-hub-ledger.md (bills, plans, goals, the two
  pockets, and the daily set-aside ramp) plus the income log; the Money Hub dashboard
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
`due: null` has no position in the queue, gets no calendar event, and gets no ramp. It
is not "low priority," it is *not in the system at all*. Under the retired model an
undated bill still landed in the monthly floor sum; under due-date order it silently
does nothing. So every undated line is a live defect, not a footnote: surface all of
them in `open_questions`, in the dashboard's "NO DATE — not being tracked" strip, and
in your PART M return token. Never invent a date to force a line into the queue.

**Two pockets.**
- **Spending** (SoFi Checking) — income lands here; this is money Lemar may spend.
- **Set-Aside** (SoFi Savings) — every day, Lemar moves the day's set-aside number from
  Spending to Set-Aside. Bills get paid out of Set-Aside.
That is the only transfer instruction this skill ever produces. The four pockets from
the retired model (Cash App checking/savings, DoorDash Crimson) are `status: parked` in
the ledger — still Lemar's accounts, no longer part of the model. Never resurrect them
without an explicit instruction.

**One number.** `daily_targets[today].total` is the single figure Lemar acts on. Every
other view exists to explain that number, never to compete with it.

## THE SOURCE OF TRUTH — one ledger, one log
- **`haven/vault/10-Personal/Money/money-hub-ledger.md`** — bills, plans, goals, the two
  pockets, the daily set-aside ramp (`daily_targets`), open questions, all in ONE fenced
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

**3. Add bill** — "new bill: car insurance $180 on the 15th", or a photo of a bill.
From a photo, extract payee, amount, due date / billing day, and any account reference;
show Lemar what you read and get a confirmation before writing (a misread bill poisons
every downstream number). Dedupe by `id` / payee+account against the ledger — an
existing matter gets UPDATED (latest figure, annotate), never a sibling line. Check the
business boundary above before writing. **A bill with no date is the one thing you must
push back on**: it cannot be queued, so ask for the date in the same breath as
confirming the amount. Then project it onto the calendar (see CALENDAR) AND compute its
set-aside ramp (see RAMP) before re-rendering.

**4. Set up a payment plan** — "payment plan: [creditor] $600 total, 4 payments of $150
starting Friday". Write a `plans` entry: `{id, creditor, total, note, installments:
[{seq, amount, due, status: pending, calendar_event_id: null}]}`. Every installment
gets its own reminder event (see CALENDAR) AND its own set-aside ramp (see RAMP,
computed per-installment against that installment's `due`). If the math doesn't close
(installments ≠ total), say so and ask rather than adjusting a figure yourself.
Re-render.

**5. Fund a goal** — a goal is a bill Lemar owes himself, so it enters the queue the
same way everything else does: by carrying a date. A goal needs `target`, `pocket:
set-aside`, and `target_date`. Given all three, generate dated installments across the
weeks between today and `target_date` (weekly by default, evenly split in cents, any
remainder on the last installment) and ramp them exactly like plan installments. **A
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
of that bill's future ramp days — a full payment clears the remaining schedule for that
bill, so recompute every future day it was touching (a day whose total then reaches $0
across all contributions gets its own event cancelled and its id cleared). Re-render.

**8. Show / rebuild the hub** — "show me the money hub", "money hub", "rebuild the
money hub". Re-render the dashboard from current ledger + log + Era state and hand back
the artifact URL.

## RAMP — even daily set-aside
Every dated line (bill, installment, goal installment) turns into an even daily savings
target, so Lemar sees ONE combined "set aside today" number instead of tracking each
line separately. This is the mechanism that makes due-date order livable: the queue says
*what* is next, the ramp says *how much today*.

- **Window:** `start` = the day after the line is logged (for a recurring bill's LATER
  cycles — i.e. every occurrence after the first — `start` = the day after the PRIOR
  cycle's due date, so cycles chain with no gap). `end` = the due date minus 7 days.
- **`end < start`** (the due date is under 8 days out when logged/chained): the FULL
  amount lands on day 1 (`start`) — do not invent a different split for a short fuse.
- **Even split:** otherwise divide the total evenly across `start..end` inclusive, in
  cents, distributing any rounding remainder across the first few days so the days sum
  EXACTLY to the total (never let rounding silently lose or gain a cent).
- **Storage:** write per-day amounts into `daily_targets` in the ledger — ISO date keys
  → `{total, calendar_event_id, contributions: [{bill_id, amount, status: pending}]}`. A
  day that already holds other lines' contributions gets its `total` RECOMPUTED (sum of
  all that day's contributions), never overwritten/clobbered.
- **Undated → no ramp.** Never guess a date to force one.

## OVERLOAD CHECK — the brake on the ramp (added 2026-08-10)
The ramp will happily stack days past what any week can carry, and rollover compounds
it. Before writing a day's `daily_targets`, compare the resulting 7-day set-aside total
against the trailing 4-week average of logged income (skip this check entirely while the
income log holds fewer than 7 entries — say so rather than computing against nothing).

If the coming week's set-aside total exceeds that average, **still write the ramp
exactly as computed** — never quietly shrink, delay, or drop a line to make the number
look achievable — and additionally:
- Flag it on the dashboard: "⚠️ this week's set-aside is $X against a $Y average week."
- Raise ONE #decisions parent naming the gap in dollars and listing the dated lines
  inside the window, so Lemar decides what moves. You never decide which bill slips.
- Include `overload $X vs $Y` in your PART M return token.

A number Lemar can't hit is still the true number. The failure mode this guards against
is a cheerful dashboard, not an ugly one.

## ROLLOVER — end of day (runs inside PART M, last hourly scan of the day)
On Samira's LAST hourly scan of the day (≥5pm ET — same style as the existing PART C
timing gate, so this never fires mid-morning): for every `daily_targets[today]`
contribution still `status: pending`, flip it to `rolled` and add its amount into
`daily_targets[tomorrow]` (create tomorrow's entry/event if it doesn't exist yet), then
update BOTH days' aggregate events (today's total drops by what rolled, tomorrow's
total gains it). Never touch a contribution already `paid` — a payment always wins over
a rollover. This is a mechanical daily housekeeping step, not a "mark paid" — it never
assumes anything got paid, it only moves an un-acted-on target forward one day so
nothing silently disappears.

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
- `day: null` or `due: null` → NO event (and no ramp — see RAMP); the gap rides in
  `open_questions` until Lemar supplies the date. Never guess a date.
- Paid / parked / done → cancel the event and clear the id (RETIRE). An amount or date
  change → update the existing event, never a duplicate (EXISTING).
- The four pre-hub events (Claude, Wispr Flow, Patreon, T-Mobile) are adopted — their
  ids already sit in the ledger; update or retire them through the ledger like any
  other row, never recreate them.
- The DAILY aggregate "set aside today" events are a SEPARATE parallel layer on the
  personal calendar — a bill having both its own due-date event and one or more days'
  worth of ramp contribution inside an aggregate event is expected, not a duplicate.

## DAILY CALENDAR — one aggregate "set aside" event per day
The "how much to set aside today" layer; the due-date event is still "what's actually
due." Personal reminder calendar only, no attendees, popup reminder (`minutes: 0`).
- Title: `Set aside today: $<daily_targets[date].total>`. Description lists each
  contributing line + amount, flagging anything carried in from a missed day ("rolled
  from `<date>`") and naming the pocket move: Spending → Set-Aside.
- A day's total changing (new bill lands on it, a payment clears part of it, a rollover
  adds to it) updates THAT SAME event — reuse `daily_targets[date].calendar_event_id`,
  never create a duplicate for a date that already has one (EXISTING).
- A day whose total reaches $0 (every contribution `paid` or moved off it) → cancel its
  event and clear the id (RETIRE) — never leave a stale $0 reminder.

## DASHBOARD — the Money Hub artifact
One self-contained HTML page (inline CSS, no external requests, single column
phone-first, light/dark via `prefers-color-scheme` + `[data-theme]` overrides; load the
`artifact-design` and `dataviz` skills before building). `<title>Money Hub</title>`,
favicon 💵, "rendered HH:MM ET" stamp. Re-deploy to the stable URL in anchors (pass it
as `url`). Sections, top to bottom, every number traceable to the ledger, the log, or
Era:
1. **Set aside today** — `daily_targets[today].total` as the biggest number on the
   page, the contributing lines beneath it, and the one instruction: move it from
   Spending to Set-Aside. This is the point of the page; nothing outranks it.
2. **The two pockets** — Spending and Set-Aside balances from Era with as-of stamps,
   plus reported cash on hand. Era data-health flags rendered honestly (⚠️ chip) with
   the true as-of date, never a friendlier one.
3. **The queue — next 14 days** — every dated line, soonest first, with a running total
   so Lemar can see where the money runs out.
4. **NO DATE — not being tracked** — every active line with no date, stated as a defect:
   these are invisible to the queue and will never ring. Each one is a question.
5. **This week** — the latest run's numbers: income logged vs. what the next 7 days
   need. No run yet this week → "say 'run my week'".
6. **Goals** — target, saved, target date, and the weekly number it implies. A goal with
   no target date is listed under section 4, not here.
7. **Spending snapshot** — Era categories/cash-flow when available; until SoFi is
   reconnected, one honest "reconnect SoFi at era.app to unlock" line.
8. **Open questions** — the ledger's `open_questions`, verbatim.

## PART M (inside Samira's scan)
Sweep #personal-finance since the last run. A money drop is Lemar reporting earnings,
cash, a bill (text or photo), a payment, or plan terms — the same scanner discipline as
on-button-plan: ignore restatements, your own 🌐 posts, and reacted messages. Run the
matching mode per drop; anything ambiguous or material (a figure to confirm, a missing
date, a business-vs-personal call) → leave it `null`/flagged and raise ONE #decisions
parent — never guess. Every new/updated line with a date also gets its RAMP computed and
its DAILY CALENDAR event(s) created/updated in the same pass, then the OVERLOAD CHECK.
On the LAST hourly scan of the day (≥5pm ET) also run ROLLOVER before re-rendering.
Re-render the dashboard once at the end ONLY if something changed. PART M captures,
ramps, checks, and renders; it never runs the weekly view (mode 6 stays on-demand).

## SAFETY (applies to the whole skill)
You MAY: read and write the two Money notes' data blocks + Update sections (including
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
`money ✓ <what changed — e.g. +1 bill · earnings +$140 · today $X · undated N ·
overload $X vs $Y · rolled $Y> · hub ✅/⚠️` — or `money —` when the sweep found nothing.

## Worked example
Lemar drops in #personal-finance: "New bill, car insurance $182 a month on the 15th.
Also made $210 doordashing this weekend." PART M: (1) adds
`{id: car-insurance, amount: 182, cadence: monthly, day: 15}` to the ledger — it has a
date, so it queues; creates the recurring event `Bill: Car insurance — $182` on the 15th
with both popups and stores the id; computes its ramp (`end` = 15th − 7 days; if today
falls before that, $182 splits evenly across `start..end`, else the full $182 lands on
`start`) and creates/updates the matching `daily_targets` day(s). (2) Appends
`{date: <sat>, source: doordash, amount: 210}` to the income log. (3) Runs the OVERLOAD
CHECK: if the coming week's set-aside now exceeds the trailing 4-week average income, it
writes the ramp anyway and raises one #decisions parent naming the gap. (4) Touches
`updated`, appends one `## Update` line, commits
`money-hub: +car-insurance bill, +$210 earnings, ramp $26/day`, re-renders the hub,
returns `money ✓ +1 bill · earnings +$210 · today $26 · undated 6 · hub ✅`. Later Lemar
says "run my week": the 14-day queue is sorted by date, the next 7 days summed against
income logged, the gap stated in dollars with the exact line the money stops at, the
table lands in the ledger, #personal-finance, and the dashboard. If 5pm ET arrives with
today's `car-insurance` contribution still `pending`, ROLLOVER flips it to `rolled` and
folds it into tomorrow — and if that's its third straight roll, a #decisions parent says
so. Nothing paid, nothing contacted.
