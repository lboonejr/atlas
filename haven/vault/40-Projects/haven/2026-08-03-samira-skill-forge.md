---
created: 2026-08-03T00:00-04:00
updated: 2026-08-03T00:00-04:00
domain: project
type: decision
status: done
tags: [samira, skill-forge, atlas-system, routine-change, safety]
source: claude
---

# Samira can build her own skills — forge + approval gate

Lemar asked to change Samira so she can make skills herself. He picked the autonomy
level and the scope explicitly; this note is the record of what was chosen and why.

## The decision

**Autonomy — "build it, you approve it."** Samira now writes the real, complete
`SKILL.md` herself. It lands in the quarantine `.claude/skills-proposed/<slug>/`, which
sits outside the skill-loading path, so nothing she forges can run. She raises ONE
`#decisions` card; Lemar's ✅ promotes it live on a LATER scan. Rejected: full autonomy
(a bad skill would silently change every future run before he saw it) and
proposal-only (the status quo — she could describe a gap but never close it).

**Scope — new skills, plus proposed revisions to existing ones.** She may create a
skill that doesn't exist, and when a live skill misfires the same way 3 times she may
draft a complete replacement — but a live file is only ever overwritten on an explicit
✅ on that revision's card.

## What actually changed

- **NEW** `.claude/skills/skill-forge/SKILL.md` — the workshop. Three modes: A (forge a
  new skill), B (propose a revision), C (promote, on Lemar's ✅, from PART A).
- **NEW** `.claude/skills-proposed/README.md` — the quarantine and its rules. Verified
  empirically: the skill loader registered `skill-forge` and registered nothing from
  `skills-proposed/`.
- `.claude/routines/samira-atlas-executor.md` — SAFETY block rewritten (the blanket "no
  creating skills mid-run" became a precise "author yes, activate never"); PART A gained
  the promotion branch; **PART H rewritten** from "post a candidate to #skills-lab, you
  never build skills yourself" into the forge trigger + floor; digest gained a `forge:`
  token.
- `.claude/routines/stormy-ideation.md` + `.claude/skills/stormy/SKILL.md` — skill specs
  now route to `skill-forge` instead of a manual `skill-creator` run. Stormy still writes
  specs only, never files.
- `.claude/routines/daily-brief.md` — Dawn's prohibition kept, repointed at PART H.
- `.claude/anchors.md` — `#skills-lab` (`C0BBZ5J8805`) changed role: it is now the build
  LOG (one line per promoted skill), not where candidates are proposed. Candidates are a
  real file plus a `#decisions` card.
- `PORTABILITY.md` — the platform-neutral loop gained a FORGE step, with the rule any
  replacement platform must preserve.

## The guardrails, and what each one is for

| Guardrail | What it prevents |
|---|---|
| Quarantine outside the loading path | A forged skill running before a human reads it |
| Promotion only on a LATER scan | Forging and self-activating in one unattended run |
| Inherits Samira's SAFETY floor, can never widen it | A skill that grants itself sending/paying/posting |
| Never writes `.claude/routines/`, `anchors.md`, or the schema | Rewriting the runbook that constrains it |
| **skill-forge may never revise itself** | A forge editing its own limits |
| Core skills (haven-capture, vault-keeper, report-result) need a 🔴 CORE card | Quietly breaking the record-keeping Lemar would notice problems through |
| ≥3 dated occurrences as evidence, or no forge | Skill sprawl from one-off work |
| 1 forge/run, 2 open proposals max | A flood of cards |
| 6 self-checks, re-run at promotion time | Promoting something that no longer validates |

The line the skill states in its own words: *she is allowed to build her own tools; she
is not allowed to decide what she is allowed to do.*

## Open / next

- Nothing forged yet — PART H returns `forge idle` until a real 3rd-occurrence trigger
  fires. First real proposal is the thing to watch: check the card reads clearly and the
  six self-checks were honest.
- `#skills-lab` has old candidate-style posts in it from the previous PART H. They are
  history now; no cleanup done.

## Update 2026-08-03 — rebased on the `automation` domain

`main` landed the new `automation` domain (schema §3) while this was in review. It raises a
question the forge would otherwise have to guess at every run: a spec note is *about*
automation, so should it be `domain: automation`?

No — and the schema already settles it: *"work on building or fixing a routine is still
`project`."* The line is who the note is **about**. A routine reporting its own run is
`automation`; designing the tool is `project`. Made explicit in `skill-forge` step 2 so a
later run doesn't re-derive it and land spec notes in `70-Automation/`. This note's own
`domain: project` is correct on the same rule.

Also added the `.claude/CHANGELOG.md` entry — that convention landed on `main` in the same
window, and a PART H cutover is exactly the kind of narrative it is for.

## Sources
- `.claude/skills/skill-forge/SKILL.md` — the procedure
- `.claude/skills-proposed/README.md` — the quarantine
- `.claude/routines/samira-atlas-executor.md` — SAFETY, PART A, PART H, digest
- Prior state: [[2026-07-26-samira-self-evaluation]] (PART H under the old rule found no
  skill gap that scan)
