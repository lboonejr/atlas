---
created: 2026-08-10T23:15-04:00
updated: 2026-08-10T23:15-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run log, 2026-08-10 (11pm ET)

**Mode:** LIVE (DRY_RUN=false)
**Account:** lemar@cuzziesnj.com

## Summary

- **Part A (vendor menus archived):** 42 threads labeled `Vendor Menus` (Label_8) and
  removed from Inbox. Query: `in:inbox has:attachment (subject:menu OR subject:"price
  sheet" OR subject:"live menu" OR subject:availability OR subject:"in stock" OR
  subject:drop)`, one page reviewed (50 results, 201 total estimate — more remain further
  back than Oct 2025 for a future run). 8 threads skipped as starred, weakly-a-menu, or
  really AR/collections/account-status threads misfiled by the query (thegardensociety.com
  payment reminders, Grön Edibles x2 starred, HF Fresh Menu 1.23.26 starred, Delight & KAI
  WSA starred, Cannabist menu starred, Humble Camp "Menu is Hottt" starred, Happy Eddie
  account-status thread starred, Sun Extractions meeting-recap thread).
- **Part B (old promo/social/forums trashed, >12mo):** 2 threads trashed, 0 over the
  200/run cap. 150 candidates reviewed across 3 pages (of ~201 total) for
  `in:inbox older_than:1y (category:promotions OR category:social OR category:forums)`;
  ~148 left untouched — the overwhelming majority carry Gmail's auto-`IMPORTANT` label
  somewhere in the thread, with a smaller number protected by the NEVER-TOUCH allowlist
  (`parkebank.com`, `*.sos.nj.gov`, `intuit.com`/QuickBooks, `stellaconnect.net`/Metrc,
  the FundCanna underwriting senders). Did not paginate past 150 given the very low yield
  (2/150) — remaining ~51 candidates carry forward to a future run.
- **category:updates:** ~201 threads found, report-only, no action taken. Sample sender
  domains: jotform.com/jotformsign.com (register-float approvals — operational, do not
  bulk-clear), headset.io (daily sales summaries — allowlisted), nytimes.com,
  redditmail.com, e1.theathletic.com, aiq.com.
- **Skipped for is:important/is:starred:** 7 in Part A (all starred), ~145 in Part B
  (IMPORTANT-labeled) — no allowlist domain looked miscategorized.

## Part A archive list (42 threads)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 19fd75b13bafd02a | Hillview NEW PRICING/NEW DROP SUPER RUNTZ | jaime@hillviewmed.com | 2026-08-06 |
| 19fd288e197e5bfe | 8/5 MPX Menu Re-Fresh | Sidney.Jenkins@ianthus.com | 2026-08-05 |
| 19fcca7a00a4dc9c | Hillview NEW PRICING/NEW DROP SUPER RUNTZ | Chris@hillviewmed.com | 2026-08-04 |
| 19fc9d510530ed32 | Culture Craft Menu - Hello August! | info@culture-craft.com | 2026-08-03 |
| 19fc8f10212ce1a9 | New Victory and Stash House Menu 8.3 | jshort@stashhousedistro.com | 2026-08-03 |
| 19fc8e3543613c23 | Hamilton Farms x Cuzzie's - Monday Menu Update | wholesale@hamiltonfarms.com | 2026-08-03 |
| 19fb8a7f788d349d | Hillview NEW PRICING/NEW DROP SUPER RUNTZ | Chris@hillviewmed.com | 2026-07-31 |
| 19fc7809e27e46c1 | HighTide Drink + MGB New Ounces/Prerolls Menu | jbombara55@gmail.com | 2026-08-03 |
| 19a9789f7f771f76 | MPX Menu + NEW Drops: Liquid Diamond 1G AIO | Sidney.Jenkins@ianthus.com | 2025-11-18 |
| 19a9373ce8223a6c | Revelry & Field Trip Wholesale Menu - 11.17 | tj@humblecamp.com | 2025-11-17 |
| 19a92445cc1c3079 | Menu Monday - Brute's Roots | josh@brutesroots.com | 2025-11-17 |
| 19a7ead5a3763039 | Hamilton Farms Menu Update! 20% off | breali@hamiltonfarms.com | 2025-11-13 |
| 19a7e61a2275c406 | Garden Greens End of Week Menu | loudpacklu@ggcann.com | 2025-11-13 |
| 19a7df534dfa628b | Cheetah 5-Pack Live Resin Infused Pre-Rolls | Sidney.Jenkins@ianthus.com | 2025-11-13 |
| 19a7981763ce6f85 | HUGE New ONYX Cart Drop + Green Wednesday Deals | pdemuro@sussexcultivation.com | 2025-11-12 |
| 19a6ec0ac05bee0a | Monday Motivation - New Menu | jsclocchini@stashhousedistro.com | 2025-11-10 |
| 19a6e23d9b9aac84 | Green Lightning Menu | carlee@greenlightningcannabis.com | 2025-11-10 |
| 19a5f72450ef8e7a | Next Level Brands Menu - 11.7 | tj@nextlevelbrands.net | 2025-11-07 |
| 19a5a3128a836be8 | Garden Greens End of Week Menu | loudpacklu@ggcann.com | 2025-11-06 |
| 19a556750fe50906 | Garden Greens Menu | loudpacklu@ggcann.com | 2025-11-05 |
| 19a542d47169f45f | Green Lightning Menu | carlee@greenlightningcannabis.com | 2025-11-05 |
| 19a4f8e011160f2d | Hamilton Farms Menu and Green Wednesday Promo | gcorchado@hamiltonfarms.com | 2025-11-04 |
| 19a4f639bb1cd148 | Mudd Brothers Menu 11.04.25 | wholesale@mbcannabisco.com | 2025-11-04 |
| 19a4bec877f8009a | Grön Edibles Fresh Menu | dfortunato@eatgron.com | 2025-11-03 |
| 19a4b4ab9826f946 | ONYX Menu & Nuvata Pricing Sheet - 11.3.25 | pdemuro@sussexcultivation.com | 2025-11-03 |
| 19a49de55b25a980 | Green Lightning Menu | carlee@greenlightningcannabis.com | 2025-11-03 |
| 19a3bdc51f5dcc48 | Nxt Lvl Wholesale Menu - 10.31 | tj@nextlevelbrands.net | 2025-10-31 |
| 19a3b61de4109f9b | Happy Halloween HF MENU | gcorchado@hamiltonfarms.com | 2025-10-31 |
| 19a3a475fb2fcb8f | Green Lightning Halloween Menu | carlee@greenlightningcannabis.com | 2025-10-31 |
| 19a3602ed1fbda21 | Garden Greens End of Week Menu | loudpacklu@ggcann.com | 2025-10-30 |
| 19a30aa004f582d5 | Fresh Drop Alert: THE VAULT Is Officially Unlocked | Sidney.Jenkins@ianthus.com | 2025-10-29 |
| 19a3009958ee4c6e | Green Lightning Menu | carlee@greenlightningcannabis.com | 2025-10-29 |
| 19a2ad59fe2bdcb0 | Mudd Brothers Menu 10.28.25 | wholesale@mbcannabisco.com | 2025-10-28 |
| 19a2775dc6065658 | Next Level MENU - 15% OFF | tj@nextlevelbrands.net | 2025-10-27 |
| 19a2767bdca18ad1 | Next Level MENU - 15% OFF | ttassi856@gmail.com | 2025-10-27 |
| 19a265a70d7bb6f0 | Hamilton Farms Menu & Announcement | sales@hamiltonfarms.com | 2025-10-27 |
| 19a25abc6f226dcb | Green Lightning Menu | carlee@greenlightningcannabis.com | 2025-10-27 |
| 19a17ded01127fc6 | Don't Let Your Menu Haunt You - Emunio | sberman@emuniologistics.com | 2025-10-24 |
| 19a16fd3a3ed7a3b | 10.24 Menu & Re-Stocks | Sidney.Jenkins@ianthus.com | 2025-10-24 |
| 19a1225b3bfb5e4a | Next Level Brands Wholesale Menu - 10.23 | tj@nextlevelbrands.net | 2025-10-23 |
| 19a12178ebefd50a | Garden Greens Menu | loudpacklu@ggcann.com | 2025-10-23 |
| 19a11f3911a8e3cd | $3.50 PRs, Monday's Drop - LoveGrow 10/23 | sales@lovegrow.co | 2025-10-23 |

## Part B trash audit (recoverable from Gmail Trash for 30 days, i.e. until ~2026-09-09)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 19890c4c01970992 | The Apple Shopping Event is happening right now | BestBuy@email.bestbuy.com | 2025-08-09 |
| 1988f1e060003e8e | Reminder: Follow up (Extra Space Storage review request) | extra_space@birdeye.com | 2025-08-09 |

## Judgment calls / flags for Lemar (no action taken — informational only)

1. This account's Gmail auto-`IMPORTANT` marking is extremely aggressive — it protected
   roughly 148 of 150 reviewed Part B candidates tonight. This is the safety floor working
   as designed, but it means the trash sweep will stay very low-yield run over run unless
   Lemar wants the IMPORTANT-guard tuned or narrowed.
2. Several threads matched the Part A search query on keywords alone but were actually
   AR statements, collections notices, or account-status threads from vendors
   (thegardensociety.com, budsgoods.com, prolificgrowhouse.com, illicitgardens.com,
   kivaconfections.com) — left untouched per the precision-over-recall instruction; the
   query still surfaces these as false positives and may be worth tightening later.
3. No FundCanna underwriting thread appeared in the trash candidate pool tonight — no
   risk this run.
4. Vendor-menu backlog beyond Oct 2025 (further back in time) was not reached this run;
   expect it to keep surfacing on subsequent nights.

## Sources
- claude: Basil nightly run, 2026-08-10 ~11pm ET
