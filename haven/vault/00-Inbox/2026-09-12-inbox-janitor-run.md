---
created: 2026-09-12T23:07-04:00
updated: 2026-09-12T23:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-09-12 (Basil, LIVE)

Basil (Inbox Janitor) nightly run, 2026-09-12, LIVE mode (`DRY_RUN=false` per the runbook).

## Summary
- Archived 3 vendor-menu threads out of the inbox (labeled `Vendor Menus` / `Label_8`, removed `INBOX`).
- Trashed 9 old (>12mo) promotional/social/forums threads. 0 threads left over the 200/run cap.
- Report-only: 201 threads in `category:updates` older than 12 months were left untouched per the runbook (invoices, Google Voice missed-call notices, NYTimes breaking-news alerts, CTA/sos.nj.gov updates — see notes below).

## PART A — Vendor menus archived (3)
1. `1a09132d8c87571d` · "Kiva Camino/Lost Farm Menu - September Week 2 - SEPTEMBER TO REMEMBER DEALS" · dan.grandrino@kivaconfections.com · 2026-09-11
2. `1a090e659975de12` · "🔥 Friday Wholesale Menu – Finish the Week Strong" · allanf@harvestmoonfarmsnj.com · 2026-09-11
3. `1a090a34c4df64e2` · "Ascend Updated Menu | New Strains & Flavors + Let's Link Up at NECANN" · nbonsanto@awholdings.com · 2026-09-11

Other vendor-domain threads with subject-line menu signals were found but skipped as not pure blasts (real back-and-forth correspondence mixed in — e.g. the laddsllc.com "Monday Menu Drop" thread where Hillary King is discussing Cuzzie's closure status, and a starred illicitgardens.com thread with internal team discussion). Precision over recall per the runbook.

## PART B — Trash sweep (9 threads, recovery IDs below — Gmail Trash retains 30 days)
1. `1993ac33b1afa7e9` · "Get ready now for hurricane season." · progressivecommercial@e.progressive.com · 2025-09-11
2. `1993a9fd5229ea33` · "They couldn't afford homes in the city. So they left." · fromthetimes-noreply@nytimes.com · 2025-09-11
3. `199399ecf7982982` · "🎤 Automation secrets from Meta, Vercel, AppsFlyer & more" · make-events@make.com · 2025-09-11
4. `199398043d2ceed1` · "Still juggling third-party loyalty and marketing tools? There's a better way." · marketing@dutchie.com · 2025-09-11
5. `199396b8ed76e5b7` · "Learn Brands Q3 Newsletter 2025" · max@learnbrands.com · 2025-09-11
6. `199393986296e2fc` · "Put Some Nimbus Carts in Your Shopping Cart Today!" · andrew@northlake.supply · 2025-09-11
7. `199391566ed56bab` · "Quiz: Are you prepared for a climate disaster?" · fromthetimes-noreply@nytimes.com · 2025-09-11
8. `19938e9278965ea2` · "Your August 2025 Pro Xtra Statement is Here" · homedepotpro@mg.homedepot.com · 2025-09-11
9. `19936f3a7767b01c` · "September admin update" · no-reply@email.slackhq.com · 2025-09-11

### Method and skip counts
Built the candidate set with `older_than:1y (category:promotions OR category:social OR category:forums)` — Gmail estimated 201 matching threads. Paged through the full set (5 pages, 250 thread-rows reviewed with dedup) cross-checking each against the hard floor. The overwhelming majority — roughly 190+ of the 201 — carry Gmail's own `IMPORTANT` label (Lemar interacts with these vendor senders enough that Gmail auto-flags nearly all their promo mail as important), which is a protected condition under the safety floor and was never overridden. A further ~18 thread-instances were skipped for being on the NEVER-TOUCH allowlist (`parkebank.com` ×7, `sos.nj.gov`/CTA ×11) or `STARRED` (2 terrascend.com/high-grass-farms threads). Confirmed via a second targeted query (`-is:important -is:starred` on the same base filter, 31 results) that no eligible candidates were missed — the delta was fully accounted for by the allowlist and thread-level IMPORTANT carried by later messages in a couple of mixed threads (e.g. the Hamilton Farms and Dutchie-survey threads). The 9 trashed threads are the only ones that cleared every gate: not important, not starred, not on the allowlist, no genuine (non-Samira-automation) filing label, and — for the one vendor-domain sender in the list (northlake.supply) — correctly trashable once >12mo old per the runbook's vendor-domain carve-out.

## Report-only: old `category:updates` (201 threads, untouched)
Per the runbook this category is never auto-trashed. Sampled sender domains: nytimes.com (breaking-news alerts), voice-noreply@google.com (Google Voice missed-call notices), messaging.squareup.com (Square invoices), distru.com (order-status updates), sos.nj.gov (CTA updates), jotformsign.com, linqapp.com, headset.io, revelrysupply.com. Flagging for Lemar to clear by hand if he wants to — not actioned.

## Cap
No threads were left over the 200/run cap (only 9 qualified for trash).

## Sources
- gmail: connected account lemar@cuzziesnj.com, search_threads/label_thread/apply_sensitive_thread_label calls, 2026-09-12 run
