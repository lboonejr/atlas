---
created: 2026-08-18T23:07-04:00
updated: 2026-08-18T12:07:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-18

Mode: LIVE (`DRY_RUN=false`)
Account: lemar@cuzziesnj.com

## PART A — Vendor menus archived: 8

All labeled `Vendor Menus` (`Label_8`) and removed from Inbox (still in All Mail under
the label — nothing deleted). Two vendor-menu candidates were skipped because they
carried the `IMPORTANT` flag (protected by the hard safety floor): QCC NJ Menu 8.17.26,
Prolific Menu 8.17.

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1a011b47f489ba00 | New Menu ! New Deals ! | Tyler.Marsh@verano.com | 2026-08-17 |
| 1a0110abd82f6fa8 | Harvest Moon Farms Menu 8.17.25 High Testers Updated w/OOS taken off | carlos@harvestmoonfarmsnj.com | 2026-08-17 |
| 1a010e513dcac678 | TerrAscend Menu - Debut: Cuue Chocolates + $15 Kind Tree 3.5g... | ndesiderio@terrascend.com | 2026-08-17 |
| 1a0109c3024311c9 | Illicit NJ Menu- 40% off Concentrate Sale - for delivery 8/24-8/28 | jb@illicitgardens.com | 2026-08-17 |
| 1a0108bedbc8028e | Bud's Goods Menu - Week of 8.17 | mzaidi@budsgoods.com | 2026-08-17 |
| 1a010307de8b1f00 | Kiva Camino/Lost Farm Menu - August Week 3 - Deals are Back | dan.grandrino@kivaconfections.com | 2026-08-17 |
| 1a00fd85436a0406 | Monday Wholesale Menu – Let's Start the Week Strong | allanf@harvestmoonfarmsnj.com | 2026-08-17 |
| 1a00f904bce33359 | Monday Morning APEX Menu! | Peter@canfections-nj-llc.apextrading.com | 2026-08-17 |

Recovery: reversible any time by re-adding `INBOX`, no trash involved.

## PART B — Trash sweep: 0 trashed

Candidate query: `older_than:1y (category:promotions OR category:social OR category:forums)`.
Estimated ~201 matching threads; manually reviewed 300 across the full paginated result
set (6 pages of 50). **Every single thread reviewed was protected** — each carried
`IMPORTANT`, `STARRED`, or a NEVER-TOUCH allowlist sender domain (`parkebank.com`,
`*.sos.nj.gov`). Zero threads passed all four PART B gates, so zero were trashed and
zero were left over the 200/run cap (nothing qualified to begin with).

**Operator note (tuning flag, nothing acted on tonight):** Gmail's ML "Important"
marker is applied very liberally on this account — essentially all vendor marketing
addressed personally to Lemar by name gets flagged `IMPORTANT`, even routine
promotional drops (menu blasts, webinar invites, "back in stock" emails). Because the
routine's safety floor treats `is:important` as an unconditional protection, PART B's
trash sweep is structurally near-inert on this inbox as currently written: 0 of 300
reviewed threads were trashable. If Lemar wants the sweep to actually reclaim space,
worth revisiting what "important" should mean for this purpose — no change was made
tonight; flagging only.

## category:updates — report-only, not swept

`older_than:1y category:updates` — approximately 201 matching threads, left untouched
per the routine (too mixed with invoices/bank/payroll/legal receipts to sweep safely).
Sample sender domains seen: google.com (Voice missed-call/text notices), nytimes.com,
theathletic.com (e1.theathletic.com), redditmail.com, jotform.com / jotformsign.com
(register-float approvals — operational, not junk), monday.com (automation-error
notices), headset.io (scheduled reports), cannazipbags.com, adt.com,
firstinsurancefunding.com (already allowlisted). Lemar may want to hand-clear the
Google Voice / NYT / Athletic / Reddit newsletter noise from this bucket himself.

## Summary
Archived: 8 · Trashed: 0 · Over cap: 0 · Updates (report-only): ~201

## Sources
- gmail: 8 archived vendor-menu threads (IDs above), account lemar@cuzziesnj.com
