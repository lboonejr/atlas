---
created: 2026-07-08T14:15-04:00
updated: 2026-07-08T14:15-04:00
domain: project
type: decision
status: done
tags: [samira, infra, git, main-branch]
source: slack
---

# Git write policy — no branch+PR for vault/skill writes (Lemar's call)

Follow-up to the 2026-07-08 ~13:20 ET PR-merge-gap diagnosis (two hourly scans had used
a local git-branch-and-PR flow instead of writing straight to `main`, stranding their
vault work — PRs #34/#35). Samira asked Lemar in `#decisions` (thread
1783526956.196649) whether to flip the repo's "Allow auto-merge" setting or add explicit
no-PR guidance to `CLAUDE.md`/`anchors.md`.

**Lemar's answer** (2026-07-08 1:23pm ET, plain-text reply): *"add the line to
CLAUDE.md/anchors.md."*

## What ran
No `CLAUDE.md` exists in the repo, so the guidance went into `.claude/anchors.md`'s
Repo/vault table: a new **Git write policy** row stating every session (Samira hourly
scan, Dawn's daily run, or a one-off session) must commit and push directly to `main`
for any `haven/vault/**`, `.claude/**`, or routine/skill write — never a feature
branch + PR — and to re-pull and retry on a rejected direct push rather than falling
back to branch+PR. Also corrected the now-stale "canonical branch" row (the flip to
`main` as default is confirmed live, not pending). Committed and pushed straight to
`main` (commit `339dca9`), same scan the FundCanna capture and investor-index update
landed.

## Sources
- slack: https://newworkspace-zlb6313.slack.com/archives/C0BBXA96FFV/p1783531435148299 (Lemar's answer)
- slack: https://newworkspace-zlb6313.slack.com/archives/C0BBXA96FFV/p1783534511400979 (Samira's Done ✅ reply)
- github: commit 339dca9 on `main`
