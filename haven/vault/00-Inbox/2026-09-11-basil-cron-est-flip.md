---
created: 2026-09-11T12:30-04:00
updated: 2026-09-11T12:30-04:00
domain: automation
type: task
status: active
tags: [inbox-janitor, basil, cron, dst]
source: claude
due: 2026-11-01T09:00-05:00
---

# Flip Basil's cron to EST — `7 4 * * *` UTC

DST ends Sunday 2026-11-01. Basil's nightly trigger (`trig_01JE6TpvqAnawkETpx64vvX9`)
is expressed in UTC, so on or after that morning the cron must be changed from
`7 3 * * *` (11:07pm EDT) to `7 4 * * *` (11:07pm EST) or Basil starts running at
10:07pm ET.

Steps:
1. Update the RemoteTrigger cron to `7 4 * * *` UTC.
2. Update the Cron row in `.claude/anchors.md` (Inbox Janitor block) to match, and set
   the "next flip" date there to spring 2027 (DST returns Sun 2027-03-14 → back to
   `7 3 * * *`).
3. Mark this note `status: done`.

Same flip applies in reverse every March/November; the anchors row is the standing
record of which value is live.
