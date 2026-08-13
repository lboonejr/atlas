---
created: 2026-08-13T17:15:00-04:00
updated: 2026-08-13T17:15:00-04:00
domain: automation
type: task
status: active
tags: [samira, routine-health, github, git-write-policy]
source: claude
---

# 27 stranded draft PRs against `main` — a second session-type never got direct-push access

While running this pass of the Samira Atlas Executor routine, this session found
it had been given **branch + draft-PR** git access (create a feature branch, push
there, open a draft PR) rather than the direct-to-`main` access `anchors.md`'s
"Git write policy" row calls for. That policy is explicit: *"Never open a feature
branch + pull request for `haven/vault/**`, `.claude/**`, or any routine/skill
write... If a direct push to `main` is rejected... re-pull and retry the direct
write — do not fall back to a branch+PR."* This session had no direct-push option
to fall back to, so it opened PR #61 as instructed by its own outer harness
(which explicitly requires a designated branch + draft PR) — the same conflict
this note is about.

**Checked `main`'s history and found this is not new** — `git log`/PR list show
main receiving a steady stream of direct commits all day today (e.g. `9b34b61`,
`a9be0ff`, `44635db`), confirming at least one Samira session-type genuinely has
direct-push access and uses it correctly. But `GET /repos/lboonejr/atlas/pulls`
(state=open) returned **27 open draft PRs against `main`**, dated **2026-06-15
through 2026-08-13 today** — every one titled like a Samira/Dawn hourly-scan
digest or a new-skill add, none merged, none closed. This means a second
session-type (or a recurring misconfiguration hitting the same trigger) has been
falling into branch+PR mode for at least two months, and nothing in the routine
ever reconciles those branches back into `main`.

**Not all of it is redundant.** Spot-checked the two newest (today, 2026-08-13):
- **PR #60** ("money-hub: recompute against 2026-08-13, plus same-day car/mom
  revisions") modifies `.claude/anchors.md` to add a **"Cuzzie's (Owners) —
  business money only" reminder-calendar row** that does not exist in `main`'s
  current `anchors.md`, plus `.claude/skills/money-hub/SKILL.md` and the ledger.
  This looks like real, not-yet-landed policy content (a business-vs-personal
  calendar split "locked 2026-08-10" per the PR's own diff) that every session
  reading anchors.md today has been missing.
- **PR #58** ("Add my-writing-style skill, wired to the canonical voice profile")
  — a net-new skill directory; `git ls-tree origin/main` confirms no
  `my-writing-style` path exists on `main` today.

Did **not** attempt to review, merge, or close any of the 27 PRs — that is a
judgment call outside this session's scope (some may be safe to merge, some may
be superseded by later direct-to-main work covering the same ground, and merge
order/conflicts across two months of drift need a human's read, not a guess).
Raised as a #decisions card instead.

## What would need to happen
Someone with repo-admin context needs to decide, per PR, whether to merge,
close-as-superseded, or hand-reconcile. Separately, whatever is producing the
branch+PR session-type (a second RemoteTrigger config? a different invocation
path for on-demand/GitHub-connector sessions vs. the cron RemoteTrigger?) should
either be given direct-push permissions matching `anchors.md`'s policy, or the
routine should be updated to say branch+PR is sometimes unavoidable and add a
reconciliation step so work doesn't silently strand.

## Sources
- GitHub: `lboonejr/atlas` open PRs #19–#60 (27 total, `state=open`, all `draft:
  true`, all base `main` or an already-merged ancestor branch)
- GitHub: PR #60 `get_files` diff (`.claude/anchors.md`, `.claude/skills/money-hub/SKILL.md`,
  `haven/vault/10-Personal/Money/money-hub-ledger.md`)
- Local: `git log --oneline origin/main -5` (confirms same-day direct commits
  landing successfully via a different session/path)
