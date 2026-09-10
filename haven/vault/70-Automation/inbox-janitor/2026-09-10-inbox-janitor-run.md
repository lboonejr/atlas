---
created: 2026-09-10T23:07-04:00
updated: 2026-09-10T12:08-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-09-10 (Basil)

Live run (`DRY_RUN = false`) of `.claude/routines/inbox-janitor.md` against
`lemar@cuzziesnj.com`.

## Summary
- Vendor menus archived (Vendor Menus label applied, removed from Inbox): **3**
- Threads trashed (>12mo, promotions/social/forums, not important/starred, not allowlisted): **7**
- Threads over the 200/run cap: **0**

## PART A — vendor menus archived (3)

| Thread ID | Sender | Subject |
|---|---|---|
| 1a0870c23b8f9c9f | allanf@harvestmoonfarmsnj.com | 🔥 Mid-Week Restock – Get Those Orders In! |
| 1a08680b1f3e0a1a | nbonsanto@awholdings.com | Ascend Updated Menu \| Sativa Pre Rolls + Let's Link Up at NECANN |
| 1a0867d1dc4bcb68 | kbreiner@qccnj.com | QCC NJ Menu 9.9.26 - Time to Re-stock Post LDW! |

Skipped from PART A: `laddsllc.com` "Let's get together this week? (+ Monday Menu Drop!)"
thread (1a033dac94bb1ec5) — later replies in that same thread carry Gmail's `IMPORTANT`
label and are real 1:1 correspondence with Hillary King about Cuzzie's being closed/the
Camden transition, not a menu blast. Left untouched per the never-touch-important floor.

## PART B — trash sweep audit (7 threads, recoverable in Gmail Trash 30 days)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 19930216e3aeef7f | Their beach home is a driveway | fromthetimes-noreply@nytimes.com | 2025-09-09 |
| 1992fa705454a185 | Tomorrow: Discover AIQ Loops @ Hall of Flowers ✨ 🔥 | noreply@aiq.com | 2025-09-09 |
| 1992f8b8715f3b77 | 👉 This will be on 9/8-9/19! Find out how to get your free pull-tab and win! 👉 | email@em.sherwin-williams.com | 2025-09-09 |
| 1992f43fa0eeb837 | 🎥 Hands-on AI: Build live with Make experts | info@make.com | 2025-09-09 |
| 1992ef086d812128 | 🚀 Smooth Elevation is HERE | marketing.us@terrascend.com | 2025-09-09 |
| 1992cbfd944d2d0b | "Picked too early?" (r/gardening digest) | noreply@redditmail.com | 2025-09-09 |
| 19926cb816bc1a18 | Limited stock on half gram pre rolls | Francisco@high-grass-farms.apextrading.com | 2025-09-08 |

Skipped from the 29-thread raw candidate pool (`older_than:1y (category:promotions OR
category:social OR category:forums)`, not starred/important at the query level):
- 8 threads from `parkebank.com` — NEVER-TOUCH allowlist.
- 9 threads from `CTA@sos.nj.gov` — excluded under the allowlist's `*.gov` rule.
- 3 threads where Gmail surfaced the whole thread despite the `-is:important` filter
  (per the tool's own note: a thread appears if *any* message doesn't match the
  exclusion) because another message in the same thread actually carries `IMPORTANT`:
  a `dutchie.com` implementation-survey thread, a Hamilton Farms "Weekly Menu & Go2 8ths
  release" thread (real order-terms correspondence with a customer), and an ICCC
  "mini-MBA" thread with an `IMPORTANT`-labeled duplicate message.

## PART B report-only — old `category:updates` (never auto-trashed)

~201 threads older than 12 months sit in `category:updates`. Sample sender domains seen
(the expected mix of real operational mail and marketing that the runbook says is too
dangerous to sweep): `nytimes.com` (breaking-news + sponsored digest), `jotform.com` /
`jotformsign.com` (register-float approvals, e-signed checklists), `headset.io`
(scheduled analytics reports), `extraspace.com` (storage-unit billing, including a past-due
notice), `checkr.com`, `theathletic.com`, `flowhub.com`, Google Voice missed-call
notices, `wm.com` (Waste Management payment receipts). Left untouched; Lemar can clear
by hand if desired.

## Mode

`DRY_RUN = false` — this was a live run; the actions above were taken for real.

## Sources
- gmail: 3 threads labeled `Vendor Menus` + removed from Inbox (IDs above)
- gmail: 7 threads moved to Trash (IDs above)
