# Meeting Agenda Workflow — SOP

*How to use the `meeting-agenda` Claude skill end-to-end.*

## What this is for

A workflow that treats every meeting you lead as a long-running thread. Notes you collect during the week get filed against the right upcoming meeting; the morning of, a polished HTML agenda is assembled and dropped in your Drive ready to share with attendees, partners, or anyone covering for you; after the meeting, outcomes get extracted and routed to your other skills (`task-builder`, `shortlist`, `chase`) so nothing falls through.

**Scope:** only meetings *you organize*. Externals and meetings someone else scheduled for you are excluded unless you explicitly bootstrap them.

## Where things live

- **Drive > Meeting Prep folder** — agenda HTML files, one per meeting instance. Named `<Meeting Title> — Agenda YYYY-MM-DD`. Open in Drive to view formatted; click "Open with > Google Docs" if you need to edit.
- **atlas repo > `skills/meeting-agenda/meetings/`**
  - `<slug>.md` — human-readable running notes (objective, captures-this-week, wrap-up history). Edit directly if you want.
  - `<slug>.json` — structured shadow (event IDs, attendees, carryover, history). Don't hand-edit unless you know what you're touching.

## The four modes

| Mode | When | Say to Claude |
|---|---|---|
| **Bootstrap** | First time, or adding a new meeting to track | "set up meeting-agenda" / "track *<meeting name>*" |
| **Capture** | Mid-week, when something comes up you'll want to discuss | "add this to *<meeting>*: *<note>*" (or paste a Gmail/Slack link) |
| **Build** | Day of the meeting | "build my agenda for *<meeting>*" / "prep my 2pm" / `/agenda <slug>` |
| **Wrap-up** | After the meeting | "wrap up *<meeting>*" (narrative) / "process the transcript for *<meeting>*" |

## 1. Bootstrap (first run for a meeting)

1. Say "set up meeting-agenda" or "track the <name> meeting".
2. Claude scans your calendar for the next 14 days, filters to meetings you organize, derives slugs from the titles (e.g. "Cuzzie's Team Meeting" → `cuzzies-team-meeting`), and shows you the list.
3. Confirm which ones to track. Claude creates the `.md` and `.json` for each.
4. Claude prompts you for a one-line **objective** for each meeting — the standing purpose. This shows up at the top of every agenda.

*Note: if a meeting was scheduled by your admin on your behalf, the calendar organizer is technically them. Claude will flag this and ask whether to treat it as yours. Say yes for any meeting you actually lead.*

## 2. Capture notes during the week

Three ways to file something against an upcoming meeting:

- **Tell Claude in chat:** "add this to Thursday's board meeting: we should revisit pricing on the new SKUs."
- **Paste a Gmail thread or Slack permalink:** "add to cuzzies-team-meeting: *<Slack permalink>*".
- **React with `:agenda:`** on a Slack message (or star a Gmail thread). Claude will surface these at build time and ask which meeting each belongs to.

Claude will **always confirm the matched event** before filing — one extra message beats a note filed under the wrong meeting.

## 3. Build the agenda (day of)

1. Say "build my agenda for *<meeting>*" or `/agenda <slug>`.
2. Claude runs a **pre-build sweep** — scans starred Gmail and `:agenda:`-reacted Slack messages from the last 7 days that aren't already filed, and asks if any should be added.
3. Claude runs an **open-loops sweep** — queries `task-builder`, `shortlist`, and `chase` for items tied to attendees of this meeting, so you can raise anything outstanding.
4. Claude assembles the agenda with these sections:
   - **Objective**
   - **Carryover from last meeting** (decisions and owed items from the prior instance)
   - **Topics & decisions needed** (synthesized from this week's captures, grouped by source, with links back)
   - **Open loops with attendees** (surfaced but not pre-added — you decide what to raise)
5. The agenda lands in **Drive > Meeting Prep** as a formatted HTML file. Claude returns the link in chat. Share it however you like (paste in Slack, send via email, drop in the calendar event).

## 4. Wrap-up (after the meeting)

Two ways in:

### Option A — type the outcome yourself
"Wrap up the cuzzies-team-meeting. We decided X. Malik will own Y by Friday. We're paying the supplier $12k Tuesday."

### Option B — hand Claude a transcript (recommended)
1. Before the meeting starts, turn on Google Meet's **"Take notes for me"** (Gemini in Meet). It auto-produces a Doc with the transcript and a summary.
2. After the meeting, find the Gemini-generated notes Doc in your Drive.
3. Say to Claude: "process the transcript for cuzzies-team-meeting, transcript at *<Drive URL>*".
4. Claude pulls the transcript and extracts decisions, action items (with owner + due), financial commitments, follow-ups, and a short outcome narrative.

### What happens next (both options)

1. **Review the extraction.** Claude shows you the proposed items as a checklist. *Nothing is routed until you approve.* Edit anything that's wrong — transcripts misattribute commitments all the time.
2. **Objective check.** Claude shows the stated objective and asks whether it was met (yes / partial / no) plus a one-line note. This compounds over time into a read on which meetings are actually working.
3. **Fan-out.** On approval, items route to:
   - **Action items → `task-builder`**, assigned to admin, with the meeting as context
   - **Your own follow-ups → `shortlist`**
   - **Financial commitments → `chase`** for verification

   Items that fit multiple buckets go to all of them — no deduplication.
4. **Carryover recorded.** Anything unresolved, punted, or pending becomes a carryover item for the next instance's agenda automatically.
5. **History updated.** Outcome narrative, objective-met status, and routed items get appended to the JSON history and the running-notes markdown.

## Recommended notetaker

**Google Meet's "Take notes for me"** (Gemini in Meet) is the lightest setup — toggle on at meeting start, transcript Doc lands in your Drive afterwards, hand the URL to Claude. No bots to invite, no calendar plumbing.

Alternatives if Gemini isn't available: Otter.ai, Fireflies.ai, Read.ai — each joins as a calendar attendee and emails a transcript afterwards. Paste or link the transcript to Claude the same way.

## Operational notes

- **Slug renames** are explicit — rename both `<slug>.json` and `<slug>.md` in the repo if you want to change a slug. Claude won't silently re-slug if you rename a calendar event.
- **Agenda files are never edited after emit** — each instance gets its own historical HTML file. Wrap-up records live in the markdown and JSON, not in the agenda file.
- **Calendar events are never modified** by the skill. Share agenda links manually via Slack / email / event description.
- **Cleanup:** Claude can create files in Drive but cannot delete them. If you build many agendas, manually trash older instances from the Meeting Prep folder periodically.
- **One source of truth:** the JSON is canonical for structured data (event IDs, attendees, carryover); the markdown is canonical for human-readable narrative. Both are written together — if you edit one by hand, edit the other to match or ask Claude to reconcile.

## Trigger phrase cheat sheet

- "set up meeting-agenda" — bootstrap a new tracked meeting
- "add this to *<meeting>*: *<note>*" — capture during the week
- "build my agenda for *<meeting>*" / `/agenda <slug>` — build the day-of agenda
- "wrap up *<meeting>*" — manual outcome narrative
- "process the transcript for *<meeting>*, transcript at *<URL or path>*" — transcript-driven wrap-up
