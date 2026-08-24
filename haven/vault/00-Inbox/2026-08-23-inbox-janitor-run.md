---
created: 2026-08-23T23:11-04:00
updated: 2026-08-23T23:11-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-08-23 (live)

Nightly Gmail tidy on the connected account `lemar@cuzziesnj.com`. Mode: **LIVE**
(`DRY_RUN = false`). Runbook `.claude/routines/inbox-janitor.md`, IDs from `.claude/anchors.md`.

## Counts

- **Vendor menus archived: 16** (labeled `Vendor Menus` / `Label_8`, `INBOX` removed — never trashed)
- **Threads trashed: 3** (all >12 months old, `category:promotions`)
- **Over the 200/run cap: 0**
- **Candidates skipped by the safety floor: 3 threads** — see below

## PART A — vendor menus archived (16)

Qualified on vendor-domain + menu/pricing/availability signal. Recoverable at any time —
they are in All Mail under `Vendor Menus`, only out of the inbox.

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| `1a0247533c2c793f` | 🍭 SUGAR HIGH IS HERE — Save Up to 20% on the NEW 2G AIO Launch | Matt@little-leaf-labs.apextrading.com | 2026-08-21 |
| `1a01979e74718222` | LAST CHANCE: Friday's Delivery & 20% Off Dr. Zodiak | Matt@little-leaf-labs.apextrading.com | 2026-08-19 |
| `1a01135b69388fd7` | This is your CUUE 🍫 Effects-Based Chocolates Have Arrived | marketing.us@terrascend.com | 2026-08-17 |
| `1a0105594a447482` | RS-11: CHASE THE RAINBOW 🌈 (Google Sheet menu link) | Mark@agri-kind.apextrading.com | 2026-08-17 |
| `1a01028fbb51b0bb` | FINAL DAYS: 20% OFF Every Dr. Zodiak Product | Matt@little-leaf-labs.apextrading.com | 2026-08-17 |
| `1a00fe37c21e9c1c` | NightCap is restocked! + budtender selling tip | hking@laddsllc.com | 2026-08-17 |
| `19fa9751e302f8ef` | LAST CALL - LOST FARM B1G1 AND CAMINO B2G1 | dan.grandrino@kivaconfections.com | 2026-07-28 |
| `19d6342b252a986a` | B3GO Lost Farm & Camino 4/20 Early Bird Wholesale Offer | carlos.gamez@kivaconfections.com | 2026-04-06 |
| `19d54ecc0b2f4ee8` | 🌿Fresh Grow 420 Sale 🌿 | Kathy@freshcannabis.co | 2026-04-03 |
| `19d4a217fcfcb9cb` | 🌿Fresh Grow \| 420 Blow Out Sale! 🌿 | Kathy@freshcannabis.co | 2026-04-01 |
| `19d1b1d202cde851` | 4/20 Loading… Lock In Your Inventory NOW + Major Deals | allanf@harvestmoonfarmsnj.com | 2026-03-23 |
| `19d10f0cba5d56ec` | 🌿 The 4/20 Countdown Is On… Are you Stocked? | caitlin@jerseysmooth.com | 2026-03-21 |
| `19cc4e939d8732c4` | Jersey Smooth + CUZZIES (personalized menu link) | que@jerseysmooth.com | 2026-03-06 |
| `19bfbafda57654a9` | TerrAscend - BIG Vape Sale & Legend/Kind Tree Flower Sale | ndesiderio@terrascend.com | 2026-01-26 |
| `19b70983492f0d80` | This is How January Starts (fresh drops / inventory planning) | dan@northlake.supply | 2025-12-30 |
| `19a89cd117c9a700` | Simply Herb Shake is back on the menu | nbonsanto@awholdings.com | 2025-11-15 |

**Deliberately NOT archived** though they matched the domain seed list — these are real
business correspondence, not menus: the Buds Goods invoice INV-0000153 collections thread,
the Harvest Moon / Fresh Cannabis wholesale-agreement thread, the QCC onboarding thread,
the Garden Society mock-order and net-terms thread, the Ascend manifest/delivery threads,
and the year-end vendor-balance thread. Precision over recall, per the runbook.

## PART B — trashed (3)

All three: >12 months old, `category:promotions`, not starred, not important, no genuine
filing label, sender not on the NEVER-TOUCH allowlist. **Recoverable from Gmail Trash for
30 days** using these thread IDs.

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| `198d82474bd94ee5` | Just add popcorn. ($5 certificate expires 9/1) | BestBuy@email.bestbuy.com | 2025-08-23 |
| `198d6f5237635b76` | 👀 COMING SOON: The Traveler Pro | info@fernway.com | 2025-08-23 |
| `198d4ac2824690ca` | SAVE THE DATE: You're Invited To Party With Fernway | liam@fernway.com | 2025-08-23 |

### Skipped by the safety floor (3 threads)

The old-promotions pool was only 15 threads to begin with; these were held back:

- **`CTA@sos.nj.gov`** — 9 Cannabis Training Academy threads. Held by the `*.gov` clause
  of the NEVER-TOUCH allowlist. The query's explicit `-from:crc.nj.gov` did not catch
  `sos.nj.gov`; the wildcard rule did. **Tuning note:** consider adding `sos.nj.gov`
  explicitly to the allowlist in anchors so the query filters it server-side.
- **`surveys@dutchie.com`** — dutchie implementation survey, thread `19644c6a0e498f47`.
  Carries `IMPORTANT` on two messages.
- **`sales@hamiltonfarms.com`** — thread `196110a96c91e798`. Matched promotions, but it is
  a live order-terms negotiation (minimums, payment terms) with Donte looped in, and carries
  `IMPORTANT`. Left alone.
- **`iccc@icic.org`** — ICCC "mini-MBA" thread `1826944b41c19b7a` from 2022. `IMPORTANT`.

## `category:updates` — report-only, NOT swept

Roughly **200 inbox threads older than 12 months** sit in `category:updates`. Confirmed
again tonight that this category is unsafe to automate: it holds Google Voice texts from
actual customers, jotform register-float approvals and signed-count forms, Kiva post-delivery
invoices, Monday automation errors, and Drive share notices — mixed in with newsletters.

Sender domains Lemar may want to clear **by hand**: `nytimes.com` (breaking-news +
From-the-Times ads), `e1.theathletic.com`, `redditmail.com`, `notifications.monday.com`,
`jotformsign.com` (signed-successfully receipts, not the approval requests).

## For Lemar

Nothing in tonight's sweep surfaced a business item needing action. The one item worth a
glance is the `sos.nj.gov` tuning note above.

## Sources
- gmail: connected account `lemar@cuzziesnj.com`, threads listed above
- claude: Basil nightly run, 2026-08-23 23:11 ET
