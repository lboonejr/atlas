---
created: 2026-07-15T18:15-04:00
updated: 2026-07-16T14:00-04:00
domain: project
type: note
status: active
tags: [booking-agent, barbers, tattoo-artists, side-project, saas-idea]
source: slack
---

# Booking agent for barbers, tattoo artists, etc — new project idea

Lemar wants to develop a booking-management agent aimed at barbers, tattoo artists, and
similar appointment-based independent service providers — a side project separate from
Cuzzie's/The Station.

Raw capture from #atlas: "As another project, atlas I would like to develop a booking
agent. where it helps barbers, tattoo artists, etc manage their bookings."

No scope, timeline, or business model attached yet — this needs a probe pass before it
can move to a project brief: target customer (solo operators vs. shops?), core feature
set (calendar sync, reminders, deposits/no-show fees, client history?), build-vs-buy
(custom agent vs. wrapping an existing scheduling tool), and whether this is a "someday"
idea (Stormy territory — no deadline, needs pressure-testing) or something Lemar wants
moving now (Shortlist/Atlas territory).

## Next step
Probe with Lemar: why now, target outcome, scope, and whether to route this through
Stormy's idea-pressure-test (15-question instrument) given it has no stated timeframe.

## Update 2026-07-16 — decision: active project, new channel
Lemar reacted ✅ on "Option 2 — Active project: start now, probe scope/customer/features
under Shortlist/Atlas and get a brief moving this week" on the #decisions card (message
ts `1784203926.276169`, option reply ts `1784203931.637699`), and added free-form:
"Let's just make sure we put it in a new channel."

Decision: this is now an active project, not a Stormy someday-bake. Created a dedicated
Slack channel per his ask — `#booking-agent` — for this project to live in going forward.
Next actual step (still open, per the original probe): target customer, core feature
set, build-vs-buy, and a first brief draft — to be worked under Shortlist/Atlas in the
new channel, not this scan.

## Update 2026-07-16 — scope answers from Lemar in #booking-agent
Lemar answered the open probe questions directly in the new project channel (14:00:29 ET):
"I think we start off with solo operators. All of the core features that you mentioned
there and we'll build it versus buy."

- Target customer: **solo operators** (not shops, at least to start)
- Core feature set: **all of it** — calendar sync, reminders, deposits/no-show fees,
  client history (the full set originally listed in the probe)
- Build-vs-buy: **build** (custom agent, not wrapping an existing scheduling tool)

This closes the three open scope questions from the 07-15 probe. Remaining open step:
turn this into a first project brief (per the 07-16 decision: "brief moving this week")
— this is Lemar's own project so no #decisions lift needed; next brief-drafting pass
belongs to Shortlist/Atlas working this channel.

## Update 2026-07-18 — first project brief draft (PART G, worked in-channel)

Scope answers from 7-16 are locked (solo operators, full feature set, build not buy), so
drafting the first brief now rather than leaving the "brief moving this week" step open
another day.

**Mission:** A booking-management agent for solo appointment-based service providers
(barbers, tattoo artists, and similar one-person shops) — calendar sync, reminders,
deposit/no-show fee handling, and client history in one place, built (not bought/wrapped).

**Target user:** Solo operators first — one calendar, one book of clients, no multi-staff
scheduling logic needed for v1.

**MVP feature set (all four, per Lemar's 7-16 answer):**
1. Calendar sync (two-way, at least one major calendar provider to start)
2. Automated reminders (client-facing, reduces no-shows)
3. Deposits / no-show fees (payment collection tied to booking)
4. Client history (repeat-client notes, past services, preferences)

**Build vs. buy:** Build custom — not a wrapper on an existing scheduler. Biggest
implication: payment collection (deposits/no-show fees) means a payment processor
integration (Stripe or similar) from day one, which is real scope, not a v2 add-on.

**Open questions before this can become a real dev plan:**
- Which calendar provider(s) to sync first (Google Calendar likely, given the rest of
  this workspace already runs on it)?
- Payment processor preference, or defer to whoever's cheapest/fastest to integrate?
- Is this a tool Lemar uses personally first (dogfood with one real operator — e.g. the
  friend mentioned in the original capture) before opening it to anyone else, or built
  generic from the start?
- Timeline expectation now that scope is build-not-buy — "this week" for the brief,
  but no date attached to an actual MVP yet.

**Not yet started:** no code, no accounts, no external commitments. This is a planning
brief only — Lemar's call on whether this stays a personal side-build or graduates to
something with real deadlines (in which case it may be worth a Stormy pressure-test pass
on the business model even though the scope/build decision is already made).

## Sources
- slack: #atlas 2026-07-15 18:15:39 ET, message ts 1784153739.693329 (channel C0BBWHCJUV9)
- slack: #decisions 2026-07-16 08:12:06 ET, probe card ts 1784203926.276169 (channel C0BBXA96FFV)
- slack: #booking-agent 2026-07-18, brief posted this pass (channel C0BHXTPST52)
- slack: #decisions 2026-07-16 08:26:44 ET, Lemar's free-form reply ts 1784204804.434019 ("let's just make sure we put it in a new channel")
- slack: #booking-agent 2026-07-16 14:00:29 ET, scope-answers message ts 1784224829.576589 (channel C0BHXTPST52)
