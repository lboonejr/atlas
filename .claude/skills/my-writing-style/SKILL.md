---
name: my-writing-style
description: >
  Draft or rewrite any piece of writing so it sounds exactly like Lemar Boone Jr. —
  COO and co-founder of Cuzzie's Dispensary & Delivery (Camden, NJ) and operations
  lead for The Station Dispensary (Newark, NJ). Use this skill for ANY drafting or
  rewriting task: emails, Slack messages and DMs, texts, internal memos,
  investor/partner updates, SOPs and reference docs, vendor outreach, social
  captions, apologies, praise notes, hard-news messages, or general "make this sound
  like me" / "rewrite this in my voice" / "draft this the way I'd say it" requests.
  Also use it when Lemar pastes a draft (his own or AI-generated) and asks you to fix
  the voice, or when he asks you to write something "as me" for any channel.
---

# My Writing Style Skill

You are writing or rewriting content in **Lemar Boone Jr.'s** voice. The complete
voice profile — beliefs, writing mechanics, structural preferences, hard nos, red
flags, signature phrases, and the 19-mode voice-calibration table — lives at
**`.claude/voice/voice-profile-lemar-boone-jr.md`**. That file is the repo's single
source of truth for Lemar's voice (see its own header block and the "Voice profile"
section of `.claude/anchors.md`); it supersedes every other style guidance. This
SKILL.md does not restate any of it — it's the process wrapper that tells you when
and how to use that file. If the two ever seem to disagree, the canonical file wins.

Every draft must sound like it came from Lemar himself... not from an AI, not from a
legal template, not from a generic business writer.

---

## Step 1: Identify the Job

Figure out what Lemar wants written or rewritten, and the channel it's headed to:
Slack/DM, text, email, memo, investor/partner update, SOP or reference doc, vendor
outreach, social copy, or something personal/off-work. If it's ambiguous, ask one
focused question rather than guessing the channel. This skill only produces the
voice — it doesn't send, save, or file anything anywhere; that's up to whatever else
is orchestrating the task (e.g. `samira-email-loop` saves to Gmail Drafts,
`handoff-builder` saves to Drive — this skill just drafts).

---

## Step 2: Read the Canonical Profile and Identify the Mode

Open `.claude/voice/voice-profile-lemar-boone-jr.md` and read its header block first
(the precedence rule and the Hard-Floor Lint). Then use the **Voice Calibration**
table in its Quick Reference Card to pick the right mode — e.g. Hard-news outsider,
Pitching-up, Apology, Praise, Personal, SOP/reference doc, etc. Ask the four
questions the file's "Context Matters" section lays out before writing:

1. Who is the audience? (insider / outsider / pitching-up / customer / personal)
2. What are the stakes? (hard news / praise / commitment / refusal / neutral)
3. What channel? (Slack / text / email / SOP / long-form doc)
4. What's the desired emotional register? (warm / formal / urgent / measured)

---

## Step 3: Draft

Write from the full profile, not just the Quick Reference Card — the calibration
table is a lookup index, not a substitute for reading the relevant sections. In
particular:

- Default structure for messages is the **sandwich** (soft open → substance → soft
  close); SOPs and reference docs are structured instead, with headers and emoji
  wayfinding, no sandwich.
- **"We" by default, "I" only for personal accountability.**
- Match the signature opener/closer and any signature phrases to the mode (see
  "Signature Phrases & Structures" in the canonical file).
- Vary sentence length and register within the piece — uniform pacing/tone is an AI
  tell (see "Natural Variation").
- Insert one register-shifted word per piece (a casual lift in formal prose, or a
  formal lift in casual prose).
- Use ellipses where most writers reach for em dashes. Use parentheses for emphasis.
  Never use em dashes, ALL CAPS, bold, or italics for emphasis.

---

## Step 4: Run the Canonical Hard-Floor Lint

Before presenting the draft, run the 10-item Hard-Floor Lint at the top of
`.claude/voice/voice-profile-lemar-boone-jr.md` verbatim against it — every check,
every time. Don't re-derive or restate the list here; the canonical file is the only
place it's allowed to live (same "no second copy" rule `anchors.md` applies to
platform IDs).

Also strip (but don't over-strip) the profile's use-but-cut words if this is meant to
read as cleaned-up/polished: "I think," "really," "definitely," "absolutely,"
"literally," "for the most part."

---

## Step 5: Run the Litmus Test

Before finalizing, ask the six questions from the canonical file's "Litmus Test"
section — does it sound warm, is the specificity in, did a vulnerable moment get
wrongly bowed into a lesson, any kill-list words slipped through, does it read
over-polished, and would someone close to Lemar say "yeah, that's him."

---

## Step 6: Present the Draft

Show the draft in chat. Briefly note (1-2 sentences) any key voice choices you made —
which mode you picked and why, anything you deliberately left out or softened. Ask if
Lemar wants adjustments before he uses it, unless he's clearly asked for a fire-and-
forget draft.

---

## Reference

- **`.claude/voice/voice-profile-lemar-boone-jr.md`** — the repo's single source of
  truth for Lemar's channel-agnostic voice: core identity, the full 100-question
  interview synthesis (beliefs, writing mechanics, aesthetic crimes, voice &
  personality, structural preferences, hard nos, red flags), the Quick Reference Card
  (always/never/use-but-cut/signature phrases/voice calibration table), the
  anti-overfitting usage guide, and the Instructions for Claude section. This skill
  reads that file and nothing else for voice — it does not bundle or duplicate any
  part of it.
