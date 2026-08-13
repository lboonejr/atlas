---
created: 2026-08-13T05:45-04:00
updated: 2026-08-13T05:45-04:00
domain: project
type: reference
status: active
tags: [off-button, wind-down, cuzzies, vendors, collections, index, samira]
source: claude
---

# Off Button — vendor wind-down ledger (source of truth)

This note is the **machine-readable source of truth** for Cuzzie's (Camden) vendor
wind-down. It follows the [[on-button-reopen]] and [[investor-pipeline]] `index.md`
precedent: one structured block that the `samira-off-button` skill reads, updates, and
regenerates the downstream surface from.

**The monday.com board "Off Button — Vendor Wind-Down & Payoff" (`18424191974`) is a
RENDERING of this block, not the truth.** This resolves the Monday cutover gate
(`anchors.md` — mirroring ended 2026-07-11, boards go read-only): the ledger now lives in
the vault, and the board is refreshed from it for as long as Lemar still looks at it.

Cuzzie's ceased operations **2026-06-13**. Every obligation is one entry below.
Guardrail: **tracking and negotiating-support only — nothing is ever paid, and no vendor
is ever contacted, automatically.**

## Scope
IN: Cuzzie's vendor payables, tax/government liabilities, bank/lender balances tied to
the wind-down, and any collections placement against them.

OUT (flag to Lemar, never auto-add): MCA / merchant-cash-advance obligations (Novus
Capital, Liquidibee / Elevate Funding, Nomas Recovery) and active litigation (DeWalt v.
Cuzzie's, CAM-L-1339-26). Lemar confirmed 2026-08-13 these stay off the ledger for now.

BORDERLINE: two entries belong to **The Station (Newark)**, not Cuzzie's — `primo-brands`
and `canopy-usa`. Kept for continuity; flagged, not resolved. If Off Button becomes
Cuzzie's-only, both move together.

## Editing rules (for the `samira-off-button` skill and for Lemar)
- Change data **only inside the `ledger` block below**, then touch `updated` and let the
  skill regenerate the board. Amounts are plain numbers — no `$`, no commas.
- **`amount: null` means genuinely unknown and MUST stay null.** Never guess, never
  substitute a partial figure that would understate exposure. When a figure exists only
  inside an unopened PDF, keep `null` and say where it lives in `blocked_on`.
- Dedupe by `id`. A new notice on an existing obligation UPDATES that entry — it never
  creates a second one.
- Superseded figures: keep the latest stated value only; the prior value belongs in
  `note` if the movement matters (e.g. a balance growing under fees).
- `correspondence` ∈ `waiting_on_us` | `waiting_on_them` | `not_yet_contacted` |
  `no_action_needed`. Set it from what actually happened, **including sent mail** — the
  most common error in this ledger's history was marking an item `waiting_on_us` when a
  reply had already gone out.
- `resolution` ∈ `negotiating` | `letting_lapse` | `in_collections` | `lapsed_settling` |
  `null`. Use `in_collections` only for a formal collections notice or third-party
  placement, and say in `note` which it is — a creditor's own in-house collections letter
  and an outside agency placement are different things.
- Corrections are explicit. If a prior entry was wrong, say so in `note`
  ("CORRECTION 8/13 — earlier entry said X; in fact Y"). Never silently rewrite history;
  git preserves every prior state.

## Migration note (v1, 2026-08-13)
This block was migrated from the monday.com board on 2026-08-13, carrying **current
state** for all 39 obligations. The long-form correspondence narratives still live in each
board item's Source Notes and in the Gmail threads referenced by `threads`. Subsequent
scans append here first.

```yaml
ledger:
  meta:
    entity: Cuzzie's Dispensary & Delivery LLC
    closed: 2026-06-13
    board_id: 18424191974
    last_scan: 2026-08-13
    scan_window_start: 2026-07-28

  # ---- CANNABIZ VENDORS (past due / open balance) ----
  items:
    - id: verano
      vendor: Verano
      category: cannabis
      group: cannabis
      amount: 21183.12
      last_notice: 2026-08-04
      correspondence: waiting_on_them
      resolution: negotiating
      contact: { name: Vladimir Jovanovic (AR), email: vladimir.jovanovic@verano.com, phone: "3232057432" }
      threads: [19fcdfab773968af]
      note: >
        6/4 statement $18,557.04 overdue plus new orders = $21,183.12 less a $1,358.37
        credit. 8/4/26 Vladimir warned of a credit hold; Lemar replied same day disclosing
        the closure. Waiting on Verano.

    - id: gti
      vendor: GTI (Green Thumb Industries)
      category: cannabis
      group: cannabis
      amount: 25625.00
      last_notice: 2026-06-16
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Mindy Kramer, AR Collections Lead, email: GTIAR@gtigrows.com, phone: "8158789054" }
      note: >
        Payment plan agreed 2/25/26, shifted to weekly in June, then stalled — GTI said no
        payments came through (6/11) and resent the statement 6/16 warning of collection
        agency referral. No reply since 6/16. One of the largest cannabis balances.

    - id: magic-garden
      vendor: Magic Garden Botanicals
      category: cannabis
      group: cannabis
      amount: 14272.54
      last_notice: 2026-04-06
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: M. Alvarez / O. Carrillo, email: Malvarez@magicgardenbotanicals.net }
      note: >
        Two invoices: #25-0000255 $3,817.46 and an earlier $10,455.08. Nothing after the
        4/6/26 automated notice — stale by 4+ months, confirm current status directly.

    - id: niche
      vendor: Niche, LLC
      category: cannabis
      group: cannabis
      amount: 10780.11
      last_notice: 2026-06-05
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Alap Desai (EVP Compliance) / Austin Moses, email: alap@nichenfe.com }
      note: >
        Brand Goodies. 6/5/26 QuickBooks statement, entirely 90+ day bucket. No collections
        correspondence since 1/16/26; recent Niche mail is marketing only, so the account
        may be quiet rather than resolved.

    - id: cannabist
      vendor: The Cannabist Company
      category: cannabis
      group: cannabis
      amount: 26382.21
      last_notice: 2026-07-31
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Chelsey Shindler / Matthew Velahos (AR), email: AR@cannabistcompany.com }
      note: >
        LARGEST single vendor balance. Oldest open invoice dates to 07/23/25. A $1,000/mo
        plus COD arrangement was agreed 4/13/26 and never kept — the balance has grown, not
        shrunk. Cannabist is winding down NJ ops (final-inventory emails 7/27 and 7/29).

    - id: high-grass
      vendor: High Grass Farms, LLC
      category: cannabis
      group: cannabis
      amount: 2528.88
      last_notice: 2026-07-27
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Jim Connelly, Director of Strategic Partnerships, email: jconnelly@hgfarmsnj.com }
      note: >
        Invoices High_G-918 ($1,810.70, climbing with fees) and High_G-440 ($718.18). Plan
        agreed 6/3/26 tied to a funding event, not honored; Lemar apologized 6/16. Automated
        reminders continue.

    - id: emunio
      vendor: Emunio Logistics, Inc
      category: cannabis
      group: cannabis
      amount: 2222.00
      last_notice: 2026-06-04
      correspondence: waiting_on_us
      resolution: negotiating
      collections_agency: null
      contact: { name: S. Berman / D. Kosovsky, email: sberman@emuniologistics.com, phone: "6102993714" }
      note: >
        CORRECTION 8/13/26 (per Lemar) — this entry previously carried CannaBIZ Collects and
        an in_collections status on the INFERENCE that the unattributed CannaBIZ demand was
        Emunio's. CannaBIZ is in fact collecting Little Leaf Labs' debt; that record moved to
        `little-leaf-labs`. No confirmed collections placement here. Balance unverified and
        stale since 12/3/25 — confirm directly before using in settlement math.

    - id: glass-meadows
      vendor: Glass Meadows Inc
      category: cannabis
      group: cannabis
      amount: 4617.92
      last_notice: 2026-07-27
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Accounting Team (C. Sloan / J. Muir / A. Skowron), email: accounting@glassmeadows.com }
      note: >
        Invoice 2425. Lemar disclosed the closure 6/22/26; Glass Meadows never acknowledged
        it and the daily automated reminders simply continued. No collections escalation seen.

    - id: buds-goods
      vendor: Bud's Goods of NJ Corp
      category: cannabis
      group: cannabis
      amount: 1512.10
      last_notice: 2026-08-07
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Mo Zaidi, email: mzaidi@budsgoods.com }
      threads: [19f47b030f4ddadf]
      note: >
        Invoice INV-0000153. Mo explicitly held off sending to collections as a favor
        (7/14/26) and has now checked in twice, most recently 8/7/26. Highest
        goodwill-preservation value per dollar on the ledger.

    - id: happy-farmer
      vendor: The Happy Farmer
      category: cannabis
      group: cannabis
      amount: 7109.40
      last_notice: 2026-05-26
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Justin Baldwin, email: justin@happyfarmernj.com }
      note: >
        Invoices #1505 ($1,621.80 remaining) and #1686 ($5,487.60). Justin agreed to a
        schedule twice; the payment never arrived and he went quiet after 5/26/26. Goodwill
        extended and not repaid — worth a direct update.

    - id: hamilton-farms
      vendor: Hamilton Farms
      category: cannabis
      group: cannabis
      amount: 2604.78
      last_notice: 2026-03-30
      correspondence: not_yet_contacted
      resolution: negotiating
      contact: { name: Wholesale / A. Moyer, email: sales@hamiltonfarms.com }
      note: >
        Invoice I-10070, climbing with fees. NO direct human contact has ever been made.
        Weekly wholesale marketing continues, so the relationship is intact.

    - id: green-lightning
      vendor: Green Lightning Cannabis
      category: cannabis
      group: cannabis
      amount: 9399.35
      last_notice: 2026-06-22
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Allen Livshits (Accounting) / Miles / Carl, email: accounting@greenlightningcannabis.com }
      note: >
        Three invoices (Green_-751, #97, #82). Longest chase history — reached "6th attempt"
        by 4/22/26. 6/22/26 a firmer contact (Miles) escalated; Lemar disclosed the closure
        same day. Silent since.

    - id: authorized-dealer
      vendor: Authorized Dealer, LLC
      category: cannabis
      group: cannabis
      amount: 2268.00
      last_notice: 2026-06-04
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Sheena Urciada (AR), email: AR@authorizeddealernj.com, phone: "6095968181" }
      note: >
        Invoice #0000117. GOOD track record — two prior invoices were confirmed paid in full
        (6/3/26). Relationship stayed warm (in-person meeting 6/10). One of the more
        resolvable items.

    - id: garden-society
      vendor: Garden Society NJ
      category: cannabis
      group: cannabis
      amount: 1720.00
      last_notice: 2026-07-31
      correspondence: waiting_on_them
      resolution: negotiating
      contact: { name: AR Team (Mary; cc Erin / Maggie), email: ar@thegardensociety.com }
      threads: [19ef5a3dac10b873, 19fa4d37e676e9da]
      note: >
        Invoice INV-0000048, unchanged since May. Lemar replied 7/31/26 (an earlier entry
        wrongly said no reply was sent). BANKING CHANGED effective 08/01/2026 — do not use
        pre-8/1 payment details. Open question — Kiva said NJ distribution moved from Garden
        Society to Victory Farms 7/1/26; confirm who is actually owed.

    - id: rove
      vendor: Rove (Victory Natural Farms LLC)
      category: cannabis
      group: cannabis
      amount: 760.00
      last_notice: null
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Daniel Barnett, AR Manager, email: danielb@rovebrand.com }
      threads: [19c2fac1d6ca1c92]
      note: >
        Balance per Lemar 8/3/26. $500/week plan agreed 1/2/26, stalled after 1/15/26.
        Smallest cannabis balance on the ledger; nothing new since February.

    - id: dime
      vendor: Dime Industries
      category: cannabis
      group: cannabis
      amount: 8869.99
      last_notice: 2026-08-03
      correspondence: waiting_on_them
      resolution: negotiating
      contact: { name: Marcel Carter, Manager (rep Michael Santos), email: marcel.c@dime.industries }
      threads: [19db6a33b48202eb, 19fc8b3eff8e16c0, 19e18df6caf3c859]
      note: >
        DI-NJ-SO-290 ($3,745.69) and DI-NJ-SO-385 ($5,124.30). Payment promised against the
        5/15 and 5/20 funding events, neither honored. 8/3/26 formal notice warned of HQ
        Collections referral; Lemar's reply went out the same day.

    - id: clade9
      vendor: Clade9 (via The QCC Group)
      category: cannabis
      group: cannabis
      amount: 3314.32
      last_notice: 2026-08-06
      correspondence: waiting_on_us
      resolution: in_collections
      collections_agency: The QCC Group (in-house, not a third-party agency)
      contact: { name: Jenna Arruda, Senior Accountant, email: jarruda@qccnj.com, phone: "8482608684" }
      threads: [19fd89beca2f106c]
      note: >
        ESCALATED 8/6/26 — formal collections notice from QCC for $3,314.32, an exact match
        to invoice #2825, confirming the previously unverified reference balance is real.
        GreenBooks (Zak) cc'd. QCC's own in-house collections, NOT an agency placement. QCC
        still sends weekly menus, so the relationship is not severed.

    - id: curaleaf-aga
      vendor: Curaleaf — AGA Adjustments Collections (CNJ2-000241)
      category: cannabis
      group: cannabis
      amount: 25601.41
      last_notice: 2026-08-03
      correspondence: waiting_on_us
      resolution: in_collections
      collections_agency: A.G. Adjustments, Ltd. (agent Michael Mintz)
      contact: { name: Michael Mintz, email: mail@agaltd.com }
      threads: [19fc961fdfa15928]
      note: >
        Third-party collections demand received 8/3/26, file 2532730_AGA. Standard 30-day
        dispute window closes ~9/2/26, after which AGA treats the debt as valid if undisputed.
        A holding reply is drafted in Gmail but NOT sent. No payment made or scheduled.

    - id: sun-extractions
      vendor: Sun Extractions
      category: cannabis
      group: cannabis
      amount: 11534.46
      last_notice: 2026-08-07
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Accounts Receivable, email: ar@sunextractions.com, phone: "6093220060" }
      threads: [19fddcbe635f85e5]
      note: >
        Invoices INV-0000551, INV-7000574, INV-0000591, INV-6000813; majority 90+ days.
        Vendor states repeated phone and email attempts got no response and warns formal
        collections will follow. No reply sent.

    - id: northlake
      vendor: Northlake Supply
      category: cannabis
      group: cannabis
      amount: 2232.09
      last_notice: 2026-08-10
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Dan Saita, Co-Founder / VP Sales & Marketing, email: dan@northlake.supply, phone: "9732984027" }
      threads: [19b6bc4a665e82d4]
      note: >
        Invoice North_-1803. Lemar committed to paying in full by 6/1/26 and did not.
        Closure disclosed 6/22. 8/10/26 Dan followed up again and OFFERED a payment schedule
        with no pressure applied — unusually accommodating.

    - id: loud-labs
      vendor: Loud Labs
      category: cannabis
      group: cannabis
      amount: null
      blocked_on: No dollar figure stated in either the 7/10 or 8/7 email
      last_notice: 2026-08-07
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Aaron Greene (Dir. Operations); orig. Jake Berry (CEO), email: aaron@loudlabs.co }
      threads: [19f4daa95127e89c]
      note: >
        Amount deliberately null — never stated by the vendor. Holding-reply draft saved,
        not sent. Haven note haven/vault/20-Cuzzies/2026-08-07-loud-labs-payment-followup.md.

    - id: little-leaf-labs
      vendor: Little Leaf Labs
      category: cannabis
      group: cannabis
      amount: 8331.00
      last_notice: 2026-08-13
      correspondence: waiting_on_us
      resolution: in_collections
      collections_agency: CannaBIZ Collects (mike@ / amy@cannabizcollects.com)
      contact: { name: Dhruvi (Accounting), cc Bronnie, email: Accounting@littleleaflabs.net }
      threads: [19ff518397e5b7be, 19ff96b7cfbd80e0]
      note: >
        ADDED 8/13/26. INV-0000762 ($3,175.00 remaining of $5,675.00) and INV-0000889
        ($5,156.00), both 91+ days. CHASED ON TWO FRONTS: CannaBIZ Collects demand letters
        (6/4 and 8/13, the second broadcast to five Cuzzie's addresses — escalation), plus
        the vendor's own reminders now at #12. Every reminder threatens collections AND
        notifying the state — that threat is unique to this vendor and material given the CRC
        license transition. The closure has NEVER been disclosed to Little Leaf Labs.

  # ---- NEGOTIATE (large balances) ----
    - id: progressive
      vendor: Progressive Commercial (Auto/Liability)
      category: non_cannabis
      group: negotiate
      amount: 1107.20
      last_notice: 2026-08-09
      correspondence: no_action_needed
      resolution: letting_lapse
      note: >
        Policy #997268390, cancelled 7/3/26. DECIDED — let it lapse, no payment or dispute
        (Lemar's call in #decisions). Transfers to a collections agency 08/14/2026; logged so
        the placement is expected rather than a surprise.

    - id: weedmaps
      vendor: Weedmaps
      category: non_cannabis
      group: negotiate
      amount: 6583.00
      last_notice: 2026-06-17
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Emma Donaldson (AR), email: agarcia@weedmaps.com }
      note: >
        5 invoices, 58 days past due as of 6/17. No self-serve portal. Check mailing address
        was updated per the 6/23 email.

    - id: nj-sales-tax
      vendor: NJ Sales Tax — State + Camden Local
      category: tax_government
      group: negotiate
      amount: 109900.00
      last_notice: 2026-07-10
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: GreenBooks CPA (Richard Wyse / Zak Hasanin) }
      threads: [19f7fdee27983645]
      note: >
        LARGEST liability on the ledger. ~$84.4K NJ state + ~$25.5K Camden local trust-fund
        tax on ~$1.14M sales. Q1 2026 filed without payment; 2025 Q2-Q4 appear unfiled.
        Exploring a Voluntary Disclosure Agreement plus installment plan. BLOCKED — GreenBooks
        flagged 7/31/26 that no activity is coded after Feb/Mar 2026, so VDA figures cannot be
        finalized; QuickBooks was reactivated 7/31. Also needs the ~$13.6K Jul/Aug 2025
        over-collection reconciled. Trust-fund tax = CRC license risk.

    - id: aiq
      vendor: AIQ
      category: non_cannabis
      group: negotiate
      amount: 2481.51
      last_notice: 2026-07-17
      correspondence: waiting_on_us
      resolution: negotiating
      threads: [19f70d2fa8a769e9]
      note: Invoice 68388. Lemar's call — handle upon returning.

    - id: arod-marketing
      vendor: Arod — Marketing Services
      category: non_cannabis
      group: negotiate
      amount: 7500.00
      last_notice: 2026-07-07
      correspondence: waiting_on_us
      resolution: negotiating
      blocked_on: No account, contact, or portal identified yet — needs a follow-up search
      note: Past-due marketing services. No contact reference found in any Gmail sweep to date.

    - id: gusto-payroll-tax
      vendor: Gusto — Payroll Tax Remittance (IRS/NJ)
      category: tax_government
      group: negotiate
      amount: 9739.85
      last_notice: 2026-08-11
      correspondence: not_yet_contacted
      resolution: negotiating
      threads: [19ff0a727ca28959]
      note: >
        Tax principal only (~$5,773 employee withholding + ~$3,966 employer share), 5
        biweekly payrolls behind; EXCLUDES IRS/NJ late-deposit penalties and interest. This is
        the "contact IRS, establish payment plan" item. STILL GROWING — payroll for Jul 26 -
        Aug 8 went unrun and was flagged late 8/11. Corrected 2025 W-2Cs also pending.

    - id: epli-berkley
      vendor: EPLI / Berkley Select (First Insurance Funding)
      category: non_cannabis
      group: negotiate
      amount: 14133.68
      last_notice: 2026-07-24
      correspondence: no_action_needed
      resolution: letting_lapse
      contact: { name: Cory Smith, First Insurance Funding, email: cory.smith@firstinsurancefunding.com, phone: "8475724642" }
      note: >
        Policy DEP-2335743-P1. DECIDED 7/6 — let lapse. Bring-current is $6,091.76; full
        payoff $14,133.68, up sharply from $4,051.12 on 6/23 since nothing has been paid.
        The growth confirms the lapse decision rather than reinstating.

    - id: parke-bank
      vendor: Parke Bank — Negative Balance
      category: non_cannabis
      group: negotiate
      amount: 2611.03
      last_notice: 2026-08-11
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Christopher Cabezas (ext. 142) / Meggan Hallworth, email: ccabezas@parkebank.com, phone: "8565826900" }
      threads: [19fcd0050dda065d, 19ff0bc747aa5051]
      note: >
        Cuzzie's own operating account, not a vendor. CONFIRMED 8/4/26 overdrawn $2,611.03
        and placed under LOCKOUT by senior management (prior entry carried an unverified
        $2,000 cap). The $500/mo service fee was deactivated 6/24 so it should stop growing.
        This account is the failure point behind several other entries — ACH returns are
        constant (NovusCapital II, Elevate Funding, Zapier, GoDaddy) and it is the declined
        payment method behind the Google balance.

  # ---- SELF-PAY (small balances) ----
    - id: ambotte
      vendor: Ambotte Mechanical
      category: non_cannabis
      group: self_pay
      amount: 431.83
      last_notice: null
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Stephanie Rodriguez, email: srodriguez@ambotte.com, phone: "8568488708" }
      note: Invoice #76732. No portal — contact accounting@ambotte.com.

    - id: waste-management
      vendor: Waste Management
      category: non_cannabis
      group: self_pay
      amount: 320.56
      last_notice: 2026-07-25
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { phone: "18662183220" }
      note: >
        Customer ID 32-81926-53003, 2750 Mount Ephraim Ave. Autopay bounced 7/10 and 7/13;
        formally "Payment Overdue" as of 7/25 — status changed from current to overdue.

    - id: primo-brands
      vendor: Primo Brands / ReadyRefresh (Water — Station)
      category: non_cannabis
      group: self_pay
      entity: the_station
      amount: 129.94
      last_notice: 2026-07-15
      correspondence: not_yet_contacted
      resolution: in_collections
      contact: { phone: "18002745282" }
      threads: [19f6676866a733a2]
      note: >
        THE STATION account (1245 Main St, Rahway), not Cuzzie's — flagged for scope.
        Account #6710233346. 7/15/26 notice states "extreme delinquency" — final notice
        before agency referral, threatens suspension and full replacement-value charges for
        bottles/equipment. Smallest balance on the ledger, disproportionate consequence.

    - id: first-insurance-loan
      vendor: First Insurance Funding — Loan #106241219
      category: non_cannabis
      group: self_pay
      amount: 452.60
      last_notice: 2026-08-03
      correspondence: not_yet_contacted
      resolution: null
      contact: { phone: "8008373707" }
      note: >
        Collection letter dated 8/3/26. Financed via Risk Strategies. Premiums $18,916.75
        less down payment, payments and return premiums = $452.60 due. States it is a
        debt-collection attempt; nonpayment may trigger legal action plus attorney fees.
        SEPARATE loan number from the EPLI/Berkley balance — same lender, different policy.

  # ---- NEW / UNCLASSIFIED ----
    - id: greenbooks-cpa
      vendor: GreenBooks CPA — Accounting Services
      category: non_cannabis
      group: unclassified
      amount: 7500.00
      last_notice: 2026-08-12
      correspondence: not_yet_contacted
      resolution: null
      contact: { name: Richard Wyse / Zak Hasanin (billed via Huljev CPA PLLC), email: billing@charitycpas.com }
      threads: [19ff195625635da7]
      note: >
        Invoice #6020, $1,250/mo x 6 (March-August 2026), due on receipt; reminder resent
        8/12. DISTINCT from the NJ Sales Tax item — this is GreenBooks' own fee, not the tax
        debt they are helping coordinate. Note the dependency: they are the path to the VDA.

    - id: adt
      vendor: ADT
      category: non_cannabis
      group: unclassified
      amount: 2842.83
      last_notice: 2026-08-09
      correspondence: not_yet_contacted
      resolution: null
      contact: { name: ADT Customer Service / Billing, phone: "8333260497" }
      threads: [19fe79a3a9a29946, 19fcd15705cbbf87]
      note: >
        Acct #405075455, 120 days past due. Monitoring rate INCREASES to $390.10/mo effective
        9/3/26 per the 8/4 rate-change notice — the balance grows unless the service is
        cancelled. No named rep exists; only automated senders.

    - id: leafly
      vendor: Leafly
      category: non_cannabis
      group: unclassified
      amount: 1281.60
      last_notice: 2026-08-12
      correspondence: waiting_on_us
      resolution: negotiating
      deadline: 2026-08-22
      contact: { name: Dante Coley (Market Manager), email: dante.coley@leafly.com }
      threads: [19fc1a42513c653f, 19ff345e5ac4ebfb, 19ff525477806979, 19fead80b56a07a5]
      note: >
        TIGHTEST DEADLINE ON THE LEDGER. Acct #A00020782, Case #00160771. 8/10 "at risk of
        termination", 8/12 00:01 collections transfer, 8/12 08:44 FINAL DEMAND giving 10 days
        (~8/22) before third-party collections, citing breach of contract and legal action.
        Unresolved tension: Lemar committed 8/3 to settling this in full pre-sale and
        cancellation is already approved, yet it is escalating.

    - id: google-workspace-voice
      vendor: Google Workspace + Google Voice (cuzziesnj.com)
      category: non_cannabis
      group: unclassified
      amount: null
      blocked_on: >
        Voice piece is ~$38.39 per Lemar; the Workspace figure is not stated in any email and
        must be read from admin.google.com > Billing > Payment accounts. Entering $38.39
        alone would understate exposure.
      last_notice: 2026-08-12
      correspondence: not_yet_contacted
      resolution: null
      threads: [19ff4fb03bd26214, 19fd1201e6e8efc0, 19f411600d1fc1cc, 19fc0d9d9f1f062e]
      note: >
        ADDED 8/13/26. Payments profile 1078-7383-2495. Two subscriptions: Voice Starter
        (suspended 7/13, cancellation pending) and Workspace. BILLING PARTY UNRESOLVED —
        Gusto IS an authorized Google Workspace reseller, so Workspace may sit on the monthly
        Gusto invoice while Voice is billed direct by Google; Google permits exactly that
        mixed arrangement, which would explain why only a Voice invoice exists. Settle it at
        Billing > Subscriptions, "Payment plan" column ("Reseller pricing" = reseller-billed).
        AUTOPAY IS DEAD REGARDLESS — the 7/8 debit was declined from Checking ****046, the
        locked-out Parke Bank account. Visa ****5577 was verified 7/7 and may be usable.
        OPERATIONAL PRIORITY beyond the dollars — this domain runs every cuzziesnj.com
        mailbox; suspension stops inbound mail and the wind-down trail goes dark.

    - id: canopy-usa
      vendor: Canopy USA / Acreage — The Station Newark (Acct 3105)
      category: cannabis
      group: unclassified
      entity: the_station
      amount: null
      blocked_on: Figure is inside attachment invoice-3105.pdf on the 8/6/26 email
      last_notice: 2026-08-12
      correspondence: waiting_on_us
      resolution: negotiating
      contact: { name: Terrence Guthrie, AR Specialist (cc Gary Pagano), email: Terrence.Guthrie@canopy-usa.com }
      threads: [19fd793b3fdbe929]
      note: >
        ADDED 8/13/26. THE STATION account, not Cuzzie's — Lemar confirmed 8/13 that
        invoice-3105.pdf is The Station's. Flagged for scope, kept alongside primo-brands.
        Terrence chased 8/6 and 8/12 and has escalated from email to phoning the store,
        requesting an update BY END OF WEEK. Tone still cooperative, no collections threat.
        Primary recipient is Markony Monteiro; Lemar is cc'd.
```

## Related
- [[on-button-reopen]] — the reopening plan; this ledger is its mirror image (what must be
  settled to get out, vs what must be funded to restart).
- `.claude/skills/samira-off-button/SKILL.md` — the scanner that maintains this note.
- `.claude/anchors.md` — board ID, column and group IDs for the rendered board.
