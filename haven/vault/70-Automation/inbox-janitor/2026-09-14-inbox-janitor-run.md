---
created: 2026-09-14T23:07:00-04:00
updated: 2026-09-14T08:07:50-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-09-14

Mode: **LIVE** (`DRY_RUN=false`). Account: `lemar@cuzziesnj.com`.

## Summary
- Vendor menus archived: **2**
- Threads trashed (>12mo, promo/social/forums): **2**
- Threads over the 200/run cap: **0**
- PART B candidates skipped: **22** (19 NEVER-TOUCH allowlist domain match: 11 × `*.gov`, 8 × `parkebank.com`; 3 IMPORTANT-guard)
- `category:updates` (report-only, never auto-trashed): resultCountEstimate **~201** threads >12mo in this category. Dominant sender domains worth a by-hand look: `jotform.com` / `jotformsign.com` (e-signature notifications, many), `fedex.com` (shipping notices), `nytimes.com` (newsletters), `headset.io` (already protected — NEVER-TOUCH allowlist), `distru.com`, `readyrefresh.com`, `redditmail.com`.

## Archived (PART A — `Vendor Menus` label added, `INBOX` removed)
1. Thread `18c6bd094da25e48` — "Jersey Buyers Club Catalogue and Menu" — `no-reply@canva.com` — 2023-12-15
2. Thread `198377f4ee828baa` — "Cannabist x Old Pal July Wholesale Giveaway, mid-week menu update, NEW SKUS RELOADED!!" — `Andrew.Moyer@cannabistcompany.com` — 2025-07-23

**Precision-over-recall note:** the broader vendor-domain/menu-keyword search surfaced ~30 candidates, but most (Garden Greens/ggcann.com, LoveGrow, Authorized Dealer NJ, Green Lightning, Grön Edibles, Neptune's Garden, Panda Farms, Fernway, Hamilton Farms, etc.) turned out to be live back-and-forth correspondence threads — Lemar had replied (`SENT` messages in-thread) — not one-way marketing blasts, so they were left in the inbox rather than archived. Two "Availability" subject matches from `jowie.lop.sep@gmail.com` were staffing/schedule availability, not a product menu — correctly excluded as false positives from the keyword match. One candidate (`OGeez! Inventory & Latest Menu`) was starred — skipped on that basis even though PART A's floor doesn't name starred explicitly, per "when in doubt, leave it alone."

## Trashed (PART B — Gmail Trash, recoverable 30 days)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| `19944e3d835292ec` | 30-minute chicken recipes | fromthetimes-noreply@nytimes.com | 2025-09-13 |
| `19944badd34f05e1` | Shop clearance deals at the Best Buy Outlet today | BestBuy@email.bestbuy.com | 2025-09-13 |

## Skipped in PART B (candidate set of 24, from `older_than:1y (category:promotions OR category:social OR category:forums) -is:starred -is:important`)
- 11 × `sos.nj.gov` (Cannabis Training Academy "Ask Me Anything" webinar invites) — NEVER-TOUCH allowlist (`*.gov`)
- 8 × `parkebank.com` (bank marketing/newsletters) — NEVER-TOUCH allowlist
- 3 × IMPORTANT-guard (kept because at least one message in the thread carries the `IMPORTANT` label):
  - `19644c6a0e498f47` — dutchie.com implementation survey thread
  - `196110a96c91e798` — Hamilton Farm's weekly menu that turned into a real order-terms negotiation with a reseller
  - `1826944b41c19b7a` — icic.org ICCC "mini-MBA" program thread

## Sources
- gmail: `search_threads` queries against `lemar@cuzziesnj.com`, run 2026-09-14
- routine: `.claude/routines/inbox-janitor.md` (repo `lboonejr/atlas`, `main`)
