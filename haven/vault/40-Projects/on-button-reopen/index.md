---
created: 2026-07-10T18:45-04:00
updated: 2026-09-11T16:15:00-04:00
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
  updated_label: "August 14, 2026 (Dutchie POS reactivation added)"

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
    amount: 2842.83
    tier: 1
    vendor: "ADT"
    account: "405075455 · due 8/4/2026 (supersedes prior $1,637.84 90-days-past-due statement)"
    contact: "(833) 320-1859"
    status: past-due
    note: "Lemar confirmed 7/15 (#decisions, ts 1784128401.635159) this $2,842.83 statement is the current balance on the same account — tracked line updated."
  - id: nst
    label: "National Secure Transport — cash pickup"
    amount: 868.60
    tier: 1
    vendor: "National Secure Transport"
    account: "7-invoice batch · oldest due 05/26"
    contact: "(800) 696-1934"
    status: past-due
    note: "Verified 7/11 against the 7-invoice PDF (F0BGNFR1WLR) — invoices sum to exactly $868.60, no change. New 'Friendly Reminder' emailed 7/17 requests payment by July 21, 2026; amount unchanged at $868.60. Posted to #on-button per Lemar's ask in #decisions (ts 1784319361.170599)."
  - id: pseg
    label: "PSE&G — electric"
    amount: 1051.51
    tier: 1
    vendor: "PSE&G"
    account: "2764 Mt Ephraim Ave · acct 7804704100"
    contact: "1-800-357-2262"
    status: past-due
    note: "Escalated 7/22 — automated reminder says 3 payments past due, was $391.58, now $1,051.51. Service-continuity warning in the notice; nothing paid or contacted."
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
  - id: dutchie-reactivation
    label: "Dutchie — POS reactivation"
    amount: null
    tier: 1
    vendor: "Dutchie"
    account: "balance unknown — Lemar to ask Dutchie directly on reach-out"
    contact: "Dutchie support"
    status: tbd
    note: "Added 2026-08-14 from Lemar's #on-button reactivation plan: reach out to let
           Dutchie know Cuzzie's is turning back on, ask for the current balance, update
           the payment method + user settings at reactivation. POS is required to sell
           product, so this is Tier 1 even though the dollar figure is still unknown —
           do not guess it. Separately (not a dollar line): Lemar also wants a loyalty
           contract + app scoped, and a Dutchie-driven marketing push (text/email to the
           existing customer list, graphics TBD) once reactivated — tracked narratively
           in the Update below, not as its own tier item."
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
    note: "SIN830881 (due 7/16) amount still TBD — add when it lands.
           Plan added 2026-08-14 (#on-button): once reopening, set up a NEW Weedmaps
           account rather than reactivate this one — tell the rep a new ownership group
           has taken over, fewer pins this time, more centralized toward Camden. This
           $6,583 arrears line stays tracked as-is (old account's debt); the new account
           is a separate, not-yet-priced Tier 2/3 line once Lemar names a figure."
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
  - id: northlake-supply
    label: "Northlake Supply — Invoice #1803"
    amount: 2232.09
    tier: 2
    vendor: "Northlake Supply"
    account: "Invoice #1803 (North_-1803), originally due 1/28/2026, now 224 days late"
    contact: "Dan Saita (co-founder) · dan@northlake.supply · (973) 298-4027"
    status: past-due
    note: "Added 2026-09-11 per Lemar's ask (Convo 1, thread ts 1788980988.376489) to keep
           the on-button board current. Lemar told Dan 5/27 this would be paid in full by
           6/1 once the funding event closed — that payment never landed anywhere in the
           vault. Dan followed up again 9/9, offered a call, wants to close it out.
           Nothing paid or contacted by Samira. Haven:
           haven/vault/20-Cuzzies/2026-09-09-northlake-invoice-1803-overdue.md"

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
    amount: 4617.92
    tier: 2
    vendor: "Glass Meadows"
    account: "Invoice #2425, due 5/24/2026, now 90+ days — QuickBooks statement #7442, 9/11"
    contact: "900 Haddon Ave Ste 100, Collingswood NJ · (609) 417-5553"
    status: past-due
    note: "Resolved from TBD 2026-09-11: statement #7442 (9/11 email) confirms $4,617.92, invoice #2425, aged into the 90+ days bucket. See also haven/vault/20-Cuzzies/2026-07-10-glass-meadows-statement-5791.md (same underlying invoice, prior statement number)."
  - id: chew-and-chill
    label: "Chew & Chill / PanCann"
    amount: null
    tier: 2
    vendor: "Chew & Chill / PanCann"
    status: tbd
    note: "Past due, full payment demanded 6/22 — amount not stated."
  - id: dime-industries
    label: "Dime Industries"
    amount: 8869.99
    tier: 2
    vendor: "Dime Industries"
    account: "Acct #2026-2289"
    contact: "CannaBIZ Collects (Mike Ganges) · mike@cannabizcollects.com · (312) 536-6845"
    status: collections
    note: "Resolved from TBD 2026-09-11: CannaBIZ Collects (same agency chasing Little Leaf
           Labs) sent a new collections notice 9/9 for a different creditor — Dime
           Industries LLC, $8,869.99. Offering payment plan, settlement, asset
           liquidation, product return, or an offset against Cuzzie's own uncollected
           receivables; warns of 'expedited legal review' if ignored. Nothing paid, no
           reply sent, no call made — awaiting Lemar's read on how to engage. Haven:
           haven/vault/20-Cuzzies/2026-09-09-dime-industries-cannabiz-collections.md"
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
  - id: loud-labs
    label: "Loud Labs (Pyramid / Doinks / Zoobies / Rejuv)"
    amount: null
    tier: 2
    vendor: "Loud Labs"
    account: "Invoice PSI0001634"
    contact: "Aaron Greene (Dir. Ops) aaron@loudlabs.co · Jake Berry (CEO) jake@loudlabs.co"
    status: tbd
    note: "Same wind-down vendor-debt pattern as Bud's Goods/Sun Extractions/QCC. Past-due, following up on payment status (8/7) — amount not stated in the 7/10 or 8/7 emails, TBD. Per Lemar's ask in the #decisions email card, 8/9. Haven: haven/vault/20-Cuzzies/2026-08-07-loud-labs-payment-followup.md"
  - id: fresh-grow
    label: "Fresh Grow"
    amount: 3262.06
    tier: 2
    vendor: "Fresh Grow (freshcannabis.co)"
    contact: "Kathy@freshcannabis.co"
    status: past-due
    note: "Open wholesale balance, $3,262.06 confirmed by Lemar 7/15 (no invoice/statement email found). 7/15: Samira sent Kathy a draft reply (unsent, in Gmail Drafts) noting Cuzzie's temporary closure and that the balance hasn't been forgotten."
  - id: primo-brands-readyrefresh
    label: "Primo Brands (Ready Refresh) — water/coffee delivery"
    amount: 129.94
    tier: 2
    vendor: "Primo Brands / Ready Refresh"
    account: "Acct 6710233346 · final notice before collections"
    contact: "1-800-274-5282"
    status: past-due
    note: "Logged 7/15 per Lemar's in-thread ask (#decisions ts 1784136181.354949). Small balance, not a reopen blocker — pay-or-lapse call still open in #decisions."
  - id: aiq
    label: "AIQ — SaaS subscription"
    amount: 2481.51
    tier: 2
    vendor: "AIQ (billed via Chargify)"
    account: "Invoice 68388, issued 7/17"
    contact: "ar@aiq.com"
    status: past-due
    note: "New invoice 7/17, no due date stated. Lemar asked in-thread (#decisions ts 1784305562.237219, replied \"throw this into the #on-button channel so we can take care of that upon returning\") to track it here. Not a reopen blocker — pay-or-lapse call still open in #decisions.
           RESOLVED 2026-08-14 (#on-button): Lemar's call — let it go to collections,
           negotiate the collections price, then pay it down. NOT going back to Alpine
           for loyalty. Only exception he'd consider: paying enough to regain access to
           the existing customer data. Status stays past-due/collections-track, not
           pay-or-lapse; not paid or contacted by Samira."

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
  - id: progressive
    label: "Progressive Commercial — auto/liability (letting lapse)"
    amount: 1107.20
    tier: 3
    vendor: "Progressive Commercial"
    account: "Policy #997268390 (cancelled 7/3/26)"
    contact: "progressivecommercial.com"
    status: lapsed
    note: "Moved Tier 1 → Tier 3 (2026-08-01): Lemar decided 2026-07-27 in #decisions to let this lapse rather than pay — same 7/2 #decisions call that paired this with epli-reinstate above (ts 1783026740.943679). Balance reconciled to $1,107.20, the actual cancellation-confirmation amount owed; supersedes the old $2,117.80 pre-cancellation reinstatement-quote figure, which no longer applies since the policy is confirmed cancelled effective 7/3. Escalated to a collections-threat 'final notice' 7/27, repeated 7/30 — no dispute sent, no payment made, tracking only. Restore/reinstate coverage only if decided later; not a reopen blocker. A repeat automated notice landed again 8/9, cross-referenced 8/14 to this same tracked line — no change, no new action.
           2026-09-11: the collections agency chasing this balance (Caine & Weiner, on behalf of Progressive) has emailed twice (9/2, 9/9) asking for a callback — same $1,107.20, ref file 26085261. Samira drafted a reply proposing a call time (Gmail Drafts, unsent). Lemar's 9/9 in-thread reply: told them Cuzzie's is being sold and the debt would be paid by the new owners; plans to stall further, then likely put it on a payment plan. No figure change, no payment made — tracked here, not acted on beyond the draft."
  - id: first-insurance-funding-notice
    label: "First Insurance Funding — loan #106241219 (separate policy from epli-reinstate)"
    amount: 477.60
    tier: 3
    vendor: "First Insurance Funding"
    account: "Loan #106241219 · final balance after return-premium credits applied"
    contact: "Abraham Borjon, Collections Rep · abraham.borjon@firstinsurancefunding.com"
    status: past-due
    note: "Confirmed separate policy from epli-reinstate 7/12, included in totals at $4,699.76
           (past due $3,040.95 + installment $1,658.81) at the time. RESOLVED lower
           2026-09-11: Abraham Borjon confirmed the return-premium credits for the
           cancelled Palomar policies (property + GL, cancelled 6/5) matched the
           cancellation invoices — that closes out the bulk of the old $4,699.76 figure,
           leaving a final uncovered remainder of $477.60 on this same loan. No further
           premium is coming; if unpaid it goes to 3rd-party collections (+25% fee).
           Lemar asked (9/10) whether it can go on a payment plan instead of a lump sum —
           Samira drafted that ask to Abraham (cc Jordan Mulero), sitting unsent in Gmail
           Drafts. `amount` updated 4699.76 → 477.60 to reflect the current, final
           balance on this loan (not a duplicate/new line). Nothing paid.
           Haven: haven/vault/20-Cuzzies/2026-09-09-first-insurance-funding-loan-balance-477.md"
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

## Snapshot (human-readable, as of 2026-08-09)
- **Tier 1 (open & operate):** ≈ **$106,537.20** one-time (incl. $50K inventory restock, $40K
  intercompany loan repay; ADT reconciled to $2,842.83, was $1,637.84; PSE&G escalated to
  $1,051.51, was $391.58; Progressive Commercial ($2,117.80) moved out to Tier 3 8/1 — see
  below).
- **Tier 2 (nice-to-have):** ≈ **$115,411.45** priced (Leafly escalated to collections 7/14,
  $653.30 — was $279; Fresh Grow priced 7/15 at $3,262.06 — was TBD; Primo Brands/Ready
  Refresh $129.94 added 7/15; AIQ $2,481.51 added 7/17; 9 cannabis-vendor lines still TBD,
  incl. new Loud Labs added 8/9). **Stale — see 9/11 updates below**, several TBD lines have
  since priced and Northlake Supply was added; use the 9/11 updates for current totals.
- **Tier 3 (edge):** ≈ **$18,188.96** priced (Little Leaf Labs $8,331 + EPLI $4,051.12 +
  First Insurance Funding loan #106241219 $4,699.76, confirmed 7/12 as a separate policy,
  not a duplicate + Progressive Commercial $1,107.20, moved in 8/1; strategic lines TBD).
  **Stale — see 9/11 update below**, First Insurance Funding loan #106241219 has since
  been resolved down to $477.60.
- **Tax gate (separate):** ≈ **$109,900**.
- **Monthly carry:** ≈ **$31,200/mo** → runway = (investment − one-time) ÷ 31,200.
- Reality check: opening (~$104.4K) + a 3-month cushion (~$93.6K carry) ≈ **$198K** before
  Tier 2/3 and before tax. Tier 2 fully funding now runs materially higher (~$109.2K+) once
  the cannabis-vendor arrears are included.

## Update — 2026-09-11 (Dime Industries priced, Northlake Supply added, First Insurance Funding loan reconciled down)
Lemar asked twice in Convo 1 (thread ts `1788988028.299219` "Waste Management — AP trying
to reach you" and thread ts `1788980976.011509` "Dime Industries collections —
$8,869.99") to make sure this board carries current past-due numbers. Three changes:
1. **Dime Industries** (`dime-industries`) resolved from TBD: CannaBIZ Collects sent a new
   collections notice 9/9 for a different creditor than Little Leaf Labs — acct
   #2026-2289, **$8,869.99**. `amount` null → 8869.99, `status` tbd → collections. Tier 2
   TBD count drops by one. Haven:
   `haven/vault/20-Cuzzies/2026-09-09-dime-industries-cannabiz-collections.md`
2. **Northlake Supply** (`northlake-supply`) added as a new Tier 2 line: Invoice #1803,
   **$2,232.09**, now 224 days late — Lemar had promised Dan Saita full payment by 6/1
   once the funding event closed, which never happened; Dan followed up again 9/9. Haven:
   `haven/vault/20-Cuzzies/2026-09-09-northlake-invoice-1803-overdue.md`
3. **First Insurance Funding loan #106241219** (`first-insurance-funding-notice`)
   resolved LOWER, not duplicated: Abraham Borjon confirmed 9/9 the return-premium
   credits for the cancelled Palomar policies matched the cancellation invoices, leaving
   a final uncovered remainder of **$477.60** on this same loan (was $4,699.76,
   confirmed 7/12). `amount` 4699.76 → 477.60. Nothing paid — Lemar has asked about a
   payment-plan option, drafted, unsent. Haven:
   `haven/vault/20-Cuzzies/2026-09-09-first-insurance-funding-loan-balance-477.md`
4. Checked but **no change made**: Waste Management (new AP-contact-request notice
   carries no dollar figure — left the existing $320.56/mo carry line as-is, did not
   invent a past-due figure; `haven/vault/20-Cuzzies/2026-09-09-waste-management-ap-contact-request.md`)
   and the Progressive/Caine & Weiner collections thread (same already-tracked $1,107.20
   `progressive` line — note appended there with the 9/11 collections-agency contact and
   Lemar's "selling the business, new owners pay it" stance, no figure change).

Net effect: Tier 2 priced total +$11,102.08 (Dime Industries $8,869.99 newly priced +
Northlake Supply $2,232.09 new line); Tier 3 priced total −$4,222.16 (First Insurance
Funding loan reconciled down). Page (`on-button-reopen.html`) and canvas (`F0BEN1167GB`)
regenerated from this note in the same pass. Nothing paid or contacted by Samira.

## Update — 2026-09-11 (full reconciliation pass — page was missing 18 cannabis-vendor arrears items)
Lemar picked Option 1 on the #fixes card raised earlier this pass (`C0BV5BRNH5Z:1789136462.053309`,
reply "Let's go with option one"): full reconciliation of `on-button-reopen.html`'s
`reopen-data` tier-items block against this index. The drift was much larger than the
single `glass-meadows-vendor` line flagged below — the entire "Cannabis vendor arrears"
batch (18 items: `cannabist-company`, `verano`, `sun-extractions`, `green-lightning`,
`prolific-growhouse`, `happy-farmer`, `cookies-harrison`, `hillview-med`,
`garden-society`, `curaleaf-vendor`, `glass-meadows-vendor`, `chew-and-chill`,
`dime-industries`, `hamilton-farms`, `ganja-manja`, `lovegrow-vendor`, `niche-llc`,
`fresh-grow`) was present here but absent from the page's `reopen-data` block — it had
never been added when that batch first landed 2026-07-11. Added all 18 to the page,
verified item-for-item (id set now matches exactly, 47/47). `meta.updated` set to
"September 11, 2026 (full reconciliation — 18 cannabis-vendor arrears lines added)".
**Left alone per Lemar's pick (did not choose Option 2):** the page's separate
`repay.vendors` JSON block (net/profit/margin/units/brands per vendor) — a different,
undocumented data structure this skill does not own; still unexplained who maintains it.
Canvas `F0BEN1167GB` not refreshed — `canvas_access.writable` is still `false` per the
last check (2026-09-06) and today's first-run recheck already happened this morning;
carrying the known gap rather than re-attempting a write already established as blocked.
Nothing paid or contacted.

## Update — 2026-09-11 (Glass Meadows priced)
Email-loop drop (Gmail, QuickBooks statement #7442 from Glass Meadows, 2026-09-11
14:02 ET): Cuzzie's invoice #2425 (originally due 5/24/2026) is **$4,617.92**,
now aged into the 90+ days bucket. Resolves the `glass-meadows-vendor` line from
TBD — dedupe-checked against the existing 7/10/7/17 Glass Meadows notes first
(same underlying invoice/vendor, no duplicate created). `amount` null → 4617.92,
`status` tbd → past-due. Tier 2 TBD cannabis/vendor-arrears count drops by one.

**Not regenerated this pass:** `on-button-reopen.html`'s separate vendor-analysis
JSON block (a different data structure than the `reopen-data` tier-items block
this skill owns — net/profit/margin per vendor) already carries its own
`glass-meadows` entry with `amount: null`, and a check found the `reopen-data`
block itself has no `glass-meadows-vendor` entry at all — the page has been out
of sync with this index on several TBD lines for longer than this one update.
Flagging as a known drift rather than partially patching one line while the
broader reconciliation is still open; full page regeneration deferred to a
dedicated pass. Canvas not refreshed for the same reason. Nothing paid or
contacted — tracking only.

## Update — 2026-08-14 (accounting/bookkeeping staffing note — narrative only)
New #on-button drop, ts `1786714257.383289` (after the 6-item batch logged in the entry
below): Lemar — "For accounting/bookkeeping I'll definitely see what the Claude MCP
features can do to help me with that but also suggest Julio that does the stations'
bookkeeping." Two threads to track, neither dollar-denominated and neither a vendor/tier
item:
1. Lemar is evaluating whether Claude/MCP tooling can help run Cuzzie's reopening
   bookkeeping directly.
2. He's considering bringing in **Julio** — The Station (Newark)'s existing bookkeeper —
   to also handle Cuzzie's books once reopened, rather than (or alongside) the currently
   tracked GreenBooks CPA carry line (`Accounting — GreenBooks`, $1,600/mo in the carry
   table above).
No figure or decision yet — logged narratively for the reopening-plan record; not added
as a tier item (nothing payable) and doesn't change the carry table until Lemar decides
whether Julio replaces or supplements GreenBooks. Page/canvas not regenerated (no
rendered data changed). Nothing contacted.

## Update — 2026-08-14 (Dutchie item added; Weedmaps/AIQ resolution plans; CRC/license/terminals logged narratively)
Swept #on-button, 6 new drops since the 8/13 ~6:20pm checkpoint (all genuine — none
🧹📌📊-tagged restatements), all part of Lemar dictating the reopening operations plan:

1. **Dutchie POS reactivation** (ts `1786663918.745879`, edited) — new Tier 1 item
   `dutchie-reactivation` added above: reach out that Cuzzie's is turning back on, ask
   for the current balance (unknown — not guessed, `amount: null`), update payment
   method + user settings at reactivation. Also wants a loyalty contract/app scoped and
   a Dutchie-driven marketing push (text + email to the existing customer list, graphics
   TBD) once live — tracked here narratively, not as a priced line since nothing is
   dollar-denominated yet.
2. **Debit card terminals** (ts `1786663975.759959`) — consolidate down to one company
   (possibly Kartiq's), or let the buyer pick a new terminal company if they'd rather;
   return all current terminals either way; whichever terminals end up in use must route
   to **the buyer's bank account**. Not added as a tier item (no dollar figure, and the
   "buyer's bank account" framing means this is part of the ownership-transition
   handoff, not Lemar's own reopen spend) — logged here for the record.
3. **City business license** (ts `1786664672.239019`) — renewal due ~October; Lemar wants
   to (a) confirm the renewal fee doesn't need paying / set aside time in September if it
   does, (b) have a tax plan in place by then, (c) check whether the city needs to be
   told about the ownership change separately from the CRC change-of-ownership vote.
   No dollar figure given — not added as a tier item; flagged here as a compliance
   to-do, not tracked as a payable yet.
4. **Alpine IQ (AIQ)** (ts `1786664761.933849`) — resolution plan folded into the
   existing `aiq` item's note above (let it go to collections, negotiate, pay down; no
   loyalty renewal; possible exception to regain customer-data access).
5. **New Weedmaps account** (ts `1786707952.226469`) — plan folded into the existing
   `weedmaps` item's note above (new account under new ownership, fewer/more-centralized
   Camden pins, old $6,583 arrears line untouched).
6. **CRC (NJ Cannabis Regulatory Commission)** (ts `1786710578.804169`) — inform them
   Cuzzie's is reopening, ask what's required, badge any new employees, and be ready to
   navigate whatever the CRC raises about the reopening. No dollar figure, no tier —
   logged here as the compliance thread to track; ties into the change-of-ownership
   question in item 3 above and the existing Jamone's-group transition-timeline work
   (`haven/vault/00-Inbox/2026-08-10-jamones-group-lease-transition-timeline.md`).

Nothing paid or contacted by Samira on any of these six. Page (`on-button-reopen.html`)
and canvas (`F0BEN1167GB`) regenerated from this note in the same pass.

## Update — 2026-08-09 (Loud Labs added)
Swept #on-button ts `1786277901.262699` — a new drop (not a restatement, no 🧹📌📊 tag):
**Loud Labs** (Pyramid / Doinks / Zoobies / Rejuv brands), the same wind-down vendor-debt
pattern as Bud's Goods/Sun Extractions/QCC, per Lemar's ask in the #decisions email card
8/9. Contact: Aaron Greene (Director of Operations) aaron@loudlabs.co · Jake Berry (CEO)
jake@loudlabs.co. Status: past-due, following up on payment status (8/7) against original
invoice PSI0001634. **Amount not stated in either the 7/10 or 8/7 email — flagged `tbd`
rather than guessed.** Checked for an existing entry first (this run's other PARTs, A and
D, were noted as having independently posted the same vendor drop to #on-button) — no prior
`loud-labs` id existed in this index, so added as a new Tier 2 cannabis-vendor-arrears line
(`loud-labs`), dedupe-safe against any later restatement of the same drop. Tier 2 TBD count
8 → 9. Nothing paid or contacted — tracking only. Page (`on-button-reopen.html`) and canvas
(`F0BEN1167GB`) regenerated from this note in the same pass. Haven source:
`haven/vault/20-Cuzzies/2026-08-07-loud-labs-payment-followup.md`.

## Update — 2026-08-01 (Progressive Commercial reclassified Tier 1 → Tier 3, balance reconciled)
Swept #on-button ts `1785164745.763099` (2026-07-27, Samira's own report of the "let it
lapse" call — no 🧹📌📊 tag, not a numbered restatement, carries a figure not yet in this
index, so treated as a drop per the scanner rule): Progressive Commercial's balance is
confirmed **$1,107.20** (the actual amount owed per the 7/4 cancellation-confirmation email
and the 7/27 "final notice"/collections-threat email, repeated 7/30 — see
`haven/vault/20-Cuzzies/2026-07-04-progressive-commercial-canceled-confirmed.md`), not the
$2,117.80 previously tracked (that figure was the pre-cancellation cost to *keep the policy
active*, now moot since the policy is confirmed cancelled effective 7/3). Lemar's call in
#decisions 2026-07-27 (ts `1785154909.161039`): let it lapse — no dispute, no payment.
`progressive` item updated: `amount` 2117.80 → 1107.20, `status` past-due → lapsed, and
**moved Tier 1 → Tier 3** to match the treatment of `epli-reinstate` — the same pairing from
the original 7/2 #decisions call (ts `1783026740.943679`) that decided both policies would
lapse rather than be paid, so neither is a reopen blocker; both sit in Tier 3 as coverage
that could be restored later. Tier 1 total $108,655 → **≈$106,537.20** (−$2,117.80); Tier 3
total $17,081.76 → **≈$18,188.96** (+$1,107.20). Nothing paid or contacted — tracking only.
Page (`on-button-reopen.html`) and canvas (`F0BEN1167GB`) regenerated from this note in the
same pass.

## Update — 2026-07-31 (dedupe confirmed on flagged ADT/AIQ drops; canvas resync blocked)
Swept the two #on-button items flagged for this run: Lemar's "ADT updated Balance -
$2842.83" (ts `1784556454.923039`) and the Samira-bot AIQ routing message (invoice 68388,
$2,481.51, issued 7/17, ts `1784308668.895359`). Per the scanner/dedupe rule, checked both
against this index: **ADT** already carries `amount: 2842.83` (reconciled 7/15 per Lemar's
confirmation, reconfirmed 7/20 — ts `1784556454.923039` is exactly the restatement already
logged in the "2026-07-20 (ADT reconfirmed)" entry below) and **AIQ** already exists as its
own Tier 2 item (`aiq`, added 7/17, same invoice 68388, same $2,481.51, same "handle upon
returning" routing). No yaml changes were needed — both figures were already correct.
Cross-checked the rendered `on-button-reopen.html` JSON payload directly (not just this
note) and confirmed it already carries `adt: 2842.83` (Tier 1) and the full `aiq` line
(Tier 2, $2,481.51) with `meta.updated` still reading "July 22, 2026 (PSE&G escalated)" —
page regeneration was not needed.

While verifying, found the pinned canvas `F0BEN1167GB`'s file metadata shows its last real
edit at 2026-07-15 17:13 ET (`edit_timestamp` 1784142539) — before the 7/17 AIQ addition and
the 7/22 PSE&G escalation ($391.58 → $1,051.51) — so the canvas is stale on those two
points (missing the AIQ line entirely, showing the old PSE&G figure). Attempted a full
canvas rebuild from this note's current state (precedented by the 2026-07-09 canvas-cleanup
note — "Samira rebuilds this each scan" is the canvas's own stated behavior), but every
`slack_update_canvas` call this run — full-document replace, section replace, and
`insert_after` — returned a `restricted_action` API error regardless of parameters. Canvas
writes appear blocked in this session; the refresh could not be completed. Flagging for a
follow-up pass once canvas-write access is confirmed working — no #decisions ask needed,
this is a tooling gap, not a business decision. Nothing paid or contacted; no figures
changed this run.

## Update — 2026-07-22 (PSE&G escalated)
PSE&G sent a new past-due reminder for the Camden account (2764 Mt Ephraim Ave, acct
7804704100) — now **3 payments past due**, minimum payment needed **$1,051.51** (was
$391.58 previously tracked). Same account/address already on file, no address mismatch
(this is the correct utility account for the Cuzzie's Camden property, distinct from the
2750 Mt Ephraim Ave lease-street-number). `pseg` item updated: `amount` 391.58 → 1051.51,
note appended. Tier 1 total $107,995 → **≈$108,655** (+$659.93). Nothing paid or
contacted. Page (`on-button-reopen.html`) and canvas (`F0BEN1167GB`) regenerated from
this note in the same pass. Haven: `haven/vault/20-Cuzzies/2026-07-22-pseg-electric-past-due-escalation.md`.

## Update — 2026-07-20 (ADT reconfirmed)
Lemar posted "ADT updated Balance - $2842.83" in #on-button (ts `1784556454.923039`) — this
matches the already-tracked `adt` figure exactly (no change from the 7/15 reconciliation).
Per the scanner/dedupe rule this is a restatement of an existing line, not a new drop —
`amount` and `status` unchanged. Logged as a confirmation only; page and canvas not
regenerated (no data changed). Nothing paid or contacted.

## Update — 2026-07-17 (NST reminder)
National Secure Transport emailed a "Friendly Reminder: Outstanding Invoice(s)" 7/17 —
open balance **$868.60**, unchanged, now with a concrete ask: pay by **July 21, 2026**.
Lemar reacted ✅ in #decisions on the card (ts `1784319361.170599`) and asked in-thread
"Can you make sure that this gets added to the #on-button channel?" `nst` item note
updated to record the new due-date ask; amount and Tier 1 status unchanged (already
tracked). Posted to #on-button as a drop per the scanner rule (restatement of an
already-tracked item, not a new line). Nothing paid or contacted — pay-by-7/21 decision
remains open in #decisions. Page (`on-button-reopen.html`) and canvas (`F0BEN1167GB`)
regenerated from this note in the same pass. Haven:
`haven/vault/20-Cuzzies/2026-07-17-national-secure-transport-invoice.md`.

## Update — 2026-07-17 (AIQ)
Added **AIQ** (`aiq`) as a new Tier 2 line — SaaS subscription billed via Chargify, invoice
68388, **$2,481.51**, issued 7/17, no due date stated. Lemar asked in-thread (#decisions
ts `1784305562.237219`, ✅ reaction + reply "I think we need to throw this into the
#on-button channel so we can take care of that upon returning") to route it here. Posted
to #on-button as a drop and ingested per the scanner rule. Tier 2 total $112,929.94 →
**≈$115,411.45** (+$2,481.51). Nothing paid or contacted — pay-or-lapse decision remains
open in #decisions. Page (`on-button-reopen.html`) and canvas (`F0BEN1167GB`) regenerated
from this note in the same pass. Haven: `haven/vault/20-Cuzzies/2026-07-17-aiq-invoice-68388.md`.

## Update — 2026-07-15 (Primo Brands / Ready Refresh)
Added **Primo Brands (Ready Refresh)** (`primo-brands-readyrefresh`) as a new Tier 2 line —
water/coffee delivery, account 6710233346, **$129.94** past due, final notice before
collections. Lemar asked in-thread (#decisions ts `1784136181.354949`, replied "Can we
make sure that this gets logged on the #on-button?") to track it here. Small balance, not
a reopen blocker. Tier 2 total $112,800 → **≈$112,929.94** (+$129.94). Nothing paid or
contacted — pay-or-lapse decision remains open in #decisions. Page (`on-button-reopen.html`)
and canvas (`F0BEN1167GB`) regenerated from this note in the same pass. Haven:
`haven/vault/20-Cuzzies/2026-07-15-primo-brands-readyrefresh-overdue.md`.

## Update — 2026-07-15 (ADT reconciliation)
Lemar confirmed in-thread (#decisions ts `1784128401.635159`, replied "Yes can you update
the tracked line?") that the new **ADT** statement ($2,842.83, due 8/4/2026) supersedes the
prior $1,637.84 90-days-past-due figure on the same account (405075455). `adt` item
updated: `amount` 1637.84 → 2842.83, account/note updated. Tier 1 total $106,790 →
**≈$107,995** (+$1,204.99). Nothing paid or contacted. Page (`on-button-reopen.html`) and
canvas (`F0BEN1167GB`) regenerated from this note in the same pass.

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
