---
created: 2026-07-05T22:35-04:00
updated: 2026-07-05T22:35-04:00
domain: project
type: task
status: active
tags: [dawn, daily-brief, samira, system]
source: claude
due: 2026-07-12T09:00-04:00
calendar_event_id: b7tntlvq22lioq79ho1oq16ah0
---

# Fold Dawn's brief-refresh into Samira's hourly scans

<!-- calendar_event_id is set to an event created by hand this session (not a guess), so
     haven-calendar-sync sees this note is already booked and will not duplicate it. -->

Deferred from the Dawn build ([[2026-07-05-dawn-routine-built]]). Lemar chose "1am only to
start"; this is the "add intraday refresh later" follow-up.

**Goal:** have Samira's hourly scan (8a–6p ET) refresh Dawn's living brief artifact as goals
close during the day, so the brief reflects live progress — not just the 1am snapshot.

**What to do:**
- Add a light step — ideally a Dawn-owned skill invoked by Samira, so Dawn stays the brief's
  owner — that re-deploys the current day's brief artifact with updated goal/loop states from
  #reports + Haven. Pass the persisted URL in `.claude/anchors.md` ("Living brief artifact
  URL") as the Artifact `url` so it re-deploys to the SAME link. Keep it cheap: a partial
  state refresh, not a full rebuild.
- Samira only refreshes the RENDERING; she may append an `## Update` to Dawn's `_daily` brief
  note but never rewrites it. Dawn owns the note.

**Why 2026-07-12:** bundle with the Monday-gate work (2026-07-11, when Samira's runbook is
already being edited to drop the Monday mirror) so her live runbook is touched once, and
after Dawn's 1am run has ~6 clean days. Movable.

**Prereqs:** confirm Dawn's scheduled 1am run works (first run 2026-07-06 ~1:02 AM ET) and
that the Artifact tool works headless in the cloud. If not, the brief is on the Slack-canvas
fallback and this incorporation targets the canvas (`slack_update_canvas`) instead.

## Sources
- gcal: event `b7tntlvq22lioq79ho1oq16ah0` on the reminder calendar (2026-07-12 9:00 AM ET)
- [[2026-07-05-dawn-routine-built]]
