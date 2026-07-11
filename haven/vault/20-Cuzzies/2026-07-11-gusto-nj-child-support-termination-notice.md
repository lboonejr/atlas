---
created: 2026-07-11T09:35:00-04:00
updated: 2026-07-11T11:05:00-04:00
domain: cuzzies
type: task
status: active
tags: [gusto, child-support, compliance, nj-employer, terminated-employee]
source: slack
---

# NJ Child Support — notify of terminated employee under income withholding

Gusto flagged that a terminated employee had wages garnished under a New Jersey child
support income-withholding order. NJ employers must promptly report the termination to
the NJ Child Support Employer Services Portal (njcsesp.com) / NJ NMSN Center —
continuing withholding through the final paycheck, and providing the termination date
and the employee's last known home address (new employer/address if known).

## Framework (posted to #atlas)
1. Log in to njcsesp.com (NJ Child Support Employer Services Portal) — same portal used
   for new-hire reporting.
2. File the Termination Notification for the specific employee, including: termination
   date, last known home address, and (if known) new employer name/address.
3. Withholding continues through the final paycheck already issued via Gusto; no further
   withholding needed once the report is filed.
4. If the order also carried a health-benefit provision, the employer notice will
   separately confirm no further obligation once the child support order itself is
   terminated/adjusted (that follow-up isn't on the employer to initiate).
This requires portal login on Lemar's own account — not something Samira can file.

## Decision needed (raised in #decisions)
Which employee, and does Lemar have their last known home address / any forwarding
employer info on file to complete the report.

## Update 2026-07-11 11:05 ET — details provided, Lemar self-filing
Lemar replied in #decisions (11:01 ET):
- Employee: Kenneth Jones
- Last known home address: 1561 S 8th Street, Camden, NJ 08104
- New employer/address: not on file
- Portal login (njcsesp.com) is currently rejecting both admin@cuzziesnj.com and
  lemar@cuzziesnj.com as unregistered. He is calling 1-877-654-4737 to sort account
  access, then filing directly himself. No further action from Samira — filing is his,
  not something requiring a portal login I have. Leaving `status: active` until he
  confirms filed; no reaction yet to close.

## Sources
- slack: #atlas (C0BBWHCJUV9), ts 1783775251.615809 (2026-07-11 09:07 ET)
- slack: #decisions (C0BBXA96FFV), ts 1783775382.603689 (thread reply 1783782112.223929)
- web: njcsesp.com FAQs, njchildsupport.gov/employers/responsibilities
