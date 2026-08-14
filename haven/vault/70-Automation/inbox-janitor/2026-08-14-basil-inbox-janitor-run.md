---
created: 2026-08-14T23:07-04:00
updated: 2026-08-14T08:10:25-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run, 2026-08-14 (LIVE, DRY_RUN=false)

Nightly Gmail cleanup on `lemar@cuzziesnj.com`. Archived 2 vendor menus, trashed 4 old
disposable threads (>12mo), left everything else alone. Well under the 200-thread/run cap.

## PART A — vendor menus archived (labeled `Vendor Menus`, removed from `INBOX`)

1. Thread `19ffc7874393e98a` — "Fresh Grow Menu | Beach Walker Buy 2 Get 1 Free Sale!🌴" —
   from Kathy@freshcannabis.co — 2026-08-13
2. Thread `19ffbf7e345810ef` — "TerrAscend Menu: New Rosin Gummies & Genetics + $72 Legend
   28g, $15 Kind Tree 3.5g - 8-13-26" — from ndesiderio@terrascend.com — 2026-08-13

Three other vendor-menu-signal matches were found but **skipped** under the never-touch
hard floor:
- `19ff669231a4a79a` (qccnj.com "QCC NJ Menu") — carries the `IMPORTANT` label
- `1953984f582708f1` (terrascend.com "Update on Vendor Menu Submissions") — carries a
  `STARRED` message
- `18bba3d6fdd56769` (awholdings.com "Current wholesale menu?") — carries the `IMPORTANT`
  label

## PART B — trash sweep (recoverable in Gmail Trash for 30 days)

Candidate set: `older_than:1y (category:promotions OR category:social OR category:forums)`,
21 threads matched. 4 trashed, 17 skipped by the safety floor.

**Trashed** — thread ID · subject · sender · date:
1. `198a566d2724c98f` · "A $5 certificate just for you, Lemar. 🎉" · BestBuy@email.bestbuy.com
   · 2025-08-13
2. `198a43d5ea475df7` · "🎉 Your first ZapConnect? Let's make it unforgettable." ·
   events@send.zapier.com · 2025-08-13
3. `198a414f7704a615` · "Are you part of the industry's future? Prove it." ·
   marc@necann.com · 2025-08-13
4. `198a3889ee3cdd54` · "For this 5-min Glow Up: Make plain images eye-catching" ·
   marketing@engage.canva.com · 2025-08-13

**Skipped** (17 of the 21 candidates), by reason:
- 6 threads from `parkebank@parkebank.com` — sender domain on the NEVER-TOUCH allowlist
- 6 threads from `CTA@sos.nj.gov` — `*.gov` on the NEVER-TOUCH allowlist
- `19644c6a0e498f47` (surveys@dutchie.com, dutchie implementation survey) — carries
  `IMPORTANT`-labeled messages
- `196110a96c91e798` (sales@hamiltonfarms.com, "Hamilton Farm's Weekly Menu & Go2 8ths
  release!") — carries `IMPORTANT`-labeled messages; also live correspondence with Donte
  re: order minimums, not disposable
- `1826944b41c19b7a` (iccc@icic.org, "Apply Now for the ICCC Program") — carries an
  `IMPORTANT`-labeled message
- 2 more threads counted above under PART A's skip list (vendor-menu candidates, not
  trash candidates — listed there, not double-counted here)

Per-run cap (200 threads): not approached.

## `category:updates` — report-only, never auto-trashed

`in:inbox older_than:1y category:updates` = **201 threads**. Per the runbook this
category mixes invoices/bank/payroll/legal receipts with ads, so it is never swept.
Sample sender domains seen this run, for Lemar to clear by hand if he wants:
`jotform.com` / `jotformsign.com` (approvals, e-signatures) · `voice-noreply@google.com`
(Google Voice missed-call notices) · `nytimes.com` (newsletters) · `slack-mail.com`
(Slack notifications) · `distru.com` (password resets).

## Recovery

All 4 trashed threads sit in Gmail Trash for 30 days and can be restored by thread ID
above if any was a mistake.

## Sources
- gmail: search `in:inbox older_than:1y (category:promotions OR category:social OR
  category:forums) -is:starred -is:important` and the vendor-menu queries above, run
  2026-08-14 (Basil nightly routine)
