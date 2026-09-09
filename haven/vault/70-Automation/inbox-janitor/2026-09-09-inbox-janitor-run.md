---
created: 2026-09-09T02:00-04:00
updated: 2026-09-09T11:11:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-09-09 (Basil)

Live run (`DRY_RUN = false`) of `.claude/routines/inbox-janitor.md` against
`lemar@cuzziesnj.com`.

## Summary
- Vendor menus archived (Vendor Menus label applied, removed from Inbox): **12**
- Threads trashed (>12mo, promotions/social/forums, not important/starred, not allowlisted): **1**
- Threads over the 200/run cap: **0**

## PART A — vendor menus archived (12)

| Thread ID | Sender | Subject |
|---|---|---|
| 1a08365afa11e164 | Tyler.Marsh@verano.com | 30% off still going ! Easy Landings Pre orders Live ! |
| 1a0828d048267d0a | Kathy@freshcannabis.co | Fresh Grow Menu \| New Products Coming Soon |
| 1a082544a8151aa3 | bbreslow@novafarms.com | Road to Croptober: Tuesday Touchdown |
| 1a0821600183d988 | ndesiderio@terrascend.com | TerrAscend Menu - $13 Kind Tree 3.5g, $26.40 2g Legend Vapes... |
| 1a0820da36d5d8b7 | kellie@parksgrove.com | Parks Grove Menu Update |
| 1a081da7fa5b2731 | carlos@harvestmoonfarmsnj.com | Harvest Moon Farms Labor Day Menu 9.8.26 |
| 1a081b56ba46cd31 | jb@illicitgardens.com | Re: Illicit NJ Menu- $5 Award Winning "Low-Dose Gummies"... |
| 1a081ac8a7d4b855 | Mark@agri-kind.apextrading.com | Bright Citrus. Big Terps. Meet Roasted Lemons. |
| 1a0819595df5f19a | mzaidi@budsgoods.com | Bud's Goods Menu Week Of 9.8 - B3G1 ALL 3.5G FLOWER |
| 1a0816e15160dccd | dan.grandrino@kivaconfections.com | Kiva Camino/Lost Farm Menu - September Week 2 |
| 1a08146629ca7ef1 | allanf@harvestmoonfarmsnj.com | New Week, Updated Menu – Let's Get Those Shelves Stocked |
| 1a081371c356507a | anthony@prolificgrowhouse.com | PROLIFIC MENU 9.8 \| HUGE RESTOCK + 5 NEW FLOWER STRAINS |

Skipped from PART A (weak signal or genuine 1:1 correspondence, not a menu blast):
[[laddsllc]] "Monday Menu Drop" thread (real back-and-forth with Hillary King re:
Cuzzie's status), northlake.supply "Labor Day cleared your shelves" (no
attachment/explicit menu signal), and all AR/collections/banking/invoice/event-invite
threads from vendor domains ([[the-garden-society]] collections notices, [[verano]] AR
statements, [[budsgoods]] invoice thread, [[qcc]] collections notice, [[illicit-gardens]]
delivery invoices, [[jersey-smooth]] event invites) — these are financial/relationship
correspondence, not vendor menus, left untouched per the "prefer precision" rule.

## PART B — trash sweep audit (1 thread, recoverable in Gmail Trash 30 days)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 199293407e7b8bf9 | A surprising (and easy) way to boost your attention span | fromthetimes-noreply@nytimes.com | 2025-09-08 |

## Tuning note for Lemar (finding only, no action taken)

Reviewed ~200 of the ~201 candidate threads matching
`in:inbox older_than:1y (category:promotions OR category:social OR category:forums)`
across 4 search pages. Nearly all of them carry Gmail's own `IMPORTANT` label (this
account auto-marks most vendor/marketing senders as important, likely from reply
frequency), which the safety floor protects from trashing — only 1 thread (the nytimes
digest above) actually qualified. A further ~15-20 were skipped specifically because the
sender domain is on the NEVER-TOUCH allowlist (`parkebank.com`, `*.sos.nj.gov`/CTA). Net
effect: PART B is trashing almost nothing most nights under the current gate, by design
(the safety floor is intentionally strict) — flagging so Lemar can decide whether that's
the intended behavior or whether the IMPORTANT-guard should be revisited later. No
allowlist or floor changes made.

## PART B report-only — old `category:updates` (never auto-trashed)

~201 threads older than 12 months sit in `category:updates` in the inbox. Sample of
sender domains seen (mixed operational + newsletter, exactly the "too dangerous to
sweep" mix the runbook describes): `jotform.com` / `jotformsign.com` (register
approvals, e-signatures, time-off requests), `google.com` (Voice missed-call/voicemail
notices, Search Console, Looker Studio reports), `nytimes.com` (daily breaking-news
digest), `headset.io` (analytics reports), `wm.com` (Waste Management payment receipts),
`extraspace.com` (storage payment receipts), `mcafee.com`, `flowhub.com`,
`theathletic.com`, `redditmail.com`. Left untouched per the runbook; Lemar can clear by
hand if desired.

## Mode

`DRY_RUN = false` — this was a live run; the actions above were taken for real.

## Sources
- gmail: 12 threads labeled `Vendor Menus` + removed from Inbox (IDs above)
- gmail: thread 199293407e7b8bf9 moved to Trash
