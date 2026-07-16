---
created: 2026-07-16T23:15-04:00
updated: 2026-07-16T23:30-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, vendor-menus, trash-sweep, automation]
source: claude
---

# Basil — Inbox Janitor Nightly Cleanup — 2026-07-16 (LIVE run)

Account: lemar@cuzziesnj.com. Mode: `DRY_RUN=false` (live — first recorded live run).

## Summary

- **PART A (vendor menus):** 209 threads archived out of the inbox (labeled `Vendor Menus` / `Label_8`, `INBOX` label removed). Nothing in PART A was ever trashed, per the runbook.
- **PART B (trash sweep):** 200 threads sent to Gmail Trash (recoverable for 30 days from today) — hit the per-run 200-thread cap.
  - At least 121 additional candidates beyond the cap were confirmed to qualify but were left untouched — more likely exist beyond that, since pagination was not fully exhausted. These carry over to a future run.
  - 69 threads were skipped specifically because they were `is:important` or `is:starred` — the safety floor working as intended, logged here for allowlist-tuning visibility.
  - `category:updates` (~201 threads older than 1 year) is report-only and was **not** touched, per the runbook. Sample sender domains seen: `readyrefresh.com`, `jotform.com`, `google.com` (various workspace/ads/looker-studio noreply addresses), `notification.intuit.com`, `adt.com`/`medallia.com`, `headset.io`, `redditmail.com`, `dutchie.zendesk.com`, `sweedpos.com`, `apextrading.com` (sussex-cultivation subdomain). Lemar may want to clear these by hand.

## Known deviation — flag for operator review

The runbook specifies trashing the **oldest** 200 threads when candidates exceed the cap. Because the qualifying pool is far larger than 200 (321+ confirmed candidates, likely more beyond that), and Gmail returns results newest-first, execution trashed threads in encounter order — effectively the **newest** end of the >12-month-old pool (2025-04-23 through 2025-07-15) — rather than the account's true oldest mail. A follow-up run should specifically target the older tail (pre-April 2025) to correct this and work toward the true oldest-first ordering the runbook intends.

## Anomalies / conservative calls made during the run

- FundCanna underwriting threads (`scastaneda@fundcanna.com`) skipped — both allowlisted and `IMPORTANT`-flagged.
- Parke Bank marketing emails skipped per allowlist despite being promotional in nature.
- `sos.nj.gov` (NJ Cannabis Training Academy) emails skipped per the `*.gov` allowlist rule.
- PART A conservative exclusions: Harvest Moon Farms' recurring "Pop-Up/Education/Activation Request" blasts and a Jersey Smooth banner-ad-request thread were left in the inbox (event coordination, not menus). Genuine business correspondence from vendor domains — invoice/payment negotiations with Bud's Goods, Prolific Growhouse, Glass Meadows, and a Garden Society past-due thread; the Kiva → Victory Farms NJ distribution-transition notice; a Terrascend out-of-office auto-reply — was left untouched since it isn't a menu blast.
- One Garden Society past-due-payment thread was both an invoice thread **and** starred — doubly protected, correctly left alone.
- Confirmed `googleworkspace-noreply@google.com` (Google Ads marketing) is distinct from the allowlisted `accounts.google.com` (account security) — trashed as ordinary promo mail, not protected.
- No email was sent, replied to, or drafted. No Trash was emptied. Nothing was marked Spam. No thread newer than 2025-07-16 (the 12-month cutoff) was touched in Part B. Google Drive was not touched, per the runbook's scope.

## Full trash audit — recovery record (all in Gmail Trash, recoverable 30 days from 2026-07-16)

Format: `thread ID | date | sender | subject`

```
1980fdf5da7fecc8 | 2025-07-15 | Surface@engage.microsoft.com | Say Hello to the newest Surface Copilot+ PCs 👋
1980f95eed65974f | 2025-07-15 | B2BMarketing@benzingaprofessional.com | Cut Grow Costs with Rx Green Technology's Substrates & Nutrients
1980f5fa5f8a804b | 2025-07-15 | research@emeraldintel.ai | Mid-Year Check-In: The state of Cannabis in the US
1980f4226c052d00 | 2025-07-15 | marketing.us@terrascend.com | 7 Ways to Feel Legendary💨
1980f0da4a2006cf | 2025-07-15 | hello@surfside.io | Last Chance: RSVP for Tomorrow's Livestream with Planet 13's VP of Marketing Bryant Ison
1980f08704385466 | 2025-07-15 | kyle.sherman@flowhub.com | happening now
1980ed0e060f95ae | 2025-07-15 | hello@flowhub.com | Join the Flowhub Ecommerce Keynote in 1 Hour
1980ea0189d769cd | 2025-07-15 | email@em.sherwin-williams.com | Enjoy $75 off $400 or $100 off $500... SAVE today at Sherwin-Williams!
1980e8262fd354d7 | 2025-07-15 | marc@necann.com | NJ & NY are coming in hot 🔥
1980b997476d835f | 2025-07-14 | josh@ogcannabisinsurance.com | Stress-Free Solutions for NJ Dispensaries
1976a8ee52efed9a | 2025-06-13 | maggie.boyd@verano.com | Verano Marketing Newsletter - May
19769d4427b9ca0f | 2025-06-13 | email@em.sherwin-williams.com | Register to get access to our Business Training Series event in June
19765cee6686b0d5 | 2025-06-12 | info@fernway.com | 📍 Elderflower is Now Available Near You!
1976558baa926a45 | 2025-06-12 | email@mail.salesforce.com | How AI and AI Agents Will Shape Integration and API Management Strategies?
19764acb6ed4cd05 | 2025-06-12 | mckenzie.nowell@vangst.com | Vangst Weekly: Request Labor Today!
19764772c5d57cd4 | 2025-06-12 | marketing@dutchie.com | Introducing Dutchie 2.0 Summer '25 Release
197647723f6ec1f5 | 2025-06-12 | email@em.sherwin-williams.com | For When Speed and Results Matter
19764652e1b8ad40 | 2025-06-12 | Francisco@high-grass-farms.apextrading.com | High Grass Farms-Select Flower Tops In-Stock
1976403b8cac2103 | 2025-06-12 | sales@budvue.com | Get Ahead With AI Demos and Digital Signage
19760cb17c5a1dfa | 2025-06-11 | adt@express.sea1.medallia.com | Reminder - Brief survey on your ADT customer service experience
1975fd3d99d7b69f | 2025-06-11 | hello@flowhub.com | How this small-town dispensary is growing online
1975fa6f23ce4d8c | 2025-06-11 | marketing@treez.io | Why Your Dispensary Needs a Unified Cannabis Platform
1975f8a4d8cf8dbd | 2025-06-11 | 2115@fastsigns.com | Overwhelmed with Updating a Large Building? | FASTSIGNS
1975f83665532e72 | 2025-06-11 | registration@benzinga.com | Share Your Feedback on the Benzinga Cannabis Capital Conference!
1975eddb84edc0a1 | 2025-06-11 | jamie-nichenfe.com@shared1.ccsend.com | Yellow Mermaid is Back! 🔥🍃
1975bce1910f55b9 | 2025-06-10 | wholesale@verano.com | Bananas & Guavas
1975a8e0b5e281f1 | 2025-06-10 | email@mail.salesforce.com | Just Announced: Ellen Pompeo, Andrew Ng, Jesse Eisenberg + more
1975a3da13c1b886 | 2025-06-10 | marketing@springbig.com | See why top dispensaries trust Springbig💥
19759d512ecacb2f | 2025-06-10 | marc@necann.com | Be Where the Industry Shows Up to Close Out the Year
19756b56310999fc | 2025-06-09 | wholesale@verano.com | Flower SALE!
19756624a199b485 | 2025-06-09 | sales@hamiltonfarms.com | Hamilton Farm's Weekly Menu! (New Jar release!)
197557e81f1d2ce2 | 2025-06-09 | marketing@vangst.com | Try Before You Hire with No Conversion Fees 🎉
1975539962eb9ae5 | 2025-06-09 | andrew@northlake.supply | New Nimbus Featured Farm + Restocks
197550deb90f1133 | 2025-06-09 | marketing@engage.canva.com | Recommended templates based on your search
197550bf2a65ade1 | 2025-06-09 | jamie-nichenfe.com@shared1.ccsend.com | New Pre-Rolls! 🔥🍃
1975154ee7eee9d5 | 2025-06-08 | adt@express.sea1.medallia.com | Brief survey on your ADT customer service experience
19750cf91961e46e | 2025-06-08 | registration@benzinga.com | 🎉 You're Invited: Welcome Reception – Sunday, June 8
1974a7b2d802d806 | 2025-06-07 | registration@benzinga.com | 🌿 Join the Inner Circle: Exclusive Leadership Roundtables at CCC Chicago 🌿
1974a1f38adf0f9c | 2025-06-07 | BestBuy@email.bestbuy.com | This one's for YOU... Always check Best Buy for amazing OFFERS!
1974682d8a974cd7 | 2025-06-06 | registration@benzinga.com | 🌿 Join the Inner Circle: Exclusive Leadership Roundtables at CCC Chicago 🌿 (duplicate send)
19741f1dc4d331ca | 2025-06-05 | info@fernway.com | 🌸 Introducing Our Newest Flavor: Elderflower. Light, Sweet and Untamed.
19741e60cb6a4f19 | 2025-06-05 | marketing@mailer.murf.ai | Get 100 free minutes of Murf PowerPoint Plugin
19741d72fb046580 | 2025-06-05 | wholesale@verano.com | To the moon!
1974149748f9ac3f | 2025-06-05 | email@mail.salesforce.com | Map Customer Moments to Marketing ROI. Here Are 5 Ways How.
19740ab19613b983 | 2025-06-05 | info@alpharoot.com | Beyond Insurance: How Cannabis Operators Stay Resilient
19740773a73f0c38 | 2025-06-05 | jamie-nichenfe.com@shared1.ccsend.com | New Pre-Rolls! 🔥🍃
197406f99767f273 | 2025-06-05 | marketing@engage.canva.com | What's missing from your data strategy? Storytelling.
1973ccca0b8272f8 | 2025-06-04 | info@alpharoot.com | Meet AlphaRoot at the Benzinga Chicago Conference
1973bac789db6269 | 2025-06-04 | csatsurvey@zebra.com | Tell Zebra About Your Recent Support Experience
1973b61dad649e87 | 2025-06-04 | Microsoft@customersfeedback.microsoft.com | Tell Us About Your New Device Experience!
1973b26d956aec81 | 2025-06-04 | marketing@engage.canva.com | Good news alert!
19737cfb946748a7 | 2025-06-03 | wholesale@verano.com | NEW pricing 🚨
197368acc484ebfc | 2025-06-03 | hello@surfside.io | Last Chance: RSVP for Tomorrow's Livestream with Jaunty's Marketing Advisor
1973674a9810fa6d | 2025-06-03 | peter@heartlandpayments.ccsend.com | Credit Card Rate Review for CUZZIE'S LLC
197364fdedf5e0ae | 2025-06-03 | email@em.sherwin-williams.com | Introducing Minwax® Color Series Premium Oil-Based Stain
19735fc7e23d37b2 | 2025-06-03 | peter@heartlandpayments.ccsend.com | Would You Like World Class Payroll for 6 Months Free?
19732567874861f4 | 2025-06-02 | wholesale@verano.com | Flower, vapes, and gummy deals!
197323b7b0a5ed59 | 2025-06-02 | BestBuy@email.bestbuy.com | Solid choice! Now get ready to up your game.
197321e94d39a00a | 2025-06-02 | marketing@dutchie.com | Exclusive Invite: Dutchie 2.0 Summer '25 Release Webinar
1973210ea1277a99 | 2025-06-02 | jamie-nichenfe.com@shared1.ccsend.com | View Our Updated Excel Menu Now! 🔥🍃
197317baf14e8e40 | 2025-06-02 | support@qr-code.io | [Action required] Your deactivated QR code could have been scanned!
1973167b007d7f9b | 2025-06-02 | marc@necann.com | Let's Finish 2025 Strong — Join Us for the Final NECANN Conventions of the Year!
197313559af34acd | 2025-06-02 | info@blunacan.com | BLUNA: TYTE & TRAVEL TYTE: Better Inside and Out
197313239bd0aa18 | 2025-06-02 | andrew@northlake.supply | Updated Inventory: New Drops, Restocks & Fast Movers - Act Fast!
19730edb893933b4 | 2025-06-02 | flyers@webstaurantstore.com | Hot sale: stock up without stress
19730d670c9826dd | 2025-06-02 | marketing@engage.canva.com | Help us improve Canva Print for your business 🖨️
1973054d25394b92 | 2025-06-02 | Chris@little-leaf-labs.apextrading.com | Re-Stocked + New Vape Flavors!
197260512afb59a4 | 2025-05-31 | BestBuy@email.bestbuy.com | Bring home a new TV for less. Shop deals on select TVs.
1972209c73c8b2fd | 2025-05-30 | email@mail.salesforce.com | Savings extended — but not for long: Save $1,300
19721a771aa29a39 | 2025-05-30 | john@emeraldintel.ai | Emerald Intel Newsletter: Cannabis banking, June events, and more
1971df5a9259034a | 2025-05-29 | info@fernway.com | 🚨 New Fernway Flavor Dropping Next Week
1971d55febc3363d | 2025-05-29 | marketing@egrovesystems.com | NJEDA: Get a Free Website & Digital Marketing Help for Your NJ Business
1971d3e653730a4f | 2025-05-29 | email@mail.salesforce.com | Learn how to Turn Data Into Meaningful Customer Moments
1971d2b7489d6bf8 | 2025-05-29 | salexander-vhrrental.com@voorheeshardware.ccsend.com | June Specials
1971d217f1d78b2a | 2025-05-29 | info@everonsolutions.com | Everon Insights: May 2025
1971c79cad32b0ac | 2025-05-29 | jamie-nichenfe.com@shared1.ccsend.com | New Excel Menu Available! 🔥🍃
1971c5792f457202 | 2025-05-29 | stephanie@logikpayments.com | Debit Solution - Competitive Commission
1971beac459397e5 | 2025-05-29 | sales@budvue.com | Cannabis Surge & AI Retail Wins
19718971678ca102 | 2025-05-28 | wholesale@verano.com | Restocked! Re: 40%?!?!
1971826d236c9a79 | 2025-05-28 | hello@flowhub.com | Coming soon: a better way to sell cannabis online
19717cbe0d41c9f8 | 2025-05-28 | jsciortino@naidb.com | UNIQUE USER-INVESTOR OPPORTUNITY
19717a43124f324b | 2025-05-28 | marketing@engage.canva.com | Make your social content shine
197176eb0749f51c | 2025-05-28 | 2115@fastsigns.com | Turn Heads Toward Your Business | FASTSIGNS
197176e070b5dd46 | 2025-05-28 | hello@surfside.io | Register Now: Livestream with Jaunty Marketing Advisor Drew Cesario
1971751d50f01185 | 2025-05-28 | flyers@webstaurantstore.com | It's Back: The 24-Hour Clear-Out
1971706b4cf16b30 | 2025-05-28 | brittanie@thrivepop.com | Live Event Today: Your CTA Sucks (Let's Fix It)
197139176d3af233 | 2025-05-27 | marketing@engage.canva.com | Your flyer is almost ready for delivery
19712a90c7d297e8 | 2025-05-27 | sales@hamiltonfarms.com | Hamilton Farm's Menu & Glass Jar Release (limited stock)
1971219a1c2d465a | 2025-05-27 | jamie-nichenfe.com@shared1.ccsend.com | New Excel Menu Available! 🔥🍃
197113dc2b4eabbf | 2025-05-27 | email@em.sherwin-williams.com | Amazing offers can be found right here...
1970d658af6f511d | 2025-05-26 | andrew@northlake.supply | High-Testing Prerolls In Stock
19701f50864108b9 | 2025-05-24 | BestBuy@email.bestbuy.com | See what we can offer YOU... Come this way for huge savings on great tech 💸
196fdae5435753ec | 2025-05-23 | andrew@northlake.supply | Honoring Memorial Day – Thank You from North Lake Supply 🇺🇸
196fd99aaef1bcce | 2025-05-23 | jamie-nichenfe.com@shared1.ccsend.com | New Excel Menu Available! 🔥🍃
196f9aa14b7d2064 | 2025-05-22 | info@fernway.com | Show Some Love to Our New Partners
196f988e85765038 | 2025-05-22 | jamie-nichenfe.com@shared1.ccsend.com | Help Us Understand Your In-Store Marketing Options 🍃
196f930c30032978 | 2025-05-22 | email@mail.salesforce.com | Supercharge your Salesforce integration: discover the top 5 patterns
196f8e6ec1f638ad | 2025-05-22 | email@mail.salesforce.com | One week left to save big and get perks.
196f88f785ba4d41 | 2025-05-22 | jamie-nichenfe.com@shared1.ccsend.com | New Excel Menu Available! 🔥🍃
196f854a4ae71b6f | 2025-05-22 | email@em.sherwin-williams.com | NEW in the PPC Spring Issue
196f7df51496e478 | 2025-05-22 | BestBuy@email.bestbuy.com | We like all things tech! Get ready for excellent savings on TVs.
196f7de60d27d273 | 2025-05-22 | sales@budvue.com | Boost Sales with AI and Premium Cannabis
196f4c1ee7453769 | 2025-05-21 | wholesale@verano.com | Breakfast time! 38.73%
196f46f988fa6f54 | 2025-05-21 | BestBuy@email.bestbuy.com | ❇ Lemar, enjoy your recent purchase.
196f43b3c69c55a9 | 2025-05-21 | noreply@aiq.com | Say hello to faster, smarter support at AIQ
196f415e2aaa7c66 | 2025-05-21 | BestBuy@email.bestbuy.com | Memorial Day Sale: Save big on major appliances and more
196f395798cb1840 | 2025-05-21 | noreply@mail.lendistry.com | News & Resources for Small Businesses
196ef647c58e0466 | 2025-05-20 | wholesale@verano.com | Spice🌶️ up your high!
196ef281bd2b480c | 2025-05-20 | Chris@little-leaf-labs.apextrading.com | Growfather & Moonrock NEW PROUCTS
196eeffc30f3b94c | 2025-05-20 | brittanie@thrivepop.com | Stop Losing Clicks, Start With This
196ee3bd516eca06 | 2025-05-20 | email@em.sherwin-williams.com | There's so much to see at Sherwin-Williams
196edf40714539ef | 2025-05-20 | marc@necann.com | Close Out 2025 Strong with NECANN Miami, New Jersey & New York!
196ea6ca3d8a1a09 | 2025-05-19 | marketing@egrovesystems.com | NJEDA: Get a Free Website & Digital Marketing Help for Your NJ Business
196ea3b18b04b3d2 | 2025-05-19 | BestBuy@email.bestbuy.com | Memorial Day Sale starts today!
196e9c8b3c7e043b | 2025-05-19 | info@affordablesweepingservices.com | From Dirt to Done – Professional Sweeping & Rentals That Work for You
196e93f6661f59c4 | 2025-05-19 | jamie-nichenfe.com@shared1.ccsend.com | New Excel Menu Available! 🔥🍃
196e868bf337949a | 2025-05-19 | andrew@northlake.supply | Stock Up for Memorial Day – Free NLS Hats + Fresh Drops Inside
196df7410aa80ec5 | 2025-05-17 | BestBuy@email.bestbuy.com | Clearance deals are here. Shop the Best Buy Outlet today.
196df23de06dddbd | 2025-05-17 | marketing@engage.canva.com | Every format... Now in one design?! 🤯
196d9eeb751488fd | 2025-05-16 | wholesale@verano.com | Last chance!
196d99cc9d531fde | 2025-05-16 | BestBuy@email.bestbuy.com | Lemar, review your purchase and get a $5.00 reward certificate.
196d98f7d06ff7ca | 2025-05-16 | marketing@emeraldintel.ai | Lemar We have your next trade show target list
196d988455131115 | 2025-05-16 | jamie-nichenfe.com@shared1.ccsend.com | New Excel Menu Available! 🔥🍃
196d59e7f4f65add | 2025-05-15 | info@fernway.com | 🔜 New Fernway Loading... Take a Look!
196d526a5fec4ffa | 2025-05-15 | email@mail.salesforce.com | Accelerate Sales Growth with AI, Data & CRM
196d254026d6d027 | 2025-05-15 | noreply@redditmail.com | "I love New Jersey but not this much. . ."
196d0155e389d13a | 2025-05-14 | BestBuy@email.bestbuy.com | ** Hold up ** Wanna see some top offers?
196cf9c2417afc4d | 2025-05-14 | jamie-nichenfe.com@shared1.ccsend.com | New Excel Menu Available! 🔥🍃
196cf89cc2283be5 | 2025-05-14 | olivia-rpconsultingnj.com@shared1.ccsend.com | Join Mayor Vic Carstarphen & the Camden Strong Team
196cf88ce31fb1b5 | 2025-05-14 | emily.nathanson@urban-gro.com | Supporting Extraction and Processing with urban-gro
196cf74f066626f8 | 2025-05-14 | brittanie@thrivepop.com | One Small Tweak = Way More Conversions
196cf58dd6a06c12 | 2025-05-14 | 2115@fastsigns.com | Elevate the Fan Experience with Custom Signs | FASTSIGNS
196ceda5e4c6301b | 2025-05-14 | HomeDepotCustomerCare@mg.homedepot.com | You recently bought Hampton Bay... Tell us about it!
196cad1a1d5d654a | 2025-05-13 | marketing@egrovesystems.com | NJEDA: Get a Free Website & Digital Marketing Help for Your NJ Business
196ca86d1e55a116 | 2025-05-13 | marketing@engage.canva.com | Every format... Now in one design?! 🤯
196ca5e5d406ffb4 | 2025-05-13 | email@mail.salesforce.com | Just $999 to attend. Register now.
196ca2f6e6819d72 | 2025-05-13 | email@em.sherwin-williams.com | Your $100 purchase online & on the PRO app comes with $20 off
196c92806f302e60 | 2025-05-13 | BestBuy@email.bestbuy.com | Save up to $700 on select MacBook Pro
196c556850cedfe2 | 2025-05-12 | events@send.zapier.com | You're missing out! Register now to see AI workflows in action.
196c5561f9ca5f35 | 2025-05-12 | support@qr-code.io | [Important] Your free trial and QR codes will expire in 1 day!
196c4ae9c53106f8 | 2025-05-12 | andrew@northlake.supply | North Lake Supply - Weekly Menu ReSend
196c4a4edf613213 | 2025-05-12 | andrew@northlake.supply | New Product Launch – 2g Caramel Dream Vapes, Sour Melon 10-pks & More
196c42df85b7a976 | 2025-05-12 | BestBuy@email.bestbuy.com | Hello there... These offers are only here for a limited time. ⌛
196c0e47df812efc | 2025-05-11 | BestBuy@email.bestbuy.com | These savings are a big deal. Shop Best Buy's Top Deals today.
196bab58068d5738 | 2025-05-10 | BestBuy@email.bestbuy.com | Happy Saturday! Get TVs for as low as $69.99
196b6becbb8f3359 | 2025-05-09 | maggie.boyd@verano.com | Verano Marketing Newsletter - April
196b1bd7f02d162a | 2025-05-08 | MicrosoftRewards@customermail.microsoft.com | Is this your LUCKY week? See how you could be a $10K winner
196b19979e45e128 | 2025-05-08 | info@fernway.com | 🌿 Blue Mirage: New Strain in Stores Now!
196b148ae7dba410 | 2025-05-08 | hello@flowhub.com | How Nova Farms Runs 6 High-Volume Stores as a Vertically Integrated MSO
196b1192d737176b | 2025-05-08 | email@mail.salesforce.com | Power your productivity with tips from these 9 Slack success stories
196b06efc878080a | 2025-05-08 | marketing@engage.canva.com | Monthly Glow Up: Organize your ideas in just 5 minutes
196b02768924f1e1 | 2025-05-08 | marketing@emeraldintel.ai | Lemar Tackle CRM Data Decay With Emerald Intel
196aba2a5f2b5848 | 2025-05-07 | salexander-vhrrental.com@voorheeshardware.ccsend.com | May Specials!
196ab7eb939e3651 | 2025-05-07 | jessica@rpconsultingllc.ccsend.com | Join Mayor Vic Carstarphen & the Camden Strong Team
196ab5c4c265a3a5 | 2025-05-07 | homedepotpro@mg.homedepot.com | Your April 2025 Pro Xtra Statement is Here
196ab13f19346ca1 | 2025-05-07 | marketing@engage.canva.com | Don't miss out on the latest from Canva Create!
196aad1070f374a1 | 2025-05-07 | HomeDepotCustomerCare@mg.homedepot.com | You recently bought Hampton Bay... Tell us about it!
196a741a6b31914a | 2025-05-06 | BestBuy@email.bestbuy.com | Lemar, tell us about your experience.
196a608c763977d9 | 2025-05-06 | hello@surfside.io | Last Chance: RSVP for Tomorrow's Livestream with Mitten Extracts' CMO
196a18b5fb8465d2 | 2025-05-05 | andrew@northlake.supply | NJ's First Preroll Variety Pack Has Landed - Now Available!
196a0d91139f78a6 | 2025-05-05 | sales@hamiltonfarms.com | Hamilton Farm's Weekly Menu & Thanks
196a0cd2891f8423 | 2025-05-05 | marketing@engage.canva.com | Don't miss out on the latest from Canva Create!
196a0b56ba406743 | 2025-05-05 | flyers@webstaurantstore.com | Sweet deals to flavor up your week.
196a0a7047648a64 | 2025-05-05 | Microsoft@customersfeedback.microsoft.com | Give Feedback for Windows 11!
196980111ee230b7 | 2025-05-03 | BestBuy@email.bestbuy.com | Hi there - TVs as low as $69.99 is an amazing DEAL... 💰
196919ee885150f9 | 2025-05-02 | wholesale@verano.com | Preorder available!
196918eee2a18048 | 2025-05-02 | jamie-nichenfe.com@shared1.ccsend.com | Dont Miss Out: New Strain! 🔥🍃
1968dfb781f52e66 | 2025-05-01 | info@fernway.com | 🤔 Secure Your Sneak Peek of the New Flavor
1968d8b14b20ba27 | 2025-05-01 | wholesale@verano.com | Check out these strains!
1968d56930601adb | 2025-05-01 | andrew@northlake.supply | New Cartridges Just Landed + Free Preroll Promo & Final Trim Drop!
1968d4e7f6f7f5ce | 2025-05-01 | john@emeraldintel.ai | Emerald Intel Newsletter: Get more out of cannabis trade shows
1968d0d0e79775b8 | 2025-05-01 | email@mail.salesforce.com | 22 ways to automate your most tedious tasks, all in Slack
1968d05685f80973 | 2025-05-01 | HomeDepotCustomerCare@mg.homedepot.com | Reminder: The Home Depot would love your feedback! 3-minute survey
1968c3aad796610b | 2025-05-01 | email@em.sherwin-williams.com | NEW! ScotchBlue™ PROSharp™ Advanced Multi-Surface Painter's Tape
1968bb8f08560e06 | 2025-05-01 | sales@budvue.com | Boost Sales Despite Price Drops
19687e59fd8354cf | 2025-04-30 | googleworkspace-noreply@google.com | Reminder: You have a $500 Google Ads credit offer
196878ba0b8f7623 | 2025-04-30 | jsciortino@naidb.com | UNIQUE USER-INVESTOR OPPORTUNITY
196876aae84cf9ad | 2025-04-30 | marketing@emeraldintel.ai | Let's Make Some Noise for Cannabis Reform — Join Us in D.C.!
19687633f8b2c343 | 2025-04-30 | 2115@fastsigns.com | Refresh Your Space with Captivating Custom Visuals | FASTSIGNS
196875807eda3e03 | 2025-04-30 | flyers@webstaurantstore.com | Don't Miss Out. End of Month Savings.
1968705b3597722b | 2025-04-30 | jamie-nichenfe.com@shared1.ccsend.com | Dont Miss Out: New Pre Rolls Available! 🔥🍃
1968703880957bc7 | 2025-04-30 | hello@surfside.io | Register Today: Livestream with Mitten CMO Trent McCurren
19686d14a2bda56f | 2025-04-30 | HomeDepotCustomerCare@mg.homedepot.com | You recently bought Everbilt Standard Toilet Wax Ring. Tell us about it!
1968288e4bd3dac5 | 2025-04-29 | marketing@egrovesystems.com | NJEDA's program for FREE eCommerce Development & Digital Marketing!
196823d79e44dd45 | 2025-04-29 | email@mail.salesforce.com | Dreamforce registration opens soon. Are you ready?
19681b03a9b7b535 | 2025-04-29 | matthewmatey@worldinsurance.com | Reminder: Join Us May 8 for Insights on Prescription Benefits
1967e008ff3e8faa | 2025-04-28 | jamie-nichenfe.com@shared1.ccsend.com | Dont Miss Out: New Pre Rolls Available! 🔥🍃
1967de495acd5fbd | 2025-04-28 | HomeDepotCustomerCare@mg.homedepot.com | The Home Depot requests your feedback.
1967d3c8f9d38b53 | 2025-04-28 | salexander-vhrrental.com@voorheeshardware.ccsend.com | Thank You Very Mulch!
1967d24fde3fde1a | 2025-04-28 | jessica@rpconsultingllc.ccsend.com | Join Mayor Vic Carstarphen & the Camden Strong Team
1967c6b7d8ba20c4 | 2025-04-28 | sales@hamiltonfarms.com | Hamilton Farm's Weekly Menu & MJ Unpacked
19673a8deab21754 | 2025-04-26 | BestBuy@email.bestbuy.com | Limited time: Save up to 50% on clearance and open-box items
19672e3d860e3ea5 | 2025-04-26 | canvacreate@engage.canva.com | Missed it live? Watch Canva Create sessions here.
1966ecdfb18413b7 | 2025-04-25 | wholesale@verano.com | Live Resin - Preorder now!
196699b9267428aa | 2025-04-24 | info@fernway.com | 💐 Infinite Vibes. (Plus, New Strain Alert!)
1966954f7458e354 | 2025-04-24 | companyinsights@risk-strategies.com | Stay Informed: Risk Strategies State of the Insurance Market Report
19669046414e6412 | 2025-04-24 | email@mail.salesforce.com | IDC MarketScape Names Slack a Leader in Worldwide Team Collaboration
19668958d4447c07 | 2025-04-24 | canvacreate@engage.canva.com | Missed it live? Watch Canva Create sessions here.
1966481f0ce6bcbe | 2025-04-23 | wholesale@verano.com | PRODUCT DROP 🏃‍♂️💭
1966397c794ca5df | 2025-04-23 | justin.goods@flowhub.com | Will you be at MJ Unpacked in Atlantic City next week?
```

## Sources
- gmail: lemar@cuzziesnj.com inbox — PART A sweep (`in:inbox` vendor-domain + menu-signal + attachment/link combination) and PART B sweep (`older_than:1y (category:promotions OR category:social OR category:forums) in:inbox`), executed 2026-07-16 via the Basil inbox-janitor routine (`.claude/routines/inbox-janitor.md`).
