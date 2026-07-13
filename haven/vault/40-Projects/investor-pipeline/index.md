---
created: 2026-07-04T13:30-04:00
updated: 2026-07-13T14:45-04:00
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
| FundCanna | Cuzzie's | Sal Castaneda (Director of Partnerships) · scastaneda@fundcanna.com · 858-652-9437 — AE Peter Gladish cc'd | Operating Capital Line to restructure existing MCAs (Elevate, Novus, Liquid Bee) | [folder](https://drive.google.com/drive/folders/1FfYcoHmGVuih-Iup8Yo4tRZn98wn2C7T) — built by Lemar 7/8, all 3 MCA agreements + 11mo Parke Bank statements + payment-confirmation docs + debt investment summary · [[2026-07-08-fundcanna-restructure-application]] | Negotiating | **Declined 7/13 2:45pm ET** — Sal: application declined, but wants to review what's needed to position for approval "over the next couple of months." Josh (not a Samira draft) confirmed a call Tue 7/14 11:00 AM ET to discuss. Awaiting outcome of that call | 2026-07-13 |
| George Irwin | Cuzzie's | George Irwin · george@agreenroof.com · [LinkedIn](https://www.linkedin.com/in/georgeirwin/) | Lender/equity — angle: bridge loan; no ask amount given yet | [folder](https://drive.google.com/drive/folders/1PhEHnU6tbrI0xYqskjuCHejzYMGa4sm7) | Sent | Lemar sent a direct follow-up email himself 7/10 3:14pm ET (business snapshot + data room link, offered a call this week) — not a Samira draft. Still no ask amount/debt-vs-equity split, so masters remain un-tailored (BizFundsHub lesson). Awaiting George's reply — ask figure and/or a call time | 2026-07-10 |
| Eagle Bend Capital | Cuzzie's | David Martinsen (President) · david@eaglebendcapital.com · office (216) 312-6440 | Debt-restructuring assistance re: existing MCA obligations; no dollar figure/facility stated | [Lemar's own shared folder](https://drive.google.com/drive/folders/1Cs99W9vorYIQgKQyGt6tR4xZDbJOF2nR) (managed directly by Lemar, not a Samira-built room) | Sent | **Backfilled 2026-07-11** — active thread since 6/24, entirely Lemar-run, never labeled `Samira/investor`. 7/10 David requested MCA agreements + asked if operational/in default; Lemar replied same day (agreements added, confirmed temp closure/not generating revenue, current on lender obligations). Awaiting Eagle Bend's debt-restructuring partners' review — see [[2026-07-11-eagle-bend-capital-backfill]] | 2026-07-11 |

## Sources
- drive: Data Rooms parent + Master Templates folder (IDs in repo `.claude/anchors.md`)
- slack: #investor-pipeline (thread links live on each deal's receipt note)
