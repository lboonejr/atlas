---
created: 2026-09-06T23:07-04:00
updated: 2026-09-06T23:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run log, 2026-09-06

Mode: **LIVE** (`DRY_RUN = false`)
Account: `lemar@cuzziesnj.com`

## PART A — vendor menus archived: 3

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1a0721f538d91d8e | Labor Day Special !!!! Buy 4 Get 1 across the whole menu !!!! | Austin@niche.apextrading.com | 2026-09-05 |
| 1a06cd9d10c40a4c | Labdor Day Weekend Sale: Niche x Goodies | Austin@niche.apextrading.com | 2026-09-04 |
| 1a063fe6267372e3 | End of Summer Savings! | maggie.boyd@verano.com | 2026-09-02 |

All three qualified on domain-on-seed-list (apextrading.com subdomain, verano.com) AND
either an explicit "menu" keyword or an itemized SKU/price list with a live ordering
link ("Shop Now" per-SKU links; Verano's "Order on Leaf Trade" catalog link). All were
labeled `Vendor Menus` (`Label_7063567382570959882`) and removed from Inbox — nothing
trashed, fully recoverable in All Mail under the label.

Other seed-list domain hits in the inbox (16 total matched `from:` the seed list) were
reviewed and skipped as not genuine menus (precision over recall): 5 "Account On Hold" /
"Friendly Reminder – Outstanding Balance" collections notices from awholdings.com, a
run of Verano AR-statement correspondence threads (incl. Lemar's own replies), two
TerrAscend out-of-office notices, and a QCC/qccnj.com onboarding-docs thread that also
carries genuine filing labels `Action Needed` + `Finance Bills`. None of these are
vendor marketing/menus — all are 1:1 business correspondence and were left untouched.

## PART B — trash sweep: 0 trashed, 0 candidates

Searched `older_than:1y (category:promotions OR category:social OR category:forums)` —
zero threads. Cross-checked each category individually
(`category:promotions older_than:1y`, `category:social older_than:1y`,
`category:forums older_than:1y`) — all independently zero. Consistent with every prior
run this month: this account's categorized promo/social/forums mail does not extend
past the 12-month cutoff, so there was no qualifying candidate set tonight. Nothing was
skipped for starred/important since the candidate set itself was empty.

`category:updates older_than:1y` (report-only, never auto-trashed): 1 thread — a
Weedmaps pickup-notification (hello@email.weedmaps.com, 2025-09-04). Not worth a
by-hand-clearing recommendation at this volume; noted for completeness only.

## Per-run cap

Not triggered (0 trash candidates, well under the 200/run cap).

## Safety checks

Live Gmail label table re-verified against `.claude/anchors.md` before acting — exact
match, no drift (Label_1 Sweep/Review, Label_2–6 Samira automation labels,
Label_374039230306167562 Action Needed, Label_4897882779882705846 Finance Bills,
Vendor Menus Label_7063567382570959882). No thread was trashed, spammed, sent, drafted,
or permanently deleted. No account other than `lemar@cuzziesnj.com` touched; Drive
untouched.

## Recovery

N/A this run — nothing was moved to Trash. The 3 archived menu threads remain fully
accessible in All Mail under the `Vendor Menus` label; removing that label and re-adding
`INBOX` restores any of them to the inbox if miscategorized.

## Sources
- gmail: 3 threads listed above (Vendor Menus label applied, removed from Inbox)
