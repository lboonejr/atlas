---
created: 2026-07-22T23:07-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail, cleanup, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-22 (LIVE, first live run)

**Mode:** `DRY_RUN=false` — first real-action run; prior runs were dry-run preview only.
**Account acted on:** lemar@cuzziesnj.com (business, connected account).

## PART A — Vendor menus archived: 48 threads

Labeled `Vendor Menus` (`Label_8`) and removed from `INBOX`. This was a backlog
accumulated during the dry-run period — menu blasts from vendors on/near the seed list
(Harvest Moon Farms, Kiva, Fernway, Apex Trading sellers, Mudd Brothers, QCC NJ, Illicit
Gardens, North Lake Supply, Green Lightning, Garden Greens, Hamilton Farms, Kushi Labs,
Brute's Roots, Glass Meadows, Ayr Wellness, Distru, Binske, Chill Medicated, PMC, and a
few accessory/hardware vendors) spanning roughly March–July 2026. Precision-first: skipped
weaker candidates (relationship/social marketing without a real menu/price signal, active
1:1 negotiation threads, internal Drive-share notifications, ambiguously-addressed threads).
Full 48 thread IDs live in Gmail under the Vendor Menus label — not restated here.

## PART B — Trash sweep: 31 threads trashed (>12mo, promotions/social/forums)

Gate applied: `older_than:1y`, category promotions/social/forums, NOT starred, NOT
important, no genuine filing label, sender domain not on the NEVER-TOUCH allowlist.
Well under the 200/run cap. **Recovery window: Gmail Trash, 30 days from tonight
(clears ~2026-08-21).**

Audit (thread ID · sender · subject · date):

1. `1982f02bbc86966f` · wholesale@verano.com · "Nothing's rotten here" · 2025-07-21
2. `1982df12f782f9c9` · andrew@northlake.supply · "Serving Up Sussex Sour Apple, Plus Get Mobster Mango 2 Grams While You Still Can!" · 2025-07-21
3. `1982dc7e66ff470a` · marketing.us@terrascend.com · "Experience the High Life 💎 Diamond Infused Pre-Roll 2PKs" · 2025-07-21
4. `1982d8a0259d7b72` · info@blunacan.com · "BLUNA: BLUNA to Exhibit at Cannafair 2025 in Düsseldorf, Germany" · 2025-07-21
5. `1982d6fd7a0fb949` · andrew@northlake.supply · "New Drops & Fan Favorites Restocked - Let's Talk Promos" · 2025-07-21
6. `1982d5b44a9c953a` · jamie-nichenfe.com@shared1.ccsend.com · "Smalls are Back - 2 SKU's Added Today!!" · 2025-07-21
7. `1982d4d7e0ba58cf` · jonathon@hoodieanalytics.com · "Live Webinar from Hoodie Analytics: Flying Blind" · 2025-07-21
8. `1982d365247e0022` · sales@hamiltonfarms.com · "Hamilton Farms Weekly Menu & Promotion" · 2025-07-21
9. `1982cbc3a86aacfc` · Chris@little-leaf-labs.apextrading.com · "New Products- Our Best Flavors Yet" · 2025-07-21
10. `1982ca4bd3011f00` · jason@bridgecitycollective.com · "PANDA FARMS is KILLIN it!!" · 2025-07-21
11. `1938298575ae69f0` · microsoft.start@email2.microsoft.com · "Trump picks loyalist Kash Patel to head FBI" · 2024-12-01
12. `193883dd7173fe57` · sales@hamiltonfarms.com · "Hamilton Farms Updated Menu!" · 2024-12-02
13. `1938835f15d33495` · blog@send.zapier.com · "Automate recurring tasks" · 2024-12-02
14. `1938834ba19b8b20` · sales@hamiltonfarms.com · "Hamilton Farms Updated Menu!" (duplicate send) · 2024-12-02
15. `19388281ea4c86db` · dan@northlake.supply · "Spark Greatness with Highsman by Ricky Williams" · 2024-12-02
16. `19387c616aa8d739` · marketing@leaftrade.com · "Shop Grassroots Flower!" · 2024-12-02
17. `19387b1c22a6e154` · jenna@newjerseycannabusinessassociation.ccsend.com · "You don't want to miss out!" · 2024-12-02
18. `193874c01e4d33c5` · emanuel@alphasecurity.ccsend.com · "Keep Your Home Safe and Secure" · 2024-12-02
19. `1937a7c5f0788d0a` · update@dotcards.net · "ALMOST OVER – 30% Off Everything We Sell" · 2024-11-30
20. `1937a21a2bb814db` · update@dotcards.net · "Happening Now: 30% Off Everything" · 2024-11-29
21. `19379a9dfec319a5` · faai@covasoftware.com · "Get Ready for the Most Anticipated MJBizCon After Party" · 2024-11-29
22. `193797f90ccd1a25` · dayna@covasoftware.com · "Here's How to Connect with Cova at MJBizCon!" · 2024-11-29
23. `193793cb8d1512cb` · update@dotcards.net · "EVERYTHING Is 30% OFF - Our Best Sale of the Year" · 2024-11-29
24. `1937909d9aec2205` · salexander-vhrrental.com@voorheeshardware.ccsend.com · "One Day Bucket Sale!" · 2024-11-29
25. `1937875033090ac8` · marketing@engage.canva.com · "25% off print products: Holiday gifting = sorted" · 2024-11-29
26. `19377eb11a85a454` · no-reply@marketing.otter.ai · "Final Reminder: Black Friday Bonus—8 Months Free with Pro Annual!" · 2024-11-29
27. `19377a1d006786e4` · emanuel@alphasecurity.ccsend.com · "Last Day for Black Friday Deals" · 2024-11-29
28. `19373658df3f7663` · main-palmestatesco.com@shared1.ccsend.com · "Your Holiday Real Estate Update" · 2024-11-28
29. `1936fc75906a76b0` · jenna@newjerseycannabusinessassociation.ccsend.com · "You don't want to miss out!" · 2024-11-27
30. `1936eb90bf005fe4` · update@dotcards.net · "Happening Now: 25% Off Everything" · 2024-11-27
31. `1943baba70409e20` · dan@northlake.supply · "North Lake Supply: Exclusive Deals Just for You!" · 2025-01-06

**Skipped-for-protection:** the large majority of scanned candidates (roughly 120+ of
~150 reviewed across 3 search pages) were skipped because they carried `is:important` or
`is:starred`, or the sender domain was on the NEVER-TOUCH allowlist (`parkebank.com`,
`intuit.com`/`notification.intuit.com`, `stellaconnect.net`, `*.gov` domains like
`sos.nj.gov`). This confirms the runbook's own recon finding that this inbox
over-applies Gmail's IMPORTANT label broadly — the gate held conservative as designed.

**Coverage note:** PART B only scanned back to 2024-11-27 (~8 months of the >12mo-old
backlog) before stopping for tonight. More qualifying candidates likely exist further
back and will be picked up on subsequent nightly runs — well under the 200/run cap
either way, no urgency.

## category:updates (report-only, never auto-trashed)

Large volume (200+ estimate) of old `updates`-category mail, confirmed mixed with
financial/operational mail per the runbook's warning — sender domains seen:
`quickbooks@notification.intuit.com`, `IntuitPartners@dp.intuit.com`, `info@headset.io`,
`no-reply@fedex.com` / `no-reply.ecommerce@fedex.com`, `noreply@jotform.com` /
`jotformsign.com`, `socialequity@weedmaps.com`, `no-reply@leaflink.com`,
`CTA@sos.nj.gov`. Left untouched per the routine — Lemar may want to clear some of these
by hand.

## Next run

`DRY_RUN` stays `false`. The vendor-menu backlog for the current seed list looks
substantially cleared. PART B should keep working backward through the >12mo backlog on
subsequent nightly runs.

## Sources
- gmail: lemar@cuzziesnj.com inbox sweep, 2026-07-22 (thread IDs above)
