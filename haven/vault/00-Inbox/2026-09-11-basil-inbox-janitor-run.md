---
created: 2026-09-11T23:07:00-04:00
updated: 2026-09-11T23:07:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run log — 2026-09-11

**Date:** 2026-09-11 (nightly ~11pm ET run)
**Mode:** LIVE (DRY_RUN = false)
**Account:** lemar@cuzziesnj.com

## Summary
- Archived 3 vendor menus out of the inbox (labeled `Vendor Menus`, removed `INBOX`)
- Trashed 6 old disposable threads (>12mo, category promotions/social/forums, passed every safety gate)
- 0 threads over the 200/run cap
- 22 of 28 initial trash candidates were skipped: 19 for NEVER-TOUCH allowlist domains (11 `*.gov` / CTA New Jersey, 8 `parkebank.com`), 3 for carrying an `IMPORTANT` label on at least one message in the thread (Dutchie survey thread, Hamilton Farms menu/order thread, ICCC program thread)
- `category:updates` older than 1 year: ~201 threads, report-only per policy (mix of QuickBooks/Intuit invoices, JotForm register-float approvals, Google Voice call/voicemail notices, NYT breaking news, Headset.io reports, World Insurance digest, ExtraSpace storage past-due reminder) — not touched, left for Lemar to clear by hand if desired

## PART A — Vendor menus archived (3)
| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1a08c877966d2e77 | TerrAscend Menu - 50% OFF Edibles and KT 3.5g + New Cookies PRJ & More - 9-10-26 | ndesiderio@terrascend.com | 2026-09-10 |
| 1a08c6d80e95c24d | Harvest Moon Farms Menu 9.10.26 | carlos@harvestmoonfarmsnj.com | 2026-09-10 |
| 1a08c20ddc8b3170 | Canfections APEX Menu! | Peter@canfections-nj-llc.apextrading.com | 2026-09-10 |

Skipped as only weakly menu-like or genuine 1:1 conversations (precision over recall): "Let's get together this week? (+ Monday Menu Drop!)" (laddsllc.com, live back-and-forth), "⛽️🔥 Illicit Menu -20% Off Sale" (illicitgardens.com, live back-and-forth w/ starred reply), "Update on Vendor Menu Submissions" (terrascend.com, admin correspondence, starred), "Current wholesale menu?" (awholdings.com, live back-and-forth).

## PART B — Trash sweep (6), recoverable in Gmail Trash for 30 days
| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 19934d294a868707 | Don't miss LeVar Burton at ZapConnect! | events@send.zapier.com | 2025-09-10 |
| 199349c0ebc67403 | Lemar, find your visual advantage inside | marketing@engage.canva.com | 2025-09-10 |
| 199349a2761346f6 | FedEx Office wants to know what you think, Lemar | fedexoffice@us.confirmit.com | 2025-09-10 |
| 1993446b384d2955 | Our New Menu! 9.10.25 | sales=greenmedicinenj.com@hubspotstarter.hs-send.com | 2025-09-10 |
| 199341efe3d46ece | Elevate Your Taste 🍒🍑 Three Fruity New Twists | marketing.us@terrascend.com | 2025-09-10 |
| 19933c0b581e2e42 | (FREE) Curbside Pickup > Pull Up & Go | homedepotpro@mg.homedepot.com | 2025-09-10 |

Note: the terrascend.com marketing thread already carried the `Vendor Menus` label from a prior PART A run; per the runbook, vendor-domain marketing over 12 months old is trashable regardless of that label (PART A only protects recent menus from being trashed, it does not shield old ones).

## Skipped — allowlist (19)
All `CTA@sos.nj.gov` (*.gov, 11 threads) and all `parkebank@parkebank.com` (NEVER-TOUCH, 8 threads) — never touched.

## Skipped — IMPORTANT present (3)
Dutchie implementation survey thread, Hamilton Farms weekly menu/order thread (real correspondence about payment terms), ICCC mini-MBA program thread — each carried an `IMPORTANT` label on at least one message, so the whole thread was left alone per the safety floor.

## Next run
No runbook changes made. `DRY_RUN` stays `false`. Allowlist and vendor-domain seed list unchanged this run — nothing found that needs adding.

## Sources
- gmail: 9 threads actioned (3 archived, 6 trashed), IDs listed above
