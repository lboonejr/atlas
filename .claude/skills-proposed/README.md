# `.claude/skills-proposed/` — the quarantine

Every skill Samira writes herself lands **here first**, never in `.claude/skills/`.

This directory is deliberately **outside the skill-loading path**. Nothing in it is
discoverable or runnable by any agent — a proposal is a file on disk and a card in
`#decisions`, and that is all it is until Lemar approves it.

## Shape of a proposal

```
.claude/skills-proposed/<slug>/
  _PROPOSAL.md   ← the machine-readable header: mode, target, spec note, card ts, self-check
  SKILL.md       ← the real, complete skill file, ready to run the moment it is promoted
```

`_PROPOSAL.md` is what later scans read to know a proposal is pending, what it targets,
and whether it has already been promoted. Never delete it — on promotion it moves into
the archive line of the spec note and the directory goes away with `git mv`.

## Lifecycle

```
skill-forge writes here  →  ONE #decisions card  →  Lemar reacts
                                                     ✅ → promoted to .claude/skills/<slug>/ (next scan)
                                                     ⛔ → parked; the directory stays, the card closes
                                                     🫡 → closed; recorded in the spec note
```

**A promoted skill is live on the run AFTER promotion, never the run that promotes it.**
That is the same buffer rule PART B/PART C already use, applied to behavior changes.

## Rules that make the quarantine mean something

- Samira may write **only** inside `.claude/skills-proposed/<slug>/`. She never writes
  into `.claude/skills/` except by the promotion `git mv`, and only on an explicit ✅.
- A proposed skill may never claim a capability Samira's own SAFETY block forbids. The
  forge inherits the floor; it cannot widen it.
- A proposed skill may never write to `.claude/routines/`, `.claude/anchors.md`, or
  `haven/vault/_system/schema.md`.
- `skill-forge` may never propose a revision to **itself**.
- At most **2** proposals may be open at once, and at most **1** forge action per run.

The full procedure lives in `.claude/skills/skill-forge/SKILL.md`.
