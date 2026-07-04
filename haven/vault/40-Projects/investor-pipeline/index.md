---
created: 2026-07-04T13:30-04:00
updated: 2026-07-04T13:30-04:00
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
| BizFundsHub | Cuzzie's | David Cancro · submissions@BizFundsHub.com | Bridge loan or equity (lender/debt-equity) | [folder](https://drive.google.com/drive/folders/1G4vqdv-5kz0x5ATpSCTjDC_tJyEsnkFv) | Needs info | Master exec summary + deck missing from Master Templates — Lemar to confirm the master doc; no outreach until tailored | 2026-07-04 |
| 420 Solutions (Suite420) | Cuzzie's | — | Lender — docs requested | folder in Data Rooms parent | Needs info | Lender doc list requested 2026-07-03 — see [[2026-07-03-suite420-solutions-lender-docs-needed]] | 2026-07-04 |
| Star Renovate Funding | Cuzzie's | — | — | folder in Data Rooms parent | Working | Confirm contact + ask; tailor room once masters exist | 2026-07-04 |
| Getty Advance | Cuzzie's | — | — | folder in Data Rooms parent | Working | Confirm contact + ask; tailor room once masters exist | 2026-07-04 |

## Sources
- drive: Data Rooms parent + Master Templates folder (IDs in repo `.claude/anchors.md`)
- slack: #investor-pipeline (thread links live on each deal's receipt note)
