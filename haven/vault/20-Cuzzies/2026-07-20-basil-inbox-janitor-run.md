---
created: 2026-07-20T23:15:00-04:00
updated: 2026-07-20T08:04:43-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-20

**Mode:** LIVE (DRY_RUN=false) · **Account:** lemar@cuzziesnj.com

## Summary
- **91 vendor-menu threads archived** (PART A) — labeled `Vendor Menus` (Label_8), removed from Inbox, retained in All Mail. Zero failures.
- **136 threads trashed** (PART B) — 12-month-old promotions/social/forums mail, well under the 200/run cap. Zero failures. Recoverable in Gmail Trash for 30 days (until ~2026-08-19).
- **0 threads skipped for being over cap.**
- Skipped from the trash candidate pool for protection: 5 threads from `parkebank.com` (NEVER-TOUCH allowlist), 6 threads from `sos.nj.gov` (`*.gov` allowlist), and 2 threads that carried an IMPORTANT-labeled message despite matching the category/age filter (one Dutchie survey thread, one Hamilton Farms thread with an active payment-terms negotiation reply from a broker).
- **Backlog note:** both the vendor-menu archive queue and the trash-eligible pool still had more candidates beyond this run's ~91/~136 batch (Gmail estimated ~200+ matches for each search before per-thread filtering). This reads as a first substantial catch-up run covering roughly Jan–Jul 2025 vendor menus and Jan–Jul 2025 old promo/social mail. Expect smaller nightly deltas going forward — Basil will keep working the remainder on subsequent nights.
- **Report-only `category:updates`:** ~201 old (>12mo) threads found, never auto-trashed per the runbook. Sample sender domains seen: softtouchpos.com, jotform.com, jotformsign.com, headset.io (allowlisted), adt.com, voice-noreply@google.com. Mixes invoices/POS/security-system notices with some ads — worth a manual look if Lemar wants that area lighter, but Basil does not touch it.

## PART A — Vendor menus archived (91 threads, sample of distinct senders)
apextrading.com, ianthus.com (MPX menus), hamiltonfarms.com, canopy-usa.com, culture-craft.com, hillviewmed.com, jbombara55@gmail.com (MGB/Sun broker), brutesroots.com, humblecamp.com, hgfarmsnj.com, authorizeddealernj.com, ggcann.com (Garden Greens), kushilabs.com, day1distro.com, cannabistcompany.com, stashhousedistro.com, saylessus.com, gse420.com, greenlightningcannabis.com, sussexcultivation.com, holidayze.biz.

All 91 threads now carry the `Vendor Menus` Gmail label — search `label:"Vendor Menus"` in Gmail to review the full set. None of these sender domains are on the NEVER-TOUCH allowlist, so their >12-month-old marketing becomes trash-eligible under PART B on a future run once it ages out.

## PART B — Full trash audit (136 threads — ID · subject · sender · date)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 198241b7aeb776c4 | Hello there... Come and take a look at our DEALS | BestBuy@email.bestbuy.com | 2025-07-19 |
| 1954867db2d9d40e | Events this month: | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-02-27 |
| 194fc05177950760 | NJCBA Members Get a Discount at MJ Unpacked | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-02-12 |
| 194fb277ad9f7bbb | Ending soon: Get 2 months FREE after rebate | marketing@leaflink.com | 2025-02-12 |
| 194fad904ab5a5a0 | All Profit-Passive Income From The #1 Cannabis ATM Provider | kenneth.komarek@brinksinc.com | 2025-02-12 |
| 194fac666f33ed5b | [Free Trial Inside] Get free shipping & big perks | flyers@webstaurantstore.com | 2025-02-12 |
| 194fa4cac1fddc8d | (7/9) Get videos to the final version faster | no-reply@em-s.dropbox.com | 2025-02-12 |
| 194fa0a1fc918312 | The Presidents' Day Sale... | BestBuy@email.bestbuy.com | 2025-02-12 |
| 194f64808c8b0183 | The Secret Formula...? | brittanie@thrivepop.com | 2025-02-11 |
| 194f5c5a721853d4 | Your January 2025 Pro Xtra Statement is Here | homedepotpro@mg.homedepot.com | 2025-02-11 |
| 194f5c58a747c58a | 2/17 is coming quickly... | email@em.sherwin-williams.com | 2025-02-11 |
| 194f58ea437f286d | What's new in Canva this February? | marketing@engage.canva.com | 2025-02-11 |
| 194f56ae16a28b7f | Final Reminder: Benefits Compliance Webinar... | matthewmatey@worldinsurance.com | 2025-02-11 |
| 194f51adc5487c9d | (6/9) Edit your photos and videos... | no-reply@em-s.dropbox.com | 2025-02-11 |
| 194f1a4d121dffaa | NLS Updated Inventory, Special Pricing... | dan@northlake.supply | 2025-02-10 |
| 194f18d1d80c21f3 | Good news - catch the Presidents' Day SALE... | BestBuy@email.bestbuy.com | 2025-02-10 |
| 194f152dcafeb89d | 420 planning season kick-off | hello@flowhub.com | 2025-02-10 |
| 194f0b37b3d358eb | Upcoming Event This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-02-10 |
| 194f06badc83986e | Passive Income Secret In Cannabis | kenneth.komarek@brinksinc.com | 2025-02-10 |
| 194eff2a5934e856 | (5/9) Search everything all at once | no-reply@em-s.dropbox.com | 2025-02-10 |
| 194ebb0719a5e4f4 | A Tale As Old As Websites | noreply@mail.squarespace.com | 2025-02-09 |
| 194eaff2d4bc4f2f | (4/9) Install the desktop app | no-reply@em-s.dropbox.com | 2025-02-09 |
| 194e6fc930e9bf27 | WOW! Check out big-screen TVs | BestBuy@email.bestbuy.com | 2025-02-08 |
| 194e5ab9b8cca453 | (3/9) Edit PDFs right in Dropbox | no-reply@em-s.dropbox.com | 2025-02-08 |
| 194e1d1105e08d08 | Retail Insider: February 2025 Edition | marketing@leaflink.com | 2025-02-07 |
| 194e1bca5bb99aa7 | Now available: New Samsung Galaxy S25 Series | BestBuy@email.bestbuy.com | 2025-02-07 |
| 194e1aac54790d94 | One Wrong Number, Best Mistake Ever... | dayna@covasoftware.com | 2025-02-07 |
| 194e0ee77f6c7062 | Ensure you get the benefits of Dropbox | no-reply@em-s.dropbox.com | 2025-02-07 |
| 194e0cdc556561d3 | Upcoming Event This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-02-07 |
| 194e0a671945e022 | (2/9) Sharing is caring | no-reply@em-s.dropbox.com | 2025-02-07 |
| 194dca9a496afa84 | New AI trends emerging among software engineers | email@mail.salesforce.com | 2025-02-06 |
| 194dc3a786abe958 | Your guide to better cannabis finance | marketing@leaflink.com | 2025-02-06 |
| 194dc15390bf22a2 | Payroll For CUZZIE'S LLC | peter@heartlandpayments.ccsend.com | 2025-02-06 |
| 194dbc699e770416 | What's fueling this family dispensary's growth? | hello@flowhub.com | 2025-02-06 |
| 194d746bfc87afa5 | The 420 State Fair is back! | info@farechild.com | 2025-02-05 |
| 194d73c835c6f0e2 | Reminder: You have a $500 Google Ads credit offer | googleworkspace-noreply@google.com | 2025-02-05 |
| 194d72767bfbfa33 | AI Won't Replace You. But the Brand Using It Will. | innovate@spokesdigitalus.com | 2025-02-05 |
| 194d6e93e254a72d | I didn't know FASTSIGNS did that! | 2115@fastsigns.com | 2025-02-05 |
| 194d6e04718f0ab5 | What's New in Supernormal: January 2025 | danelle@supernormal.com | 2025-02-05 |
| 194d6a4ad9f5b9dd | Join these award winners at Canva Create | canvacreate@engage.canva.com | 2025-02-05 |
| 194d66e7fd223dfe | NEW Grassroots Strain Coming Soon - Pineapple Donut | marketing@leaftrade.com | 2025-02-05 |
| 194d294daa008534 | Now Playing: Budtender of the Hour... | dayna@covasoftware.com | 2025-02-04 |
| 194d256972196424 | Turnkey ATMs In New Jersey | Kenneth.Komarek@brinksinc.com | 2025-02-04 |
| 194d210de3641eb2 | Prime NJ Retail Locations... | Julian@cd.cdre.co | 2025-02-04 |
| 194d16254a1b00ce | NEW Ozone PIXI Disposable Vapes Are Now Available! | marketing@leaftrade.com | 2025-02-04 |
| 194d0aa193645ca7 | We're counting down to the end of these savings | email@em.sherwin-williams.com | 2025-02-04 |
| 194cc6f5af8eeab6 | have you shared your year in connection yet? | account@dot.cards | 2025-02-03 |
| 194cc5e778dbddaa | Your fresh February deals of 2025! | flyers@webstaurantstore.com | 2025-02-03 |
| 194cc1e92d935a45 | We're glad you're here. | BestBuy@email.bestbuy.com | 2025-02-03 |
| 194bce70a04f379f | Pennsylvania Cannabis Convention 2025... | marc@necann.com | 2025-01-31 |
| 194bca7851502114 | Get Featured + Earn $250 for Sharing Your Story | noreply@aiq.com | 2025-01-31 |
| 194b89cc3dda01a4 | How to be a meeting hero... | email@mail.salesforce.com | 2025-01-30 |
| 194b84c43a45799b | Why Dispensaries are Switching to Treez... | marketing@treez.io | 2025-01-30 |
| 194b7bf4e03efe6f | Print Disney's Mickey & Friends... | marketing@engage.canva.com | 2025-01-30 |
| 194b3dfb42c36b8b | Create product listings in seconds | hello@flowhub.com | 2025-01-29 |
| 194b37d6aaa08ea8 | NJCBA Members Get a Discount at MJ Unpacked | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-29 |
| 194b357d09b4c5b1 | New Grassroots Strain Coming Soon - Cheddar Cheeze | marketing@leaftrade.com | 2025-01-29 |
| 194b3544dae26402 | SCREEN REPAIR SPECIAL | salexander-vhrrental.com@shared1.ccsend.com | 2025-01-29 |
| 194b26ac37d9dfc8 | Emerald Intel Newsletter... | john@emeraldintel.ai | 2025-01-29 |
| 194af4a53d4fa40d | Have you been denied banking services for cannabis? | hello@flowhub.com | 2025-01-28 |
| 194ae8510f6ffdba | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-28 |
| 194ae4cc136440ac | Reminder: Register for tomorrow's webinar... | team@leaflink.com | 2025-01-28 |
| 194ae2ccbf6a6f07 | Get Ahead of 2025 Compliance Changes | matthewmatey@worldinsurance.com | 2025-01-28 |
| 194addc2205eca81 | Adobe would like your input... | mail@mail.adobe.com | 2025-01-28 |
| 194ada636f50db16 | Enjoy these offers... | email@em.sherwin-williams.com | 2025-01-28 |
| 194a959a49c142fa | The Secret Step For 2025 In Retail Cannabis | kenneth.komarek@brinksinc.com | 2025-01-27 |
| 194a87c829ab4a53 | Webinar Rescheduled... | hello@surfside.io | 2025-01-27 |
| 194a85074a826ddd | Hamilton Farm's updated menu | sales@hamiltonfarms.com | 2025-01-27 |
| 194a8485557050d2 | Get 20% off Valentine's materials... | marketing@engage.canva.com | 2025-01-27 |
| 194a80e6fa249667 | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-27 |
| 194a500bcd3dc90e | Apple Pay is ready to use. | applepay@insideapple.apple.com | 2025-01-26 |
| 194990d7b7528926 | Webinar: Retailer Academy Unit 3 - Negotiating | team@leaflink.com | 2025-01-24 |
| 19498badf77e1370 | You're missing out on premium Fiverr Pro... | no-reply@announce.fiverr.com | 2025-01-24 |
| 19498aae5dab01f7 | The easiest way to create videos... | marketing@engage.canva.com | 2025-01-24 |
| 194989f9f24c031d | Discover what's new at AIQ | noreply@aiq.com | 2025-01-24 |
| 194950b411f0b11a | Hit the High January Buzzer Beater | info@fernway.com | 2025-01-23 |
| 1949495424a3721e | Last chance to watch your dot.Rewind | account@dot.cards | 2025-01-23 |
| 19493e98cdc7fba6 | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-23 |
| 19493de2e4661114 | Credit Card Processing for Tough Leaf Members | peter@heartlandpayments.ccsend.com | 2025-01-23 |
| 19493c1017be53a6 | NEW in the PPC Winter Issue... | email@em.sherwin-williams.com | 2025-01-23 |
| 19493b45690fa963 | New Grassroots Strain Drop Coming Soon - Lemon Fresh! | marketing@leaftrade.com | 2025-01-23 |
| 194938d7167c25a3 | Local Content Insights x Vineyard Offshore... | local@localcontent.com | 2025-01-23 |
| 19492eebab9caa3b | Unlock Microsoft offers and updates! | Microsoft@engage.microsoft.com | 2025-01-23 |
| 1948f6e74b68ea1b | Your AI in Slack playbook... | email@mail.salesforce.com | 2025-01-22 |
| 1948f63cb7a2b4a1 | Good news: You've helped us make a positive impact | marketing@engage.canva.com | 2025-01-22 |
| 1948f04b2bd036c9 | Navigate the Future with Interactive Wayfinding | 2115@fastsigns.com | 2025-01-22 |
| 1948f027be9005de | Grow your business with Google Ads | googleworkspace-noreply@google.com | 2025-01-22 |
| 1948a0d9bf9068b8 | Last chance to share your feedback! | cx@trustmineral.com | 2025-01-21 |
| 1948a09a4231b893 | Passive Income Solution For Retail Cannabis | kenneth.komarek@brinksinc.com | 2025-01-21 |
| 1948a0893380609f | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-21 |
| 19489eb071039921 | CCDC Inaugural Dinner Fundraiser on 1/28 | jessica@rpconsultingllc.ccsend.com | 2025-01-21 |
| 194897ca0780364d | 2024 was a huge year for you... | account@dot.cards | 2025-01-21 |
| 194894ebfcc8bb8c | Last Chance: Register for Tomorrow's Webinar... | hello@surfside.io | 2025-01-21 |
| 19489443d80a833d | New Savvy 100mg Macro Dose Gummies... | marketing@leaftrade.com | 2025-01-21 |
| 19488921f9f3e85c | $50 Off $300 or $100 Off $400! | email@em.sherwin-williams.com | 2025-01-21 |
| 19484d42d7b47f1d | Hamilton Farms Menu Update! | sales@hamiltonfarms.com | 2025-01-20 |
| 1947eb3e4334f8d9 | Start your free 3-month trial. | applefitnessplus@insideapple.apple.com | 2025-01-19 |
| 1947aebb8fa60bf6 | I just shot a video for you! | Dawid@driveeasyauto.com | 2025-01-18 |
| 19476c1ced9b7eac | You just got 3 free months of Apple Arcade | applearcade@insideapple.apple.com | 2025-01-18 |
| 1947550a1b5579bf | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-17 |
| 1947142410d4eb36 | High January: More Chances to Win Every Week! | info@fernway.com | 2025-01-16 |
| 1947071ae3ae8685 | How to Navigate a Competitive Market... | hello@surfside.io | 2025-01-16 |
| 19470489f29bdb52 | Next Week: Grow Your Customer Base with AIQ's... | noreply@aiq.com | 2025-01-16 |
| 1946fb35a04d1ddd | Cannabis decision makers, one click away | marketing@emeraldintel.ai | 2025-01-16 |
| 1946f7049bb2c038 | Welcome to Wreck Wise! | info@wreckwise.com | 2025-01-16 |
| 1946b705cf40ef57 | 36% higher sales win rates... | email@mail.salesforce.com | 2025-01-15 |
| 1946b43ea0e244b9 | Coming Soon in 2025: Releases & Updates... | hello@surfside.io | 2025-01-15 |
| 1946b37a5f244f1a | Take Your Dispensary Payments to the Next Level | marketing@treez.io | 2025-01-15 |
| 1946b1200b840e27 | Retail/Office Building For Lease | jen@naidb.ccsend.com | 2025-01-15 |
| 1946aee6559cdcda | We Want Your Thoughts: Share Your Voice! | mail@mail.adobe.com | 2025-01-15 |
| 1946a76835efe934 | Your 2025 Cannabis Calendar Awaits | brittanie@thrivepop.com | 2025-01-15 |
| 1946a418b044c192 | Rip Into Relaxation With Effin' Chillin' Gummies! | marketing@leaftrade.com | 2025-01-15 |
| 1946a3ad5248b3d5 | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-15 |
| 19469f1d12fd463d | Reminder: Keeping your Business Secure | emanuel@alphasecurity.ccsend.com | 2025-01-15 |
| 19466009b812058a | there's still time to share your feedback | cx@trustmineral.com | 2025-01-14 |
| 1946592585012fbc | ProBuy Deals Are Here! | email@em.sherwin-williams.com | 2025-01-14 |
| 194658b43368ecc3 | Why our customers love dot.Profile+ | account@dot.cards | 2025-01-14 |
| 194650a5d0c51d9e | Snow Time? | salexander-vhrrental.com@shared1.ccsend.com | 2025-01-14 |
| 194650313791d448 | CCDC Inaugural Dinner Fundraiser on 1/28 | jessica@rpconsultingllc.ccsend.com | 2025-01-14 |
| 19461128d2147b8a | 15% Off North Lake Supply Wholesale | dan@northlake.supply | 2025-01-13 |
| 19460729a5a8eb66 | Hamilton Farms updated menu | sales@hamiltonfarms.com | 2025-01-13 |
| 19460206e7410a1c | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-13 |
| 1945d1a968f87827 | Keeping your Business Secure | emanuel@alphasecurity.ccsend.com | 2025-01-13 |
| 19451b79d8e405b5 | Happy New Year from LeafLink | marketing@leaflink.com | 2025-01-10 |
| 19450b0837af5bd1 | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-10 |
| 1945023d7d402d7d | Our Latest Work | emanuel@alphasecurity.ccsend.com | 2025-01-10 |
| 1944d16ed4a35ed1 | High January: Aim High, Win Big. | info@fernway.com | 2025-01-09 |
| 1944c3c4c35aff97 | We'd Love Your Feedback... | cx@trustmineral.com | 2025-01-09 |
| 1944c1afaeced684 | The Future of Cannabis Sales Is Here... | innovate@spokesdigitalus.com | 2025-01-09 |
| 1944bd04456647d9 | Your December 2024 Pro Xtra Statement is Here | homedepotpro@mg.homedepot.com | 2025-01-09 |
| 1944aefc94520756 | Who Will You Connect With in 2025? | account@dot.cards | 2025-01-09 |
| 1944707d7e891849 | Reach new customers with $500 in Google Ads credit | googleworkspace-noreply@google.com | 2025-01-08 |
| 19446cb91675cb58 | Unlock the Future with Digital Signage Solutions | 2115@fastsigns.com | 2025-01-08 |
| 19446c612f9aeffa | Take these new collaboration tools for a spin | mail@email.adobe.com | 2025-01-08 |
| 194466e399c62d5a | Act fast to get 30% off dot.Profile+... | account@dot.cards | 2025-01-08 |
| 194461bf0442eb5e | CCDC Inaugural Dinner Fundraiser on 1/28 | jessica@rpconsultingllc.ccsend.com | 2025-01-08 |

## Recovery
All 136 trashed threads are recoverable from Gmail Trash for 30 days from tonight (2026-07-20), i.e. until roughly 2026-08-19. To restore any of them, search the thread ID in Gmail Trash and move it back to Inbox.

## Sources
- gmail: PART A search `in:inbox (subject:menu OR subject:availability OR subject:"live menu" OR subject:"price sheet" OR subject:drop OR subject:"in stock") has:attachment` + vendor-domain seed list — 91 threads archived to `Vendor Menus`
- gmail: PART B search `in:inbox older_than:1y (category:promotions OR category:social OR category:forums) -is:starred -is:important` — 136 threads trashed after per-thread allowlist/important checks
