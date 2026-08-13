---
created: 2026-08-12T10:00-04:00
updated: 2026-08-13T15:30:00-04:00
domain:    # UNRESOLVED — set one of: personal | cuzzies | station | project | reference | legal | automation
type: task
status: active
tags: [google-workspace, google-voice, subscription, cuzziesnj-domain]
source: gmail
---

# Google Voice subscription (cuzziesnj.com) — scheduled for cancellation Sep 11

Automated Google Workspace notice received 2026-08-12: the Google Voice
Starter subscription on the `cuzziesnj.com` Workspace account
(`username: lemar@cuzziesnj.com`) was **suspended July 13, 2026** and is
now **scheduled for cancellation on/after September 11, 2026**.

If not reactivated before then (Admin console → Billing > Subscriptions),
Google states **associated data and phone numbers will be deleted** once
cancelled. No-reply automated sender — nothing to correspond on, but it
is a real decision point: reactivate (paid subscription spend) or let it
lapse — relevant given the Cuzzie's (Camden) wind-down context. Not my
call to make — Lemar decides.

- **Account:** lemar@cuzziesnj.com (Workspace domain cuzziesnj.com)
- **Suspended:** July 13, 2026
- **Cancellation target:** on/after September 11, 2026
- **Action to keep:** sign in to Google Admin console (https://admin.google.com) → Billing > Subscriptions → reactivate

## Sources
- gmail: thread `19ff61b5c3452082` ("Your Google Voice subscription is scheduled for cancellation", workspace-noreply@google.com, 2026-08-12)

## Update 2026-08-13 — broader escalation, likely the same root cause

A second, broader automated notice landed today: **"Set up billing for Google
Workspace Business Standard for cuzziesnj.com"** — the *entire* Workspace
subscription (not just Voice) "is no longer provided to you through your
reseller." Services continue **until August 20, 2026**, after which **all
Workspace services for all users on cuzziesnj.com are suspended** — this
would include `lemar@cuzziesnj.com` email itself, not just Google Voice.

This reads as the likely root cause of the Voice suspension above: the
reseller relationship backing the whole Workspace account appears to have
lapsed, not just the Voice add-on. Same decision shape, now higher-stakes
and with a harder near-term deadline (8/20, vs. Voice's 9/11):
- **Do nothing** → all Workspace services (including primary business
  email) suspend 8/20/2026.
- **Set up direct billing** → sign in to Google Admin console
  (admin.google.com) → Billing, and add a payment method directly with
  Google instead of through the (former) reseller.

Not executed — setting up billing is a payment-method decision, outside
Samira's authority. Raised as a #decisions card given the harder deadline
and business-email-wide blast radius.

- **Customer ID:** `C00hppi2w`
- **Deadline:** services suspend after **August 20, 2026**

### Sources (this update)
- gmail: thread `19ffc043a83ed7d0` ("Set up billing for Google Workspace
  Business Standard for cuzziesnj.com", workspace-noreply@google.com,
  2026-08-13)

## Update 2026-08-13 (2) — Lemar picks Option 1: self-serve direct billing

Lemar reacted ✅ on Option 1 in the `#decisions` card ("Google Workspace
(cuzziesnj.com) — billing lapse, ALL services suspend 8/20", ts
`1786641661.331369`, option ts `1786641664.664189`): he will set up direct
billing himself in the Google Admin console — no action needed from Samira
on the billing setup itself.

He then flagged a **dependency** in-thread: setting up the new Workspace
billing/payment plan in Admin console will first require paying down the
overdue **Google Voice** balance he's behind on (the suspension tracked
above) — the two issues share the same reseller/billing root cause, and the
Voice arrears look like they're blocking the Workspace fix.

**Status:** decision logged, no payment made or authorized by Samira. Both
the Google Voice reactivation (Update above) and this Workspace direct-billing
setup remain Lemar's direct action in the Admin console; the sequencing is
now: clear Google Voice balance → then Workspace billing can be set up.

### Sources (this update)
- slack: #decisions ts `1786641661.331369` (card) / `1786641664.664189`
  (Option 1, ✅'d) / `1786642451.199409` (Lemar's dependency note)
