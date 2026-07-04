---
created: 2026-07-03T17:09-04:00
updated: 2026-07-04T13:30-04:00
domain: cuzzies
type: task
status: active
tags: [samira, gmail, weedmaps, invoice, po, blocked]
source: gmail
---

# Weedmaps invoice SIN830881 — due Jul 16, 2026

[[weedmaps]] (Ghost Management Group, LLC dba Weedmaps) sent invoice **SIN830881**, due
**Thu Jul 16, 2026**. Amount not stated in the email body (see the attached PDF
`InvoiceSIN830881.pdf` on the Gmail thread for the dollar figure — Samira did not open
the attachment).

Admin legwork (not a payment authorization): log/record this PO in the PO tracker via
po-payment-recorder so it isn't lost, ready for Lemar to authorize payment closer to the
due date. Staged as a fenced prompt in #admin 2026-07-03, run on a later scan (buffer
rule).

## Update 2026-07-03
PART C ran the staged #admin prompt (`task:20260703_weedmaps-invoice-sin830881`).
PO logged to the Monday PO tracker (item 12443675380, status Waiting): vendor, invoice
number, due date. Record-only — no payment authorized.

**Blocked:** the dollar amount is only visible in the attached PDF and Samira had no
PDF-reading tool that session, so the amount could not be pulled. Flagged to #decisions
asking Lemar to supply the amount or open the PDF himself. Source prompt in #admin
marked ⏳ (waiting), not ✅ — task is partially complete pending the amount.

## Update 2026-07-04
Merged the separate note `2026-07-03-weedmaps-invoice-sin830881-po-logged-amount-blocked`
into this one per the schema §7 thread rule (one matter, one note); that file is removed.

## Sources
- gmail: thread 19f24ea3bd41fa12 (invoice PDF attached)
- slack: https://newworkspace-zlb6313.slack.com/archives/C0BBXA96FFV/p1783116397144069 (amount-blocked flag in #decisions)
- slack: #admin staged prompt ts 1783113007.302029
- monday: board 18418714876, item 12443675380
