---
created: 2026-08-03T14:20-04:00
updated: 2026-08-03T14:20-04:00
domain: project
type: brief
status: awaiting-decision
tags: [samira, skill-forge, doc-naming]
source: slack
---

# Skill spec — doc-naming

Forged by skill-forge in the supervised PART H test run. Proposal quarantined at
`.claude/skills-proposed/doc-naming/`; not runnable until Lemar's ✅.

## The evidence — a direct request, not a recurrence

Lemar, #skills-lab 2026-07-10 14:41 (ts `1783694505.201439`), verbatim:

> "I want to make a skill that gives every doc that Samira creates a clean, easy to
> reference file name. The name should include the subject and the date in a standardized
> format"

This is the **direct-request** trigger, so his ask is the evidence. Per skill-forge step 2
no occurrence count is required and none is manufactured here — there is no logged tally
of badly-named documents, and this note does not pretend otherwise.

Supporting detail that is real: PART C already generates documents
("Documents → docx/xlsx/pptx/pdf, attached to the mirror item and linked in the outcome
note") with no naming rule anywhere in the runbook or any skill, so every filename to date
has been improvised per-run. The vault has had a naming standard since day one
(schema §5: `kebab-case.md`, date-led when time-bound) — documents simply never inherited
it. This skill carries that existing convention across the boundary rather than inventing
a second one.

## Inputs / outputs

- **Reads**: the document about to be produced (its subject/purpose), the task that
  generated it, and the Haven outcome note's date.
- **Writes**: nothing of its own — it returns a filename string that the producing step
  uses. It is a naming authority, not a file mover.
- **Format**: `YYYY-MM-DD-subject-in-kebab-case.ext`, mirroring schema §5 so a document
  and its note sort together and read the same way.

## Surfaces

None directly. It is called in-process by whatever produces a document (PART C, the
investor loop's data-room builds, meeting-prep). It posts nowhere and touches no channel.

## Safety envelope

The narrowest of any skill in the system: it returns a string. It reads nothing sensitive,
writes no file, sends nothing, and cannot rename anything that already exists — renaming a
delivered document would break the links in outcome notes and mirror items, which is the
standing "never overwrite existing content" rule.

## Chains with

PART C (document production), `samira-investor` (data-room files), `meeting-prep` (prep
docs), `samira-report-result` (the outcome note that links the file).

## Open question for Lemar

Whether the date should be the **document's subject date** (the meeting, the invoice
period) or the **creation date**. They differ often enough to matter — an invoice from
July filed in August. The proposal defaults to subject date when one is unambiguous, else
creation date, and says so; if he wants it always creation date that is a one-line change
before promotion (Option 2 on the card).

## Sources
- slack: #skills-lab (`C0BBZ5J8805`) ts `1783694505.201439` — Lemar's request, quoted above
- `haven/vault/_system/schema.md` §5 — the naming convention this extends
- `.claude/routines/samira-atlas-executor.md` PART C — where documents are produced
- Proposal: `.claude/skills-proposed/doc-naming/SKILL.md`
