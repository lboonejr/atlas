---
created: 2026-07-10T23:07:00-04:00
updated: 2026-07-10T08:10-04:00
domain: cuzzies
type: log
status: active
tags: [inbox-janitor, basil, gmail, dry-run, automation]
source: claude
---

# Basil — Inbox Janitor dry run — 2026-07-10

`DRY_RUN = true` in `.claude/routines/inbox-janitor.md` — this was the first supervised
preview run. **No Gmail changes were made** (no archive, no label, no trash). Everything
below is "would archive / would trash" for Lemar to vet before flipping `DRY_RUN = false`.

## PART A — vendor menus (would archive)

Searched the inbox for vendor-seed-list domains (anchors.md) with attachments. Sampled
2 pages / 100 threads (Gmail's own estimate is ~201 total matching threads; remaining
pages were not fetched this run).

- **74 of the 100 sampled** are clean vendor-menu blasts (subject/snippet carries a menu
  signal — "menu", "drop", "availability", etc.), dated 2026-06-16 through 2026-07-09.
  These would get labeled `Vendor Menus` (`Label_8`) and archived out of the inbox.
- **Important finding — 3 threads must be excluded**, and were:
  - `19effba6d8f7c423` and `19ed686d78d9605e` (duplicates): "Prolific Growhouse Overdue
    Invoice/New Bank Account" from maylissa@prolificgrowhouse.com — an overdue-invoice /
    bank-change notice, not a menu.
  - `19ef5a3dac10b873`: "Past Due Payment Reminder" from ar@thegardensociety.com — a
    **live collections thread Lemar personally replied to** (SENT reply on file,
    IMPORTANT-flagged, already processed by Samira's email loop with
    Label_1/Label_3/Label_4). A naive domain-match sweep would have wrongly archived
    this out of the inbox.
- **Recommended runbook fix before going live:** PART A should (1) honor the same
  is:starred / is:important / genuine-filed-label safety floor PART B already has, and
  (2) skip threads whose subject/snippet carries invoice/payment/past-due/overdue
  signals even when the sender domain is on the vendor-menu seed list.
- The remaining ~100 threads beyond the two sampled pages were not fetched; a live run
  would paginate through all of them with the same logic.

## PART B — trash sweep (would trash)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)
-is:starred -is:important`. Sampled 2 pages / 100 threads (Gmail estimate ~201 total
matching; remaining pages not sampled).

- **99 of the 100 sampled** are clean disposable candidates (ads, dead subscriptions,
  old vendor marketing >12mo, newsletters, surveys), dated 2025-04-29 through
  2025-07-09. None touched a NEVER-TOUCH allowlist domain.
- **1 borderline thread excluded from the count, flagged for manual review:**
  `197c198384246d22` — "EXCLUSIVE: 2 NJ Cannabis Opportunities - Immediate (Stockton) +
  Early Stage (Millville)" from Julian@cd.cdre.co (2025-06-30). Reads as a genuine
  real-estate/licensing business-development lead, not disposable junk, even though
  Gmail filed it under promotions.
- Sanity-checked the inverse (same criteria but is:starred OR is:important): every
  sampled protected thread was correctly excluded, several also on the NEVER-TOUCH
  allowlist (intuit.com/quickbooks invoices, apextrading.com vendor threads marked
  important) — the importance/star guard and the allowlist are both working as
  designed.
- Per-run cap is 200 trashes; even a full pagination of the ~201 estimated candidates
  would land at or under the cap.

## category:updates (report-only — never auto-trashed)

`older_than:1y category:updates`: Gmail estimate ~201 threads. Frequent senders worth a
manual look: **headset.io** (very high volume — daily/weekly automated reports; already
NEVER-TOUCH-allowlisted, so safe but cluttering — consider unsubscribing at the
source), quickbooks@notification.intuit.com (old invoices), parkebank.com,
extraspace.com (storage unit), progressive.com (commercial insurance), cfins.com
(insurance portal OTP/password-reset codes — sensitive, never touch), fedex.com
receipts, Google account/workspace notices.

## Bottom line

No Gmail changes made tonight. Before flipping `DRY_RUN = false` in
`.claude/routines/inbox-janitor.md`:
1. Confirm the vendor-menu and trash-sweep sample lists above look right.
2. Patch PART A with the safety-floor + invoice/payment exclusion described above so the
   Prolific/Garden Society-style false positives can't happen live.
3. Decide on the one borderline business-opportunity thread (`197c198384246d22`).

## Sources
- gmail: account lemar@cuzziesnj.com, threads referenced above by ID
- claude: Basil (Inbox Janitor) nightly routine, 2026-07-10 run
