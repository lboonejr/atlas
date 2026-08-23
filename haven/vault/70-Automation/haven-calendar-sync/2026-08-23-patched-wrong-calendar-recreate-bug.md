---
created: 2026-08-23T17:07:00-04:00
updated: 2026-08-23T17:07:00-04:00
domain: automation
type: decision
status: done
tags: [samira, calendar-sync, bug, skill-patch]
source: slack
---

# haven-calendar-sync — patched the wrong-calendar RECREATE bug

## What ran

Lemar reacted ✅ on Samira's #decisions card ("calendar-sync recurring bug — checks
wrong calendar for business notes"), picking **Option 1 — patch haven-calendar-sync to
check the Cuzzie's (Owners) calendar for cuzzies/station notes before concluding
"deleted."** This note records that patch landing.

## Result

Edited `.claude/skills/haven-calendar-sync/SKILL.md` directly (no skill invoked — this
was a direct edit to a skill file, per PART A "execute the staged action"):

- Added a "Which calendar owns a note" section: home calendar is resolved from a note's
  `domain` (`personal` → reminder calendar; `cuzzies`/`station` → Cuzzie's (Owners)
  calendar), never assumed.
- Rewrote the Classify step (step 2) so the "does this event still exist" lookup always
  checks the note's own home calendar first, and RECREATE only fires after confirming
  the id is genuinely absent from *that* calendar — not just absent from the reminder
  calendar by default.
- Updated the ANCHORS/Target line to state the per-domain calendar routing explicitly,
  matching the locked 2026-08-10 policy already documented in `.claude/anchors.md` and
  the money-hub skill.

Root cause addressed: the RECREATE check previously looked up cuzzies/station notes'
`calendar_event_id` only on the personal reminder calendar, found nothing (because the
event correctly lived on the Cuzzie's (Owners) calendar), and concluded "deleted,"
recreating duplicates in the wrong place — the failure behind both of today's incidents
(8:03am Regus/IWG + Gusto false positives, and the 22-note duplicate incident ~14:xx UTC).

Commit: `a2329d149150a9f1e535e339d984143cab1fea56` on `main`.

## Sources
- github: `lboonejr/atlas` commit `a2329d149150a9f1e535e339d984143cab1fea56`
- Slack #decisions `C0BBXA96FFV` ts `1787495798.327079` — Lemar's ✅ on Option 1
- `haven/vault/40-Projects/samira-skills/2026-08-23-calendar-sync-wrong-calendar-bug.md`
  — the incident writeup this patch responds to
