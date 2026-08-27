# The rework — running the loop on a Claude Teams plan + Tag

Lemar's call, 2026-08-27 (supersedes the earlier same-day "minus the Tag feature"
moment): **the productivity-loop infrastructure gets reworked through a Claude Teams
plan and Claude Tag.** This file is the target architecture and the migration plan.
It amends `decisions.md` (see its Amendment section) and, once merged, drives the
build.

The governing idea: **Teams is the org, Tag is the presence, Haven stays the truth.**
The rework changes *where the intelligence lives* (in Slack, live, under an org) —
it does not change the laws (capture-first, done = a filed Haven note, the send-gate,
the safety floor, one decision surface).

## 1. Target architecture

| Layer | Today | Target |
|---|---|---|
| Org / accounts | Lemar's personal claude.ai account + Arianna's personal account | **Claude Teams org** (becomes the business's org): Lemar on a Premium seat, Arianna on a Standard seat, adjust after a month of real usage |
| In-Slack intelligence | Samira bot (custom Vercel MCP app) posting on hourly scans | **Claude Tag** installed in Marspace: live @Claude in channels, ambient follow-ups, scheduled in-channel jobs |
| Scheduled backbone | Samira hourly RemoteTrigger (11 scans/day) + Dawn (1am) + Basil (11pm) on Lemar's personal account | Phased: routines stay where they are until Tag/org equivalents are proven, then move or retire one at a time (section 3) |
| Shared work | Threads siloed per personal account, relayed via Slack | **Shared org Projects** — one project per major task, both humans inside it, edit/view permissions |
| Source of truth | Haven (`haven/vault/`) | **Unchanged.** Haven remains truth; Slack/Drive/Calendar remain renderings |
| Decision surface | #decisions, reaction engine | **Unchanged** as the surface; who reads the reactions migrates only if Tag proves it can (open item V3) |
| Send-gate | Samira never sends; humans send | **Unchanged**, and now enforced structurally: Tag's admin access bundle gets draft-only scopes |

What Tag takes over (the live half of the organizer/executor):

- Live status answers in any channel ("where are we on Camden Phase 00?") from
  channel history + connected Drive.
- Arianna's in-thread workbench: drafting emails, call scripts, and documents where
  the task lives — her whole executor role without leaving Slack.
- The 3-way group DM as a working surface: lead triage on arrival, drafted replies,
  on-demand open-items summaries.
- The accountability loop (decisions C18–C21): ambient-mode follow-ups are the
  bounded-nudge engine, live instead of hourly.
- Scheduled in-channel jobs: Arianna's daily to-do post, the VA weekly research drop,
  a Friday week-in-review.

What deliberately does NOT move to Tag (at least until parity is proven per phase):

- The deterministic vault machinery: vault-keeper, calendar-sync, the digest +
  `_daily` journal, the state file/watermarks.
- The #decisions reaction engine and PT-card pressure-test loop.
- Dawn's morning brief and Basil's inbox janitor.
- Anything on the MUST-NOT floor: sending, paying, posting publicly, deleting.

## 2. Standing rules for the Tag era

1. **Access bundle = the safety floor, in hardware.** Configure Tag's org credential
   bundle (claude.ai/admin-settings/claude-tag) with read + draft scopes only: Gmail
   drafts yes / send no; Drive read-write inside the project folders; Calendar
   create on the internal calendars, no external invitees; GitHub connector included
   so Tag can file Haven notes (capture-first survives live work). No payment or
   social credentials in the bundle, ever — those stay human.
2. **Lane rule: Tag never acts on #decisions cards.** The card engine stays Samira's
   (or its successor's) until the reaction-engine migration is proven. One message,
   one worker — same doctrine that keeps PART A and PART R off each other's cards.
3. **Persona continuity.** Tag posts as the shared "Claude" bot; keep the persona
   convention (the Basil pattern): work signed "— Samira" (and Dawn/Stormy lines where
   those jobs migrate), so the team-facing identities survive the plumbing change.
4. **Spend caps set before ambient mode goes on.** Org-wide and per-channel caps
   (they hard-decline work when hit — size them so a busy Camden week doesn't stall).
   Channel work bills the org; DMs to Tag bill the individual seat.
5. **Haven writes are the finish line, still.** Tag work that produces something
   durable files the Haven note (via the GitHub connector) or explicitly hands off to
   the scheduled sweep. A Slack-only result is still not done.
6. **Lemar's existing personal account is not merged, moved, or closed** until the
   last routine on it has been rebuilt and verified in the org. Accounts cannot be
   merged into a Teams org; triggers and connector auths do not migrate — every move
   is a rebuild, so the old one keeps running until its replacement is proven.

## 3. Migration phases

**Phase 0 — Stand up (no behavior changes).**
Create the Teams org (Lemar Premium, Arianna Standard) · verify Tag's seat minimum on
a 2-seat org before paying (open item V1) · install Tag in Marspace (Slack owner
account) · configure the access bundle per rule 1 · set spend caps · invite Tag to a
pilot set of channels only: #camden-launch, the 3-way group DM, Arianna's surfaces.
Samira/Dawn/Basil untouched. Exit: Tag answers a status question in #camden-launch
correctly and files a test Haven note through the GitHub connector.

**Phase 1 — Tag takes the live layer (2-week pilot).**
Arianna onboards with Tag as her daily driver · shared org Projects replace
solo-account threads for new tasks · ambient follow-ups switched on in the pilot
channels as the accountability loop · lead intake lands in the 3-way DM for Tag
triage · the per-post social cards and call-confirmation prompts run through Tag.
Samira's hourly scan keeps running everything else; the lane rule keeps them apart.
Exit: two weeks with no doubled work, no missed Haven filings, caps holding.

**Phase 2 — Scheduled jobs migrate one at a time.**
Move each recurring job to a Tag scheduled task (or org Cowork) only when its output
is verified equal for a week against the incumbent: Arianna's daily to-do → VA weekly
research → morning-brief-style summaries → the accountability digest. The vault
machinery (vault-keeper, calendar-sync, state file, `_daily`) moves LAST, and only if
Tag/org scheduling can run it with runbook fidelity; otherwise it stays a RemoteTrigger
routine indefinitely — that is an acceptable end state, not a failure.
Each migration = one #decisions card, per the standing routine-change governance.

**Phase 3 — Decommission the duplicated plumbing.**
Whatever Tag has fully absorbed gets retired with a tombstone (the PART F pattern):
potentially the custom Samira/Dawn Vercel bot apps, the capture DM (if captures move
to @Claude anywhere), individual-account routines. Anchors updated; CHANGELOG entry;
Lemar's personal account only then consolidated or kept as personal-only.

## 4. Open items to verify (gates, not assumptions)

- **V1 — Tag seat minimum.** Sources conflict (2-seat Team floor vs. a 5-seat Tag
  minimum). Confirm before paying; it is the difference between ~$120–150/mo and
  ~$300+/mo.
- **V2 — GitHub connector in the Tag bundle.** Confirm Tag can write to the
  `lboonejr/atlas` repo through the org bundle — this is what keeps "done = a filed
  Haven note" alive for live work. If not, all Tag output routes through the
  scheduled sweep instead.
- **V3 — Reactions.** Confirm whether Tag can read (and respect never-setting)
  Lemar's reaction signals. Until proven, the reaction engine does not migrate.
- **V4 — Scheduled-task fidelity.** Whether a Tag/org scheduled job can execute a
  long runbook deterministically (locks, watermarks). Decides how far Phase 2 goes.
- **V5 — Private-channel behavior** in practice: Tag respects private-channel
  boundaries by design; verify with #camden-launch (client-confidential) before
  ambient mode is enabled there.

## 5. What this changes in the design package

- `prompt-v2.md` section 4 (target infrastructure): the design session should now
  treat Teams + Tag as the decided platform, and produce runbook diffs that assume
  the phase plan above rather than a pure RemoteTrigger world.
- The question bank's theme A/B/C answers stand; the *mechanism* delivering several
  of them (accountability nudges, Arianna's to-do surface, lead triage) is now Tag.
- The reviewer routine (F37–F40) gains one check: Tag health — ambient follow-ups
  firing, spend caps not silently exhausted, bundle scopes unchanged.
