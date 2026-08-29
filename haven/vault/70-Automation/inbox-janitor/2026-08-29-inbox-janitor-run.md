---
created: 2026-08-29T23:07-04:00
updated: 2026-08-29T09:48-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-29 (live run, DRY_RUN=false)

Account acted on: `lemar@cuzziesnj.com`.

## Summary
- Vendor menus archived (labeled Vendor Menus, removed from Inbox): **8**
- Threads trashed (>12mo, promotions/social/forums, not starred/important/allowlisted): **6**
- Threads over the 200/run cap: **0**
- Candidates skipped in PART B for is:important / allowlist protection: **13** total — 3
  IMPORTANT-labeled threads (a Dutchie implementation-survey thread, a Hamilton Farms
  wholesale-menu thread that turned into a real payment-terms negotiation, an ICCC
  "mini-MBA" program thread) and 10 threads from `CTA@sos.nj.gov` protected by the
  `*.gov` NEVER-TOUCH allowlist clause.

## PART A — Vendor menus archived (label `Vendor Menus` / `Label_8`, removed from Inbox)

| Thread ID | Sender domain | Subject | Date |
|---|---|---|---|
| `1a048e344468a3c3` | kivaconfections.com | Camino/Lost Farm Menu - Last Call for Labor Day Load In | 2026-08-28 |
| `1a048aa81c7ce960` | awholdings.com | Ascend Updated Menu \| NEW STRAIN Snake Eyes + 1906 GO is Back! | 2026-08-28 |
| `1a0488b20c35d015` | budsgoods.com | Bud's Goods Menu - NEW BOGO DEAL, NEW GOODIES, 3.5G and 14G FLOWER!! | 2026-08-28 |
| `1a0487631fd438f6` | harvestmoonfarmsnj.com | 🔥 Friday Menu Update – Fan Favorites Are BACK! | 2026-08-28 |
| `1a048ed225cf7db7` | arescanna.com | Sun Menu - Labor Day SALE | 2026-08-28 |
| `1a048f310f85ef5b` | arescanna.com | Woodstock Menu - Labor Day SALE | 2026-08-28 |
| `1a034379ff1e7fcc` | agri-kind.apextrading.com | GMO Pre-Rolls Are Bringing the Heat (Google Sheet menu link) | 2026-08-24 |
| `1a039367f8546123` | agri-kind.apextrading.com | Stock Up. Get Rewarded. Up to 8 FREE Cases of Pre-Rolls. (Google Sheet menu link) | 2026-08-25 |

Other same-domain threads in the inbox were left alone: most lacked an explicit
menu/price-sheet signal (product-launch or promo blasts without "menu"/"price
sheet"/"drop" + attachment), and several explicit "Menu" threads (a QCC NJ menu, a
second Ascend menu, a Garden Society past-due notice) carried the `IMPORTANT` label, or
were genuine 1:1 correspondence (the Ladds LLC "let's get together" thread with real
replies from Lemar) — all protected by the never-touch floor.

## PART B — Trash audit (recoverable in Gmail Trash for 30 days)

| Thread ID | Sender | Subject | Date |
|---|---|---|---|
| `198f27c67720ad91` | fromthetimes-noreply@nytimes.com | Avoiding ultraprocessed foods might double weight loss, study suggests | 2025-08-28 |
| `198f273bc6753956` | andrew@northlake.supply | Get Nimbus Carts and Live Resin for a Lower Price! | 2025-08-28 |
| `198f23668cb57fa6` | stella@cannacontent.co | Here's Why Discount-Based Marketing Strategies Don't Work | 2025-08-28 |
| `198f137ea0b35db6` | email@em.sherwin-williams.com | (( Blue Bucket Sale )) Did somebody say FINAL HOURS? | 2025-08-28 |
| `198f105c79c956f4` | make-events@make.com | Last chance: Waves '25 Early Bird ⏰ | 2025-08-28 |
| `198f067d297b99f7` | Francisco@high-grass-farms.apextrading.com | All-in-one Vapes now shipping | 2025-08-28 |

The last two are vendor-seed-list domains (`northlake.supply`, an `apextrading.com`
subdomain) — per the runbook, their >12-month-old marketing is trashable even though
PART A separately archives their *recent* menus; neither is on the NEVER-TOUCH allowlist.

**Skipped** (never-trash floor): 10 threads from `CTA@sos.nj.gov` (2025-05 through
2025-08-26, `*.gov` allowlist); a Dutchie implementation-survey thread (IMPORTANT reply
present); a Hamilton Farms wholesale-menu thread that turned into a real payment-terms
negotiation with a prospective buyer (IMPORTANT, genuine correspondence); an ICCC
"mini-MBA" program thread (IMPORTANT).

## Report-only: old `category:updates` (never auto-trashed)

~201 threads older than 12 months sit in `category:updates`. Sample sender domains
surfaced for manual review, not touched: `headset.io` (scheduled report emails, already
allowlisted), `messaging.squareup.com` (paid/received invoice notifications），
`jotformsign.com` / `jotform.com` (signed-document + approval notifications),
`voice-noreply@google.com` (Google Voice missed-call/voicemail alerts), `nytimes.com`,
`mcafee.com`, `order.eventbrite.com`, `e1.theathletic.com`. Financial/operational
notices (Square invoices, Jotform approvals) are mixed in here — left untouched per the
report-only rule; Lemar can clear by hand if he wants to.

## Cap
Per-run cap (200 trashed/run) not reached — only 6 threads met all trash criteria this run.

## Sources
- gmail: see thread IDs above (account lemar@cuzziesnj.com)
