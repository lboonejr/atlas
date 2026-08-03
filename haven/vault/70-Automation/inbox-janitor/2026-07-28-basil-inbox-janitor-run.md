---
created: 2026-07-28T23:07-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-28

Live run (`DRY_RUN=false`). Account: `lemar@cuzziesnj.com` (the only connected Gmail
account; Drive out of scope). Archived 21 vendor-menu threads out of the inbox and
trashed 184 old promotional/social/forum threads (all recoverable in Gmail Trash for
30 days). Both actions stayed under their per-run caps and respected the NEVER-TOUCH
allowlist and the starred/important floor from `.claude/anchors.md`.

## PART A — Vendor menus archived (21)

Query: vendor-domain seed list (from anchors) AND `has:attachment` AND `in:inbox`,
201 domain-matched threads total; scanned 3 pages (~150 threads) and applied
precision-over-recall per the runbook — required an explicit menu signal ("menu",
"menu drop", "wholesale menu", etc.) in the subject or snippet, not just domain +
attachment. AR statements, overdue-invoice threads, event invites, and general
newsletters from the same vendors were left alone even though they matched the
domain filter. 21 threads qualified and were labeled `Vendor Menus` (`Label_8`) then
had `INBOX` removed:

| Thread ID | Sender | Subject | Date |
|---|---|---|---|
| 19fa6683ec9feddd | carlos@harvestmoonfarmsnj.com | Harvest Moon Farm Wholesale Menu 7.27.26 | 2026-07-27 |
| 19fa56efb0dfcd06 | Tyler.Marsh@verano.com | New Menu ! New Deals ! | 2026-07-27 |
| 19fa43ab5537c788 | ndesiderio@terrascend.com | TerrAscend Menu - $15 KT 3.5g... | 2026-07-27 |
| 19fa40553ad50d56 | kbreiner@qccnj.com | QCC NJ Menu 7.27.26 - Fresh Inventory & Promo Unit Incentives! | 2026-07-27 |
| 19fa3fd70937e085 | dan.grandrino@kivaconfections.com | Kiva Camino/Lost Farm Menu - Last of July & Deals Extended | 2026-07-27 |
| 19fa3df95ef68a76 | allanf@harvestmoonfarmsnj.com | New Week, New Menu – Fresh Drops & Ready to Ship | 2026-07-27 |
| 19fa3dd1b825df41 | hking@laddsllc.com | Monday Menu Drop | 2026-07-27 |
| 19fa3d76fafc0cbd | nbonsanto@awholdings.com | Ascend Menu \| NEW SIMPLY HERB 1.0g FLAVORS | 2026-07-27 |
| 19fa3d5e8c578bee | mzaidi@budsgoods.com | "Retuuuurn of the Pack" Party Pack's Now Available! (Fresh menu) | 2026-07-27 |
| 19fa3c530b22a186 | anthony@prolificgrowhouse.com | Prolific Menu 7.27 \| Limited Inventory | 2026-07-27 |
| 19d49a574a7466ae | caitlin@jerseysmooth.com | Not everything you read today is real! (Excel/Apex Menu attached) | 2026-04-01 |
| 19d2c841b26813cd | kellie@parksgrove.com | Fresh Drops from Parks Grove (menu update) | 2026-03-26 |
| 19d2bb2bcb6497f4 | caitlin@jerseysmooth.com | Thursday Check-in! (Excel/Apex Menu attached) | 2026-03-26 |
| 19caf3366cfa647e | allanf@harvestmoonfarmsnj.com | Huge Week Ahead — 7Gs Are Here (wholesale menu) | 2026-03-02 |
| 19c8b781ebd41bed | allanf@harvestmoonfarmsnj.com | Snowed In? Let's Move Weight (wholesale menu) | 2026-02-23 |
| 19c78c3989c4283f | kellie@parksgrove.com | End February on a High Note (latest menu) | 2026-02-20 |
| 19c71ac8bde5bfc7 | tj@arescanna.com | Ares Canna Menus - 2.18 | 2026-02-18 |
| 19c20ab05434d1fb | tj@arescanna.com | Ares Canna Menus - 2.2 | 2026-02-02 |
| 19c04dcd7e7505b3 | nbonsanto@awholdings.com | Last Call for Delivery (Ascend menu attached) | 2026-01-28 |
| 19c0b89c9d015884 | kellie@parksgrove.com | Start February Fresh With a Parks Grove Refresh (menu/order form) | 2026-01-29 |
| 19c109af467e3731 | leena@thegardensociety.com | Friday Menus- Order today | 2026-01-30 |

## PART B — Trash sweep (184 threads)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)
-is:starred -is:important in:inbox`. Scanned 4 pages (~200 of an estimated 201
candidates). Excluded 12 threads on the NEVER-TOUCH allowlist and 2 threads that
carried an IMPORTANT-labeled message despite matching the category filter — see
"Skipped" below. Remaining **184 trashed**, all dated 2024-06-19 through 2025-07-17
(well past the 12-month cutoff). Recoverable from Gmail Trash for 30 days; use
`in:trash` in Gmail search to find a specific one by sender/subject/date if a
mistake needs undoing. 0 threads left over the 200/run cap tonight.

Recurring senders swept (marketing/newsletter noise, not vendor or business
correspondence): `microsoft.start@email2.microsoft.com` (MSN daily news digest,
~30 threads), `learn@send.zapier.com`, `email@mail.salesforce.com` (Slack
marketing), `noreply@jotform.net`/`.com`, `hello@flowhub.com`, `info@fernway.com`,
`news@onfleet.com`, `email@em.sherwin-williams.com`, `mail@email.adobe.com`,
`main-palmestatesco.com@shared1.ccsend.com` / `shop-shotoclock.co@shared1.ccsend.com`
(SBA-loan spam), `jenna@newjerseycannabusinessassociation.ccsend.com`,
`marketing@leaflink.com`, `HomeDepotCustomerCare@mg.homedepot.com`, and similar.

This was a bounded first-pass scan, not exhaustive of the full multi-year backlog —
future nightly runs will keep working through the remainder plus whatever
accumulates.

### Skipped (floor / allowlist hits)
- `parkebank.com` — 6 threads skipped (NEVER-TOUCH allowlist)
- `*.sos.nj.gov` (NJ Cannabis Training Academy) — 6 threads skipped (`*.gov` allowlist)
- 2 threads skipped for carrying an IMPORTANT-labeled message despite matching the
  promo/social category: the Dutchie implementation-survey thread (`19644c6a0e498f47`)
  and the Hamilton Farms menu/order-minimum correspondence thread (`196110a96c91e798`)

## Report-only: `category:updates` (never auto-trashed)

~201 threads older than 12 months in `category:updates` — **not touched**, per the
runbook (this category mixes invoices, bank notices, payroll, and legal receipts in
with ads; too risky to sweep automatically). Sample sender domains seen: `google.com`
(Drive share notifications), `nytimes.com`, `headset.io` (already on the allowlist),
`adtcontrol.com`, `theathletic.com`, `redditmail.com`, `jotform.com`. Lemar may want
to clear these by hand.

## Next run
`DRY_RUN` stays `false`. The vendor-menu domain sweep covered ~150 of 201 matching
inbox threads and the trash sweep covered ~200 of an estimated 201 — both queues
still have a small remainder plus nightly accumulation to pick up next time.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox, live sweep 2026-07-28
