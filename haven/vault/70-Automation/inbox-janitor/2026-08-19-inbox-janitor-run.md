---
created: 2026-08-19T23:07-04:00
updated: 2026-08-19T09:06:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-08-19 (Basil)

Nightly Gmail cleanup, executed live (`DRY_RUN = false`) against `lemar@cuzziesnj.com` per
`.claude/routines/inbox-janitor.md`.

## Run summary
- Mode: LIVE
- Archived 6 vendor menus (PART A)
- Trashed 3 old promotional threads (PART B) — 0 over the 200/run cap
- 20 PART B candidates evaluated but skipped (protected): 8 by the `*.gov` allowlist entry
  (`sos.nj.gov` CTA webinar emails), 9 by the `parkebank.com` allowlist entry, 3 because the
  thread carried an IMPORTANT-flagged message somewhere in it (a dutchie survey thread, a
  Hamilton Farms wholesale-menu negotiation thread, an ICCC mini-MBA thread)
- `category:updates` old-mail count (report-only, never auto-trashed): ~201 threads older
  than 1 year. Sample sender domains: `voice-noreply@google.com` (Google Voice),
  `noreply@jotform.com`, `fromthetimes-noreply@nytimes.com`, `info@headset.io`,
  `notifications@monday.com`, `info@protect.mcafee.com`, `looker-studio-noreply@google.com`,
  `contact@linqapp.com`. Lemar may want to clear these by hand.

## PART A — vendor menus archived (labeled `Vendor Menus`, removed from INBOX)
1. "Fresh Grow Menu | New Pricing & Weekly Specials" — Kathy@freshcannabis.co — 2026-08-18 —
   thread `1a01673a6c56ecd5`
2. "Sun & Woodstock Menu" — tj@arescanna.com — 2026-08-18 — thread `1a01609a2f22498c`
3. "Hillview Flower Menu - 3 NEW STRAINS 32-34% THCa" — tj@arescanna.com — 2026-08-18 —
   thread `1a015e7791882f23`
4. "Prolific Menu 8.17 | 3 New Bob's Pre-Rolls & Full Vape Lineup!" —
   ethan@prolificgrowhouse.com — 2026-08-17 — thread `1a0112e1fdd0fff9`
5. "QCC NJ Menu 8.17.26 - Tahoe OG is BACK & $4.50 Pre-Rolls!" — kbreiner@qccnj.com —
   2026-08-17 — thread `1a0106f66656b361`
6. "Ascend Most Up to Date! | Simply Herb Shake is Back + New Strains This Week" —
   nbonsanto@awholdings.com — 2026-08-17 — thread `1a010264330e3976`

Other vendor-domain threads with attachments were found but deliberately excluded from
archiving — they were genuine business correspondence (invoices, AR/collections statements,
contract/WSA negotiation threads, event invites) rather than routine menu blasts. Precision
over recall per the runbook.

## PART B — trash audit (recoverable in Gmail Trash for 30 days from 2026-08-19)
1. Thread `198bd98824ce222a` — "Hamilton Farms Weekly Menu! NEW STRAIN DROP!!" —
   sales@hamiltonfarms.com — 2025-08-18
2. Thread `198bd0eae200cd20` — "How to save money on groceries, according to our readers" —
   fromthetimes-noreply@nytimes.com — 2025-08-18
3. Thread `198bab3818acada9` — "Time to replace these 17 household essentials" —
   fromthetimes-noreply@nytimes.com — 2025-08-17

All three: `category:promotions`, `older_than:1y`, not starred, not important, sender domain
not on the NEVER-TOUCH allowlist.

## Sources
- gmail: threads listed above (Basil's live search/action, 2026-08-19)
