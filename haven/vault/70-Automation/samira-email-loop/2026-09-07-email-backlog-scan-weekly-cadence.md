---
created: 2026-09-07T12:11-04:00
updated: 2026-09-07T13:05-04:00
domain: automation
type: task
status: active
tags: [email, gmail, samira-email-loop, skill-candidate, weekly-cadence]
source: slack
---

# Email backlog scan — last 2 weeks + a weekly cadence

Lemar dropped this in Convo 2 (self-DM, ts `1788792120.484359`, 2026-09-07 10:42 ET):

> "I think we need to do a scan on my open emails from the last couple of weeks I feel
> like there's been things I haven't responded to. And maybe we make this something
> that runs weekly."

Two parts:
1. **One-time backlog scan** — go back further than the email loop's normal watermark
   (`gmail_after_epoch`, which only looks since the last hourly pass) and check the
   last ~2 weeks of inbox mail for anything reply-worthy that never got a draft or a
   reply.
2. **Skill-candidate**: a recurring **weekly** deep scan, distinct from the hourly
   `samira-email-loop` triage — hourly catches new mail off the watermark; this would
   be a periodic wider sweep to catch anything that slipped through (missed due to a
   run being skipped, a label miss, etc.).

## What this is not
Not a change to the hourly loop's cadence or its watermark logic — those keep working
off `gmail_after_epoch` exactly as they do today. This is an additional, separate pass.

## Open questions for Lemar (Convo 1 card)
- Run the one-time 2-week backlog scan now?
- Want the weekly cadence as a new scheduled trigger, or folded into one of the
  existing hourly Samira scans (e.g. only on the day's first run)?

## Sources
- slack: Convo 2 (self-DM `D0BBVV54L5R`), ts `1788792120.484359`
