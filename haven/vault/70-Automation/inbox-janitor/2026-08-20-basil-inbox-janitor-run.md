---
created: 2026-08-20T23:07-04:00
updated: 2026-08-20T12:05:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run, 2026-08-20 (live)

Nightly Gmail cleanup on the connected account `lemar@cuzziesnj.com`. `DRY_RUN = false` —
this run took real, recoverable action per `.claude/routines/inbox-janitor.md`.

## PART A — vendor menus archived (3)

Moved out of Inbox, labeled `Vendor Menus` (`Label_8`), still readable in All Mail:

1. Thread `1a01a8a6a11861f9` — "Camino/Lost Farm Mid Week Menu - August Week 3 - Deals Continue" — dan.grandrino@kivaconfections.com — 2026-08-19
2. Thread `1a01a66cf8b86dc8` — "Ascend Updated Menu | Order by 11am Today to Get Order Before the Weekend!" — nbonsanto@awholdings.com — 2026-08-19
3. Thread `1a01a5878a82cc6c` — "QCC NJ Menu 8.19.26" — kbreiner@qccnj.com — 2026-08-19

**Note for tuning:** the first-pass query (vendor domain + `has:attachment`, ~201 estimated
matches) was far too loose — it pulled AR statements, collections notices, banking-change
notices, and overdue-invoice threads from the same vendor domains. Narrowed to a
subject-based menu-signal query (menu/availability/price sheet/live menu) before archiving
anything, per the runbook's "prefer precision over recall" rule. Two more candidates were
hand-reviewed and skipped as not genuinely menus: a 2025-02 terrascend "Update on Vendor
Menu Submissions" policy thread (contains a STARRED message) and a 2023-11 awholdings
"Current wholesale menu?" negotiation thread (IMPORTANT, substantive correspondence, not a
recurring blast).

## PART B — trash sweep (4 trashed, recoverable in Gmail Trash 30 days)

All `older_than:1y`, `category:promotions/social/forums`, sender domain not on the
NEVER-TOUCH allowlist, no starred/important/genuine filing label:

1. Thread `198c359584233a6e` — "Last Chance: RSVP for Tomorrow's Livestream with Story Cannabis VP of Marketing Aaron Dubois" — hello@surfside.io — 2025-08-19
2. Thread `198c2ddd847063ef` — "August 25-29 Blue Bucket Sale! Can't Miss Deals Starting Soon!!" — email@em.sherwin-williams.com — 2025-08-19
3. Thread `198c24f000939b65` — "The secret to more repeat customers" — hello@flowhub.com — 2025-08-19
4. Thread `198c1c71c5e9470e` — "AIQ Loops – The future of cannabis retail marketing." — noreply@aiq.com — 2025-08-19

12 candidates in the same batch were found and **skipped** (left untouched): 9 threads
from `CTA@sos.nj.gov` (protected — `*.gov` is on the NEVER-TOUCH allowlist), plus 3 threads
(a dutchie implementation-survey thread, a hamiltonfarms weekly-menu/order-minimum
negotiation thread, and an ICCC mini-MBA program thread) that each carried at least one
`IMPORTANT`-labeled message, failing the "not is:important" gate. No threads were skipped
for being starred this run. 0 threads were over the 200/run cap.

`category:updates` is report-only per the runbook (never auto-trashed — it mixes
invoices/bank/payroll/legal receipts with ads). Roughly **201 old (>12mo) `updates`
threads** exist; a sample of sender domains Lemar may want to clear by hand:
`jotformsign.com` (e-signature receipts), Google Voice missed-call/voicemail notices
(`voice-noreply@google.com`), `expertpay.com`, `aiq.com` (Alpine IQ), `cfins.com` (Crum &
Forster insurance), `calendly.com`, `northlake.supply`, `nytimes.com`. (`notification.
intuit.com` and `headset.io` also appear heavily there but are already on the allowlist
and were never trash candidates.)

## Safety confirmation

No email was sent, replied to, or drafted. No Spam applied. No Trash emptied. Only the
connected account (`lemar@cuzziesnj.com`) was touched. Google Drive was not touched
(out of scope per the runbook).

## Sources
- gmail: threads listed above (archived + trashed), account lemar@cuzziesnj.com
