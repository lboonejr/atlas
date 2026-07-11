---
created: 2026-07-11T23:07:00-04:00
updated: 2026-07-11T18:00:00-04:00
domain: cuzzies
type: brief
status: done
tags: [inbox-janitor, basil, gmail, dry-run, vendor-menus, trash-sweep]
source: gmail
---

# Inbox Janitor (Basil) — 2026-07-11 DRY RUN preview

First supervised run of the nightly Inbox Janitor routine (`.claude/routines/inbox-janitor.md`)
against `lemar@cuzziesnj.com`. `DRY_RUN = true` — **no Gmail mutations were made.** Everything
below is a preview for Lemar to vet before flipping `DRY_RUN = false` in the runbook.

## Preflight
- `Vendor Menus` label already exists (`Label_8`) — no creation needed.

## PART A — vendor menus (would-archive preview)
Query: `in:inbox has:attachment` AND (vendor-domain-seed-list match OR subject signal:
menu / availability / price sheet / drop / in stock / live menu).

Sampled **150** qualifying inbox threads across 3 pages (Gmail's search estimate caps
around ~200 and a `nextPageToken` remained after the sample, so the true population is
likely larger — this is a representative preview, not an exhaustive count). Threads span
roughly 2026-06-12 through 2026-07-10.

Top senders by volume: `harvestmoonfarmsnj.com`, `awholdings.com` (Ascend),
`qccnj.com`, `kivaconfections.com`, `terrascend.com`, `verano.com`, `freshcannabis.co`,
`novafarms.com`, `budsgoods.com`, `jerseysmooth.com`, `prolificgrowhouse.com`,
`missgrass.com`, `laddsllc.com`, `northlake.supply`, `arescanna.com`, `parksgrove.com` —
all on the anchors.md vendor-domain seed list, plus a handful of adjacent
cannabis-wholesale senders carrying clear menu/drop/in-stock signals not yet on the seed
list: `stashhousedistro.com`, `hamiltonfarms.com`, `hillviewmed.com` / `hillviewfarms.com`,
`thegardensociety.com`, `high-grass-farms.apextrading.com`, `sussex-cultivation.apextrading.com`,
`little-leaf-labs.apextrading.com`. **Worth adding these to the seed list in anchors.md**
once Lemar confirms they're legitimate menu senders.

Would archive: **~150** (sampled) threads — label `Vendor Menus`, remove `INBOX`. Nothing
in Part A is ever trashed.

## PART B — trash sweep (would-trash preview)
Query: `older_than:1y (category:promotions OR category:social OR category:forums)
-is:starred -is:important`.

Sampled **150** candidate threads across 3 pages (more exist beyond a remaining
`nextPageToken` — comfortably under the 200/night per-run cap for now; the routine will
keep working through the backlog on later nights once live). Date range: 2025-06-08
through 2025-07-10 (all >12 months old as of today).

**NEVER-TOUCH allowlist check:** 1 thread excluded — `197a8cdb6f1d9200`, "CTA Level 6
\"Ask Me Anything\" Instructor Q&A This Friday", sender `CTA@sos.nj.gov`, 2025-06-25 —
excluded because `*.gov` is on the allowlist. No other sampled thread matched the
allowlist (checked against intuit.com, quickbooks, tsheets.com, gusto.com, parkebank.com,
fundcanna.com, firstinsurancefunding.com, pactsafe.com, docusign, `*.gov`,
accounts.google.com, headset.io, stellaconnect.net). No starred/important threads
appeared (already excluded by the query). No genuine user filing labels were present on
any sampled thread.

**Net: 149 threads would be trashed** (recoverable in Gmail Trash for 30 days if this
were live). Full audit list below — this is the recovery record if any of these turn out
to be a mistake.

**Gap to close next run:** this preview did not separately tally old `category:updates`
senders (report-only per the routine — never auto-trashed). A future run should list a
handful of old-`updates` sender domains in the digest per the runbook's intent.

### Would-trash audit list (149 threads)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 197f626cdf43a580 | 📣 Your Call to the Table. Let's Eat. | info@fernway.com | 2025-07-10 |
| 197f5411f91e0bf8 | New! Bring your team. Save $1,300 per pass. | email@mail.salesforce.com | 2025-07-10 |
| 197f4db5a1b88e99 | Last Chance to Lock In 25% Savings on Paint | homedepotpro@mg.homedepot.com | 2025-07-10 |
| 197f4b58bd027027 | Order up! Do more for less | flyers@webstaurantstore.com | 2025-07-10 |
| 197f4b109e29e872 | Ready to scale? Make sure you're covered. | info@alpharoot.com | 2025-07-10 |
| 197f4619d1f7afc3 | Your Monthly Digest Is Delivered | matthewmatey@worldinsurance.com | 2025-07-10 |
| 197f066ac9c45479 | Build lasting relationships with data powering AI and Agentforce. | email@mail.salesforce.com | 2025-07-09 |
| 197f01659e718eca | Join us at ZapConnect 2025! | events@send.zapier.com | 2025-07-09 |
| 197efc34700f3239 | Custom Visuals Bring a Property to Life \| FASTSIGNS | 2115@fastsigns.com | 2025-07-09 |
| 197ef2a4aac6d371 | Lemon Cherry Gelato is back and better than ever! | jamie-nichenfe.com@shared1.ccsend.com | 2025-07-09 |
| 197ebf238973562b | Classic Summer Strains | wholesale@verano.com | 2025-07-08 |
| 197eb7c5c0cfd5db | 2025 New Jersey Cannabis Convention & NECANN Cup | marc@necann.com | 2025-07-08 |
| 197eac851f0bd244 | Register Now: Livestream with Planet 13 VP of Marketing | hello@surfside.io | 2025-07-08 |
| 197eab68836c2ac8 | mommy... mamacita..? | brittanie@thrivepop.com | 2025-07-08 |
| 197ea98fa3cf5ae3 | Your June 2025 Pro Xtra Statement is Here | homedepotpro@mg.homedepot.com | 2025-07-08 |
| 197e771220095753 | Growfather NEW Releases | Chris@little-leaf-labs.apextrading.com | 2025-07-08 |
| 197e6e7e3688de23 | J's galore! | wholesale@verano.com | 2025-07-07 |
| 197e633f5abb85bf | Hear from experts at Canva and Meta | marketing@engage.canva.com | 2025-07-07 |
| 197e6202544a99a6 | Stacked with Diamonds - New Pre-Rolls Hit Different | marketing.us@terrascend.com | 2025-07-07 |
| 197e5bf16def1b8c | Feedback on the New Kiosk Payment Workflow | payments@dutchie.com | 2025-07-07 |
| 197e5ba9eb3f7907 | The Hidden Cost of Summer Absenteeism | marketing@vangst.com | 2025-07-07 |
| 197e59d40667e266 | New SKU's - Don't Miss Out! | jamie-nichenfe.com@shared1.ccsend.com | 2025-07-07 |
| 197e57bb1e36f0d7 | Post-4th Restock: New Preroll Strains & Nimbus Vapes | andrew@northlake.supply | 2025-07-07 |
| 197e56cc6e452ada | [[ 7/7 to 7/14 ]] Get the most out of this offer | email@em.sherwin-williams.com | 2025-07-07 |
| 197e52a48321ae32 | It's time! Bulk up on BIG savings | flyers@webstaurantstore.com | 2025-07-07 |
| 197e524eeec2cd45 | Two shows. Endless opportunity. | marc@necann.com | 2025-07-07 |
| 197e4f3123b78072 | Last Call! Treez Innovation Showcase | marketing@treez.io | 2025-07-07 |
| 197e19bbe86b071c | Reminder – Brief survey on your ADT visit | adt@express.sea1.medallia.com | 2025-07-06 |
| 197dc7a88214c4ea | Your inbox just got some more deals | BestBuy@email.bestbuy.com | 2025-07-05 |
| 197d570aa9a563a0 | How was your Grainger delivery? | Grainger@feedback.grainger.com | 2025-07-04 |
| 197d2c044fac3684 | Welcome to Memberstack! | support@memberstack.com | 2025-07-04 |
| 197d21ddea8e48de | Brief survey on your ADT visit | adt@express.sea1.medallia.com | 2025-07-03 |
| 197d1f5a4360b576 | The Season of Abundance is Here | info@fernway.com | 2025-07-03 |
| 197d18dad8d102ba | All the Stars! | wholesale@verano.com | 2025-07-03 |
| 197d12011ef96871 | Still dealing with staffing gaps? | marketing@vangst.com | 2025-07-03 |
| 197d0e671f826258 | New SKU's - Don't Miss Out! | jamie-nichenfe.com@shared1.ccsend.com | 2025-07-03 |
| 197d09fe9e9a776d | Coverage cannabis companies can actually rely on | info@alpharoot.com | 2025-07-03 |
| 197d09a1d3a79fcd | Recommended templates based on your search | marketing@engage.canva.com | 2025-07-03 |
| 197ce8220cb41d96 | New reward available | noreply@www.learnbrands.com | 2025-07-03 |
| 197cd27f89db702a | NEW PRODUCT ALERT | wholesale@verano.com | 2025-07-02 |
| 197cc58e8f39e3bf | Ready to say goodbye to endless searches | email@mail.salesforce.com | 2025-07-02 |
| 197cbf9797383b0b | Need workers you can count on | marketing@vangst.com | 2025-07-02 |
| 197cbeb2c7b72bd1 | Make your social content shine | marketing@engage.canva.com | 2025-07-02 |
| 197cbc4a197a6b08 | ONYX Apex Menu - Wednesday, July 2nd | Phil@sussex-cultivation.apextrading.com | 2025-07-02 |
| 197cb635180ac90e | We Can't Say Much… But It's 🔥 | marketing.us@terrascend.com | 2025-07-02 |
| 197cb05f7ea83419 | Don't Miss Out: Treez Cannabis Innovation Showcase | marketing@treez.io | 2025-07-02 |
| 197c903660ade268 | "Bought a house last February..." (r/gardening) | noreply@redditmail.com | 2025-07-02 |
| 197c8028ed7af33b | Verano NJ Wholesale Order Guide | wholesale@verano.com | 2025-07-01 |
| 197c73337152b902 | Employees calling in again? | marketing@vangst.com | 2025-07-01 |
| 197c6ab25dcb4413 | Happy 4th of July! + Next Week's Pre-Orders | andrew@northlake.supply | 2025-07-01 |
| 197c64062b3ad79c | Request for Assistance | customerexperience@feedback.wm.com | 2025-07-01 |
| 197c6254c6001acc | Sell Thru Starts Here | marketing.us@terrascend.com | 2025-07-01 |
| 197c5fafa5005eed | How was your delivery? Grainger | Grainger@feedback.grainger.com | 2025-07-01 |
| 197c5e814580d743 | How to Launch Your Cannabis Business Successfully | michelle-thinkcanna.com@cannaadvisors.ccsend.com | 2025-07-01 |
| 197c21e9c2a4544d | Coming next week: Game-changing upgrades to AIQ | noreply@aiq.com | 2025-06-30 |
| 197c198384246d22 | EXCLUSIVE: 2 NJ Cannabis Opportunities | Julian@cd.cdre.co | 2025-06-30 |
| 197c0fd2ca09b159 | Final Call: Two Opportunities. One Deadline. | marc@necann.com | 2025-06-30 |
| 197b62308f4c6d7d | TVs as low as $199.99 | BestBuy@email.bestbuy.com | 2025-06-28 |
| 197b26a8efdb2634 | Enter before 8/7! sweepstakes | email@em.sherwin-williams.com | 2025-06-27 |
| 197ae1a51a25ce99 | We Hope You're Hungry... | info@fernway.com | 2025-06-26 |
| 197ad5943a57a815 | Real ROI starts at Dreamforce | email@mail.salesforce.com | 2025-06-26 |
| 197ad1380a59c9d0 | Still Dealing with Staffing Headaches? | marketing@vangst.com | 2025-06-26 |
| 197ac95a14701891 | Your recent design didn't use a template | marketing@engage.canva.com | 2025-06-26 |
| 197ac8f3481691f7 | Why top cannabis businesses choose AlphaRoot | info@alpharoot.com | 2025-06-26 |
| 197ac5dc41d2bebb | Summer Specials | salexander-vhrrental.com@voorheeshardware.ccsend.com | 2025-06-26 |
| 197ac22840d5f1a2 | You're Invited: Treez Innovation Showcase | marketing@treez.io | 2025-06-26 |
| 197a8c8aebbada50 | Deals Across the Board! | wholesale@verano.com | 2025-06-25 |
| 197a8530e0b27ee8 | Planning for 4th of July? Let's Team Up | andrew@northlake.supply | 2025-06-25 |
| 197a84d9f1bf8a49 | Accelerate your digital transformation | email@mail.salesforce.com | 2025-06-25 |
| 197a7d612baafa24 | Final Call for Cup Entries in MA & NJ | marc@necann.com | 2025-06-25 |
| 197a7a0de41a3243 | Signage For a Striking Entertainment Venue | 2115@fastsigns.com | 2025-06-25 |
| 197a7715fa7b56fc | Bidding is Getting Smarter with VendorLine | hello@vendorline.com | 2025-06-25 |
| 197a75b26ac27e20 | Webinar tomorrow at 11 CT | jonathon@hoodieanalytics.com | 2025-06-25 |
| 197a756d13eb681d | Stock Up and Save | flyers@webstaurantstore.com | 2025-06-25 |
| 197a3e6f53fbaebb | PRODUCT DROP | wholesale@verano.com | 2025-06-24 |
| 197a27acff54265e | BOGO FrogTape | email@em.sherwin-williams.com | 2025-06-24 |
| 197a2400b12f44cf | Quick Reminder: CCC Survey | registration@benzinga.com | 2025-06-24 |
| 197a20ba87aa705a | We're still interested in your feedback | marketing@engage.canva.com | 2025-06-24 |
| 197a1f8e8bce04e1 | 3-in-1 VAPES are HERE | marketing.us@terrascend.com | 2025-06-24 |
| 1979e97f5840dfe4 | Incubus Giveaway | maggie.boyd@verano.com | 2025-06-23 |
| 1979d3a5805db4f0 | New SKU's - New Smalls! | jamie-nichenfe.com@shared1.ccsend.com | 2025-06-23 |
| 1979d337dbd87771 | Hamilton Farms Weekly Menu & 4th of July | sales@hamiltonfarms.com | 2025-06-23 |
| 1979d24de36b4a04 | New This Week: Garlic Jam... | andrew@northlake.supply | 2025-06-23 |
| 1979d182651b8c4d | Hey Lemar, we miss you... | marketing@engage.canva.com | 2025-06-23 |
| 19793fb18bb64d95 | TVs as low as $69.99 | BestBuy@email.bestbuy.com | 2025-06-21 |
| 19793852c21ac5bf | ONYX- Exciting menu drop 6-21-25 | Miles@sussex-cultivation.apextrading.com | 2025-06-21 |
| 1978e18065b1e01c | New SKU's - New Smalls! | jamie-nichenfe.com@shared1.ccsend.com | 2025-06-20 |
| 1978d9be8bf06bd6 | Summer tastes better on the exhale | marketing.us@terrascend.com | 2025-06-20 |
| 1978a30081ad408d | Meet Our Newest Partners | info@fernway.com | 2025-06-19 |
| 19789c7c7e8b682e | Giveaway - Incubus Live! | maggie.boyd@verano.com | 2025-06-19 |
| 1978906fcb2343fb | Looking for temporary staff | marketing@vangst.com | 2025-06-19 |
| 197887e175fc6451 | Cannabis businesses deserve better insurance | info@alpharoot.com | 2025-06-19 |
| 197885b1920c492a | Monthly Glow Up | marketing@engage.canva.com | 2025-06-19 |
| 197872d274fe5c1b | Cut Localization Time by 90% | marketing@mailer.murf.ai | 2025-06-19 |
| 197851145ff0d539 | 30% & above only! | wholesale@verano.com | 2025-06-18 |
| 197844d24bc9129b | We've got big news: Welcoming Terpli to AIQ | noreply@aiq.com | 2025-06-18 |
| 19784395be5fd137 | Data anxiety is real | marketing@engage.canva.com | 2025-06-18 |
| 197842bdc474a941 | Just Launched: The New Home of ThrivePOP | brittanie@thrivepop.com | 2025-06-18 |
| 19783ef8e554ce48 | Finally, A Bidding Platform for Small Vendors | hello@vendorline.com | 2025-06-18 |
| 19783c71158b0f75 | News & Resources for Small Businesses | noreply@mail.lendistry.com | 2025-06-18 |
| 19783c30aaefc53b | Ready to build the Dispensary of Tomorrow? | marketing@dutchie.com | 2025-06-18 |
| 19783b098dc4f2fe | KOTODO: Matcha Essentials Are Back | news@kotodocan.com | 2025-06-18 |
| 197835cdc9a8be2f | Live Webinar from Hoodie Analytics | jonathon@hoodieanalytics.com | 2025-06-18 |
| 19781e0ef6e0184a | Inspiration, help and updates on Make blog | info@make.com | 2025-06-18 |
| 1977fbef9341c20a | It's J's Season | wholesale@verano.com | 2025-06-17 |
| 1977ef71dba9a2cf | Need Temporary Help? Vangst | marketing@vangst.com | 2025-06-17 |
| 1977eabaaf18fd77 | Meet Our New Account Manager – Will Andes | jamie-nichenfe.com@shared1.ccsend.com | 2025-06-17 |
| 1977e701c6be2219 | The upgrades you've been waiting for | no-reply@updates.otter.ai | 2025-06-17 |
| 1977e696998490df | Save 25% on Paint for 90 Days | homedepotpro@mg.homedepot.com | 2025-06-17 |
| 1977e3dbc58ab3db | Recommended templates | marketing@engage.canva.com | 2025-06-17 |
| 1977de129a1a5918 | A Vape Unlike Any Other | marketing.us@terrascend.com | 2025-06-17 |
| 1977d621853f9c27 | Come and be a winner! Spin the wheel | email@em.sherwin-williams.com | 2025-06-17 |
| 1977cba83b6e1270 | Joining forces: Connect with fellow Makers | info@make.com | 2025-06-17 |
| 197799dabf306280 | Hi 🚀 (LaunchPass) | seth.lesky@launchpass.intercom-mail.com | 2025-06-16 |
| 19779505e03b35d9 | Menu Update: Shoreburst OG Almost Gone | andrew@northlake.supply | 2025-06-16 |
| 19779184a32e4c22 | We've reached an important milestone | marketing@engage.canva.com | 2025-06-16 |
| 19778d2eb0a50d34 | Hamilton Farm's Weekly Menu & Promotion | sales@hamiltonfarms.com | 2025-06-16 |
| 1977794201dd7e96 | Level up your Make skills | info@make.com | 2025-06-16 |
| 197715b0f20a8597 | Welcome to Make, Lemar! | info@make.com | 2025-06-15 |
| 1976fa6e4412f1a2 | Get Apple devices for less | BestBuy@email.bestbuy.com | 2025-06-14 |
| 1976b5d7ba5896a4 | New Smalls - New Promos! | jamie-nichenfe.com@shared1.ccsend.com | 2025-06-13 |
| 1976b1b129cb96b5 | Reminder - ADT customer service survey | adt@express.sea1.medallia.com | 2025-06-13 |
| 1976a8ee52efed9a | Verano Marketing Newsletter - May | maggie.boyd@verano.com | 2025-06-13 |
| 19769d4427b9ca0f | Register: Business Training Series | email@em.sherwin-williams.com | 2025-06-13 |
| 19765cee6686b0d5 | Elderflower is Now Available Near You | info@fernway.com | 2025-06-12 |
| 1976558baa926a45 | How AI and AI Agents Will Shape Integration | email@mail.salesforce.com | 2025-06-12 |
| 19764acb6ed4cd05 | Vangst Weekly: Request Labor Today! | mckenzie.nowell@vangst.com | 2025-06-12 |
| 19764772c5d57cd4 | Introducing Dutchie 2.0 Summer '25 Release | marketing@dutchie.com | 2025-06-12 |
| 197647723f6ec1f5 | For When Speed and Results Matter | email@em.sherwin-williams.com | 2025-06-12 |
| 19764652e1b8ad40 | High Grass Farms-Select Flower Tops In-Stock | Francisco@high-grass-farms.apextrading.com | 2025-06-12 |
| 1976403b8cac2103 | Get Ahead With AI Demos and Digital Signage | sales@budvue.com | 2025-06-12 |
| 19760cb17c5a1dfa | Reminder - ADT survey | adt@express.sea1.medallia.com | 2025-06-11 |
| 1975fd3d99d7b69f | How this small-town dispensary is growing online | hello@flowhub.com | 2025-06-11 |
| 1975fa6f23ce4d8c | Why Your Dispensary Needs a Unified Cannabis Platform | marketing@treez.io | 2025-06-11 |
| 1975f8a4d8cf8dbd | Overwhelmed with Updating a Large Building? | 2115@fastsigns.com | 2025-06-11 |
| 1975f83665532e72 | Share Your Feedback on Benzinga CCC | registration@benzinga.com | 2025-06-11 |
| 1975eddb84edc0a1 | Yellow Mermaid is Back! | jamie-nichenfe.com@shared1.ccsend.com | 2025-06-11 |
| 1975bce1910f55b9 | Bananas & Guavas | wholesale@verano.com | 2025-06-10 |
| 1975a8e0b5e281f1 | 2 Days Left: Register for Dreamforce | email@mail.salesforce.com | 2025-06-10 |
| 1975a3da13c1b886 | See why top dispensaries trust Springbig | marketing@springbig.com | 2025-06-10 |
| 19759d512ecacb2f | Be Where the Industry Shows Up | marc@necann.com | 2025-06-10 |
| 19756b56310999fc | Flower SALE! | wholesale@verano.com | 2025-06-09 |
| 19756624a199b485 | Hamilton Farm's Weekly Menu! (New Jar release!) | sales@hamiltonfarms.com | 2025-06-09 |
| 197557e81f1d2ce2 | Try Before You Hire with No Conversion Fees | marketing@vangst.com | 2025-06-09 |
| 1975539962eb9ae5 | New Nimbus Featured Farm + Restocks | andrew@northlake.supply | 2025-06-09 |
| 197550deb90f1133 | Recommended templates | marketing@engage.canva.com | 2025-06-09 |
| 197550bf2a65ade1 | New Pre-Rolls! | jamie-nichenfe.com@shared1.ccsend.com | 2025-06-09 |
| 1975154ee7eee9d5 | Brief survey on your ADT customer service experience | adt@express.sea1.medallia.com | 2025-06-08 |
| 19750cf91961e46e | You're Invited: Welcome Reception (Benzinga) | registration@benzinga.com | 2025-06-08 |

### Excluded by NEVER-TOUCH allowlist (not in the would-trash list above)

| Thread ID | Subject | Sender | Date | Reason |
|---|---|---|---|---|
| 197a8cdb6f1d9200 | CTA Level 6 "Ask Me Anything" Instructor Q&A This Friday | CTA@sos.nj.gov | 2025-06-25 | `*.gov` on NEVER-TOUCH allowlist |

## Next step
Lemar: vet this list (especially the ~150 vendor-menu senders and the 149 would-trash
senders) for any false positives, then flip `DRY_RUN = false` in
`.claude/routines/inbox-janitor.md` on `main` to make tomorrow's run act for real.

## Sources
- gmail: search `in:inbox has:attachment (...)` — vendor-menu candidates
- gmail: search `older_than:1y (category:promotions OR category:social OR category:forums) -is:starred -is:important` — trash-sweep candidates
