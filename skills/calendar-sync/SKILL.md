---
name: calendar-sync
description: Project Haven notes that carry a `due` date onto Google Calendar so they fire native, 24/7 phone reminders. One-way, Haven → Calendar. Triggers when Atlas dispatches the hourly calendar pass, or when the user says "sync the calendar", "push due dates to my calendar", "run calendar-sync". A Samira executor job.
---

# Calendar Sync

The alarm-clock arm of **Haven**. Where `vault-keeper` files the Inbox,
calendar-sync takes any note that carries a `due` date and projects it onto
**Google Calendar**, so the reminder fires natively on the phone at the right
time — even if Claude and the loop are down. It is the twin of vault-keeper: a
**Samira executor**, dispatched by **Atlas** on the same hourly loop.

This job is **one-way: Haven → Calendar.** Haven is the source of truth; the
calendar is only a rendering of the `due` field. calendar-sync never reads
anything *back* from the calendar into a note except the event id it created.

The rulebook is the vault's own `_system/schema.md`. If this file and the schema
ever disagree, **the schema wins** — read it first (`haven/vault/_system/schema.md`).

## When to run

Run when Atlas dispatches the hourly calendar pass, or when the user asks
directly ("sync the calendar", "push due dates"). Default scope is every note in
the vault that carries a `due` field.

## Procedure

### 1. Read the schema, then find due notes

Read `haven/vault/_system/schema.md` for the current `due` / `calendar_event_id`
definitions. Then scan the vault for every note whose frontmatter has a `due`
field. Ignore notes without one — most notes are not time-bound.

### 2. Reconcile each due note against its event

For each note with a `due`, decide the action by comparing it to Google Calendar:

- **No `calendar_event_id` yet** → **create** a calendar event, then write the
  returned event id back into the note's `calendar_event_id` field (and touch
  `updated`). This is the only thing calendar-sync writes into a note.
- **Has `calendar_event_id`, and `due` (or the title) changed** → **update** the
  existing event to match the note.
- **Has `calendar_event_id`, and `status` is now `done` or `archived`** →
  **cancel/delete** the event and clear `calendar_event_id`. Finished and
  archived work should not keep ringing.
- **Has `calendar_event_id`, nothing changed** → leave it alone.

Match a note to its event by the stored `calendar_event_id`, never by title —
titles are not unique.

### 3. Keep the event thin (it is a pointer, not a copy)

The event is a signpost back to the truth in Haven, so keep it minimal:

- **Title** = the note's `# H1` title.
- **Start/time** = the note's `due` (ISO 8601 ET). Use a default reminder offset
  unless the note specifies one.
- **Description** = one line of context plus **which Haven note it came from**
  (the vault-relative path), so when it buzzes the user knows where to look.

Do not pour the note body into the event. If the details change, they change in
Haven; the next pass re-syncs.

### 4. Report internally only

Post a concise status to the internal surface (`#decisions` / Open Items) — never
outward:

- Events created / updated / cancelled this pass, each with the note it maps to.
- Any note whose `due` could not be parsed (leave it; flag it for the human).
- Any calendar write that failed, with the reason, so it can be retried.

## Guardrails

- **One-way only.** Haven → Calendar. Never treat a calendar entry as truth, and
  never edit a note from the calendar except to store/clear `calendar_event_id`.
- **Never invent a `due`.** If a note has no `due`, it gets no event. Deciding
  something is time-bound is the human's or the capturing skill's call, not this
  job's.
- **Never send email, never post publicly, never touch money.** Calendar writes
  and internal status only.
- **Idempotent.** Running twice in a row must not create duplicate events — that
  is what `calendar_event_id` guarantees. Always match on it before creating.
- **Keep the vault portable.** The `due` date is plain text in the note; the
  Google-specific event id is a machine field, and no other calendar/Google
  syntax ever leaks into the note body.

## Registration & wiring (operational, not part of the vault)

- Register calendar-sync on the **Atlas Skills and Accounts Registry** board
  (`18419004984`) as a **Samira executor** skill, alongside `vault-keeper`.
- Dispatch: Atlas hourly loop, 8am–6pm, seven days a week (same loop as
  vault-keeper). The calendar itself fires reminders 24/7, independent of the loop.
- Target calendar: Lemar's Google Calendar (via the Calendar connector).
- Status surface: `#decisions` / the Open Items canvas.
