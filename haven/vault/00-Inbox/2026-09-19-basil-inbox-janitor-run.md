# Basil — Inbox Janitor run — 2026-09-19

---
created: 2026-09-19T23:07:00-04:00
updated: 2026-09-19T23:07:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

## Run summary
- Date: 2026-09-19 (~11pm ET scheduled run)
- Mode: LIVE (`DRY_RUN=false`)
- Account: lemar@cuzziesnj.com
- Vendor menus archived: 1
- Threads trashed (>12mo, promotions/social/forums): 10
- Threads over the 200/run cap: 0

## PART A — vendor menu archived
- Thread `1a0af81163a94a9a` — "🚨 BLUEPRINT HAS LANDED – VERY LIMITED SUPPLY" — allanf@harvestmoonfarmsnj.com — 2026-09-17 — labeled **Vendor Menus**, removed from INBOX. Genuine wholesale-menu blast with `.xlsx` order-sheet attachments; bcc'd to Lemar, no personal reply thread attached to it.
- Reviewed roughly 140 of the 201 inbox threads from the vendor-domain seed list across several targeted searches (plain domain search, `subject:menu`+attachment, body:menu+attachment). The overwhelming majority were relationship correspondence, AR/collections notices, banking-info updates, event/NECANN invites, and sweepstakes — not menu blasts — so per the routine's "prefer precision over recall" rule they were left in the inbox untouched.

## PART B — trash audit (full recovery list, all in Gmail Trash for 30 days from 2026-09-19)
1. `1995f0fda34a1efd` · "Prepare for a natural disaster with these items" · fromthetimes-noreply@nytimes.com · 2025-09-18
2. `1995e6bd3cf24a2c` · "Did you catch Loops at Hall of Flowers?" · noreply@aiq.com · 2025-09-18
3. `1995dd801f887dc0` · "Breaking news: Judge stops Trump administration from removing Guatemalan children" · breakingnews-noreply@nytimes.com · 2025-09-18
4. `1995dc90ed520c79` · "Can your current loyalty & marketing tool show you direct revenue per campaign?" · marketing@dutchie.com · 2025-09-18
5. `1995d6b93fde06cd` · "Our New Menu! 9.18.25" · sales=greenmedicinenj.com@hubspotstarter.hs-send.com · 2025-09-18 (a competitor dispensary's marketing blast, not one of Lemar's own vendors — correctly promotional, not a vendor menu)
6. `1995d612ada4fee0` · "Transform with Warrior Yoga - Sept. 20th & 27th!" · info@vedawarrior.com · 2025-09-18
7. `1995d3bf36a76be7` · "Recommended templates based on your search" · product@engage.canva.com · 2025-09-18
8. `1995d3744fd8dd1e` · "NY/NJ Regional Supply Chain Luncheon x Staten Island Transportation & Infrastructure" · local@localcontent.com · 2025-09-18
9. `1995d2bab42589db` · "Grow Smarter, Not Harder — Partner with Leafwire" · marc@necann.com · 2025-09-18
10. `1995cbacb5f2732a` · "Final Chance: Request for Assistance" · customerexperience@feedback.wm.com · 2025-09-18

All 10 were `older_than:1y`, in `category:promotions/social/forums`, not starred, not important, carried no protective label, and their sender domain was not on the NEVER-TOUCH allowlist.

## Skipped candidates (tuning data for the allowlist / important-guard)
- 12 threads from `CTA@sos.nj.gov` skipped — `*.gov` allowlist protection.
- 8 threads from `parkebank@parkebank.com` skipped — explicit allowlist domain.
- 6 threads from `apextrading.com` subdomains (Jade@hearth-wellness-llc, Francisco@high-grass-farms, andrew@northlake.supply) skipped — already carry the **Vendor Menus** label, which counts as a protective user label under the routine's safety floor (only the 5 Samira automation labels are non-protective; every other user label protects).
- 3 threads skipped for carrying an IMPORTANT-labeled message: a Dutchie surveys thread (`19644c6a0e498f47`), a Hamilton Farms correspondence thread (`196110a96c91e798`), and an ICCC thread (`1826944b41c19b7a`).
- Total candidate pool matching `older_than:1y` + `category:promotions/social/forums` (mailbox-wide, not just inbox) was 39; 10 trashed, 29 excluded by the gates above.

## `category:updates` — report only (never auto-trashed per routine)
~201 threads older than 12 months sit in `category:updates`. Sample sender domains seen: nytimes.com, jotform.com/jotformsign.com, adt.com, readyrefresh.com, headset.io (allowlisted), notification.intuit.com (allowlisted). This category mixes real financial/legal mail with ads per the routine's own warning — left untouched; Lemar can clear it by hand if he wants.

## Sources
- gmail: nightly sweep across `lemar@cuzziesnj.com`, 2026-09-19
