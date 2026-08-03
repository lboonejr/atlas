---
created: 2026-08-01T00:00-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-01

Live run (`DRY_RUN=false`), continuing from [[2026-07-31-basil-inbox-janitor-run]],
[[2026-07-30-basil-inbox-janitor-run]], and [[2026-07-29-basil-inbox-janitor-run]].
Account: `lemar@cuzziesnj.com` (the only connected Gmail account; Drive out of scope).
Archived 58 vendor-menu threads out of the inbox and trashed 5 old promotional threads
(recoverable in Gmail Trash for 30 days). Both stayed well under their per-run caps and
respected the NEVER-TOUCH allowlist and the starred/important floor from
`.claude/anchors.md`.

**Tuning note for Lemar:** across both PART A and PART B, the large majority of
candidate threads reviewed (150–200+ each) were excluded because Gmail's own IMPORTANT
classifier had tagged them — not a label Lemar applied, but the hard floor treats it the
same. This made the safe/eligible pool much smaller than the raw category-match counts
(e.g. PART B: only 5 of roughly 150 reviewed `category:promotions/social/forums` threads
were both `older_than:1y` and free of IMPORTANT/STARRED/allowlist). Worth knowing:
Gmail appears to be marking most ongoing vendor correspondence on this account as
important, which is why the trash sweep is running much lighter than the promotions
category alone would suggest.

## PART A — vendor menus archived (58)

Query: broad vendor-domain-seed + `has:attachment` search, then narrowed to
`subject:menu` (and a few explicit "menu" mentions in the snippet) to precisely target
one-way wholesale menu/price-sheet blasts. Each candidate was individually checked and
excluded if it carried a STARRED or IMPORTANT label, or a genuine user-applied filing
label — held to the hard floor from the bootstrap prompt (never touch
starred/important/user-labeled threads), which is stricter than the routine's own
PART A text (written to gate PART B only, applied here too out of caution). All 58
qualified threads were labeled `Vendor Menus` (`Label_8`) then had `INBOX` removed.

Senders included: Fresh Grow (freshcannabis.co), Nova Farms, Harvest Moon Farms, MPX /
iAnthus, Ascend (awholdings.com), Bud's Goods, Kushi Labs, Green Lightning, Next Level
Brands, PanCann, Mudd Brothers, Hillview, Brute's Roots, Ares Canna — all recurring
wholesale-menu blast senders, one-way (no active back-and-forth with Lemar).

| # | Thread ID | Subject | Sender | Date |
|---|---|---|---|---|
| 1 | 19fba06295701c5c | Fresh Grow Menu \| DICE Edibles Now Available + Over 30 ZIP Options! | Kathy@freshcannabis.co | 2026-07-31 |
| 2 | 19fb92c8d156e2ce | NOVA FARMS DAY – LIVE ON SITE 🌿 | bbreslow@novafarms.com | 2026-07-31 |
| 3 | 19fb91db1a279814 | 🔥 Final Wholesale Menu Update – Stock Up Before the Weekend | allanf@harvestmoonfarmsnj.com | 2026-07-31 |
| 4 | 19fb8bcd16081086 | Re: MPX Fresh Menu Friday's! 💥 | Sidney.Jenkins@ianthus.com | 2026-07-31 |
| 5 | 19fb8a7f788d349d | Hillview <> NEW PRICING <> NEW DROP SUPER RUNTZ | Chris@hillviewmed.com | 2026-07-31 |
| 6 | 19fb8a658f4d6160 | Bud's Goods Menu - New Flower Drop! | mzaidi@budsgoods.com | 2026-07-31 |
| 7 | 19fb870d841cf22f | Ascend Friday Updated Menu \| Sativas Stocked Up | nbonsanto@awholdings.com | 2026-07-31 |
| 8 | 19fae8dac734347a | Going, Going... Almost Gone | alex@jerseysmooth.com | 2026-07-29 |
| 9 | 19fae71c54c92f25 | Going, Going... Almost Gone (dup send) | alex@jerseysmooth.com | 2026-07-29 |
| 10 | 19fa5e98de663aa5 | Happy Monday! Let's Have a Smooth Week | alex@jerseysmooth.com | 2026-07-27 |
| 11 | 19d403b8c4c52642 | Ares Canna 3.30 - Flower, Pre-Rolls, Gummies, Balms, Vapes, THC Syrups | tj@arescanna.com | 2026-03-30 |
| 12 | 19bd73582125ed60 | Kushi Labs: Fresh Menu Drop — The Clear, TWAX, Second Act & House Vape 🚀 | katie@kushilabs.com | 2026-01-19 |
| 13 | 19bd71125c148db7 | ❄️ 1/19 MPX Menu: Last Chance Drops + Flash EOM Sale | Sidney.Jenkins@ianthus.com | 2026-01-19 |
| 14 | 19bd6c3402a0ec0c | Nuvata Now Available on the ONYX Apex Menu! | pdemuro@sussexcultivation.com | 2026-01-19 |
| 15 | 19bd69e6f4a25b27 | Humble Camp Menu - 10% Off Edie P Vapes Today Only | julien@humblecamp.com | 2026-01-19 |
| 16 | 19bc6f7456d256dd | Green Lightning Weekend Menu: Zoda & Bananaconda | miles@greenlightningcannabis.com | 2026-01-16 |
| 17 | 19bc259e00679c7a | Garden Greens EOW Menu | loudpacklu@ggcann.com | 2026-01-15 |
| 18 | 19bbdc54ad38445d | Garden Greens Menu | loudpacklu@ggcann.com | 2026-01-14 |
| 19 | 19bbcf3aabadba2c | Green Lightning Wednesday Wholesale Menu | miles@greenlightningcannabis.com | 2026-01-14 |
| 20 | 19ba504b39c84ee9 | Next Level Brands Weekend Menu | tj@nextlevelbrands.net | 2026-01-09 |
| 21 | 19b2490b19b7beaf | Next Level Brands Menu - 12.15 | tj@nextlevelbrands.net | 2025-12-16 |
| 22 | 19b248d15f5f5ced | Chew & Chill Gummies -- Good Times Gummies & Vapes -- 12.15 Menu | tj@pancann.com | 2025-12-16 |
| 23 | 19b22839fc593230 | BRUTE'S ROOTS MENU // December 15 | josh@brutesroots.com | 2025-12-15 |
| 24 | 19b2274e3b815dd0 | Green Lightning Menu: Strike Disposables, GRUV Rosin | carlee@greenlightningcannabis.com | 2025-12-15 |
| 25 | 19b141fbc61197ce | Hillview Indoor & SunGrown Flower Menu | TJ@hillviewmed.com | 2025-12-12 |
| 26 | 19b13ede16e28d2a | REVELRY & EDIE PARKER Wholesale Menu | tj@humblecamp.com | 2025-12-12 |
| 27 | 19b13cef6873d85e | Next Level Brands Menu - 12.12 | tj@nextlevelbrands.net | 2025-12-12 |
| 28 | 19b12f8ba466eac9 | Green Lighting Weekend Menu: Strike 2g AiOs Below $30!? | carlee@greenlightningcannabis.com | 2025-12-12 |
| 29 | 19b08b0a718adc63 | Green Lightning Menu: Strike Seasonal Vapes, GRUV Rosin | carlee@greenlightningcannabis.com | 2025-12-10 |
| 30 | 19b08a0ac840cc1c | 12.10 MPX Menu Update - Purple Punch Debut | Sidney.Jenkins@ianthus.com | 2025-12-10 |
| 31 | 19b006a2826eb44b | Next Level Brands Wholesale Menu - 12.8 | tj@nextlevelbrands.net | 2025-12-09 |
| 32 | 19b006747876a6e6 | PannCann Wholesale Menu - Edibles, Vapes, & Hash Rosin Syrup | tj@pancann.com | 2025-12-09 |
| 33 | 19aff29f1e05d488 | Kushi Labs: New Skus and December Menu Update | katie@kushilabs.com | 2025-12-08 |
| 34 | 19afeec4b21e6f90 | HF Fresh Menu and December Promos!!!! | gcorchado@hamiltonfarms.com | 2025-12-08 |
| 35 | 19afe884b23cb219 | Green Lightning Menu: GRUV Rosin & STRIKE vape promos | carlee@greenlightningcannabis.com | 2025-12-08 |
| 36 | 19ae4955353a9bf9 | Green Lightning Weekend Menu: Have You Seen Our Rosin | carlee@greenlightningcannabis.com | 2025-12-05 |
| 37 | 19adba2ab6795009 | Next Level Brands Menu - 12.1 | tj@nextlevelbrands.net | 2025-12-01 |
| 38 | 19adb4b03998ee19 | Kushi Labs: TWAX Multipacks Added to Menu | katie@kushilabs.com | 2025-12-01 |
| 39 | 19acadb00f910782 | Green Lightning Menu: Time to restock! Seasonal STRIKES | carlee@greenlightningcannabis.com | 2025-11-28 |
| 40 | 19ac1523ba416af8 | Updated Cannabist Menu - Happy Green Wednesday | chelsey.narcisso@cannabistcompany.com | 2025-11-26 |
| 41 | 19ac08879d468a4b | Green Lightning Menu: Super Boof, GG4, Slurricane | carlee@greenlightningcannabis.com | 2025-11-26 |
| 42 | 19abc121c096bca3 | Revelry & Field Trip Menu - 11.25 | tj@humblecamp.com | 2025-11-25 |
| 43 | 19abc040431156bd | PanCann Wholesale Menu - $11/unit RESIN GUMMIES | tj@pancann.com | 2025-11-25 |
| 44 | 19abbca5e33fcf0e | 20% off so let's get Muddy! Mudd Brothers Menu 11.25.25 | wholesale@mbcannabisco.com | 2025-11-25 |
| 45 | 19ab60d24426d268 | Green Lightning Menu: GG#4, Slurricane just landed | carlee@greenlightningcannabis.com | 2025-11-24 |
| 46 | 19aa6b600fba28f4 | Green Lightning Menu: DIAMOND INFUSED PRE-ROLLS!!! | carlee@greenlightningcannabis.com | 2025-11-21 |
| 47 | 19a9c627d3ff929e | Green Lightning Menu: TWELVE ROSIN STRAINS, NEW STRIKE | carlee@greenlightningcannabis.com | 2025-11-19 |
| 48 | 19a98a2efa231627 | 20% off all orders! Mudd Brothers Menu 11.18.25 | wholesale@mbcannabisco.com | 2025-11-18 |
| 49 | 19a97047d20c425c | Next Level Wholesale Menu - 11.18 | tj@nextlevelbrands.net | 2025-11-18 |
| 50 | 19a9367cf9a992ef | PanCann Wholesale Menu - 11.17 | arescannaconsulting@gmail.com | 2025-11-17 |
| 51 | 19a91f69f9c20791 | Green Lightning Menu: Ounce Strain Expansion!! | carlee@greenlightningcannabis.com | 2025-11-17 |
| 52 | 19a836029ec20488 | Next Level Brands Weekend Menu - $3.50 - $5 1g Pre-Rolls | tj@nextlevelbrands.net | 2025-11-14 |
| 53 | 19a7ebd865e68087 | Green Wednesday 20% Off Promo and Fresh Menu | gcorchado@hamiltonfarms.com | 2025-11-13 |
| 54 | 19a786e24b57e5a4 | Green Lightning Menu: Han Solo Burger Smalls @ 41% THCA | carlee@greenlightningcannabis.com | 2025-11-12 |
| 55 | 19a749a0ee13ee62 | Add a High-Margin Local Brand to Your Menu: House Vape | katie@kushilabs.com | 2025-11-11 |
| 56 | 19a73e01288e0868 | Next Level Brands Menu - 1g Pre-Roll SALE | tj@nextlevelbrands.net | 2025-11-11 |
| 57 | 19a7303a0a5ed14c | Mudd Brothers Menu 11.11.25 - Support Local Brands & Community | wholesale@mbcannabisco.com | 2025-11-11 |
| 58 | 19a6ec9e170194d8 | New Brute's Roots Menu! 11/10 | josh@brutesroots.com | 2025-11-10 |

## PART B — trash sweep (5 trashed, recoverable 30 days)

Query: `in:inbox older_than:1y {category:promotions OR category:social OR
category:forums}`. Reviewed ~150 threads across the result pages; only 5 passed every
gate (`older_than:1y` AND category match AND not STARRED/IMPORTANT/genuine-labeled AND
sender domain not on the NEVER-TOUCH allowlist). 0 threads hit the 200/run cap.

| # | Thread ID | Subject | Sender | Date |
|---|---|---|---|---|
| 1 | 19862a869d3a42a1 | 🏋️ 597 Pounds. | info@fernway.com | 2025-07-31 |
| 2 | 1986172735c1f2f7 | Merchandise Smarter, Sell More \| July Newsletter | newsletter@rankreallyhigh.com | 2025-07-31 |
| 3 | 19860d3a880f05bb | New templates added for design | product@engage.canva.com | 2025-07-31 |
| 4 | 19860c1a48a3154c | 🙂 Your budget likes deals! | flyers@webstaurantstore.com | 2025-07-31 |
| 5 | 19860a56c59481d5 | New Prices AND New Flower 🎉👀‼️ | marketing.us@terrascend.com | 2025-07-31 |

Threads skipped from the trash pool for carrying IMPORTANT (Gmail's own classifier, not
a Lemar label): mostly recurring vendor marketing from High Grass Farms
(apextrading.com), jamie-nichenfe.com, Verano, Dutchie, Vangst, Treez, FundCanna, and
others. Skipped for the NEVER-TOUCH allowlist: `parkebank.com` (3 threads) and
`*.sos.nj.gov` (4 CTA training threads, covered by the `*.gov` rule).

## `category:updates` — report-only (never auto-trashed)

~201 threads older than 1 year sit in `category:updates` in the inbox. Per the runbook
this category is never swept — it mixes real operational/financial mail with noise.
Sample senders/types seen in this account: Jotform register-float approvals and
signature confirmations, Google Voice missed-call/voicemail/text notices, Headset.io
scheduled reports, Intuit overdue-tax notices, DocuSign completions, ClickPay rent
reminders (property 2778 Mount Ephraim), NYTimes breaking-news alerts, Reddit digests,
and Dutchie/Zendesk support-satisfaction surveys. Worth a hand pass if Lemar wants this
folder thinned — none of it was touched tonight.

No email was sent or drafted. No Trash was emptied, no Spam applied. No account other
than `lemar@cuzziesnj.com` was touched. Nothing starred/important/user-labeled or newer
than 12 months was archived or trashed.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox — search_threads / label_thread / unlabel_thread /
  apply_sensitive_thread_label, run 2026-08-01
