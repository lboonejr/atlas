---
created: 2026-07-07T09:15-04:00
updated: 2026-07-07T10:25-04:00
domain: cuzzies
type: task
status: done
tags: [jotform, hipaa, saas, wind-down]
source: gmail
---

# Jotform — HIPAA compliance warning, forms disable effective 2026-07-10

Jotform emailed (7/7 ~6:33 AM ET, account username `Boone_Lemar`): the current
Free plan has not enabled HIPAA compliance features, so all forms will be
disabled effective **2026-07-10** unless the account is upgraded to the Gold
plan, or HIPAA compliance is explicitly removed from account settings
(Data section). Submission data already collected is unaffected either way.
Staged as a `run:admin-3x` prompt in #admin (2026-07-07 09:16 ET).

## Resolution — no action needed
Checked the live account via the Jotform API:
- `isHIPAA: "0"` and `hipaaCompliance: false` — HIPAA compliance is **already
  not enabled** on this account. Nothing to remove.
- Account `status: ACTIVE`, all 3 forms `status: ENABLED` (Destruction Report,
  Post-Destruction Report, The Station Dispensary — all NJ CRC/METRC cannabis
  inventory-destruction compliance forms; none collect PHI or any
  HIPAA-covered data), 0 submissions on each, well under the Free plan's
  5-form limit.
- The separate 7/6 "account disabled" email also doesn't match current
  reality — the account is active and forms are live.

Given the account already has HIPAA compliance off and all forms are enabled
with no HIPAA-relevant data collected, the 7/10 disable threat does not apply
as described. No settings change was made. If forms actually go down on or
after 7/10, that would indicate the warning email meant something Jotform's
API isn't reflecting yet — worth a manual look at jotform.com/myaccount/data
at that point, not before.

## Sources
- gmail: thread `19f3b482b43aa4cb`, message `19f3b482b43aa4cb`, 2026-07-07
  06:33 ET, from hipaa@jotform.com
- slack: #admin, `run:admin-3x` prompt, 2026-07-07 09:16:53 ET (TS 1783430213.555919)
- jotform: `user` API — `isHIPAA: "0"`, `hipaaCompliance: false`, 3 forms all `ENABLED`
