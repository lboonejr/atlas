---
created: 2026-09-11T08:45:00-04:00
updated: 2026-09-11T08:45:00-04:00
domain: automation
type: decision
status: done
tags: [card-format, doctrine, fix, closing-mechanic]
source: slack
---

# Card "closed" redefined as a thread reply, not a parent edit

**Background:** the 100th scan found 19 Convo 1 cards that had a 🫡-close signal (many
already fully executed with a "Done ✅" reply) but were never actually marked closed,
because no tool in either Slack connector (Samira's own bot, or the personal connector)
can edit an already-posted message. The doctrine's "edit the parent to begin ✅ CLOSED"
step was never actually achievable with current tooling — every close attempt could
only ever land as a thread reply, invisible to a headline-only scan, so closed cards
kept resurfacing as "open" every pass, for weeks in some cases.

That scan posted a #fixes card (thread `C0BV5BRNH5Z:1788898652.010999`) with two
options: (1) redefine "closed" in `.claude/doctrine/card-format.md` as the thread's
last message being a `✅ CLOSED — [outcome]` reply (checkable with current tools), or
(2) something else.

**Decision:** Lemar replied "Let's go with option 1" (2026-09-11).

**Outcome this pass:** updated `.claude/doctrine/card-format.md` (Follow Up section)
and `.claude/skills/samira-loop/SKILL.md` (Closeout section) to define a closed card
as one whose thread's last message is a `✅ CLOSED — [outcome]` reply, rather than an
edited parent. Replied in the #fixes thread confirming the fix. Leaving the card open
for a Follow Up round on a later scan to verify the new definition actually holds
(per the standing rule that a fix card's Follow Up round verifies the fix, rather than
closing on the strength of "fixed" as a claim).

## Sources
- slack: #fixes thread `C0BV5BRNH5Z:1788898652.010999`
- repo: `.claude/doctrine/card-format.md`, `.claude/skills/samira-loop/SKILL.md`
