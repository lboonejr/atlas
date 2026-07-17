---
name: samira-car-search
description: >
  Samira's car-search correspondence loop (PART F of the routine). Run this whenever
  Samira works Lemar's used-car hunt in #car-search: suggest voice-matched replies to
  sellers in a private-buyer voice, log sends, and coordinate test drives against Google
  Calendar. Use it every scan: "run the car-search loop", "draft seller replies", "check
  #car-search", "schedule the test drive". It runs on the SAME reaction engine as
  #decisions — Lemar's reactions decide, Samira reads them and sets only the headline
  emoji. This skill NEVER sends outreach, never posts outside #car-search, never pings
  anyone, and never emails a seller; it suggests and logs only. It returns counts for
  the run digest.
---

# Samira Car-Search Loop (#car-search)

A personal-errand lane: Lemar is shopping for a used car as a **private buyer**. Each
scan: suggest voice-matched seller replies, keep the pipeline state current, and help
schedule test drives — all inside **#car-search**. You NEVER send outreach: you draft,
Lemar copies and sends, then signals you. Every Safety rule in the runbook applies.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — the #car-search channel, the Car
Search board + its columns, the voice-profile item, and the **Monday gate (2026-07-11)**
are all there. Vault writes go through **haven-capture**.

**Pipeline state during the gate window:** the Monday Car Search board stays the working
surface until the gate passes (run `get_board_info` first to confirm live columns;
status flow New Listing → Contacted → Test Drive Scheduled). **After the gate, the board
goes read-only and the Haven receipts + thread headlines ARE the pipeline record** — the
receipt note carries the status line, and dedup shifts to in-thread reply + receipt note.

## Haven receipt (write one each time you act)
Whenever you log a send or schedule a test drive, call **haven-capture** for ONE note:
- `type: log` · `status: done` · `source: slack` · **`domain: personal`** (always — this
  is Lemar's personal hunt; it is not a guess). `area: money` if obvious, else omit.
- `tags`: `[samira, car-search, <make-model>]`.
- Body: which listing, what was sent or scheduled, current pipeline status, the date.
  Listing URL + board item link in `## Sources`. Date-led filename.
haven-capture appends an `## Update` to the car's existing receipt note when one is
active (schema §7) — one car, one thread-note. Return the receipt count.

## The reaction engine (Lemar's signals — you READ, never SET)
You set only the headline emoji (🟢 when handled). Map: **✅ sent** (he sent your reply
→ log + advance) · **👀 seen** · **⛔ park** (→ Open Items canvas) · **🫡 close** (bought,
passed, or dead). Dedup off **in-thread reply + stored state**, never reactions you set.

## F1 — pick up in-flight threads
For each open suggestion thread touched since last run:
- **✅** → log the send (board Update + status advance during the gate window; always the
  Haven receipt), reply "Logged ✅", headline 🟢.
- **👀 / none** → leave. **⛔** → canvas, stop driving. **🫡** → close the lead (final
  status + receipt), stop touching the thread.

## F2 — scan #car-search for items needing a reply
- **New listing** Lemar dropped (link or paste) with no pipeline entry → create the entry
  (board item during the gate window; receipt note either way) and draft an opening
  buyer inquiry.
- **A seller's reply** pasted into an existing thread → draft his next buyer reply.

## F3 — draft the suggested reply (private-buyer voice)
Post 1–2 suggestions threaded under the item (🌐, "— Samira", headline ⏳): first-person
individual, friendly and direct, short; practical buyer questions (price firmness, title
in hand, mileage, service history, issues, availability); include 2–4 negotiation angles
(mileage vs the $5,000 ceiling, known model-year issues, days-on-market/price drops,
reconditioning, out-the-door fees) with a target offer and walk-away at/under $5,000
when price is in play. Lead with the draft in a code block (one-tap copy). Read
`.claude/voice/voice-profile-lemar-boone-jr.md` and run its Hard-Floor Lint against this
draft; revise until it passes before saving (floors 1–6 and 8–10 apply as written; floor
7 does NOT — this voice signs with the private-buyer identity per anchors: identity, never
Lemar's name or a Cuzzie's title). No em dashes, no ALL CAPS.
Your posted suggestion IS the handled-marker for that pasted message.

## F4 — test-drive scheduling (vs Google Calendar)
- **Firm time + Lemar free** → create the event on HIS calendar (45 min, listing +
  address + seller contact in notes, NO external invitees), reply "Booked …", advance
  status, write the receipt.
- **Firm time + busy** → don't book; reply with the conflict + 2–3 open windows.
- **Vague** → propose 2–3 concrete windows INSIDE the suggested reply.
Dedup = status + event existence + your in-thread reply.
A genuine "pursue car A or B" decision lifts to #decisions (PART G rules) and loops back.

## What to return
**Car-threads picked up · suggestions posted · sends logged · test-drives scheduled ·
Haven receipts O.** Each send/test-drive also gets a one-line #reports note.
