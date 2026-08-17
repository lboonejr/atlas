---
created: 2026-08-17T23:15-04:00
updated: 2026-08-17T23:15-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run, 2026-08-17

Mode: LIVE (DRY_RUN=false)
Account: lemar@cuzziesnj.com

## Summary
- Vendor menus archived out of inbox: **48**
- Threads trashed (>12mo, promotions/social/forums, safety floor applied): **2**
- Threads over the 200/run cap: 0 (cap not reached)
- Old `category:updates` threads found (report-only, not touched): ~201 estimated. Sample sender domains: nytimes.com (breaking-news alerts), voice-noreply@google.com (Google Voice missed-call notices), headset.io (scheduled reports), jotform.com / jotformsign.com (register approvals, checklists), monday.com (automation-error notices), theathletic.com, redditmail.com. Mixed in with real invoices/receipts per the runbook's warning — left untouched, worth a manual pass by Lemar if he wants it lighter.

## PART A — vendor menus archived (Vendor Menus label applied, removed from Inbox)
48 threads qualified as genuine vendor-menu / product-drop blasts (subject signals: "menu", "drop", "in stock", "new SKU", "restock", etc. from the vendor-domain seed list, cross-checked against snippet content). Excluded from this batch on purpose: threads that had evolved into personal 1:1 correspondence (order negotiations, restock requests, personnel intros), invoice/collections notices that merely matched a keyword like "New Bank Account", and any thread carrying a STARRED message (left alone out of caution, even though PART A's gate doesn't strictly require it — "when in doubt, leave alone").

Vendors represented: TerrAscend / Kind Tree, North Lake Supply, Ascend Wellness Holdings (Ozone), Little Leaf Labs / Growfather (Apex Trading), Verano, High Grass Farms (Apex Trading), Illicit Gardens, Kiva Confections, Sussex Cultivation / ONYX (Apex Trading), Hearth Wellness / Shady (Apex Trading).

Thread IDs archived (48):
1a000ca435095d5f, 19ff653f5623983e, 19fed2968c9c706c, 19c7b660f46d45d3, 19a6eab91903b52f, 199dc2cdb69c23df, 199bfbf0edc3793f, 199771149534b328, 19971d5f258fa676, 1997194946bfc1cc, 1992cdd6ffea813b, 1992b74b3a65fc55, 1992b12187d84bde, 198e7c2cda24654f, 198e192dd1a1fb66, 198c86b4804d5a19, 198996bd905b5a60, 19861092832277dc, 198526417b7f3f30, 198419d2d5bc9c69, 197fae337ec155b8, 197e5516c51007fe, 197acb22829c5e8f, 19778ad50cf88223, 19755dcf9cc64192, 196aca93b23f2b43, 1967f556c660630d, 196376e6c29cd7c3, 1961569ed22c2a06, 1955d7aa61f6442b, 19539c7125bc3678, 19514d72d0ac4c2f, 194f22c30297b1a5, 194cd6a6912ca0be, 194a9aa19820d056, 194a871468167882, 1948550ddd225659, 1946130838a40615, 1943d0ba364e079d, 192d530f7e461626, 192b0e473280c62c, 192b09456e59c417, 192af58fd56b3484, 1926824d15bc7c31, 192498ff59e91074, 191d933d282a4efb, 191b89272feea408, 19193fea43b3ad8e

## PART B — trash audit (recoverable in Gmail Trash for 30 days)
1. Thread `198b4b14068e6c4d` — "How to prevent and treat hair loss" — from fromthetimes-noreply@nytimes.com — 2025-08-16
2. Thread `198b456b2b370004` — "Get your hands on an amazing deal - take advantage of Best Buy Tech Fest." — from BestBuy@email.bestbuy.com — 2025-08-16

Reviewed ~280+ candidate threads across the `older_than:1y (category:promotions OR category:social OR category:forums)` query (resultCountEstimate 201, paginated 6x). The overwhelming majority were protected by the safety floor: Gmail's own IMPORTANT marker covers nearly all vendor/marketing mail in this account (a side effect of years of reply history training the classifier), plus the NEVER-TOUCH allowlist (parkebank.com, intuit.com, *.gov, stellaconnect.net) and a handful of STARRED threads. Only these 2 threads carried no protective signal at all. Effectively the entire remaining ~278 reviewed candidates were skipped for is:important / is:starred / allowlist.

## Notes
- Vendor Menus label (`Label_8`) already existed — no creation needed this run.
- No emails sent, replied to, or drafted. No Spam actions taken. No Trash emptied. No account other than lemar@cuzziesnj.com touched. No Drive activity.

## Sources
- gmail: account lemar@cuzziesnj.com, nightly sweep 2026-08-17
