---
created: 2026-08-19T00:28-04:00
updated: 2026-09-11T10:30:00-04:00
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

## Update 2026-09-10T14:10-04:00 — kickoff date set, roadmap needs finalizing

Lemar drop, Convo 2 self-DM (thread ts `1789061736.927349`, reply `1789062477.908009`),
2026-09-10: "Finalize the Camden group licensing roadmap. Start lining everything up. Be
ready to hit the ground running on September 16th, when we will be getting started."
First concrete start date attached to this engagement since infrastructure stood up
2026-08-19 — it has sat at Phase 00 with no client work run through the loop yet (see
State above). Nothing finalized yet; the roadmap itself, and what "lining everything up"
requires, still needs to be worked as a Camden Launch card per the overlay before 9/16.

## Update 2026-09-11T10:30-04:00 — 8/25 confirmed, real target is 9/21 not 9/16

Convo 1 card (thread ts `1789063833.434589`), Lemar's reply: the 8/25 Jamil meeting did
happen but the engagement letter was **not signed**. On 9/5 the group pushed again —
"ready to go after the 15th," letter going to them 9/16 (not the 5th as Lemar first
expected). Lemar now targets **launch with the Camden Group on 9/21**, wants to be ready
earlier if they move sooner, and named four concrete infrastructure asks: a well-defined
file system, a backup location/system, a roadmap/blueprint of the licensing + entity-
formation process, a way to track progress, and doing the whole engagement inside
Samira's Loop.

Three of the four are already standing infrastructure, not new builds — flagging the
gap rather than re-building what exists:
- **File system**: the Drive tree (00 Command Center / 01 Client-Facing / 02 Internal,
  phase subfolders 00-05) already exists, stood up 2026-08-19 — see "Where everything
  lives" above.
- **Progress tracking**: the Working Log Doc already serves this, plus this Convo 1
  card thread.
- **Work entirely within Samira's Loop**: already the mechanism — #camden-launch +
  Convo 1 cards + the loop's eight lenses is how every prior Camden item has run.

Genuinely not yet built: a **backup** location distinct from Drive's own version
history (Drive folder is the only copy right now), and the actual **content** of the
roadmap/blueprint — Phase 00-05 exist as folder structure, not as a drafted checklist
a client-facing person could follow. Still no signed engagement letter and still no
first milestone in the Working Log since 8/24. Flagged both gaps and the open
signature question back on the Convo 1 card rather than drafting the full roadmap
against an unconfirmed engagement — a licensing roadmap promising a timeline to a
client who hasn't signed is a scope/outcome-language risk under the overlay's six
gates.

## Sources
- repo: `.claude/projects/camden-dispensary-launch-project-instructions.md` (PRs #68, #70, #71)
- repo: `.claude/anchors.md`, section "Camden Dispensary Launch"
- drive: 00 Command Center `1waKvkdsc9yr2ZAu_BhY8EneONKvtDhcM` (Working Log, proposal, handoffs)
- slack: #camden-launch `C0BRZT2V89W` · Convo 1 card ts `1789063833.434589`
