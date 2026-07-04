---
name: samira-email-loop
description: >
  Samira's email draft loop (her email job, PART D of the routine). Run this whenever
  Samira needs to draft replies to reply-worthy mail in Lemar's voice and run the
  approval loop with him in #decisions, AND scan reply-worthy + substantive mail for
  actionable tasks. The loop is Haven-first: "done = a filed Haven note" — every saved
  draft, closed thread, and detected task lands a note in the vault (the durable
  record); #decisions / Gmail Drafts become notifications about it. Use it every scan:
  "run the email loop", "draft email replies", "scan inbox for Samira", "pick up
  in-flight email threads". Lemar's reactions decide; Samira reads them and never sets
  them (except the headline emoji). This skill ONLY saves to Gmail Drafts and NEVER
  sends email. It returns the counts Samira needs for the digest.
---

# Samira Email Loop (Haven-first, runs through #decisions)

Each scan: draft replies to reply-worthy mail in Lemar's voice and run the approval loop
in **#decisions** — the single place Lemar decides, by reacting. Also scan reply-worthy +
substantive mail for tasks. Live-loop state is tracked with **Gmail labels**; the
**durable record is a Haven note**. You ONLY ever save to Gmail Drafts — you NEVER send
email. Every Safety rule in the runbook applies here.

(The old #emails channel is archived; the loop lives inside #decisions, deduped by Gmail
labels + in-thread reply.)

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
- **Detected task** → captured BEFORE it is staged (capture-first): `type: task`,
  `status: active`, `source: gmail`. Reference the note path on the staging card.
- **Closed thread** (Lemar 🫡) → `type: log`, `status: done`, `source: gmail`. Worded
  from the signal ("Lemar saluted, so I closed it") — never assert the mail "was sent."
If a close records a decision Lemar made, the note is `type: decision` (schema §3).
Return the note count for the digest.

## The #decisions reaction engine (Lemar's signals — you READ, never SET)
You set only the headline emoji (🔴/🟡/🟢/⏳). Map: **✅** choose/execute · **👀** seen
· **⛔** park (→ Open Items canvas) · **🫡** close (his sent-signal).

## One-time setup
Confirm the four labels exist (`list_labels`; `create_label` for any missing) and that
their IDs match `.claude/anchors.md`; if you create one, record its ID there.

## D1 — pick up in-flight email threads in #decisions
Read your open email cards touched since last run (thread + reactions):
- **✅ on an option** (or his own edited reply) → merge his pick + edits, produce the
  final reply in his voice, SAVE to Gmail Drafts (`create_draft`, threaded onto the
  original mail — never a new thread). Write the saved-draft Haven note. Reply "Saved to
  your Gmail Drafts — ready to send · filed to Haven." Apply `Samira/drafted`. Headline 🟢.
- **👀 / none** → leave it. **⛔** → park to canvas.
- **🫡** → close: apply `Samira/sent`, write the closed-thread Haven note, one #reports
  line, stop touching the thread.

## D2 — scan for new mail and triage
`search_threads`: `in:inbox newer_than:2d -label:<Samira/seen ID>`. Read each thread
(`get_thread`), sort into ONE bucket, then apply `Samira/seen` to every thread examined:
- **REPLY-WORTHY** (a real person waiting on a response; Lemar hasn't already sent the
  latest message; not a pure ack; not merely CC'd) → D3 + D4.
- **SUBSTANTIVE but not reply-worthy** (no-reply invoice, statement, past-due or
  compliance notice, or an answered thread that still implies work) → D4 only.
- **INVESTOR / LENDER / CAPITAL** (investor, lender, term sheet, LOI, raise, diligence)
  → hand off: apply `Samira/investor` (+ seen); the samira-investor loop works it in
  #investor-pipeline. Skip D3/D4 here.
- **JUNK** (newsletter, marketing, receipt with nothing to do, pure ack) → skip both;
  one tally line in the #reports digest; never posted to #decisions, never written to Haven.

## D3 — summarize + draft options in #decisions
Per reply-worthy thread: ONE parent (🌐, "— Samira", headline ⏳/🟡): who, what they're
asking, any deadline, a one-line read; add "⚠️ counsel/regulator/lender on thread —
review carefully" when applicable. Then 2–3 DRAFT OPTIONS as threaded replies (Option
A/B/C), key line quoted, in Lemar's voice (email-responder skill, draft only, +
feedback_voice_profile.md: no em dashes, no ALL CAPS, "we" by default, correct
signature). Genuinely distinct angles only. Apply `Samira/seen`.
(No Haven note yet — the record is written when the draft is SAVED in D1.)

## D4 — task detection (capture-first, then stage)
Over every reply-worthy AND substantive thread:
- **Capture to Haven first** (`haven-capture`, `type: task`) — the vault is written
  before the Slack staging. Keep the note path.
- **A channel/role can execute it** (admin paperwork; pay/record an invoice) → STAGE a
  fenced `run:admin-3x` prompt UN-REACTED to the right channel (admin → #admin;
  otherwise auto-discover), referencing the note path. It runs on a LATER scan (buffer);
  report-result writes the done outcome note.
- **Needs Lemar** (approval, payment authorization, judgment) → ONE #decisions parent
  with the source link + note path.
- A payment or transfer is outward-facing — NEVER execute it.

## What to return
**E summarized · R drafts saved · Cl closed · T tasks staged · O Haven notes written.**
Each close and each saved draft also gets its one-line #reports note pointing at the
Haven note path.
