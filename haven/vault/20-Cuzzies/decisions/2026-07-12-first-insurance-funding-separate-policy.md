---
created: 2026-07-12T15:07-04:00
updated: 2026-07-12T15:07-04:00
domain: cuzzies
type: decision
status: done
tags: [on-button, insurance, first-insurance-funding, epli, reopen-plan]
source: slack
---

# Decision: First Insurance Funding notice (loan #106241219) is a separate policy, not a duplicate of epli-reinstate

Samira flagged an ambiguity 2026-07-12 (#decisions parent, ts `1783876542.732339`): a
`Notices.pdf` dropped in #on-button 7/9 showed loan #106241219 (past due $3,040.95 +
current installment $1,658.81 = $4,699.76 total, insurance cancelled) that did not match
the loan number already tracked on the `epli-reinstate` line (#105889646, $4,051.12,
decided 7/6 to let lapse).

**Lemar picked Option B** (reacted on the parent): this is a **separate insurance line**
financed through the same lender (First Insurance Funding), not a later statement on the
same EPLI policy.

## What changed
- `haven/vault/40-Projects/on-button-reopen/index.md`: item `first-insurance-funding-notice`
  status moved `tbd-confirm` → `past-due`; label dropped "UNCONFIRMED"; now included in the
  Tier 3 snapshot total (was $12,382, now **$17,081.76**).
- `on-button-reopen.html` (repo root) and the pinned canvas `F0BEN1167GB` regenerated to
  match.
- Nothing paid or contacted — tracking only.

## Sources
- slack: #decisions `C0BBXA96FFV` ts `1783876542.732339` (the ask + Lemar's Option B reaction)
- slack: #on-button `C0BEQUW5NPP`, drop `F0BG52EUSKD` (Notices.pdf, 7/9)
- vault: [[2026-07-10-cuzzies-reopening-plan]] (on-button-reopen index)
