# ESPN Fantasy — read-only league client

Feeds the **fantasy-gm** skill (`.claude/skills/fantasy-gm/`, PART N of Samira's runbook).

## Read-only by design

There are **no write paths in this package** and none should be added. Setting a lineup,
submitting a waiver claim, dropping a player, and accepting a trade are Lemar's taps in
the ESPN app. The skill hands him the moves; he makes them. Same posture as the money
hub, which computes the number but never moves the money.

## Setup

1. **League id** — from your league URL: `fantasy.espn.com/football/league?leagueId=XXXXXXX`

2. **Cookies** (private leagues only). In Chrome, logged in to `fantasy.espn.com`:
   DevTools → Application → Storage → Cookies → `https://fantasy.espn.com`, copy
   `espn_s2` and `SWID`.

   ```bash
   cp .claude/state/espn-credentials.env.example .claude/state/espn-credentials.env
   # fill it in, then:
   set -a && . .claude/state/espn-credentials.env && set +a
   ```

   That file is gitignored. These are **live session cookies** — anyone holding them can
   act as you on ESPN. They never belong in a Slack message, a Haven note, or a commit.
   They also expire; a `401` means re-pull them.

3. **Network allowlist.** `lm-api-reads.fantasy.espn.com` must be reachable. As of
   2026-08-30 the cloud environment's policy returns **403 (policy denial)** for it —
   add it to the environment's allowlist, or run the fetch somewhere with open egress
   and hand the JSON over via `--offline`.

## Usage

```bash
python3 apps/espn-fantasy/fetch_league.py                      # current week
python3 apps/espn-fantasy/fetch_league.py --week 4             # a specific week
python3 apps/espn-fantasy/fetch_league.py --free-agents        # + the waiver pool
python3 apps/espn-fantasy/fetch_league.py --offline raw.json   # from a saved payload
python3 apps/espn-fantasy/fetch_league.py --out /tmp/league.json
```

Output is one normalized snapshot: league settings (size, scoring, lineup slots), every
team with record and full roster, this week's matchups, and optionally the top available
players. Each player carries slot, position, pro team, injury status, weekly projection,
weekly actual, season total, and roster-percentage momentum — the fields a start/sit or
waiver call actually turns on.

## Verification status

Normalization is tested against `tests/fixture_league.json`, a payload shaped like ESPN's
v3 response (half-PPR scoring detection, lineup-slot mapping, pro-team mapping, starter
vs. bench vs. IR, the projected/actual/season stat split, week-filtered matchups, and
players with empty stat arrays). Error paths are covered too: missing league id, missing
offline file, and SWID brace normalization.

**The live ESPN call is unverified** — the network policy blocked it from the environment
this was built in, so the request shape, view names, and auth flow are written to the
documented v3 API but have not been exercised against a real league. Expect to shake out
one or two field-shape details on the first real fetch.

## Files

| file | what it is |
|---|---|
| `espn_client.py` | API client, id→label maps, snapshot normalization |
| `fetch_league.py` | CLI entrypoint |
| `tests/fixture_league.json` | Synthetic payload for offline verification |
