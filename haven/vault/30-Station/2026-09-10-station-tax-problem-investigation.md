---
created: 2026-09-10T14:10:00-04:00
updated: 2026-09-11T10:45:00-04:00
domain: station
type: task
status: active
tags: [station, tax, weekend-visit]
source: slack
---

# The Station — dig into what the tax problem might be

Lemar drop, Convo 2 self-DM (thread ts `1789061736.927349`, reply `1789062366.201209`),
2026-09-10: "Try to dig into what the station's tax problem might be." No detail yet on
what the problem is, which tax (municipal, state, entity-level), or how it surfaced —
that is exactly what needs investigating while he's on-site this weekend.

Possibly connected to the CRC renewal game plan for Cuzzie's
([[2026-09-10-cuzzies-crc-renewal-game-plan]]), which separately calls out getting
"good with the municipality and the state as far as the taxes and our standing" — that
note is about Cuzzie's, this one is The Station, but the two may turn out to share a
root cause. Nothing investigated yet.

## Update 2026-09-11T10:45-04:00 — likely identified: this IS the UEZ blocker

Convo 1 card (thread ts `1789063831.351469`), Lemar's reply: when The Station tried to
sign up for UEZ certification, the NJ portal stopped them and said they need to
"handle things with NJ's Division of Taxation first." That's very likely the answer to
this note's open question — the "tax problem" and the UEZ application's blocker
([[2026-09-06-station-uez-certification-application]]) may be the same underlying
issue, not two separate ones.

Public NJ process (confirmed via web search, not yet verified against Station's actual
account): UEZ business certification requires a **Division of Taxation Tax Clearance
Certificate** — the business must be current on all required state tax filings, with
no outstanding discrepancies, before certification proceeds. If The Station has an
unfiled return, a balance due, or a registration gap with the Division of Taxation,
that would explain both the portal block and the vague "tax problem" flag in one shot.
Division of Taxation's UEZ clearance contact: `UEZTaxClearances@treas.nj.gov`.

**Not yet confirmed against Station's actual account** — this is the general public
process, not a lookup of Station's specific standing. What would confirm it: logging
into NJ's Premier Business Services / Division of Taxation account for The Station and
checking for an open clearance issue. That login is the same PBS credential blocker
already tracked on the UEZ note (waiting on Markony). A ready-to-run Claude-in-Chrome
prompt for this check was drafted on the Convo 1 card — Lemar to run it himself with
his own logged-in session.

## Sources
- slack: Convo 2 `D0BBVV54L5R` thread `1789061736.927349`, reply `1789062366.201209` ·
  Convo 1 card ts `1789063831.351469`
- web: NJ Division of Taxation — Urban Enterprise Zone overview
  (nj.gov/treasury/taxation/businesses/salestax/uez-over.shtml) · Clearance/License
  Verification (nj.gov/treasury/taxation/organization/cea-clearance.shtml)
