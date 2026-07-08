---
created: 2026-07-08T08:20-04:00
updated: 2026-07-08T08:20-04:00
domain: project
type: task
status: awaiting-decision
tags: [dawn, daily-brief, artifact, feature-request, samira]
source: slack
---

# Dawn artifact — chat bubbles linking flagged items to their Slack thread

Lemar posted in #atlas (2026-07-08 07:56 ET): he wants to be able to address issues
directly on the Dawn morning-brief artifact — thinking chat bubbles that link to the
Slack thread in question, so he can update those situations "directly" from the
artifact rather than going back into Slack to find the thread.

## What's clear
- Target is the Dawn/morning-brief system (`.claude/skills/morning-brief`,
  `.claude/skills/meeting-prep`), which currently re-deploys a static living artifact
  to a stable URL each run (see [[2026-07-05-dawn-routine-built]] and the "Living brief
  artifact URL" / "Living meeting-prep artifact URL" rows in anchors.md).
- The shape he's describing: each flagged loop/goal on the artifact gets a small
  UI element (a "chat bubble") that deep-links out to the originating Slack thread.

## What's genuinely open (not safe to guess and build)
1. **Scope** — just the morning-brief artifact, or meeting-prep too (both are separate
   living artifacts per anchors.md)?
2. **"Update directly" — read-only deep link, or an actual write-back?** A simple
   link-out (click the bubble → opens the Slack thread in a new tab) is a small,
   safe addition. A true in-artifact write-back (typing a reply that posts to Slack
   from the artifact itself) is a materially bigger build — Claude Artifacts are
   static HTML with no live backend, so a real write-back would need a separate
   mechanism (e.g. a form that opens a pre-filled Slack deep link, since the artifact
   can't call the Slack API directly). Building the wrong one wastes real effort.

Posted the scope/shape question to #decisions rather than guessing — see that thread.
No fenced build prompt staged yet; this resumes once Lemar answers.

## Sources
- slack: #atlas https://newworkspace-zlb6313.slack.com/archives/C0BBWHCJUV9/p1783511790997129 (2026-07-08 07:56:30 EDT)
