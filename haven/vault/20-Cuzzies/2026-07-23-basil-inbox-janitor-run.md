---
created: 2026-07-23T23:07-04:00
updated: 2026-07-23T23:15-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor run, 2026-07-23 (LIVE)

Nightly unattended Gmail cleanup on `lemar@cuzziesnj.com`, per `.claude/routines/inbox-janitor.md`. Mode: **LIVE** (`DRY_RUN = false`). Acted only within the runbook's SAFETY floor — no sends, no drafts, no Spam, no Trash-emptying, nothing starred/important/user-labeled touched, nothing under 12 months old touched.

## Part A — vendor menus archived: 48

Archived (labeled `Vendor Menus` / `Label_8`, removed from Inbox) 48 vendor-menu marketing blasts, dated 2026-02-02 through 2026-07-22. Query: `in:inbox (subject:menu OR subject:availability OR subject:"live menu" OR subject:"price sheet" OR subject:drop OR subject:"in stock") has:attachment`, cross-checked against the vendor-domain seed list in anchors.

**This was a first-time backlog pass, not a full clean-out.** Recon surfaced several hundred more qualifying vendor-menu threads still sitting in the inbox going back to at least January 2026 (likely further — the account appears to have never had this label applied before tonight). Tonight's batch was deliberately scoped to single-message, high-confidence marketing blasts only. Threads where the vendor-menu subject line had evolved into **real order/payment correspondence** (a Lemar reply present) were explicitly left alone and NOT archived — examples: Buds Goods "Week of 2.23" partnership intro, Hamilton Farms "HF Fresh Menu 2.3.26" COD/Net-30 negotiation, Humble Camp "Living Soil" order, Jersey Smooth "1/26/26" order confirmation. Two internal forwards from Markony (business partner, The Station) were also left untouched. Senders archived tonight span: freshcannabis.co, ianthus.com (MPX), qccnj.com, kivaconfections.com, brutesroots.com, awholdings.com (Ascend), harvestmoonfarmsnj.com, prolificgrowhouse.com, cannabistcompany.com, ggcann.com (Garden Greens), hillviewmed.com, humblecamp.com, greenlightningcannabis.com, hamiltonfarms.com, missgrass.com, canopy-usa.com, terrascend.com, kushilabs.com.

**Remainder:** hundreds more qualifying vendor-menu threads remain in the inbox older than what tonight covered. No cap exists in the runbook for Part A, but processing the full historical backlog in one run wasn't practical; subsequent nightly runs will continue working through it incrementally since each run re-queries `in:inbox` fresh (already-archived threads simply drop out).

## Part B — old disposable mail trashed: 35

Trashed 35 threads via `apply_sensitive_thread_label(TRASH)`. Query: `older_than:1y (category:promotions OR category:social OR category:forums) -is:starred -is:important`. Well under the 200/run cap. All dated 2024-11-21 through 2025-07-22 (well past the 12-month cutoff). Recoverable from Gmail Trash for 30 days from 2026-07-23 (i.e. through ~2026-08-22).

Of the 50 candidates reviewed on the first results page, **15 were skipped** by the safety floor:
- 6 from `parkebank.com` — NEVER-TOUCH allowlist
- 7 from `CTA@sos.nj.gov` — `*.gov` allowlist
- 1 Dutchie survey thread carrying IMPORTANT-labeled messages within it
- 1 Hamilton Farms thread ("Weekly Menu & Go2 8ths release") that had turned into real referral correspondence (forwarded lead, payment-terms reply)

More trash candidates likely exist beyond this first page (resultCountEstimate stayed pinned at ~201 across pages); future nightly runs will continue the sweep against the live cutoff.

### Full trash audit (thread ID · subject · sender · date)

1. `198339ec18c84404` · "The industry's cannabis-friendly bank" · B2BMarketing@benzingaprofessional.com · 2025-07-22
2. `19832dee3367bc0a` · "ONYX Apex Menu Link - 7.22.25 - Reduced MOQ for Garlic Knots 2g Baller Jars!" · Phil@sussex-cultivation.apextrading.com · 2025-07-22
3. `19832a6c3abeb2bf` · "Know someone who needs better insurance coverage?" · info@alpharoot.com · 2025-07-22
4. `198329caaa3324f9` · "Help Us Win Our First Emjay! 🏆" · marketing@emeraldintel.ai · 2025-07-22
5. `198326f965a80bb8` · "This dispensary's online menu now drives 40% of sales" · hello@flowhub.com · 2025-07-22
6. `1936eab2a1355bf6` · "New course available" (Dead Head Rolling/Blazy Susan/Wana/Sano/Vape Battery Tech — 5 msgs) · noreply@www.learnbrands.com · 2024-11-27
7. `1936e9546adfde84` · "Interfaces + Tables = Game-changer" · learn@send.zapier.com · 2024-11-27
8. `1936e0a43b17164d` · "Delivered Digest: A Thanksgiving Thank-You for All You Do!" · news@onfleet.com · 2024-11-27
9. `1936d631a3536663` · "Reminder: Happy Thanksgiving Lemar Boone" · emanuel@alphasecurity.ccsend.com · 2024-11-27
10. `1936ad72c9ad361f` · "🔥 Fuel Your Fire at MJBizCon 2024!" · jeanette@weco.blue · 2024-11-26
11. `1936a65bdc5f6eff` · "Connect with Surfside at MJBizCon" · hello@surfside.io · 2024-11-26
12. `1936963207d0b00e` · "You don't want to miss out!" · jenna@newjerseycannabusinessassociation.ccsend.com · 2024-11-26
13. `193695301fb379a5` · "Exciting Announcement: Leaf Trade Joins Forces with LeafLink" · support@leaftrade.com · 2024-11-26
14. `19368754a16f45d8` · "Black Friday Bonus—8 Months Free with Pro Annual!" · no-reply@marketing.otter.ai · 2024-11-26
15. `19365345e017e094` · "Lemar Save on Payroll in 2025" · peter@heartlandpayments.ccsend.com · 2024-11-25
16. `19364c3c6b7d6ea8` · "[Dec. 11 Office Hours] Learn about K8s..." · team@m.ngrok.com · 2024-11-25
17. `19364b3c39d34fb4` · "Black Friday: Up to 50% off dot.Profile+" · update@dotcards.net · 2024-11-25
18. `193647f2f286acb6` · "Surprise: $15 off Your Next Purchase..." · homedepotpro@mg.homedepot.com · 2024-11-25
19. `19364798582b47c3` · "New course available" (Fernway NJ) · noreply@www.learnbrands.com · 2024-11-25
20. `1936451ecbfce743` · "What trends shaped the cannabis industry this fall? 🍃🍂" · marketing@leaflink.com · 2024-11-25
21. `193642174fe383ae` · "Limited Edition Scarlet Briq Now Available!" · marketing@leaftrade.com · 2024-11-25
22. `19363d8a157680c1` · "Help shape Canva Print's 2025 lineup 🎨" · marketing@engage.canva.com · 2024-11-25
23. `19363bca6c412fae` · "Big project coming up? Manage it with Fiverr Pro." · no-reply@announce.fiverr.com · 2024-11-25
24. `19363bb6276280be` · "You don't want to miss out!" (dup) · jenna@newjerseycannabusinessassociation.ccsend.com · 2024-11-25
25. `1936316576c9608e` · "Happy Thanksgiving Lemar Boone" (dup) · emanuel@alphasecurity.ccsend.com · 2024-11-25
26. `1936305f389f0791` · "💲 Begin your week with DEALS!..." · email@em.sherwin-williams.com · 2024-11-25
27. `1935e702be3a8b6c` · "Marketing… This Ain't Our First Rodeo 🤠" · brittanie@thrivepop.com · 2024-11-24
28. `1935af2dfe95744a` · "I just shot a video for you!" · Dawid@driveeasyauto.com · 2024-11-23
29. `1935573d0dbf4f92` · "Unlock Exclusive Savings: $500 OFF Your Next Vehicle!" · Dawid@driveeasyauto.com · 2024-11-22
30. `1935468169b07b52` · "Small Business Programs Available" · main-palmestatesco.com@shared1.ccsend.com · 2024-11-22
31. `193544b893eb3fa3` · "Delivered Digest: Are you ready for the holiday season?" · news@onfleet.com · 2024-11-22
32. `19353fa7fd591777` · "You don't want to miss out!" (dup) · jenna@newjerseycannabusinessassociation.ccsend.com · 2024-11-22
33. `19353a3422e5cde4` · "Check Out Our Black Friday Deals Lemar Boone" · emanuel@alphasecurity.ccsend.com · 2024-11-22
34. `193506dcd11c366a` · "Save 20% – Black Friday Early Access" · update@dotcards.net · 2024-11-21
35. `19350506e9c70002` · "Retailer Academy Unit 3: Maximizing Margins 🌿" · team@leaflink.com · 2024-11-21

## category:updates — report-only, no action taken

Per policy this category is never auto-trashed (it mixes invoices/bank/payroll/legal receipts with ads). ~200+ old threads (`older_than:1y`) sitting here for Lemar's manual review if he wants to clear them by hand. Sample sender domains seen: `notification.intuit.com` (invoices), `headset.io`, `adt.com`, `printful.com`, `readyrefresh.com`, `txt.voice.google.com` (Google Voice), `jotform.com` / `jotformsign.com`, `nytimes.com`, `redditmail.com`, `sos.nj.gov` (CTA).

## Sources
- gmail: `lemar@cuzziesnj.com` inbox, 2026-07-23 run
- claude: Basil / Inbox Janitor cloud routine, `.claude/routines/inbox-janitor.md`
