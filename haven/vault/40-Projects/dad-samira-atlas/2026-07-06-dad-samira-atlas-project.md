---
created: 2026-07-06T06:53:45-04:00
updated: 2026-07-17T16:45-04:00
domain: project
type: brief
status: active
tags: [samira, atlas, productization, dad, air-force, stormy]
source: slack
---

# Building a "Samira/Atlas" for others — starting with Dad

Lemar wants to help loved ones (and possibly sell to businesses) by building a
version of this Samira/Atlas system for other people, starting with his dad. Dad's
job is very different from Lemar's — he works on alarms on an Air Force base — so
the workflow this system would need to support is unknown yet.

This is the seed of a possible productized offering. Before a real plan can be built,
need Dad's actual workflow: what tools he already uses day-to-day (email, a work
order/ticketing system, radios, paper logs?), what's repetitive or error-prone in his
day, what he'd actually want automated vs. what needs a human, and whether he has any
software/security constraints given it's a military base (this alone could rule out
a lot of the current architecture — Slack/Gmail/Calendar/GitHub — if base IT policy
doesn't allow third-party cloud tools on work devices).

Probing questions posted back in the #atlas thread (2026-07-06) to start narrowing
this down before any architecture gets proposed.

## Update 2026-07-17 — onboarding job form idea (Samira capture DM)

Lemar dropped a concrete first step for productizing this: an onboarding intake form
(built in Jotform — already a connected tool) for any individual/business he wants to
bring AI help to (this project, and [[booking-agent]] as a live example). The form
would collect: their basic info + business info, what tools they already use (so a
Claude account can be wired to the right connectors), the issues they're dealing with
(to identify what to build), and their desired outcome (to tailor the build).

His stated goal: fill out the form once, then Lemar can "immediately start building it
using Samira's loop" straight from the answers — i.e. the form output becomes the raw
capture that feeds Gear 1 (Capture & Develop) for a brand-new person/business.

Raw capture (Samira capture DM, 2026-07-17 08:04 ET): "So to start my journey with
trying to help individuals and businesses leverage AI (i.e., think my booking agent or
bringing Samira to my dad), I basically want to start with an onboarding job for the
form... Basically the point of the job form is for me to just plug it straight into
Samira. Once it's completed by the individual or business, I can immediately start
building it using Samira's loop."

This is a no-deadline, multi-step idea — Stormy territory (same fork booking-agent hit
on 2026-07-15) — but Lemar hasn't said whether he wants it pressure-tested first or
built directly. Flagged to #decisions alongside the related capture below rather than
guessing which path he wants.

## Update 2026-07-17 (2) — related capture: "pressure tester" agent

Same session, a second capture (2026-07-16 ~21:00 ET, Samira capture DM): "I think we
should make an entirely new agent that's just a pressure tester. When I want to
pressure test an idea, I'll call this agent and then he'll start probing me... trying
to get details so that we can flesh everything out." This describes the **Stormy**
skill, which already exists in this repo (`.claude/skills/stormy/`) and already does
exactly this — a 15-question pressure-test instrument for no-deadline ideas. Flagged
to Lemar in the same #decisions card: does Stormy already cover what he's picturing,
and if so, does he want to run the onboarding-form idea above through it now?

## Update 2026-07-17 (3) — Option 1 picked: route through Stormy

Lemar reacted ✅ on Option 1 in the #decisions thread (message ts `1784290600.449469`):
"Run the onboarding-form idea through Stormy now ('stormy this idea'), confirm Stormy
is the pressure-tester you meant, bake it fully before any building starts." Decision
recorded — Stormy is confirmed as the pressure-tester agent Lemar was picturing, and
the onboarding-form idea above is the first thing to run through it.

Stormy's 15-question pressure-test instrument is a live Q&A session — this hourly scan
can log the routing decision but can't sit through the interview on Lemar's behalf.
Next step is his call: say "stormy this idea" (or "resume stormy") on this
onboarding-form idea whenever he's ready to sit through the pressure test.

## Update 2026-07-17 (4) — Stormy pressure test underway (PART Q)

Lemar confirmed in #decisions (ts `1784306179`, 12:36 ET): "I'm ready. Let's /stormy this
idea. Let's get it moving." Stormy dropped the seed into the private #stormy channel and
opened the 15-question pressure test this same hour:

- **Seed posted** in #stormy 16:09 ET (ts `1784318958.144999`) — restates the AI-onboarding
  intake form idea (Jotform basic-info/tools-in-use/pain-points/desired-outcome, feeds
  straight into Samira's build loop for a new person or business — dad, the booking-agent).
- **Q1 (Section A — Problem)** posted 16:11 ET (ts `1784319080.586059`). Lemar answered
  16:34 ET (ts `1784320495.581389`): the core problem is that operators/individuals
  struggle with day-to-day pieces of their job — booking-based businesses struggle managing
  bookings, lead-based jobs struggle finding leads, businesses struggle with inventory,
  individuals want better workflows generally. The jotform is the front door: it identifies
  the person/business and the specific problem before anything gets built.
- **Q2 + Q3 asked** this scan (~16:45 ET) — beneficiary scope (internal/family use only for
  now, vs. an explicit External partner/Customers productized play) and the first-version
  scope + hardest constraint (intake form alone vs. form + Lemar building the automation
  after, and what's most likely to slow it down). Awaiting Lemar's reply in #stormy; picked
  up and logged on the next PART Q scan.

Section A/B of the 15-point instrument in progress. No plan is locked yet — `status` stays
`active` (this note was already active pre-Stormy; the bake itself tracks via these Updates,
not a separate `awaiting-decision` note, per the append-not-duplicate rule since this is the
same matter as the existing dad-samira-atlas brief).

## Sources
- slack: #atlas 2026-07-06 06:53 ET
- slack: Samira capture DM (D0BHPKMDNEP) 2026-07-17 08:04:18 ET, ts 1784288658.057799 — onboarding job form idea
- slack: Samira capture DM (D0BHPKMDNEP) 2026-07-16 21:00:06 ET, ts 1784257206.265089 — "pressure tester" agent idea
- slack: #decisions message ts `1784290595.494019` (parent, probe card) / `1784290600.449469` (Option 1, ✅ picked)
- slack: #decisions ts `1784306179` — Lemar: "I'm ready. Let's /stormy this idea. Let's get it moving"
- slack: #stormy (C0BJ37SU1TL) ts `1784318958.144999` (seed drop) / `1784319080.586059` (Q1) / `1784320495.581389` (Lemar's Q1 answer) / `1784323007.567499` (Q2+Q3, this scan)
