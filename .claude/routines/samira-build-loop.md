---
name: samira-build-loop
description: >
  The Samira Loop's scan-side half — **PART R of Samira's hourly run**, not a standalone
  routine. Threads in the "Samira's Loop" Claude project hand her things they built (or
  things they want built in the cloud); this loop advances each one's pressure test across
  the day's remaining scans in #decisions, locks it when the questions run out, then either
  builds it in the cloud, hands Lemar a Chrome run block for anything behind a login, or
  hands him a run-ready prompt for his machine. The full spec
  — lanes, card format, the eight lenses, closeout, #reports lines — lives in
  the **samira-loop** skill (`.claude/skills/samira-loop/SKILL.md`); this file is the loop's
  operational detail. All platform IDs live in `.claude/anchors.md`.
---

# The Samira Loop — build + pressure-test (PART R)

Lemar works in threads. Whatever a thread produces gets landed as a Haven note and opened
as a **🧪 PT card** in #decisions; your job at PART R is to move every open PT card one
round forward each scan until it locks, then finish it.

**Invoke the samira-loop skill once per run before working any card**
(`.claude/skills/samira-loop/SKILL.md`). Its sections 2 (cadence), 6 (the card, the eight
lenses, the signals), 7 (closeout), and 8 (#reports) govern; do not restate or re-derive them
here. The thin project rulebooks that live in `.claude/projects/` point at the same skill, so
a thread and a scan are always working from one text.

Different lane from Stormy: **Stormy bakes no-deadline ideas in #stormy and never
executes.** This loop is the right-now lane — same-day pressure test, then a real build.
An item that turns out to have no date on it gets handed to #stormy and dropped here.

## Where it sits
Run order: `… → D → E → Q → **R** → H → M → T → canvas → P → digest`. It runs after Stormy so
an idea misfiled into the wrong lane can be moved in the same pass, and before PART M so a
money-shaped outcome still reaches the ledger this run.

## Surfaces
- **#decisions `C0BBXA96FFV`** — the PT cards and every question. Only channel that pings him.
- **#reports `C0BBZJL85RT`** — one line per state change (project instructions §8).
- The **project channel** the item belongs to — where a cloud build gets staged as a fenced
  `run:admin-3x` prompt for PART C, and where the outcome loops back.
- Haven — the durable record. Every round is written to the note **before** it is posted.

## Watermarks
PT cards are ordinary #decisions cards, so they use the state file's existing
`decisions_threads` map (per-card latest-reply `ts`) — **no new state key**. A card whose
thread `ts` is unchanged and whose reactions are unchanged has no new signal; do not re-ask,
do not re-post, just carry it.

## PART A / PART R boundary (read this before touching a card)
**PART A skips any #decisions parent whose first line contains `🧪 PT`** — those cards are
worked here, and only here. PART R touches no other #decisions card. This keeps one card
from being executed twice by two PARTs in the same scan.

## The loop
1. **Find the open cards.** #decisions parents you posted whose first line contains
   `🧪 PT ·` and which do **not** begin `✅ CLOSED`. Parse the control line
   (`pt:<slug> · note:<path> · lane:<cloud|browser|local> · lenses:k/8`) for state. If the control
   line is missing or unparseable, rebuild it from the Haven note — the note is truth, the
   card is a rendering.
2. **Check for an engagement overlay.** A card whose title names a client engagement
   (today: "Camden Launch") is worked under that engagement's overlay in `.claude/projects/`,
   read BEFORE the round: its rules outrank the skill's mechanics and it adds gates that must
   clear before the card can lock. The engagement's index note
   (`40-Projects/<engagement>/index.md`) carries the pointers. No overlay named → generic
   loop rules apply.
3. **Compute the cadence** (the skill's §2): which scan of 11 this is and how many
   are left today. It sets the batch size and whether you compress to close today.
4. **Cap the work.** At most **three** active PT cards get a round in one scan, oldest
   first. Any beyond that carry, and the digest says so — a scan that half-answers six
   cards is worse than one that fully advances three.
5. **For each card, in order:**
   - **Read the thread** from its stored `ts` plus reactions on the parent and every
     question reply. Plain replies count as answers; ✅ agrees; 👀 means seen, carry it and
     never re-ask; ⛔ drops that line; 🫡 on the parent means lock it now.
   - **Record first.** Append an `## Update` to the Haven note through **haven-capture**:
     the answers, the lens coverage after them, what is still open. No round advances
     without the note landing — if the vault write fails, stop on that card, say so in the
     digest, and leave the card untouched.
   - **Then post one round** — 3–5 questions (5–7 compressed), batched by what belongs
     together, each with its one-line "why", as numbered replies under the parent. Refresh
     the parent's control line (`lenses:k/8`, `round N`) and its headline emoji.
   - **Or lock it** when all eight lenses are covered with nothing unanswered, or he 🫡'd.
6. **Closeout** per the skill's §7 — three lanes, not two: **cloud** builds get
   staged (buffer: never run in the scan they were staged) or executed directly when small
   and safe; **browser** items get the `CHROME RUN` block (Lemar drives Chrome, and it never
   submits, pays, sends, or clicks a binding button); **local** items get the `run:manual`
   run-ready prompt. Browser and local both put Samira in PM mode (one status check a day,
   max, in-thread). Every outcome lands through **samira-report-result**: Haven note first,
   then the #reports block, then `✅ CLOSED — [outcome]` on the parent.
7. **Housekeeping.** Apply the two-day rule (one honest "still worth doing?" line at day
   two, park on ⛔ or on silence by day four). Hand a no-date item to #stormy and close its
   card with the reason.
8. **Return a digest token**: `pt: <slug> r3 5/8 · <slug> locked · <slug> built · 2 carried`
   — or `pt —` when nothing is open. Do not write a separate `_daily` line; the run digest
   already appends the run.

## New work arriving from a thread
A thread that had GitHub access has already written the note and opened the card — you just
pick it up in step 1. A thread in a degraded mode (the skill's §10) drops its
summary in the **Samira capture DM** instead; that is **PART B's** job, not yours. When
PART B develops a capture tagged `samira-loop` / `pressure-test`, it opens the PT card and
this loop takes it from the next scan.

## SAFETY
Samira's standing SAFETY block governs unchanged, plus the loop's own floor: never build
anything in the cloud that requires an outward-facing action (send, pay, post publicly,
invite an external guest, change sharing) — those stop and become one 🟢 card awaiting his
✅. Never guess an answer he has not given in order to close a lens. Never invent a number,
a date, or a source to make a document look finished; an unverified figure stays flagged.
Never close a card whose Haven note did not land.
