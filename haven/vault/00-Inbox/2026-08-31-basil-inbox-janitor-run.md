---
created: 2026-08-31T23:07-04:00
updated: 2026-08-31T23:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-31

Nightly run of the Inbox Janitor routine (`.claude/routines/inbox-janitor.md`), live mode
(`DRY_RUN = false`). Account: `lemar@cuzziesnj.com`.

## Counts

- Vendor menus archived (PART A): **73**
- Threads trashed (PART B): **0** — no candidates found
- Threads over the 200/run cap: 0
- Old `category:updates` threads to flag for manual review: 0

## PART A — vendor menus

Qualifying signal: sender domain on the vendor-domain seed list combined with a
"menu"/"drop"/menu-signal keyword in the subject or snippet. 75 threads matched the
criteria; **73 were archived** (labeled `Vendor Menus`, `INBOX` removed). Vendors
represented: TerrAscend, Verano, Apex Trading (Niche / Goodies / Little Leaf Labs),
Prolific Grow House, North Lake Supply.

**2 threads were left in the inbox, not archived** — they qualified as vendor menus but
carry an undocumented Gmail label `Action Needed` (`Label_374039230306167562`), which
does not appear on any automation-label list anywhere in the repo. Treated as a genuine,
deliberately-applied Lemar filing flag per the "when unsure, don't touch" floor:

- Thread `19e18f27a696c6af` — Verano, "New Menu New Deals !", 2026-05-11
- Thread `19d88c3d4cb37873` — Verano, "NEW ROSIN HYPHEN | 20% OFF MENU| Verano Order Guide DRAFT 4.13.26", 2026-04-13

## PART B — trash sweep

Candidate query `older_than:1y (category:promotions OR category:social OR
category:forums)` returned **zero threads**. Confirmed this isn't a query bug:
`older_than:1y` alone returns 200+ threads (mostly business correspondence, vendor
menus, payment remittances — `category:primary`), but none of them are
Gmail-categorized as promotions/social/forums. `category:updates older_than:1y` was
also empty. Nothing trashed; no audit/recovery list needed this run.

## Anomaly — anchors.md Gmail label registry is stale

The connected mailbox's actual labels don't match `.claude/anchors.md`'s "Gmail
labels" table:

- Anchors says `Label_1` = "Samira"; actual `Label_1` = **"Sweep/Review"**.
- Anchors says Vendor Menus = `Label_8`; actual Vendor Menus label id is
  **`Label_7063567382570959882`** (used for tonight's archiving — no duplicate label
  was created).
- Two labels exist in the account that aren't documented anywhere in anchors.md:
  **"Action Needed"** (`Label_374039230306167562`, 71 msgs / 43 threads) and
  **"Finance Bills"** (`Label_4897882779882705846`, 16 msgs / 9 threads).

I did not edit anchors.md myself: this session's harness assigned a working branch
with an explicit no-direct-push-to-main instruction that conflicts with anchors.md's
own "always push straight to main for `.claude/**`" policy, so I left the registry
untouched rather than resolve that conflict unattended.

**Recommend a live/interactive session reconcile anchors.md's Gmail labels table
against the real account.** The stale `Label_1`–`Label_7` automation-label IDs are what
PART B's never-trash carve-out logic (Samira/Car-Hunt automation labels don't count as
protective) keys off of — if they're wrong for this account, that carve-out could
currently be silently inert or silently wrong. The two undocumented labels should be
registered (or explained if intentional and out of scope for Basil).

## Recovery

Nothing was trashed tonight, so there is no Trash-recovery list. All 73 archived
threads remain fully recoverable — remove the `Vendor Menus` label and re-add `INBOX`
to restore any of them to the inbox.

## Sources
- gmail: 73 threads archived under label `Vendor Menus` (`Label_7063567382570959882`), account `lemar@cuzziesnj.com`
