---
created: 2026-08-16T23:07-04:00
updated: 2026-08-16T08:05:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-08-16 (live)

Basil, the nightly Inbox Janitor, ran unattended against `lemar@cuzziesnj.com` (~11pm ET).

**Mode:** LIVE (`DRY_RUN=false`)

## Summary
- Vendor menus archived: **21**
- Threads trashed (>12mo, promotions/social/forums): **1**
- Threads over the 200/run cap: **0**

## PART A — Vendor menus archived (labeled `Vendor Menus`, removed from `INBOX`)

Every candidate was opened and confirmed to carry a genuine menu attachment or menu
link before archiving. Precision over recall: most vendor-domain inbox mail this run
turned out to be invoice/AR/collections/negotiation correspondence tied to Cuzzie's
wind-down, not disposable menu blasts — that mail was left untouched in the inbox.

| # | Thread ID | Vendor | Subject | Date |
|---|---|---|---|---|
| 1 | `19b6a7930abcdd05` | Ascend (nbonsanto@awholdings.com) | FINAL CHANCE TO TAKE ADVANTAGE OF EOY DEALS...WEDNESDAY DELIVERY!!!!! | 2025-12-29 |
| 2 | `19b5be2bd155be37` | Ascend (nbonsanto@awholdings.com) | Post Christmas Re-Up? Ascend Has You Covered! | 2025-12-26 |
| 3 | `19b50aac115fc340` | Ascend (nbonsanto@awholdings.com) | 🎄Merry Christmas Ya Filthy Animals \| EOY Deep Discounts Are LIVE From Ascend | 2025-12-24 |
| 4 | `19a9cb90a3961219` | Ascend (nbonsanto@awholdings.com) | IMPORTANT: LAST CALL FOR DELIVERIES BEFORE THE WEEKEND!!! | 2025-11-19 |
| 5 | `1990ab388cd22845` | Ascend (nbonsanto@awholdings.com) | 🚨 LAST CALL: FINAL CHANCE TO GRAB AIRO PRODUCTS | 2025-09-02 |
| 6 | `198ebe5a3cc1307a` | Ascend (nbonsanto@awholdings.com) | 🚨LAST CALL FOR DELIVERY BEFORE LABOR DAY WEEKEND!!! | 2025-08-27 |
| 7 | `199a1b2e3b9b0c22` | Ascend (nbonsanto@awholdings.com) | EXICITING NEWS FROM ASCEND: Simply Herb Disposables Are Finally Here!!! | 2025-10-01 |
| 8 | `197c17b375222781` | Ascend (nbonsanto@awholdings.com) | NEW Month NEW Promos from Ascend | 2025-06-30 |
| 9 | `197acbe740da6db6` | Ascend (nbonsanto@awholdings.com) | STOCK UP FOR 4TH OF JULY WEEKEND! FINAL CALL FOR JUNE DELIVERY! | 2025-06-26 |
| 10 | `197a29e34833e618` | Ascend (nbonsanto@awholdings.com) | HEAT WARNING...NOT TALKING ABOUT THE WEATHER! | 2025-06-24 |
| 11 | `197887749cc714ed` | Ascend (nbonsanto@awholdings.com) | NEW BLACKBERRY SOFT CHEWS!! | 2025-06-19 |
| 12 | `197551776ecd57ea` | Ascend (nbonsanto@awholdings.com) | BLACK BUDDHA IS BACK + AIRO BLADE 2G | 2025-06-09 |
| 13 | `19ffb67a99fc6eb5` | Verano (Tyler.Marsh@verano.com) | Essence Deal $12.50 Still Live ! | 2026-08-13 |
| 14 | `19bd8f237e61f2db` | Verano (Tyler.Marsh@verano.com) | New Swift Lifts Are LIVE ! | 2026-01-20 |
| 15 | `19bb462686689d77` | Verano (Tyler.Marsh@verano.com) | ALL Reserve Flower 20% OFF! | 2026-01-12 |
| 16 | `199bb68b0eda9e72` | Verano (Tyler.Marsh@verano.com) | Hyphen Vape Pre Orders Are LIVE Check It Out ! | 2025-10-06 |
| 17 | `193ad7542c3718f2` | Verano (Tyler.Marsh@verano.com) | Verano NJ-Order Sheet-12/9 | 2024-12-09 |
| 18 | `1a000662987c7369` | APEX Trading / Hamsa (Peter@canfections-nj-llc.apextrading.com) | New Product on APEX! (people like "New") | 2026-08-14 |
| 19 | `19ffb5352dcff36a` | APEX Trading / Little Leaf Labs (Matt@little-leaf-labs.apextrading.com) | 🌙 Moonwalkers Take the Lead — 3G Infused Packs Now Just $20! | 2026-08-13 |
| 20 | `1a001046ef2a67fa` | APEX Trading / Little Leaf Labs (Matt@little-leaf-labs.apextrading.com) | 🚀 20% OFF ALL Dr. Zodiak — The Entire Line Is On Sale! | 2026-08-14 |
| 21 | `1a001b80a6ea04be` | Nova Farms (bbreslow@novafarms.com) | Stashie: Sweeten Up Your August | 2026-08-14 |

## PART B — Trashed (recoverable in Gmail Trash for 30 days)

| # | Thread ID | Sender | Subject | Date |
|---|---|---|---|---|
| 1 | `198af53189118e94` | fromthetimes-noreply@nytimes.com | This world record has stood for 30 years. Is it unbreakable? | 2025-08-15 |

Qualified on all four gates: `older_than:1y`, `category:promotions`, not starred/important,
sender not on the NEVER-TOUCH allowlist.

### Skipped from the PART B candidate set (11 of 12 raw hits) — for the allowlist/tuning record
- 8 threads from `CTA@sos.nj.gov` (NJ Cannabis Training Academy) — skipped: `*.gov` sender,
  covered by the NEVER-TOUCH allowlist regardless of category.
- 1 thread from `surveys@dutchie.com` ("How was your implementation experience with
  dutchie?") — skipped: thread carries IMPORTANT-labeled messages.
- 1 thread from `sales@hamiltonfarms.com` / `breali@hamiltonfarms.com` ("Hamilton Farm's
  Weekly Menu & Go2 8ths release!") — skipped: live order-negotiation thread with
  IMPORTANT-labeled replies, not disposable.
- 1 thread from `iccc@icic.org` ("Apply Now for the ICCC Program") — skipped: thread
  carries an IMPORTANT-labeled message.

## `category:updates` — report-only, never auto-trashed

~201 threads older than 12 months sit in `category:updates`. Sample sender domains seen
this run: `google.com` (Google Voice missed-call/voicemail notices), `jotformsign.com`
(signed-form receipts), `nytimes.com` (breaking-news alerts), `headset.io` (scheduled
reports), `notification.intuit.com` (QuickBooks invoices), `cannazipbags.com`, `adt.com`,
`yerbalist.com`/`esignatures.com`. This category is mixed with real financial/legal mail
per the routine's design — too dangerous to sweep automatically. Flagging for Lemar to
clear by hand if he wants to.

## Notes for future runs

- The vendor-domain seed list in `anchors.md` is, for most domains, dominated by active
  AR/collections/negotiation correspondence tied to Cuzzie's wind-down rather than
  recurring menu blasts. Only **Ascend (awholdings.com)**, **Verano**, **APEX Trading**
  subdomains, and **Nova Farms** showed a genuine recurring "menu blast" pattern tonight.
  The remaining seed-list domains (qccnj.com, terrascend.com, freshcannabis.co,
  kivaconfections.com, illicitgardens.com, harvestmoonfarmsnj.com, budsgoods.com,
  prolificgrowhouse.com, missgrass.com, jerseysmooth.com, thegardensociety.com) had no
  qualifying standalone menu blasts in the inbox tonight — worth re-checking as inbox
  contents change on future runs.
- PART B's IMPORTANT/STARRED floor is tight given roughly half of this inbox carries the
  IMPORTANT label — most promotions/social/forums threads older than a year already carry
  IMPORTANT on at least one message, sharply limiting what's eligible for trash. This is
  expected, correct behavior per the routine's safety floor, not a bug.

## Sources
- gmail: 21 threads archived to `Vendor Menus` (Label_8), 1 thread trashed — see tables above for full IDs.
