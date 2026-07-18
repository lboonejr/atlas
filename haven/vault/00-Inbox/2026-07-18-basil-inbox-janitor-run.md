---
created: 2026-07-18T23:07-04:00
updated: 2026-07-18T23:07-04:00
domain: cuzzies
type: log
status: done
tags: [basil, inbox-janitor, gmail, cleanup]
source: claude
---

# Basil — Inbox Janitor nightly run — 2026-07-18

Basil ran live (`DRY_RUN=false`) against the connected Gmail account `lemar@cuzziesnj.com`,
per `.claude/routines/inbox-janitor.md`. Per-run cap (200 trashed/run) was not hit.

## PART A — Vendor menus archived (8)

Labeled `Vendor Menus` (`Label_8`) + removed `INBOX`. All had explicit "menu attached/live"
language from vendor-seed domains, none starred/important:

1. `19f71bf2b92d4bef` — bbreslow@novafarms.com — "Stashie Claus? Promo Continues" (2026-07-17)
2. `19f70feb66be694d` — Kathy@freshcannabis.co — "Fresh Grow Menu | Limited-Time Sale..." (2026-07-17)
3. `19f70c219e07bdf2` — allanf@harvestmoonfarmsnj.com — "Friday Menu Update – Last Call Before the Weekend" (2026-07-17)
4. `19f7062c2b63b89d` — nbonsanto@awholdings.com — "Ascend Menu | Ounces Taking Over + Fresh Weekend Drops" (2026-07-17)
5. `19f6b6eb13ac15f5` — carlos.gamez@kivaconfections.com — "Kiva Camino B3GO ALL SKUS & BOGO LOST FARM ALL SKUS OFFER" (2026-07-16)
6. `19e45817ba0db46a` — nbonsanto@awholdings.com — "LAST CHANCE!! GET ORDER IN BEFORE 1PM TODAY" (2026-05-20)
7. `19e47058da054e8f` — Kathy@freshcannabis.co — "Fresh Reserve Drop + Memorial Day Specials!" (2026-05-20)
8. `19e217b2ff92c278` — nbonsanto@awholdings.com — "LAST CALL FOR DELIVERY BEFORE THE WEEKEND!" (2026-05-13)

Many more vendor-domain threads exist in the inbox (novafarms, jerseysmooth, thegardensociety,
harvestmoonfarmsnj, apextrading subdomains, etc.) but were skipped this run — either the menu
signal was too weak (general marketing/event/payment threads, not an actual menu) or the thread
was marked IMPORTANT/STARRED, and PART A erred conservative. Left for a future run to reassess.

## PART B — Trash sweep (69 threads)

All older than 12 months, `category:promotions/social/forums`, none important/starred, sender
not on the NEVER-TOUCH allowlist. Applied `TRASH` (recoverable in Gmail Trash for 30 days from
2026-07-18). Full audit — thread ID · subject · sender · date:

1. `1981a592e592c10d` · Gummies and Carts specials! · wholesale@verano.com · 2025-07-17
2. `19819637325bd10c` · You've never mellowed like this 🍒🍃 COMING SOON · marketing.us@terrascend.com · 2025-07-17
3. `19818b95a9c0dfab` · The best product locator available · jonathon@hoodieanalytics.com · 2025-07-17
4. `19818b3f161c2b3f` · $150 OFF Your Next Purchase! · email@em.sherwin-williams.com · 2025-07-17
5. `19818ab068d02ef6` · Get today's dose of deals! · flyers@webstaurantstore.com · 2025-07-17
6. `195f2ddd7f6a2e01` · Get your ID scanning ready for 4/20 · jkossman@idscan.net · 2025-04-01
7. `195f28ddbfc30f67` · Seeking better tools for your sales team? · email@mail.salesforce.com · 2025-04-01
8. `195f1df88307cb6a` · Introducing ScotchBlue PROSharp Tape · email@em.sherwin-williams.com · 2025-04-01
9. `195f19077322f288` · Last Chance: RSVP Livestream w/ Wyld · hello@surfside.io · 2025-04-01
10. `195f171def7e9e2b` · Empower your team: Invite to WorkCanvas · team@workcanvas.com · 2025-04-01
11. `195f13c11613adef` · LEAKED: The Fernway Files · info@fernway.com · 2025-04-01
12. `195ee2b03413cc4f` · Double Bubble 🫧 · wholesale@verano.com · 2025-03-31
13. `195edaa971c574d3` · This isn't just any SALE... · BestBuy@email.bestbuy.com · 2025-03-31
14. `195ed23e9d9c010d` · North Lake Supply 4/20 Promos · andrew@northlake.supply · 2025-03-31
15. `195e9e34e978f9d2` · Growfather Discounts & New Product Releases! · Chris@little-leaf-labs.apextrading.com · 2025-03-31
16. `195e6f0d24b36bd1` · Today's the Day! PACC is Here! · marc@necann.com · 2025-03-30
17. `195e31ee3ded8aa3` · TVs as low as $69.99 · BestBuy@email.bestbuy.com · 2025-03-29
18. `195e28d87abfc147` · I just shot a video for you! · Dawid@driveeasyauto.com · 2025-03-29
19. `195ded9220a5415f` · On the Road to 4/20: Fern:20 Tour · info@fernway.com · 2025-03-28
20. `195dd14aa97210e6` · Reminder: USVI CannaPro Summit · michelle-thinkcanna.com@cannaadvisors.ccsend.com · 2025-03-28
21. `195d953732bdded6` · Get Your Keyword to the Top of Search Results · contact@elitesiteoptimizer.com · 2025-03-27
22. `195d8e542a6766c3` · Final Hours to Save on MJ Unpacked · jenna@newjerseycannabusinessassociation.ccsend.com · 2025-03-27
23. `195d88c45ed9d860` · Cannabis Retailers: 4/20 Survival Kit · chart@greencheckverified.com · 2025-03-27
24. `195d7fc72a8e8643` · Tips For A Successful 4/20 In Retail · kenneth.komarek@brinksinc.com · 2025-03-25
25. `195d7ee29767a7d9` · Register Today: Livestream w/ Wyld · hello@surfside.io · 2025-03-27
26. `195d7ea8795c0ab5` · Last Chance to Win a $100 eGift Card · email@em.sherwin-williams.com · 2025-03-27
27. `195d7bdb00354694` · Present your vision clearly ✨ · team@workcanvas.com · 2025-03-27
28. `195d45d38d0d4532` · 4/20 deals are HERE! · wholesale@verano.com · 2025-03-26
29. `195d3f05eba4e75b` · Kickstart your Presentation · marketing@engage.canva.com · 2025-03-26
30. `195d32ea9d904a65` · Ready to Explore Your Options? · Dawid@driveeasyauto.com · 2025-03-26
31. `195d2b6286cfaf4b` · UNIQUE USER-INVESTOR OPPORTUNITY · jsciortino@naidb.com · 2025-03-26
32. `195d292c1635c6c0` · Power up your Canvas with templates · team@workcanvas.com · 2025-03-26
33. `195ce2839cd0eca2` · Start New Payroll for Q2 · peter@heartlandpayments.ccsend.com · 2025-03-25
34. `195cdd583bc50a88` · It's time to change the way you email · research@emeraldintel.ai · 2025-03-25
35. `195cd6557d56e724` · Visualize your first workflow · team@workcanvas.com · 2025-03-25
36. `195ca11f87542997` · Introducing the Fernway SmartPack · info@fernway.com · 2025-03-24
37. `195c9bbd3a470efa` · NJEDA's free eCommerce program · njedasupport@egrovesys.com · 2025-03-24
38. `195c946651575431` · New Brand Alert + 4/20 Deals · andrew@northlake.supply · 2025-03-24
39. `195c8fc4b900e4ed` · AIQ earns top workplace recognition · noreply@aiq.com · 2025-03-24
40. `195c8bf9f5754f4c` · Hamilton Farm's Updated menu & 420 discussion · sales@hamiltonfarms.com · 2025-03-24
41. `195c85bbd5468909` · THANK YOU BOSTON! · marc@necann.com · 2025-03-24
42. `195bff2b6eaee0f2` · Massive OFFERS here... · BestBuy@email.bestbuy.com · 2025-03-22
43. `195ba14fd6cff456` · Check out our portal! · maggie.boyd@verano.com · 2025-03-21
44. `195b8b1ae5d2a757` · Today's the Day! NECANN Boston · marc@necann.com · 2025-03-21
45. `195b4c14feb3e27e` · See your 24/7 teammate: Agentforce · email@mail.salesforce.com · 2025-03-20
46. `195b49ee6bbc8e6e` · Create your Org Chart · team@workcanvas.com · 2025-03-20
47. `195b46533518dfcc` · Welcome to WorkCanvas! · team@workcanvas.com · 2025-03-20
48. `195b3de0041660e7` · Reminder: Chance to Win $100 eGift Card · email@em.sherwin-williams.com · 2025-03-20
49. `195b043055c42c98` · Guava is a go! · wholesale@verano.com · 2025-03-19
50. `195af65218c8b3b9` · One Week Till Deadline: Bid on 3 Locations · Julian@cd.cdre.co · 2025-03-19
51. `195af61d08be12cb` · Marketers, ready to seize AI advantage? · marketing@engage.canva.com · 2025-03-19
52. `195aef5f20d3e5b3` · Boost Your Brand's Impact with Signage · 2115@fastsigns.com · 2025-03-19
53. `195ab65e274e95be` · Click here to see something great · email@em.sherwin-williams.com · 2025-03-18
54. `195aa586fec357cf` · Unlock Exclusive Savings: $500 OFF Vehicle · Dawid@driveeasyauto.com · 2025-03-18
55. `195aa28897b647f8` · 4/20 Grow Book 2025 · sales@surfside.io · 2025-03-18
56. `195a9d6de4da6556` · KOTODO: New Eco-Friendly packaging · news@kotodocan.com · 2025-03-18
57. `195a9acd25c76ca4` · PACC x NECANN Partnership · marc@necann.com · 2025-03-18
58. `195a98e527024d3a` · Make 420 Count: Loyalty Program · hello@flowhub.com · 2025-03-18
59. `195a972e800c1d89` · Proven Step For A Successful 4/20 · kenneth.komarek@brinksinc.com · 2025-03-18
60. `195a968b7f6d4a75` · Counting down to our biggest launch · canvacreate@engage.canva.com · 2025-03-18
61. `195a50ca06355537` · Events this month · jenna@newjerseycannabusinessassociation.ccsend.com · 2025-03-17
62. `195a50887f1c2b3c` · Hamilton Farm's Weekly Menu! (New drop) · sales@hamiltonfarms.com · 2025-03-17
63. `195a5077de5cc21b` · New Brand Alert + 4/20 Deals - Stock Up Now! · andrew@northlake.supply · 2025-03-17
64. `195a4c9a227c49d1` · Oops! Corrected Link: Win $100 eGift Card · email@em.sherwin-williams.com · 2025-03-17
65. `195a483de858e13b` · Upgrade collaboration with Jotform Enterprise · benjamin@jotform.com · 2025-03-17
66. `195a46a40141a845` · Chance to Win a $100 eGift Card · email@em.sherwin-williams.com · 2025-03-17
67. `195a467cc781c54c` · Meet up at NECANN Boston? · jenna.maney@flowhub.com · 2025-03-17
68. `1959b353264f6981` · We've got TVs for as low as $69.99! · BestBuy@email.bestbuy.com · 2025-03-15
69. `19595ec579fbb70f` · Verano Marketing Newsletter - February · maggie.boyd@verano.com · 2025-03-14

**Skipped for safety:** the vast majority of vendor/marketing threads in the >12mo
promotions/social/forums window were marked `IMPORTANT` by Gmail (Francisco@high-grass-farms.apextrading.com,
Chris@little-leaf-labs.apextrading.com, fundcanna.com, wholesale@verano.com, and others recur
constantly with `IMPORTANT` applied) and were left untouched per the hard floor. Allowlist
domains skipped on sight: parkebank.com, sos.nj.gov (`*.gov`), intuit.com, stellaconnect.net
(Metrc). Did not hit the 200/run cap — the remainder of the ~201 estimated matching threads
beyond the 69 processed here is left for future nightly runs.

## category:updates — report only, not touched

~201 threads older than 12 months in `category:updates`. Confirmed this category is a mix of
invoices (`quickbooks@notification.intuit.com`), Square invoice notifications, FedEx receipts,
Google Voice call/text notifications, Headset.io scheduled reports, and bank-connection notices
— left entirely alone per the runbook (too dangerous to sweep). Sample sender domains for manual
review if desired: `intuit.com` / `notification.intuit.com`, `messaging.squareup.com`,
`fedex.com`, `headset.io`, `trustaltus.com`, `quickbooks.intuit.com`.

## Recovery

All 69 trashed threads sit in Gmail Trash for 30 days from 2026-07-18 and can be restored using
the thread IDs above.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox sweep, 2026-07-18
