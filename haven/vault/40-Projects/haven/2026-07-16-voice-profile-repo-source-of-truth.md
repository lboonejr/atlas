---
created: 2026-07-16T21:28:00-04:00
updated: 2026-07-16T21:28:00-04:00
domain: project
type: log
status: done
tags: [voice-profile, atlas, haven, skills, samira, source-of-truth, anchors]
source: claude
---

# 2026-07-16 Voice profile moved into the repo as the single source of truth

Moved Lemar's canonical voice profile into the atlas repo and made it authoritative
over all other style guidance, so cloud routines can read it (the old desktop OneDrive
path was unreachable from the cloud).

## What changed

- **Canonical profile now lives in the repo:** `.claude/voice/voice-profile-lemar-boone-jr.md`.
  The original ~983-line profile is preserved verbatim (byte-identical to the OneDrive
  source, diff-verified), with two blocks prepended above it:
  1. a **header block** carrying the precedence rule — this file supersedes ALL other
     style guidance, including the email-responder skill's `references/writing-style.md`
     (which conflicts, e.g. it permits em dashes; the profile forbids them);
  2. a **Hard-Floor Lint** — a 10-point floor every draft must pass before it is done.
- **Three repo draft-skills wired** to read the profile and run the Hard-Floor Lint
  before saving: `samira-email-loop` (D1 save gate + D3 draft-options, repointed off the
  retired email-responder guide), `samira-investor` (I3 outreach), and `samira-car-search`
  (F3 — floors 1–6, 8–10 apply; floor 7 yields to the private-buyer identity so the
  car-buyer voice stays anonymous).
- **`.claude/anchors.md`:** added a Voice profile section recording the canonical path,
  marking the OneDrive copy as a non-authoritative convenience copy, and noting the
  email-responder skill is retired from the send path (precedence governs if it fires).
- **Memory pointer** `feedback_voice_profile.md`: canonical source updated to the repo
  path (was OneDrive); email-responder conflict now resolved by precedence.

## Not done (out of repo)

`task-builder`, `Aaron` (aaron-exec), and `Chase` (chase-commitments) are anthropic-skills
plugin/session skills, not vendored in this repo — they could not be wired via local git.
They stay governed only by the header-block precedence rule until the pending
chat-skills → repo conversion lands them in `.claude/skills/`, at which point they get the
same lint wiring.

## Commit

Pushed straight to `main` via local git (per the no-PR git-write policy):
`46b0429` — "Make voice profile the repo source of truth; wire draft-skills to it"
(5 files changed, +1067 / −13).

Related: [[shortlist-anchors]] · [[2026-07-03-samira-atlas-framework-rework-handoff]]
