---
created: 2026-07-08T18:10-04:00
updated: 2026-07-16T11:00-04:00
domain: cuzzies
type: task
status: active
tags: [slack, billing, subscription, payment-failed]
source: gmail
---

# Slack workspace payment overdue — Cuzzie's Dispensary & Delivery

Slack (feedback@slack.com) emailed lemar@cuzziesnj.com at 2026-07-08 17:42 ET: payment
collection failed for the **Cuzzie's Dispensary & Delivery** workspace
(cuzziesdispen-olw2921.slack.com). The workspace will be downgraded from Pro soon if the
payment method isn't updated.

Two paths, both need Lemar's call — no autonomous payment action taken:
- Update payment details to keep Pro: https://cuzziesdispen-olw2921.slack.com/x-t9244775582213-11549104593009/admin/billing/failed
- Switch the workspace to the Free plan: https://cuzziesdispen-olw2921.slack.com/x-t9244775582213-11549104593009/admin/billing

Relevant context: Cuzzie's is winding down mid-2026, which may make downgrading to Free
(or letting it lapse) the more sensible call rather than fixing payment for a Pro plan.

## Sources
- gmail: thread 19f43ae8b17065bf (Slack "Overdue payment for Cuzzie's Dispensary & Delivery", 2026-07-08 17:42 ET)
- gmail: thread 19f67e0d4f3628eb (Slack "Your workspace will be downgraded in 7 days", 2026-07-15 18:23 ET — escalation)

## Update 2026-07-09
Lemar picked Option B in #decisions (✅, 2026-07-08 evening): switch the workspace to
Free, let Pro lapse. Logged here; this is a Slack workspace-admin billing action
Samira has no tool/login to perform — needs Lemar to click through in the Slack admin
billing page (link above). Leaving `status: active` until that's done.

## Update 2026-07-16
Slack escalated: new no-reply notice says the workspace will be **downgraded to Free in
7 days** (by ~7/22) if payment isn't received, and spells out the consequences —
shared channels disconnected permanently, guests disconnected, only the most recent
10,000 messages viewable, 5 GB file cap. Decision was already made (switch to Free) but
the manual click-through in Slack's billing admin still hasn't happened. Nudging in
#decisions since there's now a hard date; no autonomous billing action taken.
