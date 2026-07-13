---
created: 2026-07-13T23:07-04:00
updated: 2026-07-13T23:07-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail, dry-run, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor nightly run — 2026-07-13 (DRY RUN)

Mode: **DRY_RUN = true** (first supervised preview run per
`.claude/routines/inbox-janitor.md` — no Gmail mutations performed: nothing archived,
nothing labeled, nothing trashed, nothing sent). Account acted on (read-only this run):
`lemar@cuzziesnj.com`.

## PART A — vendor menus (would-archive preview)

`Vendor Menus` label already exists (`Label_8`) — no creation needed.

Sampled 150 of an estimated 200+ inbox threads from the 20 vendor-menu seed domains in
anchors.md (qccnj.com, verano.com, terrascend.com, awholdings.com, freshcannabis.co,
kivaconfections.com, illicitgardens.com, harvestmoonfarmsnj.com, apextrading.com +
subdomains, budsgoods.com, novafarms.com, prolificgrowhouse.com, parksgrove.com,
laddsllc.com, missgrass.com, jerseysmooth.com, thegardensociety.com, arescanna.com,
1906.shop, northlake.supply).

Of those 150, **~93 (62%)** carry an explicit menu/drop signal in subject or snippet
("Fresh Grow Menu", "QCC NJ Menu", "Ascend Menu", "TerrAscend Menu", "Prolific Menu",
"Bud's Goods Menu", etc.) and would be archived out of Inbox under `Vendor Menus`. The
remainder were non-menu vendor mail (pop-up/activation requests, invoice/payment
notices, general check-ins) correctly left alone per "precision over recall." The true
full-inbox count is likely higher than the 150 sampled — pagination continued past what
was reviewed this run.

Representative thread IDs that would be archived: `19f4d524cfdab7f1` (Fresh Grow Menu),
`19f4d07a74a6fb61` (Sun Extracts MENU), `19f4c7c917ccd6bb` (Ascend Menu),
`19f48063524f1fd9` (Kiva Camino Lost Farm Menu), `19f41f519a5e168d` (QCC NJ Menu 7.8.26),
`19f37a11188c99b5` (Bud's Goods Menu), `19f3cc5a67d76989` (Prolific Menu 7.7),
`19f390811490d745` (Illicit NJ Menu), `19f3849456e6070c` (Miss Grass Menu),
`19f377220410b751` (TerrAscend Menu).

## PART B — trash sweep (would-trash preview)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)`.
Sampled 148 of an estimated 200+ matching threads. After the full safety gate (exclude
`is:starred`, `is:important`, NEVER-TOUCH allowlist domains, genuine user filing labels —
Samira/Car-Hunt automation labels do not count as protective), **~131 (89%) would be
trashed**, **~17 excluded**.

Exclusion breakdown in the sample: 12 threads excluded for `is:important` (e.g. High
Grass Farms product updates, Vangst staffing pitch, Alpine IQ announcement, WM feedback
survey), 1 excluded for `is:starred` (jamie-nichenfe.com "New SKU's" promo, 2025-06-30),
2 excluded for NEVER-TOUCH allowlist domains (`CTA@sos.nj.gov` under the `*.gov` rule;
`metrc@stellaconnect.net` under the stellaconnect.net rule).

The mailbox almost certainly holds well over 200 qualifying threads total (pagination
continued past what was sampled). On the first live run, the **200-threads-per-run cap
will bind** — only the oldest 200 get trashed and the remainder rolls to subsequent
nights. This is expected per the runbook's cap design, not an error.

Representative thread IDs that would be trashed: `197ffd1f10e950f5` (Best Buy promo),
`197f5411f91e0bf8` (Salesforce Dreamforce), `197f4db5a1b88e99` (Home Depot Pro paint
promo), `197efc34700f3239` (FASTSIGNS), `197ebf238973562b` (Verano wholesale guide),
`197e633f5abb85bf` (Canva marketing), `1979d3a5805db4f0` (jamie-nichenfe.com promo SKU
blast).

Representative thread IDs correctly **excluded** by the safety gate (do not touch):
`197c133bac012440` (STARRED — jamie-nichenfe.com "New SKU's"), `197a8cdb6f1d9200`
(`CTA@sos.nj.gov` — allowlist `*.gov`), `197dc05ecf8b4053` (`metrc@stellaconnect.net` —
allowlist), `197fae337ec155b8` (IMPORTANT — High Grass Farms).

## PART B (report-only) — `category:updates`, `older_than:1y`

Sampled 50 threads. Confirms the runbook's warning that this category mixes real
financial/operational mail with marketing — **never auto-trashed.** Notable sender
domains seen, for Lemar to clear by hand if desired:

- `headset.io` — daily/scheduled sales & inventory reports, very high volume (several/day)
- `quickbooks@notification.intuit.com` and other Intuit senders — invoices (allowlisted, protected regardless)
- `parkebank.com` — bank notice (allowlisted)
- `fedex.com` — receipts
- `no-reply@accounts.google.com` — security alerts (allowlisted)
- `noreply@redditmail.com` — r/gardening personal-interest digest
- `adtcontrol.com` — alarm system pending-alarm notifications, several/day
- `trustaltus.com` / `cfins.com` — payment processor notices
- `info@cuzziesnj.com` — Cuzzie's own marketing blasts + `info@headset.io` daily
  summaries (business is winding down per anchors — Lemar may want to unsubscribe from
  the headset.io and adtcontrol.com notification volume by hand)

## Recommendation

Vet the samples above. If the allowlist/starred/important exclusions look right and no
false positives appear in the "would archive" or "would trash" samples, flip
`DRY_RUN` to `false` in `.claude/routines/inbox-janitor.md` on `main` to go live next
run. Given inbox volume, expect the first live run to hit the 200-thread trash cap and
spread the full backlog over several nights.

No Gmail mutations occurred this run. No email sent, drafted, spammed, or permanently
deleted. Only the connected account `lemar@cuzziesnj.com` was read.

## Sources
- gmail: search `in:inbox {from:<20 vendor-menu seed domains>}` — PART A sample
- gmail: search `older_than:1y (category:promotions OR category:social OR category:forums)` — PART B sample
- gmail: search `older_than:1y category:updates` — PART B report-only sample
