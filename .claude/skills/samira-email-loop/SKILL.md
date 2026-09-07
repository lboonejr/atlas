---
name: samira-email-loop
description: >
  Samira's email draft loop (her email job, PART 6a of the routine). Run this whenever
  Samira needs to draft replies to reply-worthy mail in Lemar's voice and run the
  approval loop with him as Convo 1 cards, AND scan reply-worthy + substantive mail for
  actionable tasks. The loop is Haven-first: "done = a filed Haven note" — every saved
  draft, closed thread, and detected task lands a note in the vault (the durable
  record); Convo 1 cards / Gmail Drafts become notifications about it. Use it every
  scan: "run the email loop", "draft email replies", "scan inbox for Samira", "pick up
  in-flight email threads". Lemar's signals decide — reactions AND plain replies;
  Samira reads them and never sets reactions (except the headline emoji). This skill
  ONLY saves to Gmail Drafts and NEVER sends email. It returns the counts Samira needs
  for the digest.
---

# Samira Email Loop (Haven-first, runs through Convo 1 cards)

Each scan: draft replies to reply-worthy mail in Lemar's voice and run the approval loop
as **Convo 1 cards** (the Samira DM, `D0BHPKMDNEP` — format per
`.claude/doctrine/card-format.md`), where Lemar decides by reacting or replying. Also
scan reply-worthy + substantive mail for tasks. Live-loop state is tracked with **Gmail
labels**; the **durable record is a Haven note**. You ONLY ever save to Gmail Drafts —
you NEVER send email. Every Safety rule in the runbook applies here.

(The old #emails channel is archived; the loop lived in #decisions until 2026-09-06,
when #decisions retired — it now runs on Convo 1 cards, deduped by Gmail labels +
in-thread reply.)

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — channel IDs AND the Gmail label IDs
(`Samira/seen` · `Samira/drafted` · `Samira/sent` · `Samira/investor`) are recorded
there; Gmail search and `label_thread` take IDs, never display names. Vault writes go
through **haven-capture** (never hand-written); do not write the retired local reader copy.

## Done = a filed Haven note
Land a note at each point where work is done or captured — stamp only what you're sure
of, leave the rest UNRESOLVED. haven-capture applies schema §7 automatically (if the
matter already has an active note, it appends an `## Update` instead of a sibling) and
puts thread links in `## Sources` (schema §8):
- **Saved draft** → `type: log`, `status: done`, `source: gmail`. Body: recipient,
  subject, gist of the reply; Gmail thread id in Sources.
- **Detected task** → captured BEFORE it is carded (capture-first): `type: task`,
  `status: active`, `source: gmail`. Reference the note path on the Convo 1 card.
- **Closed thread** (Lemar 🫡) → `type: log`, `status: done`, `source: gmail`. Worded
  from the signal ("Lemar saluted, so I closed it") — never assert the mail "was sent."
If a close records a decision Lemar made, the note is `type: decision` (schema §3).
Return the note count for the digest.

## The card engine (Lemar's signals — you READ, never SET)
You set only the headline emoji (🔴/🟡/🟢/⏳). Map: **✅** choose/execute · **👀** seen
· **⛔** park (→ the Haven open-items note; the canvas is retired) · **🫡** close (his
sent-signal). AND: a plain REPLY from Lemar is an equal, first-class signal — read it
every pass; it can add nuance to an emoji, override an option, or answer with no
reaction at all. When a reply and a reaction conflict, the reply wins (doctrine).

## One-time setup
Confirm the four labels exist (`list_labels`; `create_label` for any missing) and that
their IDs match `.claude/anchors.md`; if you create one, record its ID there.

## D1 — pick up in-flight email cards in Convo 1
Read your open email cards touched since last run (thread + reactions + replies — a
plain reply is an equal signal; on conflict it wins):
- **✅ on an option** (or his own edited reply) → merge his pick + edits, produce the
  final reply in his voice. Read `.claude/voice/voice-profile-lemar-boone-jr.md` and run
  its Hard-Floor Lint against this draft; revise until it passes before saving. Then SAVE
  to Gmail Drafts (`create_draft`, threaded onto the original mail — never a new thread).
  Write the saved-draft Haven note. Reply "Saved to your Gmail Drafts — ready to send ·
  filed to Haven." Apply `Samira/drafted`. Headline 🟢.
- **👀 / none** → leave it. **⛔** → park per the doctrine (reply "Parked ⏳", record in
  the Haven open-items note).
- **🫡** → close: apply `Samira/sent`, write the closed-thread Haven note, one #reports
  line, stop touching the thread.

## D2 — scan for new mail and triage
`search_threads`: `in:inbox after:<gmail_after_epoch> -label:<Samira/seen ID>` — the
epoch comes from `.claude/state/samira-state.json` (runbook PART 0); advance it when the
scan finishes. ONE canonical query, never two overlapping `newer_than:` windows (they
kept resurfacing already-seen threads). Fall back to `newer_than:2d` only if the
watermark is null. Read each thread
(`get_thread`), sort into ONE bucket, then apply `Samira/seen` to every thread examined:
- **REPLY-WORTHY** (a real person waiting on a response; Lemar hasn't already sent the
  latest message; not a pure ack; not merely CC'd) → D3 + D4.
- **SUBSTANTIVE but not reply-worthy** (no-reply invoice, statement, past-due or
  compliance notice, or an answered thread that still implies work) → D4 only.
- **INVESTOR / LENDER / CAPITAL** (investor, lender, term sheet, LOI, raise, diligence)
  → hand off: apply `Samira/investor` (+ seen); the samira-investor loop (PART 6b)
  works it as Convo 1 cards. Skip D3/D4 here.
- **JUNK** (newsletter, marketing, receipt with nothing to do, pure ack) → skip both;
  one tally line in the #reports digest; never carded to Convo 1, never written to Haven.

## D3 — summarize + draft options as a Convo 1 card
Per reply-worthy thread: ONE card (doctrine format; 🌐, "— Samira", headline ⏳/🟡) —
Headline, then a Context reply: who, what they're asking, any deadline, a one-line
read; add "⚠️ counsel/regulator/lender on thread — review carefully" when applicable.
Then 2–3 DRAFT OPTIONS as one-reply-per-option decision-round replies (Option
A/B/C), key line quoted, in Lemar's voice per the canonical profile at
`.claude/voice/voice-profile-lemar-boone-jr.md` (the single source of truth — it
supersedes the email-responder guide and every other style reference; each option should
pass its Hard-Floor Lint). Genuinely distinct angles only. Apply `Samira/seen`.
(No Haven note yet — the record is written when the draft is SAVED in D1.)

## D4 — task detection (capture-first, then card)
Over every reply-worthy AND substantive thread:
- **Capture to Haven first** (`haven-capture`, `type: task`) — the vault is written
  before the Slack card. Keep the note path.
- **Samira can execute it** (admin paperwork; record an invoice) → ONE Convo 1 card as
  a single-action parent, referencing the note path. It is worked on a LATER scan's
  PART 3 (buffer) from Lemar's signals; report-result writes the done outcome note.
  (Fenced `run:admin-3x` prompt staging is RETIRED — the PART C sweep ended 2026-09-06;
  cards replace fences.)
- **Needs Lemar** (approval, payment authorization, judgment) → ONE Convo 1 card
  with the source link + note path.
- A payment or transfer is outward-facing — NEVER execute it.

## What to return
**E summarized · R drafts saved · Cl closed · T tasks carded · O Haven notes written.**
Each close and each saved draft also gets its one-line #reports note pointing at the
Haven note path.
