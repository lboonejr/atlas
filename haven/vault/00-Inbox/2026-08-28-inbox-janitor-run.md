---
created: 2026-08-28T23:07:00-04:00
updated: 2026-08-28T23:07:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run log — 2026-08-28

Mode: LIVE (`DRY_RUN = false`)
Account: lemar@cuzziesnj.com

## Summary
- Vendor menus archived (PART A): **2**
- Threads trashed (PART B): **6**
- Threads over the 200/run cap: **0**
- Old `category:updates` threads (report-only, not touched): **~201**

## PART A — vendor menus archived (labeled `Vendor Menus`, removed from INBOX)
1. Thread `1a0436da20b2c1c5` — "Harvest Moon Farms Menu Update 🌝🌝🌝" — allanf@harvestmoonfarmsnj.com — 2026-08-27
2. Thread `1a0434b1056ab406` — "TerrAscend Menu - 50% OFF Valhalla, $15 KT 3.5g, New RSO & Chocolates - 8-27-26" — ndesiderio@terrascend.com — 2026-08-27

A broader domain-match sweep surfaced ~201 additional inbox threads from seed-list vendor
domains, but the large majority were promo blasts without an explicit menu-signal subject,
personal 1:1 correspondence (e.g. the Hillary King / Ladd's LLC thread, the Prolific
Growhouse partnership thread), or protected by IMPORTANT/STARRED. Left in place per the
runbook's "prefer precision over recall" rule — a real menu wrongly left in the inbox is
harmless.

## PART B — trash sweep (12-month cutoff, category:promotions/social/forums, recoverable 30 days)
1. Thread `198eda73408f84c7` — "Guava is a Go!" — wholesale@verano.com — 2025-08-27
2. Thread `198ec849fa166a0d` — "News & Resources for Small Businesses" — noreply@mail.lendistry.com — 2025-08-27
3. Thread `198ec5f1a45c0c21` — "ZapConnect 2025: Explore the full agenda 👀" — events@send.zapier.com — 2025-08-27
4. Thread `198ec212ed33acd8` — "🔥 NEW GMO Root Beer + Fresh Prerolls & Limited Drops Inside" — Francisco@high-grass-farms.apextrading.com — 2025-08-27
5. Thread `198eb6889b2f7b64` — "6 sublime beaches on the Great Lakes" — fromthetimes-noreply@nytimes.com — 2025-08-27
6. Thread `198e8731ff555929` — "Flower + Pre-rolls!" — wholesale@verano.com — 2025-08-26

### Skipped candidates (27 total in the 12mo promo/social/forums sweep; 21 skipped)
- **18** skipped for NEVER-TOUCH allowlist domain: `sos.nj.gov` (`*.gov`, 10 threads — CTA
  "Ask Me Anything" webinar notices) and `parkebank.com` (8 threads — newsletters / fraud tips)
- **3** skipped because the thread carried an IMPORTANT-labeled message somewhere in it:
  surveys@dutchie.com implementation survey; the sales@hamiltonfarms.com weekly-menu thread
  that turned into a live order conversation with Donte Bronaugh; iccc@icic.org ICCC program
  invite

## Report-only: old `category:updates` (never auto-trashed)
~201 threads older than 12 months in `category:updates`. Sample sender domains seen:
nytimes.com (breakingnews), jotform.com / jotformsign.com, headset.io (on the allowlist —
correctly left alone), google.com (voice-noreply, Google Play developer notices), evite.com,
cannazipbags.com, ellacash.com (carried an IMPORTANT message), slack.com. Lemar may want to
clear these by hand; Basil never sweeps this category — invoices, bank, payroll, and legal
receipts live mixed in here per the runbook.

## Recovery
Everything trashed above sits in Gmail Trash for 30 days and is recoverable by thread ID.

## Sources
- gmail: 8 threads acted on this run (2 archived, 6 trashed) — IDs listed above
