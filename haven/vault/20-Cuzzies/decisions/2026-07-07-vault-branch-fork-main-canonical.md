---
created: 2026-07-07T10:13:00-04:00
updated: 2026-07-07T10:13:00-04:00
domain: cuzzies
type: decision
status: done
tags: [samira, infrastructure, haven, git]
source: slack
---

# Vault git-branch fork — `main` chosen as sole canonical branch

`main` and `claude/star-crash-thread-context-2npbr` had diverged since ~2026-07-04
with completely unrelated git histories — two different automation triggers were
apparently writing to two different branches. Flagged to Lemar in #decisions
(2026-07-07 09:20 ET) with 3 options; he picked **Option A** (✅ on the reply):
treat `main` as canonical (it's what this session's bootstrap already reads as the
repo's default branch, confirmed via the GitHub API `default_branch: main`), port
the handful of `star-crash`-only 7/7-morning items onto `main`, then archive/delete
the stale branch.

## What was done
Ported the 6 items that existed only on `star-crash` onto `main` (verified each was
genuinely missing, not a duplicate):
- `10-Personal/2026-07-07-trading-cards-side-hustle.md`
- `10-Personal/Health/2026-07-07-basketball-fitness-plan.md`
- `20-Cuzzies/2026-07-07-cuzzies-mail-redirect-options.md`
- `10-Personal/2026-07-07-lexus-ls400-friend-deal.md`
- `20-Cuzzies/2026-07-07-eddie-osefo-followup-email.md`
- Jerzey Grown call outcome appended as an `## Update` to the existing active note
  `20-Cuzzies/2026-07-05-jarred-jerzeygrown-business-call.md` (schema §7 — same
  matter, not a new note)

Two other star-crash-only items (Eddie/Happy Eddie meeting note, Anthropic billing
note) were already properly filed on `main` — nothing to port.

## Not done
Did NOT delete/archive the `claude/star-crash-thread-context-2npbr` branch — no way
to verify from this session whether a live RemoteTrigger still points at it, and
branch deletion is irreversible. Left for Lemar to confirm directly in GitHub
Settings. Two accidental commits I made to that branch early in this same run (before
catching the fork) are harmless — same content now lives correctly on `main`.

## Sources
- slack: #decisions, 2026-07-07 09:20:24 ET (TS 1783430424.691769), Lemar's ✅ on
  Option A at TS 1783430430.887739
- slack: my reply confirming completion, TS 1783433587.851119
