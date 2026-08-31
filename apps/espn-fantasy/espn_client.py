"""ESPN Fantasy Football v3 read-only client.

Pulls a league snapshot and normalizes it into the shape the `fantasy-gm` skill
reasons over. Read-only by design: this module has no write paths. Lineups,
waiver claims, and trades are executed by Lemar in the ESPN app, never here.

Credentials (private leagues) come from the environment, never from source:
    ESPN_LEAGUE_ID, ESPN_SEASON, ESPN_S2, ESPN_SWID
"""

from __future__ import annotations

import json
import os
from typing import Any

BASE = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons"

# ESPN lineup slot ids -> human labels.
SLOT = {
    0: "QB", 1: "TQB", 2: "RB", 3: "RB/WR", 4: "WR", 5: "WR/TE", 6: "TE",
    7: "OP", 8: "DT", 9: "DE", 10: "LB", 11: "DL", 12: "CB", 13: "S",
    14: "DB", 15: "DP", 16: "D/ST", 17: "K", 18: "P", 19: "HC",
    20: "BENCH", 21: "IR", 22: "-", 23: "FLEX", 24: "ER",
}
STARTING_SLOTS = {0, 2, 3, 4, 5, 6, 7, 16, 17, 23}

POSITION = {1: "QB", 2: "RB", 3: "WR", 4: "TE", 5: "K", 16: "D/ST"}

PRO_TEAM = {
    0: "FA", 1: "ATL", 2: "BUF", 3: "CHI", 4: "CIN", 5: "CLE", 6: "DAL",
    7: "DEN", 8: "DET", 9: "GB", 10: "TEN", 11: "IND", 12: "KC", 13: "LV",
    14: "LAR", 15: "MIA", 16: "MIN", 17: "NE", 18: "NO", 19: "NYG",
    20: "NYJ", 21: "PHI", 22: "ARI", 23: "PIT", 24: "LAC", 25: "SF",
    26: "SEA", 27: "TB", 28: "WSH", 29: "CAR", 30: "JAX", 33: "BAL", 34: "HOU",
}

# Anything not ACTIVE is worth surfacing to a human before lineups lock.
RISKY_INJURY = {"QUESTIONABLE", "DOUBTFUL", "OUT", "INJURY_RESERVE", "SUSPENSION"}


class ESPNError(RuntimeError):
    """Raised with an actionable message rather than a bare HTTP error."""


def load_credentials() -> dict[str, str]:
    """Read config from the environment. Never logs or returns cookie values."""
    league_id = os.environ.get("ESPN_LEAGUE_ID", "").strip()
    if not league_id:
        raise ESPNError(
            "ESPN_LEAGUE_ID is not set. Copy .claude/state/espn-credentials.env.example "
            "to .claude/state/espn-credentials.env, fill it in, and source it."
        )
    swid = os.environ.get("ESPN_SWID", "").strip()
    if swid and not swid.startswith("{"):
        swid = "{" + swid.strip("{}") + "}"
    return {
        "league_id": league_id,
        "season": os.environ.get("ESPN_SEASON", "2026").strip(),
        "espn_s2": os.environ.get("ESPN_S2", "").strip(),
        "swid": swid,
    }


def fetch_raw(creds: dict[str, str], views: list[str], week: int | None = None,
              extra_headers: dict[str, str] | None = None) -> dict[str, Any]:
    """GET the league endpoint with the given views. Requires network access."""
    import requests

    url = f"{BASE}/{creds['season']}/segments/0/leagues/{creds['league_id']}"
    params: list[tuple[str, str]] = [("view", v) for v in views]
    if week is not None:
        params.append(("scoringPeriodId", str(week)))

    cookies = {}
    if creds.get("espn_s2") and creds.get("swid"):
        cookies = {"espn_s2": creds["espn_s2"], "SWID": creds["swid"]}

    headers = {"User-Agent": "atlas-fantasy-gm/1.0", "Accept": "application/json"}
    headers.update(extra_headers or {})

    try:
        resp = requests.get(url, params=params, cookies=cookies,
                            headers=headers, timeout=30)
    except Exception as exc:  # network/proxy/TLS
        raise ESPNError(
            f"Could not reach ESPN ({exc.__class__.__name__}). If this is a 403 from "
            "the agent proxy, lm-api-reads.fantasy.espn.com is not on this "
            "environment's network allowlist yet."
        ) from exc

    if resp.status_code == 401:
        raise ESPNError(
            "ESPN returned 401. The espn_s2 / SWID cookies are missing or expired — "
            "pull fresh ones from a logged-in browser session."
        )
    if resp.status_code == 404:
        raise ESPNError(
            f"ESPN returned 404 for league {creds['league_id']} season "
            f"{creds['season']}. Check the league id and that the season has started."
        )
    if resp.status_code != 200:
        raise ESPNError(f"ESPN returned HTTP {resp.status_code}: {resp.text[:200]}")

    data = resp.json()
    # Some endpoints return a single-element list rather than an object.
    return data[0] if isinstance(data, list) and data else data


def _stat(player: dict, *, source: int, week: int | None) -> float | None:
    """Pull an appliedTotal. source 0 = actual, 1 = projected."""
    for row in player.get("stats") or []:
        if row.get("statSourceId") != source:
            continue
        if week is None:
            if row.get("statSplitTypeId") == 0:  # full season
                return row.get("appliedTotal")
        elif row.get("scoringPeriodId") == week and row.get("statSplitTypeId") == 1:
            return row.get("appliedTotal")
    return None


def normalize_player(entry: dict, week: int | None) -> dict[str, Any]:
    """Flatten one roster entry into the fields a start/sit call actually needs."""
    pool = entry.get("playerPoolEntry") or entry
    player = pool.get("player") or {}
    own = player.get("ownership") or {}
    status = (player.get("injuryStatus") or "ACTIVE").upper()
    return {
        "player_id": player.get("id"),
        "name": player.get("fullName") or "UNKNOWN",
        "position": POSITION.get(player.get("defaultPositionId"), "?"),
        "pro_team": PRO_TEAM.get(player.get("proTeamId"), "?"),
        "slot": SLOT.get(entry.get("lineupSlotId"), "?"),
        "starting": entry.get("lineupSlotId") in STARTING_SLOTS,
        "injury_status": status,
        "injury_flag": status in RISKY_INJURY,
        "projected": _stat(player, source=1, week=week),
        "actual": _stat(player, source=0, week=week),
        "season_total": _stat(player, source=0, week=None),
        "percent_owned": round(own.get("percentOwned") or 0.0, 1),
        "percent_started": round(own.get("percentStarted") or 0.0, 1),
        "percent_change": round(own.get("percentChange") or 0.0, 2),
    }


def normalize(raw: dict[str, Any], week: int | None = None) -> dict[str, Any]:
    """Turn a raw league payload into the snapshot the skill reads."""
    settings = raw.get("settings") or {}
    status = raw.get("status") or {}
    current_week = week or status.get("currentMatchupPeriod") or raw.get("scoringPeriodId")

    scoring = settings.get("scoringSettings") or {}
    ppr = 0.0
    for item in scoring.get("scoringItems") or []:
        if item.get("statId") == 53:  # receptions
            ppr = item.get("points", 0.0) or 0.0
            break
    scoring_label = {0.0: "standard", 0.5: "half-PPR", 1.0: "full PPR"}.get(ppr, f"{ppr}/rec")

    roster_cfg = (settings.get("rosterSettings") or {}).get("lineupSlotCounts") or {}
    lineup = {SLOT.get(int(k), k): v for k, v in roster_cfg.items() if v}

    teams = []
    for team in raw.get("teams") or []:
        record = ((team.get("record") or {}).get("overall") or {})
        entries = ((team.get("roster") or {}).get("entries")) or []
        teams.append({
            "team_id": team.get("id"),
            "name": (team.get("name")
                     or f"{team.get('location','')} {team.get('nickname','')}".strip()
                     or f"Team {team.get('id')}"),
            "abbrev": team.get("abbrev"),
            "wins": record.get("wins", 0),
            "losses": record.get("losses", 0),
            "ties": record.get("ties", 0),
            "points_for": round(record.get("pointsFor") or 0.0, 1),
            "points_against": round(record.get("pointsAgainst") or 0.0, 1),
            "roster": [normalize_player(e, current_week) for e in entries],
        })

    matchups = []
    for game in raw.get("schedule") or []:
        if game.get("matchupPeriodId") != current_week:
            continue
        matchups.append({
            "home_team_id": (game.get("home") or {}).get("teamId"),
            "away_team_id": (game.get("away") or {}).get("teamId"),
            "home_score": (game.get("home") or {}).get("totalPoints"),
            "away_score": (game.get("away") or {}).get("totalPoints"),
        })

    return {
        "league_id": raw.get("id"),
        "league_name": settings.get("name"),
        "season": raw.get("seasonId"),
        "current_week": current_week,
        "team_count": settings.get("size") or len(teams),
        "scoring": scoring_label,
        "ppr_value": ppr,
        "lineup_slots": lineup,
        "teams": teams,
        "matchups": matchups,
    }


FA_FILTER = {
    "players": {
        "filterStatus": {"value": ["FREEAGENT", "WAIVERS"]},
        "limit": 150,
        "sortPercOwned": {"sortAsc": False, "sortPriority": 1},
    }
}


def fetch_free_agents(creds: dict[str, str], week: int) -> list[dict[str, Any]]:
    """Top available players by roster percentage — the waiver-wire candidate pool."""
    raw = fetch_raw(
        creds, ["kona_player_info"], week=week,
        extra_headers={"x-fantasy-filter": json.dumps(FA_FILTER)},
    )
    out = []
    for entry in raw.get("players") or []:
        out.append(normalize_player(entry, week))
    return out
