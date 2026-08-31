#!/usr/bin/env python3
"""Pull an ESPN fantasy league snapshot for the fantasy-gm skill.

    python3 fetch_league.py                     # current week, live
    python3 fetch_league.py --week 4            # a specific week
    python3 fetch_league.py --free-agents       # include the waiver pool
    python3 fetch_league.py --offline raw.json  # normalize a saved payload

Read-only. Writes JSON to stdout (or --out). Never sets a lineup or a claim.
"""

from __future__ import annotations

import argparse
import json
import sys

import espn_client as espn

VIEWS = ["mTeam", "mRoster", "mSettings", "mMatchupScore", "mNav"]


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch an ESPN fantasy league snapshot.")
    ap.add_argument("--week", type=int, help="Scoring period. Defaults to the current week.")
    ap.add_argument("--free-agents", action="store_true",
                    help="Also pull the top available players (waiver pool).")
    ap.add_argument("--offline", metavar="FILE",
                    help="Normalize a saved raw payload instead of calling ESPN.")
    ap.add_argument("--out", metavar="FILE", help="Write to FILE instead of stdout.")
    args = ap.parse_args()

    try:
        if args.offline:
            with open(args.offline) as fh:
                raw = json.load(fh)
            if isinstance(raw, list) and raw:
                raw = raw[0]
            snapshot = espn.normalize(raw, args.week)
            snapshot["source"] = f"offline:{args.offline}"
        else:
            creds = espn.load_credentials()
            raw = espn.fetch_raw(creds, VIEWS, args.week)
            snapshot = espn.normalize(raw, args.week)
            snapshot["source"] = "espn-live"
            if args.free_agents:
                snapshot["free_agents"] = espn.fetch_free_agents(
                    creds, snapshot["current_week"]
                )
    except espn.ESPNError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    text = json.dumps(snapshot, indent=2)
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(text)
        print(f"wrote {args.out} "
              f"(week {snapshot['current_week']}, {len(snapshot['teams'])} teams)",
              file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
