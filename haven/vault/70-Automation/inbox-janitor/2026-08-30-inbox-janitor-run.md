---
created: 2026-08-30T23:07-04:00
updated: 2026-08-30T08:03:50-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor — 2026-08-30 (live run)

Basil's nightly Gmail cleanup, live mode (`DRY_RUN = false`). Account: `lemar@cuzziesnj.com`.

## Run summary
- Vendor menus archived (PART A): **2**
- Threads trashed (PART B, >12mo old, promotions/social/forums): **5**
- Threads over the 200/run cap: **0**
- Trash candidates skipped — NEVER-TOUCH allowlist domain: **18**
  (`CTA@sos.nj.gov` ×10 — `*.gov` allowlist rule; `parkebank@parkebank.com` ×8 — `parkebank.com` on allowlist)
- Trash candidates skipped — is:important guard (thread contained an IMPORTANT-labeled message): **3**
  (`surveys@dutchie.com` thread `19644c6a0e498f47`; `sales@hamiltonfarms.com` thread `196110a96c91e798`; `iccc@icic.org` thread `1826944b41c19b7a`)

No repo/tool access issues this run. Every action taken is reversible: archived menus
can be re-added to the inbox by removing the `Vendor Menus` label; trashed threads sit
in Gmail Trash for 30 days and can be restored with the thread IDs below.

## PART A — vendor menus archived
Labeled `Vendor Menus` (`Label_8`) and removed from `INBOX`. Never trashed.

1. Thread `1a03e6a1a6e420a7` — "QCC NJ Menu 8.26.26 - New Labor Day Weekend Promos!" — from `kbreiner@qccnj.com` — 2026-08-26
2. Thread `1a03e52094ce5769` — "Ascend Updated Menu | Order by 12pm Today for Delivery Before the Weekend + Ozone 14g Restock" — from `nbonsanto@awholdings.com` — 2026-08-26

A broader domain-only search on the vendor seed list surfaced ~201 results, but nearly
all of those were promos, invoices, AR/collections notices, pop-up/activation requests,
or live back-and-forth correspondence rather than standalone vendor-menu blasts — e.g.
the `laddsllc.com` "Monday Menu Drop" thread and the `illicitgardens.com` /
`terrascend.com` / `awholdings.com` "menu" threads were skipped because they carry
substantive ongoing conversation, not a simple blast (precision over recall, per the
runbook). Only the two above were clean single-message vendor-menu blasts.

## PART B — trash audit (recoverable in Gmail Trash for 30 days)

1. Thread `198f78058ecc65c5` — "Generate AI presenters in moments with D-ID AI Presenter" — from `marketing@engage.canva.com` — 2025-08-29
2. Thread `198f6ac35f38b6c6` — "📢 It's a Big Week: New Products Incoming..." — from `info@fernway.com` — 2025-08-29
3. Thread `198f667d7f0ec36d` — "IMPORTANT FALL LAWN CARE" — from `salexander-vhrrental.com@voorheeshardware.ccsend.com` — 2025-08-29
4. Thread `198f606c9e4b81c2` — "Let's Talk Packaging at NECANN NJ" — from `marketing@cannazipbags.com` — 2025-08-29
5. Thread `198f5e7c6b8e8407` — "Your Teams Insider: Level up your workflow today" — from `canvateams@engage.canva.com` — 2025-08-29

## category:updates — report only, never auto-trashed

Roughly **201** threads older than 12 months sit in `category:updates`. This category is
never swept (it mixes invoices/bank/payroll/legal receipts with ads — too dangerous per
the runbook). Sender domains seen in a recon sample, for Lemar to clear by hand if he
wants: `jotformsign.com` / `jotform.com`, `evite.com` (`mailva.evite.com`),
`nytimes.com` (breaking-news alerts), `readyrefresh.com`, `headset.io` (NEVER-TOUCH
allowlisted — correctly untouched either way), `emeraldintel.ai`,
`voice-noreply@google.com`. Nothing in this category was touched.

## Sources
- gmail: 26 candidate threads reviewed for PART B (`older_than:1y (category:promotions OR category:social OR category:forums) -is:starred -is:important`); 5 trashed, 21 skipped per allowlist/important guard.
- gmail: vendor-domain search for PART A (~201 broad matches, narrowed to 6 subject-menu-signal matches, 2 archived).
