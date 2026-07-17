---
created: 2026-07-17T00:00-04:00
updated: 2026-07-17T00:00-04:00
domain: project
type: log
status: done
tags: [samira, infra, duplicate-execution, decisions-hygiene]
source: slack
---

# Duplicate/concurrent Samira execution flag — closed

Samira's #decisions card (thread ts `1784237329`) reported that two (then a third)
concurrent Samira sessions had run the same hourly routine in parallel, causing
redundant #reports noise and a race on the Pulse dashboard artifact. The threaded reply
also raised three follow-up items:

1. This session's overlap (the duplicate/concurrent runs themselves).
2. Whether extending the reaction-engine bot-identity fix to Dawn (a separate assistant
   that never reads reactions back) was actually justified, since it was applied by
   analogy without its own #decisions ask.
3. Samira's bot still needing `/invite` into #atlas and #skills-lab.

Lemar reacted 🫡 on the parent card. No closing reply had been posted for this thread
before this scan (only the original flag + follow-up reply existed), so this note is
that closing receipt.

Disposition on the three follow-ups: (3) is already covered — a separate #decisions card
(2026-07-16, "Samira bot needs #atlas/#skills-lab invites") was reacted 🫡 and closed
once the bot-identity switch made the point moot. (2) is a standing open question, not
an action item — no #decisions ask has been raised for Dawn's connector scope, and none
is being raised here; if Lemar wants that reviewed on its own it should get its own card.
(1) — the overlap itself — has no corrective action defined in the runbook beyond what
already exists (git-write retry-on-reject policy for concurrent vault writes); flagging
it here as a standing operational risk worth watching, not something this note resolves.

## Sources
- slack: #decisions thread `1784237329` (flag + reply, 🫡 from Lemar)
- repo: `.claude/routines/samira-atlas-executor.md` — PART A closing rule
