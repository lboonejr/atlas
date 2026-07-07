---
created: 2026-07-07T11:05:00-04:00
updated: 2026-07-07T11:05:00-04:00
domain: cuzzies
type: task
status: awaiting-decision
tags: [gusto, security, 2fa, payroll]
source: gmail
---

# Gusto — "verify identity to remove two-step auth" — 5x in 9 minutes, unrequested?

Gusto sent 5 near-identical "Verify your identity for Gusto support" emails between
2026-07-07 09:19–09:28 AM ET, each saying: "At your request, we're working on removing
two-step authentication from your account. Please take a moment to verify your
identity to continue this process."

Nothing in Haven shows Lemar (or anyone) asked Samira to touch Gusto's 2FA settings,
and there's no Haven record of Lemar mentioning this himself. The rapid-fire
duplication (5x in 9 minutes) is unusual for a routine self-service flow and matches
the pattern of an account-security/social-engineering attempt as easily as it matches
a genuine but glitchy Gusto request flow.

**No action taken — did not open or click any link in these emails.** This needs
Lemar's direct read: did he (or Josh, or an accountant with account access) actually
request 2FA removal on Gusto? If not, this may be someone trying to weaken account
security on a system tied to payroll/banking — worth a direct check of Gusto's
account activity/security log outside of any link in these emails.

## Sources
- gmail: messages 19f3cbc24d067639, 19f3cbe7b3400593, 19f3cc1f48b0de04,
  19f3cc3d90e06f2c, 19f3cc3d99f1825c (all "Verify your identity for Gusto support",
  2026-07-07 09:19–09:28 ET)
