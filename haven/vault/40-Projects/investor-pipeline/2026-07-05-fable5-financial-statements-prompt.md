---
created: 2026-07-05T11:04-04:00
updated: 2026-07-05T11:16-04:00
domain: project
type: brief
status: active
tags: [fable5, financials, balance-sheet, pl-statement, investor-pipeline, cuzzies]
source: slack
---

# Fable 5 prompt — build Cuzzie's balance sheet + P&L before access lapses

Lemar captured in #atlas (2026-07-05 11:04 ET): he has Fable 5 access for only a
few more days and wants to use it to build balance sheets and P&L statements —
anything financial an investor or lender might need — before it's gone. He wants
the prompt planned carefully so Fable pulls in everything available.

## Why this matters right now
The investor pipeline is explicitly blocked on this: `[[index]]` (investor
pipeline) shows BizFundsHub's data room stalled on a missing "master exec summary
+ deck," and 420 Solutions/Suite420 has an open lender doc request
([[2026-07-03-suite420-solutions-lender-docs-needed]]). A real balance sheet + P&L
is the single artifact that unblocks multiple asks at once.

## What Haven already knows (for Fable to work from — not exhaustive, source docs needed)
**Cash position / cash flow**
- Parke Bank account **-8046** overdrawn **$1,243.13** as of 7/3, after 3 NSF
  returns (Intuit $151, PayPal $17.55, PayPal $3.94).
- Gusto flagged the 7/3 payroll run may not clear given current cash balance.

**AP / vendor obligations (tracked on the #on-button canvas)**
| Vendor | Amount | Status |
|---|---|---|
| ADT | $1,637.84 | 90 days past due |
| Progressive Commercial | $2,117.80 | policy cancels if unpaid |
| EPLI (Berkley Select / First Insurance Funding) | $4,051.12 | to reinstate |
| Comcast Business | $267.74 | due 7/16, current |
| PSEG | $391.58 | 2 payments past due |
| Leafly | unknown | ~2 weeks past due |

**AR / unresolved vendor statements (amounts not yet extracted — PDFs unopened this session)**
- Curaleaf AR statement `CNJ2-000241` — [[2026-07-04-curaleaf-account-statement]]
- Weedmaps invoice `SIN830881` — [[2026-07-03-weedmaps-invoice-sin830881]]

**Legal liability**
- Harrison Acquisitions eviction, Camden County CAM-LT-004393-26, arrears
  **~$42,157.37**, trial 7/30/2026.

**Operating status**
- Cuzzie's Dispensary & Delivery — temporarily closed, wind-down in progress.
- Gusto payroll account being split into Cuzzie's / Station Dispensary sub-accounts.

## What's still needed before Fable can produce something lenders will trust
This list above is enough for context, not enough for real statements — a balance
sheet/P&L needs source documents Samira hasn't opened this session: bank
statements (Parke Bank, full period), Dutchie POS sales reports, Gusto payroll
register, and full AP/AR aging (the Curaleaf and Weedmaps PDFs need opening).

## The drafted Fable 5 prompt
Posted to #admin as a `run:manual` fence (Lemar runs this himself in Fable, not
Samira) — see the #admin post for the exact text to paste in.

## Sources
- slack: #atlas capture, 2026-07-05 11:04 ET (channel C0BBWHCJUV9, ts 1783263848.695329)
- haven: `haven/vault/40-Projects/investor-pipeline/index.md`
- haven: `haven/vault/20-Cuzzies/2026-07-03-gusto-jul3-payroll-funding-shortfall.md`
- haven: `haven/vault/20-Cuzzies/2026-07-05-on-button-canvas-leafly-sync.md` (canvas totals)
