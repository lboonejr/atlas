---
created: 2026-09-16T23:10:00-04:00
updated: 2026-09-17T14:10:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-09-16

## Run summary (live run, DRY_RUN=false)
Account: lemar@cuzziesnj.com

- Vendor menus archived (PART A): 6
- Threads trashed (PART B, >12mo old promotions/social/forums): 6
- Old `category:updates` threads (report-only, not touched): resultCountEstimate ~201

## PART A — Vendor Menus archived (label added, removed from INBOX)
1. `1a0a643ac3e997db` — Alex@the-happy-farmer-llc.apextrading.com — "Happy Farmer: A Pheno Tommy Staple is BACK!" — 2026-09-15
2. `1a0a5c6c35cfe151` — jb@illicitgardens.com — "⛽️🔥 Illicit NJ Menu- 28G Fat Sacks are BACK- 30%+ testing - for delivery 9/21 - 9/25" — 2026-09-15
3. `1a0a592e59941b63` — carlos@harvestmoonfarmsnj.com — "Harvest Moon Farms Menu 9.15.26" — 2026-09-15
4. `1a0a583d2a935f31` — dan.grandrino@kivaconfections.com — "Kiva Camino/Lost Farm Menu - September to Remember Deals Continue" — 2026-09-15
5. `1a0a543410d4949c` — ndesiderio@terrascend.com — "TerrAscend Menu - $17.50 Legend Carts, $18 Cookies 3.5g & More - 9-15-26" — 2026-09-15
6. `1a0a511202574386` — Peter@canfections-nj-llc.apextrading.com — "APEX Menu Update!" — 2026-09-15

Vendor-domain seed list search returned ~201 inbox candidates total this run; only the
most-recent, unambiguous menu-drop subset was processed under a precision-first read.
Deliberately left alone (not menus): NECANN booth/event invites and launch-party mail,
rep-change/OOO notices, AR statements and collections notices, banking-info-change
notices, pop-up/activation scheduling requests, and mixed personal-correspondence
threads that included Lemar's own replies (e.g. the laddsllc.com and prolificgrowhouse.com
"let's get together" threads). The bulk of the ~201 candidates were this kind of
non-menu vendor mail (invoices, AR, correspondence) rather than fresh menu drops — carries
to the next run rather than guessed at.

## PART B — Trashed (recoverable in Gmail Trash 30 days)
1. `1994f65c37c61388` — fromthetimes-noreply@nytimes.com — "18 high-protein breakfasts you can prep in advance" — 2025-09-15
2. `1994e5fbe28198f2` — sales-authorizeddealernj.com@shared1.ccsend.com — "Authorized Dealer has a fresh Monday Menu for you!" — 2025-09-15
3. `1994e3b1c73c53c9` — andrew@northlake.supply — "Turtle Taffy 10-Pks Restocked, 15% Off • 20% Off Whole-Flower Prerolls" — 2025-09-15
4. `1994df5b720dc756` — noreply@aiq.com — "Maximize Your AIQ Investment with Terpli" — 2025-09-15
5. `1994dcaed1de77e9` — sales@hamiltonfarms.com — "Hamilton Farms weekly menu" — 2025-09-15
6. `1994da8dd8ddcc88` — Jade@hearth-wellness-llc.apextrading.com — "Bada Bing, Bada Boom 🎰💨 — Honeydew Boba Is Here" — 2025-09-15

All six: `older_than:1y`, `category:promotions`, no IMPORTANT/STARRED label, no genuine
filing label, sender domain not on the NEVER-TOUCH allowlist (northlake.supply and the
apextrading.com subdomain are vendor-seed-list domains, which the runbook explicitly
marks trashable once >12 months old, since PART A already archived their recent menus).

Candidates skipped: the `older_than:1y (category:promotions OR category:social OR
category:forums) -is:starred -is:important` query surfaced 29 threads. 23 were protected:
15 from `CTA@sos.nj.gov` (`*.gov`, NEVER-TOUCH allowlist), 6 from `parkebank@parkebank.com`
(NEVER-TOUCH allowlist), and 2 threads (a dutchie.com implementation-survey thread and an
icic.org program-invite thread) that carried IMPORTANT on at least one message in the
thread. No candidate hit the 200/run cap.

## PART B — report-only (`category:updates`, never auto-trashed)
resultCountEstimate ~201 threads older than 1 year in this category. Dominated by:
`jotform.com` / `jotformsign.com` (form-fill and e-sign notifications), `headset.io`
(already NEVER-TOUCH allowlisted), Google system notices (`voice-noreply@google.com`,
`googleplay-noreply@google.com`, `looker-studio-noreply@google.com`,
`drive-shares-dm-noreply@google.com`), `nytimes.com` (breaking-news/newsletter alerts),
`checkr.com`, `distru.com`, `weedmaps.com`, `theathletic.com`, `leaflink.com`,
`redditmail.com`, and `quickbooks@notification.intuit.com` (already NEVER-TOUCH
allowlisted). Left untouched per the runbook — surfaced here for Lemar to clear by hand
if he wants.

No repo/tool unreachability this run. `DRY_RUN=false` (per `.claude/routines/inbox-janitor.md`
at run time). Gmail label check (`list_labels`) confirmed Vendor Menus = `Label_8`,
matching anchors.md.

## Sources
- gmail: account lemar@cuzziesnj.com, PART A + PART B thread IDs above
