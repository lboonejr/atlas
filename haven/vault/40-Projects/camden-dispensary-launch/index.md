---
created: 2026-08-19T00:28-04:00
updated: 2026-08-19T00:28-04:00
domain: project
type: reference
status: active
tags: [camden-launch, client-engagement, licensing, samira-loop, index]
source: claude
---

# Camden Dispensary Launch — index

Lemar is advising a client group through New Jersey CRC licensing, from where they stand
today to a facility the Commission has inspected and cleared to open. He is the **advisor,
not the owner**: the group stays the applicant, the owner, and the decision maker. We hold
no equity and no financial interest in their license, deliberately, so their ownership
disclosure stays clean.

This note is the vault's pointer to the engagement. The rules live in the overlay, the live
status lives in the Working Log, and neither is duplicated here.

## The scope line, which is the rule that gets broken first

The engagement **ends at inspection clearance**. It does not include opening the store or
running it. Anything an inspector checks is in scope; anything that makes the store money is
not. Suppliers, banking, menu, pricing, margin, payroll, accounting, hiring, floor training,
opening week, first orders, and delivery are a separate, unpriced engagement called
**opening services**. When a request crosses that line, name it as opening services rather
than absorbing it quietly.

## Where everything lives

| Thing | Where |
|---|---|
| The rules (scope, role, accuracy, voice, gates, fee) | `.claude/projects/camden-dispensary-launch-project-instructions.md` |
| The mechanics it runs on | the **samira-loop** skill, `.claude/skills/samira-loop/SKILL.md` |
| Every channel and folder id | `.claude/anchors.md`, section "Camden Dispensary Launch" |
| Live phase, status, milestones, decision record | the **Working Log** Doc in 00 Command Center (`12JG69I2RWZ9l3rR7AdFZXhyiuM52FEhmqi-52S3OC9Q`) |
| Questions and decisions | **#decisions** `C0BBXA96FFV`, cards titled "Camden Launch" |
| The work (staged prompts, artifacts, outcomes) | **#camden-launch** `C0BRZT2V89W`, private, bot in-channel |
| Client-facing and internal files | Drive root `1oLwp2UkmXX2AgxcxDO6sEfuxWtQUmBs1` → 00 / 01 / 02 |

**Precedence.** The overlay's engagement rules and its safety floor outrank the loop's
mechanics wherever the two disagree. A Camden card is never worked on generic loop rules
alone: read the overlay first.

## Two records, one job each

The **Working Log** is the engagement's source of truth for phase, status, milestones, and
the decision record — the thing a human reads to know where we are. A **Haven note** per
item is the build record: what got built, the pressure-test rounds, the lane, the outcome.
Each links the other, and nothing closes until both exist.

## The six gates

Beyond the loop's eight lenses, nothing on this engagement locks until all six clear: scope
(is it opening services?), authority (is it legal, tax, or accounting advice?), outcome
language (does anything promise a license or a result?), facts (sourced or unknown?),
approvals (planning board site plan vs City resolution of local support, kept separate), and
placement (01 or 02, named to convention, superseding what it replaces).

## Standing hazards

- **Never promise or imply a license or inspection outcome.** The Commission and the City
  decide. Process language only: working toward, preparing, positioning.
- **Not their attorney, not their accountant.** Legal questions route to their counsel.
- **Adult use recreational.** No medical, therapeutic, or health claims, ever.
- **The two approvals are not the same thing.** They hold planning board site plan approval;
  they do NOT hold the City of Camden resolution of local support, and the Commission asks
  for the second.
- **Never quote a number outside the fee schedule.** Opening services is unpriced; if asked,
  we would rather price it once we can see what the operation needs.

## Unknown, and not to be guessed

- The group's name, property address, and contact.
- The planning board approval's conditions and expiration.
- Whether site control is actually executed.

The first two of those are Phase 00 deliverables, so they resolve as the Position Audit runs.

## State

Phase 00, Position Audit. Infrastructure stood up 2026-08-19: Drive tree, Slack channel with
the bot in it, the overlay, and the ids recorded in anchors. No client work has run through
the loop yet. The Working Log carries the live checklist and dates.

## Sources
- repo: `.claude/projects/camden-dispensary-launch-project-instructions.md` (PRs #68, #70, #71)
- repo: `.claude/anchors.md`, section "Camden Dispensary Launch"
- drive: 00 Command Center `1waKvkdsc9yr2ZAu_BhY8EneONKvtDhcM` (Working Log, proposal, handoffs)
- slack: #camden-launch `C0BRZT2V89W`
