---
name: decision-loopback
description: >
  Closes the loop between #decisions and the project channel that raised the question.
  When a #decisions card closes — Lemar ✅'d an option or 🫡'd the card — this posts ONE
  short closure notice back in the originating project channel, in the SAME scan the
  reaction is read, so the channel stops believing the question is still open. Carries the
  title, the pick, one line on what happens next, the Haven note path, and a link to the
  #decisions thread. Runs from PART A right after samira-report-result lands the outcome
  note; also on demand: "loop back the closed decisions", "did that decision get posted
  back", "close the loop on [card]". It posts one message to one project channel and
  nothing else — it never posts to #decisions, #reports, or the capture DM, never sends
  email or anything outward, never sets or reads a reaction as its own key, and never
  re-posts a notice that is already there.
---

# Decision loopback — the origin channel hears the answer

A decision raised in a project channel gets lifted to #decisions, Lemar decides, and then
the origin channel hears nothing. Days later a scan notices and back-fills an awkward
"this closed on [date] but never got looped back here." Meanwhile everyone in that channel
has been treating a settled question as open.

You close that gap in the same scan the reaction lands. You carry news, nothing more.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — #decisions (`C0BBXA96FFV`) and the
project-channel table. Never hardcode a channel id found anywhere else.

## SAFETY — inherits Samira's SAFETY block; this skill's own floor

You MAY: read closed #decisions cards and their threads; read an origin project channel's
recent messages; post ONE closure notice to that origin channel.

You MUST NOT, ever: post to #decisions, #reports, #stormy, #investor-pipeline, or the
Samira capture DM (the card and the #reports line are already handled — a second ping is
noise); send email or any outreach; set or remove any reaction (all reactions in a project
channel are Lemar's or another member's, never yours); edit or delete an existing message;
post a notice for a decision whose outcome note does not exist yet; re-post a notice that
is already in the channel; invent the origin — no citation means no post.

## When you run

**PART A, immediately after `samira-report-result` lands the outcome note** for a card
closed this scan (✅ on an option, or 🫡 on the parent). Also on demand when Lemar asks.

You never fire on 👀 (still deciding) or ⛔ (parked — the origin channel should not hear
"resolved" about something that was shelved; a parked item shows on the Open Items canvas
instead).

## The procedure

### 1. Establish the origin — no guessing
Read the closed card. Every card Samira posts carries its source link and, when lifted
from a project channel, an origin tag (PART G: "lift to #decisions tagged with origin").
- Origin is a project channel → continue.
- Origin is the capture DM, an email, a Haven note, or Samira's own sweep → **no loopback.**
  Nothing raised it in a channel, so nothing is waiting there. Stop silently.
- Origin is unreadable or ambiguous → **stop.** Do not infer a channel from the card's
  topic. Note it for the digest as `loopback: 1 skipped (no origin)`. A notice in the
  wrong channel is worse than none.

### 2. Confirm the outcome note exists
The notice links the Haven note, so the note must already exist —
`samira-report-result` writes it first. If it is missing, the task is not landed: stop
and let the report-result failure path own it. **Never post a closure notice for an
outcome that has no durable record.** Done = a filed Haven note; this message only points
at one.

### 3. Dedupe against the channel, not against a reaction
Read the origin channel since the card's close time. If a closure notice for this card is
already there — yours or a human's — stop. Your idempotency key is **the posted notice**,
found by reading. Never treat a reaction as your key: in a project channel the reactions
belong to Lemar and the other members.

### 4. Post exactly one notice

```
🌐 *Decision closed — [card title]*
[The pick, in one line — what was chosen.]
Next: [one line on what actually happens now, or "nothing further — this is settled".]
Record: [Haven note path] · [link to the #decisions thread]
— Samira
```

Keep it to those four lines. The channel needs the answer and where to read more, not the
deliberation. If the pick carries a date or an amount, it goes in the pick line — that is
the part people scroll back for.

### 5. Return your count
`loopback: N posted · M skipped` (or `loopback idle`), for Samira's run digest. Skipped
reasons worth naming: no origin, no outcome note, already posted.

## What this skill does NOT do

It does not close the card (PART A does), write the Haven note (samira-report-result
does), update the Open Items canvas (the canvas refresh does), or chase anything. It is a
one-message courier and it stays that small.

## Vault writes

**None.** The outcome note already exists before this runs; adding a second record would
fragment the matter against schema §7. This skill is a notification, and notifications do
not get their own notes.
