---
created: 2026-07-26T23:07:00-04:00
updated: 2026-07-26T23:07:00-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail, housekeeping]
source: claude
---

# Basil — Inbox Janitor nightly run — 2026-07-26

Mode: **LIVE** (`DRY_RUN=false`). Account acted on: `lemar@cuzziesnj.com` (connected Gmail,
business account). Full runbook: `.claude/routines/inbox-janitor.md`.

## Summary

- **PART A — vendor menus:** archived 10 threads out of the inbox into the `Vendor Menus`
  label (`Label_8`). All were bulk marketing/menu-drop mail from the vendor-domain seed
  list (novafarms.com, jerseysmooth.com, kivaconfections.com, verano.com, northlake.supply,
  apextrading.com, terrascend.com). No thread carrying an `IMPORTANT`/`STARRED` flag was
  touched, even when the sender domain matched — the safety floor applies across every
  PART, not just the trash sweep.
- **PART B — trash sweep:** trashed **84** threads older than 12 months in
  `category:promotions/social/forums`. None were starred, important, allowlisted, or
  carried a genuine filing label. Recoverable in Gmail Trash for 30 days.
- **Skipped from the trash sweep (protected):** 7 threads from `parkebank.com`
  (NEVER-TOUCH allowlist), 7 threads from `CTA@sos.nj.gov` (`*.gov` allowlist), and 2
  threads that carried at least one `IMPORTANT`-flagged message in the thread (a Dutchie
  implementation-survey thread and a Hamilton Farms weekly-menu thread that turned into a
  live order-terms conversation).
- **`category:updates` — report-only, not touched** (per runbook; this category mixes
  invoices/bank/payroll with ordinary marketing, too dangerous to sweep). ~201 threads
  older than 1y estimated in this category. Sample sender domains Lemar may want to
  hand-clear: `nytimes.com` (breaking-news alerts), `google.com` (Voice missed-call
  notices — security alerts from this domain are separately allowlisted/protected
  regardless), `jotformsign.com`/`jotform.com` (e-sign receipts), `trustaltus.com`,
  `redditmail.com`, `slack.com`, `distru.com`, `theathletic.com`, `cannazipbags.com`,
  `everonsolutions.com`. Actual invoice/bank/payroll/legal mail in this category
  (`intuit.com`, `docusign.net`, `headset.io`) is on the NEVER-TOUCH allowlist and was
  left alone.
- **Per-run cap** (200 trash/night) not reached — 84 of an estimated ~201
  promotions/social/forums candidates processed this run. Basil runs incrementally, not
  exhaustively, each night, so the remainder is expected to surface again on a future run.

## Vendor-menu threads archived (PART A)

| Thread ID | Subject | Sender |
|---|---|---|
| 19f953b3c8de3e97 | Stashie: Frieday Update, Farm day details | bbreslow@novafarms.com |
| 19f94ea1e0038b2d | ⏳ Weekend Loading... | alex@jerseysmooth.com |
| 19f94bf6757d74f2 | ***LAST CALL ON B2G1 CAMINO AND B1G1 LOST FARM... | dan.grandrino@kivaconfections.com |
| 19f90ff6d7bcec23 | Pods on Pods on Pods! | maggie.boyd@verano.com |
| 19f90c37a1f0d5cd | ORDER NIMBUS ICON AND LIVE TERPS FOR $20/UNIT!! | dan@northlake.supply |
| 19f8a96c174592ed | Do you know what day it is? | alex@jerseysmooth.com |
| 19f8a1933fdd5f39 | Launch Alert: DANK 510 Carts Are Here | Matt@little-leaf-labs.apextrading.com |
| 19f80d2395806595 | Stashie Scoop: Lock In Your July Orders | bbreslow@novafarms.com |
| 19f80a8a5d368777 | Throwback Flavors / Faster Effects | marketing.us@terrascend.com |
| 19f8073dc96a2648 | Tell a friend, Guess Who's Back (Back Again) | alex@jerseysmooth.com |

## Trash audit (PART B — full recovery list, 30-day Trash window)

| # | Thread ID | Subject | Sender | Date |
|---|---|---|---|---|
| 1 | 1984362d4c517300 | Reminder - Brief survey on your ADT alarm monitoring experience | adt@express.sea1.medallia.com | 2025-07-25 |
| 2 | 198422c4f7ab3902 | EXCLUSIVE: Millville, NJ Opening Soon for Dispensary Licenses | Julian@cd.cdre.co | 2025-07-25 |
| 3 | 19841e8f400110d2 | Webinar Reminder_July 31st | jonathon@hoodieanalytics.com | 2025-07-25 |
| 4 | 192b9744f0d7e332 | You recently bought Southwire... | HomeDepotCustomerCare@mg.homedepot.com | 2024-10-23 |
| 5 | 192b666e4c26c232 | Professional Networking Starts With dot.Profile+ | update@dotcards.net | 2024-10-22 |
| 6 | 192b55600c418507 | Calling all retail professionals | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-22 |
| 7 | 192b4bf16b319c6b | Small Business Programs Available Now | main-palmestatesco.com@shared1.ccsend.com | 2024-10-22 |
| 8 | 192b45f633863941 | Exclusive-Harris holds 46%-43%... | microsoft.start@email2.microsoft.com | 2024-10-22 |
| 9 | 192b4104bdb07d45 | In Case You Missed It: US Virgin Islands... | michelle-thinkcanna.com@cannaadvisors.ccsend.com | 2024-10-22 |
| 10 | 192b0095866fe29a | New betas, new features... | mail@email.adobe.com | 2024-10-21 |
| 11 | 192af571b4ca187b | NEW Select RSO X-Bites | marketing@leaftrade.com | 2024-10-21 |
| 12 | 192af3eb18649675 | Election 2024 live updates... | microsoft.start@email2.microsoft.com | 2024-10-21 |
| 13 | 192aa122cbcc4787 | Barack Obama targets... | microsoft.start@email2.microsoft.com | 2024-10-20 |
| 14 | 192a4e93c07fb7a3 | Killing Sinwar... | microsoft.start@email2.microsoft.com | 2024-10-19 |
| 15 | 192a17b25d5e5874 | Step-by-Step: Customize Your Metal dot.card... | update@dotcards.net | 2024-10-18 |
| 16 | 192a12f8126d4a78 | Calling all retail professionals | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-18 |
| 17 | 192a11a49810fe94 | New Fernway Partners Dropped. | info@fernway.com | 2024-10-18 |
| 18 | 192a0e7d5a306ba6 | Shop with confidence this holiday | Microsoftstore@microsoftstore.microsoft.com | 2024-10-18 |
| 19 | 1929ff0a7ad40aaa | Your Business may be eligible for the SBA Express Program | main-palmestatesco.com@shared1.ccsend.com | 2024-10-18 |
| 20 | 1929fd995df83d8b | Delivered Digest: Amazon Pharmacy... | news@onfleet.com | 2024-10-18 |
| 21 | 1929fc44d28feebd | Hamas Chief Yahya Sinwar Killed... | microsoft.start@email2.microsoft.com | 2024-10-18 |
| 22 | 1929fadd01d784bc | HELP HIBERNATE YOUR LAWN | salexander-vhrrental.com@voorheeshardware.ccsend.com | 2024-10-18 |
| 23 | 1929bfc24f0729e1 | TreezPay Webinar... | marketing@treez.io | 2024-10-17 |
| 24 | 1929bc687a413030 | You've got until 10/24... | email@em.sherwin-williams.com | 2024-10-17 |
| 25 | 1929ba87b22417ac | Top Tricks & Treats for Retailers | dayna@covasoftware.com | 2024-10-17 |
| 26 | 1929b7bfe5b13f93 | Time to Switch Payroll? | peter@heartlandpayments.ccsend.com | 2024-10-17 |
| 27 | 1929b430d59844d2 | Secure, integrated cashless payments... | marketing@dutchie.com | 2024-10-17 |
| 28 | 1929aaed3f94cd0f | Capture the best ideas with whiteboards | marketing@engage.canva.com | 2024-10-17 |
| 29 | 1929a9f3e2786a3c | Harris steps out... | microsoft.start@email2.microsoft.com | 2024-10-17 |
| 30 | 1929a9e228262541 | What should be in my tech stack? | marketing@treez.io | 2024-10-17 |
| 31 | 1929686e893f8625 | Discover new ways of working, with Slack | email@mail.salesforce.com | 2024-10-16 |
| 32 | 1929685e8ba418fa | Your productivity is about to skyrocket | mail@email.adobe.com | 2024-10-16 |
| 33 | 1929663f4d07af31 | See why Fortune 500 companies... | update@dotcards.net | 2024-10-16 |
| 34 | 192961516fdf739f | Retail Insider: October 2024 Edition | marketing@leaflink.com | 2024-10-16 |
| 35 | 19295a529c2f00ec | Last Chance: RSVP for Tomorrow's Webinar with Bryan Benavides | hello@surfside.io | 2024-10-16 |
| 36 | 192957ac586808de | Harris to court Republican voters... | microsoft.start@email2.microsoft.com | 2024-10-16 |
| 37 | 19290b55b830e6aa | New Photoshop features... | mail@mail.adobe.com | 2024-10-15 |
| 38 | 192907b11470a4f9 | Your Business may be eligible for the SBA Express Program | main-palmestatesco.com@shared1.ccsend.com | 2024-10-15 |
| 39 | 19290524d2a6f93d | Walz to unveil Harris' plan... | microsoft.start@email2.microsoft.com | 2024-10-15 |
| 40 | 19290113a8c74d90 | [Last chance at Office Hours!]... | team@m.ngrok.com | 2024-10-15 |
| 41 | 1928d0544f9c45fc | Connect Smarter — Try dot.Profile Plus | update@dotcards.net | 2024-10-14 |
| 42 | 1928cc712af9449b | Type your Zap idea + watch AI create it! | learn@send.zapier.com | 2024-10-14 |
| 43 | 1928cb58988b04ed | Calling all retail professionals | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-14 |
| 44 | 1928c36f7409c301 | Industry Updates and More! | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-14 |
| 45 | 1928bd1dcac698dc | Lemar, we want to buy your vehicle. | easyautopa@alstspecials.com | 2024-10-14 |
| 46 | 1928b357a2f207e2 | Election 2024 live updates... | microsoft.start@email2.microsoft.com | 2024-10-14 |
| 47 | 1928852db8233b9f | Unlock Canva's premium features | start@engage.canva.com | 2024-10-13 |
| 48 | 19286065cd7d4b00 | Biden to announce over $600M... | microsoft.start@email2.microsoft.com | 2024-10-13 |
| 49 | 19281bfc74a0d239 | Crop images for better composition | marketing@engage.canva.com | 2024-10-12 |
| 50 | 1928190cfee5f0ef | Thanks for getting Cova nominated for an Emjay!... | dayna@covasoftware.com | 2024-10-12 |
| 51 | 1927cf5c4fee931c | Invites you to join him in support of the Camden City Democrats... | jessica@rpconsultingllc.ccsend.com | 2024-10-11 |
| 52 | 1927be763496e3bc | Your Business may be eligible for the SBA Express Program | main-palmestatesco.com@shared1.ccsend.com | 2024-10-11 |
| 53 | 1927bcc46835f06e | Delivered Digest: Hurricane Milton's Impact... | news@onfleet.com | 2024-10-11 |
| 54 | 1927bbbb0a508868 | Hurricane Milton tracker... | microsoft.start@email2.microsoft.com | 2024-10-11 |
| 55 | 19276d16631b432b | NEW in the PPC Fall Issue... | email@em.sherwin-williams.com | 2024-10-10 |
| 56 | 19276bd5a40452d4 | RSVP Today: Learn How to Scale Your Cannabis Business | hello@surfside.io | 2024-10-10 |
| 57 | 19276b628cffdcee | [Ask ngrok anything!]... | team@m.ngrok.com | 2024-10-10 |
| 58 | 19276924fc5b0248 | Hurricane Milton live updates... | microsoft.start@email2.microsoft.com | 2024-10-10 |
| 59 | 19272b6bae4abde5 | Declassified Details: The Cannabis Royale MJBizCon After-Party | dayna@covasoftware.com | 2024-10-09 |
| 60 | 19272a1a6db3c9c4 | New personalization features boost retention and sales | marketing@dutchie.com | 2024-10-09 |
| 61 | 1927293bd6580fc1 | NJEDA's free program for eCommerce Development... | njedasupport@egrovesys.com | 2024-10-09 |
| 62 | 192728e8656f53df | NEW: Custom Metal dot.cards—Precision Meets Power | update@dotcards.net | 2024-10-09 |
| 63 | 19271d7c2cad7b7f | Discover the Secrets to Retail Success \| FASTSIGNS | 2115@fastsigns.com | 2024-10-09 |
| 64 | 19271b8853faa542 | Discover Agentforce... | email@mail.salesforce.com | 2024-10-09 |
| 65 | 192717302d476a80 | Nobel Prize in chemistry... | microsoft.start@email2.microsoft.com | 2024-10-09 |
| 66 | 192715a8f9e29ff8 | Last chance to register! | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-09 |
| 67 | 19271273eb702d8b | Unlock the secret to engaging presentations | marketing@engage.canva.com | 2024-10-09 |
| 68 | 1926d5348ca168e1 | New AI trends emerging among sales professionals | email@mail.salesforce.com | 2024-10-08 |
| 69 | 1926cddc59903e0e | Reminder to join tomorrow's kiosk training! | hello@flowhub.com | 2024-10-08 |
| 70 | 1926cb1ce8dda04e | Your September 2024 Pro Xtra Statement is Here | homedepotpro@mg.homedepot.com | 2024-10-08 |
| 71 | 1926cafb579f4287 | Calling All Retail Professionals | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-08 |
| 72 | 1926c82c5e21cee5 | Win With Premium is Ending Soon! | email@em.sherwin-williams.com | 2024-10-08 |
| 73 | 1926c80d9a1df511 | Your Business may be eligible for the SBA Express Program | main-palmestatesco.com@shared1.ccsend.com | 2024-10-08 |
| 74 | 1926c5163386cf33 | 'Godfather of AI' shares Nobel Prize... | microsoft.start@email2.microsoft.com | 2024-10-08 |
| 75 | 1926c00f70ef738b | Great work on your first presentation! | marketing@engage.canva.com | 2024-10-08 |
| 76 | 19269867da7c55a2 | Preserve your favorite recipes with Microsoft 365 | Microsoft365@engagement.microsoft.com | 2024-10-08 |
| 77 | 19268e3f20e63f54 | OpenAI 1o-mini and o1-preview are now available! | updates@send.zapier.com | 2024-10-07 |
| 78 | 19267f7f309b782f | Discover the building blocks of design | mail@email.adobe.com | 2024-10-07 |
| 79 | 19267823f9518472 | A Briq to take you back to the shore | marketing@leaftrade.com | 2024-10-07 |
| 80 | 1926781292e895bf | Bad. Ass. Kiosk. Experience. | hello@flowhub.com | 2024-10-07 |
| 81 | 1926763b01ef67f8 | Calling All Retail Professionals | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-07 |
| 82 | 192672012e0679a3 | Hamas Fires Rockets at Tel Aviv... | microsoft.start@email2.microsoft.com | 2024-10-07 |
| 83 | 19261f711da9c6a1 | Israel-Gaza-Lebanon updates... | microsoft.start@email2.microsoft.com | 2024-10-06 |
| 84 | 1925ea18a4992e76 | Calling All Retail Professionals | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-05 |

## Sources
- gmail: 94 threads actioned (10 labeled/archived, 84 trashed) on `lemar@cuzziesnj.com`, see tables above for full thread-ID audit trail
- claude: Basil nightly routine run, `.claude/routines/inbox-janitor.md`, 2026-07-26
