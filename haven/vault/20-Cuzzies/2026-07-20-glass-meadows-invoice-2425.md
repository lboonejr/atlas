---
created: 2026-07-20T09:22-04:00
updated: 2026-07-21T09:05:00-04:00
domain: cuzzies
type: task
status: active
tags: [invoice, glass-meadows, accounts-payable, quickbooks]
source: gmail
---

# Glass Meadows Inc — Invoice 2425 ($4,617.92) needs recording/review

QuickBooks notification (`quickbooks@notification.intuit.com`) on behalf of vendor
**Glass Meadows Inc** (900 Haddon Ave Ste 100, Collingswood, NJ · accounting@glassmeadows.com
· +1 609-417-5553) — Invoice **2425**, total / balance due **$4,617.92**. Sent to
lemar@cuzziesnj.com and admin@cuzziesnj.com. This is a no-reply vendor notification (not a
thread expecting a reply) — the same invoice notification also landed the day before
(7/19) under a separate thread id, so this looks like a recurring QuickBooks reminder for
the same underlying invoice, not two separate invoices.

Needs: confirm this invoice against received goods/services, record it in the books, and
route for payment authorization per normal AP process. Samira does not pay or authorize
payment — that stays with Lemar/admin.

- Vendor: [[glass-meadows]]
- Amount: $4,617.92 · Invoice #2425
- Attachment: `Invoice_2425_from_Glass_Meadows_Inc.pdf` (on the source email)

## Update — 2026-07-20 — checked against wind-down stance, no action taken
Ran the staged `run:admin-3x` admin task (#admin ts `1784553795.722189`). Samira has no
QuickBooks write access, so "record it in the books" isn't an action she can perform
directly — flagging that gap rather than guessing at a bookkeeping entry. This is the
same recurring invoice 2425 notice already closed multiple times this month
([[glass-meadows]] — see `2026-07-17-glass-meadows-invoice-2425.md`, `2026-07-16`,
`2026-07-15`, `2026-07-14`, `2026-07-13`, `2026-07-04` repeats) under the established
wind-down stance: no call, no portal login, no payment made by Samira (safety floor).
Leaving `status: active` since actual QuickBooks recording + payment authorization is
still Lemar's/admin's to do; nothing further for Samira to execute here.

## Update — 2026-07-21 — same invoice, another daily QuickBooks reminder
Same notification recurred again (7/21 1:02pm ET, gmail thread `19f84c59624c5d54`),
identical vendor/amount/invoice number — no new information. Same wind-down stance as
7/20: no action Samira can take (no QuickBooks write access), recording + payment
authorization stays with Lemar/admin. Labeled `Samira/seen` in Gmail; no new
#decisions/#admin post (already staged and closed with the same finding). Leaving
`status: active`.

## Sources
- gmail: thread `19f7fa0541d4432b` (7/20 9:03am ET notification, PDF attached)
- gmail: thread `19f7a7dc89b00edf` (7/19 9:08am ET, same invoice/amount, earlier notification)
- gmail: thread `19f84c59624c5d54` (7/21 1:02pm ET, same invoice/amount, another repeat)
- slack: #admin `1784553795.722189` — staged run:admin-3x task
