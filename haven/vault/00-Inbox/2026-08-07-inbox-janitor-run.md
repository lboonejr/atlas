---
created: 2026-08-07T23:07-04:00
updated: 2026-08-07T23:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-08-07

Basil's nightly Gmail cleanup, run live (`DRY_RUN = false`) against `lemar@cuzziesnj.com`.

## PART A — Vendor Menus (archived out of inbox)

2 threads archived to the `Vendor Menus` label and removed from `INBOX`:

1. Thread `19fd86c6cabcfa17` — "Prolific Menu 8.6 | Gelato Cream Returns! + The Debut of Orange Cream Pie & Refreshed Vape Lineup" — from anthony@prolificgrowhouse.com — 2026-08-06
2. Thread `19fd805052be2783` — "TerrAscend Menu - \"One\" Debut + 2G Vape Restock, $15 KT Eighths & More - 8-6-26" — from ndesiderio@terrascend.com — 2026-08-06

Several other vendor-domain threads were scanned (broad query returned ~201 loose matches,
narrowed to 4 on tight subject+attachment signals) but were **skipped** as only weakly
matching the menu signal — wholesale-agreement negotiations, restock requests, invoice/WSA
threads, or a thread carrying a starred/important message. Precision over recall, per the
runbook.

## PART B — Trash sweep (older_than:1y, promotions/social/forums)

Base candidate query (`older_than:1y AND (category:promotions OR social OR forums) AND
NOT starred/important`) returned **22 threads**. After the full gate (allowlist, genuine
labels, hard floor on any starred/important message anywhere in the thread), **5 threads
passed every clause and were trashed** (recoverable in Gmail Trash for 30 days):

1. Thread `198800b9f9c4cb17` — "Big Exposure, No Booth Needed – NJ Event Sponsorships Inside" — marc@necann.com — 2025-08-06
2. Thread `1987ff769120c9d3` — "Signs That Make the Grade With Students | FASTSIGNS" — 2115@fastsigns.com — 2025-08-06
3. Thread `1987fc909dbe1abf` — "Nothing Beats the Nimbus Beast Coast Berry!" — andrew@northlake.supply — 2025-08-06 (vendor-marketing domain, >12mo old — trashable per runbook, not on the allowlist)
4. Thread `1987fb622513c40d` — "Wanted to share this with you" — jonathon@hoodieanalytics.com — 2025-08-06
5. Thread `1987fa884cacf3fa` — "Trending now: new arrivals!" — flyers@webstaurantstore.com — 2025-08-06

**17 candidates skipped**, all for hard-floor reasons — none trashed:
- 7 threads from `CTA@sos.nj.gov` — `*.gov` is on the NEVER-TOUCH allowlist.
- 5 threads from `parkebank@parkebank.com` — on the NEVER-TOUCH allowlist.
- 3 threads (dutchie.com survey thread `19644c6a0e498f47`, Hamilton Farms weekly-menu
  thread `196110a96c91e798`, ICCC/icic.org thread `1826944b41c19b7a`) — each thread carries
  at least one message labeled `IMPORTANT`, even though a different message in the same
  thread matched the promo/social/forums search. Hard floor: never touch a thread that
  contains a starred/important message.

0 threads hit the 200/run cap — nothing left over for tomorrow.

`category:updates` is report-only per the runbook (never auto-trashed): **~201 threads**
older_than:1y in `category:updates` were counted but not touched. Sample sender domains for
Lemar to clear by hand if he wants: `jotform.com`, `jotformsign.com`, Google Voice missed-call
notices (`voice-noreply@google.com`), `breakingnews-noreply@nytimes.com`, `headset.io`
(on the allowlist, never trashed automatically), `notifications@monday.com`, `no-reply@box.com`,
`adobesign.com`.

## Recovery

Everything trashed tonight sits in Gmail Trash for 30 days and can be restored via the
5 thread IDs listed above.

## Sources
- gmail: 2 threads archived (Vendor Menus), 5 threads trashed — IDs listed above
