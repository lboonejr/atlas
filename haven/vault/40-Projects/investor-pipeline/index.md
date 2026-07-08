---
created: 2026-07-04T13:30-04:00
updated: 2026-07-08T21:15-04:00
domain: project
type: reference
status: active
tags: [investor, pipeline, index, samira]
source: claude
---

# Investor pipeline — index

One row per company/lender. **This table is the pipeline's state** — maintained by the
`samira-investor` skill (row edits + `updated` are its sanctioned machine writes; git
history preserves every prior state). Statuses: Working · Room ready · Sent ·
Needs info · Negotiating · Passed · Committed · Parked. Dead deals go Passed or
Parked — rows are never deleted.

| Company | Entity | Contact | Ask | Data room | Status | Next step | Last update |
|---|---|---|---|---|---|---|---|
| BizFundsHub | Cuzzie's | David Cancro · submissions@BizFundsHub.com (also corresponding from davidcancro7486@gmail.com) | Bridge loan or equity (lender/debt-equity); coverage caps at 2 of 3 MCAs | [folder](https://drive.google.com/drive/folders/1G4vqdv-5kz0x5ATpSCTjDC_tJyEsnkFv) | Sent | Lemar decided 7/8: Liquidibee is the MCA left out, Novus + Elevate Funding stay covered — no dollar terms yet, nothing to confirm to David in writing this scan. Original Gmail outreach draft (r-5106031061493058589) still unsent and may now be redundant — Lemar's call whether to discard | 2026-07-08 |
| 420 Solutions (Suite420) | Cuzzie's | Dave Miesner · dave@suite420solutions.com | Lender — $250K debt investment; term sheet pending | [folder](https://drive.google.com/drive/folders/1rzzLDg6V77dzPWF2tOawLABholzoJDoV) | Needs info | Dave needs 2025 YE + 2026 YTD financials (Income Statement + Balance Sheet) and a Guarantor PFS before he can finish the term sheet — financials are GreenBooks/QuickBooks pulls, PFS is personal; both Lemar's to complete, not a Samira draft — see [[2026-07-03-suite420-solutions-lender-docs-needed]] | 2026-07-07 |
| Star Renovate Funding | Cuzzie's | — | — | [folder](https://drive.google.com/drive/folders/1PBThQptYMzBigg7Z8RZiRKutoCdFtFWy) | Working | Masters now available in Master Templates — still need contact + ask confirmed by Josh before tailoring | 2026-07-07 |
| Getty Advance | Cuzzie's | — | — | [folder](https://drive.google.com/drive/folders/1tn5uZbSjWk3ffcJq6-CjggH4SotVc4pX) | Working | Masters now available in Master Templates — still need contact + ask confirmed by Josh before tailoring | 2026-07-07 |
| FundCanna | Cuzzie's | Sal Castaneda (Director of Partnerships) · scastaneda@fundcanna.com · 858-652-9437 — AE Peter Gladish cc'd | Operating Capital Line to restructure existing MCAs (Elevate, Novus, Liquid Bee) | [folder](https://drive.google.com/drive/folders/1FfYcoHmGVuih-Iup8Yo4tRZn98wn2C7T) — built by Lemar 7/8, all 3 MCA agreements + 11mo Parke Bank statements + payment-confirmation docs + debt investment summary · [[2026-07-08-fundcanna-restructure-application]] | Sent | Josh sent the full package to Sal by email 7/8 6:21pm ET (Drive folder linked, not a Samira draft); Sal confirmed receipt 7/8 8:50pm ET and is reviewing — no reply needed until FundCanna comes back with questions or a term sheet | 2026-07-08 |

## Sources
- drive: Data Rooms parent + Master Templates folder (IDs in repo `.claude/anchors.md`)
- slack: #investor-pipeline (thread links live on each deal's receipt note)
