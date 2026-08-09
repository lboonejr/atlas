---
created: 2026-08-08T23:17-04:00
updated: 2026-08-09T00:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run log, 2026-08-08 (11pm ET)

**Mode:** LIVE (DRY_RUN=false)
**Account:** lemar@cuzziesnj.com

## Summary

- **Part A (vendor menus archived):** 82 threads labeled `Vendor Menus` and removed from
  Inbox. 159 threads reviewed across the vendor-domain seed list query (4 pages, fully
  paginated); 77 skipped as genuine 1:1 conversations, invoices, order/delivery
  coordination, OOO notices, personnel intros, or compliance notices. The backlog for this
  exact query is now fully cleared (no further page). `Vendor Menus` label now holds
  roughly 2,376 threads total.
- **Part B (old promo/social/forums trashed, >12mo):** 4 threads trashed, 0 over the
  200/run cap. 21 total candidates reviewed; 17 left untouched (7 `parkebank.com`
  allowlist, 7 `*.sos.nj.gov` allowlist, 3 protected by an IMPORTANT-labeled message
  somewhere in the thread).
- **category:updates:** ~201 threads found, report-only, no action taken. Sample sender
  domains: google.com (voice), nytimes.com, jotform.com/jotformsign.com, headset.io
  (allowlist), notification.intuit.com (allowlist), communication.microsoft.com,
  trustaltus.com, box.com, hellosign.com, monday.com, redditmail.com, theathletic.com.
- **Skipped for is:important/is:starred:** 7 in Part A, 3 in Part B — no allowlist domain
  looked miscategorized.

## Part B trash audit (recoverable from Gmail Trash for 30 days, i.e. until ~2026-09-08)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1988b553a5c948c4 | Nimbus Cannabis Co. and its Art of Extraction | andrew@northlake.supply | 2025-08-08 20:17:54Z |
| 1988a1167fd03802 | Thanks for stopping by! | marketing@cannazipbags.com | 2025-08-08 14:24:12Z |
| 19889e2f48c721e9 | Don't Miss the Final Two NECANN Conventions of the Year! | marc@necann.com | 2025-08-08 13:33:14Z |
| 19889b7b1436a459 | 💥 Shady Extract's BOBA IS MOVING FAST — LOCK IN YOUR ORDER NOW 💥 | Jade@hearth-wellness-llc.apextrading.com | 2025-08-08 12:46:12Z |

## Judgment calls / flags for Lemar (no action taken — informational only)

1. `192c58724372cf3e` (Verano) — a message-recall notification, not the promo itself.
   Left untouched; a human call on whether recall notices should be trash-eligible going
   forward.
2. Verano "assets" emails (maggie.boyd@verano.com — holiday photos, 4/20 screens/banners,
   Valentine's assets) were consistently skipped in Part A since they're retailer
   marketing collateral, not a menu/deal. Could loosen the archive criteria next run if
   Lemar wants these swept too.
3. NEVER-TOUCH allowlist looked correctly applied throughout — no miscategorization
   found. `parkebank.com` and `*.sos.nj.gov` hits in Part B were genuine
   newsletter/informational content, correctly protected.
4. No FundCanna underwriting thread appeared in either candidate pool — no risk this run.

## Sources
- claude: Basil nightly run, 2026-08-08 ~11pm ET, executed via general-purpose sweep agent
