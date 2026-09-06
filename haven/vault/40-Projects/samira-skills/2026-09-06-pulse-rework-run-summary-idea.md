---
created: 2026-09-06T15:05:32-04:00
updated: 2026-09-06T15:05:32-04:00
domain: project
type: brief
status: active
tags: [pulse-dashboard, skills-lab, samira-loop]
source: slack
---

# Pulse rework idea — at-a-glance "what moved this run" summary

Lemar dropped this in Convo 2 (self-DM, ts `1788721532.651329`, 15:05 ET 2026-09-06):
"I think we need to rework the pulse reports to accommodate this new type of workflow.
Maybe it could just be at a glance: this is a summary of all the open items and all the
things that were done in the last Samira run."

Reads as feedback on the Pulse dashboard's shape now that the three-conversation
restructure (2026-09-06) has changed what Samira's hourly run actually produces — more
PT-card / build-lane activity than the old per-channel model. He wants Pulse to lead
with a per-run delta (open items + what got done last run) rather than only the
standing full-picture view it renders today.

Routed as a skill-candidate proposal (not built this scan) since it changes an
existing skill's output shape — `.claude/skills/pulse-dashboard/SKILL.md`.

## Proposed shape (starter, not locked)
- New top section: "This run" — a short delta list (cards closed/opened, notes filed,
  money moved) sourced from the same run digest Samira already computes for #reports.
  This is largely already-computed data, so the lift may be mostly a template/ordering
  change rather than new logic.
- Existing full-picture sections (calendar roadmap, money, workout, project pulses,
  routine health) stay below it, unchanged.

## Sources
- slack: Convo 2 (self-DM) drop, ts `1788721532.651329`, 2026-09-06 15:05 ET
