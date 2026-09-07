---
name: samira-build-loop
description: >
  The Samira Loop's scan-side half — the **PART 3 PT-round detail** of Samira's hourly
  run (was PART R until the 2026-09-06 restructure), not a standalone routine. Threads
  in the "Samira's Loop" Claude project hand her things they built (or things they want
  built in the cloud); this loop advances each one's pressure test across the day's
  remaining scans as decision rounds on its Convo 1 card, locks it when the questions
  run out, then either builds it in the cloud, hands Lemar a Chrome run block for
  anything behind a login, or hands him a run-ready prompt for his machine. The full
  spec — lanes, card format, the eight lenses, closeout, #reports lines — lives in
  the **samira-loop** skill (`.claude/skills/samira-loop/SKILL.md`); this file is the loop's
  operational detail. All platform IDs live in `.claude/anchors.md`.
---

# The Samira Loop — build + pressure-test (PART 3 PT-round detail; was PART R)

Lemar works in threads. Whatever a thread produces gets landed as a Haven note and opened
as a **🧪 PT card** in Convo 1 (the Samira DM); your job inside the PART 3 Convo 1 pass is
to move every open PT card one round forward each scan until it locks, then finish it.

**Invoke the samira-loop skill once per run before working any card**
(`.claude/skills/samira-loop/SKILL.md`). Its sections 2 (cadence), 6 (the card, the eight
lenses, the signals), 7 (closeout), and 8 (#reports) govern; do not restate or re-derive them
here. The thin project rulebooks that live in `.claude/projects/` point at the same skill, so
a thread and a scan are always working from one text.

Different lane from Stormy: **Stormy bakes no-deadline ideas in Convo 2's deep-dive mode
and never executes.** This loop is the right-now lane — same-day pressure test, then a real
build. An item that turns out to have no date on it gets handed to Stormy's lane and
dropped here.

## Where it sits
PT rounds run **inside PART 3** (the Convo 1 pass — run order P0 → P1 → P2 → **P3** → P4 →
P5 → P6 → P7 → P8 → digest). Running ahead of PART 4 means an item this pass re-lanes (to
Stormy's bake, or a money-shaped outcome to the money-hub sweep) can still be picked up by
the Convo 2 machinery in the same run, and PART 7's timeline pass records anything a PT
round moved before the digest closes.

## Surfaces
- **Convo 1 — the Samira DM `D0BHPKMDNEP`** — the PT cards and every question. The only
  surface that pings him for work decisions (PT cards moved off #decisions 2026-09-06).
- **#reports `C0BBZJL85RT`** — one line per state change (project instructions §8).
- The **project channel** the item belongs to — an append-only TIMELINE where movements
  and the outcome are recorded (the fenced `run:admin-3x` staging lane is retired; a
  timeline is never swept).
- Haven — the durable record. Every round is written to the note **before** it is posted.

## Watermarks
PT cards are ordinary Convo 1 cards, so they ride the state file's **`card_threads`** map
(per-open-card latest-reply `ts`, keyed `"<channel_id>:<parent_ts>"`) — the retired
`decisions_threads` map is gone with #decisions. A card whose thread `ts` is unchanged and
whose reactions are unchanged has no new signal; do not re-ask, do not re-post, just carry
it.

## Card-pass / PT-round boundary (read this before touching a card)
Within PART 3, **the generic card pass skips any Convo 1 parent whose first line contains
`🧪 PT`** — those cards are worked by this detail, and only by it. This detail touches no
other Convo 1 card. This keeps one card from being worked twice by two passes in the same
scan.

## The loop
1. **Find the open cards.** Convo 1 parents you posted whose first line contains
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
6. **Closeout** per the skill's §7 — three lanes, not two: **cloud** builds get executed
   directly when small and safe, or carried on the card across scans until the acceptance
   test passes (the retired `run:admin-3x` staging lane is replaced by these two paths;
   the buffer rule survives — a card opened this pass is first worked on a later scan);
   **browser** items get the `CHROME RUN` block (Lemar drives Chrome, and it never
   submits, pays, sends, or clicks a binding button); **local** items get the `run:manual`
   run-ready prompt, unchanged — never swept by anything. Browser and local both put Samira in PM mode (one status check a day,
   max, in-thread). Every outcome lands through **samira-report-result**: Haven note first,
   then the #reports block, then `✅ CLOSED — [outcome]` on the parent.
7. **Housekeeping.** Apply the two-day rule (one honest "still worth doing?" line at day
   two, park on ⛔ or on silence by day four). Hand a no-date item to Stormy's lane
   (Convo 2's deep-dive mode) and close its card with the reason.
8. **Return a digest token**: `pt: <slug> r3 5/8 · <slug> locked · <slug> built · 2 carried`
   — or `pt —` when nothing is open. Do not write a separate `_daily` line; the run digest
   already appends the run.

## New work arriving from a thread
A thread that had GitHub access has already written the note and opened the card — you just
pick it up in step 1. A thread in a degraded mode (the skill's §10) drops its
summary in **Convo 2 (Lemar's self-DM)** instead; that is **PART 4's** job, not yours. When
PART 4 develops a drop tagged `samira-loop` / `pressure-test`, it opens the PT card and
this loop takes it from a later scan.

## SAFETY
Samira's standing SAFETY block governs unchanged, plus the loop's own floor: never build
anything in the cloud that requires an outward-facing action (send, pay, post publicly,
invite an external guest, change sharing) — those stop and become one 🟢 card awaiting his
✅. Never guess an answer he has not given in order to close a lens. Never invent a number,
a date, or a source to make a document look finished; an unverified figure stays flagged.
Never close a card whose Haven note did not land.
