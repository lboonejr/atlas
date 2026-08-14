---
created: 2026-08-11T17:50-04:00
updated: 2026-08-14T16:50-04:00
domain: cuzzies
type: task
status: active
tags: [insurance, crum-forster, premium-audit, compliance]
source: gmail
---

# Crum & Forster - final premium audit, documents needed

Jason Kanner (Manager, Premium Audit Mgmt at Crum & Forster) emailed 2026-08-11 requesting the final premium audit package for the expired policy (Policy #408-756018-6, period 4/4/26-6/15/26).

Documents requested:
- Master payroll journals + summary for the policy term (gross wages by state/employee/class code)
- Subcontractor / 1099 vendor detail (amounts paid + Certificates of Insurance)
- Federal + State quarterlies for four quarters covering the policy term
- List of elected executive officers/owners/partners
- General description of operations (entity/location/any changes)

Can submit via email or their secure portal (GoOnlineAudit.com/cfins, Control ID 45947). No hard deadline stated in the body beyond it being the "final" audit on an already-expired policy - worth confirming receipt promptly so the audit doesn't default to an estimated/penalty premium.

Cuzzie's has been in a temporary closure since June 13, so pulling together current payroll/1099 records may take longer than usual - worth flagging that in the reply and asking for some flexibility on timing.

## Update 2026-08-11 (PART C, run:admin-3x attempt 1)
Ran the staged `run:admin-3x` document-gathering prompt from #admin (ts `1786482807.791379`).
Searched connected Google Drive for payroll/1099 records — found general payroll exports
(`Cuzzies - ...Payroll-template-2025-04-01-to-2026-02-26.csv`, a P&L detail workbook, Gusto
resource links) but nothing pre-packaged for the specific 4/4/26-6/15/26 audit period, and no
subcontractor/1099 detail, quarterlies, officer list, or operations description located via
Drive search. Assembling and representing a "final" audit package to an outside insurer is a
factual submission on Lemar's behalf — not something to package and send without his review,
even though no payment is involved. Not marking this run:admin-3x task done; leaving it staged
(un-reacted) in #admin for a follow-up pass, and flagging that full completion likely needs
Lemar to pull current payroll/1099 detail directly (Gusto access) rather than Drive search
alone. The reply-only #decisions card (ts `1786482812.188359`) is separate and still open,
awaiting Lemar's pick.

## Update 2026-08-12 (PART C, run:admin-3x attempt 2)
Re-ran the staged prompt. Re-checked Drive: the payroll export on file
(`Cuzzies-...-Payroll-template-2025-04-01-to-2026-02-26.csv`) ends 2026-02-26, before the
audit period starts (4/4/26) — confirms attempt 1's finding that no payroll/1099/quarterly
data covering the actual policy term is available via Drive search; that data lives in Gusto,
which isn't a connected tool here.

Per the safety floor (Gmail Drafts only, never send), saved a reply draft on the original
thread (Gmail thread `19ff22c4e7226c09`, draft id `r-6414875302012055811`) rather than sending
anything: it confirms receipt, supplies the two items that ARE safely answerable from the
company's own records without judgment calls (officer list — Lemar Boone & Joshua Evans, both
Owners, per the Cuzzie's payroll template; and a one-line operations description — licensed NJ
adult-use retail + delivery at 2750 Mount Ephraim Ave, Camden, no entity/location changes), and
asks Jason Kanner for timing flexibility on the remaining payroll/1099/quarterly documents given
Cuzzie's temporary closure since June 13. Nothing sent — draft is Lemar's to review/send.

Full package assembly (payroll journals + 1099 detail + quarterlies for the exact audit period)
remains blocked without Gusto-level access; this is the second `run:admin-3x` pass without a
tool path to close it out. Recommend Lemar either grant a Gusto-connected tool or pull those
three items directly — reacting ✅ on the #admin prompt to reflect the draft-reply progress made
this pass, but the underlying document gap stays open in this note.

## Update 2026-08-14 (PART B capture — Lemar's own priority signal)
Lemar dropped a note in the capture DM: "Next week we're also gonna have to work on
that final audit from Crum & Forster. Tryna knock that out" (ts `1786740623.047939`).
Confirms he intends to prioritize closing out the document gap next week. No new
action taken here — the open reply draft (Gmail draft `r-6414875302012055811`) is
still his to review/send, and the underlying blocker (payroll/1099/quarterly detail
lives in Gusto, not a connected tool) is unchanged. Logged as a priority signal only.

## Sources
- gmail: thread `19ff22c4e7226c09` - Jason Kanner (Crum & Forster) final audit request, 2026-08-11;
  reply draft `r-6414875302012055811` saved 2026-08-12, not sent
- slack: #admin ts `1786482807.791379` (staged run:admin-3x prompt) · #decisions ts `1786482812.188359` (reply card) · capture DM `D0BHPKMDNEP` ts `1786740623.047939` (2026-08-14 priority signal)
