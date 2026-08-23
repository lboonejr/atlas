---
created: 2026-08-23T23:15-04:00
updated: 2026-08-23T12:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

## Basil — Inbox Janitor run log
**Date:** 2026-08-23 (~11pm ET cadence)
**Account:** lemar@cuzziesnj.com
**Mode:** LIVE (DRY_RUN = false)

### Summary
- Vendor menus archived: 1
- Threads trashed (>12mo, disposable categories): 3
- Threads over the 200/run cap: 0

### PART A — vendor menus archived

Reviewed ~201 broad candidate matches (vendor-domain senders from the anchors.md seed
list combined with menu-signal keywords, with and without attachments). The large
majority were invoices, delivery notices, wholesale-agreement/onboarding threads, and
promotional blasts that only weakly matched menu keywords in body text — per the
runbook's "prefer precision over recall," these were left in the inbox. Only one thread
was an unambiguous vendor-menu drop:

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1a029b6ea79637b3 | Fresh Grow Menu \| Pre-Roll Specials, New Half Pricing & Dice Restock | Kathy@freshcannabis.co | 2026-08-22 |

Action: labeled `Vendor Menus` (Label_8), removed `INBOX`.

### PART B — trash sweep (audit list, recoverable 30 days in Gmail Trash)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 198d2405b91f1a8e | Ready to level up? These sessions deliver. | marc@necann.com | 2025-08-22 |
| 198d22037ecff524 | New weekday hours! Shop as early as 6:00 AM at select stores. | email@em.sherwin-williams.com | 2025-08-22 |
| 198d1a9e8f8efa07 | Lemar, don't forget about your reward certificate | BestBuy@email.bestbuy.com | 2025-08-22 |

Candidate set: `older_than:1y (category:promotions OR category:social OR category:forums)
-is:starred -is:important in:inbox` → 23 raw candidates. Skipped from that set:
- 9 threads from `CTA@sos.nj.gov` (`.gov` domain — NEVER-TOUCH allowlist)
- 8 threads from `parkebank@parkebank.com` (explicit NEVER-TOUCH allowlist entry)
- 3 threads that matched the query but contain at least one IMPORTANT-labeled message
  inside the thread (Dutchie implementation survey, Hamilton Farms weekly
  menu/pricing-negotiation thread, ICCC mini-MBA program invite) — kept per the
  never-touch-if-any-message-fails-the-gate rule

Net: 3 of 23 candidates cleared every gate clause and were trashed. No candidates
exceeded the 200/run cap.

### Report-only — category:updates (never auto-trashed)

`older_than:1y category:updates in:inbox` → resultCountEstimate 201. Not touched (per
runbook, this category mixes invoices/bank/payroll/legal receipts with disposable
notices — too dangerous to sweep). Sample of recurring sender domains an operator could
hand-clear: `voice-noreply@google.com` (Google Voice missed-call notices — very high
volume), `noreply@jotform.com` / `noreply@jotformsign.com`,
`breakingnews-noreply@nytimes.com`, `notifications@monday.com`,
`TheAthletic@e1.theathletic.com`, `noreply@redditmail.com`.

### Recovery
Trashed threads sit in Gmail Trash for 30 days; the thread IDs above are sufficient to
restore any of them via `untrash_thread` if needed.

## Sources
- gmail: connected account lemar@cuzziesnj.com, PART A/B search_threads + label/trash actions, 2026-08-23
