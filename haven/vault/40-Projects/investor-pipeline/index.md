---
created: 2026-07-04T13:30-04:00
updated: 2026-07-07T13:15-04:00
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
| BizFundsHub | Cuzzie's | David Cancro · submissions@BizFundsHub.com (also corresponding from davidcancro7486@gmail.com) | Bridge loan or equity (lender/debt-equity) | [folder](https://drive.google.com/drive/folders/1G4vqdv-5kz0x5ATpSCTjDC_tJyEsnkFv) | Sent | David already has folder access and is actively corresponding — asked Lemar directly (7/6) for Josh's license + June bank statement; Lemar replied and supplied both himself, no draft needed. Original Gmail outreach draft (r-5106031061493058589) still unsent and may now be redundant — Lemar's call whether to discard | 2026-07-07 |
| 420 Solutions (Suite420) | Cuzzie's | — | Lender — docs requested | folder in Data Rooms parent | Needs info | Lender doc list requested 2026-07-03 — see [[2026-07-03-suite420-solutions-lender-docs-needed]] | 2026-07-04 |
| Star Renovate Funding | Cuzzie's | — | — | folder in Data Rooms parent | Working | Masters now available in Master Templates — still need contact + ask confirmed by Josh before tailoring | 2026-07-06 |
| Getty Advance | Cuzzie's | — | — | folder in Data Rooms parent | Working | Masters now available in Master Templates — still need contact + ask confirmed by Josh before tailoring | 2026-07-06 |

## Sources
- drive: Data Rooms parent + Master Templates folder (IDs in repo `.claude/anchors.md`)
- slack: #investor-pipeline (thread links live on each deal's receipt note)
