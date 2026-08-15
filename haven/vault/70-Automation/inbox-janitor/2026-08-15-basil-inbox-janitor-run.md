---
created: 2026-08-15T23:07-04:00
updated: 2026-08-15T08:04-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-15

Live run (`DRY_RUN=false`). Account acted on: `lemar@cuzziesnj.com` (Basil's only scope,
per anchors).

## PART A — vendor menus archived: 5

Labeled `Vendor Menus` and removed from `INBOX` (reversible, still in All Mail):

1. Thread `1a000c1842b3cfef` — "🔥 Friday Wholesale Menu - Harvest Moon Farms" — allanf@harvestmoonfarmsnj.com — 2026-08-14
2. Thread `1a000959e76e09e7` — "Ascend Menu!! SIMPLY HERB & HIGH WIRED SHAKE RESTOCKED!! OZONE RSO GUMMIES!!" — mgargiule@awholdings.com — 2026-08-14
3. Thread `19ff669231a4a79a` — "QCC NJ Menu - Hot New SKUs & Disposables Back to Menu!" — kbreiner@qccnj.com — 2026-08-12
4. Thread `19b37791ca1675fb` — "Fresh Grow Holiday Sale 20% off | Zip Restock" — Kathy@freshcannabis.co — 2025-12-19
5. Thread `196490580b653b90` — "420 Restock?? We've Got You Covered!" — nbonsanto@awholdings.com — 2025-04-18

Skipped as only weakly a menu (left in inbox): AR statements, invoices, collections
notices, event invites, and genuine correspondence threads (e.g. "Current wholesale
menu?", "Update on Vendor Menu Submissions", "Request for 7g Savvy Restock Notification")
from the same vendor domains — these are substantive business threads, not marketing
blasts, so precision-over-recall left them alone.

## PART B — trash sweep: 9 trashed, 0 over the 200/run cap

Candidate set: `older_than:1y (category:promotions OR category:social OR category:forums)`,
every gate clause verified per thread (not starred, not important on **any** message in
the thread, no genuine filing label, sender domain not on the NEVER-TOUCH allowlist):

1. Thread `198aa7f317c8decd` — "Business tools to help you do more" — tmobileforbusiness@tmobiz.t-mobile.com — 2025-08-14
2. Thread `198aa6891f0e49fe` — "Re-up on your favorites!" — wholesale@verano.com — 2025-08-14
3. Thread `198a9c42f92f4963` — "AI frontends are cool. Yours can be local." — team@m.ngrok.com — 2025-08-14
4. Thread `198a996ba116a384` — "Feelin' Cherrymellow? 🍒 You Will After This‼️" — marketing.us@terrascend.com — 2025-08-14
5. Thread `198a98b773afc3af` — "Join Us Live: Surf Sessions with Story Cannabis VP of Marketing" — hello@surfside.io — 2025-08-14
6. Thread `198a900c39439952` — "🌊 Waves '25: Agenda preview incoming! 🤖" — make-events@make.com — 2025-08-14
7. Thread `198a8e5ceea1e5ae` — "$150 OFF Your Next Purchase is Still Waiting!" — email@em.sherwin-williams.com — 2025-08-14
8. Thread `198a5203cdceb082` — "Deals and Steals" — wholesale@verano.com — 2025-08-13
9. Thread `198a2a8bb55865d6` — "ONYX Live Apex Menu Link" — Phil@sussex-cultivation.apextrading.com — 2025-08-13

All 9 recoverable from Gmail Trash for 30 days from trash date.

### Candidates found but explicitly skipped (never-trash floor): 10

- 7 threads from `CTA@sos.nj.gov` (NJ Secretary of State — protected under the `*.gov`
  NEVER-TOUCH allowlist clause)
- Thread "How was your implementation experience with dutchie?" (surveys@dutchie.com) —
  thread contains IMPORTANT-labeled messages
- Thread "Hamilton Farm's Weekly Menu & Go2 8ths release!" (sales@hamiltonfarms.com) —
  thread contains substantive IMPORTANT-labeled order-terms correspondence
- Thread "Apply Now for the ICCC Program..." (iccc@icic.org) — contains an
  IMPORTANT-labeled message

These were caught by inspecting every message in a matched thread, not just the one
that satisfied the search query — the search tool can surface a whole thread on one
unstarred/unimportant message even when a sibling message in that thread is protected.

## category:updates — report-only, never auto-trashed

~201 threads older than 1 year in `category:updates`. Recurring sender domains observed:
`jotform.com` / `jotformsign.com` (register-float approvals, signed forms),
`voice-noreply@google.com` (missed-call notices), `headset.io` (scheduled report
emails), `messaging.squareup.com` (invoice paid/received notices), `distru.com` (vendor
invoices), `notifications@monday.com` (automation-error alerts), `CTA@sos.nj.gov`
(newsletter), plus subscription noise from `nytimes.com` / `theathletic.com` /
`redditmail.com`. Left alone per the runbook — this category mixes real financial/legal
mail with ads, too dangerous to sweep unattended. Flagged here if Lemar wants to clear
any by hand.

## Totals

5 menus archived · 9 threads trashed · 0 over cap · 10 candidates explicitly protected
and skipped · ~201 old `updates` threads noted report-only.

## Sources
- gmail: 5 archived + 9 trashed thread IDs listed above (connected account `lemar@cuzziesnj.com`)
