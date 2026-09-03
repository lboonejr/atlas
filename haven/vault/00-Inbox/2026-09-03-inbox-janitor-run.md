---
created: 2026-09-03T23:07-04:00
updated: 2026-09-03T23:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run log, 2026-09-03

Mode: **LIVE** (`DRY_RUN = false`)
Account: `lemar@cuzziesnj.com`

## PART A — vendor menus archived: 14

All 14 qualified on a combination of signals (a menu signal in the subject/snippet AND
either a real attachment or in-body shop/menu links). Each was labeled `Vendor Menus`
(`Label_7063567382570959882`) and removed from the Inbox — nothing trashed, fully
recoverable in All Mail under the label.

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1a062b506e595801 | Niche x Goodies Menu | Austin@niche.apextrading.com | 2026-09-02 |
| 1a0101ef9d9d67d4 | Fresh Menu! 8/17 | romeo.dilla@brutesroots.com | 2026-08-17 |
| 19fc9d50ebf9e7e3 | Culture Craft Menu - Hello August! ☀️ | info@culture-craft.com | 2026-08-03 |
| 19fc8d9d60f0415a | Hamilton Farms x Cuzzie's Dispensary - Monday Menu Update | wholesale@hamiltonfarms.com | 2026-08-03 |
| 19faa2181f6ae697 | 🔥 Fresh Drop Alert: Green Crack × Baja Blast | info@culture-craft.com | 2026-07-28 |
| 19fa4337fe4d5f7c | Hamilton Farms x Cuzzie's Dispensary- Your Monday Menu Update | amoyer@hamiltonfarms.com | 2026-07-27 |
| 19f8a32f07cda470 | Fresh Menu! 7/22 | romeo.dilla@brutesroots.com | 2026-07-22 |
| 19f6634a685dcf93 | Hamilton Farms x Cuzzie's Dispensary Brand Reactivation - Mid-week Menu Update | wholesale@hamiltonfarms.com | 2026-07-15 |
| 19f13639f4b654b8 | Hamilton Farms x Cuzzie's Dispensary Wholesale Menu - Fresh Drops | wholesale@hamiltonfarms.com | 2026-06-29 |
| 19f00c0f9dd096c0 | 🥅NEW MENU ALERT🥅 Hash 4 Euros | info@culture-craft.com | 2026-06-25 |
| 19eff625bf3266c7 | Hamilton Farms Mid-Week Menu Update - Panama Red, Grapefruit Chem & Tyson Drops | wholesale@hamiltonfarms.com | 2026-06-25 |
| 19ed7080079f0a06 | Hamilton Farms x Cuzzie's Dispensary - Mid-Week Menu Update | wholesale@hamiltonfarms.com | 2026-06-17 |
| 19ecb69742a3252f | Brute's Roots - 6/15 Menu 💨💨💨 | josh@brutesroots.com | 2026-06-15 |
| 19eb27263ac08725 | 🌱 Hamilton Farms x Cuzzie's Dispensary Wholesale Menu Update | wholesale@hamiltonfarms.com | 2026-06-10 |

**Tuning note:** only 1 of the 14 (apextrading.com) was on the anchors.md vendor-domain
seed list. The other 13 came from three recurring menu senders not yet in the seed
list: `brutesroots.com`, `culture-craft.com`, `hamiltonfarms.com`. They qualified on the
subject-signal branch of the PART A gate (explicit "Menu"/"Drop" text plus a real
attachment). Recommend adding these three domains to the seed list in `anchors.md` so
future runs match them on the domain signal directly.

## PART B — trash sweep: 0 trashed, 0 candidates

Searched `older_than:1y (category:promotions OR category:social OR category:forums)`
and each category individually — all returned zero threads. Cross-checked with
`older_than:6m`, `older_than:180d`, and `older_than:365d` variants combined with
`category:promotions` — all zero too. This account's Gmail category classification
(promotions/social/forums) does not appear to extend past roughly 90 days of mail
history, so there was no qualifying trash-sweep candidate set tonight. Nothing was
skipped for starred/important since the candidate set itself was empty.

`category:updates older_than:1y` (report-only, never auto-trashed): 0 threads — nothing
to list as "old updates to clear by hand."

## Per-run cap

Not triggered (0 trash candidates, well under the 200/run cap).

## Recovery

N/A this run — nothing was moved to Trash. The 14 archived menu threads remain fully
accessible in All Mail under the `Vendor Menus` label; removing that label and re-adding
`INBOX` restores any of them to the inbox if one was miscategorized.

## Sources
- gmail: 14 threads listed above (Vendor Menus label applied, removed from Inbox)
