---
created: 2026-07-15T23:07-04:00
updated: 2026-07-15T23:07-04:00
domain: cuzzies
type: log
status: done
tags: [inbox-janitor, basil, gmail, dry-run, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor nightly run, 2026-07-15 (DRY RUN — no action taken)

`DRY_RUN = true` in `.claude/routines/inbox-janitor.md` on `main` at run time (unchanged
this run). Per the routine, PART A and PART B were run to completion as *searches only*:
nothing was archived, labeled, or trashed. Findings below are for Lemar to vet before
flipping `DRY_RUN = false`.

## PART A — vendor menus (would archive)

Searched the inbox against the vendor-domain seed list in anchors (qccnj.com,
verano.com, terrascend.com, awholdings.com, freshcannabis.co, kivaconfections.com,
illicitgardens.com, harvestmoonfarmsnj.com, apextrading.com + seller subdomains,
budsgoods.com, novafarms.com, prolificgrowhouse.com, parksgrove.com, laddsllc.com,
missgrass.com, jerseysmooth.com, thegardensociety.com, arescanna.com, 1906.shop,
northlake.supply).

**Result: the vendor-menu backlog is very large — well over 200 qualifying threads.**
Gmail's own result-count estimate caps out at "201" for every variant of this query, so
the true number is higher. A 6-page / ~290-raw-thread sample still extended back to
2026-05-29 with no end in sight, meaning this backlog has been accumulating since before
the routine's first run (2026-07-09, per anchors) and has kept growing every night since
because DRY_RUN was never flipped to live.

A handful of same-domain threads were correctly **excluded** from the "would archive"
count because they are not menus — real 1:1 correspondence, not marketing blasts:
- "Prolific Growhouse Overdue Invoice/New Bank Account" (prolificgrowhouse.com)
- "Harvest Moon Farms Pop Up / Activation Request" threads (harvestmoonfarmsnj.com)
- "Past Due Payment Reminder" from thegardensociety.com — one instance is **STARRED**,
  doubly protected under the Safety floor
- Verano (verano.com) delivery-scheduling threads with Andrew Pallottie

These stay in the inbox untouched under both PART A and PART B, as the routine requires.

Representative sample of qualifying vendor-menu senders/subjects (most recent):
Fresh Grow Menu (freshcannabis.co) · Harvest Moon Farms Menu (harvestmoonfarmsnj.com) ·
TerrAscend Menu (terrascend.com) · QCC NJ Menu (qccnj.com) · Ascend Menu (awholdings.com) ·
Kiva Camino/Lost Farm Menu (kivaconfections.com) · Bud's Goods Menu (budsgoods.com) ·
Sun/Woodstock/Hillview Menu (arescanna.com) · Garden Society Menu (thegardensociety.com) ·
Nimbus cart promos (northlake.supply) · APEX menu blasts (apextrading.com subdomains) ·
Miss Grass menu updates (missgrass.com) · Jersey Smooth drops (jerseysmooth.com).

**Would archive: 200+ threads** (exact count exceeds what one dry-run digest can
enumerate; the live run's own tally, once flipped, will be authoritative). PART A has
no per-run cap, so a live run would likely need several nights to fully clear this.

## PART B — trash sweep (would trash, >12mo old, promotions/social/forums only)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)` minus
starred, important, and the NEVER-TOUCH allowlist domains (intuit.com/quickbooks/
notification.intuit.com, tsheets.com, gusto.com, parkebank.com, fundcanna.com,
firstinsurancefunding.com, pactsafe.com, docusign, crc.nj.gov/*.gov, accounts.google.com,
headset.io, stellaconnect.net).

**Result: also well over 200 qualifying threads** (same "201" estimate cap). Sampled the
most recent ~50 (2025-07-02 through 2025-07-14) — all clean, disposable marketing/
survey/event-invite mail (Canva, Vangst, Salesforce, Best Buy, Home Depot Pro, Fernway,
NECANN, Webstaurant, Sherwin-Williams, aged-out vendor blasts, etc.). None were starred,
important, or carrying a genuine filing label, and none matched an allowlist domain.

**Would trash: 200+ candidates, which exceeds the per-run 200-thread cap.** On the
first LIVE run, expect Basil to trash the oldest 200 and report the remainder as
"left for tomorrow" in the digest — likely repeating for several nights before the
backlog clears.

Sample audit (thread ID · subject · sender · date) for spot-vetting:

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1980ae6e1f951333 | ⏳ Croptober is just 7 weeks away — Are you fully staffed? | marketing@vangst.com | 2025-07-14 |
| 1980a63f38fde4f5 | Hamilton Farms Weekly Menu | sales@hamiltonfarms.com | 2025-07-14 |
| 1980a3d0f2ebaef1 | Don't miss our webinar with Meta | marketing@engage.canva.com | 2025-07-14 |
| 1980985bf85486bd | New Summer Menu: Price Drops + Watermelon Sorbet Vapes | andrew@northlake.supply | 2025-07-14 |
| 198090a48afc1bf3 | Ecommerce is now available for all dispensaries! | hello@flowhub.com | 2025-07-14 |
| 198089810b875208 | PANDA FARMS New Strain Drops!! | jason@bridgecitycollective.com | 2025-07-14 |
| 197ffd1f10e950f5 | Black Friday in July (and awesome tech)... | BestBuy@email.bestbuy.com | 2025-07-12 |
| 197fae337ec155b8 | High Grass Farms- Check out our new prices | Francisco@high-grass-farms.apextrading.com | 2025-07-11 |
| 197fa61a8a9cca53 | ONYX Live Apex Menu - 7.11.25 | Phil@sussex-cultivation.apextrading.com | 2025-07-11 |

(Full candidate set exceeds what a single dry-run digest can enumerate; the live run
will produce the authoritative 200-item audit list per its own cap and recovery window.)

## category:updates (report-only — never auto-trashed)

Also very large (200+ estimate) and confirmed genuinely mixed/dangerous to sweep, per
the runbook's warning: sampled contents include QuickBooks invoice-due reminders
(`quickbooks@notification.intuit.com` — real payables), Jotform employee time-off
approvals, Headset daily sales/inventory reports, Google Voice call/billing notices, and
Looker Studio analytics reports, all interleaved. Left entirely alone, as designed.
Senders Lemar may want to hand-clear eventually: `notification.intuit.com`,
`noreply@jotform.com`, `noreply@jotformsign.com`, `info@headset.io`,
`voice-noreply@google.com`.

## Bottom line for Lemar

DRY_RUN has now run silently for about a week (first run 2026-07-09) without being
vetted/flipped, and the qualifying backlog in both PART A and PART B has grown past
200 each — larger than one night's cap can clear in one pass. **Nothing has been
touched.** Recommend: spot-check the samples above, then flip `DRY_RUN = false` in
`.claude/routines/inbox-janitor.md` on `main` when ready. Expect the first several live
runs to each hit the 200-trash cap while the backlog drains, and PART A archiving to
take multiple nights too since it has no cap.

No irreversible action was taken this run. No Drive access, no email sent/drafted, and
no starred / important / user-labeled / allowlisted thread was touched or counted toward
either total.

## Sources
- gmail: lemar@cuzziesnj.com inbox searches, 2026-07-15 (PART A domain query, PART B
  trash-sweep query, category:updates recon)
- claude: Basil inbox-janitor routine run, cloud env `env_01Xatmag93x2WA2Gd84D9iHj`
