---
created: 2026-07-19T23:07-04:00
updated: 2026-07-19T23:07-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail, cleanup, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor — first LIVE run (2026-07-19)

`DRY_RUN = false` in the runbook going into this run — this is the first run since the
supervised-preview flag was flipped off, executed against the connected Gmail account
`lemar@cuzziesnj.com` per `.claude/routines/inbox-janitor.md`.

## PART A — vendor menus archived

**116 threads** labeled `Vendor Menus` (`Label_8`) and removed from `INBOX` (still live
in All Mail under the label — fully reversible, nothing deleted). Qualifying threads
were one-way vendor broadcasts — weekly menu updates, restock/drop announcements, promo
blasts — from vendor domains: qccnj.com, verano.com, terrascend.com, awholdings.com,
freshcannabis.co, kivaconfections.com, illicitgardens.com, harvestmoonfarmsnj.com,
apextrading.com subdomains (little-leaf-labs, high-grass-farms, sussex-cultivation,
canfections-nj-llc, garden-state-exotix, the-happy-farmer-llc), budsgoods.com,
novafarms.com, parksgrove.com, laddsllc.com, jerseysmooth.com, thegardensociety.com,
arescanna.com, northlake.supply, missgrass.com.

**Left in the inbox untouched:** invoice/payment correspondence and disputes,
delivery-scheduling threads, staff intros, out-of-office notices, event
invites/cancellations, and generic brand newsletters with no concrete product/menu
signal (precision over recall, per the runbook).

**Coverage:** swept 4 pages of the vendor-domain search (~190 of an estimated ~201
raw inbox threads matching the vendor-domain seed list). More vendor-menu backlog is
likely still in the inbox for subsequent nightly runs to keep clearing — this was a
large first-run backlog, not a steady-state count.

## PART B — trash sweep (old promotions/social/forums, >12 months)

**96 threads** moved to Gmail Trash (recoverable 30 days). Candidate set:
`in:inbox older_than:1y (category:promotions OR category:social OR category:forums)`,
then gated to exclude anything `is:important`, `is:starred`, on the NEVER-TOUCH
allowlist (intuit.com, parkebank.com, fundcanna.com, stellaconnect.net, etc.), or
carrying a genuine filing label. Per-run cap of 200 was not reached.

**Notable finding:** the large majority of raw promotions/social/forums candidates in
this inbox are Gmail-flagged `IMPORTANT` (vendor marketing seems to get flagged
important here), and the safety floor protects anything `is:important` — so only 96 of
several hundred raw candidates were actually eligible to trash this run. If Lemar wants
a more aggressive sweep, the IMPORTANT-guard would need to be relaxed for specific
vendor domains — Basil is not doing that unilaterally.

**Coverage:** swept 4 pages (~193 of an estimated ~201 raw candidates) — remainder
deferred to future nightly runs.

### Trash audit (thread ID · subject · sender · date) — for 30-day recovery if needed

1981f5850a41e981 · Fernway Recycling Program · info@fernway.com · 2025-07-18
1981e5f6cac8a846 · Backfill Your OOO Gaps Now · marketing@vangst.com · 2025-07-18
19591da955823238 · A Pinch of the Good Stuff · info@fernway.com · 2025-03-13
1959186c4326683d · terp time! · wholesale@verano.com · 2025-03-13
19590b1b1727714d · Introducing Monthly Glow Up · marketing@engage.canva.com · 2025-03-13
1958efca2f979c88 · Blue Bucket Sale · email@em.sherwin-williams.com · 2025-03-13
1958c43de8e8097d · Preorder before they're gone! · wholesale@verano.com · 2025-03-12
1958b6fb94fdfad9 · 9 Days Left MJU Cannabis Cup · newjerseycannabusinessassociation.ccsend.com · 2025-03-12
1958ac3595e89018 · Unlock collaboration Jotform · benjamin@jotform.com · 2025-03-12
1958abd6d734b8b5 · Canva Create speaker · canvacreate@engage.canva.com · 2025-03-12
1958a9cf44ab74f5 · Unique User-Investor Opportunity · jsciortino@naidb.com · 2025-03-12
1958679fb053f39f · Events this month · newjerseycannabusinessassociation.ccsend.com · 2025-03-11
1958663ff7192a4a · Cannabis ATM passive income · kenneth.komarek@brinksinc.com · 2025-03-11
195863147bfbeb02 · Content Quadrant · brittanie@thrivepop.com · 2025-03-11
19585c15fb373b11 · Blueprint AI advantage · noreply@mail.squarespace.com · 2025-03-11
19585be7dce9c8b3 · Feb Pro Xtra Statement · homedepotpro@mg.homedepot.com · 2025-03-11
195839cb858ac732 · Growfather Apex Trading launch · Chris@little-leaf-labs.apextrading.com · 2025-03-11
1958201323c5ad2c · Jotform Enterprise · benjamin@jotform.com · 2025-03-10
195816421307a587 · NJEDA free eCommerce program · njedasupport@egrovesys.com · 2025-03-10
19581430092a7fa9 · Slack from Salesforce · email@mail.salesforce.com · 2025-03-10
19580f8f77eac5f0 · Credit Card Rate Review · peter@heartlandpayments.ccsend.com · 2025-03-10
19580d07abfb1db9 · Pick your final four (LeafLink) · marketing@leaflink.com · 2025-03-10
19580cd552a25b61 · 40 days until 4/20 · hello@flowhub.com · 2025-03-10
1958091fb8bacb16 · Cannabis Industry Trends · info@alpharoot.com · 2025-03-10
195807a0b71c5bce · NECANN seed cultivation session · marc@necann.com · 2025-03-10
1958071c53fa0dc0 · Hamilton Farms Weekly Menu · sales@hamiltonfarms.com · 2025-03-10
1958063e51567bc9 · Canva sales webinar · marketing@engage.canva.com · 2025-03-10
19577b0a7d9dc6bf · Best Buy Apple products · BestBuy@email.bestbuy.com · 2025-03-08
19571857bf61cec7 · Events this month · newjerseycannabusinessassociation.ccsend.com · 2025-03-07
1956d60d8fa799c7 · Fern:20 Tour · info@fernway.com · 2025-03-06
1956cf5bfac3096a · LeafLink Retail Insider · marketing@leaflink.com · 2025-03-06
1956c0c36c1be3bc · Canva Create agenda · canvacreate@engage.canva.com · 2025-03-06
1956853a9b3fba99 · Product Drop · wholesale@verano.com · 2025-03-05
195675eb87474368 · AIQ Ecommerce · noreply@aiq.com · 2025-03-05
195675d21cb5c352 · Canva whiteboards · marketing@engage.canva.com · 2025-03-05
1956750fea56e75d · VHR Hardware spring · voorheeshardware.ccsend.com · 2025-03-05
195670fad1cca9f1 · FASTSIGNS wayfinding · 2115@fastsigns.com · 2025-03-05
19566f272edfb946 · Events this month · newjerseycannabusinessassociation.ccsend.com · 2025-03-05
19562d0ad48356aa · Website Maintenance $99/mo · sales@egrovesys.com · 2025-03-04
19562739040ac71d · Cashless ATM shutdown solution · kenneth.komarek@brinksinc.com · 2025-03-04
195621c630813d71 · NECANN Boston · marc@necann.com · 2025-03-04
19561f1fa079459a · H&R Block tax prep · homedepotpro@mg.homedepot.com · 2025-03-04
19561e5ca7f177aa · Blue Bucket Sale sneak peek · email@em.sherwin-williams.com · 2025-03-04
19561954b25bf1b1 · Surf Sessions webinar · hello@surfside.io · 2025-03-04
1955d6c53778f980 · Slack productivity · email@mail.salesforce.com · 2025-03-03
1955d30a45dccd8c · March Dankness voting · marketing@leaflink.com · 2025-03-03
1955d02968c0d16a · Supernormal Feb updates · danelle@supernormal.com · 2025-03-03
1955c862cebc43cd · Events this month · newjerseycannabusinessassociation.ccsend.com · 2025-03-03
19553645db1afadc · Best Buy TV deal · BestBuy@email.bestbuy.com · 2025-03-01
195525c0f87c10b3 · Cannabis Tech guide · dayna@covasoftware.com · 2025-02-28
1954d7f344267170 · KOTODO price increase · news@kotodocan.com · 2025-02-28
1954d4e4b8a7b61e · Flower Power nomination · marketing@leaflink.com · 2025-02-28
1954d20504c31086 · Sherwin-Williams delivery · email@em.sherwin-williams.com · 2025-02-28
1954998875f8b84d · Fernway Americano flavor · info@fernway.com · 2025-02-27
19548914467f3d0f · Flowhub 420 gift · hello@flowhub.com · 2025-02-27
195488d4d8fb3deb · Surfside press release · sales@surfside.io · 2025-02-27
1954867db2d9d40e · Events this month · newjerseycannabusinessassociation.ccsend.com · 2025-02-27
195479f87e6a9fc9 · Everon Insights Feb · info@everonsolutions.com · 2025-02-27
19543e9c7a4b2366 · Surf Sessions RSVP · hello@surfside.io · 2025-02-26
19543d4e819644ff · NJEDA eCommerce program · njedasupport@egrovesys.com · 2025-02-26
19543788c4e6a08e · MJU Cannabis Cup · newjerseycannabusinessassociation.ccsend.com · 2025-02-26
195435675916568b · USVI CannaPro Summit · cannaadvisors.ccsend.com · 2025-02-26
1953e81e28907f62 · Tariff increase secure order · liam@alphasecurityus.com · 2025-02-25
1953dd52477d130a · March Dankness nominations · marketing@leaflink.com · 2025-02-25
1953cd06674c32f2 · FrogTape BOGO · email@em.sherwin-williams.com · 2025-02-25
1953a007e728f08d · Cannabis banking offer · marketing@leaflink.com · 2025-02-24
195389b382f7e0dc · Cannabis events calendar · marketing@emeraldintel.ai · 2025-02-24
195387d897ec6c33 · Cashless ATM shutdown · kenneth.komarek@brinksinc.com · 2025-02-24
195362d211c3fbb3 · Cannabis ATM problems · kenneth.komarek@brinksinc.com · 2025-02-21
1952f58125dd3890 · Best Buy Apple Trade-Up · BestBuy@email.bestbuy.com · 2025-02-22
1952926342039638 · Industrial building for sale · naidb.com (shared1.ccsend.com) · 2025-02-21
19528d20a93f2d22 · AIQ referral rewards · noreply@aiq.com · 2025-02-21
19525b49cfa66fcf · Fern:20 Tour announcement · info@fernway.com · 2025-02-20
19524c1d9ce0025a · Slack AI agents · email@mail.salesforce.com · 2025-02-20
19523724f6bc0157 · Lendistry small business news · noreply@mail.lendistry.com · 2025-02-20
1951efaf94c5e93e · Canva Create speakers · canvacreate@engage.canva.com · 2025-02-19
1951ef4e2474d837 · FASTSIGNS · 2115@fastsigns.com · 2025-02-19
1951aaee128bfa49 · NJEDA eCommerce program · njedasupport@egrovesys.com · 2025-02-18
1951a3c7565aa354 · Cannabis ATM success · kenneth.komarek@brinksinc.com · 2025-02-18
1951a3a95df9a814 · AIQ Academy live · noreply@aiq.com · 2025-02-18
19519d461b8d61fb · Heartland free payroll · peter@heartlandpayments.ccsend.com · 2025-02-18
195195f4ae3bd7ef · AIQ growth hack · noreply@aiq.com · 2025-02-18
195191ee14749ece · Last day to register · newjerseycannabusinessassociation.ccsend.com · 2025-02-18
19514db5441ed713 · Apple Pay setup · applepay@insideapple.apple.com · 2025-02-17
19514ba710619d73 · Vehicle trade-in offer · easyautopa@alstspecials.com · 2025-02-17
195145f236f81796 · Upcoming Event This Month · newjerseycannabusinessassociation.ccsend.com · 2025-02-17
19514160d4e5c9f1 · Winter Specials ladders/scaffolding · voorheeshardware.ccsend.com · 2025-02-17
1950bb64f8bb02df · Best Buy Presidents Day · BestBuy@email.bestbuy.com · 2025-02-15
19505d053fbe9b3d · Cova POS pitch · dayna@covasoftware.com · 2025-02-14
19505893983a8450 · AIQ product updates · launchnotes.io · 2025-02-14
1950537599ffa4d0 · AIQ CSAT survey · noreply@aiq.com · 2025-02-14
19504a332bac38d6 · Upcoming Event This Month · newjerseycannabusinessassociation.ccsend.com · 2025-02-14
195048d8031e19cc · Dropbox digital signature · no-reply@em-s.dropbox.com · 2025-02-14
1950131594ee4ed3 · Fernway artist collab · info@fernway.com · 2025-02-13
19500b610149d385 · Salesforce AI trust report · email@mail.salesforce.com · 2025-02-13
19500b1d9230b593 · Upcoming Event This Month · newjerseycannabusinessassociation.ccsend.com · 2025-02-13
194ff9f0db616828 · AIQ growth hack · noreply@aiq.com · 2025-02-13
194ff8000418515e · Dropbox convert files · no-reply@em-s.dropbox.com · 2025-02-13

## category:updates — report-only, never auto-trashed

~201 estimated old (>12mo) threads in this category, mixing invoices/payroll
(notification.intuit.com, quickbooks), inventory/sales reports (headset.io daily
summaries), security-system alerts (adtcontrol.com), payment receipts
(messaging.squareup.com, FedEx, trustaltus.com/Altus collections), signed-form
confirmations (jotformsign.com), and insurance (progressive.com) — exactly the mixed
bag the runbook warned about. Left entirely untouched. Lemar may want to hand-clear old
headset.io / jotformsign.com / adtcontrol.com noise himself, but Basil will not sweep
this category.

## Worth Lemar's attention

Most raw promotions/social/forums candidates in this inbox carry Gmail's `IMPORTANT`
flag, which the safety floor protects — so the actual trash-eligible set (96) was a
small fraction of the raw category match across the pages swept. If a more aggressive
sweep is wanted, the IMPORTANT-guard would need loosening for specific vendor domains —
a call for Lemar, not something Basil should do unilaterally.

## Next run

Both PART A and PART B searches returned ~201 estimated raw results; only ~190-193 were
swept this run (4 pages each). Expect meaningful continued cleanup over the next several
nightly runs until the backlog reaches steady state.

## Sources
- gmail: lemar@cuzziesnj.com inbox sweep, 2026-07-19 (Basil / Inbox Janitor routine)
