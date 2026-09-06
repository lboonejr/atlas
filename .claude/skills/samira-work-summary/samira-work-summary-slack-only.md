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
surface won't have wired up anyway). That identity is exactly what the primary route
needs: only Lemar's own account can post into his self-DM. No GitHub, no other
connector required.

## Known hardcoded values (duplicated here on purpose — see "On drift" below)
- **Convo 2 — Lemar's SELF-DM**: `D0BBVV54L5R` (the intake notepad since 2026-09-06;
  it replaced the bot DM as the capture inbox). The primary target — never invent a
  different one. Reachable only from Lemar's own account (a bot cannot enter a
  self-DM), which is the identity this surface already uses.
- **Convo 3 — #fixes**: `C0BV5BRNH5Z` (private; where anything wrong with Samira herself
  gets worked, since 2026-09-06). The target when the thread's subject IS her.
- **Convo 1 — the Samira bot DM**: `D0BHPKMDNEP` (the card surface). Used here ONLY as
  the courtesy fallback if, unusually, this session posts through a bot identity
  instead of Lemar's own account.

## Step 1 — Summarize the thread
Same as the full skill: what this thread is, state (done / in progress / blocked),
decisions Lemar actually made, open questions, and — if the work isn't finished — one
concrete recommended next step.

Then the same two calls, in the same order. **First the SUBJECT** — whose problem is this?
- **FIX** — the subject is *Samira herself*: a routine that misfired, a stale or
  self-contradicting skill, a connector/access gap, a wrong or duplicated output she
  produced. → #fixes, and the mode below doesn't apply.
- **WORK** — everything else, i.e. Lemar's own projects and tasks. → the self-DM, and the
  mode decides how the drop reads.

**Then, for WORK threads, the MODE:**
- **CONTINUE** — unfinished, with a concrete next step Samira could execute.
- **ARCHIVE** — finished, or nothing actionable left; this is purely a record.

Never split one thread across two surfaces — route on what the handoff is actually asking
for: if what still needs doing is hers, it's FIX; if it's the project's, it's WORK.

## Step 2 — Drop it where it gets swept (this IS the whole delivery mechanism)

Since the 2026-09-06 restructure there is no channel-staging branch: project channels
are append-only timelines nobody sweeps, so a fenced prompt or a "Samira, do X"
instruction posted to one would sit forever unread. **Never post to a project channel** —
not even as a record. Everything goes through a surface Samira actually sweeps: **Lemar's
self-DM** (`D0BBVV54L5R`) for WORK, **#fixes** (`C0BV5BRNH5Z`) for FIX.

### FIX → a plain drop in #fixes
Post the summary top-level in #fixes, un-reacted, no globe emoji, in the same plain
first-person register as below — Lemar's own report of what's broken. PART 5 treats his
drops there as intake and opens the fix card. Include what's broken in one line, what this
thread found (cause, files involved), and **what "fixed" would look like** — PART 5's
follow-up round verifies the fix held on a later run, so give it something concrete to
check. If the thread already produced the fix, say so and say whether it's committed.

### WORK → a plain drop in the self-DM

Post the Step 1 summary there, top-level, un-reacted, written **exactly as Lemar would
type a raw brain-dump**: no globe emoji (a 🌐 prefix marks a message as Samira's own
and excludes it from the sweep), not addressed to Samira by name, plain first-person
register. Posted from Lemar's own Slack account with no reaction, that's
indistinguishable from a real capture, so Samira's PART 4 sweep ("a top-level message
without a 🌐 prefix, with no status reaction") develops it — probe, land the Haven
note, graduate real work into a Convo 1 card — on her own next scan.

- **CONTINUE mode** — include the concrete next step plainly ("next step: …"), written
  self-contained: the skill/tool to use, the IDs/links needed, the one concrete
  outcome. PART 4 is capture-first, so the Haven record lands as part of developing
  it — no need to spell that out. If the next step genuinely needs Lemar's own hands,
  say so in the drop ("this one's on me: …") so the card carries it as his open item.
- **ARCHIVE mode** — say plainly that it's finished and just needs filing ("done,
  nothing left to do — just for the record: …", with a type hint: decision if it
  recorded a choice Lemar made, else a plain log). PART 4's routing files it and
  posts the project channel's timeline entry — which is exactly why you don't.

### Fallback — only a bot identity is reachable
If this session can't post as Lemar's own account (so the self-DM is unreachable),
post a 🌐-signed courtesy record to **Convo 1** (`D0BHPKMDNEP`) via the bot instead,
explicitly flagged in the message as not auto-swept — a 🌐 bot post in Convo 1 is
never card input — and tell Lemar it needs him or a live Samira turn to be noticed.

For a FIX item, try #fixes first — it's a real channel, so a bot may reach it even when
the self-DM is out of reach; post there 🌐-signed with the same not-auto-swept flag. If
the bot isn't in the channel either, fall back to Convo 1 and tag the message 🔧.

## Step 3 — Tell Lemar where it went
One or two lines: the route, and where it went — "dropped it in your self-DM, Samira will
develop it and land the Haven record on her next hourly pass", or "dropped it in #fixes,
she'll open a fix card next scan" (or, in the fallback case, "posted a courtesy record in
your Samira DM — flag it to her live if you want it acted on"). **Never say it's "saved to
Haven" or "filed"** — this version can't confirm that write happened, only that it handed
Samira the material to do it. Samira's cadence is hourly, roughly 8am–6pm ET — so say
"next scan," not "now."

## Hard floor
Never send email or any outward-facing action, never pay or transfer anything, never
post outside the self-DM, #fixes, or the Convo 1 courtesy fallback, never post a project
channel's timeline entry (PART 4 and PART 7 own those), never create a new Slack
channel, never claim a Haven write happened that this surface didn't (and can't)
perform itself.

## On drift
This file hardcodes the self-DM, #fixes, and Convo 1 ids because it has no repo access to
read `.claude/anchors.md` live. If any of them (or the workspace) ever changes, this file
goes stale until someone updates it by hand — unlike the main skill, which always reads
anchors.md fresh. (It already went stale once: until 2026-09-06 it pointed at the bot
DM `D0BHPKMDNEP` as the capture inbox and staged fenced prompts to project channels.)
Prefer the main skill whenever GitHub access is available; treat this file as the
fallback for when it genuinely isn't.
