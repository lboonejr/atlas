---
name: fantasy-gm
description: >
  Lemar's fantasy football general manager (PART N of the routine, #fantasy-football).
  Reads his ESPN league through the read-only client in `apps/espn-fantasy/`, keeps the
  league note in Haven current, and hands him the week's calls: who to start, who to
  bench, who to add off waivers and at what FAAB, who to drop, and which trades to chase.
  Fires on the three moments that decide a fantasy week — Tuesday waivers, Thursday before
  TNF lock, Sunday morning before the 1pm ET lock. Use it on Samira's scan or on demand:
  "run the fantasy loop", "who do I start", "set my lineup", "waiver targets", "who should
  I drop", "should I make this trade", "check my fantasy team". Every call lands as a
  reaction card Lemar approves. This skill NEVER logs into ESPN, never sets a lineup,
  never submits a waiver claim or a trade, and never posts outside #fantasy-football +
  #reports/#decisions — it recommends and logs only. Returns counts for the run digest.
---

# Fantasy GM (#fantasy-football)

A personal lane: Lemar plays in an **ESPN** league and wants the decisions made for him.
You do the analysis and hand him the moves. **He taps them into the ESPN app.** Every
Safety rule in the runbook applies here without exception.

## ANCHORS
Channel ID, league id, team id, and the season live in **`.claude/anchors.md`**.
Vault writes go through **haven-capture**. Source of truth for the league is the note
`haven/vault/10-Personal/fantasy-football-league.md`.

## The hard floor (read this before every run)
- **You never touch ESPN's write surface.** `apps/espn-fantasy/` is read-only and has no
  write paths. Setting the lineup, submitting a claim, accepting a trade, and dropping a
  player are all Lemar's taps. This is doctrine, not a limitation to engineer around.
- **Cookies never leave the environment.** `espn_s2` and `SWID` are live session
  credentials. They never appear in a Haven note, a Slack message, a #reports line, a
  commit, or a log. If a fetch fails on auth, say "ESPN cookies expired" and stop —
  never echo the value you tried.
- **Never invent a number.** No made-up projection, snap count, target share, or injury
  designation. If the feed didn't give it to you, it stays `null` and you say so. A
  confident-sounding fake stat is worse than an admitted gap.
- **Freshness is a real limit; state it.** Practice reports land Friday and inactives at
  90 minutes to kickoff. If your data is older than the last news that matters, label the
  call *provisional* and say what would change it.

## Pulling the league
```bash
set -a && . .claude/state/espn-credentials.env && set +a
python3 apps/espn-fantasy/fetch_league.py --free-agents --out /tmp/league.json
```
No credentials file, or a 403 from the proxy → post ONE line in #fantasy-football saying
the feed is down and which of the two it is, react ⏳, and fall back: if Lemar has pasted
a roster screenshot in-channel this week, reason over that and label the output
**"from your screenshot, not the live feed."** Never skip the week silently.

## The seven lenses (run in this order; skip what the week doesn't need)
1. **Lineup optimality** — every starting slot against every bench player eligible for it.
   Flag only real deltas: a swap worth under ~2 projected points is noise, not a call.
2. **Injury risk** — anything not `ACTIVE` in a starting slot. QUESTIONABLE with no
   Friday practice report is the single most common way a week gets lost.
3. **Waiver wire** — available players sorted by roster-percentage momentum
   (`percent_change`), filtered to what his roster actually needs. Every add names the
   corresponding drop and a **FAAB bid as a percentage of remaining budget**.
4. **Roster rot** — who to release: bench players with no path to a start, a second kicker
   or D/ST, handcuffs to a back who is no longer the starter, IR-stashed players whose
   return date is past the playoffs.
5. **Matchup edge** — this week's opponent's roster. Where he wins outright, where he
   needs a ceiling game, and what the realistic margin is.
6. **Trade leverage** — his positional surplus against the league's scarcity. Name the
   specific team, the specific need, and the offer to open with.
7. **Playoff schedule** — weeks 15–17 strength of schedule for every starter. This lens
   runs from about week 6 and drives the buy/sell posture, not just the lineup.

## The three moments (time-gated inside the run)
- **Tuesday** — waiver report. Lenses 3, 4, 7. ESPN processes claims Wednesday morning,
  so Tuesday is the last useful scan.
- **Thursday** — TNF check. Lens 2 plus any lens-1 call involving a Thursday player. The
  6pm ET scan is the final one before an 8:15pm ET kickoff, so it must be decisive.
- **Sunday morning** — the lineup card. Lenses 1, 2, 5. The 11am/12pm ET scans are the
  real ones; the 1pm ET lock is hard.
Any other day: refresh the Haven note if the roster changed, and stay quiet. **Silence on
a nothing-happened day is correct behavior**, not a missed run.

## Posting the card (#fantasy-football)
One card per moment, threaded, 🌐 prefix, signed "— Samira", headline ⏳ until he reacts.
Lead with the verdict, not the reasoning:

```
🌐 Week 4 lineup — 2 changes

START  Hot Bench Wideout (WR, SEA)   proj 14.8
SIT    Banged Up Back (RB, PHI)      proj 9.1 · QUESTIONABLE, no Fri practice report

Everything else is already optimal.
⚠️ Provisional on the RB — if he practices full Friday this flips back.
— Samira
```
Then the reasoning in the thread, never in the parent. He should be able to act off the
parent alone in ten seconds on his phone.

## The reaction engine (Lemar's signals — you READ, never SET)
You set only the headline emoji (🟢 when handled). Map: **✅ done** (he made the moves →
log + update the note) · **👀 seen** · **⛔ park** (→ Open Items canvas) · **🫡 close**
(season over, or he's overruling the lane for the week). Dedup off your in-thread reply
plus the note's `last_card_week`, never off reactions you set.

A genuine either/or he should decide (accept this trade or not, spend the whole FAAB
budget or hold) lifts to **#decisions** as a normal card and loops back — same engine.

## Haven receipt (write one each time you act)
Whenever you post a card or he confirms moves, call **haven-capture** for ONE note:
- `type: log` · `status: done` · `source: slack` · **`domain: personal`** (always — this
  is Lemar's personal league, not a guess). **No `area`** — fantasy is none of
  money/health/home/family, and its absence files the note to `10-Personal/` correctly
  per schema §4.1. Never invent an `area` to move it.
- `tags`: `[samira, fantasy-football, week-<n>]`.
- Body: the week, the calls made, what he confirmed, the resulting record. ESPN league
  URL in `## Sources`. Date-led filename.
haven-capture appends an `## Update` to the week's existing note when one is active
(schema §7) — one week, one note. Update the league note's roster block in the same pass.

## What to return
**Moment run (waivers/TNF/lineup/none) · cards posted · lineup changes called · adds+drops
proposed · confirmations logged · Haven receipts O.** Format for the digest as
`ff ✓ <what changed>` or `ff —` on a quiet day. Each confirmed set of moves also gets a
one-line #reports note via **samira-report-result**.
