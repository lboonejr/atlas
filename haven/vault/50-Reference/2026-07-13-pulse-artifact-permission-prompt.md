---
created: 2026-07-13T09:05-04:00
updated: 2026-07-13T18:05-04:00
domain: reference
type: note
status: awaiting-decision
tags: [atlas-system, pulse-dashboard, permissions, tooling]
source: slack
---

# Pulse skill — stop the per-run artifact permission prompt

Lemar (#atlas, 2026-07-13 05:50 EDT): "Atlas I want to make a change to my Pulse skill
where it doesn't ask me for permission to build an artifact every run."

## What this is
Lemar wants the friction removed where he's asked to approve/allow the tool call before
Pulse (re)publishes its dashboard artifact each run.

## Why it's not a simple fix
- The `pulse-dashboard` skill itself (`.claude/skills/pulse-dashboard/SKILL.md`) already
  documents that Samira's automated hourly render is unattended — "no one approves
  anything at runtime." So the prompt Lemar is hitting is most likely happening on a
  surface where HE runs Atlas/Pulse interactively (desktop/phone Claude Code session),
  not in Samira's cloud run.
- The actual gate is a Claude Code **tool-permission setting** (governs the `Artifact`
  tool), not skill logic. Checked this repo (`lboonejr/atlas`, default branch) for a
  committed `.claude/settings.json` / `settings.local.json` — none exists. That means
  the permission prompt is controlled by config that lives outside this repo (on
  Lemar's local machine, or in whichever session/environment he's running Pulse from),
  so Samira/Atlas has no file here to edit that would fix this.
- Even if a settings change is the right move, it would typically allow-list the
  `Artifact` tool broadly (not scoped to "only when the pulse-dashboard skill runs") —
  worth Lemar knowing before approving it, since it would reduce prompts for artifact
  publishing generally, not just Pulse.

## Open question
Posted a clarifying card to #decisions asking which surface this happens on and whether
he wants the `Artifact` tool broadly allow-listed (via the `update-config` skill /
`.claude/settings.json` on the surface he uses) versus some narrower fix. Leaving
`domain` unresolved — this is an Atlas/tooling meta-request, not personal/cuzzies/
station/project/reference/legal.

## Update 2026-07-13 13:35 ET
Lemar answered in the #decisions thread: he sees the prompt on **Claude Code on his
phone**, and confirmed he wants the `Artifact` tool allow-listed generally (not scoped
to just Pulse).

Action taken: added `.claude/settings.json` to this repo (via the `update-config`
skill) with `permissions.allow: ["Artifact"]`, committed straight to `main` per this
repo's git write policy — commit `861e4483a0d92249aac2df9f01ebdb20e4ddbda8`. This
resolves the prompt for any Claude Code session that loads this repo's project
settings. Caveat carried back to Lemar: if his phone session doesn't operate on this
same repo/project, the repo-level setting won't reach it — in that case the fix is
choosing "Always allow" the next time the prompt appears on that device, which Samira
cannot do on his behalf.

Replied "Done ✅" in the #decisions thread. Leaving this note `awaiting-decision` and
`domain` unresolved — separately, Lemar also replied "This is an atlas/tooling
metarequest" on the Haven Inbox stuck-note card without picking one of the six domain
values; asked him to confirm `reference` as the closest fit rather than guessing.

## Update 2026-07-13 (vault-keeper sweep)
Lemar confirmed in the Haven Inbox card thread: "Yes you can move it to tooling" (reply
to Samira's `reference` proposal). Domain resolved to `reference` — filed out of the
Inbox into `50-Reference/` this sweep.

## Sources
- slack: https://newworkspace-zlb6313.slack.com/archives/C0BBWHCJUV9/p1783936218981789 (the #atlas capture)
- slack: #decisions thread, parent ts 1783944688.284069 (surface + allow-list confirmation, reply ts 1783961560.064609)
- slack: #decisions thread, parent ts 1783951524.673069 (Haven Inbox card, domain confirmed ts 1783976896.713689)
- github: commit 861e4483a0d92249aac2df9f01ebdb20e4ddbda8 (.claude/settings.json)
