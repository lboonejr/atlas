---
name: samira-work-summary
description: >
  Lemar's thread-to-Samira handoff — usable from ANY live Claude session, Claude Code or
  chat. Summarizes what he's been working on in the current thread (state, decisions
  made, files/code touched, open questions, recommended next step), lands it in Haven
  FIRST as the durable record (via haven-capture), then finds the thread's home in the
  Marspace Slack workspace: an existing project channel gets a fenced ready-to-run
  prompt that Samira's hourly sweep (PART C) picks up and continues automatically; no
  clear home falls back to a plain top-level drop in Lemar's capture DM with Samira's
  bot, written exactly the way Lemar himself would drop a brain-dump, so her PART B
  sweep develops it the same as anything else he types there. Use whenever Lemar wants
  the state of a thread handed off to Samira — "give Samira a summary of this", "loop
  Samira in", "hand this off to Samira", "let Samira continue this", "keep Samira
  posted on this thread", "save this thread to Haven", "Samira, pick this up", "brief
  Samira on where I left off", or at the natural end or pause of a work session he
  wants tracked instead of lost when the thread closes. It never sends outward-facing
  actions, never pays, never posts outside the matched channel or the capture DM, and
  never claims a handoff landed unless the Haven write actually succeeded.
---

# Samira Work Summary — thread-to-Samira handoff

Any live Claude thread — a Claude Code session on this repo, or a plain claude.ai chat —
can reach a point where Lemar wants to step away and have Samira either **keep pushing
the work forward** or **just file the record** so nothing said in the thread evaporates
when it closes. This skill is that off-ramp. It does three things, in order, every time:
**(1) summarize the thread → (2) land it in Haven → (3) route it in Slack** so Samira
actually sees it on her own schedule instead of it dying in a closed tab.

This is a lighter, on-demand cousin of Atlas Gear 2 ("find the home," stage a prompt) —
reuse that logic, don't reinvent it — but it never creates a new Slack channel, and its
no-home fallback is a DM to Samira instead of standing up a new surface.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it before routing anywhere.
Constants this skill uses:
- Vault: `haven/vault/` on repo `lboonejr/atlas`, default branch. Writes go through
  **haven-capture** only — never hand-write a note.
- Slack workspace "Marspace": the channel table in anchors.md, plus the **Samira capture
  DM** `D0BHPKMDNEP` (Lemar ↔ Samira's bot) — the ONLY DM target, never invent a new one.
- Two Slack identities, and which one matters here: the **shared personal connector**
  (posts as Lemar's own Slack account — what a live Atlas/Claude session uses) vs.
  **Samira's dedicated bot** (`mcp__Samira__*`, posts as a separate bot user, always
  🌐-signed). Use whichever is reachable in this session; which one you use changes how
  the message downstream is read (see Step 3).
- Git-write policy: commit straight to `main` (no feature branch/PR for Haven or skill
  writes — see anchors.md's "Git write policy" row).

---

## Step 1 — Summarize the thread

Read back over the current conversation (and, in a Code session, `git log`/`git diff`/
the PR if one exists) and write a tight summary, skipping any section with nothing to
say:
- **What this thread is** — one line: the task, project, or question it's about.
- **State** — what's done, what's in progress, what's blocked.
- **Decisions made** — any choice Lemar actually made in the thread (these matter for
  Step 2's `type` call).
- **Files/code touched** — for a Code session: files changed, the branch, PR link/number
  if one exists.
- **Open questions** — anything genuinely unresolved that the next person needs an
  answer to before continuing.
- **Recommended next step** — one concrete action, if the work isn't finished. This is
  what becomes the fenced prompt in Step 3, if anything.

Decide the **mode** up front, it drives everything downstream:
- **CONTINUE** — work is unfinished and there's a concrete next step Samira (or a future
  Claude session) could execute.
- **ARCHIVE** — work is finished, or there's nothing actionable left; this is purely a
  record.

## Step 2 — Land it in Haven (capture-first is law, same as everywhere else in this repo)

Call **haven-capture** with the Step 1 summary as the body. Stamp only what you're sure
of, per haven-capture's own discipline:
- **`type`** — the decision rule (schema §3) wins first: if the thread recorded a real
  choice Lemar made, `type: decision`. Otherwise: `task` + `status: active` for CONTINUE
  mode (the next step IS the point of the note); `log` + `status: done` for ARCHIVE mode.
- **`source: claude`** — always, this is a Claude-session capture.
- **`domain`** — only if the thread's subject is unambiguous (cuzzies / station /
  personal / project / reference / legal / automation); otherwise leave UNRESOLVED.
- **`tags`** — `[samira, work-summary, <topic tags>]`.
- **Body** — the Step 1 summary, plus a `## Handoff` section carrying the recommended
  next step verbatim (this is what Step 3's fenced prompt echoes), plus a `## Sources`
  block: for Code, the repo/branch/PR; for chat, "claude: chat session, `<date>`."

If the Haven write fails, **stop and say so** — do not proceed to Slack, and do not tell
Lemar the handoff landed. No note, no handoff.

## Step 3 — Route it: find the home, or fall back to Samira's DM

**First, check `.claude/anchors.md`'s channel table** for a project channel that
obviously matches the thread's subject. **If nothing's obvious**, search Marspace
(`slack_search_channels`, whichever Slack tool is reachable) for a channel whose name,
topic, or recent history is a genuine fit — never post on a loose name match alone.

### A channel is a clear fit
Post there, top-level, un-reacted, 🌐-led (Atlas's Slack message rules):
```
🌐 [what this thread is] — [CONTINUE or ARCHIVE, one line]
[the Step 1 summary, tightened for Slack]
Haven note: <path>
```
CONTINUE mode with a concrete next step → append the fenced prompt so Samira's PART C
sweep (which reads every channel except #reports/#decisions/#stormy/the capture DM) picks
it up on her next scan:
```
===ATLAS PROMPT START | task:[slug] | run:admin-3x===
[self-contained: the skill/tool to use, the IDs/links needed, the one concrete outcome]
===ATLAS PROMPT END===
```
Use `run:manual` instead if this genuinely needs Lemar's own hands. Never pre-react your
own post — the ✅ is Samira's done-key once she runs it.

### No clear channel fit
Fall back to the **Samira capture DM** (`D0BHPKMDNEP`) — never create a channel, never
invent a different DM. **Post it via the shared personal Slack connector, not Samira's
bot, and do NOT prefix it with 🌐.** Written that way, it lands in the DM exactly as if
Lemar had typed it himself, and Samira's PART B sweep ("a top-level message in that DM
from Lemar, not a 🌐 bot post, with no status reaction") treats it as a genuine new
capture and runs Atlas's Capture & Develop gear on it — probe, develop, find the home,
stage — on her own next hourly scan. Write the message self-contained enough that the
probe step finds it "already answered": the Step 1 summary plus the recommended next
step, in Lemar's-brain-dump register, not a status report register.

```
[what this thread is about, in one line]
[the state / decision / next step, written plainly — this is what Samira develops]
```

If only Samira's dedicated bot connector is reachable (no personal-connector path in this
session), post it 🌐-signed via the bot instead, and say so plainly to Lemar: this path
is a courtesy record only — it will NOT be auto-swept (the capture DM is excluded from
PART C, and a 🌐-signed bot post is excluded from PART B), so it needs Lemar or a live
Samira turn to notice it. Never claim it'll be picked up automatically when it won't be.

## Step 4 — Tell Lemar where it landed

One or two lines, plain: the mode (CONTINUE/ARCHIVE), the Haven note path, and where it
went — "posted to #channel, Samira's PART C sweep will run it next scan" or "DM'd Samira,
she'll pick it up developing it on her next hourly pass" (or, in the bot-only fallback
case, "DM'd Samira as a record — flag it to her live if you want it acted on sooner").

## What this skill does not do
It never sends outward-facing actions (email, public posts, payments) — only internal
Haven writes and internal Slack posts to Marspace. It never creates a new Slack channel
(unlike Atlas Gear 2 — this is a lighter, on-demand tool; if the same kind of thread
keeps landing in the capture-DM fallback, that's a signal for a real project channel,
which is Lemar's or Atlas's call, not this skill's). It never re-derives or duplicates a
Haven note for the same matter — haven-capture's own step-zero dedupe (schema §7) handles
a thread that's a continuation of an already-open matter.
