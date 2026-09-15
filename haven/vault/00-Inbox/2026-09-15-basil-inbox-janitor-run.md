---
created: 2026-09-15T23:10:00-04:00
updated: 2026-09-15T23:10:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-09-15

## Run summary (live run, DRY_RUN=false)
Account: lemar@cuzziesnj.com

- Vendor menus archived (PART A): 10
- Threads trashed (PART B, >12mo old promotions/social/forums): 2
- Old `category:updates` threads (report-only, not touched): resultCountEstimate ~201+ (Gmail API estimate did not resolve further with paging). This category holds a mix of genuine business operational mail (Jotform register-float approvals, purchase order forms, Headset.io reports, FedEx receipts, ReadyRefresh delivery notices, Checkr autopay-failure notices) interleaved with clearable noise (NYT breaking-news/ad alerts from `fromthetimes-noreply@nytimes.com` and `breakingnews-noreply@nytimes.com`, r/gardening notifications from `noreply@redditmail.com`, The Athletic newsletters from `TheAthletic@e1.theathletic.com`, Google Voice missed-call/voicemail notices from `voice-noreply@google.com`). Per the runbook this category is never auto-trashed — left for Lemar to clear by hand if he wants.

## PART A — Vendor Menus archived (label added, removed from INBOX)
1. `1a0a1efe0f78a693` — Tyler.Marsh@verano.com — "New Menu! Easy Landings is Live And Still 30% off Everything!" — 2026-09-14
2. `1a0a19dc5e722785` — tj@arescanna.com — "Hillview Flower & Cannabis Philosophy - Menu" — 2026-09-14
3. `1a0a0f0261e0107f` — Kathy@freshcannabis.co — "Fresh Grow Menu | NEW DICE AIO NOW AVAILABLE!" — 2026-09-14
4. `1a0a0b6e92e4c89c` — mzaidi@budsgoods.com — "Bud's Goods Menu - Week of 9.14. New Jays 2pks, 5pks, and Party Packs!" — 2026-09-14
5. `1a0a074d67e966da` — kbreiner@qccnj.com — "QCC NJ Menu 9.14.26 - Fall Promos Are in the Air!" — 2026-09-14
6. `1a0a05d1a8431446` — carlos@harvestmoonfarmsnj.com — "HARVEST MOON FARMS MENU 9.14.26 Monday" — 2026-09-14
7. `1a0a0554ffb5cdbc` — nbonsanto@awholdings.com — "Ascend Updated Menu | Monday Update + Let's Link Up at NECANN!" — 2026-09-14
8. `1a0a054b0105eb5a` — dan.grandrino@kivaconfections.com — "Kiva Camino/Lost Farm Menu - September Week 3 - September to Remember Deals" — 2026-09-14
9. `1a0a01d23402549c` — anthony@prolificgrowhouse.com — "Prolific Menu 9.14 | Reloaded Menu! Grab These New SKUs While Available" — 2026-09-14
10. `1a0a12599392cbac` — dan@northlake.supply — "This Week's Menu + We're at NECANN Sep 18-19" — 2026-09-14

Skipped as non-menu despite domain+attachment match (precision-over-recall per runbook): AR statements, collections/past-due notices, banking-info-change notices, invoices, delivery confirmations, a legal demand letter, and event/calendar invites from the same vendor domains — none archived, left in inbox untouched. Also skipped: any thread carrying STARRED, and one mixed personal/menu thread (laddsllc.com "Let's get together this week? + Monday Menu Drop") since it was primarily a personal relationship conversation, not a vendor blast.

## PART B — Trashed (recoverable in Gmail Trash 30 days)
1. `19948e95ef08911e` — Phil@sussex-cultivation.apextrading.com — "ONYX Apex Menu Link - More New Rosin Jam, Cold Cure & Carts!!" — 2025-09-14
2. `1994863fa4799d34` — Francisco@high-grass-farms.apextrading.com — "Football weekend supplies" — 2025-09-14

Both: `older_than:1y`, `category:promotions`, no IMPORTANT/STARRED label, sender domain (apextrading.com subdomains) is on the vendor seed list and NOT on the NEVER-TOUCH allowlist.

Candidates skipped: scanned ~250 threads total across the `older_than:1y (category:promotions OR category:social OR category:forums)` query (paged from 2026-09-14 back to 2024-07-29). The overwhelming majority carried Gmail's IMPORTANT label (this account's ML importance-marker flags nearly all vendor/promotional mail as important, apparently due to frequent interaction with these senders) and were therefore protected by the never-trash floor. The remaining non-important threads were almost entirely from `CTA@sos.nj.gov` (`*.gov`, NEVER-TOUCH) or `parkebank@parkebank.com` (NEVER-TOUCH). No candidate hit the 200/run cap.

## Operator note (not an instruction, just surfaced for awareness)
Several vendor domains (thegardensociety.com, harvestmoonfarmsnj.com, prolificgrowhouse.com) sent repeated "updated/new banking instructions" emails mixed with collections/past-due notices during this scan window. Not acted on (correctly out of scope for Basil — no send/reply/trash of financial correspondence), just noting the pattern in case Lemar wants to verify those banking-change notices are genuine before anyone acts on them.

No repo/tool unreachability this run. `DRY_RUN=false` (per `.claude/routines/inbox-janitor.md` at run time).

## Sources
- gmail: account lemar@cuzziesnj.com, PART A + PART B thread IDs above
