---
created: 2026-07-24T23:15:00-04:00
updated: 2026-07-24T23:15:00-04:00
domain: project
type: log
status: done
tags: [basil, inbox-janitor, gmail, cleanup, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor run, 2026-07-24

Nightly unattended Gmail cleanup on `lemar@cuzziesnj.com`, per
`.claude/routines/inbox-janitor.md` (live runbook) and `.claude/anchors.md`
(platform IDs). Mode: **LIVE** (`DRY_RUN = false`).

## Run summary

- Archived **37** vendor-menu threads out of the inbox (labeled `Vendor Menus` /
  `Label_8`, `INBOX` removed — recoverable any time from All Mail).
- Trashed **85** old (>12 months), clearly-disposable promo/social/forum threads.
  Recoverable from Gmail Trash for 30 days.
- Skipped **15** trash candidates that otherwise matched the age+category filter:
  13 hit the NEVER-TOUCH allowlist (`parkebank.com` ×6, `sos.nj.gov`/`*.gov` ×7 —
  see list below for exact split), 2 were threads whose history contained an
  IMPORTANT-labeled message (a Dutchie survey thread and a Hamilton Farms payment
  correspondence thread).
- Did **not** hit the 200-thread trash cap this run (used 85/200).
- `category:updates` old-mail (report-only, never auto-trashed): ~201 threads
  estimated older than 12 months. Notable sender domains: `jotform.com`,
  `jotformsign.com`, `nytimes.com` (breaking-news alerts), `docusign.net`
  (already allowlisted), `cannazipbags.com`. Lemar may want to hand-clear these.
- Both the vendor-menu search and the trash-sweep search estimated ~201 total
  matching threads each — this run processed the first page(s) of each. The
  remainder rolls to future nightly runs by design (the routine is incremental,
  not one-shot).

**Operator note (safety interpretation):** the bootstrap prompt's hard floor says
"never touch a starred/important/user-labeled thread" without carving out PART A.
The runbook's own PART A text only gates *PART B* (trash) on importance. This run
resolved the ambiguity conservatively: **IMPORTANT-labeled threads were skipped in
both PART A (archive) and PART B (trash)** this time, not just PART B. That's a
stricter read than the runbook's literal text and means fewer vendor menus were
archived than PART A alone would allow (several IMPORTANT-labeled TerrAscend /
Illicit Gardens / Jersey Smooth / Ares Canna / Harvest Moon menu threads were left
in the inbox). Flagging this for Lemar to confirm intent — if PART A should archive
IMPORTANT vendor menus too, say so and future runs will pick up more per pass.

## Archived vendor-menu threads (37)

thread ID · subject · sender · date

- 19f8ff297b09e0c7 · Terrascend Menu - 2G Vape Restock + $18 Kind Tree 3.5g... · ndesiderio@terrascend.com · 2026-07-23
- 19f8a2201ea3f1c6 · Explore This Week's Garden Society Menu! · njwholesale@thegardensociety.com · 2026-07-22
- 19cb8b1b7d61771f · New landscape prerolls hitting the menu · Francisco@high-grass-farms.apextrading.com · 2026-03-04
- 19c8cb251bfd8c47 · New Menu Is Live! 14g Discount 20% Off! · Tyler.Marsh@verano.com · 2026-02-23
- 19c8c411e092c6fa · FRESH RESERVE IS AVAILABLE!! | FRESH GROW MENU · Kathy@freshcannabis.co · 2026-02-23
- 19c8ba26b6a00cb6 · TerrAscend Menu - 30% OFF Cookies, Legend & More! · ndesiderio@terrascend.com · 2026-02-23
- 19c8b79a1a051657 · Snowday GS & TerpX Menu · leena@thegardensociety.com · 2026-02-23
- 19c8b3bd9e92455d · Prolific - BIGGEST MENU YET · anthony@prolificgrowhouse.com · 2026-02-23
- 19c8b18188a52d34 · COLD WEATHER - HOT INVENTORY | UPDATED MENU FROM ASCEND · nbonsanto@awholdings.com · 2026-02-23
- 19c7746794d236b8 · TerrAscend Menu - 20% Off Ounces and More · ndesiderio@terrascend.com · 2026-02-19
- 19c76434ffeb254a · Hi5 Launch Menu + Five Islands - NOW LIVE!!!! · mzaidi@budsgoods.com · 2026-02-19
- 19c71a406253aad7 · Updated Menu From Ascend!! · nbonsanto@awholdings.com · 2026-02-18
- 19c7185c4acc4d19 · Fresh Grow Menu | Pre Roll Restock! · Kathy@freshcannabis.co · 2026-02-18
- 19c6c47bdc003659 · Tuesday Ascend Menu Update · nbonsanto@awholdings.com · 2026-02-17
- 19c676e9c0b921e2 · TerrAscend Menu - New Ounce Sale + Vape Sale · ndesiderio@terrascend.com · 2026-02-16
- 19c6743ce51b230b · Kiva Lost Farm/Camino Menu Feb Week 3 Menu! · carlos.gamez@kivaconfections.com · 2026-02-16
- 19c6712cf3fbf211 · Prolific Menu - Bob Pre-Rolls, Moonrocks & 510 Carts · anthony@prolificgrowhouse.com · 2026-02-16
- 19c66d36ec76d19b · Buds Goods Menu - Week of 2/16 · mzaidi@budsgoods.com · 2026-02-16
- 19c668b2911d018c · Monday Menu + Last Chance to Participate in Women's Month Promo · leena@thegardensociety.com · 2026-02-16
- 19c58f4c42bda04b · Ares Canna Menu - 2.13 · tj@arescanna.com · 2026-02-13
- 19c5857d38726747 · FRIDAY MENU + 2nd Request Fwd: Women-Owned Wednesday Promo · leena@thegardensociety.com · 2026-02-13
- 19c580ef4c574223 · Fresh Grow Menu | 20% Off All Eighths · Kathy@freshcannabis.co · 2026-02-13
- 19c577b069074925 · Ascend Menu Friday the 13th Edition!! · nbonsanto@awholdings.com · 2026-02-13
- 19c532353f133cf0 · TerrAscend Menu - 40% Off Cont. + New Concentrate · ndesiderio@terrascend.com · 2026-02-12
- 19c4dac82bd931fa · New Ascend Menu!! NEW LIQUID DIAMONDS Disposables!! · mgargiule@awholdings.com · 2026-02-11
- 19c48db1ab406067 · Fresh Grow Menu | 20% off All Eighths · Kathy@freshcannabis.co · 2026-02-10
- 19c43ca5cb85cc94 · Ares Canna Menu 2.9 - Hillview THC Seltzers NOW AVAILABLE! · tj@arescanna.com · 2026-02-09
- 19c43be776e21758 · TerrAscend Menu - $15 Live Terp Carts & $16.50 All-In-Ones · ndesiderio@terrascend.com · 2026-02-09
- 19c43a36a26a76c1 · Kiva LOST FARM B2GO + Updated Camino Menu! · carlos.gamez@kivaconfections.com · 2026-02-09
- 19c43153fac2d607 · Women-Owned Wednesday Promo Program + Monday Menu · leena@thegardensociety.com · 2026-02-09
- 19c42ec5a77f7242 · Prolific Menu — 50% Off Promos + Fully Stocked Bob Carts · anthony@prolificgrowhouse.com · 2026-02-09
- 19c42c7e21544559 · Buds Goods Menu - Week of 2/9 · mzaidi@budsgoods.com · 2026-02-09
- 19c42bcfff331f92 · Monday Menu Drop from Ascend | Major Sales · nbonsanto@awholdings.com · 2026-02-09
- 19c3372263fcd776 · Updated Menu from Ascend - 48 Flavors of Distillate · nbonsanto@awholdings.com · 2026-02-06
- 19c3120c6663fa3b · Your Shelves, Covered: Parks Grove Current Menu · kellie@parksgrove.com · 2026-02-06
- 19c2f033a6f3edab · TerrAscend Menu - 40% OFF Live Terp Carts & Disposables · ndesiderio@terrascend.com · 2026-02-05
- 19c290f79be39cdc · Updated Menu From Ascend · nbonsanto@awholdings.com · 2026-02-04

## Trashed threads (85) — recoverable from Gmail Trash for 30 days

thread ID · subject · sender · date

- 198395af2c528eb2 · Get it while it's hot! · wholesale@verano.com · 2025-07-23
- 1983916697b2d03a · Reminder - Brief survey on your ADT alarm monitoring experience · adt@express.sea1.medallia.com · 2025-07-23
- 1983881d2787ea08 · [Analyst Report] 96% of peers recommend Slack · email@mail.salesforce.com · 2025-07-23
- 19838059bd9f8c33 · News & Resources for Small Businesses · noreply@mail.lendistry.com · 2025-07-23
- 19837dc874ec4e40 · Elevate Your Business by Bringing Nature Inside · 2115@fastsigns.com · 2025-07-23
- 198378ff35f5b109 · New items alert: latest merch inside! · flyers@webstaurantstore.com · 2025-07-23
- 198372ce2cf19f0e · NECANN = Your next big connection · marc@necann.com · 2025-07-23
- 19350272efe0208c · A million dollar sweepstakes—claim your free entry · Microsoft@engage.microsoft.com · 2024-11-21
- 193502520897687e · See you soon! (MJBizCon) · hligon@idscan.net · 2024-11-21
- 1934f80f9ff87ec7 · Your High-Grade MJBizCon Experience Starts with Treez · marketing@treez.io · 2024-11-21
- 1934f4ca5795d9d3 · Color tools, custom social posts & more from PRO+ · email@em.sherwin-williams.com · 2024-11-21
- 1934b8a20e7910df · Create, save, and win the holiday season with Microsoft 365 · Microsoft365@engagement.microsoft.com · 2024-11-20
- 1934b53280c2e7ac · Build your own operations portal · learn@send.zapier.com · 2024-11-20
- 1934afcc66404505 · Level up your sales game with Slack · email@mail.salesforce.com · 2024-11-20
- 1934ac0eef571014 · Tired Of Counting Sheep? · marketing@leaftrade.com · 2024-11-20
- 1934a562a1d744dd · Elevate Your Space | FASTSIGNS · 2115@fastsigns.com · 2024-11-20
- 1934a13534a3847e · Time to check your POS tech · hello@flowhub.com · 2024-11-20
- 193462b1b7ab80b4 · Why this gift is on everyone's wish list... · update@dotcards.net · 2024-11-19
- 193457c0bb247081 · SMALL BUSINESS SATURDAY · salexander-vhrrental.com@voorheeshardware.ccsend.com · 2024-11-19
- 1934574bc65f1b1e · Minimize Hassle, Maximize your Business · team@leaflink.com · 2024-11-19
- 19344f1d3517e94c · Small Business Resources Available · main-palmestatesco.com@shared1.ccsend.com · 2024-11-19
- 19344dfc1166dd63 · Ride Shotgun with Marketing Pros (MJBizCon) · brittanie@thrivepop.com · 2024-11-19
- 19344d4045d1f440 · West marks 1,000 days of Russia's full-scale war · microsoft.start@email2.microsoft.com · 2024-11-19
- 1934421b603ec9f6 · Come to Sherwin-Williams for a great deal · email@em.sherwin-williams.com · 2024-11-19
- 19341fb7304c6627 · Enter to Win Tickets to the Cova Cannabis Royale MJBizCon After Party · dayna@covasoftware.com · 2024-11-18
- 19341eef135cf7be · Save more when you shop with Microsoft Edge · microsoftedge@engage.microsoft.com · 2024-11-19
- 19340a3eae17b0d3 · Get Ready: Green Wednesday is coming · marketing@leaflink.com · 2024-11-18
- 193401e8ff1ddc03 · Block distractions · blog@send.zapier.com · 2024-11-18
- 1933fbbb50c97d36 · Design and launch unique websites in minutes · marketing@engage.canva.com · 2024-11-18
- 1933f26adf98ca6d · Check Out Our Black Friday Deals Lemar Boone · emanuel@alphasecurity.ccsend.com · 2024-11-18
- 19336c797f67c615 · I just shot a video for you! · Dawid@driveeasyauto.com · 2024-11-16
- 19331e63f9934f33 · Hey Lemar... ready to earn something awesome? · info@fernway.com · 2024-11-15
- 193316c6995dcf17 · Small business owners 🤝 Zapier · learn@send.zapier.com · 2024-11-15
- 19330e2e5d63616d · Final Day for Custom Card Holiday Delivery · update@dotcards.net · 2024-11-15
- 19330697197f6806 · Small Business Resources Available Today · main-palmestatesco.com@shared1.ccsend.com · 2024-11-15
- 193300356bc9ed16 · LAST CHANCE 20% OFF NORTH LAKE SUPPLY · dan@northlake.supply · 2024-11-15
- 1932d91338a10efa · Microsoft Copilot grows with you · Copilot@engagement.microsoft.com · 2024-11-15
- 1932d5a88c57bae1 · Join your teammates on Otter · no-reply@updates.otter.ai · 2024-11-15
- 1932c22cb0fe6b30 · Only pay for what you sell 👏 · team@leaflink.com · 2024-11-14
- 1932bd57471b348e · Create quickly with free Photoshop templates · mail@email.adobe.com · 2024-11-14
- 1932b69aa1d7ca28 · Your next lunch break podcast is ready! · marketing@emeraldintel.ai · 2024-11-14
- 1932b50541b176d5 · KOTODO: Discover the Secret to Freshness · news@kotodocan.com · 2024-11-14
- 1932aedccbd65b28 · Giddyup! (MJBizCon) · brittanie@thrivepop.com · 2024-11-14
- 1932833e54662306 · Otter AI Chat: Get answers instantly · no-reply@updates.otter.ai · 2024-11-14
- 19327a2cc9e665fc · Career moves, powered by Acrobat · mail@email.adobe.com · 2024-11-13
- 1932792dc615880c · Enter to Win Tickets to Cova Cannabis Royale MJBizCon After Party · dayna@covasoftware.com · 2024-11-13
- 19326f09d7aad4cd · Curb legacy software tools and sluggish incident resolution · email@mail.salesforce.com · 2024-11-13
- 19326d6e469f3d1b · Don't Wait: Last chance for Custom dot.cards · update@dotcards.net · 2024-11-13
- 19326d46f982476d · Better Payroll for CUZZIE'S LLC in 2025 · peter@heartlandpayments.ccsend.com · 2024-11-13
- 19326bdc5397c974 · Discover fall 2024 cannabis trends with our latest report · marketing@leaflink.com · 2024-11-13
- 19325eea0a49d2aa · Secure Your Spot Now! · jenna@newjerseycannabusinessassociation.ccsend.com · 2024-11-13
- 19325a3567a47ce2 · Lemar, don't wait to see what your vehicle is worth · easyautopa@alstspecials.com · 2024-11-13
- 193219c87df4b1db · NEW AIQ x Adentro Integration · noreply@alpineiq.com · 2024-11-12
- 193211d4da1bee09 · Grow online sales with Dutchie's ecommerce solutions · marketing@dutchie.com · 2024-11-12
- 193210029e145cb0 · 1,189 people are coming. Are you? (Zapier webinar) · events@send.zapier.com · 2024-11-12
- 19320ea94731dd99 · Small Business Programs Available Now · main-palmestatesco.com@shared1.ccsend.com · 2024-11-12
- 19320f152eb325a6 · Feeling Lucky? Spin to Win for an Exclusive Discount! · email@em.sherwin-williams.com · 2024-11-12
- 193208d454ba2227 · Just 1 Day To Go! Secure Your Spot Now! · jenna@newjerseycannabusinessassociation.ccsend.com · 2024-11-12
- 1931e797a9ca75db · [Last chance at Office Hours!] ngrok · team@m.ngrok.com · 2024-11-12
- 1931c5fc5385b75f · From Vegas, With Love: Sponsors of Cannabis Royale After-Party · dayna@covasoftware.com · 2024-11-11
- 1931c5efbdd0394a · Photoshop tutorials, picked just for you · mail@email.adobe.com · 2024-11-11
- 1931c34e6795f3e3 · Unlock A Free Gift 🎁 · update@dotcards.net · 2024-11-11
- 1931c3202511f244 · Just 2 Days To Go! Secure Your Spot Now! · jenna@newjerseycannabusinessassociation.ccsend.com · 2024-11-11
- 1931ba2f3d52f618 · UP TO 20% OFF NORTH LAKE SUPPLY · dan@northlake.supply · 2024-11-11
- 193139a4063081f9 · Save time by sending OtterPilot to take your meeting notes · no-reply@updates.otter.ai · 2024-11-10
- 1930ee1abfa93593 · Otter your conversations from anywhere · no-reply@updates.otter.ai · 2024-11-09
- 1930e739353e444b · Record your first conversation with Otter · no-reply@updates.otter.ai · 2024-11-09
- 1930dbc1bf24aacf · Last Day to Save 20% on Custom dot.cards · update@dotcards.net · 2024-11-08
- 1930cc1830ac2ce3 · We couldn't join your meeting — Cuzzies <> MPX Connect · noreply@supernormal.com · 2024-11-08
- 1930c68e1411973d · You don't want to miss out! · jenna@newjerseycannabusinessassociation.ccsend.com · 2024-11-08
- 1930c529db1e6795 · Small Business Programs Available Now · main-palmestatesco.com@shared1.ccsend.com · 2024-11-08
- 1930c2a68682bb13 · United Nations warily awaits Donald Trump's return to power · microsoft.start@email2.microsoft.com · 2024-11-08
- 19307e7c7afbc3d0 · [Ask ngrok anything!] Office Hours '#003' · team@m.ngrok.com · 2024-11-07
- 19307aedb3ff1772 · What's next in the cannabis industry? · marketing@leaflink.com · 2024-11-07
- 193075e886c4d2b1 · Your October 2024 Pro Xtra Statement is Here · homedepotpro@mg.homedepot.com · 2024-11-07
- 19303f6d5ce1de1a · Let's dive in to your Scan Summary reports · hello@idscan.net · 2024-11-07
- 19302f76828dac26 · Don't wait – 20% off custom dot.cards ends tomorrow · update@dotcards.net · 2024-11-06
- 19302e4c7f915ff6 · Save 97 minutes weekly with Slack AI · email@mail.salesforce.com · 2024-11-06
- 19302e0f2ccfa56a · Last chance! Get up to $5,000 in 3 easy steps · marketing@leaflink.com · 2024-11-06
- 193027a679e398df · [Webinar] Make Zapier your business command center · events@send.zapier.com · 2024-11-06
- 1930252dac48eb5b · Custom Visuals Bring a Property to Life | FASTSIGNS · 2115@fastsigns.com · 2024-11-06
- 19301d9468b9e0dc · NEW Bits Dragonfruit LOL! · marketing@leaftrade.com · 2024-11-06
- 19301d4d6c33362e · Donald Trump defeats Kamala Harris to become the next U.S. president · microsoft.start@email2.microsoft.com · 2024-11-06
- 192fdeb680b74fe5 · Unlock Exclusive Savings: $500 OFF Your Next Vehicle! · Dawid@driveeasyauto.com · 2024-11-05
- 192fd48d67ccbafe · Scale your operations while staying compliant · marketing@dutchie.com · 2024-11-05

## Skipped trash candidates (15)

- `parkebank.com` (NEVER-TOUCH allowlist): 1981a30b57c70748, 196d5bf79e48117d, 1963b40e0e98503b, 195ab0ec06428d60, 195011d672d21c19, 193d66ca4c8bfe3d
- `sos.nj.gov` / `*.gov` (NEVER-TOUCH allowlist): 197a8cdb6f1d9200, 197419750281bd21, 1970730e3fb4672a, 196f9a74f675ba18, 196edc5766b6e391, 196d636a720c0a90, 196d59ad5a8b99df
- Contains IMPORTANT-labeled message: 19644c6a0e498f47 (dutchie.com survey thread), 196110a96c91e798 (hamiltonfarms.com payment correspondence thread)

## Sources

- gmail: `lemar@cuzziesnj.com` inbox, search queries per `.claude/routines/inbox-janitor.md`
  PART A / PART B, run 2026-07-24
