---
created: 2026-08-19T21:34:48-04:00
updated: 2026-08-19T21:34:48-04:00
domain: automation
type: task
status: awaiting-decision
tags: [samira, vault-integrity, part-v, camden-launch]
source: claude
---

# Integrity defect: ops-admin-lane-and-ariana.md filed without `created`/`updated`

PART V flagged this on the 2026-08-19 14:22 ET scan and correctly did not repair it.
The flag lived only in the `_daily/2026-08-19.md` run journal, which scrolls out of
reach — this note gives it a durable home so it stops being rediscovered every sweep.

## The defect

`haven/vault/40-Projects/camden-dispensary-launch/ops-admin-lane-and-ariana.md` is
filed with a valid container (opener on line 1, well-formed block, LF endings) but two
of the six required fields absent entirely:

```yaml
domain: project        # present
type: decision         # present
status: awaiting-decision
source: claude
tags: [samira-loop, camden-launch, phase-00]
# created:  MISSING
# updated:  MISSING
```

## Why it was not repaired

Schema §4.5 and the vault-keeper ANCHORS both put this outside the repairable set:

- Repairable defects are **containers** (stray lines above the opener, missing opener,
  lossless base64, CRLF). This container is fine — the gap is in the **values**.
- "A **required field absent entirely** on a filed note" is listed explicitly under
  *Do NOT repair — flag and leave*.
- "**Never invent a missing `created`**" is stated as law in the same section.

Repairing a container is never licence to fill in a value. Leaving it flagged is the
enforcement mechanism working, not a backlog item.

## What the correct value would be, if Lemar authorizes it

Not a guess — both fields are recoverable from record:

| field | value | source |
|-------|-------|--------|
| `created` | `2026-08-19T12:00:40-04:00` | commit `e351156` — "Add Haven note: Ops ADMIN lane and Ariana (Camden launch, phase 00)", the only commit ever to touch the file |
| `updated` | `2026-08-19T12:00:40-04:00` | same commit; the file has not been edited since |

The note's own body corroborates the date ("Round 1 run 2026-08-19", "Drafted and
placed", both Drive docs stamped `_20260819`).

## Likely root cause

The note records that the GitHub connector returned 403 on writes during a Cowork
session on 2026-08-19, so it had to reach the vault through GitHub's web upload rather
than through `haven-capture`. That path bypasses the skill that stamps `created` and
`updated`, which is consistent with those two fields — and only those two — being
absent while the four hand-authored controlled fields survived. Worth watching: any
future note that takes the web-upload path will land with the same gap.

## Decision needed from Lemar

1. Authorize the backfill with the git-derived timestamps above (one edit, disclosed
   in the note), **or**
2. Leave it flagged, matching the standing decision on `_daily/2026-08-01.md`.

## Sources
- vault: `haven/vault/40-Projects/camden-dispensary-launch/ops-admin-lane-and-ariana.md` (untouched)
- vault: `haven/vault/_daily/2026-08-19.md` line 31 — the original PART V flag
- git: commit `e351156`, 2026-08-19 12:00:40 -0400
- schema: `_system/schema.md` §4.5, "Do NOT repair" list
- precedent: `70-Automation/samira/2026-08-09-corrupted-daily-log-2026-08-01-decision.md`
