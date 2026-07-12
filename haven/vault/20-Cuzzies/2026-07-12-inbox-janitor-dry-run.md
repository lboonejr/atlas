---
created: 2026-07-12T23:07-04:00
updated: 2026-07-12T12:30-04:00
domain: cuzzies
type: log
status: active
tags: [inbox-janitor, basil, gmail-cleanup, dry-run, vendor-menus]
source: claude
---

# Inbox Janitor (Basil) — DRY RUN — 2026-07-12

## Run metadata
- Date: 2026-07-12 (nightly ~11pm ET routine, run via GitHub-hosted runbook `.claude/routines/inbox-janitor.md`)
- Mode: `DRY_RUN = true` (first supervised night — no Gmail mutations performed; nothing archived, nothing labeled, nothing trashed)
- Account acted on (read-only this run): lemar@cuzziesnj.com
- Vendor Menus label confirmed existing: `Label_8`

## PART A — vendor menus (would-archive)
Searched the inbox for `has:attachment` mail matching either (a) the vendor-domain seed
list in `anchors.md`, or (b) menu-signal subject terms (menu/availability/price sheet/
drop/in stock/live menu), per the runbook's "combination of signals" rule.

Sampled ~90 unique qualifying threads across both query angles. Gmail's own count
estimate suggests the true full population is larger — roughly 150–200+ across the
recent inbox window 6/16–7/10/2026. Did not exhaustively paginate every result, since
DRY_RUN's purpose is precision-vetting, not final tallying (per the runbook's own
"first night" guidance).

**Vendor-seed-list domains generating heavy volume:** freshcannabis.co, arescanna.com,
novafarms.com, awholdings.com, harvestmoonfarmsnj.com, kivaconfections.com, qccnj.com,
terrascend.com, jerseysmooth.com, prolificgrowhouse.com, verano.com, missgrass.com,
budsgoods.com, laddsllc.com, parksgrove.com.

**New vendor-menu senders NOT currently on the seed list** (qualified via subject-signal
+ attachment, not domain match) — recommend Lemar review and add to the seed list in
anchors.md if desired: cannabistcompany.com, stashhousedistro.com, hamiltonfarms.com,
getblur.com, canopy-usa.com, culture-craft.com, kushilabs.com, hillviewmed.com /
hillviewfarms.com, and `jbombara55@gmail.com` (a personal Gmail address sending "MGB"
brand wholesale menus — flagged as borderline since it's a personal-looking address, not
a company domain).

**False positives caught by the precision gate** (matched the raw query but are NOT
menus — excluded from the would-archive set):
- 2x "Prolific Growhouse Overdue Invoice/New Bank Account" (maylissa@prolificgrowhouse.com) — an invoice, not a menu.
- "TerrAscend — Out of office next week" (ndesiderio@terrascend.com) — an OOO notice.
- Kiva "Important Update: New Jersey Distribution Transition" — a business/distribution notice, not a menu.
- **"Past Due Payment Reminder"** thread from thegardensociety.com (ar@thegardensociety.com) — marked `IMPORTANT` AND contains a genuine reply from lemar@cuzziesnj.com in the thread (a Cuzzie's-closure update). This is real correspondence, not disposable marketing — correctly excluded, and a reminder that thegardensociety.com carries real billing correspondence, not just menus.

**Action taken: NONE (DRY_RUN).** Would have labeled these threads `Vendor Menus` and
removed them from INBOX.

## PART B — trash sweep (would-trash), 12-month cutoff
Query: `older_than:1y (category:promotions OR category:social OR category:forums)`.

Sampled 50 threads (one page); Gmail's count estimate suggests a larger true population
(150–200+) older than 12 months in these categories. Full itemization deferred to a live
run once DRY_RUN is vetted and off, per the runbook's per-run 200-thread cap and audit-
list requirement.

**Representative trashable domains seen:** verano.com and terrascend.com marketing
blasts, `*.apextrading.com` seller subdomains (high-grass-farms, sussex-cultivation),
plus non-vendor promo noise: homedepotpro (Home Depot), webstaurantstore.com,
alpharoot.com, salesforce.com, zapier.com, fastsigns.com, canva.com, treez.io,
vangst.com, necann.com, thrivepop.com, sherwin-williams.com, bestbuy.com, grainger.com,
memberstack.com, learnbrands.com, cannazipbags.com, fernway.com, medallia/ADT survey
mail.

**Safety floor caught 6 threads** in this same promo/social/forums result page marked
`IMPORTANT` that must NOT be trashed despite matching category+age: two from
Francisco@high-grass-farms.apextrading.com, one from Phil@sussex-cultivation.apextrading.com,
two from customerexperience@feedback.wm.com, and one from **metrc@stellaconnect.net**
(doubly protected — both `IMPORTANT` and on the NEVER-TOUCH allowlist, since
stellaconnect.net = Metrc).

No starred threads observed in this sample.

**Action taken: NONE (DRY_RUN).** Would have applied the TRASH sensitive-label to the
qualifying subset (recoverable 30 days).

## category:updates — report-only (never auto-trashed, per runbook)
Confirmed this category is exactly as risky as the runbook warns: it mixes real
financial/security mail with noise. Sample included live Dutchie support correspondence
(with Lemar's own SENT replies), QuickBooks/Intuit invoices and payment confirmations,
ADT alarm system notifications, a ParkeBank banking-update notice (allowlisted), FedEx
receipts and print-order confirmations, scheduled Headset vendor/inventory reports
(allowlisted, headset.io), Google Workspace/security alerts, cfins.com password-reset
codes, a Progressive commercial-insurance payment-due reminder, Extra Space Storage
account emails, an NECANN newsletter, and personal r/gardening Reddit-digest mail.

Old sender domains worth Lemar clearing by hand if desired: fedex.com (receipts),
redditmail.com (personal subscription), extraspace.com, cannazipbags.com, thrivepop.com.

Left entirely untouched, as designed.

## Bottom line
First supervised DRY_RUN night behaved as intended: found real candidates in both PART A
and PART B, and the precision/safety gates correctly excluded genuine correspondence,
IMPORTANT-flagged threads, and an allowlisted vendor thread that would otherwise have
looked disposable.

**Recommend Lemar:**
1. Skim this note and tonight's #reports digest.
2. Optionally add the newly-discovered vendor-menu domains (above) to the seed list in `anchors.md`.
3. Confirm no false positives concern him.
4. Then flip `DRY_RUN = false` in `.claude/routines/inbox-janitor.md` on `main` to go live on the next run.

## Sources
- gmail: search_threads queries against lemar@cuzziesnj.com inbox, 2026-07-12 (PART A vendor-menu candidates + PART B trash-sweep candidates + category:updates sample)
