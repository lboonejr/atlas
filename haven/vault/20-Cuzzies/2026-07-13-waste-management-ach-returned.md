---
created: 2026-07-13T16:10:00-04:00
updated: 2026-07-26T15:05:00-04:00
domain: cuzzies
type: task
status: active
tags: [waste-management, billing, payment-failed, ach]
source: gmail
---

# Waste Management — ACH payment returned, needs a payment-method fix

Waste Management (noreply_paymentservices@wm.com) emailed 2026-07-13 ~13:16 ET: a
recent ACH payment was returned by the financial institution on file. "Please review
your payment method and try again."

No amount given in the notification itself — needs Lemar to log into the WM account
portal to see the returned amount and update the payment method (likely tied to
the same Parke Bank overdraft pattern affecting other vendor ACH pulls this month —
Elevate Funding, GoDaddy, PayPal returns already tracked). Samira has no WM login.

## Update 2026-07-25
Waste Management sent another automated "Your payment is overdue" notice
(noreply@communications.wm.com) 2026-07-25 ~10:48am ET — second WM payment notice
this month. Service address 2750 Mount Ephraim Ave, Camden NJ 08104, Customer ID
32-81926-53003. No dollar amount is printed in the notice text itself (template
lacks a merge value) — same gap as the 7/13 notice. No reply drafted: sender is
no-reply, and this is a portal-login/payment-authorization item, not a correspondence
thread. Likely the same cash-timing pattern behind the other returned-item threads
(this routes through #decisions for Lemar to authorize payment — Samira never
executes a payment).

## Update 2026-07-26 (PART A reaction sweep)
Lemar reacted ✅ on the #decisions card (ts `1784992521.248129`). Read as: acknowledged,
proceed as far as possible — but this remains a portal-login/payment-authorization item
Samira has no credentials for (no WM account login), so nothing further was executed:
no call placed, no portal login attempted, no payment made. Closing the loop with a
"Done ✅" reply in-thread so this doesn't keep re-surfacing; the actual portal fix is
still Lemar's to run directly. Also repaired this note during this pass — it had been
stored on `main` as a raw base64 blob (same double-encoding bug logged in
`haven/vault/50-Reference/2026-07-25-base64-corruption-repair.md`); decoded and
rewritten as plain markdown, no content lost or changed beyond this Update section.

## Sources
- gmail: thread 19f5b9ee5a24e411 ("Your Payment was Returned", 2026-07-13 13:16 ET)
- gmail: thread 19f99bf9ec108e31 ("Your payment is overdue", 2026-07-25 ~10:48am ET)
- slack: #decisions message ts `1784992521.248129` (✅ reacted 2026-07-26, PART A sweep)
