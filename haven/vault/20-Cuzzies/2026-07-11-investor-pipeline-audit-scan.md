---
created: 2026-07-11T13:20:00-04:00
updated: 2026-07-11T13:20:00-04:00
domain: cuzzies
type: log
status: active
tags: [samira, investor, audit, bobby-lee, sweet-leaf-finance, jason-klein, cann-dev]
source: slack
---

# Investor pipeline — PART E audit scan (2026-07-11 ~13:20 ET)

No new work this scan (Gmail `Samira/investor` empty, #investor-pipeline quiet since the
10:14 ET pass — all 7 index rows unchanged and accurate). Spent the scan auditing Drive
against the index and the channel's full history instead, and turned up three things
worth a durable record even though none of them changed the index.

## 1. Jason Klein — Data Room (Drive) is NOT an investor-pipeline deal
A folder named **"Jason Klein — Data Room"** was created 2026-07-10 23:49–2026-07-11
00:24 ET directly under the Investor Data Rooms parent
(`1U7GFTuA5Tj6TMD0CWgfZhWwSbwWKWDfF`), holding Cuzzie's closing-report/bank-statement/
license/MCA diligence docs. Jason Klein is the Cann.Dev **sell-side M&A broker** sourcing
a buyer for the Camden dispensary license + lease (the $250K→$400K sale track, entity
already stubbed at `50-Reference/Entities/cann-dev.md`, updates filed at
`20-Cuzzies/2026-07-09-camden-dispensary-sale-update.md`) — the opposite direction of an
investor/lender relationship. **Correctly NOT added to the investor-pipeline index.**
Flagging only because the folder now sits inside the *investor* Data Rooms parent
alongside lender rooms, which will confuse anyone browsing that parent later — Lemar's
call whether to leave it (harmless) or relocate it under a Cuzzie's-sale folder. Not
moved or touched here.

## 2. Two 2026-06-27 deals (Bobby Lee, Sweet Leaf Finance) fell out of tracking with dead Drive links
Thread history (`#investor-pipeline`, parent messages 1782525779.553489 and
1782525781.961709) shows both got a full data-room build + Gmail draft on 2026-06-27:
- **Bobby Lee** (Emirates Investment, Bobby@emiratesinvestment.com) — $250K Cuzzie's-only
  bridge loan, 36mo/18% APR, deck built, folder created
  (`drive.google.com/drive/folders/1A5Q5F0ch-jQFjsXmCKQBf_gCDyyPOpqR`), draft
  `r7132968590892364192` staged awaiting Josh/Lemar's send + a 🫡 salute.
- **Sweet Leaf Finance** (info@sweetleaffinance.com) — debt-restructuring angle, folder
  created (`drive.google.com/drive/folders/1HHQfbClA64pI_uUyqn40OgugsdaU3fcr`), draft
  `r-8901499958598431100` staged, same ask for a 🫡 once sent.

Neither ever got the salute, neither ever got an index row, and both then simply stopped
appearing in scans after ~2026-07-01 with no formal Passed/Parked disposition. Checked
today: **both Drive folder IDs now come back "ineligible" via `get_file_metadata` and
return zero hits via `search_files` by title** — they read as gone, not just unlinked.
Not rebuilt or re-drafted here (would be guessing at whether Lemar wants these two
revived at all, and the data likely needs refreshing if so). Flagged to Lemar in
#investor-pipeline for a call: revive (rebuild room + resend) or mark stale.

## 3. Five older cold leads never got a data room and never got a formal close
Ian Lindemann (Lead Funding, leadfunding.com, email never confirmed), Shya Mousavipour
(GVS/NSS Corp, gvsnsscorp.com — domain confirmed 6/29, send status unconfirmed), Mickey
Wills (mickeymixconsult@icloud.com), Meyer Goldman (email loop closed positively per
6/29 note, ball was in Lemar's court for a call), and Alfonso Rodrigo (LinkedIn only, no
email) — all Josh-sourced 6/25–6/29, all appeared in "standing queue" scans through
Scan 43 (2026-07-01) and then dropped from every subsequent pass with no Passed/Parked
disposition and no Drive folder ever built (`search_files` by name returns nothing).
Flagged to Lemar for the same call: revive or close out.

No index rows added or changed. No drafts, rooms, or sends this scan.

## Sources
- slack: #investor-pipeline C0BCCUKEUQ2 (full channel read, msgs 2026-06-25→2026-07-11
  10:14 ET) and threads on parent ts 1782525779.553489 (Bobby Lee) and 1782525781.961709
  (Sweet Leaf Finance)
- drive: Investor Data Rooms parent `1U7GFTuA5Tj6TMD0CWgfZhWwSbwWKWDfF` (current listing
  checked 2026-07-11)
- haven: `haven/vault/40-Projects/investor-pipeline/index.md`,
  `haven/vault/50-Reference/Entities/cann-dev.md`,
  `haven/vault/20-Cuzzies/2026-07-09-camden-dispensary-sale-update.md`
