---
created: 2026-07-15T23:15-04:00
updated: 2026-07-15T08:53-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail, cleanup, vendor-menus, trash-sweep]
source: claude
---

# Inbox Janitor run — 2026-07-15 (first live run, DRY_RUN=false)

First live run of the Inbox Janitor (Basil) routine on `lemar@cuzziesnj.com`, after
`DRY_RUN` was flipped to `false` in `.claude/routines/inbox-janitor.md`. This cleared a
large backlog that had never been swept before (vendor menus and old promo mail going
back to mid-May 2026 / mid-2025 respectively).

## PART A — vendor menus archived (labeled "Vendor Menus", removed from INBOX; never trashed)

**244 threads archived**, 0 errors. Query: sender on the vendor-domain seed list AND
subject contains "menu", restricted to `in:inbox`. Covers wholesale menu blasts from:
qccnj.com, verano.com, terrascend.com, awholdings.com (Ascend), freshcannabis.co,
kivaconfections.com, illicitgardens.com, harvestmoonfarmsnj.com, apextrading.com
(multiple sub-brand senders), budsgoods.com, novafarms.com (Stashie), prolificgrowhouse.com,
parksgrove.com, laddsllc.com, missgrass.com, jerseysmooth.com, thegardensociety.com,
arescanna.com, 1906.shop, northlake.supply, gse420.com, stashhousedistro.com, ianthus.com
(MPX), cannabistcompany.com, and Mudd Brothers (brevosend.com). Date range archived:
2026-05-08 through 2026-07-14. Processed in 5 batches of ~50 (49+46+49+50+50=244), all
clean.

## PART B — trash sweep (old, clearly unnecessary mail only, >12mo, recoverable 30 days)

**130 threads trashed**, 0 errors. Query: `in:inbox older_than:1y (category:promotions OR
category:social OR category:forums)`, each candidate individually gated on NOT
starred/important, no genuine filing label, sender not on the NEVER-TOUCH allowlist.
Processed in 3 batches (44+42+44=130), all clean. Did not hit the 200/run cap.

**18 candidates were screened OUT and left alone** (the safety floor working as designed):
- 15 for `is:important`
- 1 for `is:starred` — `jamie-nichenfe.com@shared1.ccsend.com`, 2025-06-30, "New SKU's -
  Don't Miss Out!"
- 1 for `.gov` domain — `CTA@sos.nj.gov`, 2025-06-25, "CTA Level 6 Ask Me Anything"
- 1 for NEVER-TOUCH allowlist + important — `metrc@stellaconnect.net`, 2025-07-05,
  "Tell us how we're doing"

### Trash audit list (thread ID · date · sender · subject) — all recoverable from Gmail Trash for 30 days

```
1980ae6e1f951333 · 2025-07-14 · marketing@vangst.com · Croptober is just 7 weeks away
1980a63f38fde4f5 · 2025-07-14 · sales@hamiltonfarms.com · Hamilton Farms Weekly Menu
1980a3d0f2ebaef1 · 2025-07-14 · marketing@engage.canva.com · Don't miss our webinar with Meta
1980985bf85486bd · 2025-07-14 · andrew@northlake.supply · New Summer Menu: Price Drops + Watermelon Sorbet Vapes
1980968882b9e502 · 2025-07-14 · jamie-nichenfe.com@shared1.ccsend.com · Summer Drops: Lemon Cherry Gelato and Peelz!
198090a48afc1bf3 · 2025-07-14 · hello@flowhub.com · Ecommerce is now available for all dispensaries!
198089810b875208 · 2025-07-14 · jason@bridgecitycollective.com · PANDA FARMS New Strain Drops!!
197ffd1f10e950f5 · 2025-07-12 · BestBuy@email.bestbuy.com · Black Friday in July
197fa61a8a9cca53 · 2025-07-11 · Phil@sussex-cultivation.apextrading.com · ONYX Live Apex Menu 7.11.25
197f9f7f629e1013 · 2025-07-11 · marketing.us@terrascend.com · NEW Legendary 1G Pre-Rolls
197f626cdf43a580 · 2025-07-10 · info@fernway.com · Your Call to the Table
197f5411f91e0bf8 · 2025-07-10 · email@mail.salesforce.com · Bring your team, save $1,300/pass
197f4db5a1b88e99 · 2025-07-10 · homedepotpro@mg.homedepot.com · 25% Savings on Paint
197f4b58bd027027 · 2025-07-10 · flyers@webstaurantstore.com · Order up! Do more for less
197f4b109e29e872 · 2025-07-10 · info@alpharoot.com · Ready to scale? Make sure you're covered
197f4619d1f7afc3 · 2025-07-10 · matthewmatey@worldinsurance.com · Your Monthly Digest
197f066ac9c45479 · 2025-07-09 · email@mail.salesforce.com · Build lasting relationships with data/AI
197f01659e718eca · 2025-07-09 · events@send.zapier.com · ZapConnect 2025
197efc34700f3239 · 2025-07-09 · 2115@fastsigns.com · Custom Visuals FASTSIGNS
197ef2a4aac6d371 · 2025-07-09 · jamie-nichenfe.com@shared1.ccsend.com · Lemon Cherry Gelato is back
197ebf238973562b · 2025-07-08 · wholesale@verano.com · Classic Summer Strains
197eb7c5c0cfd5db · 2025-07-08 · marc@necann.com · 2025 NJ Cannabis Convention & NECANN Cup
197eac851f0bd244 · 2025-07-08 · hello@surfside.io · Livestream with Planet 13 VP Marketing
197eab68836c2ac8 · 2025-07-08 · brittanie@thrivepop.com · mommy... mamacita..?
197ea98fa3cf5ae3 · 2025-07-08 · homedepotpro@mg.homedepot.com · June 2025 Pro Xtra Statement
197e771220095753 · 2025-07-08 · Chris@little-leaf-labs.apextrading.com · Growfather NEW Releases
197e6e7e3688de23 · 2025-07-07 · wholesale@verano.com · J's galore!
197e633f5abb85bf · 2025-07-07 · marketing@engage.canva.com · Canva and Meta experts
197e6202544a99a6 · 2025-07-07 · marketing.us@terrascend.com · Stacked with Diamonds new pre-rolls
197e5bf16def1b8c · 2025-07-07 · payments@dutchie.com · Kiosk Payment Workflow feedback
197e5ba9eb3f7907 · 2025-07-07 · marketing@vangst.com · Hidden Cost of Summer Absenteeism
197e59d40667e266 · 2025-07-07 · jamie-nichenfe.com@shared1.ccsend.com · New SKU's - Don't Miss Out
197e57bb1e36f0d7 · 2025-07-07 · andrew@northlake.supply · Post-4th Restock
197e56cc6e452ada · 2025-07-07 · email@em.sherwin-williams.com · 7/7-7/14 offer
197e52a48321ae32 · 2025-07-07 · flyers@webstaurantstore.com · Bulk up on BIG savings
197e524eeec2cd45 · 2025-07-07 · marc@necann.com · Two shows. Endless opportunity
197e4f3123b78072 · 2025-07-07 · marketing@treez.io · Treez Innovation Showcase last call
197e19bbe86b071c · 2025-07-06 · adt@express.sea1.medallia.com · ADT visit survey reminder
197dc7a88214c4ea · 2025-07-05 · BestBuy@email.bestbuy.com · 4th of July deals
197d570aa9a563a0 · 2025-07-04 · Grainger@feedback.grainger.com · Grainger delivery survey
197d2c044fac3684 · 2025-07-04 · support@memberstack.com · Welcome to Memberstack
197d21ddea8e48de · 2025-07-03 · adt@express.sea1.medallia.com · ADT visit survey
197d1f5a4360b576 · 2025-07-03 · info@fernway.com · Season of Abundance
197d18dad8d102ba · 2025-07-03 · wholesale@verano.com · All the Stars!
197d12011ef96871 · 2025-07-03 · marketing@vangst.com · Staffing gaps
197d0e671f826258 · 2025-07-03 · jamie-nichenfe.com@shared1.ccsend.com · New SKU's
197d09fe9e9a776d · 2025-07-03 · info@alpharoot.com · Coverage cannabis companies rely on
197d09a1d3a79fcd · 2025-07-03 · marketing@engage.canva.com · Recommended templates
197ce8220cb41d96 · 2025-07-03 · noreply@www.learnbrands.com · New reward available
197cd27f89db702a · 2025-07-02 · wholesale@verano.com · New Product Alert
197cc58e8f39e3bf · 2025-07-02 · email@mail.salesforce.com · Slack enterprise search
197cbf9797383b0b · 2025-07-02 · marketing@vangst.com · Need workers you can count on
197cbeb2c7b72bd1 · 2025-07-02 · marketing@engage.canva.com · Make your social content shine
197cbc4a197a6b08 · 2025-07-02 · Phil@sussex-cultivation.apextrading.com · ONYX Apex Menu July 2
197cb635180ac90e · 2025-07-02 · marketing.us@terrascend.com · Kind Tree drop teaser
197cb05f7ea83419 · 2025-07-02 · marketing@treez.io · Treez rooftop celebration
197c903660ade268 · 2025-07-02 · noreply@redditmail.com · r/gardening digest
197c8028ed7af33b · 2025-07-01 · wholesale@verano.com · 7/10 deals
197c73337152b902 · 2025-07-01 · marketing@vangst.com · Employees calling in again?
197c6ab25dcb4413 · 2025-07-01 · andrew@northlake.supply · Happy 4th of July pre-orders
197c64062b3ad79c · 2025-07-01 · customerexperience@feedback.wm.com · Request for Assistance
197c6254c6001acc · 2025-07-01 · marketing.us@terrascend.com · Sell Thru Starts Here
197c5fafa5005eed · 2025-07-01 · Grainger@feedback.grainger.com · Delivery survey
197c5e814580d743 · 2025-07-01 · michelle-thinkcanna.com@cannaadvisors.ccsend.com · Cannabis Business Newsletter
197c21e9c2a4544d · 2025-06-30 · noreply@aiq.com · AIQ campaigns upgrade
197c198384246d22 · 2025-06-30 · Julian@cd.cdre.co · 2 NJ Cannabis Opportunities
197c0fd2ca09b159 · 2025-06-30 · marc@necann.com · Final Call: Two Opportunities
197b62308f4c6d7d · 2025-06-28 · BestBuy@email.bestbuy.com · TVs as low as $199.99
197b26a8efdb2634 · 2025-06-27 · email@em.sherwin-williams.com · Sweepstakes entry
197ae1a51a25ce99 · 2025-06-26 · info@fernway.com · We Hope You're Hungry
197ad5943a57a815 · 2025-06-26 · email@mail.salesforce.com · Dreamforce ROI
197ad1380a59c9d0 · 2025-06-26 · marketing@vangst.com · Staffing headaches
197ac95a14701891 · 2025-06-26 · marketing@engage.canva.com · Design didn't use a template
197ac8f3481691f7 · 2025-06-26 · info@alpharoot.com · Why choose AlphaRoot
197ac5dc41d2bebb · 2025-06-26 · salexander-vhrrental.com@voorheeshardware.ccsend.com · Summer Specials
197ac22840d5f1a2 · 2025-06-26 · marketing@treez.io · Treez rooftop celebration invite
197a8c8aebbada50 · 2025-06-25 · wholesale@verano.com · Deals Across the Board
197a8530e0b27ee8 · 2025-06-25 · andrew@northlake.supply · 4th of July team up
197a84d9f1bf8a49 · 2025-06-25 · email@mail.salesforce.com · Mulesoft integration
197a7d612baafa24 · 2025-06-25 · marc@necann.com · Final Call for Cup Entries
197a7a0de41a3243 · 2025-06-25 · 2115@fastsigns.com · Signage FASTSIGNS
197a7715fa7b56fc · 2025-06-25 · hello@vendorline.com · VendorLine bidding
197a75b26ac27e20 · 2025-06-25 · jonathon@hoodieanalytics.com · Webinar tomorrow
197a756d13eb681d · 2025-06-25 · flyers@webstaurantstore.com · Stock Up and Save
197a3e6f53fbaebb · 2025-06-24 · wholesale@verano.com · Product Drop
197a27acff54265e · 2025-06-24 · email@em.sherwin-williams.com · BOGO FrogTape
197a2400b12f44cf · 2025-06-24 · registration@benzinga.com · CCC Survey reminder
197a20ba87aa705a · 2025-06-24 · marketing@engage.canva.com · Canva Print feedback
197a1f8e8bce04e1 · 2025-06-24 · marketing.us@terrascend.com · 3-in-1 VAPES
1979e97f5840dfe4 · 2025-06-23 · maggie.boyd@verano.com · Incubus Giveaway
1979d3a5805db4f0 · 2025-06-23 · jamie-nichenfe.com@shared1.ccsend.com · New SKU's - New Smalls
1979d337dbd87771 · 2025-06-23 · sales@hamiltonfarms.com · Hamilton Farms Weekly Menu & 4th of July
1979d24de36b4a04 · 2025-06-23 · andrew@northlake.supply · Garlic Jam Live Rosin Prerolls
1979d182651b8c4d · 2025-06-23 · marketing@engage.canva.com · Hey Lemar, we miss you
19793fb18bb64d95 · 2025-06-21 · BestBuy@email.bestbuy.com · TVs as low as $69.99
19793852c21ac5bf · 2025-06-21 · Miles@sussex-cultivation.apextrading.com · ONYX menu drop
1978e18065b1e01c · 2025-06-20 · jamie-nichenfe.com@shared1.ccsend.com · New SKU's, welcome Will Andes
1978d9be8bf06bd6 · 2025-06-20 · marketing.us@terrascend.com · Summer tastes better on the exhale
1978a30081ad408d · 2025-06-19 · info@fernway.com · Meet Our Newest Partners
19789c7c7e8b682e · 2025-06-19 · maggie.boyd@verano.com · Giveaway - Incubus Live
1978906fcb2343fb · 2025-06-19 · marketing@vangst.com · Temporary staff
197887e175fc6451 · 2025-06-19 · info@alpharoot.com · Cannabis businesses deserve better insurance
197885b1920c492a · 2025-06-19 · marketing@engage.canva.com · Monthly Glow Up
197872d274fe5c1b · 2025-06-19 · marketing@mailer.murf.ai · AI Dubbing Demo
197851145ff0d539 · 2025-06-18 · wholesale@verano.com · 30% and above only
197844d24bc9129b · 2025-06-18 · noreply@aiq.com · Welcoming Terpli to AIQ
19784395be5fd137 · 2025-06-18 · marketing@engage.canva.com · Data anxiety
197842bdc474a941 · 2025-06-18 · brittanie@thrivepop.com · New Home of ThrivePOP
19783ef8e554ce48 · 2025-06-18 · hello@vendorline.com · Bidding Platform for Small Vendors
19783c71158b0f75 · 2025-06-18 · noreply@mail.lendistry.com · Small Business News
19783c30aaefc53b · 2025-06-18 · marketing@dutchie.com · Dispensary of Tomorrow
19783b098dc4f2fe · 2025-06-18 · news@kotodocan.com · Matcha Essentials
197835cdc9a8be2f · 2025-06-18 · jonathon@hoodieanalytics.com · Hoodie Analytics webinar
19781e0ef6e0184a · 2025-06-18 · info@make.com · Make blog inspiration
1977fbef9341c20a · 2025-06-17 · wholesale@verano.com · It's J's Season
1977ef71dba9a2cf · 2025-06-17 · marketing@vangst.com · Need Temporary Help
1977eabaaf18fd77 · 2025-06-17 · jamie-nichenfe.com@shared1.ccsend.com · New Account Manager Will Andes
1977e701c6be2219 · 2025-06-17 · no-reply@updates.otter.ai · Otter.ai upgrades
1977e696998490df · 2025-06-17 · homedepotpro@mg.homedepot.com · 25% Paint 90 Days
1977e3dbc58ab3db · 2025-06-17 · marketing@engage.canva.com · Recommended templates
1977de129a1a5918 · 2025-06-17 · marketing.us@terrascend.com · Vape Unlike Any Other
1977d621853f9c27 · 2025-06-17 · email@em.sherwin-williams.com · Spin to Win
1977cba83b6e1270 · 2025-06-17 · info@make.com · Connect with fellow Makers
197799dabf306280 · 2025-06-16 · seth.lesky@launchpass.intercom-mail.com · LaunchPass intro
19779505e03b35d9 · 2025-06-16 · andrew@northlake.supply · Menu Update Shoreburst OG
19779184a32e4c22 · 2025-06-16 · marketing@engage.canva.com · 10 million trees milestone
19778d2eb0a50d34 · 2025-06-16 · sales@hamiltonfarms.com · Weekly Menu & Promotion
1977794201dd7e96 · 2025-06-16 · info@make.com · Level up your Make skills
197715b0f20a8597 · 2025-06-15 · info@make.com · Welcome to Make, Lemar
1976fa6e4412f1a2 · 2025-06-14 · BestBuy@email.bestbuy.com · Apple Trade-Up Event
1976b5d7ba5896a4 · 2025-06-13 · jamie-nichenfe.com@shared1.ccsend.com · New Smalls - New Promos
1976b1b129cb96b5 · 2025-06-13 · adt@express.sea1.medallia.com · ADT survey reminder
```

## Report-only note (category:updates — never auto-trashed)

`category:updates` threads older than 1y still sitting in the inbox: **~201**, left
untouched per the runbook — this bucket mixes QuickBooks/Intuit invoices, bank/Metrc
notices, and headset.io reports with HR/jotform approvals and low-value automated mail,
too dangerous to auto-sweep. Sample sender domains seen: `notification.intuit.com`
(QuickBooks — allowlisted), `headset.io` (allowlisted), `jotform.com` (HR approvals),
`google.com` (Voice/Workspace/Ads/Looker), `dutchie.zendesk.com`, `redditmail.com`,
`extraspace.com`. Left for Lemar to clear by hand if he wants to.

## What did NOT happen (safety floor)

No email was sent, drafted, or replied to. Nothing was permanently deleted or emptied
from Trash. No Spam labels applied. Google Drive was not touched. All 130 trashed
threads remain recoverable in Gmail Trash for 30 days from today.

## Sources
- gmail: Gmail search + label/archive/trash operations on `lemar@cuzziesnj.com`, 2026-07-15
