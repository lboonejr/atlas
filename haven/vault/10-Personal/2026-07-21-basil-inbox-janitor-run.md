---
created: 2026-07-21T23:15-04:00
updated: 2026-07-21T14:15-04:00
domain: personal
type: log
status: done
tags: [basil, inbox-janitor, gmail, automation, run-log]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-21 (live)

First **live** run (`DRY_RUN` flipped to `false` on `main`) — previous runs were dry-run previews. Gmail account acted on: `lemar@cuzziesnj.com`.

## Summary

- **Part A — vendor menus:** Archived **51** vendor-menu threads out of the inbox (labeled `Vendor Menus` / `Label_8`, `INBOX` removed — still readable in All Mail). Sourced from the anchors vendor-domain seed list plus several additional clearly-vendor senders whose subject/body confirmed real wholesale cannabis menus with attachments: stashhousedistro.com, ianthus.com/MPX, mojobotanica.com, saylessus.com, hamiltonfarms.com, ggcann.com, greenlightningcannabis.com, canopy-usa.com, hillviewmed.com, cannabistcompany.com, kushilabs.com, brutesroots.com, eatgron.com. Skipped threads that were really active correspondence rather than marketing blasts (e.g. a GSE payment-terms negotiation thread, an internal forward from a business partner at The Station).
- **Part B — trash sweep:** query `older_than:1y (category:promotions OR category:social OR category:forums)`. Scanned 250 threads across 5 search pages (resultCountEstimate ~201, some overlap). Only **131** cleared the never-trash gate (not starred, not important, no genuine filing label, sender domain not on the NEVER-TOUCH allowlist) — trashed those 131 (recoverable in Gmail Trash for 30 days). The remaining ~119 were skipped, overwhelmingly because Gmail auto-applied the `IMPORTANT` label — even to obvious cannabis-vendor marketing blasts and generic promo mail — or because the sender domain is on the allowlist (`parkebank.com`, `intuit.com`, `stellaconnect.net`/Metrc, `*.sos.nj.gov` all showed up repeatedly).
  - **Flag for Lemar:** Gmail's `IMPORTANT` auto-classifier is extremely aggressive on this account. It is currently blocking the large majority of otherwise-disposable old promo mail from ever being cleaned up by this routine. Worth reviewing Gmail's importance markers/filters if a lighter inbox is the goal — PART B is working as designed but starved of eligible candidates.
- **category:updates (report-only, never auto-trashed):** ~201 estimate, dominated by `notifications@adtcontrol.com`, `softtouchpos.co`, `headset.io`, `no-reply@accounts.google.com`, `noreply@jotform.com`, `noreply@redditmail.com`, `voice-noreply@google.com`, `ads-noreply@google.com`. Consistent with the runbook's expectation that this category mixes real operational notices with disposable ones — left untouched. Available for Lemar to clear by hand if he wants it lighter.
- **Vendor-menu backlog:** the Part A search returned a much larger set (~200 estimate) than the 51 processed tonight — more vendor-menu marketing remains in the inbox for future nightly runs to keep working through.

## Trash audit (thread ID · subject · sender · date) — recoverable in Gmail Trash for 30 days

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 19829a24f82df2c3 | Brief survey on your ADT alarm monitoring experience | adt@express.sea1.medallia.com | 2025-07-20 |
| 1944230a9b374e31 | Stronger tech partnerships = better leads | email@mail.salesforce.com | 2025-01-07 |
| 19441ecd2d5fa657 | Introduction to TIMELESS - LETS GET TO WORK! | nick.lamorgese@timelessrefinery.com | 2025-01-07 |
| 19441bfcefea5fc3 | 3 Biggest Problems with Dispensary ATMs | kenneth.komarek@brinksinc.com | 2025-01-07 |
| 1944165b2a8abe69 | [Office Hours] ngrok CEO Q&A | team@m.ngrok.com | 2025-01-07 |
| 194415f7eb6a5795 | Don't Miss Exclusive PRO+ Text Alerts Offers | email@em.sherwin-williams.com | 2025-01-07 |
| 1944153a0ef7d6ea | Upcoming Events This Month | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-07 |
| 19441196449f4f8f | Last chance discounted Canva Create 2025 tickets | canvacreate@engage.canva.com | 2025-01-07 |
| 1943dab1116f7d89 | Keeping your Business Secure | emanuel@alphasecurity.ccsend.com | 2025-01-06 |
| 1943d6b0041264a4 | Back at Work? dot.Profile+ | account@dot.cards | 2025-01-06 |
| 1943d1721a1e1566 | Maximize Creative Cloud benefits 2025 | mail@email.adobe.com | 2025-01-06 |
| 1943cc7b67a382fb | 2025 Cannabis Stats & Predictions | hello@flowhub.com | 2025-01-06 |
| 1943c330e8677306 | Hamilton Farms Menu & New Strain! | sales@hamiltonfarms.com | 2025-01-06 |
| 1943bcf2175bf488 | The best to-do list apps | blog@send.zapier.com | 2025-01-06 |
| 1943bb96428ecb37 | MSN Daily Jan 6 2025 | microsoft.start@email2.microsoft.com | 2025-01-06 |
| 194338d57339a4ea | Confirm your email address (Best Buy) | BestBuy@email.bestbuy.com | 2025-01-04 |
| 1942e66f680ee312 | Confirm your email address (Best Buy) | BestBuy@email.bestbuy.com | 2025-01-03 |
| 1942c0b2c321cd36 | Our Latest Work | emanuel@alphasecurity.ccsend.com | 2025-01-03 |
| 194294095ee12c90 | Confirm your email address (Best Buy) | BestBuy@email.bestbuy.com | 2025-01-02 |
| 194293e7532f482c | Fernway High January Has Officially Begun | info@fernway.com | 2025-01-02 |
| 194281041d1d00f2 | Virtual GMP Training | jenna@newjerseycannabusinessassociation.ccsend.com | 2025-01-02 |
| 19427f8bb6f6dfdc | Can't-miss inspiration to start your year | mail@email.adobe.com | 2025-01-02 |
| 194276d404f0cc40 | CCDC Inaugural Dinner Fundraiser | jessica@rpconsultingllc.ccsend.com | 2025-01-02 |
| 194241a2572bf78f | Confirm your email address (Best Buy) | BestBuy@email.bestbuy.com | 2025-01-01 |
| 194226ab09fb59ff | We couldn't join your meeting (Supernormal) | noreply@supernormal.com | 2025-01-01 |
| 1942191016e380d4 | $20 off $100 (Sherwin-Williams) | email@em.sherwin-williams.com | 2025-01-01 |
| 1941cd40465cd936 | MSN Daily Dec 31 2024 | microsoft.start@email2.microsoft.com | 2024-12-31 |
| 1941c9873b5f05b5 | Happy New Year (Alpha Locksmith) | emanuel@alphasecurity.ccsend.com | 2024-12-31 |
| 19418792521ef41c | Hamilton Farms Menu & New Strains | sales@hamiltonfarms.com | 2024-12-30 |
| 19417c28891b4235 | The best free AI tools in 2025 | blog@send.zapier.com | 2024-12-30 |
| 19417727fa992935 | Happy Chanukkah (Alpha Locksmith) | emanuel@alphasecurity.ccsend.com | 2024-12-30 |
| 19414a749fb48548 | Confirm your email address (Best Buy) | BestBuy@email.bestbuy.com | 2024-12-29 |
| 19412baaf7924802 | Welcome, just one more thing (Best Buy) | BestBuy@email.bestbuy.com | 2024-12-29 |
| 194083e0ea733092 | MSN Daily Dec 27 2024 | microsoft.start@email2.microsoft.com | 2024-12-27 |
| 194083de30f869ac | Happy Holidays (VHR Rental) | salexander-vhrrental.com@shared1.ccsend.com | 2024-12-27 |
| 19404d9a3feb5d13 | High January Is Almost Here (Fernway) | info@fernway.com | 2024-12-26 |
| 19404243b20e4f92 | Paint Rewards Bronze Status (Home Depot) | homedepotpro@mg.homedepot.com | 2024-12-26 |
| 193fdcc13dba64fd | Reminder: Keep Your Home Safe (Alpha Locksmith) | emanuel@alphasecurity.ccsend.com | 2024-12-25 |
| 193fdb0a48bd4c50 | Happy Chanukkah (Alpha Locksmith) | emanuel@alphasecurity.ccsend.com | 2024-12-25 |
| 193f9b46e6d02b94 | Hamilton Farms Menu & Happy holidays! | sales@hamiltonfarms.com | 2024-12-24 |
| 193f88e9c5ccabcc | Merry Christmas (Alpha Locksmith) | emanuel@alphasecurity.ccsend.com | 2024-12-24 |
| 193f4e19ff3dd6fb | Free Photoshop templates | mail@email.adobe.com | 2024-12-23 |
| 193f4be05930cf9d | Pre-Order Rosin Prerolls (North Lake Supply) | dan@northlake.supply | 2024-12-23 |
| 193f3884ad90b985 | Keep Your Home Safe (Alpha Locksmith) | emanuel@alphasecurity.ccsend.com | 2024-12-23 |
| 193e3fe7a031349a | Holiday Discounts (Alpha Locksmith) | emanuel@alphasecurity.ccsend.com | 2024-12-20 |
| 193e2a2490ad1102 | Crush your New Year creativity goals (Adobe) | mail@email.adobe.com | 2024-12-20 |
| 193e155522621b4a | Unwrap joy & innovation with Microsoft | Microsoft@engage.microsoft.com | 2024-12-19 |
| 193e10eda90fb484 | Get Ready for High January (Fernway) | info@fernway.com | 2024-12-19 |
| 193e0edb4a2c91cd | Get your startup off to best start 2025 (Slidebean) | caya@slidebean.com | 2024-12-19 |
| 193dfc87875031ab | Earn Up to $1,000 AIQ Referrals | noreply@aiq.com | 2024-12-19 |
| 193dfaad925f020a | Happy Holidays from Emerald Intel | john@emeraldintel.ai | 2024-12-19 |
| 193dc636b516467b | Microsoft Defender holiday protection | Microsoft365@engagement.microsoft.com | 2024-12-19 |
| 193dae5d5cba4513 | LeafLink List 2024 | marketing@leaflink.com | 2024-12-18 |
| 193da87da85e93eb | 2024 Color of the Year (Fastsigns) | 2115@fastsigns.com | 2024-12-18 |
| 193da7fc7c5fb335 | Season's Greetings (AYR Wellness) | caleb.barcus@ayrwellness.com | 2024-12-18 |
| 193da6449894f886 | Happy Holidays 2024 Content Unwrapped (Flowhub) | hello@flowhub.com | 2024-12-18 |
| 193da4e24efcad12 | The ONE thing before 2024 ends (Zapier) | learn@send.zapier.com | 2024-12-18 |
| 193da1e2eec696d5 | New Essence J's 7 Pack (Leaf Trade) | marketing@leaftrade.com | 2024-12-18 |
| 193da04257cebe79 | Registration Closed (NJCBA) | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-12-18 |
| 193d9bfc8c3bfba0 | Reminder: Keeping your Business Secure (Alpha) | emanuel@alphasecurity.ccsend.com | 2024-12-18 |
| 193d699442384666 | Vehicle worth trade-in (Easy Auto) | easyautopa@alstspecials.com | 2024-12-17 |
| 193d5d7cbd6a0f97 | Agentforce 2.0 launch (Salesforce) | email@mail.salesforce.com | 2024-12-17 |
| 193d5a73df143208 | Hamilton Farm menu & brand release | sales@hamiltonfarms.com | 2024-12-17 |
| 193d5698654d3a67 | TreezPay Lite free hardware | marketing@treez.io | 2024-12-17 |
| 193d533d2c75afdc | Season's Greetings (KOTODO) | news@kotodocan.com | 2024-12-17 |
| 193d5277ebb14a43 | Order Grassroots Premium Flower (Leaf Trade) | marketing@leaftrade.com | 2024-12-17 |
| 193d50844643bc77 | Only 1 Day Left (NJCBA) | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-12-17 |
| 193d1d4577a02c9d | Sesh Together Merch Drop (Fernway) | info@fernway.com | 2024-12-16 |
| 193d0e35c1a76c76 | Key benefits of Slack (Salesforce) | email@mail.salesforce.com | 2024-12-16 |
| 193d0c18f6a93a6f | Holiday Deals (North Lake Supply) | dan@northlake.supply | 2024-12-16 |
| 193d03a3394e9e09 | Five Days of Deals (Sherwin-Williams) | email@em.sherwin-williams.com | 2024-12-16 |
| 193d03821fc1fdfa | AIQ Ecommerce updates | noreply@aiq.com | 2024-12-16 |
| 193d01814946abaf | 2025 NECANN Cup | marc@necann.com | 2024-12-16 |
| 193cfe453e819311 | 2025 Design Trend (Canva) | marketing@engage.canva.com | 2024-12-16 |
| 193cfa9f4d2f30a7 | Send emails from spreadsheet (Zapier) | blog@send.zapier.com | 2024-12-16 |
| 193cf6e020ce9b9b | Keeping your Business Secure (Alpha) | emanuel@alphasecurity.ccsend.com | 2024-12-16 |
| 193c7e2138eb826c | Your year in Canva | marketing@engage.canva.com | 2024-12-15 |
| 193c277f7bca5cf6 | Share your thoughts chance to win $500 (Adobe) | mail@mail.adobe.com | 2024-12-14 |
| 193c1479e9b2827e | TreezPay Lite free hardware | marketing@treez.io | 2024-12-13 |
| 193c0a8e3c1286da | Agentforce 2.0 launch reminder (Salesforce) | email@mail.salesforce.com | 2024-12-13 |
| 193c06ebd25fb5f8 | You don't want to miss out (NJCBA) | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-12-13 |
| 193bfc8bd91de9ea | Ready to upgrade building security (Alpha) | emanuel@alphasecurity.ccsend.com | 2024-12-13 |
| 193bdcee19bb5461 | Holiday savings Microsoft Copilot | Copilot@engage.microsoft.com | 2024-12-13 |
| 193bbff52f495de3 | Last Chance Payroll switch (Heartland) | peter.romero-heartland.us@shared1.ccsend.com | 2024-12-12 |
| 193bbedfc0422a99 | New Photoshop features (Adobe) | mail@email.adobe.com | 2024-12-12 |
| 193bb2f1f2c4beaf | Register PAX webinar (Surfside) | hello@surfside.io | 2024-12-12 |
| 193b7bca35136a77 | Fernway Chocolate Mint Has Arrived | info@fernway.com | 2024-12-11 |
| 193b70ee970c03de | STIIIZY switched POS (Flowhub) | hello@flowhub.com | 2024-12-11 |
| 193b6fd7c6757d37 | End of year got your head spinning (Zapier) | learn@send.zapier.com | 2024-12-11 |
| 193b6f719f24eca0 | Turnkey ATMs in NJ (Brinks) | Kenneth.Komarek@brinksinc.com | 2024-12-11 |
| 193b6bf2ac86b56c | LeafLink List 2024 award | marketing@leaflink.com | 2024-12-11 |
| 193b65d5eafe2f38 | Agentforce 2.0 first look (Salesforce) | email@mail.salesforce.com | 2024-12-11 |
| 193b63d8d1b44240 | What's new in Canva December | marketing@engage.canva.com | 2024-12-11 |
| 193b5b36dd25a866 | Reminder: Keeping your Business Secure (Alpha) | emanuel@alphasecurity.ccsend.com | 2024-12-11 |
| 193b155683ff4294 | Gallery Series Topcoat (Sherwin-Williams) | email@em.sherwin-williams.com | 2024-12-10 |
| 193b14c8864a019d | Best-In-Class Buds (Leaf Trade) | marketing@leaftrade.com | 2024-12-10 |
| 193b0e96d5b7297e | Create 2025 countdown (Canva) | canvacreate@engage.canva.com | 2024-12-10 |
| 193b0e6b1cb7b0e4 | PAX livestream invite (Surfside) | hello@surfside.io | 2024-12-10 |
| 193b0de29a1ff0bf | Double up on Juice (Leaf Trade) | marketing@leaftrade.com | 2024-12-10 |
| 193ae7b6b66540af | $1 Million Sweepstakes (Microsoft Rewards) | MicrosoftRewards@customermail.microsoft.com | 2024-12-10 |
| 193ac42a7eca3faa | Hamilton Farms Menu (Dark Krystal) | sales@hamiltonfarms.com | 2024-12-09 |
| 193ac28e9e1ec57f | You don't want to miss out (NJCBA) | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-12-09 |
| 193abfcad24d8f6c | Q4 Market Brief (Emerald Intel) | research@emeraldintel.ai | 2024-12-09 |
| 193aba5ddb8f17f3 | Weekly Menu Update (North Lake Supply) | dan@northlake.supply | 2024-12-09 |
| 193ab586ff95a4fb | Keeping your Business Secure (Alpha) | emanuel@alphasecurity.ccsend.com | 2024-12-09 |
| 193a692010eb0fb4 | ADT customer service survey reminder | adt@express.sea1.medallia.com | 2024-12-08 |
| 1939dc4cabeff038 | MJBizCon follow up (Emerald Intel) | john@emeraldintel.ai | 2024-12-06 |
| 1939d921192b2f53 | Ho! Ho! Ho! (Voorhees Hardware) | salexander-vhrrental.com@voorheeshardware.ccsend.com | 2024-12-06 |
| 1939d8e3ccb350c8 | Cova Retail Software of the Year | dayna@covasoftware.com | 2024-12-06 |
| 1939d76e9dbc7bca | Retail Insider December 2024 (LeafLink) | marketing@leaflink.com | 2024-12-06 |
| 1939cd81819ddadc | We couldn't join your meeting (Supernormal) | noreply@supernormal.com | 2024-12-06 |
| 1939cb69fcf92db1 | Pro Xtra Statement Nov 2024 (Home Depot) | homedepotpro@mg.homedepot.com | 2024-12-06 |
| 1939ca0f947027c4 | Meet Agentforce 2.0 (Salesforce) | email@mail.salesforce.com | 2024-12-06 |
| 1939c93734a46a05 | SBA 7(a) Verify Eligibility | main-palmestatesco.com@shared1.ccsend.com | 2024-12-06 |
| 1939c61692d5a83b | You don't want to miss out (NJCBA) | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-12-06 |
| 1939a68f968b1a69 | Ditch spreadsheets for Tables (Zapier) | learn@send.zapier.com | 2024-12-06 |
| 193990f8fc226f2a | Ready to Explore Your Options (Easy Auto) | Dawid@driveeasyauto.com | 2024-12-05 |
| 19397b63feda6c2f | Stop wasting time on Gmail replies (Zapier) | updates@send.zapier.com | 2024-12-05 |
| 1939348be59712a2 | AIQ Support Model Transformation | noreply@alpineiq.com | 2024-12-04 |
| 19393148828c3c82 | Strengthen workplace communication (Salesforce) | email@mail.salesforce.com | 2024-12-04 |
| 193930b4c05548b8 | A New Chapter (SevenPoint Interiors) | info@sevenpointinteriors.com | 2024-12-04 |
| 193928fd699d8ba6 | Operations portal guide (Zapier) | learn@send.zapier.com | 2024-12-04 |
| 193926db802391ee | Make Your Brand Shine Bright (Fastsigns) | 2115@fastsigns.com | 2024-12-04 |
| 193923387b4c9da7 | 15% off personalized gifts (Canva) | marketing@engage.canva.com | 2024-12-04 |
| 19391f70794de669 | ADT customer service survey | adt@express.sea1.medallia.com | 2024-12-04 |
| 1938e7bbec77ea44 | I just shot a video for you (Easy Auto) | Dawid@driveeasyauto.com | 2024-12-03 |
| 1938d3bad1c4657c | Small Business Programs Available (SBA/Palm Estates) | main-palmestatesco.com@shared1.ccsend.com | 2024-12-03 |
| 1938d33e44763c07 | Exclusive Shelf Space NJ Cannabis Brands | Julian@cd.cdre.co | 2024-12-03 |
| 1938d235b095b4df | Last Chance Ladder Event (Sherwin-Williams) | email@em.sherwin-williams.com | 2024-12-03 |
| 19389ba1ac2e57c9 | I just shot a video for you (Easy Auto) | Dawid@driveeasyauto.com | 2024-12-02 |
| 193895b3dc93e1d6 | Introduction to TIMELESS | nick.lamorgese@timelessrefinery.com | 2024-12-02 |

## Archived vendor-menu threads (Part A, 51 total)

Labeled `Vendor Menus` (`Label_8`), removed from `INBOX` — not trashed, still readable in All Mail. Senders included: Verano, Illicit Gardens, North Lake Supply, TerrAscend, Ascend/AW Holdings, Kiva, QCC NJ, Bud's Goods, Harvest Moon Farms, Ladds LLC, Stash House/Victory, MPX/Ianthus, Mojo Botanica, Say Less, Hamilton Farms, Garden Greens, Green Lightning, Canopy-USA/Botanist, Hillview, MGB/Ejay, Grön Edibles, Kushi Labs, Cannabist, Brute's Roots.

## Next actions for Lemar

1. Review the Gmail `IMPORTANT`-classifier issue noted above — it's suppressing most of PART B's intended cleanup on this account.
2. There's a large vendor-menu backlog beyond tonight's 51 — expect PART A to keep chipping at it on subsequent nightly runs.
3. `category:updates` has ~201 threads mixing real notices with disposable ones — worth a manual pass by Lemar if he wants that inbox truly light.

## Sources
- gmail: PART A search `in:inbox` (vendor-domain seed list + menu-signal keywords), 51 threads archived
- gmail: PART B search `older_than:1y (category:promotions OR category:social OR category:forums)`, 131 threads trashed
- gmail: PART B report-only search `older_than:1y category:updates`, counted only
