---
created: 2026-08-03T14:10-04:00
updated: 2026-08-03T14:10-04:00
domain: project
type: brief
status: awaiting-decision
tags: [samira, skill-forge, decision-loopback]
source: slack
---

# Skill spec — decision-loopback

Forged by skill-forge as the first live test of PART H. Proposal quarantined at
`.claude/skills-proposed/decision-loopback/`; not runnable until Lemar's ✅.

## What recurs

A #decisions card closes (Lemar reacts with his pick), but the resolution never gets
posted back to the project channel that raised it. A much later scan notices the silence
and back-fills a "this closed on [date] but never got looped back here" message. The
origin channel spends days believing the question is still open.

Three dated occurrences, all from the 2026-07-31 PART H sweep
([[#skills-lab ts 1785517930.308179]]):

1. **2026-07-20** — `#pitch-deck-pressure-test`, Q1 valuation/stake. Closed in #decisions
   7/20; looped back only when the 7/31 scan caught it.
2. **2026-07-11** — `#cuzzys-brand`, brand-name decision. Closed 7/11, looped back 7/11
   but logged explicitly as a backfill, not a same-scan close.
3. **2026-07-20** — `#delivery-in-a-box`, G Factory / Loud House outreach. Closed 7/20,
   backfilled later.

This is an execution gap, not a missing instruction: PART G already says "when fulfilled,
post the outcome back to the project channel and close." It says to do it and it
demonstrably is not happening, which is exactly the shape a skill fixes — the runbook
names the obligation, the skill carries the procedure.

## Inputs / outputs

- **Reads**: closed #decisions cards (Lemar's ✅ on an option, or 🫡), the card's origin
  citation, the Haven outcome note samira-report-result just wrote, and the origin
  channel's recent messages (to check a notice isn't already there).
- **Writes**: ONE short closure notice in the origin project channel — title, the pick,
  one line on what happens next, the Haven note path, a link back to the #decisions thread.
- **Timing**: the SAME scan the reaction is read, in PART A, not N scans later. That
  immediacy is the entire point of the skill.

## Surfaces

Origin project channels only (`#pitch-deck-pressure-test`, `#cuzzys-brand`,
`#delivery-in-a-box`, `#comedy-club`, `#trading-cards`, `#free-books-partnership`,
`#booking-agent`, `#personal-finance`, and any future project channel). It never posts to
#decisions, #reports, the capture DM, or #stormy.

## Safety envelope

Fully inside Samira's existing floor — posting to a project channel is already permitted
("post to #reports / #decisions / the loop channels per their skills") and PART G already
directs this exact message. It sends nothing outward, moves no money, touches no
permissions, and sets no reaction of Lemar's. Its own idempotency key is its posted
notice, found by re-reading the channel — never a reaction.

## Chains with

`samira-report-result` (the outcome note must exist first — the notice links it), PART A
(where it fires), PART G (whose obligation it discharges).

## Owner

Samira, unattended, once promoted. No human step in the loop — the decision was already
made when Lemar reacted; this only carries the news.

## Sources
- slack: #skills-lab (`C0BBZ5J8805`) ts `1785517930.308179` — the original candidate post,
  including the line "Not built this run per the safety floor (no skill creation mid-run)"
- `.claude/routines/samira-atlas-executor.md` PART G — the standing obligation
- Proposal: `.claude/skills-proposed/decision-loopback/SKILL.md`
