---
created: 2026-08-25T23:07:00-04:00
updated: 2026-08-25T23:07:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-08-25 (live)

Basil's nightly Gmail cleanup, mode: **live** (`DRY_RUN = false`). Account: `lemar@cuzziesnj.com`.

## Counts
- **Vendor menus archived:** 8 (out of inbox, into `Vendor Menus` label)
- **Threads trashed:** 0
- **Threads over the 200/run cap:** 0
- **Old `category:updates` threads (report-only, not touched):** ~201 (resultCountEstimate)

## PART A — vendor menus archived (label added, INBOX removed)
| Thread ID | Sender | Subject |
|---|---|---|
| 1a035fe578b33a71 | Tyler.Marsh@verano.com | New Menu! Easy Landings Pre Orders LIVE! |
| 1a034e99beed0f6b | jpina@terrascend.com | TerrAscend Menu: New RSO 1G Syringe, 50% OFF Valhalla, Buy 2 Get 1 Legend Carts, $15 Kind Tree 3.5G, & Moree! |
| 1a034d35742ca857 | dan@northlake.supply | This Week's Menu: NLS Vapes Up to 30% Off + Nimbus Carts from $20 |
| 1a0347c76baf0e4f | Peter@canfections-nj-llc.apextrading.com | A trusted favorite that is 61.5% THC (APEX Menu Share) |
| 1a0346837076de88 | carlos@harvestmoonfarmsnj.com | Harvest Moon Farm Menu 8.24.26 |
| 1a034654160e477e | dan.grandrino@kivaconfections.com | Camino Lost Farm Menu - August Week 4 - LAST CHANCE FOR DEALS |
| 1a0344e86fd9299c | kbreiner@qccnj.com | QCC NJ Menu 8.24.26 |
| 1a033eab243a2382 | anthony@prolificgrowhouse.com | Prolific Menu 8.24 \| Gelato Cream Fully Stocked + Prolific & Bob Vapes Available! |

A larger batch of vendor-domain hits (~200 estimate) also came back on the seed-domain
search, but the rest were correspondence — invoices, manifests, payment disputes,
onboarding threads, OOO notices, event invites, personal replies from Lemar — not weekly
menu drops. Left alone per the "prefer precision" rule. Several older (2025-dated,
pre-cutoff) vendor promo blasts (e.g. northlake.supply, `*.apextrading.com` "Shady
Extracts" series) surfaced too; those are >12mo old and belong to PART B's judgment, not
PART A, and none of them qualified for trash either (see below).

## PART B — trash sweep
Candidate query: `older_than:1y (category:promotions OR category:social OR category:forums) -is:starred -is:important` → 20 candidates. **All 20 were protected** — none trashed:
- 12 from `CTA@sos.nj.gov` (`*.gov` — NEVER-TOUCH allowlist)
- 7 from `parkebank@parkebank.com` (NEVER-TOUCH allowlist)
- 1 from `iccc@icic.org` (thread carries an `IMPORTANT`-labeled message)

(One additional candidate, the `dutchie.com` survey thread and the `hamiltonfarms.com`
menu-turned-negotiation thread, also surfaced in the raw search but both carry
`IMPORTANT`-labeled messages / genuine correspondence, so both were skipped per the
Safety floor before ever reaching the allowlist check.)

**0 threads trashed. 0 over the cap.**

## `category:updates` — report-only, not touched
~201 old (`older_than:1y`) updates-category threads. Representative sender domains seen:
`nytimes.com` (news digests), `theathletic.com` (sports newsletter), `redditmail.com`
(subreddit digests), `notifications@monday.com` (stale automation-error alerts),
`voice-noreply@google.com` (missed-call notices), `info@headset.io` (scheduled report
exports — allowlisted, not for trash), `noreply@jotform.com` / `jotformsign.com`
(register float approvals — business-critical, not disposable),
`notification.intuit.com` (QuickBooks invoices — allowlisted). Lemar may want to
hand-clear the news/sports/reddit newsletter noise; nothing here was touched.

## Notes
- No allowlist or seed-domain-list changes needed this run.
- No genuine business items surfaced that need Lemar's attention beyond what's already
  tracked elsewhere.

## Sources
- gmail: `lemar@cuzziesnj.com`, run 2026-08-25 ~11pm ET
