---
created: 2026-07-06T06:53:45-04:00
updated: 2026-07-17T08:20-04:00
domain: project
type: brief
status: active
tags: [samira, atlas, productization, dad, air-force]
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

## Update 2026-07-17 — related capture: "pressure tester" agent

Same session, a second capture (2026-07-16 ~21:00 ET, Samira capture DM): "I think we
should make an entirely new agent that's just a pressure tester. When I want to
pressure test an idea, I'll call this agent and then he'll start probing me... trying
to get details so that we can flesh everything out." This describes the **Stormy**
skill, which already exists in this repo (`.claude/skills/stormy/`) and already does
exactly this — a 15-question pressure-test instrument for no-deadline ideas. Flagged
to Lemar in the same #decisions card: does Stormy already cover what he's picturing,
and if so, does he want to run the onboarding-form idea above through it now?

## Sources
- slack: #atlas 2026-07-06 06:53 ET
- slack: Samira capture DM (D0BHPKMDNEP) 2026-07-17 08:04:18 ET, ts 1784288658.057799 — onboarding job form idea
- slack: Samira capture DM (D0BHPKMDNEP) 2026-07-16 21:00:06 ET, ts 1784257206.265089 — "pressure tester" agent idea
