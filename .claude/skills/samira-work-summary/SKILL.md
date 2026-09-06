---
name: samira-work-summary
description: >
  Lemar's thread-to-Samira handoff — usable from ANY live Claude session, Claude Code or
  chat. Summarizes what he's been working on in the current thread (state, decisions
  made, files/code touched, open questions, recommended next step), lands it in Haven
  FIRST as the durable record (via haven-capture), then routes it in the Marspace
  Slack workspace: unfinished work (CONTINUE mode) goes as a plain, un-🌐-prefixed
  top-level drop in Lemar's SELF-DM (Convo 2, via the personal Slack connector),
  written exactly the way Lemar himself would drop a brain-dump, so Samira's hourly
  PART 4 sweep develops it the same as anything else he types there; finished work
  (ARCHIVE mode) is the Haven note plus ONE append-only timeline entry in the matching
  project channel. Use whenever Lemar wants the state of a thread handed off to Samira
  — "give Samira a summary of this", "loop Samira in", "hand this off to Samira", "let
  Samira continue this", "keep Samira posted on this thread", "save this thread to
  Haven", "Samira, pick this up", "brief Samira on where I left off", or at the
  natural end or pause of a work session he wants tracked instead of lost when the
  thread closes. It never sends outward-facing actions, never pays, never posts
  outside the self-DM, the matched timeline channel, or the Convo 1 courtesy
  fallback, and never claims a handoff landed unless the Haven write actually
  succeeded.
---

# Samira Work Summary — thread-to-Samira handoff

Any live Claude thread — a Claude Code session on this repo, or a plain claude.ai chat —
can reach a point where Lemar wants to step away and have Samira either **keep pushing
the work forward** or **just file the record** so nothing said in the thread evaporates
when it closes. This skill is that off-ramp. It does three things, in order, every time:
**(1) summarize the thread → (2) land it in Haven → (3) route it in Slack** so Samira
actually sees it on her own schedule instead of it dying in a closed tab.

This is a lighter, on-demand cousin of Atlas Gear 2 — reuse its judgment, don't
reinvent it — but it never creates a new Slack channel, never opens a card itself, and
its whole delivery mechanism is the intake surface Samira already sweeps.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it before routing anywhere.
Constants this skill uses:
- Vault: `haven/vault/` on repo `lboonejr/atlas`, default branch. Writes go through
  **haven-capture** only — never hand-write a note.
- Slack workspace "Marspace": the channel table in anchors.md, plus **Convo 2 — Lemar's
  SELF-DM** `D0BBVV54L5R` (the intake notepad, reachable ONLY via the personal Slack
  connector — a bot cannot enter a self-DM) and **Convo 1 — the Samira bot DM**
  `D0BHPKMDNEP` (the card surface; used here only as the bot-only courtesy fallback).
  Never invent a different DM.
- Two Slack identities, and which one matters here: the **shared personal connector**
  (posts as Lemar's own Slack account — what a live Atlas/Claude session uses, and the
  ONLY way into the self-DM) vs. **Samira's dedicated bot** (`mcp__Samira__*`, posts as
  a separate bot user, always 🌐-signed). Which one is reachable decides the route
  (see Step 3).
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

## Step 3 — Route it by mode (the fenced-prompt-to-channel era is over)

Fenced-prompt staging to project channels ENDED with the 2026-09-06 restructure —
project channels are append-only timelines nobody sweeps, so a prompt posted there
would sit forever. The route now follows the Step 1 mode:

### CONTINUE mode → a plain drop in Lemar's self-DM (Convo 2)
Post the handoff as a **plain, un-🌐-prefixed top-level message in Lemar's SELF-DM**
(`D0BBVV54L5R`), **via the shared personal Slack connector** (the only identity that
can reach a self-DM — Samira's bot cannot enter it). Do NOT prefix it with 🌐. Written
that way, it lands in the notepad exactly as if Lemar had typed it himself, and
Samira's PART 4 sweep ("a top-level message without a 🌐 prefix, with no status
reaction") treats it as a genuine new capture and develops it — Haven-checked,
probed, graduated into a doctrine-format Convo 1 card — on her own next hourly scan.
Write the message self-contained enough that the probe step finds it "already
answered": the Step 1 summary plus the recommended next step, in Lemar's-brain-dump
register, not a status report register.

```
[what this thread is about, in one line]
[the state / decision / next step, written plainly — this is what Samira develops]
Haven note: <path>
```

(The note path is fine to include — PART 4's quick-update routing uses it to find the
matter instead of opening a duplicate.)

### ARCHIVE mode → the Haven note + ONE timeline entry
The record is already landed (Step 2). If a project channel in the anchors table
obviously matches the thread's subject, append ONE 🌐-led timeline entry there —
top-level, one or two lines, append-only, linking the Haven note:
```
🌐 [what this thread was] — ARCHIVE
[one line of what happened / was decided]
Haven note: <path>
— Samira
```
Never edit or delete a prior entry, and never post a timeline entry expecting anyone
to sweep it — it's a record for Lemar to look back on. No matching channel → the Haven
note alone IS the record; post nothing.

### Fallback — only the bot connector is reachable
If the personal connector isn't available in this session (so the self-DM is out of
reach), post a **🌐-signed courtesy record in Convo 1** (`D0BHPKMDNEP`) via the bot,
explicitly flagged in the message as **not auto-swept** — a 🌐 bot post in Convo 1 is
never card input, so it needs Lemar or a live Samira turn to notice it. Say so plainly
to Lemar; never claim it'll be picked up automatically when it won't be.

## Step 4 — Tell Lemar where it landed

One or two lines, plain: the mode (CONTINUE/ARCHIVE), the Haven note path, and where it
went — "dropped it in your self-DM, Samira's PART 4 sweep will develop it into a card
on her next hourly pass", or "filed in Haven + one line on the #channel timeline" (or,
in the bot-only fallback case, "posted a courtesy record in your Samira DM — flag it to
her live if you want it acted on sooner").

## What this skill does not do
It never sends outward-facing actions (email, public posts, payments) — only internal
Haven writes and internal Slack posts to Marspace. It never creates a new Slack channel
and never opens a Convo 1 card itself — graduating a drop into a card is PART 4's job
(unlike Atlas Gear 2 — this is a lighter, on-demand tool; if the same kind of thread
keeps landing in the self-DM, that's a signal for a real project timeline, which is
Lemar's or Atlas's call, not this skill's). It never re-derives or duplicates a Haven
note for the same matter — haven-capture's own step-zero dedupe (schema §7) handles a
thread that's a continuation of an already-open matter.

## No-GitHub chat / Cowork surfaces
This version needs the GitHub connector (to write the Haven note directly, via
haven-capture) and lands the record instantly. On a surface with a Slack connector but
NO GitHub access — a plain claude.ai chat, or a Cowork session not attached to this repo
— use **`samira-work-summary-slack-only.md`** in this same folder instead: it skips the
direct Haven write and composes the Slack message so Samira's own scheduled run (which
does have GitHub access) lands the record when she processes it on her next scan. Prefer
this version whenever GitHub access is available.
