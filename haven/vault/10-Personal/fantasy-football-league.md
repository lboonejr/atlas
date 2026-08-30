---
created: 2026-08-30T11:31-04:00
updated: 2026-08-30T11:31-04:00
domain: personal
type: reference
status: active
tags: [fantasy-football, espn, samira, fantasy-gm]
source: manual
---

# Fantasy Football — ESPN League

Source of truth for the **fantasy-gm** skill (PART N). The ESPN app is where moves get
made; this note is where the league's state and every decision are recorded. Samira reads
this note, refreshes it from the read-only feed in `apps/espn-fantasy/`, and never writes
to ESPN.

## League config

| field | value |
|---|---|
| Platform | ESPN |
| League ID | **UNRESOLVED** — from the league URL `?leagueId=XXXXXXX` |
| Season | 2026 |
| Lemar's team ID | **UNRESOLVED** — resolved on the first successful fetch |
| Team name | **UNRESOLVED** |
| League size | **UNRESOLVED** — read from `settings.size` |
| Scoring | **UNRESOLVED** — standard / half-PPR / full PPR, read from the feed |
| Roster slots | **UNRESOLVED** — read from `rosterSettings.lineupSlotCounts` |
| Waiver type | **UNRESOLVED** — FAAB budget or rolling priority |
| Keeper / dynasty | **UNRESOLVED** |

Everything above except League ID is **self-resolving**: the first successful
`fetch_league.py` run reads it straight out of `mSettings` and fills this table in.
Only the league id has to come from Lemar. Per schema doctrine these stay UNRESOLVED
rather than guessed.

## Credentials

Not here, and never here. `espn_s2` and `SWID` live only in
`.claude/state/espn-credentials.env`, which is gitignored. See
`.claude/state/espn-credentials.env.example`.

## Season log

_One entry per decided week: the calls made, what Lemar confirmed, the result._

| week | calls | confirmed | result |
|---|---|---|---|
| — | season not started | — | — |

## Standing preferences

_Fill these in as they come up — they shape every call the skill makes._

- **Risk posture:** UNRESOLVED (chase ceiling vs. protect floor)
- **FAAB aggression:** UNRESOLVED
- **Untouchables:** UNRESOLVED (players not to trade regardless of value)
- **League context:** UNRESOLVED (money league? friends? rivalries worth playing to?)

## Sources
- ESPN league: UNRESOLVED (paste the league URL here)
- Skill: `.claude/skills/fantasy-gm/SKILL.md`
- Client: `apps/espn-fantasy/`
