---
created: 2026-07-16T14:10-04:00
updated: 2026-07-17T17:23-04:00
domain: cuzzies
type: task
status: done
tags: [nj-sales-tax, greenbooks, karbon, tax-gate, wind-down]
source: gmail
due: 2026-07-20T09:00-04:00
---

# Karbon request — Q2 2026 NJ sales tax filing needs Lemar's response by Monday

Jessica (jessica@huljevgroup.com) emailed asking Lemar to respond to a "Karbon request"
— the NJ sales tax filing for Q2 2026 is due Monday 2026-07-20 and they need his
response to file on time. No specifics on what the request asks for; a Karbon portal
notification typically requires logging in directly (not something a drafted email
reply resolves).

This lands squarely on the open NJ sales tax exposure question already tracked:
GreenBooks filed Q1 2026 without payment and flagged that 2025 back quarters "appear
not to have been filed"; the 2026-07-12 research pass found no follow-up confirming
back-period filing status (see `[[2026-07-12-nj-sales-tax-greenbooks-status-research]]`).
Whether "Huljev Group"/Jessica is GreenBooks staff, a Karbon-hosted subcontractor, or a
separate firm is unconfirmed — GreenBooks' known contacts on file are Michael Gavigan,
Tiffany, and Richard Wyse (@greenbookscpa.com), not huljevgroup.com.

Needs Lemar directly: logging into the Karbon portal is not something Samira can do,
and confirming/authorizing a tax filing is a judgment call, not a draft-and-send.

## Update 2026-07-16 (PART D email loop — Lemar asked us to check for a portal link)
Searched Gmail for a Q2 Karbon portal link. Jessica's message is plain text with no
button/link embedded — nothing to click there. The only Karbon portal links on file
are from the Q1 2026 GreenBooks checklist reminders (Reminder #1–5, mgavigan@greenbookscpa.com,
2026-04-18 through 2026-04-22): domain `clientportal.karbonhq.com`, tenant key
`3tGL7RHfCGdX` (GreenBooks' Karbon tenant), each link a checklist-item-specific token
("Confirm date, amount and bank of NJ State Sales Tax Payment" — the Q1 item). No
GreenBooks/Karbon email with a fresh Q2 checklist link has landed in the inbox yet as
of this scan. Those old tokens are almost certainly scoped/expired for the Q1 item, not
usable for Q2. Likely path: either a Q2 checklist email hasn't gone out yet (worth
following up with Jessica/GreenBooks directly), or Lemar can try logging into
`https://clientportal.karbonhq.com` directly with his account rather than waiting on a
link. Posted this finding back in the #decisions thread; no email drafted (nothing to
reply to — this needs a portal login, not a reply).

## Update 2026-07-17 (PART D email loop — Jessica replied with the actual figures)
Lemar's own 7/17 reply (sent directly from Gmail, not through a Samira draft) asked
Jessica to resend the Karbon link/access details. She replied same day (16:14 ET):
says she may be having delivery issues on her end, resent the request inline instead of
via Karbon. The figures she's asking Lemar to review and confirm:

- Cannabis Sales: $100,624.06
- Non-Cannabis Sales: $487.08
- Total Sales for the Quarter: $101,111.14
- Sales Tax Due: $6,698.61

She also asked Lemar to confirm the bank account/routing number to use for payment —
that is a controlled financial field Samira will never fill in or guess; it has to come
from Lemar directly, never over email in a Samira-drafted reply.

Posted 3 reply-option drafts as threaded replies under the existing #decisions card
(thread `1784225480.998989`) rather than opening a new card, since this is the same
open item, just with more information now. None of the options confirm the dollar
figures as accurate (only Lemar can verify against internal records) and none include
banking details — all three route the account/routing exchange to a direct call.

## Update 2026-07-17 later (PART D email loop — verified: Lemar closed this himself)
This run was asked to check whether Lemar's capture-DM request ("respond to that
Jessica email asking for a Karbon link") had actually been actioned, since the capture
was dedup-marked ✅ but showed no visible in-thread resolution. Checked Gmail directly:
Lemar sent his own reply at 13:15 ET on 7/17 (bypassing the Samira draft loop) asking
Jessica exactly for the Karbon link/access details — wording matches the draft Samira
had already saved to Gmail Drafts earlier that morning. Jessica resent the figures
inline (16:14 ET); Lemar himself replied directly again at 16:24 ET confirming the
figures match internally ("$100624.06 cannabis, $487.08 non-cannabis, $101111.14
total, $6698.61 due. Nothing to [flag]"). Jessica confirmed at 16:28 ET she'll file the
return today. No further draft or Slack action needed — the ask is fully resolved by
Lemar's own direct emails, so the outstanding filing-response task is closed. The three
#decisions reply options posted earlier are now moot (superseded by Lemar's direct
reply) and are being left un-reacted rather than nudged again. Marking status `done`;
the underlying due-Monday filing/payment itself is tracked separately via the
compliance calendar (`due` field retained here as a pointer, not an open task).

## Update 2026-07-17 (calendar-sync — reminder retired)
Status is `done`; the 7/20 09:00 ET reminder event (`t5mqt1d85canl5ugdgl12hcrec`) has
been cancelled and the id cleared per the calendar-sync RETIRE rule.

## Sources
- gmail: thread 19f6c18133f23ab2 ("Q2 2026 NJ Sales Tax", jessica@huljevgroup.com) —
  latest message id `19f70e883fa79658`, 2026-07-17T16:28:31Z, Jessica confirms she will
  file today
- gmail: thread 19db583a88878413 ("Reminder #5 - Q1 2026 NJ Sales Tax Return", mgavigan@greenbookscpa.com, 2026-04-22) — Karbon portal link pattern reference
- slack: #decisions thread `1784225480.998989`
