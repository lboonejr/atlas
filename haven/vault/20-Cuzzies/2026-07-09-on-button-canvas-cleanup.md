---
created: 2026-07-09T14:35-04:00
updated: 2026-07-09T16:15-04:00
domain: cuzzies
type: task
status: done
tags: [on-button, canvas, reopen-checklist]
source: slack
---

# On-Button canvas — clean up and update (repeat request)

Lemar asked in #atlas (2026-07-09 14:35 ET) to make sure the pinned **On-Button —
Reopen Checklist** canvas (`F0BEN1167GB` in #on-button, `C0BEQUW5NPP`) is cleaned
up and current. He asked a near-identical question on 2026-07-05
([[2026-07-05-on-button-canvas-leafly-sync]] — canvas was checked clean that day,
6 rows, no duplicates).

Between 2026-07-05 and now several new past-due / overdue items have landed in
Haven under 20-Cuzzies (e.g. Cintas, Little Leaf Labs, Ambotte Mechanical, Buds
Goods, Slack workspace payment, multiple Gusto payroll shortfalls, Regus Mount
Laurel office clearout) — worth checking whether any of these belong on the
canvas and whether #on-button itself has newer screenshots/bills dropped that
haven't been extracted yet.

**Next action:** on a later scan, re-open #on-button, re-read the canvas, dedupe
any stray/duplicate rows, and sync in any past-due item posted to the channel
since the last sync that isn't reflected on the canvas yet. Log the outcome the
same way as the 2026-07-05 pass.

## Update 2026-07-09 (16:15 ET) — cleaned up and resynced, done

Ran the staged `run:admin-3x` prompt (#admin, staged 15:13:56 ET). Re-opened
#on-button and the pinned canvas. Found the canvas structurally broken — two
duplicate/malformed blocks from a prior edit glitch (Regus/Arod/Gusto-tax/Google
Workspace rows pasted twice, one copy marked "removed — duplicate" but never
actually removed) plus two competing "Total" blocks (7/5 and 7/8 versions, one
marked superseded but left in place). Rebuilt the canvas as one clean table +
one current total (the canvas's own text says "Samira rebuilds this each scan,"
so a full rebuild is the sanctioned behavior, not an overwrite of Lemar's input).

**Deduped:** consolidated to a single 20-row table, removed the stray duplicate
blocks and the superseded total.

**Added from #on-button drops since the last real sync (2026-07-08 09:19 ET):**
- Weedmaps (Ghost Management Group), 5-invoice batch, $6,583.00, 58 days past
  due as of 7/9, threatened same-day service interruption (separate from the
  already-tracked invoice SIN830881, due 7/16, amount still unknown)
- Apple Developer Account restoration — $99.00
- Parke Bank negative balance — up to $2,000 (cap as flagged by Lemar)
- Loan from Nicky (personal) — $4,000.00
- Intercompany Inventory Loan — $40,000.00

**Added from cross-checking Haven `20-Cuzzies/`** (per the prompt's instruction):
- Little Leaf Labs — $8,331.00, 91+ days past due, Reminder 8, collections threat
- Ambotte Mechanical — $431.83 (invoice #76732; matter otherwise closed with the
  vendor, balance still unpaid)
- Bud's Goods of NJ — $1,512.10, 69 days overdue

**Left off the canvas** (judgment call, noted for visibility): Slack workspace
payment overdue and the Gusto payroll *funding-shortfall* cards (Jul 3/7/8/14) —
these are ongoing operational/SaaS costs, not "what it costs to reopen the
store" per the canvas's own stated scope. The Gusto payroll *tax remittance*
row (different matter — taxes owed, not funding shortfall) was already on the
canvas and stays. Regus Mount Laurel office clear-out is the same underlying
account (#16605480) as the existing Regus/IWG collections row — annotated in
place rather than duplicated.

**Total:** updated combined estimate (excl. Leafly — amount still unknown; excl.
Comcast/Waste Management — current, not past due; excl. EPLI $4,051.12 — Lemar
decided 7/6 to let it lapse and revisit at reopening) is approximately
**$87,055.72**, up from the 7/8 figure of ~$28,416.65 — driven mainly by the new
$40,000 Intercompany Inventory Loan and the $6,583 Weedmaps batch. Flagging the
size of that jump for visibility; no action taken beyond tracking.

Nothing paid or contacted — tracking only, per the canvas's own rules.

## Sources
- slack: #atlas capture, 2026-07-09 14:35:30 ET (channel C0BBWHCJUV9, ts 1783622130.775359)
- slack: canvas F0BEN1167GB ("On-Button — Reopen Checklist"), channel C0BEQUW5NPP
- slack: #admin staged prompt, ts 1783624436.298719
- slack: #on-button channel history through 2026-07-09 14:31 ET
