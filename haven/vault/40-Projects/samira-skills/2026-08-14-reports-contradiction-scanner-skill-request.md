---
created: 2026-08-14T16:56-04:00
updated: 2026-08-15T10:42-04:00
domain: project
type: task
status: done
tags: [skill-candidate, samira, reports, contradiction-scanner]
source: slack
---

# Skill candidate: #reports contradiction-scanner

Lemar, capture DM 2026-08-14 (ts `1786740991.727389`): wants a new skill that reads
#reports and flags any contradictions or problems Samira should be aware of, DMs him
a summary with proposed solutions, and — if it surfaces a question for Lemar — posts
it to #decisions (`C0BBXA96FFV`). Once Lemar answers there, the skill hands the fix
off to Samira to actually execute.

**Not built.** Per the hard safety floor, Samira/Atlas never build a skill mid-run —
routed as a candidate proposal to #skills-lab (`C0BBZ5J8805`) instead, in PART H's
format (what recurs, inputs/outputs, rough starter prompt). A human picks it up from
there.

## Update 2026-08-15
Lemar picked this up directly (Slack #skills-lab thread, ts `1786741654.908089`) and had
it built. Skill lives at `.claude/skills/reports-contradiction-scanner/`. It scans
#reports for conflicting figures, unresolved self-corrections, and stale claims; checks
each against the cited Haven note as ground truth; DMs Lemar a findings summary
(capture DM, only when something's found); stages obvious fixes for a later PART C pass
(new #reports line, never an edit); and posts genuinely open questions to #decisions,
worded as directly executable options so PART A's existing reaction engine handles the
handoff — no new execution logic needed. Not yet wired into the hourly runbook as its
own PART; invokable on demand until Lemar makes that call explicitly (same gate Stormy's
PART Q went through).

## Update 2026-08-15 (2)
Lemar asked to add it to the scheduled loop. Wired into
`.claude/routines/samira-atlas-executor.md` as **PART R**, run order
`... → M (money) → R (reports scan) → canvas refresh → P (Pulse) → digest`, and added
to the digest's tally line (`reports-scan: found N/open O` or `reports-scan: clean`).
No change to Safety or the reaction engine — PART R only reads, lands its own Haven log
note, DMs, and posts normal #decisions cards; PART A already executes anything Lemar
picks.

## Sources
- slack: capture DM `D0BHPKMDNEP` ts `1786740991.727389` (2026-08-14)
- slack: #skills-lab `C0BBZ5J8805` ts `1786741654.908089` (2026-08-14, candidate proposal)
