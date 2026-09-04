---
created: 2026-09-02T04:55:01-04:00
updated: 2026-09-04T16:49:51-04:00
domain:    # UNRESOLVED — set one of: personal | cuzzies | station | project | reference | legal | automation (ID-scanning vendor used for compliance/age verification — could touch Cuzzie's, Station, or both; not stated which account(s) this notice covers)
type: task
status: awaiting-decision
tags: [veriscan, idscan, security-incident, data-breach, compliance, id-verification]
source: gmail
---

# VeriScan (IDScan.net) — potential security incident, under investigation

Automated notice from IDScan.net (`hello@idscan.net`, addressed to `admin@cuzziesnj.com`),
received 2026-09-02 4:55am ET: "VeriScan Update" — IDScan.net is investigating a
**potential security incident**. As of "earlier today, September 1," they received
information suggesting certain information may have been exposed and that IDScan.net
may be implicated. Investigation is preliminary; no conclusions yet on nature or scope,
including what information was involved.

Steps they say they've taken: securing potentially affected systems, notifying their
cyber insurance carrier, engaging outside legal counsel, engaging an independent
forensic firm, coordinating with law enforcement, preserving logs. They say they'll
keep customers informed; contact is `privacy@idscan.net`.

**Why this matters:** VeriScan/IDScan.net is an ID-verification vendor — the kind of
tool used for age/ID checks in a cannabis dispensary. If Cuzzie's and/or Station uses
it for compliance ID scanning, a breach could touch customer/employee ID data, which is
a real regulatory and reputational exposure, not just a routine vendor notice. Nothing
here confirms Cuzzie's/Station data was actually involved — this is a preliminary
"heads up" notice, not a confirmed breach report.

Nothing actioned — no reply needed/possible (no-reply-style vendor notice with a
contact address, not a request). Flagging for Lemar's awareness and judgment: whether
Cuzzie's/Station actually uses VeriScan, whether any ID data would be at risk, and
whether to follow up with `privacy@idscan.net` for specifics as their investigation
progresses.

## Update 2026-09-04 4:49pm ET

Follow-up from IDScan.net (`hello@idscan.net`, subject "Update specific to Cuzzie's
Dispensary & Delivery regarding the 9/1 security incident," to `admin@cuzziesnj.com`):
investigation still ongoing, but they now believe **Cuzzie's Dispensary & Delivery
specifically** ("your organization") may have been impacted — any data on Cuzzie's
VeriScan Cloud portal between **4/18/2026 and 9/1/2026** was potentially exposed. They
state no customer PII, biometric data, ID-scan location, or third-party check
information was included in the incident, and no org-identifying metadata was in the
exposed data. A full incident report is expected in "several weeks."

**Immediate security recommendations from the vendor:**
- Rotate device IDs and passwords on VeriScan devices
- Change VeriScan Cloud portal logins/passwords (skip if using SSO)
- Review roles and permissions of all cloud users
- Review data retention settings (record length, anonymization)

They plan a public notice + national media notice + dedicated 800-number for affected
individuals, to be shared once available. Contact remains their Account Representative
for questions.

**This resolves part of the original domain question:** the notice is addressed
specifically to Cuzzie's Dispensary & Delivery (`admin@cuzziesnj.com`), not Station —
worth confirming with vault-keeper/Lemar whether this should now file as
`domain: cuzzies` rather than staying UNRESOLVED, though it doesn't rule out Station
also using VeriScan separately.

**Not actioned by Samira** — rotating credentials and reviewing portal roles/retention
settings requires someone with actual VeriScan account access; flagging as time-
sensitive security recommendations for Lemar/whoever holds that access, not something
draftable or safe to act on unattended.

## Sources
- gmail: thread `1a05f9cd34527932` ("Important security information for VeriScan
  users", hello@idscan.net, 2026-09-02 04:55 ET)
- gmail: thread `1a06e2f5866b0cc9` ("Update specific to Cuzzie's Dispensary & Delivery
  regarding the 9/1 security incident", hello@idscan.net, 2026-09-04 20:49 UTC / 4:49pm ET)
