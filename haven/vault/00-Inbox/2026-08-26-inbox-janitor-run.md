---
created: 2026-08-26T23:07:00-04:00
updated: 2026-08-26T23:07:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-08-26 (Basil)

Nightly Gmail cleanup on the connected account (`lemar@cuzziesnj.com`). Mode: **LIVE**
(`DRY_RUN=false`).

## PART A — vendor menus archived: 3

All three labeled `Vendor Menus` (`Label_8`) and removed from `INBOX`. A 4th candidate
(laddsllc.com thread "Let's get together this week? (+ Monday Menu Drop!)") was left in
the inbox — it's an active back-and-forth conversation with the vendor rep (Lemar
replied twice, discussing Cuzzie's store status), not a pure menu blast, so it failed
the "only weakly a menu, skip it" precision test.

1. Thread `1a039fb3a7a7d469` — "SUN MENU - Labor Day SALE" — tj@arescanna.com — 2026-08-25
2. Thread `1a039bdbfae914c1` — "Harvest Moon Farms: Updated Wholesale Menu" — allanf@harvestmoonfarmsnj.com — 2026-08-25
3. Thread `1a034075185c4f1e` — "Ascend Updated Menu | Limited Stock Alerts..." — nbonsanto@awholdings.com — 2026-08-24

## PART B — trash sweep: 5 trashed of 8 candidates, 0 over the 200/run cap

Query: `older_than:1y (category:promotions OR category:social OR category:forums)`,
minus starred/important/NEVER-TOUCH allowlist domains. Full audit list — recoverable in
Gmail Trash for 30 days:

1. Thread `198e21cd5e7b6517` — "Take An Extra 10% Off Your Holiday Orders!" — christopher.beyer@ayrwellness.com — 2025-08-25
2. Thread `198e1df0ad73a5b8` — "Final call: Your data deserves better" — marketing@engage.canva.com — 2025-08-25
3. Thread `198e1c55e16e033f` — "The Blue Bucket Sale is NOW ON." — email@em.sherwin-williams.com — 2025-08-25
4. Thread `198e1b1fe3e23994` — "How Was Your Recent Experience with PSE&G's Telephone Service?" — websurvey1973036@us.confirmit.com — 2025-08-25
5. Thread `198e163f07e2b1c5` — "Live Flavor. Zero Fuss." — marketing.us@terrascend.com (vendor-marketing, >12mo old, not on allowlist) — 2025-08-25

Skipped 3 candidates for carrying an `IMPORTANT` flag on at least one message in the
thread (never-trash floor):

- Thread `19644c6a0e498f47` — surveys@dutchie.com, "How was your implementation experience with dutchie?"
- Thread `196110a96c91e798` — sales@hamiltonfarms.com, "Hamilton Farm's Weekly Menu & Go2 8ths release!" — this one is a live order-terms conversation (dontebronaugh@gmail.com ↔ breali@hamiltonfarms.com), not disposable anyway
- Thread `1826944b41c19b7a` — iccc@icic.org, "Apply Now for the ICCC Program..."

## category:updates — report-only, never auto-trashed

201 threads older than 1y sit in `category:updates`. Sample sender domains observed:
jotform.com, jotformsign.com, nytimes.com, headset.io, apextrading.com, google.com
(voice-noreply), progressive.com, wm.com, aiq.com, intuit.com (notification). This
category mixes invoices/receipts/legal mail with ads per the runbook's own recon, so it
is left for Lemar to clear by hand — no action taken.

## Notes

No genuine user-applied Gmail labels exist on this account beyond the automation labels
(`Label_1`–`Label_9`), so the "genuine filing label" protection never triggered this run.

## Sources
- gmail: 8 threads actioned across PART A/B (see thread IDs above), all in-account `lemar@cuzziesnj.com`
