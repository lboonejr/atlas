---
created: 2026-09-12T14:04:00-04:00
updated: 2026-09-12T14:04:00-04:00
domain: automation
type: log
status: done
tags: [fixes, reports-contradiction, git, stale-checkout, vault-keeper]
source: slack
---

# #reports false "Inbox empty / no due notes" claim — root cause found: stale local checkout

## What happened
A #reports post 2026-09-12 ~13:54 ET, signed "Haven Keeper" via "Sent using Claude"
(Slack `app_id: A08SF47R6P4`, posted as Lemar's own user `U0BC5UTHYG4` — the same
identity/app pattern as the `samira-work-summary` auto-handoffs, i.e. a separate live
Claude Code session, not this hourly routine's bot `U0BJQ771LJU`/`A0BHSG2CA7P`), ts
`1789219244.229999`, claimed: "Inbox empty, nothing to file. No notes in the vault
carry a `due` field, so nothing to ring." This is false — 5 notes were sitting in
`00-Inbox/` at the time (unchanged from every recent scan) and dozens of vault notes
carry `due`.

Flagged as a #fixes card (`C0BV5BRNH5Z` ts `1789223860.933709`); Lemar picked Option 2
— investigate.

## Root cause (found this run, reproduced firsthand)
This run's own local git clone of `lboonejr/atlas` started on branch `main` but had
**diverged from `origin/main` by 52 local-only commits vs. 50 remote-only commits** —
a stale/mismatched checkout, not a fresh clone in the state the environment description
implies. `git diff --stat HEAD origin/main` showed 76 files different, including recent
`haven/vault/00-Inbox/` and `_daily/` content — i.e. reading the vault from that
checkout would have shown an incomplete/wrong picture, potentially including an
apparently-empty Inbox depending on which historical commit the stale ref actually
pointed to.

This is almost certainly what happened to the "Haven Keeper" session: it trusted a
local clone that looked present but wasn't actually synced to current `main`, read an
empty or outdated `00-Inbox/`/vault tree, and reported a false-clean result without
ever checking `git diff` against the remote.

## Fix applied
Added a mandatory freshness check to the runbook's "Prefer the local clone" section
(`.claude/routines/samira-atlas-executor.md`): before trusting a local clone for any
vault read or write, run `git fetch origin main && git diff --stat HEAD origin/main`;
a non-empty diff means fix it first (`git branch -f main origin/main && git checkout
main && git reset --hard origin/main`) before reading. Only report a vault state after
confirming zero diff. Applies to every session touching this vault, not just Samira's
hourly run — since the false claim came from a *different* session entirely, the fix
had to live in shared/discoverable guidance, not just this routine's own PART 1.

## What this doesn't fix
Nothing forces a random live Claude Code session (invoked directly by Lemar outside
this routine) to actually read this runbook before touching the vault. This closes the
gap for anyone who does read it; it can't close the gap for one that doesn't. No
further action recommended beyond the runbook edit — flagging this residual limit for
awareness rather than proposing unattended enforcement Samira has no way to add.

## Sources
- slack: #fixes `C0BV5BRNH5Z` ts `1789223860.933709` (finding + Option 2 pick, reply
  `1789230719.385119`)
- slack: #reports `C0BBZJL85RT` ts `1789219244.229999` (the false claim)
- git: this run's own clone, `HEAD` vs `origin/main` before reset — 76 files / 52 vs 50
  diverged commits, confirmed via `git diff --stat` and `git merge-base --is-ancestor`
