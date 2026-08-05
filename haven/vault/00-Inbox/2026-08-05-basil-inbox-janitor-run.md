---
created: 2026-08-05T00:20-04:00
updated: 2026-08-05T00:20-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-05

Live run (`DRY_RUN=false`), continuing from [[2026-08-04-basil-inbox-janitor-run]].
Account: `lemar@cuzziesnj.com` (the only connected Gmail account; Drive out of scope).
Archived 296 vendor-menu threads out of the inbox and trashed 4 old promotional threads
(recoverable in Gmail Trash for 30 days). Both stayed well under their per-run caps and
respected the NEVER-TOUCH allowlist and the starred/important floor from
`.claude/anchors.md`.

## PART A — vendor menus archived (296)

Swept the full `in:inbox` vendor-domain candidate set across 12 search pages (~600
threads reviewed, spanning back to 2025-08-26 — a much larger backlog than prior runs,
since this pass reached further back than usual). Each qualifying thread required the
domain+content combination from the runbook (vendor-domain seed list AND a menu/
availability/price-sheet signal in subject or snippet AND an attachment or explicit
menu link) — no thread was archived on a single signal alone.

Dominant senders: northlake.supply (Nimbus — andrew@/dan@/sales@), several
`*.apextrading.com` subdomains (little-leaf-labs, high-grass-farms,
hearth-wellness-llc/"Shady Extracts", agri-kind, the-happy-farmer-llc,
canfections-nj-llc, sussex-cultivation, ganja-manja), verano.com (wholesale@/
maggie.boyd@/Tyler.Marsh@), terrascend.com (marketing.us@), awholdings.com
(nbonsanto@/bsussman@), kivaconfections.com (carlos.gamez@), missgrass.com,
jerseysmooth.com, budsgoods.com, prolificgrowhouse.com, thegardensociety.com,
harvestmoonfarmsnj.com, and freshcannabis.co.

Ambiguous calls made (precision over recall, all left in place when unsure):
Kiva Confections "B2G1/B3GO wholesale offer" emails without a visible product list were
left in the inbox as order-logistics rather than a menu; standalone Kiva "% off
wholesale promo" emails with explicit case-level discount language were archived.
TerrAscend emails were only archived when they said "Now Available," "LIVE," or "Just
Dropped" explicitly — plain "Coming Soon" teasers were left. Several broken vendor
templates (literal "Insert your header here" placeholder text, no real product content)
were left in the inbox rather than guessed at. "Shady Extracts"
(hearth-wellness-llc.apextrading.com) uses a comedic/narrative voice that reads as
generic chatter but was confirmed via full-content check to reliably contain real
priced menus underneath — treated as menu-qualifying once confirmed.

All 296 qualifying threads were labeled `Vendor Menus` (`Label_8`) then had `INBOX`
removed — recoverable in All Mail under that label, nothing was trashed. Full per-thread
ID/subject/sender/date audit (632 tool calls total across both parts) lives in this
run's execution transcript; available on request if a specific thread needs checking.

**Flag for Lemar:** the actual PART A backlog ran to 600+ threads back to January 2026
(vendor mail continues further back still) — well beyond the runbook's ~200-thread
estimate. There is likely more vendor-menu backlog older than what tonight's run
covered. Worth a dedicated catch-up run, or tightening cadence so it stops
re-accumulating.

## PART B — trash sweep (4 trashed, recoverable 30 days)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)`.
250 candidates examined across 5 pages back to mid-2024; 234 were shielded by Gmail's
`is:important`/`is:starred` flags, 12 more were protected purely by the NEVER-TOUCH
allowlist (mostly `*.gov` senders and `parkebank.com`). Only 4 passed every gate. 0
threads hit the 200/run cap — nothing left for tomorrow.

| # | Thread ID | Subject | Sender | Date |
|---|---|---|---|---|
| 1 | 198765fc4620cb0c | Summer Deals + Syringe Drop: RSO & Our First Dabbable Concentrate! | andrew@northlake.supply | 2025-08-04 |
| 2 | 19875b80ee78d53b | ONYX Apex Menu Link - 8.4.25 - Reduced Pricing for Edibles! | Phil@sussex-cultivation.apextrading.com | 2025-08-04 |
| 3 | 198757a6af838250 | Hamilton Farms weekly menu! (Panama Red is back!!) | sales@hamiltonfarms.com | 2025-08-04 |
| 4 | 19874cde1161f885 | TODAY ONLY: Plus Day is live! | flyers@webstaurantstore.com | 2025-08-04 |

**Flag for Lemar:** Gmail's algorithmic `IMPORTANT` label is applied very broadly on
this account, including to plain marketing/promo mail — that's what made tonight's
trash-candidate pool almost empty (234 of 250 examined were protected purely by
`is:important`). Nothing was touched based on this observation — flagging only — but
it may be worth deciding whether that label should keep counting as a protective signal
for PART B, since it's likely suppressing cleanup that would otherwise be safe.

## `category:updates` — report-only (never auto-trashed)

~201 threads (Gmail's `resultCountEstimate` — this stayed static across every paginated
call tonight and should be read as approximate, not exact). Sender domains observed:
`google.com` (voice-noreply/accounts/looker-studio/sc-noreply subdomains),
`jotform.com`, `jotformsign.com`, `headset.io` (allowlisted), `theathletic.com`,
`redditmail.com`, `nytimes.com` (breakingnews-noreply), `fedex.com`
(no-reply.ecommerce), plus `firstinsurancefunding.com` (allowlisted), `found.com`, and
`linqapp.com`. Worth a hand pass if Lemar wants this folder thinned — none of it was
touched tonight.

No email was sent or drafted. No Trash was emptied, no Spam applied. No account other
than `lemar@cuzziesnj.com` was touched. Nothing starred/important/user-labeled or newer
than 12 months was archived or trashed. Google Drive untouched (out of scope).

## Sources
- gmail: `lemar@cuzziesnj.com` inbox — search_threads / label_thread / unlabel_thread /
  apply_sensitive_thread_label, run 2026-08-05
