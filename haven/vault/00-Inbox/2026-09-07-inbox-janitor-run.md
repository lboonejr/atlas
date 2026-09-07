---
created: 2026-09-07T23:15-04:00
updated: 2026-09-07T23:15-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-09-07 (live, DRY_RUN=false)

## Summary
Basil (Inbox Janitor) ran live for the first time this session (`DRY_RUN=false`, per
`.claude/routines/inbox-janitor.md` on `main`). Account: `lemar@cuzziesnj.com`.

- **PART A (vendor menus):** 36 threads archived to the Vendor Menus label (`Label_8`)
  and removed from INBOX. Reviewed ~100 additional candidate threads matching vendor
  domains but excluded them (invoices, AR/collections statements, personal
  correspondence, OOO notices, event invites, banking-change notices) as not genuine
  menu blasts — precision over recall per the runbook.
- **PART B (trash sweep):** 32 threads moved to Trash (`older_than:1y`,
  `category:promotions/social/forums`, none starred/important/allowlisted). Reviewed
  3 pages (150 threads) of candidates total; pages 2–3 (100 threads, Aug 2025 and
  earlier) yielded zero additional candidates because virtually every thread in that
  range was already marked `is:important` by Gmail or matched the NEVER-TOUCH
  allowlist (`parkebank.com`, `*.gov`) — the hard floor worked as designed. Stopped
  after 3 pages given diminishing returns; well under the 200/run cap.
- **`category:updates` (report-only, never auto-trashed):** ~201 threads older than 1
  year. Sampled sender domains: `jotform.com` / `jotformsign.com` (register-float
  approvals, signed forms), `notification.intuit.com` (QuickBooks invoices),
  `nytimes.com`, `headset.io` (scheduled reports), `redditmail.com`, `evite.com`,
  `softtouchpos.co`, `theathletic.com`, `voice-noreply@google.com` (Google Voice).
  Left untouched per the runbook — mixed with financial/operational mail, too
  dangerous to sweep.

## Trash audit (recoverable in Gmail Trash for 30 days) — thread ID · subject · sender · date
1. `199202956f660db3` · Hello there - we've got a DEAL with your name on it 💰 · BestBuy@email.bestbuy.com · 2025-09-06
2. `1991ee87eff8858c` · T Magazine's favorite bedrooms · fromthetimes-noreply@nytimes.com · 2025-09-06
3. `1991b1833630d33d` · Your seasonal plans start here · marketing@plans.eventbrite.com · 2025-09-05
4. `1991b09f7133b9ec` · Breakout a Beast Coast Berry By The Boardwalk! · andrew@northlake.supply · 2025-09-05
5. `1991ab34555f6414` · Make your social content shine · marketing@engage.canva.com · 2025-09-05
6. `1991aa875dd6480f` · Don't Miss a Thing - Subscribe for Dutchie Updates · do-not-reply@dutchie.com · 2025-09-05
7. `1991a71e1e7dc420` · Meet AlphaRoot at Revelry NYC Next Week · info@alpharoot.com · 2025-09-05
8. `1991a2b460cb0bdb` · 🚀 NECANN New Jersey Starts TODAY! · marc@necann.com · 2025-09-05
9. `199166e5ccfcb449` · 🍁 New Products for Fall: Honeycrisp & Pumpkin Spice · info@fernway.com · 2025-09-04
10. `19915e263541b963` · Scale Smarter, Not Harder · marketing@treez.io · 2025-09-04
11. `19915dc9f6c72cca` · Hall of Flowers, Loops, Wallet Passes & more 🙌 · noreply@aiq.com · 2025-09-04
12. `199155aa349f1ee9` · Join me at ZapConnect 2025 · events@send.zapier.com · 2025-09-04
13. `1991548274a809d2` · September Events with Veda Warrior · info@vedawarrior.com · 2025-09-04
14. `1991536a56456603` · Heading to NECANN NJ? Let's Connect · alex@rankreallyhigh.com · 2025-09-04
15. `199149c1173ab525` · Easy slow-cooker recipes · fromthetimes-noreply@nytimes.com · 2025-09-04
16. `19910a2ba986da86` · Hamilton Farms Weekly Menu · sales@hamiltonfarms.com · 2025-09-03
17. `1991071aca1e8e2f` · Order Mobster Mango Haze or You'll Sleep with the Fishes! · andrew@northlake.supply · 2025-09-03
18. `199101dfbca70623` · Bold Solutions for your Brand | FASTSIGNS · 2115@fastsigns.com · 2025-09-03
19. `19910138cc4a3323` · Take the Trip 🚀 Infused Pre-Rolls Await · marketing.us@terrascend.com · 2025-09-03
20. `1990c7364efd9259` · Say CIAO! to Encore's Newest Flavor · wholesale@verano.com · 2025-09-02
21. `1990c5c4ab5a3832` · THIS FRIDAY: Come Celebrate With Fernway In Atlantic City! · brian.a@fernway.com · 2025-09-02
22. `1990c4436774492f` · The best way to eat zucchini · fromthetimes-noreply@nytimes.com · 2025-09-02
23. `1990b4fcf57f54ba` · Post-Labor Day Restock + NECANN NJ Roll Call · andrew@northlake.supply · 2025-09-02
24. `1990ad9b3614b7ab` · Transform your deck into a doc · product@engage.canva.com · 2025-09-02
25. `1990ac919d901ae0` · TerpX Essentials Vapes Are Here — Now in NJ! · matt@terpx.com · 2025-09-02
26. `1990a8a50fc57a76` · Big Things Coming to Atlantic City 🚨 · marc@necann.com · 2025-09-02
27. `1990a4e8abcf5016` · Quiz: Can you place 8 events in chronological order? · fromthetimes-noreply@nytimes.com · 2025-09-02
28. `1990a418c7a7958c` · Cannabis Business Newsletter - September 2025 · michelle-thinkcanna.com@cannaadvisors.ccsend.com · 2025-09-02
29. `19909ea3c0364869` · The latest issue of PPC Magazine is here! · email@em.sherwin-williams.com · 2025-09-02
30. `199055f689f8dac0` · Reminder: How Was Your Recent Experience with PSE&G's Telephone Service? · websurvey1973036@us.confirmit.com · 2025-09-01
31. `198fc0dbdd955a1d` · Your next upgrade is here. Shop the Labor Day Sale. · BestBuy@email.bestbuy.com · 2025-08-30
32. `198fbe211d0a2103` · ONYX Apex Menu Live Link - 8.30.25 · Phil@sussex-cultivation.apextrading.com · 2025-08-30

## Archived to Vendor Menus (Label_8) — thread ID · subject · sender · date
1. `1a06d48cefd51662` · Frieday Re-up (deals n steals) · bbreslow@novafarms.com · 2026-09-04
2. `1a06cdd591165960` · Ascend Updated Menu | SHAKE SHAKE SHAKE!!! · nbonsanto@awholdings.com · 2026-09-04
3. `1a06c4c29aec97b7` · Fresh Grow Menu | Labor Day Specials + New Drops Coming Soon · Kathy@freshcannabis.co · 2026-09-04
4. `1a0681794219852b` · TerrAscend Menu - 50% OFF Edibles... · ndesiderio@terrascend.com · 2026-09-03
5. `1a067c1907960929` · Harvest Moon Farms Menu 9.3.26 · carlos@harvestmoonfarmsnj.com · 2026-09-03
6. `1a067b888838b633` · KIVA CAMINO & Lost Farm B2GO Last Day to Submit 9/3 · carlos.gamez@kivaconfections.com · 2026-09-03
7. `1a067767d75d25c7` · Ascend Updated Menu | SHAKE SHAKE SHAKE!!! · nbonsanto@awholdings.com · 2026-09-03
8. `1a063e10ba8a8d34` · Illicit NJ Menu- $15 eighths!!! · jb@illicitgardens.com · 2026-09-02
9. `1a0635ad4de57628` · IMPORTANT UPDATES & a full menu · alex@jerseysmooth.com · 2026-09-02
10. `1a063173a6e7dbb4` · Kiva Camino Lost Farm Menu B2GO offer ends tomorrow · carlos.gamez@kivaconfections.com · 2026-09-02
11. `1a062c88f4261091` · Harvest Moon Farms Menu 9.2.26 · carlos@harvestmoonfarmsnj.com · 2026-09-02
12. `1a06284a1ec4d9a7` · QCC NJ Menu 9.2.26 · kbreiner@qccnj.com · 2026-09-02
13. `1a0623ff79cdc04f` · Ascend Updated Menu · nbonsanto@awholdings.com · 2026-09-02
14. `1a062322eda38bba` · Wednesday Wholesale Update – The Menu Is Loaded · allanf@harvestmoonfarmsnj.com · 2026-09-02
15. `1a05d407e61d7623` · Kiva Camino Lost Farm B2GO Offer ends 9/3 · carlos.gamez@kivaconfections.com · 2026-09-01
16. `1a05d32a8fad8c59` · Harvest Moon Farms Menu 9.1.26 · carlos@harvestmoonfarmsnj.com · 2026-09-01
17. `1a05cd7b8f1441ab` · TWO Sugar High Categories · Matt@little-leaf-labs.apextrading.com · 2026-09-01
18. `1a05a7a910798083` · Everything 30% Off! · Tyler.Marsh@verano.com · 2026-09-01
19. `1a0596b88160d8fc` · Parks Grove Menu Update — Stock Up for Labor Day · kellie@parksgrove.com · 2026-08-31
20. `1a058bec691a2ecd` · TerrAscend Menu - DEBUT: Kief & Diamond · ndesiderio@terrascend.com · 2026-08-31
21. `1a058aad824aeaf7` · UPDATED CAMINO LOST FARM MENU - B2G1 · dan.grandrino@kivaconfections.com · 2026-08-31
22. `1a0589bd7f4ead3e` · QCC NJ Menu 8.31.26 · kbreiner@qccnj.com · 2026-08-31
23. `1a0588b0582ad8ce` · Fresh Grow Menu | Labor Day Sale · Kathy@freshcannabis.co · 2026-08-31
24. `1a05855b6b3f1e88` · Camino Lost Farm Menu - First for September · dan.grandrino@kivaconfections.com · 2026-08-31
25. `1a058545916f7116` · Stashie: ROAD TO CROPTOBER (Menu+ Updates) · bbreslow@novafarms.com · 2026-08-31
26. `1a058512c8d4706a` · Spend More. Get More. Up to 8 Cases FREE. · Mark@agri-kind.apextrading.com · 2026-08-31
27. `1a0582833cd74878` · Sale Prices in Place · Jake@garden-state-exotix.apextrading.com · 2026-08-31
28. `1a0580d31e0771e5` · Ascend Updated Menu | Happy Hour Pre Rolls · nbonsanto@awholdings.com · 2026-08-31
29. `1a05804c574a52f8` · Prolific Menu 8.31 · anthony@prolificgrowhouse.com · 2026-08-31
30. `1a0580387ad0b0ff` · Bud's Goods Menu - NEW DROPS! · mzaidi@budsgoods.com · 2026-08-31
31. `1a057dc315d40224` · Monday Menu Drop – Fan Favorites Are Back · allanf@harvestmoonfarmsnj.com · 2026-08-31
32. `1a054913facdedcf` · Harvest Moon Farms Menu 8.30.26 · carlos@harvestmoonfarmsnj.com · 2026-08-30
33. `1a04917ee3f13961` · Happy Farmer: BLUE DREAM DROP · Andrew@the-happy-farmer-llc.apextrading.com · 2026-08-28
34. `1a048976428c5835` · NEW Sugar High Sugar Shake + 2G AIO Launch Is Here! · Matt@little-leaf-labs.apextrading.com · 2026-08-28
35. `1a03e6f5ccf7ecfb` · Your Golden Ticket to Sugar High Has Arrived · Matt@little-leaf-labs.apextrading.com · 2026-08-26
36. `1a033ef6d3d1300f` · Welcome to the Sugar High Factory — Launch Pricing · Matt@little-leaf-labs.apextrading.com · 2026-08-24

## Skipped for Lemar's awareness (not menus, not trashed — flagged in case he wants to act)
- Two Garden Society (`thegardensociety.com`) "Response Required - To Avoid
  Collections" / "Account 95 Days Past Due" threads sitting in inbox, one marked
  IMPORTANT — a real receivable dispute, left untouched.
- Harvest Moon Farms "Important: Updated Banking Information"
  (`allanf@harvestmoonfarmsnj.com`) — bank-account-change notice, left untouched
  (also a common BEC-fraud vector worth a manual glance).
- Ladds LLC (`laddsllc.com`) personal correspondence thread ("Let's get together this
  week? + Monday Menu Drop!") with real back-and-forth about the Camden closure —
  left untouched despite matching menu keywords.

## Notes for next run
- The runbook's "every user label except 5 named Samira labels is protective" clause
  literally would also protect Vendor Menus (`Label_8`) from PART B trashing,
  contradicting the routine's own explicit statement that vendor-menu domains are
  trashable >12mo old. Resolved by treating `Label_8` as Basil's own automation label
  (like the Samira labels), not a "genuine filing label Lemar applied deliberately,"
  consistent with the routine's explicit vendor-domain-is-trashable carve-out. Worth
  clarifying in the runbook text itself so future runs don't have to re-derive this.
- PART B pages 2–3 (Aug 2025 and earlier, 100 threads) yielded zero trash candidates —
  almost everything is marked `is:important`. Future runs may see similar diminishing
  returns beyond the ~1-month window right at the 12-month boundary; a nightly run
  should mostly find the newly-aged edge of the window each night rather than needing
  to page deep.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox sweep, 2026-09-07 run (PART A + PART B thread IDs above)
