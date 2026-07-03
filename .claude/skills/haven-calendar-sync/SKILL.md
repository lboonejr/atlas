---
name: haven-calendar-sync
description: >
  The vault's alarm clock — standing job #2 in Samira's hourly loop, run right after
  vault-keeper. Google Calendar is the only thing that fires timed alerts, so this skill
  projects every Haven note that carries a `due` onto the reminder calendar as an event,
  then writes the resulting `calendar_event_id` back into the note so it is never
  double-booked. The calendar is a one-way RENDERING of the vault: the vault is truth,
  the calendar mirrors it. When a note's due changes, the event moves; when the note is
  done or archived, the event is cancelled. Calendar and vault writes are allowed
  unattended. Use it on Samira's scan or on demand ("sync the calendar", "ring my due
  Haven notes"). It creates/updates/cancels reminder events and writes back the event id
  only — it never sends invites, never adds external guests, never emails.
---

# haven-calendar-sync — the alarm clock

Haven holds truth and live status; it cannot make a phone buzz. Google Calendar can.
This skill is the bridge: any note with a `due` becomes a timed reminder event, and the
event's id is written back into the note so the projection is idempotent. Nothing about
the schedule is a source of truth — delete the event and the next sync recreates it from
the note; change the note and the next sync corrects the event. **The vault always wins.**

The rule it never breaks:

> **The calendar is a one-way projection of notes that carry a `due`. Truth lives in the
> note; the event is only a rendering. Never let the calendar drive the note** (except the
> single machine-managed field `calendar_event_id`, which this skill owns).

## HAVEN VAULT ANCHORS

```
Repo:            lboonejr/atlas   ·   branch: claude/haven-knowledge-system-4tp4sa   ·   draft PR #25
Vault (canonical):  haven/vault/          Schema (rulebook):  haven/vault/_system/schema.md
Transport:          GitHub connector. Pull latest → read `due` notes → write back `calendar_event_id` → commit → push.
DO NOT WRITE the local reader copy at C:\Users\lemar\Vaults\Haven (no .git, may drift).
Reminder calendar (the ONLY target — personal, NOT Lemar's business primary):
    c_205bab62b8bb2c4fe12eec38bbc6725abaf6f5f11b767fe99a542112cf5695d3@group.calendar.google.com
```

Always write to the reminder calendar above, never to a business/primary calendar, and
never with external attendees — these are Lemar's own reminders, not invitations.

---

## The two frontmatter fields this skill lives on

From schema §3 (optional fields):

- **`due`** — ISO 8601 with ET offset. Present only when a note is time-bound. Its
  presence is the trigger: any note with a `due` gets an event. A human or Atlas sets it.
- **`calendar_event_id`** — **machine-managed; this skill owns it.** Written back after
  the event is created so the same note is never double-booked. Never set by hand;
  vault-keeper and haven-capture never touch it.

---

## The sync, step by step

1. **Pull** the latest `haven/vault/`. Find every note in the vault (filed folders +
   `00-Inbox`) whose frontmatter contains a `due`. A stuck Inbox note can still carry a
   `due` and should still ring — ringing does not require the note to be filed.

2. **Classify** each `due` note by comparing note ↔ calendar:

   - **`due`, no `calendar_event_id`** → NEW. Create the event; write the id back.
   - **`due` + `calendar_event_id`, note still `active`/`parked`** → EXISTING. Read the
     event; if the `due` (start), the title, or the note link drifted, UPDATE the event
     to match the note. If they already match, do nothing.
   - **`status: done` or `status: archived`, has `calendar_event_id`** → RETIRE. Cancel
     (delete) the event and clear `calendar_event_id` from the note. A finished thing
     should not keep ringing.
   - **`calendar_event_id` present but `due` removed** → the note is no longer time-bound.
     Cancel the event and clear `calendar_event_id`.
   - **`calendar_event_id` points to an event that no longer exists** (Lemar deleted it) →
     recreate it from the note (the vault wins) and write the new id back. Do not treat a
     manually deleted event as "handled" — the note still has a `due`.

3. **Event shape** when creating/updating:
   - Calendar: the reminder calendar anchor above. No attendees.
   - Start: the note's `due`. Default duration 30 min (these are reminders, not meetings)
     unless the note states a window.
   - Title: `Haven: <note title>`.
   - Description: the note's repo path (so Lemar can jump to the source), plus a one-line
     summary and the References/link if the note has one. Truth lives in the note; the
     description is a convenience pointer.
   - A default popup notification so it actually alerts.

4. **Write back** `calendar_event_id` into the note's frontmatter (and clear it on
   retire), **touch `updated`**, commit and push: `calendar-sync: +A ~B -C`
   (created / updated / retired).

## What calendar-sync must NOT do
- Never send a calendar invite or add an external guest — reminders only, on the personal
  reminder calendar.
- Never change any note field other than `calendar_event_id` (and the `updated` stamp).
  It does not set `due`, does not file, does not touch bodies.
- Never treat the calendar as truth: on any disagreement, re-project from the note.
- Never write the local reader copy.

---

## Idempotency (why overlapping scans are safe)
`calendar_event_id` is the whole dedup key. A note that already has a valid id whose event
matches its `due` produces zero writes. So two scans close together do not double-book:
the first creates the event and stamps the id; the second sees the id, sees a matching
event, and moves on. This mirrors how Samira uses the green check / board state elsewhere —
here the state lives in the note itself.

## Report (for Samira's digest)
Return counts for the run digest: `rang +A (new) · ~B (updated) · -C (retired)`.

---

## Worked example
The Harvest Moon note gets its date confirmed. Lemar (or Atlas) adds to its frontmatter:

```yaml
due: 2026-07-09T09:00-04:00
```

Next sync: the note has a `due`, no `calendar_event_id` → NEW. calendar-sync creates
`Haven: Harvest Moon invoice 2425 — confirm count before paying` at 9:00 AM ET on
2026-07-09 on the reminder calendar, description = the note's repo path + "$1,840,
confirm count before paying", 30-min, popup on. It writes
`calendar_event_id: <id>` back into the note and touches `updated`.

Later, Lemar confirms the count and pays; the note's `status` goes to `done`. Next sync:
`done` + has an id → RETIRE. The event is cancelled and `calendar_event_id` cleared. The
reminder stops ringing; the note remains the durable record.
