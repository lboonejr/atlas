---
created: 2026-07-17T23:07-04:00
updated: 2026-07-17T23:07-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-17

## Basil — Inbox Janitor nightly run — 2026-07-17 (LIVE, DRY_RUN=false)

Account acted on: lemar@cuzziesnj.com (Gmail). This appears to be the first live run — a large historical backlog had accumulated (vendor menus and old promo mail going back to March/April 2025), so this run processed a bounded batch and left the remainder queued for subsequent nightly runs rather than trying to clear everything in one pass.

### PART A — vendor menus archived (Vendor Menus label, Label_8)

149 threads matching (vendor domain from anchors seed list) AND (subject contains "menu") AND (has attachment) were labeled Vendor Menus and removed from Inbox. They remain in All Mail under the label — nothing was trashed in this part. Senders included: verano.com, terrascend.com, kivaconfections.com, qccnj.com, awholdings.com, harvestmoonfarmsnj.com, budsgoods.com, freshcannabis.co, prolificgrowhouse.com, parksgrove.com, arescanna.com, missgrass.com. Date range covered: 2026-03-02 through 2026-07-16 (newest-first pagination). More vendor-menu backlog older than this range likely remains and will be picked up on future nightly runs.

### PART B — trash sweep (old promotions/social/forums, >12mo)

Candidate query: `older_than:1y (category:promotions OR category:social OR category:forums)`. Reviewed 150 candidate threads (3 pages) from newest to oldest (2025-07-16 back to 2025-04-01). Applied the never-trash floor (is:starred, is:important, allowlist domain, *.gov, or any message in the thread carrying IMPORTANT) — 76 of the 150 were protected and skipped, mostly Gmail's own IMPORTANT flag plus explicit allowlist hits (parkebank.com, fundcanna.com — including the FundCanna underwriting thread specifically protected per anchors — stellaconnect.net/Metrc, intuit.com, and *.gov / sos.nj.gov CTA mail).

74 threads were trashed (recoverable in Gmail Trash for 30 days from tonight). Full audit list (thread ID · subject · sender · date):

- 19814738af82058d · Now on-demand: Is your workforce ready for AI agents? · email@mail.salesforce.com · 2025-07-16
- 198143a3007ca282 · Apply for flexible financing to move your business forward · noreply@mail.lendistry.com · 2025-07-16
- 198142de3cf8d6de · "Your A-Team is on PTO" · marketing@vangst.com · 2025-07-16
- 198141b9e29bdd19 · Guess who's coming to ZapConnect 2025 👀 · events@send.zapier.com · 2025-07-16
- 1981409d756890c8 · Our lineup just got bigger... · email@mail.salesforce.com · 2025-07-16
- 19813a5cf9b3d7c1 · Catch the Replay: Ecommerce Keynote & Live Demo · hello@flowhub.com · 2025-07-16
- 19663288a2370800 · Post 4/20 Restock: New Carts + Cool Whip Prerolls · andrew@northlake.supply · 2025-04-23
- 19662ccecdbbf9cb · Hamilton Farm's Weekly Menu! · sales@hamiltonfarms.com · 2025-04-23
- 1965eab00a250afd · Re: Hi, just a quick question about Displays2go · feedback@survey.displays2go.com · 2025-04-22
- 1965e3e6ad3390f6 · Join Mayor Vic Carstarphen & the Camden Strong Team · jessica@rpconsultingllc.ccsend.com · 2025-04-22
- 1965e09e7def2f84 · Purdy 100th Anniversary sale · email@em.sherwin-williams.com · 2025-04-22
- 1965d61126ca64e1 · Dont Miss Out: New Pre Rolls Available! · jamie-nichenfe.com@shared1.ccsend.com · 2025-04-22
- 19658d1494dde436 · Unlock Savings: Eighths Now Just $30! · jamie-nichenfe.com@shared1.ccsend.com · 2025-04-21
- 1964ff94770584ce · Spring SALE alert · BestBuy@email.bestbuy.com · 2025-04-19
- 19648e3be3db0438 · Speak at NECANN 2025 · marc@necann.com · 2025-04-18
- 19648d2f23ad260b · 4/20 Tips: Tip #5 · brittanie@thrivepop.com · 2025-04-18
- 19646fdb36be8664 · You could be one of the $10K weekly winners · MicrosoftRewards@customermail.microsoft.com · 2025-04-18
- 196458f328c045bf · Happy 420! See you out there! · info@fernway.com · 2025-04-17
- 196447fcc443a489 · Meet the only chatbot backed by 7000+ app integrations · updates@send.zapier.com · 2025-04-17
- 1963feb407e8f27d · 4/20 Tips: Tip #4 · brittanie@thrivepop.com · 2025-04-16
- 1963f5692954e96e · News & Resources for Small Businesses · noreply@mail.lendistry.com · 2025-04-16
- 1963f23da5654c9a · April Business Training Series · email@em.sherwin-williams.com · 2025-04-16
- 1963f204f125e4d1 · Elevate Your Rebranding Strategy · 2115@fastsigns.com · 2025-04-16
- 1963ef1dc11011a5 · What's new from Canva Create: Uncharted · marketing@engage.canva.com · 2025-04-16
- 1963edf42e5725af · Don't miss your free trial (Apple Fitness+) · applefitnessplus@insideapple.apple.com · 2025-04-16
- 1963b1534ce5bc93 · NJEDA's free eCommerce program · njedasupport@egrovesys.com · 2025-04-15
- 1963aa9e8a4e3d3a · Align quickly with customer goals (Salesforce/Slack) · email@mail.salesforce.com · 2025-04-15
- 1963a380727ac0a7 · Your design is almost ready for delivery (Canva) · marketing@engage.canva.com · 2025-04-15
- 19639fc3e42c74eb · SprayBuy Spring Savings · email@em.sherwin-williams.com · 2025-04-15
- 19639dd612d6b839 · Our 4/20 Deals Are LEGIT! · jamie-nichenfe.com@shared1.ccsend.com · 2025-04-15
- 19639b9f262eb5a1 · Early access closing soon (Canva Sheets) · marketing@engage.canva.com · 2025-04-15
- 19637d21e45a5b5f · Hi, just a quick question about Displays2go · feedback@survey.displays2go.com · 2025-04-15
- 196363b55ad9a0b1 · Now Live: North Lake Supply Distillate & Live Resin Carts · andrew@northlake.supply · 2025-04-14
- 196359819632c767 · US Virgin Islands Cannabis Cultivation Licensing Webinar · michelle-thinkcanna.com@cannaadvisors.ccsend.com · 2025-04-14
- 196355eb7db06c7a · Did your recent Amazon order meet your expectations? · donotreply@amazon.com · 2025-04-14
- 196355ab7b1a076e · Drive leads with TikTok (Zapier) · learn@send.zapier.com · 2025-04-14
- 1963549d0531ed26 · Better Credit Card Processing for CUZZIE'S LLC · peter@heartlandpayments.ccsend.com · 2025-04-14
- 196353ba1c20ce87 · Our 4/20 Deals Are LEGIT! · jamie-nichenfe.com@shared1.ccsend.com · 2025-04-14
- 196347c08868ab7f · 4/20 Tips: Tip #3 · brittanie@thrivepop.com · 2025-04-14
- 1962bf395d015ec3 · TVs as low as $69.99 (Best Buy) · BestBuy@email.bestbuy.com · 2025-04-12
- 1962a65de2745779 · Come Back & Save Up To 55% (flagsonthecheap) · newsletter@email.flagsonthecheap.com · 2025-04-12
- 19625b4aae982e2e · Did your recent Amazon order meet your expectations? · donotreply@amazon.com · 2025-04-11
- 196257538cb3b226 · KOTODO: Cherry Blossoms newsletter · news@kotodocan.com · 2025-04-11
- 196253a1f64549ae · Unpopular Opinion: Being Loud Isn't Impactful · brittanie@thrivepop.com · 2025-04-11
- 19625312fd6939ac · Our 4/20 Deals Are LEGIT! · jamie-nichenfe.com@shared1.ccsend.com · 2025-04-11
- 196215bbac741164 · Webinar: Scaling Marketing Compliance (Zapier) · events@send.zapier.com · 2025-04-10
- 196214086e1352f0 · You Just Donated $14,259 to Local Shelters (Fernway) · info@fernway.com · 2025-04-10
- 19620e7fbfc83fab · Rolling Stone confirms: Top talent flooding into cannabis (Vangst) · hello@vangst.com · 2025-04-10
- 1962054d1e180c60 · Lead the charge into agentic productivity (Salesforce) · email@mail.salesforce.com · 2025-04-10
- 1962000da082f230 · This isn't your average dispensary experience (Flowhub) · hello@flowhub.com · 2025-04-10
- 1961d3b4c64fb92d · Last chance: 3 free months Apple Arcade · applearcade@insideapple.apple.com · 2025-04-10
- 1961c5c1896ef95e · Strain menu updates! (Verano) · wholesale@verano.com · 2025-04-09
- 1961c1066e5e348e · Our 4/20 Deals Are LEGIT! · jamie-nichenfe.com@shared1.ccsend.com · 2025-04-09
- 1961bc03ab1b5644 · Why Salesforce runs on Slack · email@mail.salesforce.com · 2025-04-09
- 1961b73b68ad1484 · 4/20 Tips: How to Market Smart · brittanie@thrivepop.com · 2025-04-09
- 1961af95d3c00667 · DON'T JUST DRIVE BY (Voorhees Hardware) · salexander-vhrrental.com@voorheeshardware.ccsend.com · 2025-04-09
- 1961aa3aa42e0c91 · Have your medication delivered (Amazon Pharmacy) · hello@email.pharmacy.amazon.com · 2025-04-09
- 1961734dbaf92b1e · Cypress Hill Ticket Giveaway! (Verano) · maggie.boyd@verano.com · 2025-04-08
- 196162cca0b1d8c1 · Design and launch unique websites in minutes (Canva) · marketing@engage.canva.com · 2025-04-08
- 19615f38c8146cf9 · Buy One Titan Spray Tip Get One Free · email@em.sherwin-williams.com · 2025-04-08
- 19615f1488f5c449 · Your March 2025 Pro Xtra Statement (Home Depot) · homedepotpro@mg.homedepot.com · 2025-04-08
- 19615c660eb86d29 · Canva Create spots are filling up fast · canvacreate@engage.canva.com · 2025-04-08
- 1961133946e863a9 · Bryce Vine Headlining The 420 State Fair · info@farechild.com · 2025-04-07
- 1961108f37d6b8fc · Really good 420 advice (Flowhub) · hello@flowhub.com · 2025-04-07
- 19610cd12801b3b8 · Invest In Your Business (Heartland) · peter.romero-heartland.us@shared1.ccsend.com · 2025-04-07
- 19610b616554fa5c · IWA FutureReady / Local Content newsletter · local=localcontent.com@hubspotstarter.hs-send.com · 2025-04-07
- 196082fa052c6259 · Final reminder: Apple TV+ free 3 months · appletv@insideapple.apple.com · 2025-04-05
- 195fd51d93e73004 · Invite Friends, Earn A Bonus (Fernway) · info@fernway.com · 2025-04-03
- 195fc4a6fa07bd0b · Are you ready for a new era of agentic productivity (Salesforce) · email@mail.salesforce.com · 2025-04-03
- 195fbd5d80670199 · Stay Ahead: Webinar on Prescription Costs · matthewmatey@worldinsurance.com · 2025-04-03
- 195f84f65144a379 · DON'T JUST DRIVE BY (Voorhees Hardware) · salexander-vhrrental.com@voorheeshardware.ccsend.com · 2025-04-02
- 195f7a7bf6533519 · NJEDA's free eCommerce program · njedasupport@egrovesys.com · 2025-04-02
- 195f717d5a575170 · The Power of a Rebrand with Signage (FastSigns) · 2115@fastsigns.com · 2025-04-02
- 195f3434812ce756 · 4/20 is Coming - Are You Ready!? (Verano) · wholesale@verano.com · 2025-04-01

All 74 are pure marketing/newsletter/survey mail, >12 months old, none starred/important/allowlisted. Recoverable from Gmail Trash for 30 days from tonight.

### category:updates — report-only, not touched

`older_than:1y category:updates` estimates ~200+ threads. Confirmed mixed content exactly as anchors warned: QuickBooks/Intuit invoices and tax notices, Progressive commercial-auto billing, Headset.io scheduled reports, Jotform time-off approvals and sample-tracking forms, plus some genuine clutter (Reddit digest mail). Left entirely alone per the routine — flagging for Lemar to clear by hand if desired, sender domains worth a manual look: notification.intuit.com / noreply@intuit.com, headset.io, jotform.com / jotformsign.com, progressive.com.

### Backlog remaining for future nightly runs

Both PART A and PART B candidate pools were larger than what one run processed (bounded to keep the run finite and auditable). More vendor-menu threads older than 2026-03-02 and more promo/social/forum threads older than 2025-04-01 remain in scope and will be picked up on subsequent nights as Basil continues running.

## Sources
- gmail: lemar@cuzziesnj.com inbox sweep, 2026-07-17
