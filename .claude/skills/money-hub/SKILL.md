---
name: money-hub
description: >
  Lemar's personal financial hub: report earnings and cash, post bills (typed or from a
  photo), set up payment plans, and get the week's money split. Source of truth is the
  Haven ledger note haven/vault/10-Personal/Money/money-hub-ledger.md (bills, pockets,
  plans, goals, allocation config, and the daily set-aside ramp) plus the income log;
  the Money Hub dashboard artifact and the reminder-calendar events (including the ONE
  daily "set aside today" aggregate event) are regenerated FROM the ledger, never
  hand-edited. The allocation engine implements the locked Option 3 hybrid floor +
  waterfall (2026-07-24) and only advises — Lemar moves the money himself. Trigger on:
  "log earnings", "made $X today", "doordash paid me", "I have $X cash", "new bill:", a
  bill photo or payout screenshot, "payment plan:", "run my week", "how should I split
  this", "what do I delegate", "paid the [bill]", "show me the money hub", "money hub",
  "rebuild the money hub". Also invoked by Samira's PART M for money drops in
  #personal-finance. This skill NEVER moves money, never pays anyone, never contacts a
  creditor or biller, never sends email or outreach, and never invents a number — an
  unknown stays null and gets asked.

---

# Money Hub — earnings, bills, pockets, and the weekly split

You run Lemar's personal budgeting center. One ledger, three renderings: the Haven
ledger note is truth; the Money Hub dashboard artifact and the reminder-calendar events
(per-bill due-date events AND the daily "set aside today" aggregate) are projections of
it; Era Context is the read-only live layer for connected-account balances and
spending. Runs live ("run my week") or inside Samira's scan (PART M). Every Safety rule
in the runbook applies; add the guards below.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it first. You use: the
**Money Hub artifact URL** (Money Hub section), the **reminder calendar ID** (Google
Calendar section), **#personal-finance** `C0BGLEMH99T`, and the git-write policy
(commit straight to `main`; prefix `money-hub:`). Vault outcome notes go through
**samira-report-result** when running inside Samira.

## THE SOURCE OF TRUTH — one ledger, one log
- **`haven/vault/10-Personal/Money/money-hub-ledger.md`** — bills, pockets, payment
  plans, goals, cash on hand, allocation config, the daily set-aside ramp
  (`daily_targets`), open questions, all in ONE fenced `yaml` block. Field rules live
  at the top of that note: amounts plain numbers, `null` = unknown (never invent),
  dedupe by `id`, never delete a line (flip `status`), the allocation SHAPE is locked
  (Option 3), the floor DOLLAR figure is computed from active monthly p1/p2/p4 bills ÷
  4.33.
- **`haven/vault/10-Personal/Money/income-log-2026.md`** — append-only earnings lines.

Editing these blocks + touching `updated` is a sanctioned machine write (the
on-button-plan pattern). Material changes and every allocation run also append an
`## Update YYYY-MM-DD` section to the ledger — yaml holds state, Updates hold history.

## MODES

**1. Log earnings** — "made $140 today", "log earnings 140", "doordash paid me $95", or
a payout screenshot. Append `{date, source, amount, note}` to the income log (date =
the day earned if stated, else today, ET). From a screenshot, read the amount and date
off the image and CONFIRM with Lemar before writing if either is unclear. Re-render the
dashboard.

**2. Report cash** — "I have $X cash / on hand". Set `cash_on_hand: {amount, as_of}` in
the ledger. Re-render.

**3. Add bill** — "new bill: car insurance $180 on the 15th", or a photo of a bill.
From a photo, extract payee, amount, due date / billing day, and any account reference;
show Lemar what you read and get a confirmation before writing (a misread bill poisons
every downstream number). Dedupe by `id` / payee+account against the ledger — an
existing matter gets UPDATED (latest figure, annotate), never a sibling line. Assign
`priority` only when it's obvious from the ledger's existing pattern; otherwise leave
`priority: null` and ask. Then project it onto the calendar (see CALENDAR) AND compute
its set-aside ramp (see RAMP) before re-rendering.

**4. Set up a payment plan** — "payment plan: [creditor] $600 total, 4 payments of $150
starting Friday". Write a `plans` entry: `{id, creditor, total, note, installments:
[{seq, amount, due, status: pending, calendar_event_id: null}]}`. Every installment
gets its own reminder event (see CALENDAR) AND its own set-aside ramp (see RAMP,
computed per-installment against that installment's `due`). If the math doesn't close
(installments ≠ total), say so and ask rather than adjusting a figure yourself.
Re-render.

**5. Run my week** — "run my week", "how should I split this", "what do I delegate".
On demand only, never scheduled (Lemar's call, 2026-08-05).
- **Inputs:** this week's income-log entries (Mon–Sun, ET) + `cash_on_hand` + bills and
  installments due in the next 7 days + live Era Context balances
  (`accounts__list_financial_accounts`; render a ⚠️ chip if unreachable).
- **Engine — the locked Option 3 shape:** compute the weekly floor (active monthly
  p1/p2/p4 bills ÷ 4.33, plus any one-time p1/p2/p4 item due THIS week). Fund the floor
  off the top in priority order (p1 → p2 → p4). If the week's money doesn't cover the
  floor, fund in order as far as it goes and state plainly what's unfunded and rolls
  forward — the locked logic defines no other fallback, so never invent one. Whatever
  remains waterfalls `p5 → p6 → p7`, each pocket funded toward its goal in full before
  the next sees anything.
- **Output — the delegation table:** one row per pocket: "move $X → [pocket] ([what it
  covers])", then the week's due bills with dates, then income vs the $500 target.
  Advisory only; Lemar makes the transfers. Append the table as an `## Update` to the
  ledger, post it to #personal-finance (when running with a Slack surface), re-render
  the dashboard.

**6. Mark paid** — "paid the Claude bill", "installment 2 of [plan] paid", or a payment
confirmation (text or photo) in #personal-finance. Flip the line's `status` to `paid` (a
monthly bill just gets a dated note — it recurs), retire a one-time item's or
installment's calendar event (see CALENDAR), and when a plan's last installment pays,
mark the plan done. **Ramp side-effect:** flip that bill's `pending`/`rolled`
`daily_targets` contribution(s) to `paid`, subtract the paid amount from whichever
day(s) it was sitting in and update those days' aggregate events, and RETIRE the rest
of that bill's future ramp days — a full payment clears the remaining schedule for that
bill, so recompute every future day it was touching (a day whose total then reaches $0
across all contributions gets its own event cancelled and its id cleared). Re-render.

**7. Show / rebuild the hub** — "show me the money hub", "money hub", "rebuild the
money hub". Re-render the dashboard from current ledger + log + Era state and hand back
the artifact URL.

## RAMP — even daily set-aside (extends Mode 3 + the recurring-bill path)
Every bill/expense that gets a due date should turn into an even daily savings target,
so Lemar sees ONE combined "set aside today" number instead of tracking each bill
separately.

- **Window:** `start` = the day after the bill is logged (for a recurring bill's LATER
  cycles — i.e. every occurrence after the first — `start` = the day after the PRIOR
  cycle's due date, so cycles chain with no gap). `end` = the due date minus 7 days.
- **`end < start`** (the due date is under 8 days out when logged/chained): the FULL
  amount lands on day 1 (`start`) — do not invent a different split for a short fuse.
- **Even split:** otherwise divide the total evenly across `start..end` inclusive, in
  cents, distributing any rounding remainder across the first few days so the days sum
  EXACTLY to the total (never let rounding silently lose or gain a cent).
- **One-time backfill:** run this once for any bill ALREADY in the ledger that carries a
  future `due` (not yet ramped). If today falls inside the computed window, use today as
  `start` instead of "the day after logged" (the ramp can't reach into the past).
  Recurring monthly bills (day-of-month only, no explicit `due`) are NOT auto-backfilled
  by this pass — only ramp a recurring bill's cycle when it is freshly added/chained, to
  avoid inventing a "logged" date for bills that have existed for weeks.
- **Storage:** write per-day amounts into `daily_targets` in the ledger — ISO date keys
  → `{total, calendar_event_id, contributions: [{bill_id, amount, status: pending}]}`. A
  day that already holds other bills' contributions gets its `total` RECOMPUTED (sum of
  all that day's contributions), never overwritten/clobbered.

## DAILY CALENDAR — one aggregate "set aside" event per day
Separate from each bill's own due-date event (see CALENDAR below) — this is the "how
much to set aside today" layer, the due-date event is still "what's actually due."
- Reminder calendar only (ID in anchors), no attendees, popup reminder (`minutes: 0`,
  matching the existing all-day bill-event convention).
- Title: `Set aside today: $<daily_targets[date].total>`. Description lists each
  contributing bill + amount, flagging anything carried in from a missed day ("rolled
  from `<date>`" — see ROLLOVER).
- A day's total changing (new bill lands on it, a payment clears part of it, a rollover
  adds to it) updates THAT SAME event — reuse `daily_targets[date].calendar_event_id`,
  never create a duplicate for a date that already has one (EXISTING, same doctrine as
  haven-calendar-sync).
- A day whose total reaches $0 (every contribution `paid` or moved off it) → cancel its
  event and clear the id (RETIRE) — never leave a stale $0 reminder.

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

## CALENDAR — projection, never truth
Reminder calendar ONLY (ID in anchors), no attendees, popup reminder on; the ledger
wins every conflict; every event id is written back to its ledger row so nothing is
ever double-booked (haven-calendar-sync's law, managed here because bills and
installments are many-per-note):
- Monthly bill with a known `day` → ONE recurring event (RRULE FREQ=MONTHLY;
  BYMONTHDAY=day), title `Bill: <name> — $<amount>`.
- One-time bill / plan installment with a `due` → one event, title
  `Bill: <name> — $<amount>` or `Plan: <creditor> <seq>/<N> — $<amount>`.
- `day: null` or `due: null` → NO event (and no ramp — see RAMP); the gap rides in
  `open_questions` until Lemar supplies the date. Never guess a date.
- Paid / parked / done → cancel the event and clear the id (RETIRE). An amount or date
  change → update the existing event, never a duplicate (EXISTING).
- The four pre-hub events (Claude, Wispr Flow, Patreon, T-Mobile) are adopted — their
  ids already sit in the ledger; update or retire them through the ledger like any
  other row, never recreate them.
- The DAILY aggregate "set aside today" events (see DAILY CALENDAR above) are a
  SEPARATE parallel layer on the same calendar — a bill having both its own due-date
  event and one or more days' worth of ramp contribution inside an aggregate event is
  expected, not a duplicate.

## DASHBOARD — the Money Hub artifact
One self-contained HTML page (inline CSS, no external requests, single column
phone-first, light/dark via `prefers-color-scheme` + `[data-theme]` overrides; load the
`artifact-design` and `dataviz` skills before building). `<title>Money Hub</title>`,
favicon 💵, "rendered HH:MM ET" stamp. Re-deploy to the stable URL in anchors (pass it
as `url`); if still a placeholder, publish fresh and write the URL back to anchors once.
Sections, top to bottom, every number traceable to the ledger, the log, or Era:
1. **Cash position** — Era balances per account with as-of stamps + reported cash on
   hand; Era data-health flags rendered honestly (⚠️ chip), never papered over.
2. **This week** — the latest delegation table + income this week vs the $500 target.
   No run yet this week → "say 'run my week'".
3. **Today's set-aside** — `daily_targets[today].total` (if any) with the contributing
   bills, so the single combined number is the first thing Lemar sees for today.
4. **Upcoming bills (14 days)** — bills + installments, soonest first; unknown-day
   bills listed in a "no date yet" strip.
5. **Payment plans** — per plan: paid n of N, remaining balance, next due.
6. **Spending snapshot** — Era categories/cash-flow when available; until SoFi is
   reconnected, one honest "reconnect SoFi at era.app to unlock" line.
7. **Goals** — target vs saved per goal.
8. **Open questions** — the ledger's `open_questions`, verbatim, so they stay visible
   until killed.

## PART M (inside Samira's scan)
Sweep #personal-finance since the last run. A money drop is Lemar reporting earnings,
cash, a bill (text or photo), a payment, or plan terms — the same scanner discipline as
on-button-plan: ignore restatements, your own 🌐 posts, and reacted messages. Run the
matching mode per drop; anything ambiguous or material (a figure to confirm, an
unassigned priority) → leave it `null`/flagged and raise ONE #decisions parent — never
guess. Every new/updated bill with a `due` also gets its RAMP computed and its
DAILY CALENDAR event(s) created/updated in the same pass (Mode 3's ramp step, not a
separate sweep). On the LAST hourly scan of the day (≥5pm ET) also run ROLLOVER before
re-rendering. Re-render the dashboard once at the end ONLY if something changed. PART M
captures, ramps, and renders; it never runs the weekly split (mode 5 stays on-demand).

## SAFETY (applies to the whole skill)
You MAY: read and write the two Money notes' data blocks + Update sections (including
the `daily_targets` block); append to the income log; create/update/cancel events on
the reminder calendar (both per-bill due-date events AND the daily aggregate "set aside
today" events) and write ids back; read Era Context; re-deploy the Money Hub artifact
(+ the one-time anchors URL write-back); post money-hub output to #personal-finance and
raise #decisions cards when running inside Samira; commit to `main`.
You MUST NOT, ever: move money, make a payment or transfer, or tell any surface a
payment happened that Lemar didn't report; contact any creditor, biller, or lender;
send email or any outreach; invent, round into existence, or guess a number, date, or
priority (unknown stays `null` + an ask); redesign the locked allocation shape; edit
history (prior Updates, prior log lines); write any other vault note's body; touch any
calendar other than the reminder calendar; add attendees to any event; mark a
`daily_targets` contribution `paid` except as the direct side-effect of Mode 6 (a
rollover only ever sets `rolled`, never `paid`).

## Returns (to the Samira runbook, for the digest)
`money ✓ <what changed — e.g. +1 bill · earnings +$140 · split run · ramp $X/day ·
rolled $Y> · hub ✅/⚠️` — or `money —` when the sweep found nothing.

## Worked example
Lemar drops in #personal-finance: "New bill, car insurance $182 a month on the 15th.
Also made $210 doordashing this weekend." PART M: (1) adds
`{id: car-insurance, amount: 182, cadence: monthly, day: 15, priority: null}` to the
ledger — priority isn't obvious, so it raises one #decisions parent asking which
priority it belongs to; creates the recurring event `Bill: Car insurance — $182` on the
15th and stores the id; this is a fresh monthly line so its ramp gets computed for the
upcoming 15th too (`end` = 15th − 7 days; if today falls before that, the $182 splits
evenly across `start..end`, else the full $182 lands on `start`) and the matching
`daily_targets` day(s) get created/updated with a `car-insurance` contribution. (2)
Appends `{date: <sat>, source: doordash, amount: 210}` to the income log. (3) Touches
`updated`, appends one `## Update` line, commits
`money-hub: +car-insurance bill, +$210 earnings, ramp $26/day`, re-renders the hub,
returns `money ✓ +1 bill · earnings +$210 · ramp $26/day · hub ✅`. Later Lemar says
"run my week": floor computed ≈ $463 + the $265 T-Mobile line if due that week, income
summed from the log, the table lands in the ledger, #personal-finance, and the
dashboard. If 5pm ET arrives with today's `car-insurance` ramp contribution still
`pending`, ROLLOVER flips it to `rolled` and folds it into tomorrow's aggregate total,
updating both days' calendar events — no payment assumed, nothing paid or contacted.
