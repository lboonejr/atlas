---
created: 2026-07-10T18:45-04:00
updated: 2026-07-10T18:45-04:00
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
  updated_label: "July 10, 2026"

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
  - id: little-leaf-labs
    label: "Little Leaf Labs — lab testing"
    amount: 8331
    tier: 1
    vendor: "Little Leaf Labs"
    account: "INV-0000762 + INV-0000889 · 91+ days"
    contact: "Dhruvi, Accounting"
    status: past-due
    note: "Cannabis vendor, but gates sellable tested product → Tier 1."
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
    amount: null
    tier: 2
    vendor: "Leafly"
    account: "~2 weeks past due as of 7/5"
    contact: "256-488-4697"
    status: tbd
    note: "Amount TBD — set when confirmed."

# ---- TIER 3 — Competitive edge (restore / advantage) ----
  - id: intercompany-loan
    label: "Intercompany inventory loan — repay"
    amount: 40000
    tier: 3
    vendor: "Related entity"
    status: owed
    note: "Related-entity repayment; goodwill/creditworthiness."
  - id: epli-reinstate
    label: "EPLI (Berkley Select) — reinstate"
    amount: 4051.12
    tier: 3
    vendor: "Berkley Select via First Insurance Funding"
    account: "Loan #105889646"
    contact: "Andrew Giampaolo, Marshall & Sterling · (845) 454-0800 x2397"
    status: lapsed
    note: "Decided 7/6 to let lapse; restore as coverage edge on reopen."
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

## Snapshot (human-readable, as of 2026-07-10)
- **Tier 1 (open & operate):** ≈ **$75,121** one-time (incl. $50K inventory restock).
- **Tier 2 (nice-to-have):** ≈ **$22,804** (+ Leafly TBD).
- **Tier 3 (edge):** ≈ **$44,051** (intercompany loan $40K + EPLI $4,051; strategic lines TBD).
- **Tax gate (separate):** ≈ **$109,900**.
- **Monthly carry:** ≈ **$31,200/mo** → runway = (investment − one-time) ÷ 31,200.
- Reality check: opening ($75K) + a 3-month cushion (~$93.6K carry) ≈ **$169K** before Tier 2/3 and before tax.

## Sources
- slack: #on-button `C0BEQUW5NPP` — the running drop feed; canvas `F0BEN1167GB`.
- Prior brief [[2026-07-10-cuzzies-reopening-plan]] and the per-vendor notes in `20-Cuzzies/`.
- Rendered by: `on-button-reopen.html` (repo root, via githack) — regenerated by the `on-button-plan` skill.
