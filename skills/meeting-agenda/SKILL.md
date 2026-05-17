---
name: meeting-agenda
description: Maintain per-meeting running notes through the week and assemble a Google Doc agenda on demand for meetings the user organizes. Captures notes from chat, Gmail, and Slack; carries decisions and open items forward across recurring instances; fans wrap-up outcomes out to task-builder, shortlist, and chase. Triggers on phrases like "build my agenda for <meeting>", "prep my 2pm", "add this to <meeting>", "wrap up the <meeting>", "set up meeting-agenda", or the `/agenda` slash command.
---

# Meeting Agenda

A workflow for treating each meeting the user leads as a long-running thread that compounds across the week and across recurrences. The skill **only tracks meetings the user organizes** — events where `organizer.self == true` on Google Calendar. Externals, invites, and blocks are ignored.

The skill operates in four modes — **bootstrap**, **capture**, **build**, **wrap-up** — plus an inbound coordination path from `star-craft`. Pick the mode from the trigger phrase; do not run multiple modes implicitly.

## Storage layout

```
skills/meeting-agenda/
  SKILL.md
  meetings/
    <slug>.json       # one file per tracked meeting
```

Each `<slug>.json` is the structured shadow of one meeting series:

```json
{
  "slug": "atlas-exec-sync",
  "title": "Atlas Exec Sync",
  "event_id": "<latest Google Calendar event id>",
  "recurring_event_id": "<recurringEventId if applicable>",
  "doc_url": "<Google Doc URL in Meeting Prep folder>",
  "doc_id": "<Drive file id>",
  "attendees": [{ "name": "...", "email": "..." }],
  "objective": "Why this meeting exists. Set at bootstrap, editable.",
  "captures": [
    {
      "source": "chat | gmail | slack",
      "ref": "<thread id | permalink | null>",
      "summary": "1-line summary",
      "added_at": "<iso>",
      "added_by": "user | star-craft"
    }
  ],
  "carryover": [
    { "from_instance": "<iso date>", "item": "...", "owner": "...", "due": "..." }
  ],
  "history": [
    {
      "instance_date": "<iso date>",
      "objective": "...",
      "outcome": "user's wrap-up summary",
      "objective_met": true,
      "routed": { "tasks": [...], "shortlist": [...], "chase": [...] }
    }
  ]
}
```

The human-facing running notes live in a **Google Doc per meeting**, stored in a Drive folder named exactly **"Meeting Prep"** at the root of the user's Drive. The Doc is linked into the calendar event description.

Slugs are auto-derived from the event title: lowercase, strip punctuation, hyphenate spaces (`"Atlas Exec Sync"` → `atlas-exec-sync`). On collision, append a short qualifier (`-1on1-sam`). The user can rename a slug at bootstrap or any time by editing the JSON filename — do not rename silently.

## When to run

| Trigger phrase | Mode |
|---|---|
| "set up meeting-agenda", "bootstrap meetings", first run | **Bootstrap** |
| "add this to <meeting>", "file this under <meeting>", paste-link + "add to <meeting>" | **Capture** |
| "build my agenda for <meeting>", "prep my 2pm", "what's on for the board meeting", `/agenda <slug>` | **Build** |
| "wrap up the <meeting>", "meeting done", "post-mortem the 2pm" | **Wrap-up** |

## Procedure

### Bootstrap

Run when no `meetings/` directory exists, when the user asks to set it up, or when they want to add new meetings to track.

1. Ensure the "Meeting Prep" Drive folder exists at the root of the user's Drive (`search_files` with name and `mimeType = application/vnd.google-apps.folder`). If absent, create it with `create_file`.
2. `list_events` for the next 14 days across the user's primary calendar.
3. Filter to events where the user is the organizer (`organizer.self == true`). Drop blocks, holds, and recurring instances whose parent is already tracked.
4. For each candidate, derive a slug from the title and propose: slug, title, day/time, attendee count.
5. Show the proposed list and **ask the user which to track** — do not auto-track everything.
6. For each confirmed meeting:
   - Create a Google Doc in "Meeting Prep" titled `<Meeting Title> — Running Notes`.
   - Write the `meetings/<slug>.json` skeleton (objective starts empty; prompt the user for a one-line objective).
   - `update_event` to append the Doc URL to the event description if not already linked.
7. Commit the new JSON files. Report the list of tracked meetings and their Doc links.

### Capture

Triggered by "add this to <meeting>" / "file this under <meeting>" / pasting a Gmail thread or Slack permalink with a meeting hint.

1. **Resolve the meeting.** Parse the hint (slug, partial title, day-of-week, or time). Look up tracked meetings in `meetings/`. Score by name similarity and day/time proximity.
2. **Always confirm the match** — show the matched event (title, next instance date/time, slug) and ask before filing. If ambiguous, show the top 2–3 candidates.
3. **Classify the source:**
   - **chat**: free-text note typed by the user. `ref` = null.
   - **gmail**: thread id or message link. Use `get_thread` to pull a 1-line summary; do not paste the full body into the JSON.
   - **slack**: permalink. Use `slack_read_thread` or `slack_read_channel` to fetch context for a 1-line summary.
4. Append a new entry to `captures[]` in the JSON.
5. Append a corresponding bullet to the running Google Doc under a "Captured this week" section, with a link back to the source.
6. Confirm filed and show the running count of captures for that meeting.

### Build agenda

Triggered by "build my agenda for <meeting>" / "prep my 2pm" / `/agenda <slug>`.

1. **Resolve the meeting** as in Capture step 1–2. Confirm.
2. **Pre-build nudge — surface unfiled capture candidates.** Before assembling, scan for things the user probably meant to file but didn't:
   - `search_threads` with `is:starred newer_than:7d` for starred Gmail threads whose participants overlap with the meeting attendees.
   - `slack_search_public_and_private` with `has::agenda:` (or the user's chosen flag emoji) for messages reacted in the last 7 days not already in `captures[]`.
   - For each candidate, show source + 1-line summary and ask: file under this meeting, file under a different meeting, or skip. Apply the user's choices, then continue.
3. **Open-loops sweep.** Query the user's other skills for items tied to this meeting's attendees or topics:
   - Invoke `task-builder` (read mode) for open tasks owned by or assigned to any attendee.
   - Invoke `shortlist` (read mode) for items mentioning attendees or topics.
   - Invoke `chase` (read mode) for outstanding financial commitments with any attendee.
   - Surface these as a "Open loops with attendees" section in the agenda — do not auto-add as discussion topics; the user decides which to raise.
4. **Assemble the agenda** into the Google Doc, replacing the previous "Day-of agenda" section (preserve "Captured this week" and running notes above it). Sections, in this order:
   - **Objective** — from JSON; if missing, prompt the user.
   - **Carryover from last meeting** — pulled from `carryover[]` (populated by the previous wrap-up). Each item shows owner and due date.
   - **Topics & decisions needed** — synthesized from `captures[]`, grouped by source, each with link back. Mark items that need a decision explicitly (`[DECISION NEEDED]`).
   - **Open loops with attendees** — output of step 3, listed but not pre-assigned to the agenda.
5. Update the Doc. Return the Doc URL and a one-line summary in chat — do not dump the agenda into chat.

### Wrap-up

Triggered by "wrap up the <meeting>" / "meeting done" / "post-mortem the 2pm". The user provides the outcome narrative; the skill extracts and routes.

1. **Resolve the meeting** and confirm.
2. **Capture the outcome.** Ask for (or parse from the user's message): what happened, decisions made, action items, financial commitments, follow-ups.
3. **Objective check.** Show the stated objective and ask: was it met? Record `objective_met` (true/false/partial) and a one-line note.
4. **Fan-out — route extracted items to other skills.** For every item, route to all buckets it plausibly belongs to (do not deduplicate across skills):
   - **Action items → `task-builder`, assigned to admin.** One invocation per item with the action, the meeting title + date as context, deadline if given, and admin as assignee.
   - **User's own follow-ups / things to remember → `shortlist`.** Strategic items, decisions pending, people to circle back with.
   - **Financial commitments → `chase`.** Amount, counterparty, date/window; ask `chase` to verify and update.
   - If a handoff fails, capture the error and keep going.
5. **Record carryover for next instance.** Anything punted, owed, or not resolved becomes a `carryover[]` entry. It will appear in the next instance's agenda automatically.
6. **Append to `history[]`** with date, objective, outcome, `objective_met`, and the routed items.
7. **Clear `captures[]`** for the just-completed instance.
8. Append a "Wrap-up — <date>" section to the Google Doc with the outcome narrative.
9. Report: items routed (with what each downstream skill said back, especially `chase`), carryover recorded, objective met or not.

## Inbound from star-craft

`star-craft` already routes to `task-builder`, `shortlist`, and `chase`. Extend it (separately) to also route to `meeting-agenda` when a starred thread relates to a tracked meeting in the next 7 days. When invoked as an inbound route:

1. Receive: thread id, 1-line summary, suggested slug.
2. Resolve the slug against tracked meetings. **Confirm with the user before filing** — never file silently from an inbound route, since star-craft's classification is a guess.
3. On confirm, follow Capture steps 3–5 with `added_by: "star-craft"`.

## Guardrails

- **Only track meetings the user organizes.** If asked to build an agenda for a meeting they don't own, say so and offer to bootstrap it as tracked first.
- **Always confirm the matched event** before filing, building, or wrapping up. The cost of asking is one extra message; the cost of filing under the wrong meeting is silent data drift.
- **Never auto-add open-loops items as agenda topics.** Surface them; the user decides what to raise.
- **Never dump the assembled agenda into chat.** The deliverable is the Google Doc link plus a one-line summary. Chat output stays terse.
- **Never modify the calendar event** beyond appending the Doc URL to the description during bootstrap. Do not change times, attendees, or titles.
- **Never deduplicate fan-out across skills.** If an item could be both a task and a shortlist note, route to both — each downstream skill owns its own view.
- **Never drop a failed handoff silently.** Report which routes failed and why.
- **Slug renames are explicit.** If the user wants to rename a meeting, they (or the skill, on request) renames the JSON file; the skill does not silently re-slug on event-title changes.
