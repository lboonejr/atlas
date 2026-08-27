---
created: 2026-08-27T10:12:00-04:00
updated: 2026-08-27T14:03:00-04:00
domain: automation
type: log
status: done
tags: [samira, vault-open-items-audit, pulse-dashboard, reports-contradiction-scan]
source: slack
---

# Vault open-items count — 214 vs ~37 audit (Lemar approved Option 1, 2026-08-27)

**Trigger:** reports-contradiction-scanner card "Vault open-items count discrepancy
(214 vs ~37), unresolved for 7+ digests" (#decisions ts `1787833175.960449`). Lemar
replied "Option 1 let's move forward" (ts `1787837849.122359`) — run a full open-items
audit, same shape as the 8/22 `#decisions` backlog audit
(`haven/vault/40-Projects/samira-skills/2026-08-22-decisions-backlog-audit.md`).

**Method:** read the Pulse-dashboard skill's own spec for the "Atlas — open items"
section (`.claude/skills/pulse-dashboard/SKILL.md` §7, before this note's edit):
"Open Haven notes (frontmatter `status: active | awaiting-decision | parked`,
excluding `type: entity` and `_daily/`/`_system/`), due-dated and oldest first." Then
computed BOTH readings of that sentence against the full vault (615 notes, git sha
`e4001cbb74f36d37ae9b946a6dcc44b8fbb3b362`):

1. **Literal-status-only reading** ("due-dated and oldest first" = a sort key, not a
   filter): every note with `status: active | awaiting-decision | parked`, excluding
   `type: entity` and `_daily/`/`_system/`/`_templates/`, regardless of whether it
   carries a `due` field → **213 notes** (near-exact match for the reported 214; the
   1-note gap is normal drift in the ~7 hours since that figure was first taken, not a
   counting error).
2. **`due`-required reading** ("due-dated" = a filter, restricting the section to
   notes that actually carry a `due` field): same status/type/path filters, PLUS
   `due` must be present → **37 notes exactly** — matching "prior renders' ~37" to the
   digit.

**Root cause: the skill's own wording was ambiguous between the two readings, and
different Pulse renders on 2026-08-26 landed on different sides of it** (earlier
renders that day showed ~37; the 1:14pm ET render explicitly switched to "a raw
frontmatter scan" and reported 214, flagging the jump itself as a discrepancy without
resolving which reading was correct). Nothing in the vault previously wrote down which
reading was intended.

**Decision (this audit, mirroring the 8/22 precedent — the vault was silent, so this
locks a methodology rather than guessing which existing figure is "right"):** the
`due`-required reading (37) is correct going forward. Rationale: "Atlas — open items"
is Lemar's list of time-bound things to act on, not an inventory of every note that
happens to not be archived — most of the vault's 213 status-active-family notes are
ordinary ongoing reference/vendor/project notes (126 of the 213 are `domain: cuzzies`
alone) that were never meant to surface here. The `due` field is exactly Haven's
existing signal for "this is time-bound" (it's also what drives `haven-calendar-sync`),
so requiring it is both the more sensible product definition and the one that
reproduces the number every render showed before the 1:14pm regression.

**Fix applied this run:** `.claude/skills/pulse-dashboard/SKILL.md` §7 rewritten to
state the `due` requirement explicitly and link back to this note, so a future render
can't independently re-derive the ambiguous reading. No vault notes were changed —
this is a counting-methodology fix, not a data fix.

**Reconciled count for today's Pulse render and future digests:** ~37 open items
(due-dated, active-family, non-entity) — not 214. The 214 figure was a scan bug
(missing due-filter), not a sign of ~180 backlog notes suddenly needing Lemar's
attention.

## Sources
- slack: #decisions `C0BBXA96FFV` ts `1787833175.960449` (card) / `1787837849.122359`
  (Lemar's "Option 1" reply)
- haven/vault/40-Projects/samira-skills/2026-08-22-decisions-backlog-audit.md (method
  precedent)
- haven/vault/40-Projects/samira-skills/2026-08-22-reports-contradiction-scan-log.md
  (twenty-third run — origin of the 214-vs-~37 escalation)
- .claude/skills/pulse-dashboard/SKILL.md (edited this run, §7)
- direct full-vault scan, git sha `e4001cbb74f36d37ae9b946a6dcc44b8fbb3b362`
