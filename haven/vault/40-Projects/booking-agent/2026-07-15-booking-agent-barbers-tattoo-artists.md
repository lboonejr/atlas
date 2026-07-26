---
created: 2026-07-15T18:15-04:00
updated: 2026-07-26T13:45-04:00
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

## Update 2026-07-23 — answers to the 3 open brief questions (PART G, worked in-channel)

Lemar answered all three open questions from the 07-18 brief directly in #booking-agent
(2026-07-22 ~19:14 ET, thread on the brief post):

1. **Calendar provider:** Google Calendar — matches the rest of the workspace.
2. **Payment processor:** defer to whoever's fastest/cheapest to integrate (Stripe or
   similar) — no hard preference.
3. **Dogfood plan:** yes — test with the tattoo-artist friend from the original capture,
   specifically because he's tech-averse and still tracks appointments by hand. Lemar's
   framing: "I want to make such a simple and easy solution anyone could use it" — this
   sets the actual usability bar (a tech-averse solo operator has to be able to run it),
   not just a feature checklist.

This closes all three open questions from the 07-18 brief. Nothing built yet — still a
planning-stage project. Next step (not started this pass): turn the locked scope +
dogfood plan into a build-sequencing outline, Lemar's own project, no #decisions lift
needed.

## Update 2026-07-25 — build-sequencing outline posted (PART G, worked in-channel)

Lemar pinged directly in #booking-agent ("can we proceed with the next step?", ts
`1784980354.978559`) — this is the "build-sequencing outline" step flagged open on
07-23. Posted a six-phase sequencing outline in-channel (ts `1784981661.406349`), still
his own project so no #decisions lift:

1. Foundations — account model, client/appointment schemas, Google OAuth wiring
2. Calendar sync core — two-way Google Calendar sync, timezone + conflict handling
3. Reminders — configurable-window client reminders with confirm/reschedule/cancel link
4. Payments — deposit/no-show fee processor integration (fastest/cheapest, e.g. Stripe)
5. Client history — notes, past services, preferences
6. Dogfood pilot — live test with the tattoo-artist friend (tech-averse = the real
   usability bar); ready-to-expand marker is a full month of real bookings without
   hand-holding

Nothing built or accounts opened — sequencing plan only. Next actual step (Phase 1
build) is Lemar's call to kick off. (Phase 1 was greenlit 2026-07-25, spec doc built —
see `2026-07-25-phase1-foundations-design.md`.)

## Update 2026-07-26 — potential dogfood/pilot lead surfaced (PART G, worked in-channel)

Lemar dropped a new lead in #booking-agent (ts `1785081105.504179`, ~11:51 ET):
"I found someone that wants to do the booking agent, a young guy that does independent
mechanic work." No reaction/reply on it yet — first pass on this pass.

This is new project context, not a decision needing a #decisions lift (matches the
established pattern for this channel — scope/pilot questions get worked in-channel,
same as the 07-23 and 07-25 updates above). It's ambiguous whether "wants to do the
booking agent" means (a) a candidate to swap in for or add alongside the tattoo-artist
friend as the Phase 6 dogfood pilot, or (b) just a second solo-operator vertical
(independent mechanics) to keep in mind post-launch. Posted a clarifying question
in-channel rather than guessing which; nothing else changes in the build sequence —
Phase 1 (Foundations) design spec already stands as the last completed step.

## Update 2026-07-26 (13:45 ET) — replanned build sequence around mechanic basic-tier pilot (PART C)

Lemar confirmed the mechanic lead is the Phase 6 dogfood pilot (swapping in for the
tattoo-artist friend, logged same day) and then set a scope change directly in-channel
(ts `1785086527.751709`): the mechanic's pilot version keeps reminders but **drops
payments/deposits** — his dogfood build is calendar sync + client/appointment tracking +
reminders only. In parallel, the full-featured build (deposits/no-show fees, deeper
client history) continues on its own track. End goal, per Lemar: package this as a
**tiered product** — a Basic Tracker tier and a Full-Featured tier — once both are
proven out. He asked directly: "can you replan the build sequence around this (basic
tier scope + parallel full-build track) and flag what changes in the phase order?"

**Replanned sequence:**

1. **Foundations** — unchanged, already done (spec: `2026-07-25-phase1-foundations-design.md`).
2. **Calendar sync core** — unchanged, next up.
3. **Reminders** — unchanged.
4. **Basic-tier dogfood pilot (NEW — moved up from old Phase 6)** — once Phases 1–3 are
   built, freeze that as the Basic tier (calendar sync + client/appointment tracking +
   reminders, no payments) and ship it live to the mechanic. This is the biggest order
   change: the pilot no longer waits on Payments or Client History — it only needs
   Phases 1–3, so it moves up four steps in the old sequence.
5. **Two parallel tracks, starting once the basic pilot is live:**
   - **Track A — Basic tier hardening:** iterate on Phases 1–3 against real mechanic
     usage; watch for friction (same tech-averse usability bar Lemar set 07-23).
   - **Track B — Full-featured build (old Phases 4–5, unblocked, continues independently):**
     Payments (deposit/no-show fee processor integration) and Client History depth.
     These no longer gate the first live pilot — they now build toward the
     Full-Featured tier instead.
6. **Tiered packaging (renamed from old Phase 6 "Dogfood pilot," which is now step 4
   above)** — once Track A clears its ready-to-expand marker (a full month of real
   mechanic bookings without hand-holding) and Track B completes Payments + Client
   History, package the two as a tiered product: Basic Tracker tier vs. Full-Featured
   tier.

**What changed vs. the 07-25 outline:** the dogfood pilot moves from last (old Phase 6)
to right after Reminders (new step 4), because the Basic tier scope no longer includes
Payments or Client History. Payments and Client History (old Phases 4–5) are unblocked
from gating the pilot and instead become the parallel Full-Featured track.

**Open flag, not yet answered:** whether the tattoo-artist friend still dogfoods the
Full-Featured track once Track B is ready, or whether that dogfood role is now fully
open — not guessed here, can be answered whenever Lemar has a view.

Posted this replan back to #booking-agent (no #decisions lift — Lemar's own project,
matches the established pattern). Nothing built or accounts opened.

## Sources
- slack: #atlas 2026-07-15 18:15:39 ET, message ts 1784153739.693329 (channel C0BBWHCJUV9)
- slack: #decisions 2026-07-16 08:12:06 ET, probe card ts 1784203926.276169 (channel C0BBXA96FFV)
- slack: #booking-agent 2026-07-18, brief posted this pass (channel C0BHXTPST52)
- slack: #decisions 2026-07-16 08:26:44 ET, Lemar's free-form reply ts 1784204804.434019 ("let's just make sure we put it in a new channel")
- slack: #booking-agent 2026-07-16 14:00:29 ET, scope-answers message ts 1784224829.576589 (channel C0BHXTPST52)
- slack: #booking-agent 2026-07-22 ~19:14 ET, brief-question answers ts 1784574891.283109 (channel C0BHXTPST52, thread 1784383950.961519)
- slack: #booking-agent 2026-07-25, "can we proceed with the next step?" ts 1784980354.978559; build-sequencing outline posted ts 1784981661.406349 (channel C0BHXTPST52)
- slack: #booking-agent 2026-07-26 ~11:51 ET, mechanic-lead message ts 1785081105.504179 (channel C0BHXTPST52)
- slack: #booking-agent 2026-07-26 ~13:42 ET, scope-change/replan-request message ts 1785086527.751709 (channel C0BHXTPST52)
