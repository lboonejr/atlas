---
created: 2026-08-21T23:07-04:00
updated: 2026-08-21T23:15-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-21

## Run summary
- Date: 2026-08-21 (~11pm ET scheduled run)
- Mode: LIVE (`DRY_RUN = false`)
- Account acted on: lemar@cuzziesnj.com
- Scope: Gmail only. Google Drive out of scope (no move/delete/trash tools connected).

## PART A — Vendor menus archived (3)
Each confirmed via attachment or live-menu link before archiving (labeled `Vendor Menus`,
removed from `INBOX`):

1. Thread `1a0202ba2c5a7b47` — "Parks Grove Menu Update — Ready to Restock" — kellie@parksgrove.com — 2026-08-20 — xlsx order form attached
2. Thread `1a0200702f28e5d6` — "TerrAscend Menu: New Products Added Since Monday..." — jpina@terrascend.com — 2026-08-20 — xlsx menu attached
3. Thread `1a01a576cec61f3f` — "Explore This Week's Garden Society Menu!" — njwholesale@thegardensociety.com — 2026-08-19 — live Distru menu link

Other vendor-domain hits in the inbox were general marketing (flavor-text drops, event invites,
AR statements, invoices, delivery scheduling) rather than menu blasts with an attachment/link —
left alone per the precision-over-recall rule.

## PART B — Trash sweep (7 threads)
All older than 12 months, `category:promotions`, no starred/important/genuine-filing-label
protection, sender not on the NEVER-TOUCH allowlist. Recoverable from Gmail Trash until
~2026-09-20 (30-day window).

1. Thread `198c97fb9cc0370c` — "Edibles sale!" — wholesale@verano.com — 2025-08-20
2. Thread `198c8e5781312161` — "Cooking Oils Now Available in Case Sizes of 10!" — smrita@vedawarrior.com — 2025-08-20
3. Thread `198c81d28e13fc23` — "Custom Signs Help Your School Make the Grade | FASTSIGNS" — 2115@fastsigns.com — 2025-08-20
4. Thread `198c807bdb87b4f7` — "Your mobile app, reimagined: Meet AIQ x Digital Awesome" — noreply@aiq.com — 2025-08-20
5. Thread `198c7de481c8cef6` — "You're invited: Data storytelling for business leaders" — marketing@engage.canva.com — 2025-08-20
6. Thread `198c7ba61a50f26f` — "More Styles. More Stock. DELIVERED" — homedepotpro@mg.homedepot.com — 2025-08-20
7. Thread `198c75b07bb1104a` — "Why the bread in Europe may be more tolerable" — fromthetimes-noreply@nytimes.com — 2025-08-20

No threads hit the 200/run cap.

### Skipped candidates (20 of the 27 initial matches) — allowlist/important tuning record
- 8 threads from `CTA@sos.nj.gov` — skipped, `*.gov` is on the NEVER-TOUCH allowlist
- 8 threads from `parkebank@parkebank.com` — skipped, `parkebank.com` is on the NEVER-TOUCH allowlist
- 1 thread (dutchie.com implementation survey, `19644c6a0e498f47`) — skipped, thread carries an IMPORTANT-labeled message
- 1 thread (Hamilton Farms weekly menu → real correspondence with Donte re: payment terms, `196110a96c91e798`) — skipped, genuine business correspondence plus IMPORTANT-labeled messages present
- 1 thread (ICIC mini-MBA program, `1826944b41c19b7a`) — skipped, thread carries an IMPORTANT-labeled message

This confirms the allowlist and the IMPORTANT-guard are both catching real cases — no changes
needed to either list from tonight's run.

## category:updates — report only, never auto-trashed
201 threads older than 12 months sit in `category:updates`. Per the runbook this category is
never swept automatically (invoices/bank/payroll/legal mixed with ads). Sender domains worth a
manual look if Lemar wants to clear some by hand: `notification.intuit.com` (QuickBooks
invoices/payroll), `aiq.com` (Alpine IQ), `cfins.com` (Crum & Forster insurance),
`jotform.com`/`jotformsign.com` (register float approvals — operational, not junk),
`voice-noreply@google.com` (missed-call notices), `headset.io` (scheduled reports),
`notifications@monday.com`, `nytimes.com`, `calendly.com`, `wm.com` (Waste Management),
`expertpay.com`.

## Notes
- No sends, replies, or drafts — Basil never takes an outward-facing action.
- Nothing starred, marked important, or user-labeled was touched.

## Sources
- gmail: 3 threads archived to `Vendor Menus` (Label_8), 7 threads trashed — thread IDs above
