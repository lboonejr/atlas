---
created: 2026-07-10T18:45-04:00
updated: 2026-07-15T11:34-04:00
domain: project
type: reference
status: active
tags: [on-button, reopening, reopen-plan, index, samira]
source: claude
---

# On-Button Reopen — plan index (source of truth)

This note is the **machine-readable source of truth** for the Cuzzie's reopening plan.
It follows the [[investor-pipeline]] `index.md` precedent: one structured block that the
`on-button-plan` skill reads and regenerates downstream surfaces from. **The interactive
page `on-button-reopen.html` (served via githack) and the Slack canvas `F0BEN1167GB` are
both rendered FROM this block — edit numbers here, never on the page or the canvas.**
The page has a client-side **tier-shuffle** (a what-if that lives only in that browser); its
"Apply to plan →" button emits a `Samira, ... apply these tier moves` instruction — running
`on-button-plan` on it writes the moves back HERE, which is what makes them durable.

Mission: reopen Cuzzie's (Camden) within **14 days of funds landing**, then plan the rest
of the year. Every reopening element is sorted into three tiers so any investment amount
maps to a concrete reopening path:

- **Tier 1 — Bare bones:** must-pay to legally open and operate.
- **Tier 2 — Nice-to-have:** clear as funds allow.
- **Tier 3 — Competitive edge:** restore or build advantage.

Two things are held **outside** the tiers:
- **Tax gate** — NJ sales + Camden local cannabis tax (~$110K). Trust-fund taxes owed
  regardless of cash position; an open balance is a CRC license risk. Tracked on its own
  (voluntary-disclosure + payment plan), never funded by the allocator.
- **Monthly carry** (~$31,200/mo, bare-bones crew) — the denominator for runway. **Rent
  and payroll live here, not in the one-time reopen bucket**, so they are never
  double-counted. Runway (months) = (investment − one-time spend) ÷ monthly carry.

Guardrail: tracking & planning only — nothing is paid or contacted automatically.

## Editing rules (for the `on-button-plan` skill and for Lemar)
- Change amounts, tiers, or statuses **only inside the `plan` block below**, then touch
  `updated` and let `on-button-plan` regenerate the page + canvas. Amounts are plain
  numbers (no `$` or commas). `amount: null` = a genuinely unknown figure (renders as TBD).
- New drop lands in #on-button → add or update the matching item (dedupe by `id`) → do
  NOT create a duplicate. Superseded figures: keep the latest value only.
- `tier`: `1` | `2` | `3` for allocatable one-time items · `gate` for tax · `carry` for
  monthly lines (kept here for the carry table; the constant is the headline).

## The plan

```yaml
constants:
  monthly_carry: 31200          # bare-bones crew; excludes cannabis tax
  target_open_days: 14
  updated_label: "July 14, 2026"

tax_gate:
  - id: nj-sales-tax
    label: "NJ state sales tax (6.625%)"
    amount: 84400
    note: "~$84.4K on ~$1.14M sales; back periods appear unfiled — VDA + payment plan"
  - id: camden-local-tax
    label: "Camden local cannabis tax (2%)"
    amount: 25500
    note: "owed regardless of cash position (trust-fund tax)"

# ---- TIER 1 — Bare bones (must-pay to open & operate) ----
items:
  - id: gusto-payroll-tax
    label: "Gusto — payroll tax remittance"
    amount: 9739.85
    tier: 1
    vendor: "Gusto"
    account: "5 payrolls behind; tax principal only (excl. IRS/NJ penalties+interest)"
    contact: "Gusto support / accountant"
    status: past-due
  - id: progressive
    label: "Progressive Commercial — auto/liability"
    amount: 2117.80
    tier: 1
    vendor: "Progressive Commercial"
    account: "Policy #997268390"
    contact: "progressivecommercial.com"
    status: past-due
    note: "One-time reinstatement; ongoing ~$1,400/mo re-quote sits in monthly carry."
  - id: parke-bank
    label: "Parke Bank — clear negative balance"
    amount: 2000
    tier: 1
    vendor: "Parke Bank"
    account: "Acct ending 8046"
    contact: "Christopher Cabezas, AVP · (856) 582-6900 x142"
    status: past-due
  - id: adt
    label: "ADT Security"
    amount: 1637.84
    tier: 1
    vendor: "ADT"
    account: "405075455 · 90 days past due"
    contact: "(833) 320-1859"
    status: past-due
  - id: nst
    label: "National Secure Transport — cash pickup"
    amount: 868.60
    tier: 1
    vendor: "National Secure Transport"
    account: "7-invoice batch · oldest due 05/26"
    contact: "(800) 696-1934"
    status: past-due
    note: "Verified 7/11 against the 7-invoice PDF (F0BGNFR1WLR) — invoices sum to exactly $868.60, no change."
  - id: pseg
    label: "PSE&G — electric"
    amount: 391.58
    tier: 1
    vendor: "PSE&G"
    account: "2764 Mt Ephraim Ave · acct 7804704100"
    contact: "1-800-357-2262"
    status: past-due
  - id: google-workspace
    label: "Google Workspace / Voice"
    amount: 33.97
    tier: 1
    vendor: "Google"
    account: "Payments profile 1078-7383-2495 · bounced 7/8"
    contact: "Google Payments"
    status: past-due
  - id: intercompany-loan
    label: "Intercompany inventory loan — repay"
    amount: 40000
    tier: 1
    vendor: "Related entity"
    status: owed
    note: "Related-entity repayment; goodwill/creditworthiness. Moved Tier 3 → Tier 1 per Lemar's 7/10 tier-shuffle instruction (#on-button ts 1783738175.999559)."
  - id: inventory-restock
    label: "Cannabis inventory restock"
    amount: 50000
    tier: 1
    vendor: "Multiple licensed cultivators/wholesalers"
    contact: "—"
    status: target
    note: "Working target ('if we can'). Product to actually sell — largest single Tier 1 line."

# ---- TIER 2 — Nice-to-have (as funds allow) ----
  - id: arod-marketing
    label: "Arod — marketing services"
    amount: 7500
    tier: 2
    vendor: "Arod"
    status: past-due
  - id: weedmaps
    label: "Weedmaps — menu listing"
    amount: 6583
    tier: 2
    vendor: "Weedmaps (Ghost Mgmt)"
    account: "5-invoice batch · 58 days"
    contact: "Emma Donaldson, AR"
    status: past-due
    note: "SIN830881 (due 7/16) amount still TBD — add when it lands."
  - id: loan-nicky
    label: "Loan from Nicky (personal)"
    amount: 4000
    tier: 2
    vendor: "Nicky"
    status: owed
  - id: regus-iwg
    label: "Regus / IWG — Mt Laurel office"
    amount: 2451.80
    tier: 2
    vendor: "Regus / IWG"
    account: "Acct #16605480 · in collections"
    contact: "America's Debt Collection · (469) 257-3503"
    status: collections
    note: "Settle-to-close; office being vacated."
  - id: buds-goods
    label: "Bud's Goods of NJ"
    amount: 1512.10
    tier: 2
    vendor: "Bud's Goods of NJ"
    account: "INV-0000153 · 69 days"
    contact: "mzaidi@budsgoods.com"
    status: past-due
  - id: ambotte
    label: "Ambotte Mechanical"
    amount: 431.83
    tier: 2
    vendor: "Ambotte Mechanical"
    account: "Invoice #76732"
    contact: "Stephanie Rodriguez · srodriguez@ambotte.com"
    status: past-due
  - id: cintas
    label: "Cintas — uniforms"
    amount: 225.95
    tier: 2
    vendor: "Cintas"
    account: "Payer #0027585065 · 4 invoices"
    contact: "mycintas.com"
    status: past-due
  - id: apple-dev
    label: "Apple Developer — restore"
    amount: 99
    tier: 2
    vendor: "Apple"
    contact: "Apple Developer portal"
    status: past-due
  - id: leafly
    label: "Leafly — menu listing"
    amount: 653.30
    tier: 2
    vendor: "Leafly"
    account: "Invoice INV00389006 ($279, billing period 7/6–7/7) — Collections Case #00155715"
    contact: "256-488-4697"
    status: collections
    note: "Escalated to collections 7/14 (Case #00155715, $653.30 — unconfirmed if accumulated balance or separate invoice vs. the $279 logged 7/10). Lemar's call 7/14: let the collections referral proceed under the existing 7/5 hold-until-reopen stance; tracked here per his request, nothing paid/contacted."

# ---- Cannabis vendor arrears — from 7/11 Gmail sweep digest (#on-button ts 1783801467.428439) ----
  - id: cannabist-company
    label: "The Cannabist Company"
    amount: 26382.21
    tier: 2
    vendor: "The Cannabist Company"
    account: "7 invoices, oldest 7/23/25 · statement 6/30"
    contact: "AR@cannabistcompany.com"
    status: past-due
  - id: verano
    label: "Verano"
    amount: 18557.04
    tier: 2
    vendor: "Verano"
    account: "Statement 6/4 ($21,183.12 incl. 2 new orders, less $1,358.37 payment)"
    contact: "Vladimir Jovanovic"
    status: past-due
  - id: sun-extractions
    label: "Sun Extractions"
    amount: 11534.46
    tier: 2
    vendor: "Sun Extractions"
    account: "Majority 90+ days"
    status: past-due
    note: "Payment plan accepted 5/26; first payment never landed (followed up 6/11)."
  - id: green-lightning
    label: "Green Lightning Cultivation"
    amount: 9339.35
    tier: 2
    vendor: "Green Lightning Cultivation"
    status: past-due
    note: "Escalating; last contact 6/22."
  - id: prolific-growhouse
    label: "Prolific Growhouse"
    amount: 6144.63
    tier: 2
    vendor: "Prolific Growhouse"
    account: "#2735 $1,966.40 + #2881 $4,178.23"
    status: past-due
    note: "10% discount offer → $5,530.17 if paid in full. Last chase 7/4."
  - id: happy-farmer
    label: "The Happy Farmer"
    amount: 5487.60
    tier: 2
    vendor: "The Happy Farmer"
    account: "Invoice 1686, due 2/24/26"
    status: past-due
  - id: cookies-harrison
    label: "Cookies Harrison"
    amount: 4384.08
    tier: 2
    vendor: "Cookies Harrison"
    account: "Invoice 001"
    contact: "Allan Fries"
    status: past-due
  - id: hillview-med
    label: "Hillview Med"
    amount: 2532.00
    tier: 2
    vendor: "Hillview Med"
    account: "Invoice #754, as of 5/20"
    status: past-due
  - id: garden-society
    label: "The Garden Society"
    amount: 1720.00
    tier: 2
    vendor: "The Garden Society"
    account: "INV-0000048, due 5/18"
    status: past-due
    note: "Chased 6/23."
  - id: curaleaf-vendor
    label: "Curaleaf — vendor account"
    amount: null
    tier: 2
    vendor: "Curaleaf"
    account: "Recurring statement CNJ2-000241 (latest 7/4, also 6/17, 6/4, 5/19, 5/5)"
    status: tbd
    note: "Balance is on a PDF attachment, not stated in the email body — amount TBD until read."
  - id: glass-meadows-vendor
    label: "Glass Meadows — vendor account"
    amount: null
    tier: 2
    vendor: "Glass Meadows"
    account: "Weekly QuickBooks statements (latest 7/10); incl. INV 2425"
    status: tbd
    note: "See also haven/vault/20-Cuzzies/2026-07-10-glass-meadows-statement-5791.md — amount TBD here pending consolidation."
  - id: chew-and-chill
    label: "Chew & Chill / PanCann"
    amount: null
    tier: 2
    vendor: "Chew & Chill / PanCann"
    status: tbd
    note: "Past due, full payment demanded 6/22 — amount not stated."
  - id: dime-industries
    label: "Dime Industries"
    amount: null
    tier: 2
    vendor: "Dime Industries"
    status: tbd
    note: "Open invoices listed in a 5/11 email — amount TBD."
  - id: hamilton-farms
    label: "Hamilton Farms"
    amount: null
    tier: 2
    vendor: "Hamilton Farms"
    status: tbd
    note: "Payment plan proposed ($1K start) 5/5 — outstanding balance TBD."
  - id: ganja-manja
    label: "Ganja Manja"
    amount: null
    tier: 2
    vendor: "Ganja Manja"
    status: tbd
    note: "Aging balance; threatened collections as of 4/28 — amount TBD."
  - id: lovegrow-vendor
    label: "Lovegrow — vendor account"
    amount: null
    tier: 2
    vendor: "Lovegrow"
    status: tbd
    note: "Open balance, payments stopped; chased again 6/29 — amount TBD."
  - id: niche-llc
    label: "Niche, LLC"
    amount: null
    tier: 2
    vendor: "Niche, LLC"
    account: "Statement 6/5"
    status: tbd
  - id: fresh-grow
    label: "Fresh Grow"
    amount: 3262.06
    tier: 2
    vendor: "Fresh Grow (freshcannabis.co)"
    contact: "Kathy@freshcannabis.co"
    status: past-due
    note: "Open wholesale balance, $3,262.06 confirmed by Lemar 7/15 (no invoice/statement email found). 7/15: Samira sent Kathy a draft reply (unsent, in Gmail Drafts) noting Cuzzie's temporary closure and that the balance hasn't been forgotten."

# ---- TIER 3 — Competitive edge (restore / advantage) ----
  - id: little-leaf-labs
    label: "Little Leaf Labs — lab testing"
    amount: 8331
    tier: 3
    vendor: "Little Leaf Labs"
    account: "INV-0000762 + INV-0000889 · 91+ days"
    contact: "Dhruvi, Accounting"
    status: past-due
    note: "Cannabis vendor. Moved Tier 1 → Tier 3 per Lemar's 7/10 tier-shuffle instruction (#on-button ts 1783738175.999559)."
  - id: epli-reinstate
    label: "EPLI (Berkley Select) — reinstate"
    amount: 4051.12
    tier: 3
    vendor: "Berkley Select via First Insurance Funding"
    account: "Loan #105889646"
    contact: "Andrew Giampaolo, Marshall & Sterling · (845) 454-0800 x2397"
    status: lapsed
    note: "Decided 7/6 to let lapse; restore as coverage edge on reopen."
  - id: first-insurance-funding-notice
    label: "First Insurance Funding — loan #106241219 (separate policy from epli-reinstate)"
    amount: 4699.76
    tier: 3
    vendor: "First Insurance Funding"
    account: "Loan #106241219 · past due $3,040.95 + current installment $1,658.81"
    status: past-due
    note: "From #on-button drop 7/9 (Notices.pdf, F0BG52EUSKD, no message text). Lemar confirmed 7/12 (#decisions, Option B) this is a SEPARATE insurance line financed through the same lender as epli-reinstate (#105889646) — not the same policy, not a duplicate. Tracked as its own Tier 3 line, added to snapshot math."
  - id: marketing-relaunch
    label: "Reopening marketing relaunch (promo budget)"
    amount: null
    tier: 3
    status: tbd
    note: "Set a target when decided."
  - id: full-staffing
    label: "Full staffing restore (beyond bare crew)"
    amount: null
    tier: 3
    status: tbd
    note: "Incremental monthly, not one-time — model separately."
  - id: delivery-expansion
    label: "Delivery / extended-hours expansion"
    amount: null
    tier: 3
    status: tbd
  - id: loyalty-app
    label: "Loyalty / app / branding"
    amount: null
    tier: 3
    status: tbd

# ---- Monthly carry lines (reference for the carry table; sum ≈ constants.monthly_carry) ----
carry:
  - {label: "Payroll — you + Josh + 1 employee (bare-bones)", amount: 7900}
  - {label: "Rent — Harrison Acquisitions (all-in, incl. NNN)", amount: 8467}
  - {label: "Marketing (budgeted)", amount: 2500}
  - {label: "Dutchie POS", amount: 2160}
  - {label: "Insurance — General/Product Liability", amount: 2026}
  - {label: "Accounting — GreenBooks", amount: 1600}
  - {label: "Car insurance — 2 cars (re-quote)", amount: 1400}
  - {label: "Workers' comp", amount: 1118}
  - {label: "Gas & maintenance (2 delivery cars)", amount: 700}
  - {label: "Cash deposit — National Secure Transport", amount: 520}
  - {label: "Gusto payroll software", amount: 500}
  - {label: "Parke Bank service charge", amount: 500}
  - {label: "Phone — T-Mobile, 6 lines", amount: 457}
  - {label: "PSE&G electric/gas (operating est.)", amount: 400}
  - {label: "Waste Management", amount: 320.56}
  - {label: "Comcast Business Internet", amount: 267.74}
  - {label: "QuickBooks", amount: 151}
  - {label: "METRC compliance", amount: 40}
  - {label: "Google Workspace (5 seats)", amount: 42}
  - {label: "Google Voice", amount: 34}
  - {label: "Veriscan ID verification", amount: 30}
```

## Snapshot (human-readable, as of 2026-07-15 late morning)
- **Tier 1 (open & operate):** ≈ **$106,790** one-time (incl. $50K inventory restock, $40K
  intercompany loan repay).
- **Tier 2 (nice-to-have):** ≈ **$112,800** (Leafly escalated to collections 7/14, $653.30 —
  was $279; Fresh Grow priced 7/15 at $3,262.06 — was TBD; 8 cannabis-vendor lines still TBD).
- **Tier 3 (edge):** ≈ **$17,081.76** priced (Little Leaf Labs $8,331 + EPLI $4,051.12 +
  First Insurance Funding loan #106241219 $4,699.76, confirmed 7/12 as a separate policy,
  not a duplicate; strategic lines TBD).
- **Tax gate (separate):** ≈ **$109,900**.
- **Monthly carry:** ≈ **$31,200/mo** → runway = (investment − one-time) ÷ 31,200.
- Reality check: opening ($106.8K) + a 3-month cushion (~$93.6K carry) ≈ **$200K** before
  Tier 2/3 and before tax. Tier 2 fully funding now runs materially higher (~$109.2K+) once
  the cannabis-vendor arrears are included.

## Update — 2026-07-15 (afternoon)
Lemar confirmed the **Fresh Grow** balance: **$3,262.06**. `fresh-grow` item updated:
`amount` null → 3262.06, `status` tbd → past-due. Tier 2 total 109,538 → **≈$112,800**
(+$3,262.06), TBD cannabis-vendor count 9 → 8. Page (`on-button-reopen.html`) and canvas
(`F0BEN1167GB`) regenerated from this note in the same pass.

## Update — 2026-07-15
Added **Fresh Grow** (`fresh-grow`, freshcannabis.co, contact Kathy@freshcannabis.co) as a
new Tier 2 cannabis-vendor arrears line, `amount: null` — no invoice or statement email was
found for them, only recurring wholesale menu blasts, so the balance is TBD until Lemar or
a vendor statement supplies it. Context: earlier 7/15, Samira saved (unsent) a Gmail draft
reply to Kathy letting her know Cuzzie's is temporarily closed, that reopening is the
priority, and that the balance hasn't been forgotten (Haven:
`haven/vault/00-Inbox/2026-07-15-fresh-grow-closure-balance-draft.md`). Tier 2 TBD count
9 → the dollar total is unchanged since the new line has no figure yet. Page
(`on-button-reopen.html`) and canvas (`F0BEN1167GB`) regenerated from this note in the
same pass.

## Update — 2026-07-14
Leafly (`leafly`) escalated to collections: Leafly Support emailed Joshua 7/14 3:46pm ET
(Case #00155715), account being transferred to their Collections team, **$653.30** — bigger
than the $279.00 invoice (INV00389006) priced 7/10; unconfirmed whether it's an accumulated
balance or a separate figure. Raised as a #decisions parent (ts `1784060033.368559`); Lemar
reacted ✅ + 🫡 and asked in-thread to make sure it's tracked here. `leafly` item updated:
`amount` 279 → 653.30, `status` past-due → collections, note appended. Tier 2 snapshot total
recalculated (+$374.30 → **$109,538**). Nothing paid or contacted — Lemar's 7/5 "hold until
reopen" stance stands; the collections referral proceeds under that hold. Page
(`on-button-reopen.html`) and canvas (`F0BEN1167GB`) regenerated from this note in the same
pass. Haven: `haven/vault/20-Cuzzies/2026-07-05-leafly-missed-payment.md`.

### Prior — Update 2026-07-12 (evening)
Lemar answered the #decisions ask (Option B, reacted on the parent, ts `1783876542.732339`):
the First Insurance Funding notice (loan #106241219, $4,699.76) is a **separate insurance
line** financed through the same lender as `epli-reinstate` (#105889646), not a duplicate
statement on that policy. `first-insurance-funding-notice` status moved `tbd-confirm` →
`past-due`, label updated to drop "UNCONFIRMED", and its $4,699.76 is now included in the
Tier 3 snapshot total (was $12,382, now **$17,081.76**). Page (`on-button-reopen.html`) and
canvas (`F0BEN1167GB`) regenerated from this note in the same pass.

### Prior — Update 2026-07-12 (afternoon)
Ingested from a full #on-button re-sweep (2026-07-02 → 2026-07-11 window):
1. **Leafly — priced.** The 7/10 "email pull" drop (#on-button ts `1783719691.083309`)
   named invoice INV00389006, $279, billing period 7/6–7/7 — resolves the prior TBD.
2. **First Insurance Funding notice — flagged, NOT merged.** `Notices.pdf` (`F0BG52EUSKD`,
   dropped 7/9, no message text) shows loan #106241219, past due $3,040.95 + current
   installment $1,658.81 = **$4,699.76 total**, insurance cancelled. This loan number does
   not match the tracked `epli-reinstate` line (#105889646, $4,051.12) and the total is
   ~$650 higher. Added as a new `tbd-confirm` item, excluded from Tier 3 totals to avoid
   double-counting, and raised as ONE #decisions parent (never guessing which policy this
   is or folding the figures together).
3. **Everything else re-checked and confirmed already accurate, no changes:** the 7/11
   cannabis-vendor arrears digest, NST 7-invoice total, Waste Management, Comcast, Google
   Workspace, Gusto payroll-tax detail, Regus/IWG $2,451.80, and the NJ sales-tax gate
   figures all matched what's already in this note — restatements/reactions (🧹📌📊,
   numbered recaps) correctly ignored per the scanner rule. Progressive Commercial's
   7/3 cancel date has passed with no confirming message either way — left as-is
   (`status: past-due`), not escalated again since no new figure exists to act on.
Page (`on-button-reopen.html`) and canvas (`F0BEN1167GB`) regenerated from this note in
the same pass.

### Prior — Update 2026-07-11 (evening)
Ingested two #on-button drops:
1. **National Secure Transport 7-invoice PDF** (`F0BGNFR1WLR`) — verified against the
   existing `nst` line; the 7 invoices sum to exactly $868.60, matching what was already
   tracked. No change, note added confirming the verification.
2. **"Cannabis Vendor — Open Balances & Account Statements" digest** (#on-button ts
   `1783801467.428439`, a 90-day Gmail sweep) — added 9 new priced Tier 2 lines
   (Cannabist Company $26,382.21, Verano $18,557.04, Sun Extractions $11,534.46, Green
   Lightning $9,339.35, Prolific Growhouse $6,144.63, Happy Farmer $5,487.60, Cookies
   Harrison $4,384.08, Hillview Med $2,532.00, Garden Society $1,720.00) and 8 new TBD
   Tier 2 lines whose balance is on an attachment or not stated in the body (Curaleaf,
   Glass Meadows, Chew & Chill/PanCann, Dime Industries, Hamilton Farms, Ganja Manja,
   Lovegrow, Niche LLC). Little Leaf Labs and Bud's Goods were already tracked — no
   duplicate created, figures matched. Nothing paid or contacted — tracking only.
   Tier 2 snapshot total recalculated above. Page (`on-button-reopen.html`) and canvas
   (`F0BEN1167GB`) regenerated from this note in the same pass.

### Prior — Update 2026-07-11 (morning)
Applied Lemar's tier-move instruction (#on-button `C0BEQUW5NPP`, ts `1783738175.999559`,
posted 2026-07-10 22:49:35 ET, unreacted): **Little Leaf Labs — lab testing** moved
Tier 1 → Tier 3; **Intercompany inventory loan — repay** moved Tier 3 → Tier 1.

## Sources
- slack: #on-button `C0BEQUW5NPP` — the running drop feed; canvas `F0BEN1167GB`; cannabis
  vendor digest ts `1783801467.428439`; NST PDF `F0BGNFR1WLR`.
- Prior brief [[2026-07-10-cuzzies-reopening-plan]] and the per-vendor notes in `20-Cuzzies/`.
- Rendered by: `on-button-reopen.html` (repo root, via githack) — regenerated by the `on-button-plan` skill.