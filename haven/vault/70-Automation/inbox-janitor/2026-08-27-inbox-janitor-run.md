---
created: 2026-08-27T03:07-04:00
updated: 2026-08-27T08:15:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-08-27

Basil, nightly Gmail cleanup on `lemar@cuzziesnj.com`.

**Mode:** LIVE (`DRY_RUN = false`)

## Summary
- Vendor menus archived (labeled `Vendor Menus`, removed from Inbox): **4**
- Old threads trashed (>12 months, promotions/social/forums): **3**
- Threads over the 200/run cap: **0**

## PART A — vendor menus archived (4)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1a03f45c17451e6c | Fresh Grow Menu \| Pre-Roll & Beach Walker Sale Ends 8/28 | Kathy@freshcannabis.co | 2026-08-26 |
| 1a03e790f4a7f66a | ⛽️🔥 Illicit NJ Menu- Last chance for August Orders!! - for delivery 8/31 - 9/4 | jb@illicitgardens.com | 2026-08-26 |
| 1a03f96c3f5e0445 | Pre Orders Are Still On For Easy Landings ! | Tyler.Marsh@verano.com | 2026-08-26 |
| 1a03456b66218c57 | Bud's Goods / New Strains Now Available in Bud's 3.5g & 14g Flower ! ! ! | bsantos@budsgoods.com | 2026-08-24 |

All four were single-message, non-correspondence vendor marketing (explicit menu/order-sheet
content, sender on the vendor-domain seed list, an attachment or shop link present, none
starred/important). Roughly 17 other vendor-domain threads matching menu-signal keywords were
reviewed and skipped for precision — they were live back-and-forth correspondence (order
negotiations, AR/collections, onboarding, personal replies from Lemar) rather than disposable
marketing, or carried an IMPORTANT flag.

## PART B — trash sweep (3, recoverable in Gmail Trash for 30 days)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 198e7773bba6223c | Dropping next week: Wallet Passes by AIQ 🙌 | noreply@aiq.com | 2025-08-26 |
| 198e6eedf277175f | Meet us at NE Cann in Atlantic City! September 5-6 | info@vedawarrior.com | 2025-08-26 |
| 198e3d0cda5784f5 | Breaking news: Trump removes Lisa Cook from Federal Reserve Board | breakingnews-noreply@nytimes.com | 2025-08-26 |

Candidate pool was 24 threads (`older_than:1y`, category promotions/social/forums, not
starred/important). 21 were skipped:
- 16 protected by the NEVER-TOUCH allowlist (9 × `parkebank.com`, 7 × `sos.nj.gov`/CTA)
- 3 skipped because the thread carried at least one IMPORTANT-flagged message despite
  matching the search — the never-trash floor was applied per-thread, not just
  per-message (a Dutchie surveys thread, a Hamilton Farms correspondence thread, an
  icic.org thread)

## Report-only: old `category:updates` (never auto-trashed)

Roughly 201 threads older than 12 months sit in `category:updates` in the inbox. This
category mixes invoices, bank/legal notices, and payroll with ads, so it is never swept
automatically. Sample sender domains Lemar may want to clear by hand: `jotform.com` /
`jotformsign.com`, `nytimes.com` (fromthetimes/breakingnews digests), `voice-noreply@google.com`,
`headset.io`, `theathletic.com`, `redditmail.com`, `readyrefresh.com`. (`notification.intuit.com`
/ QuickBooks mail also appears in this category but is on the allowlist — never touch.)

## Recovery

Anything trashed above sits in Gmail Trash for 30 days; thread IDs are recorded in the
table so any mistake is recoverable.

## Sources
- gmail: search + thread actions on `lemar@cuzziesnj.com`, run 2026-08-27
