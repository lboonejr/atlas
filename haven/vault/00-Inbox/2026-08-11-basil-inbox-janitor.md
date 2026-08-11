---
created: 2026-08-11T23:15-04:00
updated: 2026-08-11T23:15-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-11 (LIVE, DRY_RUN=false)

Account: lemar@cuzziesnj.com

## Summary
- Archived 13 vendor menus out of the inbox (labeled `Vendor Menus` / `Label_8`, removed `INBOX`)
- Trashed 2 old promotional threads (>12 months, category:promotions/social/forums)
- 0 threads over the 200/run cap
- 17 trash candidates in the disposable categories were found but skipped by the safety gate (allowlist domains or IMPORTANT-labeled)

## PART A — Vendor menus archived (13)

Scanned inbox threads from the vendor-domain seed list. ~201 inbox threads match those
domains total, but the large majority are genuine business correspondence — invoices, AR
statements, delivery scheduling, collections notices — and were correctly left untouched
per the routine's precision-over-recall rule. Archived only threads with an explicit
menu/price-sheet/drop signal and no correspondence thread attached:

1. `19fed66acf8fee5a` — "Essence 8th Deal $12.50 !" — Tyler.Marsh@verano.com — 2026-08-10
2. `19fed64c78f7ae42` — "Our #1 Strain Right Now, In Every Format" — dan@northlake.supply — 2026-08-10
3. `19fececd10f14205` — "TerrAscend Menu - Launch: Rosin Gummies & New Genetics..." — ndesiderio@terrascend.com — 2026-08-10
4. `19fec55eac25714a` — "Happy Farmer: Flower Refresh?" — Andrew@the-happy-farmer-llc.apextrading.com — 2026-08-10
5. `19fec397de1c2792` — "Sour Diesel. All Gas. No Brakes." — Mark@agri-kind.apextrading.com — 2026-08-10
6. `19fec33eff8e544f` — "QCC NJ Menu 8.10.26 - NEW SKUs Just Landed!" — kbreiner@qccnj.com — 2026-08-10
7. `19fec186bab0d711` — "Kiva Camino/Lost Farm Menu - August Week 2" — dan.grandrino@kivaconfections.com — 2026-08-10
8. `19febf9baaf5b7d4` — "Prolific Menu 8.10 | New Gelato Cream OZ..." — anthony@prolificgrowhouse.com — 2026-08-10
9. `19febf0db30773da` — "Two Standout Strains One Limited Reserve Drop" — marketing.us@terrascend.com — 2026-08-10
10. `19febe49c882e7e8` — "Ascend Menu!! HIGH WIRED PRE ROLLS!! OZONE RSO GUMMIES!!" — mgargiule@awholdings.com — 2026-08-10
11. `19febe3c2127ed97` — "Bud's Goods / New Strains..." — bsantos@budsgoods.com — 2026-08-10
12. `19febd72e1ae7e34` — "Illicit NJ Menu- Fat Sacks are back..." — jb@illicitgardens.com — 2026-08-10
13. `19febc488d9b11d7` — "Updated Menu + HOLIDAY at The Exchange!" — hking@laddsllc.com — 2026-08-10

Operator note: no change needed to the vendor-domain seed list — the ~188 other matched
threads are real correspondence, correctly left in the inbox.

## PART B — Trash audit (recoverable in Gmail Trash for 30 days)

1. `19895291a0e3dc66` — "*** Apple Event alert *** Did someone say 'amazing DEALS'?" — BestBuy@email.bestbuy.com — 2025-08-10
2. `198945dac50cae16` — "Make them remember your brand" — marketing@cannazipbags.com — 2025-08-10

## Skipped from trash (safety gate) — 17

- 6x `parkebank@parkebank.com` (NEVER-TOUCH allowlist)
- 6x `CTA@sos.nj.gov` (`*.gov` allowlist)
- 1x `surveys@dutchie.com` (thread carries IMPORTANT-labeled messages)
- 1x `sales@hamiltonfarms.com` thread "Hamilton Farm's Weekly Menu & Go2 8ths release!" (genuine back-and-forth correspondence re: order terms, IMPORTANT-labeled)
- 1x `iccc@icic.org` (thread carries an IMPORTANT-labeled message)

## PART B — report-only: old `category:updates`

~201 threads older than 12 months sitting in `category:updates` (never auto-trashed per
the routine). Sample sender domains seen: jotform.com, jotformsign.com, nytimes.com,
theathletic.com (e1.theathletic.com), redditmail.com, monday.com, linqapp.com, google.com
(workspace-noreply / drive-shares-dm-noreply) — plus protected senders
`quickbooks@notification.intuit.com` and `info@headset.io` mixed in (never-touch, left
alone). Lemar may want to hand-clear the non-protected newsletter/notification senders
(jotform, nytimes, theathletic, reddit) if he wants them gone — Basil does not touch
`category:updates` automatically.

## Recovery

Anything trashed above sits in Gmail Trash for 30 days and can be restored from the
thread IDs listed.

## Sources
- gmail: threads listed above (Basil nightly sweep, lemar@cuzziesnj.com)
