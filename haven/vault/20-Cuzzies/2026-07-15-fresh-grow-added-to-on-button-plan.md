---
created: 2026-07-15T11:07-04:00
updated: 2026-07-15T16:00-04:00
domain: cuzzies
type: log
status: done
tags: [samira, on-button, fresh-grow, reopen-plan]
source: claude
---

# Fresh Grow added to the on-button reopening plan

Ran the **on-button-plan** skill (direct request from Lemar) to add [[fresh-grow]]
(freshcannabis.co, contact Kathy@freshcannabis.co) as a new Tier 2 cannabis-vendor
arrears line in the reopening plan.

Result:
- `haven/vault/40-Projects/on-button-reopen/index.md` — new item `fresh-grow`,
  `amount: null` (TBD). No invoice or statement email exists for them, only recurring
  wholesale menu emails — matches the pattern of the other TBD cannabis-vendor lines
  (Curaleaf, Glass Meadows, Chew & Chill, Dime Industries, Hamilton Farms, Ganja Manja,
  Lovegrow, Niche LLC).
- `on-button-reopen.html` regenerated — Fresh Grow added to the `repay.vendors` list.
- Slack canvas `F0BEN1167GB` refreshed — row added to the Cannabis Vendor Repayments
  table, TBD count 8 → 9, 2026-07-15 update section appended.
- Committed straight to `main` (commit `8b36da2`), per the repo's git-write policy.
- Nothing paid or contacted — tracking only.

Context: earlier the same day, Samira saved an unsent Gmail draft reply to
Kathy@freshcannabis.co letting her know Cuzzie's is temporarily closed, that reopening
is the priority, and that the balance hasn't been forgotten — see
[[2026-07-15-fresh-grow-closure-balance-draft]].

## Sources
- claude: direct chat request, 2026-07-15
- slack: canvas `F0BEN1167GB`
