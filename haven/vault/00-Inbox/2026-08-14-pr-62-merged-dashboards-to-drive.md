---
created: 2026-08-14T10:10:00-04:00
updated: 2026-08-14T10:10:00-04:00
domain: automation
type: decision
status: done
tags: [samira, routine-health, pr-62, dashboards, drive, artifact-tool]
source: slack
---

# PR #62 merged — Pulse/Money Hub/morning-brief/meeting-prep move off Artifact tool to Drive snapshot Docs

Lemar reacted ✅ on the #decisions card (ts `1786713941.609669`, posted by an earlier
pass this run) staging GitHub PR #62 — a proposal opened the previous night (~8pm ET,
2026-08-13) by a separate session that used a feature branch instead of pushing straight
to `main` (a known git-write-policy miss, but this one held real content).

**Decision:** merge it (over the alternative of closing and keeping the Artifact tool).

**Action taken (PART A, this run):** marked the PR ready-for-review (it was left in
`draft` state) via `update_pull_request`, then squash-merged to `main` —
sha `f407f405311871d0eef37353a068cb7f038d2188`.

**What changed:**
- All four dashboard skills (Pulse, Money Hub, morning-brief, meeting-prep) now publish
  a new timestamped Google Doc snapshot per render into `ATLAS/Dashboards/*` in Drive,
  instead of re-deploying to a stable claude.ai artifact URL. Nothing is edited/deleted
  after creation — each folder is its own history.
- `.claude/anchors.md` — Pulse / Money Hub / Morning Brief / Meeting Prep rows replaced
  with the new Drive folder ids + notification behavior.
- `.claude/skills/pulse-dashboard/SKILL.md`, `.claude/skills/money-hub/SKILL.md`,
  `.claude/skills/morning-brief/SKILL.md`, `.claude/skills/meeting-prep/SKILL.md` —
  Output/SAFETY/Returns sections rewritten for the Drive-doc target.
- `.claude/routines/samira-atlas-executor.md` (PART P, PART M), `.claude/routines/daily-brief.md`,
  `.claude/routines/DAILY-BRIEF-TRIGGER.md` — wording updated to match.
- `.claude/CHANGELOG.md` — full writeup, including the two ruled-out alternatives
  (Drive shortcut repoint, Slack canvas pointer — both blocked by platform limits).
- `haven/vault/50-Reference/2026-07-13-pulse-artifact-permission-prompt.md` — closed via
  an `## Update` (status → `done`); the July fix's commit never actually landed in git
  history, which is the root cause this PR resolves.

**Note for this run:** the ANCHORS block this session started with still shows the OLD
stable artifact URLs for Pulse/Money Hub (they were current when this run began). Before
running PART P (Pulse render) and PART M (money-hub, if it renders the dashboard), this
session re-reads the live `.claude/anchors.md` and the relevant skill files rather than
using the stale in-context values, since this merge changed them mid-run.

Replied "Done ✅" in the #decisions thread (ts `1786716585.591279`).

## Sources
- slack: #decisions ts `1786713941.609669` (card) / `1786716585.591279` (Done ✅ reply)
- github: PR https://github.com/lboonejr/atlas/pull/62 (merged `f407f405311871d0eef37353a068cb7f038d2188`)
