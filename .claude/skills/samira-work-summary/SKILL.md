---
name: samira-work-summary
description: >
  Lemar's thread-to-Samira handoff — usable from ANY live Claude session, Claude Code or
  chat. Summarizes what he's been working on in the current thread (state, decisions
  made, files/code touched, open questions, recommended next step), lands it in Haven
  FIRST as the durable record (via haven-capture), then drops it on the ONE
  conversation Samira sweeps for that kind of thing. Work threads (both CONTINUE and
  ARCHIVE) go as a plain, un-🌐-prefixed top-level drop in Lemar's SELF-DM (Convo 2,
  via the personal Slack connector), written exactly the way Lemar himself would drop
  a brain-dump, so Samira's hourly PART 4 sweep develops it the same as anything else
  he types there — including posting the project timeline entry, which this skill
  never writes itself. A thread whose subject is Samira HERSELF (a broken routine, a
  stale skill, a connector gap) drops in #fixes (Convo 3) instead, where PART 5 opens
  it as a fix card. Use whenever Lemar wants the state of a thread handed off to
  Samira — "give Samira a summary of this", "loop Samira in", "hand this off to
  Samira", "let Samira continue this", "keep Samira posted on this thread", "save this
  thread to Haven", "Samira, pick this up", "brief Samira on where I left off", or at
  the natural end or pause of a work session he wants tracked instead of lost when the
  thread closes. It never sends outward-facing actions, never pays, never posts
  outside the self-DM, #fixes, or the Convo 1 courtesy fallback, and never claims a
  handoff landed unless the Haven write actually succeeded.
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
its whole delivery mechanism is the intake surfaces Samira already sweeps.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it before routing anywhere.
Constants this skill uses:
- Vault: `haven/vault/` on repo `lboonejr/atlas`, default branch. Writes go through
  **haven-capture** only — never hand-write a note.
- Slack workspace "Marspace": the channel table in anchors.md. The three conversations,
  and what each is to this skill:
  - **Convo 2 — Lemar's SELF-DM** `D0BBVV54L5R` — the intake notepad, and this skill's
    default target. Reachable ONLY via the personal Slack connector (a bot cannot enter
    a self-DM). Swept in PART 4.
  - **Convo 3 — #fixes** `C0BV5BRNH5Z` (private) — where anything wrong with Samira
    herself gets worked. The target when the thread's subject IS her. Swept in PART 5.
  - **Convo 1 — the Samira bot DM** `D0BHPKMDNEP` — the card surface. Used here ONLY as
    the bot-only courtesy fallback; this skill never opens a card on it.

  Never invent a different DM or channel. Project channels are append-only TIMELINES
  (since 2026-09-06) — this skill never posts to one (see Step 3).
- Two Slack identities, and which one matters here: the **shared personal connector**
  (posts as Lemar's own Slack account — what a live Atlas/Claude session uses, and the
  ONLY way into the self-DM) vs. **Samira's dedicated bot** (`mcp__Samira__*`, posts as
  a separate bot user, always 🌐-signed). The thread's SUBJECT decides the route (Step 1);
  which identity is reachable only decides whether you get the real route or the
  courtesy fallback (see Step 3).
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
  what carries the drop in Step 3, if anything.

Then two calls, in this order — the subject decides the surface, the mode decides how the
drop reads:

**First, the SUBJECT test — whose problem is this?**
- **FIX** — the thread's subject is *Samira herself*: a routine that misfired, a skill or
  doctrine file that's stale or self-contradicting, a connector/access gap, a wrong or
  duplicated output she produced. Anything you'd describe as "she's broken" rather than
  "this project needs work." → Convo 3, and the mode call below doesn't apply.
- **WORK** — everything else: Lemar's own projects, decisions, and tasks. → Convo 2, and
  the mode call decides how the drop reads.

**Then, for WORK threads, the MODE:**
- **CONTINUE** — work is unfinished and there's a concrete next step Samira (or a future
  Claude session) could execute.
- **ARCHIVE** — work is finished, or there's nothing actionable left; this is purely a
  record.

A thread can look like both (you fixed a Samira bug *while* doing project work). Route on
what the handoff is actually asking for: if the thing that still needs doing is hers, it's
FIX; if it's the project's, it's WORK. Never split one thread across two surfaces.

## Step 2 — Land it in Haven (capture-first is law, same as everywhere else in this repo)

Call **haven-capture** with the Step 1 summary as the body. Stamp only what you're sure
of, per haven-capture's own discipline:
- **`type`** — the decision rule (schema §3) wins first: if the thread recorded a real
  choice Lemar made, `type: decision`. Otherwise: `task` + `status: active` for CONTINUE
  mode (the next step IS the point of the note); `log` + `status: done` for ARCHIVE mode.
- **`source: claude`** — always, this is a Claude-session capture.
- **`domain`** — only if the thread's subject is unambiguous (cuzzies / station /
  personal / project / reference / legal / automation); otherwise leave UNRESOLVED. A
  FIX thread is always `domain: automation` — that's what the subject test established.
- **`tags`** — `[samira, work-summary, <topic tags>]`; add `fix` on a FIX thread.
- **Body** — the Step 1 summary, plus a `## Handoff` section carrying the recommended
  next step verbatim (this is what Step 3's drop echoes), plus a `## Sources` block: for
  Code, the repo/branch/PR; for chat, "claude: chat session, `<date>`."

If the Haven write fails, **stop and say so** — do not proceed to Slack, and do not tell
Lemar the handoff landed. No note, no handoff.

## Step 3 — Drop it on the surface that sweeps it (subject first, then mode)

Two rules set by the 2026-09-06 restructure govern everything here:

**Project channels are out of reach.** Fenced-prompt staging to them ENDED with the
restructure — they're append-only timelines nobody sweeps, so anything posted there sits
forever. **This skill never posts a timeline entry at all**, not even a record: PART 4
writes the entry for a Convo 2 drop it develops, and PART 7 writes one at the end of every
run for each project that moved. Writing one here would either duplicate theirs or land
misattributed (see below).

**🌐 is not yours to use.** The prefix means "Samira wrote this," and a 🌐 message is never
treated as input by any sweep. A live Claude session posts through the personal connector
*as Lemar* — so a 🌐-led, "— Samira"-signed post from here would both misattribute the
message and make it invisible to the sweep that was supposed to pick it up. Every drop
this skill writes is plain and un-prefixed. The one exception is the bot-only fallback at
the bottom, where the bot genuinely is the author.

And one mechanical rule that applies to every branch: **never react to your own drop.**
Both sweeps skip a message that already carries a status reaction (PART 4 and PART 5
alike), so a pre-reacted drop is an invisible drop. Reactions are Lemar's signals; the one
✅ Samira sets herself is the capture-dedup mark on a Convo 2 message she has fully
developed, which is hers to place, not yours.

So there are exactly three destinations, chosen by the Step 1 subject test:

### WORK + CONTINUE → a plain drop in Lemar's self-DM (Convo 2)
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

### WORK + ARCHIVE → the same drop, in the same place, flagged as finished
The record is already landed (Step 2), but it still goes to Convo 2 — that's how Samira
finds out it happened. Same surface, same personal connector, same plain un-🌐 top-level
drop; only the register changes. Say plainly that it's done and just needs filing, and
give the type hint:
```
done, nothing left to do on this — just for the record:
[one line of what happened / what was decided]
[decision if it recorded a choice Lemar made, else a plain log]
Haven note: <path>
```
PART 4's quick-update route takes it from there: it finds the matter's Haven note and its
timeline channel, appends the Update, **posts the timeline entry**, and reacts ✅. That's
why this skill doesn't post one — it would be the second copy.

### FIX → a plain drop in #fixes (Convo 3)
The thread's subject is Samira herself, so it belongs on the surface whose subject is her.
Post a **plain, un-🌐 top-level message in #fixes** (`C0BV5BRNH5Z`), **via the personal
Slack connector** — as Lemar's own report of what's broken. PART 5 treats Lemar's drops in
the channel as intake and opens the fix card, with the same card mechanics as Convo 1
(`.claude/doctrine/card-format.md`).

```
[what's broken, in one line]
[what this thread found — the cause if you got that far, the files/lines involved]
[what "fixed" would look like — the observation that would prove it held]
Haven note: <path>
```

That third line matters: PART 5's Follow Up round **verifies a fix held on a later run**
before closing the card ("fixed" is an observation, not a hope), so give it something
concrete to check against. If the thread already produced the fix, say so and say whether
it's committed — the card then exists to verify, not to decide.

### Fallback — only the bot connector is reachable
If the personal connector isn't available in this session, the self-DM is out of reach
entirely (a bot cannot enter it). Post a **🌐-signed courtesy record in Convo 1**
(`D0BHPKMDNEP`) via the bot, explicitly flagged in the message as **not auto-swept** — a
🌐 bot post in Convo 1 is never card input, so it needs Lemar or a live Samira turn to
notice it. Say so plainly to Lemar; never claim it'll be picked up automatically when it
won't be.

For a FIX item specifically: #fixes is a real channel, so the bot may be able to reach it
even when the self-DM isn't. If it can, post there 🌐-signed with the same
not-auto-swept flag. If it can't (the bot isn't in the channel), fall back to Convo 1 and
tag the message 🔧 — the interim home the migration runbook already specifies
(`.claude/routines/migration-2026-09-three-convos.md`, Step 3).

## Step 4 — Tell Lemar where it landed

One or two lines, plain: the route (CONTINUE / ARCHIVE / FIX), the Haven note path, and
where it went —
- **CONTINUE** — "dropped it in your self-DM; Samira's PART 4 sweep picks it up next scan
  and opens a card in our DM."
- **ARCHIVE** — "filed in Haven and dropped it in your self-DM as a record; she'll append
  the update and post the timeline entry on her next scan."
- **FIX** — "dropped it in #fixes; PART 5 opens a fix card next scan and verifies it held
  on a later run."
- **Bot-only fallback** — "posted a courtesy record in your Samira DM — it won't be
  auto-swept, so flag it to her live if you want it acted on."

Be accurate about timing: PART 4 turns a drop into a card on her **next** scan, and PART 3
first *works* that card on the scan **after** that (the runbook's buffer rule). So "she'll
see it next scan" is honest; "she'll have done it next scan" isn't.

## What this skill does not do
It never sends outward-facing actions (email, public posts, payments) — only internal
Haven writes and internal Slack posts to Marspace. It never creates a new Slack channel.
It **never opens a card on any surface** — graduating a drop into a Convo 1 card is PART
4's job, and into a #fixes card is PART 5's; this skill only ever writes the drop those
passes read. It **never posts a timeline entry** — PART 4 writes the one for the drop it
develops, PART 7 writes the end-of-run entry for every project that moved, and a third
copy from here would just be noise on an append-only channel nobody can tidy. (Unlike
Atlas Gear 2 — this is a lighter, on-demand tool; if the same kind of thread keeps landing
in the self-DM, that's a signal for a real project timeline, which is Lemar's or Atlas's
call, not this skill's.) It never re-derives or duplicates a Haven note for the same
matter — haven-capture's own step-zero dedupe (schema §7) handles a thread that's a
continuation of an already-open matter.

## No-GitHub chat / Cowork surfaces
This version needs the GitHub connector (to write the Haven note directly, via
haven-capture) and lands the record instantly. On a surface with a Slack connector but
NO GitHub access — a plain claude.ai chat, or a Cowork session not attached to this repo
— use **`samira-work-summary-slack-only.md`** in this same folder instead: it skips the
direct Haven write and composes the Slack message so Samira's own scheduled run (which
does have GitHub access) lands the record when she processes it on her next scan. Prefer
this version whenever GitHub access is available.
