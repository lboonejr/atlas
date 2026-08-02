---
created: 2026-08-02T00:00-04:00
updated: 2026-08-02T00:00-04:00
domain:    # UNRESOLVED — set one of: personal | cuzzies | station | project | reference | legal
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-02

Live run (`DRY_RUN=false`), continuing from [[2026-08-01-basil-inbox-janitor-run]],
[[2026-07-31-basil-inbox-janitor-run]], [[2026-07-30-basil-inbox-janitor-run]], and
[[2026-07-29-basil-inbox-janitor-run]]. Account: `lemar@cuzziesnj.com` (the only
connected Gmail account; Drive out of scope). Archived 123 vendor-menu threads out of
the inbox and trashed 1 old promotional thread (recoverable in Gmail Trash for 30 days).
Both stayed well under their per-run caps and respected the NEVER-TOUCH allowlist and
the starred/important floor from `.claude/anchors.md`.

**Note for Lemar:** tonight's PART A batch was unusually large (123 vs. ~58 on 8/1) —
the account is sitting on a substantial multi-month backlog of never-swept vendor-menu
blasts (some dating back to December 2025). This run cleared the batch surfaced by two
targeted searches (vendor-domain + attachment, and menu-subject signals with/without
attachment); there is likely more backlog further back that a future run's broader
search will keep finding. As before, most of the raw `category:promotions/social/forums`
trash-candidate pool was excluded by Gmail's own IMPORTANT classifier or the
`parkebank.com`/`*.gov` allowlist entries, leaving only 1 of 18 reviewed candidates
actually eligible to trash.

## PART A — vendor menus archived (123)

Query: `in:inbox has:attachment` combined with vendor-domain-seed list, plus
`in:inbox has:attachment subject:(menu OR "price sheet" OR "live menu" OR availability
OR drop OR "in stock")`, plus a no-attachment `subject:(menu OR "menu link")` pass to
catch link-based menu blasts (Apex/portal-hosted menus, Mudd Brothers Brevo mailings,
etc.). Each candidate was checked and excluded if it carried a STARRED message anywhere
in the thread, or was really an AR-statement / past-due / onboarding / banking-change /
collections thread from a vendor domain rather than an actual menu blast, or was an
internal Google Drive file-share notification (not a vendor email at all). All 123
qualifying threads were labeled `Vendor Menus` (`Label_8`) then had `INBOX` removed.

Senders included: Hamilton Farms, Hillview, Stash House Distro, Green Lightning,
PanCann, Next Level Brands, Cannabist Company, iAnthus/MPX, Grön Edibles, Humble Camp,
Garden Greens, Kiva Confections, GSE, Curaleaf, Kushi Labs, Grown Rogue/theCUT/Yeti,
Magic Garden Botanicals, Authorized Dealer NJ, Panda Farms/Bridge City Collective,
Jerzey Grown, Mudd Brothers, Glass Meadows, Fernway, Capitol Extracts, niche.,
Road Trip/Sunday, and the Apex NJ marketplace — all recurring one-way wholesale
menu/price-sheet blasts, no active back-and-forth pending.

Excluded on purpose (left in inbox, untouched): starred threads (MB1 Delight & KAI,
several Grön Edibles sends, a Humble Camp send, a Cannabist send, an HF Fresh Menu
1.23.26 reply), the Happy Eddie "THIRD DROP - Account Status" thread (collections, not
a menu despite "DROP" in the name), the Sun Extractions meeting-recap thread, a Leafly
product-feature notice ("New Menu Tax Indicator" — not a vendor blast), and roughly a
dozen internal Google Drive share-request notifications from Corey Rimmel / team
members forwarding menu spreadsheets (not vendor mail). A large residual backlog of
vendor-domain mail remains in the inbox by design — mostly AR statements, past-due
notices, and other financial correspondence that are not menus and should stay visible.

Archived thread IDs (first 30 of 123 shown for reference; full set now carries the
`Vendor Menus` label in Gmail / All Mail):
19d44a0d2c708959, 19c24f3d2ca4eecc, 19c23fdb5d35f1fa, 19c1a3a2bb96f393, 19be23eae32c9924,
19bd7029a54439aa, 19bd6f7ff2dd2693, 19bd6c9b904a0380, 19bd6874f3a76ab1, 19bc2ddd16249933,
19bbe3808593e9b4, 19bbe0679b27551e, 19bbd304094c3f89, 19bbcc306150b5c8, 19bb4c05710850e5,
19bb367694365354, 19bb3111f8713d5c, 19bb279fe44dabd3, 19ba4ed61eb56619, 19ba39d9d5780992,
19ba379d56888e97, 19b98d1ba52cfc8d, 19b98dde319ef104, 19b95ca1d812c09d, 19b94c1bec1e5901,
19b947d061350188, 19b9365ebd5786e9, 19b8ff16ac3da322, 19b8f98c4b476557, 19b8f362b8af90ab
(+93 more, spanning through 19bfb992b4f30a48).

## PART B — trash sweep (1 trashed, recoverable 30 days)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)
-is:starred -is:important`. 18 threads matched. Reviewed every one individually because
Gmail's thread-matching still surfaces threads containing an IMPORTANT-flagged message
even under `-is:important`. Only 1 passed every gate.

| # | Thread ID | Subject | Sender | Date |
|---|---|---|---|---|
| 1 | 19866271868b1a78 | "(( We CAN'T keep this quiet )) Winning a trip for 2 to the Leagues Cup Final..." | email@em.sherwin-williams.com | 2025-08-01 |

Skipped (17): 6 threads from `CTA@sos.nj.gov` (protected — `*.gov` allowlist entry), 5
threads from `parkebank@parkebank.com` (protected — `parkebank.com` allowlist entry),
1 `surveys@dutchie.com` thread (contains IMPORTANT-flagged messages), 1
`sales@hamiltonfarms.com` "Hamilton Farm's Weekly Menu & Go2 8ths release!" thread
(contains an IMPORTANT-flagged reply — live order-terms correspondence, not disposable),
and 1 `iccc@icic.org` thread (contains an IMPORTANT-flagged message). 0 threads hit the
200/run cap.

## `category:updates` — report-only (never auto-trashed)

~201 threads (estimate, capped) older than 1 year sit in `category:updates` in the
inbox. Per the runbook this category is never swept. Sample sender domains seen:
`notification.intuit.com` / `notifications.intuit.com` (QuickBooks), `google.com`
(Voice/Payments notifications), `fedex.com`, `nytimes.com`, `jotform.com`,
`messaging.squareup.com`, `headset.io`. Worth a hand pass if Lemar wants this folder
thinned — none of it was touched tonight.

No email was sent or drafted. No Trash was emptied, no Spam applied. No account other
than `lemar@cuzziesnj.com` was touched. Nothing starred/important/user-labeled or newer
than 12 months was archived or trashed.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox — search_threads / label_thread / unlabel_thread /
  apply_sensitive_thread_label, run 2026-08-02
