---
created: 2026-09-04T23:07-04:00
updated: 2026-09-04T23:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run log, 2026-09-04

Mode: **LIVE** (`DRY_RUN = false`)
Account: `lemar@cuzziesnj.com`

## PART A — vendor menus archived: 2

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1a0681795804ea43 | TerrAscend Menu - 50% OFF Edibles, Up to 40% OFF Flower + Shatter & Chocolate Restock - 9-3-26 | ndesiderio@terrascend.com | 2026-09-03 |
| 1a067bb7bd54d49e | Goodies Menu: Quality meets Affordability | Austin@niche.apextrading.com | 2026-09-03 |

Both qualified on domain-on-seed-list (terrascend.com, apextrading.com subdomain) AND
subject menu-signal AND an itemized menu (attachment / in-body Shop Now product links).
Both were labeled `Vendor Menus` (`Label_7063567382570959882`) and removed from Inbox —
nothing trashed, fully recoverable in All Mail under the label.

Other vendor-domain inbox hits reviewed and skipped as not genuine menus (precision over
recall): 5 "Account On Hold" / "Friendly Reminder – Outstanding Balance" collections
notices from awholdings.com; 4 Verano AR-statement thread messages; a TerrAscend OOO
notice; a QCC/qccnj.com onboarding-docs thread (also carries genuine filing labels
`Action Needed` + `Finance Bills`); and one Verano "End of Summer Savings!" promo with an
order link but no itemized menu content — weakly a menu, left alone per the skip rule.

## PART B — trash sweep: 0 trashed, 0 candidates

Searched `older_than:1y (category:promotions OR category:social OR category:forums)` —
zero threads. Cross-checked each category individually
(`category:promotions older_than:1y`, `category:social older_than:1y`,
`category:forums older_than:1y`) and with explicit date syntax
(`category:promotions before:2025/09/04`) — all zero. Consistent with recent prior runs:
this account's categorized promo/social/forums mail does not extend past the 12-month
cutoff, so there was no qualifying candidate set tonight. Nothing was skipped for
starred/important since the candidate set itself was empty.

`category:updates older_than:1y` (report-only, never auto-trashed): 0 threads — nothing
to list as "old updates to clear by hand."

## Per-run cap

Not triggered (0 trash candidates, well under the 200/run cap).

## Recovery

N/A this run — nothing was moved to Trash. The 2 archived menu threads remain fully
accessible in All Mail under the `Vendor Menus` label; removing that label and re-adding
`INBOX` restores either to the inbox if miscategorized.

## Sources
- gmail: 2 threads listed above (Vendor Menus label applied, removed from Inbox)
