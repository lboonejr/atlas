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
    <slug>.json       # structured shadow (machine-readable)
    <slug>.md         # running notes (human-readable)
```

The **running notes live as a markdown file in this repo**, not in Google Drive. The Drive MCP available to this skill can create Docs but not edit existing ones, so editing a hosted Doc each capture means recreating it and breaking the link every time. The markdown file is git-tracked, cheap to append to, and survives the ephemeral container via the remote.

The **Google Doc is only emitted at build time**, as a day-of agenda artifact named `<Meeting Title> — Agenda YYYY-MM-DD`, dropped into the "Meeting Prep" folder at the root of the user's Drive. That's a low-frequency, short-lived artifact intended to be shared/used during the meeting; recreating it per build is fine.

Each `<slug>.json` is the structured shadow:

```json
{
  "slug": "atlas-exec-sync",
  "title": "Atlas Exec Sync",
  "event_id": "<latest Google Calendar event id>",
  "recurring_event_id": "<recurringEventId if applicable>",
  "calendar_id": "<calendar id>",
  "event_url": "<htmlLink>",
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
      "agenda_doc_url": "<Google Doc URL emitted at build time>",
      "routed": { "tasks": [...], "shortlist": [...], "chase": [...] }
    }
  ]
}
```

Each `<slug>.md` is the read-friendly running notes for the meeting series:

```markdown
# <Title> — Running Notes

**Recurrence:** <weekly | …>
**Attendees:** <comma-separated>
**Event:** <event_url>

## Objective
<one paragraph>

## Captured this week
- YYYY-MM-DD (source): summary [link]
- …

## Wrap-up history
### YYYY-MM-DD — objective met: yes/partial/no
<outcome narrative, routed items>
```

Captures and wrap-ups are written to **both** the JSON (structured) and the .md (human). They are kept in sync — if you can't write one, do not write the other.

Slugs are auto-derived from the event title: lowercase, strip punctuation, hyphenate spaces (`"Atlas Exec Sync"` → `atlas-exec-sync`). On collision, append a short qualifier (`-1on1-sam`). The user can rename a slug at any time by renaming both `<slug>.json` and `<slug>.md` — do not rename silently.

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
   - Write `meetings/<slug>.json` and `meetings/<slug>.md`. The objective starts empty in both — prompt the user for a one-line objective and fill it in.
   - Do **not** create a Google Doc and do **not** modify the calendar event. Both happen only at build time.
7. Commit the new files. Report the list of tracked meetings.

### Capture

Triggered by "add this to <meeting>" / "file this under <meeting>" / pasting a Gmail thread or Slack permalink with a meeting hint.

1. **Resolve the meeting.** Parse the hint (slug, partial title, day-of-week, or time). Look up tracked meetings in `meetings/`. Score by name similarity and day/time proximity.
2. **Always confirm the match** — show the matched event (title, next instance date/time, slug) and ask before filing. If ambiguous, show the top 2–3 candidates.
3. **Classify the source:**
   - **chat**: free-text note typed by the user. `ref` = null.
   - **gmail**: thread id or message link. Use `get_thread` to pull a 1-line summary; do not paste the full body into the JSON.
   - **slack**: permalink. Use `slack_read_thread` or `slack_read_channel` to fetch context for a 1-line summary.
4. Append a new entry to `captures[]` in `<slug>.json` **and** a corresponding bullet to the "Captured this week" section of `<slug>.md`, with a link back to the source. Both writes happen in the same commit.
5. Confirm filed and show the running count of captures for that meeting.

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
4. **Assemble the agenda** with these sections, in order:
   - **Objective** — from JSON; if missing, prompt the user and persist back.
   - **Carryover from last meeting** — pulled from `carryover[]` (populated by the previous wrap-up). Each item shows owner and due date.
   - **Topics & decisions needed** — synthesized from `captures[]` in the JSON, grouped by source, each with link back. Mark items that need a decision explicitly (`[DECISION NEEDED]`).
   - **Open loops with attendees** — output of step 3, listed but not pre-assigned to the agenda.
5. **Emit the Google Doc as HTML** (see "Agenda Doc formatting" below). Create a new Doc in "Meeting Prep" titled `<Meeting Title> — Agenda <YYYY-MM-DD>` (date = the instance date). Use `create_file` with `contentMimeType: text/html` so Drive converts it into a properly formatted Doc — real headings, real bullet lists, hyperlinks, bold. Plain text uploads render as monospace blocks and look unprofessional when shared; never use plain text for the agenda Doc.
6. Do not overwrite or delete prior agenda Docs — they become a historical record per instance.
7. Append the new Doc URL to a stub history entry for this instance (`history[]`), so wrap-up later finds it. The stub has `instance_date` and `agenda_doc_url` set; other fields filled by wrap-up.
8. Return the Doc URL and a one-line summary in chat — do not dump the agenda into chat.

#### Agenda Doc formatting

The Doc may be shared with business partners, attendees, or someone covering the meeting on the user's behalf. It must look polished out of the box.

Render the agenda as HTML following this structure:

```html
<h1>{Meeting Title} — Agenda</h1>
<p><strong>Date:</strong> {YYYY-MM-DD, weekday}<br>
<strong>Time:</strong> {start–end, timezone}<br>
<strong>Attendees:</strong> {comma-separated names}</p>

<h2>Objective</h2>
<p>{objective text}</p>

<h2>Carryover from last meeting</h2>
<ul>
  <li><strong>{owner}</strong> — {item} <em>(due {due})</em></li>
</ul>
<!-- If empty: <p><em>Nothing carried over.</em></p> -->

<h2>Topics &amp; decisions needed</h2>
<h3>From chat notes</h3>
<ul><li>{summary}</li></ul>
<h3>From email</h3>
<ul><li>{summary} — <a href="{gmail link}">thread</a></li></ul>
<h3>From Slack</h3>
<ul><li>{summary} — <a href="{slack permalink}">message</a></li></ul>
<!-- Items needing a decision: prefix with <strong>[DECISION NEEDED]</strong> -->

<h2>Open loops with attendees</h2>
<ul>
  <li><strong>{attendee name}</strong> — {item} <em>(from {task-builder | shortlist | chase})</em></li>
</ul>
<!-- If empty, omit this section entirely. -->
```

Rules:
- Use `<h1>` exactly once (the title). Section headings are `<h2>`; sub-groupings under Topics are `<h3>`.
- Always use real `<ul><li>` lists — never asterisks or hyphens in paragraphs.
- Escape `&`, `<`, `>` in any user-supplied text (capture summaries, attendee names).
- Hyperlinks use `<a href="...">label</a>` with descriptive label text (e.g. "thread", "message", "doc"), not raw URLs.
- Omit empty sections silently except Carryover, which renders an "Nothing carried over." line so the reader knows the slot exists.
- Do not embed CSS or `<style>` blocks — Drive strips them and they create noise.

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
6. **Fill in the stub history entry** for this instance (created at build time) with objective, outcome, `objective_met`, and the routed items. If no stub exists (wrap-up without a prior build), append a fresh entry.
7. **Clear `captures[]`** for the just-completed instance in the JSON, and move the "Captured this week" bullets in `<slug>.md` into a new dated subsection under "Wrap-up history" alongside the outcome narrative.
8. Do **not** modify the agenda Google Doc — the wrap-up record lives in the markdown and JSON. The Doc stays as the day-of snapshot.
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
- **Never modify the calendar event.** No description edits, no time/attendee/title changes. Share the Doc link via chat/Slack instead.
- **Never edit a previously-emitted agenda Doc.** Each instance gets its own Doc; the prior one is the historical record.
- **JSON and markdown must stay in sync.** Every capture and wrap-up writes to both, in the same commit. If one write fails, roll back the other.
- **Never deduplicate fan-out across skills.** If an item could be both a task and a shortlist note, route to both — each downstream skill owns its own view.
- **Never drop a failed handoff silently.** Report which routes failed and why.
- **Slug renames are explicit.** If the user wants to rename a meeting, they (or the skill, on request) renames the JSON file; the skill does not silently re-slug on event-title changes.
