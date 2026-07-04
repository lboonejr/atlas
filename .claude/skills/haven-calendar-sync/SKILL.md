---
name: haven-calendar-sync
description: >
  The vault's alarm clock — standing job #2 in Samira's hourly loop, run right after
  vault-keeper. Google Calendar is the only thing that fires timed alerts, so this skill
  projects every Haven note that carries a `due` onto the reminder calendar as an event,
  then writes the resulting `calendar_event_id` back into the note so it is never
  double-booked. The calendar is a one-way RENDERING of the vault: the vault is truth,
  the calendar mirrors it. When a note's due changes, the event moves; when the note is
  done or archived, the event is cancelled. Use it on Samira's scan or on demand ("sync
  the calendar", "ring my due Haven notes"). It creates/updates/cancels reminder events
  and writes back the event id only — it never sends invites, never adds external
  guests, never emails.
---

# haven-calendar-sync — the alarm clock

Haven holds truth and live status; it cannot make a phone buzz. Google Calendar can.
This skill is the bridge: any note with a `due` becomes a timed reminder event, and the
event's id is written back into the note so the projection is idempotent. Delete the
event and the next sync recreates it from the note; change the note and the next sync
corrects the event. **The vault always wins.**

> **The calendar is a one-way projection of notes that carry a `due`. Truth lives in the
> note; the event is only a rendering. Never let the calendar drive the note** (except
> the single machine-managed field `calendar_event_id`, which this skill owns).

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — the reminder-calendar ID is there.
Constants:
- Vault: `haven/vault/` on repo `lboonejr/atlas`, default branch.
- Transport: GitHub connector. Pull → read `due` notes → write back `calendar_event_id`
  → commit → push.
- Target: the reminder calendar ONLY — personal, never a business primary, never
  external attendees. DO NOT write the retired local reader copy.

---

## The two frontmatter fields this skill lives on

- **`due`** — ISO 8601 with ET offset. Its presence is the trigger: any note with a
  `due` gets an event. A human or Atlas sets it.
- **`calendar_event_id`** — **machine-managed; this skill owns it.** Written back after
  the event is created. Never set by hand; vault-keeper and haven-capture never touch it.

## The sync, step by step

1. **Pull** the latest `haven/vault/`. Find every note (filed folders + `00-Inbox`)
   whose frontmatter contains a `due`. A stuck Inbox note can still ring.

2. **Classify** each `due` note by comparing note ↔ calendar:
   - `due`, no `calendar_event_id` → **NEW**: create the event; write the id back.
   - `due` + id, note still `active`/`parked`/`awaiting-decision` → **EXISTING**: if the
     start, title, or note link drifted, UPDATE the event to match the note; else nothing.
   - `status: done`/`archived` with an id → **RETIRE**: cancel the event, clear the id.
   - id present but `due` removed → cancel the event, clear the id.
   - id points to a deleted event but `due` remains → **RECREATE** (the vault wins).

3. **Event shape**: reminder calendar; no attendees; start = `due`; 30-min default;
   title `Haven: <note title>`; description = the note's repo path + one-line summary;
   popup notification on.

4. **Write back** `calendar_event_id` (or clear it), **touch `updated`**, commit + push:
   `calendar-sync: +A ~B -C`.

## What calendar-sync must NOT do
- Never send an invite or add a guest. Never change any note field other than
  `calendar_event_id` (+ `updated`). Never treat the calendar as truth. Never write the
  local reader copy.

## Idempotency
`calendar_event_id` is the whole dedup key: a note with a valid id and matching event
produces zero writes, so overlapping scans never double-book.

## Report (for Samira's digest)
Return `rang +A (new) · ~B (updated) · -C (retired)`.

## Worked example
A note gains `due: 2026-07-09T09:00-04:00` → NEW: event `Haven: Harvest Moon invoice
2425 …` created 9:00 AM ET Jul 9, id written back, `updated` touched. Later the note
goes `status: done` → RETIRE: event cancelled, id cleared. The reminder stops ringing;
the note remains the durable record.
