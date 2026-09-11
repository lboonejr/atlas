---
created: 2026-09-10T14:10:00-04:00
updated: 2026-09-11T17:07:00-04:00
domain: cuzzies
type: task
status: active
tags: [cuzzies, renewal, crc, entity-cleanup, taxes]
source: slack
---

# Cuzzie's — CRC renewal game plan

Lemar drop, Convo 2 self-DM (thread ts `1789061736.927349`, reply `1789062261.411799`),
2026-09-10: set a game plan for Cuzzie's CRC license renewal. Steps as he framed them:

1. Tidy up the entity.
2. Confirm good standing with the municipality and the state, including taxes.
3. Once 1–2 are clean, start gathering the documents needed for a renewal application,
   modeled on the process already run for The Station's renewal.

Possibly connected to [[2026-09-10-station-tax-problem-investigation]] (The Station's
tax problem) — different entity, but worth checking whether they share a root cause.
Nothing on the entity/standing/tax side has been checked yet; this note tracks the plan
as it's built, not a completed audit.

## Update 2026-09-11T12:00:00-04:00 — filing still open, new target Tue 9/15; moving to municipal standing
Lemar confirmed the 9/7 annual-report filing target passed without being filed, and
set a new target: "complete all the filings this Tuesday, 9/15" (moved the `due` on
[[2026-08-17-nj-annual-report-revocation-notice]] to match). He also said to move on
to the municipal-standing step in parallel rather than wait on the filing.

Checked what's available on the municipal/state-standing question: NJ's public
Business Name/Entity Search (DORES, njportal.com/dor/businessnamesearch) is an
interactive portal search, not something fetchable without a session — no free API
or scrapable result for entity `#152-009080`'s current status. Same for Camden's
municipal tax/license standing — not a source Samira can reach without either
(a) Lemar/Samira checking the njportal.com search directly, or (b) Lemar reporting
what he sees. Not guessing a status either way. Genuinely open:
- Cuzzie's current standing on njportal.com's Business Name Search (would also show
  whether the revocation notice is still just "pending" or has moved to actually
  revoked).
- Camden municipal tax/license account status — no public lookup identified.

## Update 2026-09-11T17:07:00-04:00 — filing target confirmed Tue 9/15; Chrome prompt drafted for njportal.com lookup
Lemar confirmed on the Convo 1 card he hasn't filed the annual report yet, wants all
filings done Tuesday 9/15, and to proceed with the municipal-standing step in
parallel. He asked for a Claude in Chrome prompt to run the njportal.com DORES
Business Name/Entity Search for entity #152-009080 himself (read-only lookup for
current status + whether the annual-report delinquency still shows) — drafted and
posted on the card. Camden municipal tax/license standing still has no known public
lookup; asked Lemar for the right portal URL if he knows one, otherwise this likely
needs a direct call to Camden's tax collector/clerk's office.

## Sources
- slack: Convo 2 `D0BBVV54L5R` thread `1789061736.927349`, reply `1789062261.411799`
- slack: Convo 1 `D0BHPKMDNEP` thread `1789063832.775699`, replies `1789136831.358239`
  / `1789136845.522919` / `1789146437.777129`