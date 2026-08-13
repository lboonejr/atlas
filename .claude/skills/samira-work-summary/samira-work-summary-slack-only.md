# Samira Work Summary — Slack-only (no GitHub) chat / Cowork version

Use this instead of the main `SKILL.md` on any surface that has a **Slack connector but
NOT the GitHub connector** — a plain claude.ai chat, or a Cowork session that isn't
attached to the `lboonejr/atlas` repo. It does the same job (summarize the thread, hand
it to Samira, don't lose the work when the thread closes) but with one deliberate
difference: **it never writes to Haven itself.** It has no repo access to do that write
with. Instead it composes the Slack message so that Samira's *own* scheduled run — which
DOES have GitHub access — lands the Haven note when she processes it. Once it goes to
Slack, that's how it gets pushed to Haven.

If GitHub access IS available in this session, use the real skill
(`.claude/skills/samira-work-summary/SKILL.md`) instead — it lands the Haven note
immediately rather than waiting on Samira's next hourly pass, which is strictly better
whenever it's available.

## What you need
Only the **Slack connector**, connected to the "Marspace" workspace, using Lemar's own
account (the standard personal connector — not a dedicated bot identity, which this
surface won't have wired up anyway). No GitHub, no other connector required.

## Known hardcoded values (duplicated here on purpose — see "On drift" below)
- **Samira capture DM**: `D0BHPKMDNEP` (Lemar's DM with Samira's bot). The only DM
  target — never invent a different one.
- There is no live channel table to consult here (that lives in `.claude/anchors.md`,
  repo-only) — find the right channel by searching Slack directly (see Step 2).

## Step 1 — Summarize the thread
Same as the full skill: what this thread is, state (done / in progress / blocked),
decisions Lemar actually made, open questions, and — if the work isn't finished — one
concrete recommended next step. Decide the mode:
- **CONTINUE** — unfinished, with a concrete next step Samira could execute.
- **ARCHIVE** — finished, or nothing actionable left; this is purely a record.

## Step 2 — Route it in Slack (this IS the whole delivery mechanism)

**First, look for a home.** Search Slack for a channel whose name, topic, or recent
history is a genuine match for the thread's subject (`slack_search_channels`,
`slack_read_channel`) — never post on a loose name match alone.

### A channel is a clear fit
Post there, top-level, un-reacted, starting with the globe emoji, **addressed to Samira
by name so her PART C sweep recognizes it as an instruction to run**, not just chatter:
- **CONTINUE mode** — either fence the concrete next step:
  ```
  ===ATLAS PROMPT START | task:[slug] | run:admin-3x===
  [self-contained: the skill/tool to use, the IDs/links needed, the one concrete outcome
  — including "record this in Haven" as part of the outcome, since nothing has written
  it there yet]
  ===ATLAS PROMPT END===
  ```
  or, if a fence is overkill for something simple, write it as a plain named
  instruction: "Samira, [do the concrete next step] — see the summary above, and land
  the record in Haven when you do." Use `run:manual` (or no fence at all, just the
  summary) instead if this genuinely needs Lemar's own hands, not Samira's.
- **ARCHIVE mode** — there's no action for Samira to execute, only a record to file, so
  say that explicitly: "Samira, save this thread summary to Haven as a record — [type
  hint: decision if it recorded a choice Lemar made, else a plain log]: [the Step 1
  summary]." That phrasing is what makes it a "named instruction" PART C's sweep will
  actually run, rather than a status update it skips as chatter.

### No clear channel fit
DM the **Samira capture DM** (`D0BHPKMDNEP`) instead — never create a channel, never
invent a different DM. Write it **exactly as Lemar would type a raw brain-dump**: no
globe emoji, not addressed to Samira by name, just the Step 1 summary in plain
first-person register. Posted from Lemar's own Slack account with no reaction, that's
indistinguishable from a real top-level capture, so Samira's PART B sweep ("a top-level
message in that DM from Lemar, not a bot post, with no status reaction") develops it —
probe, land the Haven note, find the home, stage — on her own next scan.

## Step 3 — Tell Lemar where it went
One or two lines: the mode, and where it went — "posted to #channel, Samira will run it
and land the Haven record on her next hourly scan" or "DM'd Samira, she'll develop it and
land the Haven record on her next hourly pass." **Never say it's "saved to Haven" or
"filed"** — this version can't confirm that write happened, only that it handed Samira
the material to do it. Samira's cadence is hourly, roughly 8am–6pm ET — so say "next
scan," not "now."

## Hard floor
Never send email or any outward-facing action, never pay or transfer anything, never
post outside the matched channel or the capture DM, never create a new Slack channel,
never claim a Haven write happened that this surface didn't (and can't) perform itself.

## On drift
This file hardcodes the capture DM id because it has no repo access to read
`.claude/anchors.md` live. If that ID (or the workspace) ever changes, this file goes
stale until someone updates it by hand — unlike the main skill, which always reads
anchors.md fresh. Prefer the main skill whenever GitHub access is available; treat this
file as the fallback for when it genuinely isn't.
