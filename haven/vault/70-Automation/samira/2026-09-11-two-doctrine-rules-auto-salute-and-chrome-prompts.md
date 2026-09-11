---
created: 2026-09-11T10:05:00-04:00
updated: 2026-09-11T10:05:00-04:00
domain: automation
type: task
status: done
tags: [doctrine, card-format, samira-loop, browser-lane]
source: slack
---

# Two doctrine rules, per Lemar's Convo 2 drops

Two direct rule changes Lemar dropped in his self-DM 2026-09-11 (both plain
instructions, not brain-dumps needing development — implemented directly this pass).

## Rule 1 — auto-🫡 the parent on card close

Convo 2 thread ts `1789135557.913319`: "once that close message happens at the end of
a thread, the parent item to that message automatically gets marked with the salute
emoji." Complements the 2026-09-11 card-close redefinition (last message = `✅ CLOSED —`
reply is what makes a card closed) — that fixed the mechanic, this fixes visibility:
a headline-only scan down the channel now shows closed cards too, without opening
every thread to check the last message.

Implemented as a one-line addition to `.claude/doctrine/card-format.md`'s Follow Up
section: the instant Samira posts the close reply, she reacts 🫡 on the parent
herself — the sole exception to "Samira never sets reactions," scoped narrowly to
this one mechanical step.

Applied this pass to the two cards closed today (Visit Alex — Sage Dispensary,
Quick todo list — judge/Medicaid/420 Solutions) as a light retroactive touch; not
re-processed against the full historical backlog (low value relative to cost, and
not what was asked — this is a going-forward rule).

## Rule 2 — computer-action options get a paired Claude-and-Chrome prompt

Convo 2 thread ts `1789134644.637969`: "any time a computer action is suggested, a
Claude and Chrome prompt is made so that I can just perform the action sooner."
Formalizes what already happened ad hoc on the Station weekend card this same pass
(two ready-to-run browser-lane prompts for MBE/SBE cert status + a renewal-checklist
project). Implemented in `.claude/doctrine/card-format.md`'s Decisions section: any
option requiring Lemar's own logged-in session (a portal, a gated account) now ships
with the literal prompt text to run in a Claude-in-Chrome session, not just a
description of the blocker.

## Sources
- slack: Convo 2 `D0BBVV54L5R` ts `1789134644.637969` (Chrome-prompt rule) ·
  ts `1789135557.913319` (auto-🫡 rule)
- repo: `.claude/doctrine/card-format.md`
