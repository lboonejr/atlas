---
created: 2026-08-06T23:15-04:00
updated: 2026-08-06T23:20-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-06

Run date: 2026-08-06 (~11pm ET trigger, live via `trig_01JE6TpvqAnawkETpx64vvX9`)
Mode: **LIVE** (`DRY_RUN = false`)
Account acted on: `lemar@cuzziesnj.com`

## PART A — Vendor Menus archived: 36 threads

Criteria: vendor-domain seed list (anchors) combined with an explicit menu / order-sheet /
order-guide subject or body signal, plus an attachment. Precision over recall — weak
signals (generic marketing blasts with no menu/attachment language) were left in the inbox.
Applied the runbook's blanket safety floor to PART A as well as PART B: any thread carrying
`IMPORTANT` or `STARRED` anywhere in the thread was skipped, even if it looked like a menu.
Action taken per thread: `label_thread` → `Vendor Menus` (`Label_8`), then `unlabel_thread`
→ removed `INBOX`. Threads remain in All Mail under the label, just out of the inbox.

Archived (id · subject · sender):
- 19fd27206760e7d1 · Kiva Camino/Lost Farm Menu - B2G1 Lost Farm & B3G1 Camino (Must Carry Lost Farm) · dan.grandrino@kivaconfections.com
- 19fd2410b726fc24 · QCC NJ Menu 8.5.26 | Fresh Drop: Lipsmackerz Has Returned · kbreiner@qccnj.com
- 19fd217ef23e91ff · UPDATED ASCEND MENU | NEW RSO GUMMIES + NEW OZONE & SIMPLY HERB STRAINS! · nbonsanto@awholdings.com
- 197a77345faa7f2c · LAST CALL FOR FRIDAY DELIVERY!! + BLACK BUDDHA IS STOCKED UP · nbonsanto@awholdings.com
- 1979d5d9b19300fe · PRIDE PROMOS IN FULL EFFECT AND WONT LAST LONG!! · nbonsanto@awholdings.com
- 197791ace0f627b4 · PRIDE MONTH PROMO IN FULL EFFECT!! · nbonsanto@awholdings.com
- 19769cbb8d2a50fe · LAST DAY TO TAKE ADVANTAGE OF FATHER'S DAY PROMO!! · nbonsanto@awholdings.com
- 1975f3bdef9337e4 · PRIDE MONTH + FATHER'S DAY PROMOS · nbonsanto@awholdings.com
- 1969112d42e5fcf6 · 🔥 Fresh Drops, Limited Stock & Must-Haves from Ascend! · nbonsanto@awholdings.com
- 195a653547c10c88 · New Verano Order Sheet !🔥 · Tyler.Marsh@verano.com
- 19539e4f9e08f0ca · New Order Sheet · Tyler.Marsh@verano.com
- 19515cc4c05e375e · New Verano Order Sheet ! · Tyler.Marsh@verano.com
- 194f1790ee18393c · Verano Order Sheet GO BIRDS ! · Tyler.Marsh@verano.com
- 194cd5df564e2a40 · Verano Order Sheet 2.3.2025 · Tyler.Marsh@verano.com
- 194a8c4d7a1aa384 · New Verano Order Sheet ! RSO Guaps Reloaded ! · Tyler.Marsh@verano.com
- 1948513f92806d16 · Verano Order Sheet...New 100MG Guaps Are Live ! · Tyler.Marsh@verano.com
- 194615f238c12c3d · Updated Order Sheet Attached 1.13 · Tyler.Marsh@verano.com
- 1946117f6d837913 · Verano Order Sheet 1/13 · Tyler.Marsh@verano.com
- 1943cfce3daad333 · Verano Order Sheet 1/6 · Tyler.Marsh@verano.com
- 1941936f84e42017 · 12/30 Order Sheet Happy New Year ! · Tyler.Marsh@verano.com
- 193f4e846e7bf11b · Order Sheet 12.23 Happy Holidays ! · Tyler.Marsh@verano.com
- 193d0cb408a79e08 · Updated Order Sheet Attached ! · Tyler.Marsh@verano.com
- 193d0c67836d34dd · Verano Order Sheet 12.16 · Tyler.Marsh@verano.com
- 193892793b4914aa · Verano Brands Order Guide 12/2/24 · Matthew.Sobon@verano.com
- 19364c004687c257 · Verano Brands Order Guide 11/25/24 · Matthew.Sobon@verano.com
- 193415a6881d23c0 · Verano Brands Order Guide 11/18/24 · Matthew.Sobon@verano.com
- 192f8ca336c783e3 · Verano Brands Order Guide 11/4 · Matthew.Sobon@verano.com
- 192d4a5b9caeffd5 · Verano Brands Order Guide 10/28/24 · Matthew.Sobon@verano.com
- 192c56c3b313fc9f · Verano - Order Sheet last call FLASH SALE - 10.25.24 · Gianna.Nitti@verano.com
- 1928cb3cb2d726fc · Verano Order Guide 10.14 · Lawrence.Sidari@verano.com
- 19272b6fb679a2bb · Verano Order Guide 10.9 · Lawrence.Sidari@verano.com
- 192682f7bd46948b · Verano Order Guide 10/7 · Lawrence.Sidari@verano.com
- 1925843e247ec8e0 · Verano Order Guide 10.4 - Final call ! · Lawrence.Sidari@verano.com
- 1925334fde66c834 · Verano Order Guide 10/3 · Lawrence.Sidari@verano.com
- 192444581778267a · Verano Order Guide 9/30 · Lawrence.Sidari@verano.com
- 1923491ef8055b49 · Verano Order Guide - Final call · Lawrence.Sidari@verano.com

**Backlog note:** the vendor-domain + attachment search matched ~201 inbox threads; only
two pages (91 threads) were reviewed this run to keep precision over recall. The remaining
backlog will keep surfacing on future nightly runs — no action needed on it now.

## PART B — Trash sweep: 5 threads trashed

22 candidates matched `older_than:1y (category:promotions OR category:social OR
category:forums) -is:starred -is:important`. 17 were skipped by the NEVER-TOUCH allowlist
or the thread-level IMPORTANT floor:
- 7 from `parkebank.com` (allowlist domain)
- 7 from `CTA@sos.nj.gov` (`*.gov` allowlist)
- 3 from threads that carried an `IMPORTANT`-labeled message elsewhere in the same thread
  (a dutchie.com implementation-survey thread, a hamiltonfarms.com order-minimum
  conversation, an icic.org ICCC program thread) — real conversations, not blasts.

Trashed (recoverable from Gmail Trash for 30 days):
- 1987c325042115d7 · "Allstar Lineup!" · wholesale@verano.com · 2025-08-05
- 1987bdd86d7f4907 · "Make your social content shine" · marketing@engage.canva.com · 2025-08-05
- 1987ae7a6b3aae53 · "Got a Minute? Share Your Thoughts With Us." · info@alpharoot.com · 2025-08-05
- 1987ade6da6d33e8 · "Do you have what it takes to win the Cup? 🏆" · marc@necann.com · 2025-08-05
- 1987acb33b5f89d9 · "Last Chance: RSVP for Tomorrow's Livestream with Trulieve's Iram Cesani" · hello@surfside.io · 2025-08-05

Per-run cap (200) not reached — no candidates left over for tomorrow.

**`category:updates` — report-only, never auto-trashed:** ~201 threads older than 12
months sit in this category. Sample sender domains: `notification.intuit.com` (QuickBooks
— allowlisted anyway), `parkebank.com` (allowlisted), `headset.io` (allowlisted),
`email.weedmaps.com`, `jotform.com` / `jotformsign.com`, `flowhub.com`, `monday.com`,
`voice-noreply@google.com` (Google Voice), `theathletic.com`, `redditmail.com`,
`noreply@mail.authorize.net`. Worth a manual pass on the newsletter/notification ones
(Weedmaps, The Athletic, Reddit); the financial/legal ones are correctly left alone.

## Totals

36 vendor menus archived · 5 old items trashed (>12mo) · 0 over the per-run cap.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox sweep, 2026-08-06
