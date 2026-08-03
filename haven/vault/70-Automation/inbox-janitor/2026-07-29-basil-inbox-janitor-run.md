---
created: 2026-07-29T23:07-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-29

Live run (`DRY_RUN=false`, continuing from last night's 2026-07-28 run — not the first
live run). Account: `lemar@cuzziesnj.com` (the only connected Gmail account; Drive out
of scope). Archived 98 vendor-menu threads out of the inbox and trashed 5 old
promotional threads that newly crossed the 12-month cutoff since last night (all
recoverable in Gmail Trash for 30 days). Both actions stayed under their per-run caps
and respected the NEVER-TOUCH allowlist and the starred/important floor from
`.claude/anchors.md`.

## PART A — Vendor menus archived (98)

Two combined searches: `in:inbox -label:Label_8 has:attachment` crossed with either a
vendor-domain seed-list match or a menu-keyword subject match (menu, availability,
price sheet, drop, in stock), per the runbook's combination-of-signals rule. 98 threads
qualified and were labeled `Vendor Menus` (`Label_8`) then had `INBOX` removed. Sender
domains: several from the anchors seed list (verano.com, terrascend.com, awholdings.com,
kivaconfections.com, harvestmoonfarmsnj.com, apextrading.com subdomains, prolificgrowhouse.com,
1906.shop, northlake.supply, thegardensociety.com), plus additional cannabis wholesale
vendor domains not yet on the anchors seed list that matched on menu keyword + attachment:
hamiltonfarms.com, humblecamp.com, lovegrow.co, getblur.com, stashhousedistro.com,
cannabistcompany.com, ianthus.com, greenlightningcannabis.com, ggcann.com, brutesroots.com,
eatgron.com, sussexcultivation.com, kushilabs.com, cookiesharrison.com, canopy-usa.com.
Skipped: one STARRED thread (eatgron.com "Grön Edibles Fresh Menu") out of caution even
though Part A's letter doesn't explicitly require it, and one gse420.com thread that had
turned into a live payment-terms negotiation rather than pure menu marketing.

**Backlog note:** both search queries still show a `resultCountEstimate` of 201 each —
more qualifying vendor-menu threads remain beyond tonight's 98 (recurring weekly blasts
from ~20+ vendors compound quickly). Already-archived threads drop out of future
`-label:Label_8` searches automatically, so subsequent nightly runs will keep working
through the remainder without reprocessing tonight's batch. **Suggestion for the anchors
seed list:** hamiltonfarms.com, humblecamp.com, lovegrow.co, getblur.com,
stashhousedistro.com, cannabistcompany.com, ianthus.com, greenlightningcannabis.com,
ggcann.com, brutesroots.com, eatgron.com, sussexcultivation.com, kushilabs.com,
cookiesharrison.com, and canopy-usa.com all showed up repeatedly as genuine wholesale
menu senders and look like good additions.

## PART B — Trash sweep (5 threads)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)`,
reviewed manually (not query-filtered) against `is:starred`/`is:important`/allowlist —
3 pages, ~150 candidates reviewed. Only 5 qualified and were trashed:

| Thread ID | Sender | Subject | Date |
|---|---|---|---|
| 198530d74cf05f63 | wholesale@verano.com | Casey's in town 🚗 | 2025-07-28 |
| 19852950935d9a34 | andrew@northlake.supply | You Asked, We Listened — Cheaper Pre-Rolls + New Hemp Paper Drops! 🌿 | 2025-07-28 |
| 1985207d2ad5b8ce | marketing.us@terrascend.com | 🍇Don't Sit on this Grape New Strain🍇 | 2025-07-28 |
| 19851fdb61bff98a | hello@surfside.io | Join us for a Live Conversation with Trulieve's Iram Cesani | 2025-07-28 |
| 198514e8bf10dcd0 | flyers@webstaurantstore.com | Hot stock. Cool prices! | 2025-07-28 |

All recoverable from Gmail Trash for 30 days. 0 threads over the 200/run cap.

**Tuning flag for Lemar:** of the ~150 candidates reviewed, roughly 145 (~97%) were
skipped because Gmail auto-tagged the thread `IMPORTANT` (a handful more for `STARRED`
or the NEVER-TOUCH allowlist — verano.com marketing, parkebank.com, fundcanna.com,
`*.gov`, dutchie.com survey threads). This matches last night's pattern (2026-07-28 note
skipped only 2 for importance, but that run's search query already excluded
`is:important`/`is:starred` at the Gmail-query level, so its 184-trash figure was drawn
from an already-filtered pool — consistent with, not contradicting, tonight's finding).
The account's own `list_labels` shows `IMPORTANT` applied to 9,582 of 22,150 threads —
very broad. Lemar may want to reconsider whether `is:important` should gate Part B given
how liberally Gmail applies it here (a lot of pure vendor marketing — Verano, BestBuy,
FundCanna, Dutchie, ThrivePOP, Budvue — is sitting in Inbox tagged important and will
never be trashed under the current rule), or accept that Part B will stay this
conservative and mostly catch only the small daily trickle of newly-12-months-old,
non-important mail.

## Report-only: `category:updates` (never auto-trashed)

~201+ threads older than 12 months in `category:updates` (resultCountEstimate 201 on
one page alone) — not touched, per the runbook. Notable recurring sender domains:
`google.com` (Google Voice missed-call/voicemail/text notifications — very high
volume), `notification.intuit.com` (QuickBooks invoice reminders — allowlisted anyway),
`headset.io` (scheduled sales/inventory reports — allowlisted), `nytimes.com` (breaking
news), `redditmail.com`, `jotformsign.com`, `adt.com`, `theathletic.com`, `slack.com`
(sign-in/confirmation notices). The Google Voice notification volume stands out as the
biggest single contributor — Lemar may want to adjust notification settings upstream
rather than have this cleared by hand every night.

## Next run

`DRY_RUN` stays `false`. Both queues (vendor menus, trash-eligible mail) still have a
backlog beyond tonight's batches, plus ordinary nightly accumulation.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox, live sweep 2026-07-29
- related: [[2026-07-28-basil-inbox-janitor-run]] (previous night's run)
