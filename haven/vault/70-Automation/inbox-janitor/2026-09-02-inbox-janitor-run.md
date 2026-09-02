---
created: 2026-09-02T23:07-04:00
updated: 2026-09-02T23:07-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-09-02 (live, DRY_RUN=false)

Basil's nightly Gmail cleanup on `lemar@cuzziesnj.com`.

## PART A — vendor menus archived: 102

Searched `in:inbox` against the vendor-domain seed list (anchors). 110 total domain
matches; 102 qualified as menus/marketing and were labeled `Vendor Menus`
(`Label_7063567382570959882`) and removed from `INBOX`. 8 were skipped as
non-menu 1:1 business correspondence and left untouched in the inbox:

- 4x Verano AR-statement / payment-plan threads with Lemar (`Vladimir.Jovanovic@verano.com`,
  subjects "Cuzzie's Dispensary || AR Statement || Verano" and variants) — active balance
  negotiation, not marketing.
- 4x `njaccountsreceivable@awholdings.com` "Account On Hold" / "Friendly Reminder –
  Outstanding Balance" — collections notices, not menus.
- 1x TerrAscend rep OOO notice (`ndesiderio@terrascend.com`, "Heads up, I am OOO 8/20-8/24" /
  "Out of office next week") — not a menu.
- 1x QCC onboarding-docs thread (`kbreiner@qccnj.com`) with `admin@cuzziesnj.com` replies —
  business correspondence, not a menu.

Domains archived this run: apextrading.com (Niche / Little Leaf Labs / Sugar High /
Dr. Zodiak / DANK / Goodies / Moonwalkers), verano.com (Essence / Raw Garden / Avexia /
promos), terrascend.com (Kind Tree / CUUE / Valhalla), northlake.supply (Nimbus / Cloud
2.0). No trashing occurred in this PART (archive + label only, per floor).

Four of the 102 already carried the Vendor Menus label from a prior partial run but were
still sitting in the inbox (`1a0580518ffcefb7`, `19e3c97677cebdaa`, `19e18f27a696c6af`,
`19d88c3d4cb37873`) — only `INBOX` was removed for those. Three of the archived threads
also carry the unowned "Action Needed" label (`Label_374039230306167562`) from an unknown
routine; that label was left untouched (not repurposed), per anchors guidance.

## PART B — trash sweep: 0 trashed, 0 over cap

`older_than:1y (category:promotions OR category:social OR category:forums)` returned
**zero** matching threads mailbox-wide. Nothing qualified for Trash this run — no audit
list needed. Also checked `older_than:1y category:updates` (report-only, never
auto-trashed): also **zero** old threads in that category. The account currently has no
mail older than 12 months sitting in any of the four swept categories.

## Skipped-for-safety count

N/A — PART B's candidate query itself returned 0, so there was nothing to test against
the starred/important/allowlist/genuine-label floor this run.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox + mailbox-wide category search, 2026-09-02 run
