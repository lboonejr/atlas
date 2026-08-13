---
created: 2026-08-13T23:15-04:00
updated: 2026-08-13T23:15-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run 2026-08-13

Nightly Gmail cleanup, live run (`DRY_RUN = false`). Account: `lemar@cuzziesnj.com`.

## PART A — vendor menus archived (5)

Labeled `Vendor Menus` (`Label_8`) and removed `INBOX`:

1. `19ff77354305f7ed` · "What Can Your Customers Get for Under $20? 👀" · alex@jerseysmooth.com · 2026-08-12
2. `19ff6c3bbcbdbac7` · "Harvest Moon Farms Menu Week 2 August" · carlos@harvestmoonfarmsnj.com · 2026-08-12
3. `19ff652aa5a4ec25` · "Ascend Menu!! GUAVA CANDY CRUNCH IN 3.5G & 7G! OZONE RSO GUMMIES!! 🔥" · mgargiule@awholdings.com · 2026-08-12
4. `19fecf4014e1d69d` · "Gummy Bundle: The Price is Right" · bbreslow@novafarms.com · 2026-08-10
5. `19fec9dbd9c9e35c` · "🚀 DANK Takes Center Stage! New Flavors, $15 Carts & More Retail Favorites Inside 💨🔥" · Matt@little-leaf-labs.apextrading.com · 2026-08-10

Screened out weaker/ambiguous vendor-domain mail — event invites, admin/policy notices,
and real order or payment correspondence carrying an `IMPORTANT`-labeled reply — per the
runbook's "precision over recall" rule.

## PART B — trash sweep (4 trashed, 0 over the 200/run cap)

Candidate query: `older_than:1y (category:promotions OR category:social OR category:forums)
-is:starred -is:important` → 21 candidates. 17 were skipped:
- `parkebank@parkebank.com` and `CTA@sos.nj.gov` hits — both on the NEVER-TOUCH allowlist
  (`parkebank.com` explicitly, `*.gov` as a standing rule).
- Threads that carried at least one `IMPORTANT`-labeled message even though the lead
  message wasn't flagged — the Hamilton Farms order-terms thread, the Dutchie
  implementation-survey thread, and the ICCC mini-MBA thread. All real correspondence,
  not disposable.

Trashed (recoverable in Gmail Trash for 30 days):

1. `198a016da20ac48c` · "Quiz: Can you place 8 events in chronological order?" · fromthetimes-noreply@nytimes.com · 2025-08-12
2. `1989f98041c709db` · "Top Zaps for the apps you use" · learn@send.zapier.com · 2025-08-12
3. `1989ed7cc6201c56` · "Say hello to Colormix® 2026. Say yes to Fall SprayBuy® Savings!" · email@em.sherwin-williams.com · 2025-08-12
4. `1989e2728b1d3135` · "Discover how 2 families created New Jersey's hottest dispensary 🔥" · hello@flowhub.com · 2025-08-12

## Report-only — `category:updates`

`older_than:1y category:updates` → ~201 threads. Not swept — this category mixes
invoices, bank notices, payroll, and legal/insurance receipts in with ads, and the
runbook marks it too dangerous to auto-trash. No action taken. Frequent senders Lemar
may want to clear by hand:
- `voice-noreply@google.com` — Google Voice missed-call/voicemail notices (high volume)
- `quickbooks@notification.intuit.com` — invoice receipts (also NEVER-TOUCH allowlisted)
- `info@headset.io` — scheduled report emails (also NEVER-TOUCH allowlisted)
- `noreply@jotformsign.com` — signed-document confirmations
- `breakingnews-noreply@nytimes.com` — news alerts
- `notifications@monday.com` — automation-error notices

## Notes

No starred, important, allowlisted, or user-labeled thread was touched. Repo and tools
were reachable throughout — no degraded-run warning needed.

## Sources
- gmail: search `older_than:1y (category:promotions OR category:social OR category:forums)` — PART B candidate set
- gmail: search vendor-domain + menu-signal queries — PART A candidate set
