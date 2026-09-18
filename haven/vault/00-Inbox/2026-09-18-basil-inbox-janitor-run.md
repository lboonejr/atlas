---
created: 2026-09-18T23:07-04:00
updated: 2026-09-18T23:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-09-18

Gmail account acted on: `lemar@cuzziesnj.com`. Live run (`DRY_RUN=false`).

## Summary
- Vendor menus archived (out of inbox, kept under `Vendor Menus` label): **4**
- Threads trashed (old, clearly unnecessary, >12mo): **5**
- Threads over the 200/run cap: **0**
- Old `category:updates` threads found (report-only, NOT touched): **201** (estimate)

## PART A — vendor menus archived (4)

Searched the inbox for vendor-domain-seed-list senders with an attachment AND a
menu-signal subject (combination-of-signals rule, precision over recall). 7 raw
matches; 3 were multi-message personal/business correspondence threads (not pure
marketing blasts — some carried STARRED/IMPORTANT messages) and were left alone per
"when a thread is only weakly a menu, skip it."

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| `1a0b0ac33fdf9b68` | Harvest Moon Farms Menu 9.17.26 | carlos@harvestmoonfarmsnj.com | 2026-09-17 |
| `1a0b098855aae277` | TerrAscend Menu: New Products Added Since Tuesday, 35% OFF Legend Carts, $18 Cookies 3.5g, & MOREE! | ebrody@terrascend.com | 2026-09-17 |
| `1a0afaaf246fb217` | SEPTEMBER TO REMEMBER CONTINUES - Kiva Camino/Lost Farm Menu - NECANN WEEKEND | dan.grandrino@kivaconfections.com | 2026-09-17 |
| `1a0af9476d8048cf` | Bud's Goods Menu - NEW 14G FLOWER AND PARTY PACKS!! | mzaidi@budsgoods.com | 2026-09-17 |

Skipped (real correspondence, not pure menu blasts — left in the inbox untouched):
- jerseysmooth.com thread "Let's get together this week? (+ Monday Menu Drop!)" — personal scheduling conversation with Hillary King, IMPORTANT-labeled messages present.
- terrascend.com thread "Update on Vendor Menu Submissions" — STARRED + IMPORTANT, a business-agreement setup conversation, not a menu itself.
- awholdings.com thread "Current wholesale menu?" — IMPORTANT-labeled wholesale-supply negotiation thread.

## PART B — trash sweep audit (5 trashed, recoverable in Gmail Trash for 30 days)

Candidate set: `older_than:1y (category:promotions OR category:social OR category:forums) -is:starred -is:important` → 33 raw candidates.

28 skipped:
- 12 protected by the `*.nj.gov` allowlist rule (all `CTA@sos.nj.gov`)
- 8 protected by the `parkebank.com` allowlist entry
- 5 already carrying the `Vendor Menus` label (treated as a protective filing label — conservative read, since it is not on the routine's explicit non-protective/automation-label list)
- 3 contained at least one IMPORTANT-labeled message even though the thread matched the search (dutchie.com survey thread, hamiltonfarms.com wholesale-menu negotiation thread, icic.org thread)

5 trashed:

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| `1995950519b04851` | Wanted: Your thoughts on AIQ 🤝 | noreply@aiq.com | 2025-09-17 |
| `199586e343c31d75` | News & Resources for Small Businesses | noreply@mail.lendistry.com | 2025-09-17 |
| `199583871f5995e1` | Discover the Secrets to Retail Success \| FASTSIGNS | 2115@fastsigns.com | 2025-09-17 |
| `19958361d9ce1d73` | Webinar Reminder_September 30th | jonathon@hoodieanalytics.com | 2025-09-17 |
| `199578ce364e4fd2` | Our favorite boxed macaroni and cheese | fromthetimes-noreply@nytimes.com | 2025-09-17 |

## Report-only: old `category:updates` (201 threads, untouched)

Per the runbook, `category:updates` is never auto-trashed — recon shows it mixes
invoices, bank notices, payroll, and insurance/legal receipts with ads. Sample sender
domains observed this run (Lemar may want to clear these by hand):
nytimes.com, jotform.com / jotformsign.com, headset.io, softtouchpos.co,
readyrefresh.com (billing), progressive.com (e.progressive.com), adt.com,
rankreallyhigh.com, distru.com.

## Notes
- Repo/tools were reachable throughout; no degraded-run warning needed.
- Per-run cap (200 trashed/run) was not approached.

## Sources
- gmail: 4 threads archived to `Vendor Menus` (Label_8), 5 threads trashed — IDs above
