---
created: 2026-07-09T23:00-04:00
updated: 2026-07-09T23:00-04:00
domain: cuzzies
type: log
status: active
tags: [inbox-janitor, basil, gmail-cleanup, dry-run, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor DRY RUN preview — 2026-07-09

First supervised run of the nightly Inbox Janitor routine (`.claude/routines/inbox-janitor.md`,
commit `e4ceb5d`). `DRY_RUN = true` for this run — **zero Gmail actions were taken**: no
archive, no label, no trash. This note is the preview Lemar should vet before flipping
`DRY_RUN` to `false`.

Account acted on (read-only this run): `lemar@cuzziesnj.com`.

## PART A — Vendor menus (would-archive)

Query matched inbox threads from the 20-domain vendor seed list in anchors (qccnj.com,
verano.com, terrascend.com, awholdings.com, freshcannabis.co, kivaconfections.com,
illicitgardens.com, harvestmoonfarmsnj.com, apextrading.com + subdomains, budsgoods.com,
novafarms.com, prolificgrowhouse.com, parksgrove.com, laddsllc.com, missgrass.com,
jerseysmooth.com, thegardensociety.com, arescanna.com, 1906.shop, northlake.supply).

- **Total inbox threads matching these domains:** ~201
- **Would-archive** (genuine vendor menu/price-sheet/promo emails — the intended target): **~175-180**
- **Would NOT archive** — found mixed into the domain match, real correspondence that must stay in the inbox:
  - Prolific Growhouse "Overdue Invoice/New Bank Account" — 3 separate reminders (threads
    `19effba6d8f7c423`, `19ed686d78d9605e`, `19eb27b65b1411e5`)
  - "Past Due Payment Reminder" from The Garden Society AR (threads `19ef5a3dac10b873` and
    `19ead8aa48036015` — the second is **STARRED** and contains Lemar's own reply disclosing
    Cuzzie's temporary closure)
  - "Payment Update" thread with Harvest Moon Farms (`19eb246b48bf09fa`) — real investment/
    payment conversation, multiple sent replies from Lemar
  - "Scheduling Verano Delivery - Cuzzie's" (`19ed1ecbcaa738ee`) + its auto-reply (`19ed2053345f03e3`)
  - "Cuzzie's || AR Statement || Verano" (`19e949131349800b`)
  - "Harvest Moon Farms connecting with Cuzzie's" (`19ea884575d02d16`) — real meeting-scheduling thread
  - "HOB Payment Instructions" from Bud's Goods (`19e8da657e3e713e`)
  - "Important Update - Linden Transfer Tax" (`19ed19b411ff6473`)
  - "Introducing - Hillary King!" personnel announcement (`19ed2afe4e185b2d`)
  - "Out of office next week" auto-reply from TerrAscend (`19edd616a0787f97`)
  - ~10 further weak matches skipped per "precision over recall" (brand-awareness pitches,
    Pride Month greetings, personnel congratulations, banner-ad requests, self-ordering info)

**Tuning finding:** the vendor-domain seed list is doing double duty — the same reps who send
menus also send AR/invoice/scheduling correspondence, and PART A's current "domain OR subject
signal" gate is too loose to tell them apart reliably. Recommend PART A require an explicit
menu/pricing signal (not domain membership alone) before going live, so recurring vendor AR
threads don't get swept into Vendor Menus.

## PART B — Trash sweep (would-trash)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)`
(cutoff: before 2025-07-09).

- **Total matching threads:** ~201 (estimate); reviewed in depth across ~150
- **Hard-floor exclusions confirmed working correctly** (would stay untouched even live):
  - 1 STARRED thread (`197c133bac012440`, Niche "New SKU's - Don't Miss Out!")
  - ~15 IMPORTANT-flagged threads (apextrading.com sub-brands, vangst.com, treez.io, make.com,
    hoodieanalytics.com, aiq.com)
  - 1 `*.gov` sender: `CTA@sos.nj.gov` (`197a8cdb6f1d9200`) — allowlist protected
  - 1 `intuit.com` sender caught in this category (`1976446b606e2260`, QuickBooks appointment
    note) — allowlist protected (also IMPORTANT)
- **Net genuine disposable promo/social/forum threads:** roughly 130+ in the reviewed sample;
  full set likely ~170-180 after exclusions, under the 200/run cap.
- Representative senders: wholesale@verano.com, marketing.us@terrascend.com, marketing@vangst.com,
  marketing@engage.canva.com, marketing@treez.io, info@fernway.com, email@em.sherwin-williams.com,
  BestBuy@email.bestbuy.com, info@make.com, noreply@aiq.com, jamie-nichenfe.com (Niche),
  flyers@webstaurantstore.com, hello@vendorline.com, apextrading.com sub-brand marketing,
  adt@express.sea1.medallia.com survey reminders, Grainger/Home Depot Pro survey emails.
- **No threads were trashed.**

## category:updates (report-only — never auto-trashed)

Query: `older_than:1y category:updates`, ~201 estimate. Confirms the runbook's warning: this
category mixes real financial/legal mail with disposable notices in this inbox. Sample sender
domains found: `notification.intuit.com` (QuickBooks invoices), `parkebank.com` (bank notice),
`firstinsurancefunding.com` (e-payment confirmation), `pactsafe.com` (legal agreement),
`accounts.google.com` (security alert), `sos.nj.gov` (CTA newsletter), `extraspace.com`
(storage account/rental), `jotform.com` (receipt), `softtouchpos.com` (POS verification code),
`readyrefresh.com` (water service), `glueupmail.com` (trade association), `headset.io`
(analytics report). None auto-trashed — flagged for Lemar to clear by hand if desired.

## Bottom line

Zero Gmail actions taken tonight. The one real finding worth acting on before going live:
tighten PART A's vendor-menu match logic so it doesn't sweep real AR/invoice/scheduling
correspondence out of the inbox alongside genuine menus. PART B's safety floor (starred /
important / allowlist / `*.gov`) held up correctly against a real, messy inbox.

## Sources
- gmail: search `in:inbox {from:<vendor-domain-list>}` — PART A candidate set
- gmail: search `older_than:1y (category:promotions OR category:social OR category:forums)` — PART B candidate set
- gmail: search `older_than:1y category:updates` — report-only set
