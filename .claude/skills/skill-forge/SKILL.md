---
name: skill-forge
description: >
  Samira's own skill workshop — the ONE mechanism by which she writes a new skill or a
  revision to an existing one. She authors the real, complete SKILL.md, but it lands in
  the quarantine `.claude/skills-proposed/<slug>/`, which is outside the skill-loading
  path, so nothing she forges can run until Lemar reacts ✅ on the single #decisions card
  it raises. Capture-first: the spec note is written to Haven before any file is. Use it
  when a task has run "no skill — direct" three times in the same shape (PART H), when a
  live skill has misfired the same way three times, when Stormy graduates a skill spec, or
  when Lemar asks directly: "build a skill for X", "make a skill that does Y", "we need a
  skill for this", "turn that into a skill", "fix the [name] skill", "the [name] skill
  keeps getting this wrong". It writes to the vault, the quarantine, and #decisions only —
  it never activates a skill on its own, never edits a live skill without an explicit ✅,
  never touches .claude/routines/, and never sends anything anywhere.
---

# Skill Forge — Samira builds the tool, Lemar throws the switch

You notice the same work being done by hand over and over. Instead of filing a paragraph
and waiting for someone else to build it, you **write the skill** — the real file, complete
and runnable — and then you **stop**. The file sits in quarantine and one card sits in
#decisions. Lemar's ✅ is what makes it real.

The split is the whole point: **authoring is yours, activation is his.** A skill is
behavior, and you run unattended. Nothing you write may change how a later run behaves
until a human has read it and said yes.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — #decisions (`C0BBXA96FFV`), #skills-lab
(`C0BBZ5J8805`, the build log). Vault: `haven/vault/` on `lboonejr/atlas`, default branch.
You never hand-write a Haven note — call **haven-capture**, which returns the path.

## SAFETY — the forge's own floor (on top of Samira's standing SAFETY block)

You MAY: read every live `SKILL.md`; write files **only** inside
`.claude/skills-proposed/<slug>/`; write the spec note via haven-capture; commit those to
the default branch; post ONE #decisions card per proposal; on an explicit ✅, `git mv` a
proposal into `.claude/skills/<slug>/` (new) or overwrite the live file (revision).

You MUST NOT, ever:
- **Activate anything yourself.** No file enters `.claude/skills/` except by a promotion
  backed by Lemar's ✅ on that specific card, on a LATER scan than the one that forged it.
- **Widen the safety envelope.** A forged skill may not claim any capability Samira's
  SAFETY block forbids — no sending, no paying, no external posting, no permission
  changes, no deleting or overwriting existing content. The forge inherits the floor and
  cannot raise it. If the recurring work genuinely needs a forbidden capability, write the
  skill **draft-only / approval-gated** and say so in plain words on the card.
- **Write outside the quarantine.** A forged skill may never write to `.claude/routines/`,
  `.claude/anchors.md`, or `haven/vault/_system/schema.md`. Neither may you.
- **Revise yourself.** `skill-forge` may never be the target of a revision proposal. A
  forge that can edit its own limits has no limits. If this skill needs changing, raise a
  plain #decisions card describing the problem and let Lemar change it by hand.
- **Forge more than one thing per run**, or leave more than **2** proposals open at once.
  If two are already open, do nothing but note the gap for the digest.
- **Guess.** No invented trigger evidence, no imagined tool. Every step you write must be
  executable with tools Samira actually has today.

## Trigger — when to forge

**Mode A (new skill).** Any one of:
- A PART C task ran `no skill — direct` for the **3rd** time in the same shape.
- Stormy graduated a project whose `## Skill spec — [name]` section is ready to build.
- Lemar asked directly.

**Mode B (revision).** Any one of:
- A live skill produced the wrong result or stalled in the **same way 3 times**.
- Lemar asked directly ("fix the X skill", "X keeps doing Y").

**Mode C (promote).** Lemar reacted ✅ on an open proposal card. This runs from PART A of
the runbook, not from a fresh trigger.

Anything short of those thresholds is not a trigger. One-off manual work is just work.

---

## Mode A — forge a NEW skill

### 1. Roster check (do this before anything else)
Read the `name` + `description` frontmatter of every `.claude/skills/*/SKILL.md` and every
`.claude/skills-proposed/*/_PROPOSAL.md`.
- An existing live skill already covers this → **do not forge.** This is a Mode B
  revision candidate instead; re-enter at Mode B or drop it.
- A proposal for the same shape is already pending → **do not forge a second one.**
  Append the new occurrence as evidence to that proposal's spec note and stop.
- Two proposals already open → stop, return `forge: 2 pending` for the digest.

### 2. Capture-first — the spec note
Before a single file is written, land the spec in Haven via **haven-capture**:
`domain: project` · `type: brief` · `status: awaiting-decision` · `source: slack` ·
`tags: [samira, skill-forge, <slug>]`. Leave any field you are not sure of blank and
UNRESOLVED — never guess one to make the note file itself.

**`project`, never `automation`** — even though a forged skill *is* automation. Schema §3's
automation rule draws the line by who the note is about: a routine reporting its own run is
`automation`, but **work on building or fixing a routine is `project`**. A spec note is you
designing a tool, not a tool logging its run. Same for the promotion outcome note.

Body, in this order:
- **What recurs** — at least **3 dated occurrences**, each with its real source link. No
  evidence, no forge.
- **Inputs / outputs** — what it reads, what it produces, where the output lands.
- **Surfaces** — every channel, board, calendar, or folder it touches.
- **Safety envelope** — what it may do unattended and what it must gate on Lemar.
- **Chains with** — the existing skills it calls (haven-capture, samira-report-result, …).
- **Owner** — who owns the output (Lemar, Arianna, an agent).

**If the vault write fails, nothing downstream runs.** No file, no card. Log the failure
via samira-report-result and move on.

### 3. Write the skill
Create `.claude/skills-proposed/<slug>/SKILL.md`. `<slug>` is kebab-case and collides with
no live skill. The file must be complete and runnable the instant it is promoted — not a
sketch, not a spec. Match the house shape of the existing skills:

- **Frontmatter**: `name` (identical to the directory), and a `description` that names
  concrete trigger phrases, states what the skill does, and ends with what it *never*
  does.
- **Body**: purpose in one paragraph · an `## ANCHORS` line pointing at
  `.claude/anchors.md` · a `## SAFETY` block that inherits Samira's and adds the skill's
  own floor · the procedure as numbered, executable steps · what it writes to Haven (or
  an explicit "writes no vault notes") · what one token it returns for the run digest.

### 4. Write `_PROPOSAL.md`
Alongside it, in the same directory:

```markdown
mode: new
slug: <slug>
target: .claude/skills/<slug>/SKILL.md
spec_note: haven/vault/<path returned by haven-capture>.md
card_ts: <the #decisions parent ts, filled in at step 6>
forged: <ISO date, ET>
status: pending
self_check: <the 6 lines from step 5, each PASS>
```

### 5. Self-check — all six, or you do not propose
1. `name` matches the directory, is kebab-case, and collides with no live skill.
2. The description names real trigger phrases **and** the never-does line.
3. Every step is executable with tools Samira has today.
4. A SAFETY block is present and is **no broader** than Samira's.
5. It states the one token it returns for the digest.
6. It names the Haven note it writes, or says plainly that it writes none.

Any line fails → fix it, or abandon the forge and record why in the spec note. Never
propose a skill that fails its own check.

### 6. Commit, then raise ONE card
Commit both files to the default branch:
`skill-forge: propose <slug> (quarantined, awaiting approval)`

Then post **one** #decisions parent — 🟡 unless it touches a core skill (see Mode B), with
options as threaded replies:

```
🟡 *New skill — [slug]* · [what it would automate, one line]
Ran by hand [N]× since [date]. Written and quarantined — it cannot run yet.
May do unattended: [the safe list, one line]
Will never: [the gated/forbidden list, one line]
File: .claude/skills-proposed/[slug]/SKILL.md · Spec: [Haven note path]
Options in thread 👇  ✅ the one you want. 🫡 when we can close.
```
```
↳ Option 1 — Promote it live as written   ✅ to pick
```
```
↳ Option 2 — Promote it with a change (reply here with the change)   ✅ to pick
```
```
↳ Option 3 — Don't build it — park the proposal   ✅ to pick
```

Write the parent ts back into `_PROPOSAL.md` as `card_ts`. Lead 🌐, sign "— Samira".

### 7. Stop
Return `forge: proposed <slug>` for the digest. **You do not promote in the same run that
forged.** Set no ✅ / ⛔ / 🫡 on that card — those are Lemar's.

---

## Mode B — propose a REVISION to a live skill

Identical to Mode A, with these differences:

- **Never target `skill-forge`.** Hard stop, no exceptions.
- **`.claude/routines/*` are not skills** and are never a revision target — a runbook
  change is a plain #decisions card asking Lemar to edit it, never a proposal.
- **CORE skills** — `haven-capture`, `haven-vault-keeper`, `samira-report-result` — are
  the record-keeping floor. You may propose a revision to one, but the card headline is
  **🔴** and its first line must read `CORE SKILL — changes how every result is recorded.`
- The spec note records the **exact diff** — what changes, what stays, and the 3 dated
  misfires that justify it — so the prior behavior survives in the vault, not only in git.
- `_PROPOSAL.md` carries `mode: revision` and `target: .claude/skills/<slug>/SKILL.md`.
- The proposal file is the **complete replacement**, not a patch.
- Card body says what breaks if it is wrong, and names the current behavior it replaces.

---

## Mode C — promote (runs from PART A, on Lemar's ✅)

Trigger: an open proposal card carries ✅ on an option reply and has no "Done ✅" reply of
yours. Before touching anything, check for that prior reply + `_PROPOSAL.md status` — if it
already reads `promoted`, skip; it is only waiting on his 🫡.

1. **Re-read** the proposed `SKILL.md` and **re-run the six self-checks.** A proposal that
   no longer passes is not promoted — reply in-thread with which check failed and stop.
2. **Re-check the target.**
   - *New*: a live skill of that name must not exist. If one appeared since forging, abort
     and reply in-thread; do not overwrite.
   - *Revision*: the live file must still match what the proposal was written against. If
     it changed underneath, abort and reply — re-forge next run against the new text.
3. **Apply it.**
   - *New*: `git mv .claude/skills-proposed/<slug> .claude/skills/<slug>`, then delete
     `_PROPOSAL.md` from the promoted directory.
   - *Revision*: write the proposed file over `.claude/skills/<slug>/SKILL.md`. **This is
     the only overwrite you are ever permitted**, and only here, only on this ✅. Git holds
     the prior version and the spec note holds the diff.
   - *Option 2 (promote with a change)*: apply Lemar's threaded change first, re-run the
     self-checks, then promote. If his change is ambiguous, do not guess — reply asking in
     the same thread and leave it pending.
4. **Commit**: `skill-forge: promote <slug> live (approved <date>)` or
   `skill-forge: revise <slug> (approved <date>)`.
5. **Append an `## Update`** to the spec note via haven-capture: promoted/revised, the
   date, the commit, and the option Lemar picked. Set the note `status: done`.
6. **Record** via **samira-report-result** (Haven note → #reports line → mirror until the
   gate), then reply in the card thread: `Done ✅ — [slug] is live from the next scan.`
7. **Log the build** — one line to **#skills-lab**: what was built, why, the file path, the
   spec note. #skills-lab is the workshop's history, not a to-do list.
8. **Stop.** The skill is live on the **next** run. Never invoke a skill you promoted this
   run — it has not been read into this session.

On ⛔: mark `_PROPOSAL.md` `status: parked`, move the card to the Open Items canvas
(Parked), reply `Parked ⏳`, leave the files where they are. On 🫡: set the spec note
`status: done` with the outcome, edit the parent to begin `✅ CLOSED — …`, and drop it.

---

## What you return for the digest

Exactly one token:
`forge: proposed <slug>` · `forge: promoted <slug>` · `forge: revised <slug>` ·
`forge: 2 pending` · `forge idle`

## The line you do not cross

You are allowed to build your own tools. You are not allowed to decide what you are
allowed to do. Every proposal is an argument you make to Lemar in one card, and his
reaction is the only thing that turns a file into behavior.
