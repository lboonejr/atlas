---
created: 2026-09-17T23:07:00-04:00
updated: 2026-09-17T23:07:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-09-17 (LIVE, DRY_RUN=false)

Nightly Gmail cleanup on `lemar@cuzziesnj.com`. Mode: **LIVE** (`DRY_RUN=false`).
Archived 7 vendor menus to the `Vendor Menus` label, trashed 5 old promotional/
social/forum threads (>12 months old), left 201 old `category:updates` threads
untouched (report-only per the runbook — mixes invoices/bank/payroll with ads,
too dangerous to sweep).

## PART A — vendor menus archived (label `Vendor Menus` / `Label_8`, removed from INBOX)

1. Thread `1a0ab8eefe66d92d` — "Fresh Grow Menu | New DICE AIOs + Strain Restocks" — Kathy@freshcannabis.co — 2026-09-16
2. Thread `1a0aad985490527c` — "Brute's Roots Menu - Happy NECANN eve! Old Pal 14g Flower Available!" — chelsey.shindler@brutesroots.com — 2026-09-16
3. Thread `1a0aaa02ded15f13` — "QCC NJ Menu 9.16.26 - Fresh Fall Restocks & Added Value" — kbreiner@qccnj.com — 2026-09-16
4. Thread `1a0aa71ba3850c07` — "Updated Ascend Menu | Last Call for Delivery Before the Weekend & NECANN!" — nbonsanto@awholdings.com — 2026-09-16
5. Thread `1a0a0789a746e88b` — "Brute's Roots Menu - Old Pal is Back on Market! Stock up on your Faves!" — chelsey.shindler@brutesroots.com — 2026-09-14
6. Thread `1a09fd6d9312717c` — "Hillview Menu <> NEW DROPS <> GMO Rootbeer 38.52% <>Super Runtz 32% <> KALO 5MG THC BEVERAGES" — jaime@hillviewmed.com — 2026-09-14
7. Thread `1a0a1c791bafa229` — "Cuzzie's Dispensary x Hamilton Farms - Menu Updated" — wholesale@hamiltonfarms.com / amoyer@hamiltonfarms.com (2 vendor-only messages, no reply from Lemar) — 2026-09-14/15

Skipped as weak/ambiguous menu signals (left alone, precision over recall): several
vendor-domain + attachment matches that were genuine 1:1 correspondence — invoices, AR
statements, past-due/collections notices, and active negotiation threads — rather than
bulk menu blasts. Also skipped a "Monday Menu Drop" thread from laddsllc.com because it
was a real back-and-forth conversation with Lemar, not a marketing blast.

## PART B — trash sweep audit (recoverable in Gmail Trash for 30 days)

Candidate set: `older_than:1y (category:promotions OR category:social OR
category:forums) -is:important -is:starred` → 28 candidates found; 5 qualified after
the full gate (not starred/important, sender domain not on the NEVER-TOUCH allowlist,
no protective label):

1. Thread `199543a1085c2a02` — "New Badders Dropped — Fuggedaboutit" — Jade@hearth-wellness-llc.apextrading.com — 2025-09-16
2. Thread `199539a061ee6bc0` — "Real rewards. Real results. No extra integrations required." — marketing@dutchie.com — 2025-09-16
3. Thread `1995340641a059c7` — "Customers like you count! Grainger wants to hear from you." — noreply@feedback.grainger.com — 2025-09-16
4. Thread `19952dbce9d85c4d` — "Don't miss our AI webinar" — marketing@engage.canva.com — 2025-09-16
5. Thread `1995203c5ac2d2c7` — "Reserve your spot for our Virtual Business Training Series Event..." — email@em.sherwin-williams.com — 2025-09-16

Skipped from the 28 candidates:
- **20 threads** — sender on the NEVER-TOUCH allowlist (12 from `CTA@sos.nj.gov` under
  the `*.gov` rule, 8 from `parkebank@parkebank.com`).
- **3 threads** — carried at least one `is:important`-flagged message despite the
  query's exclusion (Gmail surfaces a whole thread if any one message matches): a
  Dutchie survey thread (`19644c6a0e498f47`), a Hamilton Farms thread that was actually
  a real order-terms conversation forwarded to a third party (`196110a96c91e798`), and
  an ICIC.org training-program thread (`1826944b41c19b7a`).

No threads hit the 200/run cap.

## PART B — report-only: `category:updates` (never auto-trashed)

201 old (`older_than:1y`) threads in `category:updates` in the inbox — left completely
untouched per the runbook (this category mixes invoices/bank/payroll/legal receipts
with ads, too dangerous to sweep). A sample of sender domains seen, for Lemar to clear
by hand if he wants: `jotform.com` / `jotformsign.com` (form + signature
notifications), `nytimes.com` (news alerts), `theathletic.com`, `redditmail.com`,
`distru.com`, `aiq.com`, `cannazipbags.com`, `rankreallyhigh.com`, `softtouchpos.com`,
`adtcontrol.com`.

## Counts

- Vendor menus archived: **7**
- Threads trashed: **5**
- Threads skipped (allowlist): **20**
- Threads skipped (important-flagged): **3**
- Old `category:updates` threads (report-only, untouched): **201**
- Per-run cap (200): not hit

## Recovery

Anything trashed sits in Gmail Trash for 30 days. Thread IDs above are the recovery
keys.

## Sources
- gmail: lemar@cuzziesnj.com inbox, PART A/B searches run 2026-09-17
