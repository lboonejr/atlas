---
name: samira-car-search
description: >
  Samira's car-search correspondence loop (formerly PART F of the routine). Run this
  whenever Samira works Lemar's used-car hunt in #car-search: suggest voice-matched
  replies to sellers in a private-buyer voice, log sends to the Car Search board, and
  coordinate test drives against Google Calendar. Use it every scan: "run the car-search
  loop", "draft seller replies", "check #car-search", "any new listings", "schedule the
  test drive". It runs through #car-search on the SAME reaction engine as #decisions —
  Lemar's reactions decide, Samira reads them and sets only the headline emoji. This skill
  NEVER sends outreach, never posts outside #car-search, never pings anyone, and never
  emails a seller; it suggests and logs only. It returns counts for the run digest.
---

# Samira Car-Search Loop (#car-search)

This is a personal-errand lane: Lemar is shopping for a used car as a private buyer. Each
scan, suggest voice-matched replies to sellers, keep the Car Search board current, and help
schedule test drives — all inside **#car-search (C0BEC2RFC00)**. You NEVER send outreach
yourself: you draft, Lemar copies and sends, then signals you. Every Safety rule in the main
routine still applies. Board = Monday **"Car Search" 18418974601** (run `get_board_info`
first to learn the live columns); status flow **New Listing → Contacted → Test Drive Scheduled**.

This is an **outward-facing pipeline that STAYS live on Monday** — the board is the working
surface and does not move to Haven. But each time you ACT, you ALSO drop a **receipt note** into
Haven so the vault holds a durable record of the hunt (see "Haven receipt" below).

## HAVEN VAULT ANCHORS
```
Repo:  lboonejr/atlas  ·  branch: claude/haven-knowledge-system-4tp4sa  ·  draft PR #25
Vault (canonical):  haven/vault/     Inbox:  haven/vault/00-Inbox/     Schema:  haven/vault/_system/schema.md
Transport:  GitHub connector — you never hand-write a note; call the haven-capture skill,
            which writes the .md to 00-Inbox, commits, pushes, and returns the note path.
DO NOT write the local reader copy at C:\Users\lemar\Vaults\Haven.
```

## Haven receipt (write one each time you act)
The Monday board stays the live pipeline; Haven gets a parallel receipt. Whenever you log a
send or schedule a test drive, call the **`haven-capture`** skill to land ONE note in the Inbox:
- **`type: log`**, **`status: done`**, **`source: slack`**, **`domain: personal`** — this is
  Lemar's personal car hunt, so `domain` is always `personal` (stamp it; it is not a guess).
- **`tags`**: `[samira, car-search, <make-model>]`.
- Body: which listing, what was sent or scheduled, the Monday item link, and the date. Link the
  lead with a `[[wiki-link]]`. Name it date-led (`2026-07-03-<make-model>-<action>.md`).
Never guess a field you are unsure of; `domain` here is the one you are sure of. Return the
receipt count for the digest.

## The reaction engine (same as #decisions — Lemar's signals, you READ, you do not SET)
Every reaction in #car-search is **Lemar's**. You set only the **headline emoji** (🟢 when an
item is handled/done); you never add ✅/👀/⛔/🫡 yourself. The original bespoke car cursors
(💬/🗃️/📆) were dropped — use this one engine. Map:
- **✅ sent** — Lemar copied your suggested reply and sent it to the seller → log the send and
  advance the board status.
- **👀 seen** — he's seen it but hasn't acted → leave it this scan.
- **⛔ park** — drop the lead to the Open Items canvas (Parked); stop driving it.
- **🫡 close** — the lead is done (bought, passed, or dead) → close it on the board.

Dedup off **in-thread reply + board status** (mirrors the email loop), not off reactions you set.

## F1 — pick up in-flight #car-search threads (drive the loop forward)
Read your open suggestion threads touched since your last run, including replies
(`slack_read_thread`) and reactions (`slack_get_reactions`). For each:
- **Lemar reacted ✅ (sent)** → log the send to the Car Search board: note in the item Update
  what he sent and when, and advance status (New Listing → Contacted; or, if it was a
  scheduling message and a time is set, → Test Drive Scheduled). Set the thread headline 🟢.
- **👀 / no reaction** → leave it.
- **⛔ park** → move the lead to the Open Items canvas; stop driving it.
- **🫡 close** → close the lead on the board (final status / note); stop touching the thread.

## F2 — scan #car-search for items that need a reply
Read #car-search since your last run, into threads. Two kinds of new item:
- **A new listing** Lemar dropped in (a link or paste) with no board item yet → create a Car
  Search item (status New Listing) and draft an opening buyer inquiry.
- **A seller's reply** Lemar pasted into an existing thread → draft his next buyer reply.

## F3 — draft the suggested reply (private-buyer voice)
Post 1–2 suggested replies as threaded messages under the item (globe emoji, "— Samira",
headline ⏳). Write in a **private-buyer voice**, NOT Lemar's business/exec voice and NOT his
business signature: first-person individual, friendly and direct, short, asks the practical
buyer questions (price firmness, title in hand, mileage, service history, any issues,
availability to view). Keep the house floors from `feedback_voice_profile.md` that still apply
(no em dashes, no ALL CAPS). Lemar picks/sends, then reacts ✅ (F1).

## F4 — test-drive scheduling (vs Google Calendar)
When a seller is ready to schedule a viewing/test drive:
1. Check Lemar's calendar for conflicts (`list_events`) and propose 2–3 concrete windows in the
   suggested reply, so he can offer real times.
2. Once a time is confirmed (Lemar reacts ✅ on the scheduling message, or says the time is
   set), create the event on **his own calendar** (`create_event`) with the listing details in
   the notes — **no external invitees**, so no email goes to the seller. Advance the board
   status to Test Drive Scheduled.
- **Safety:** never email or message the seller, never add the seller as a calendar guest,
  never post outside #car-search, never ping anyone. You suggest and log; Lemar does the sending.

## What to return
Hand back to the routine the tallies for the digest:
**car-threads picked up, suggestions posted, sends logged, test-drives scheduled, and Haven
receipts written O.** Each send logged and each test drive scheduled also gets a one-line
#reports note and a Haven receipt note.
