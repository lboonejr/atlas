---
created: 2026-07-22T10:10:17-04:00
updated: 2026-08-02T08:15:00-04:00
domain: cuzzies
type: task
status: active
tags: [leafly, invoice, collections]
source: gmail
---

# Leafly — new invoice $349.30, account already escalated to collections at $653.30

Two no-reply billing automations landed together (2026-07-22): a new invoice
(INV00390714, due today, $349.30, addressed to Lemar and Joshua) sitting alongside a
collections escalation notice from the day before (case #00157347, $653.30 past due,
addressed to Joshua/cc Lemar) that had no Haven note yet. Filed together on the
#decisions card (parent, ts `1784722765.550729`) since it wasn't clear whether the new
invoice sits inside or on top of the $653.30 collections figure — not guessed.

## Update 2026-07-22 (10:10 ET) — closed
Lemar reacted 🫡 on the #decisions card — read as "close/let ride" per the card's own
options (✅ once handled · 🫡 to close/let ride). No payment made, no reply drafted; the
$349.30 invoice and the $653.30 collections case both stand as-is. Replied in-thread
noting the close (message-edit tooling isn't available to this connector, so the parent
was left as posted rather than edited to "CLOSED").

## Update 2026-07-26 (~10:05 ET) — repeat past-due notice, no new figure
Another automated notice landed (Gmail thread `19f9d971f0ac3cb3`, 2026-07-26 ~4:42am
ET, `accountsreceivable@leafly.com`, "Cuzzie's Dispensary & Delivery is PAST DUE"),
asking Lemar to confirm an ETA for payment. No dollar figure included beyond what's
already on file here. Consistent with the standing 🫡 let-ride decision — not
re-flagged in #decisions; logged here only. If a new/changed balance shows up, or this
escalates further (legal, service cutoff), that's a new flag.

## Update 2026-07-29 (~09:20 ET) — escalated further, new case, higher balance
Gmail thread `19fab0271af4ddbb` (2026-07-28 ~11:14pm ET, `help@leafly.com`, to
joshua@cuzziesnj.com / cc lemar@cuzziesnj.com), subject "Your Account Is Being
Transferred To Collections - Pay Today!": new case #00159241, balance now
**$1,002.60** (up from $653.30), explicit "pay today" ultimatum, states the account
will be transferred to their Collections team due to no response, invites a reply
("simply reply to this email"). Meets the escalation bar this note flagged on
2026-07-26 (new/changed balance) — reopening status to `active`; 3 draft reply
options posted to #decisions matching the established pattern for this saga (short
holding reply / brief ack / no-reply-let-ride, consistent with Lemar's prior 🫡
decision on this exact account).

## Update 2026-07-29 (2, ~09:35 ET) — closed again, Lemar saluted (let ride)
Lemar reacted 🫡 directly on the #decisions parent (message ts `1785290148.421429`,
no option ✅'d) for the case #00159241 / $1,002.60 collections-transfer card — same
"close/let ride again" signal as the 7/22 close on this account, per the card's own
option text. No reply sent, no payment made or scheduled; the $1,002.60 balance and
collections-transfer status stand as-is. Replied in-thread noting the close (parent
left as posted, message-edit tooling still unavailable on this connector). Status
moved back to `done` for this round — if the balance changes again or this escalates
past a collections-transfer notice (legal, service cutoff), that's the next flag.

## Update 2026-08-02 (~08:15 ET) — reopened, another direct contact request
New thread this pass, Gmail thread `19fc1a42513c653f` (2026-08-02 ~08:43 ET,
`accountsreceivable@leafly.com`, "Your Account Requires Immediate Attention"): Leafly's
Accounting Team asks Lemar to contact them today about the account and payment
options, and separately asks for payment details (date/amount/method/remittance name)
if funds were already sent, with rep Dante offered as a contact. No new balance figure
given beyond the $1,002.60 / case #00159241 already on file here. Reopening status to
`active` (same pattern as the 7/29 reopen) — 3 draft reply options posted to
#decisions, matching the established short-holding-reply pattern for this saga. No
reply sent, no payment made or scheduled.

## Sources
- slack: #decisions (C0BBXA96FFV), card ts `1784722765.550729`, Lemar's 🫡 reaction
- gmail: thread `19f9d971f0ac3cb3` (2026-07-26 past-due notice, repeat, no new figure)
- gmail: thread `19fab0271af4ddbb` (2026-07-28 ~11:14pm ET, collections transfer
  notice, case #00159241, $1,002.60)
- slack: #decisions (C0BBXA96FFV), card ts `1785290148.421429`, Lemar's 🫡 reaction
  (closed 7/29, let ride again)
- gmail: thread `19fc1a42513c653f` (2026-08-02 ~08:43 ET, "Your Account Requires
  Immediate Attention", direct contact request)
- slack: #decisions (C0BBXA96FFV) — new card posted 2026-08-02 with 3 draft reply
  options
