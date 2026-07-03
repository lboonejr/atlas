---
name: haven-capture
description: Write a properly-framed Markdown note into the Haven Inbox (00-Inbox) with valid frontmatter, so it can file itself. This is the shared front door every other skill and capture source uses to report to Haven. Triggers when a skill needs to record something into the source of truth, or when the user says "capture this to Haven", "save this to the vault", "log this to Haven".
---

# Haven Capture

The single front door into **Haven** (the source of truth). Any skill, routine,
or capture source that produces something worth remembering calls haven-capture
to drop a note into `haven/vault/00-Inbox/`. The note carries complete, valid
frontmatter, so on the next pass `vault-keeper` files it automatically.

**The one rule of Haven:** every new capture writes to the vault *first*. Monday
and Drive are downstream. haven-capture is how that rule is enforced in practice
— it is the write path other skills report through.

## When to run

- Another skill needs to record an outcome, decision, meeting, or fact into the
  source of truth (e.g. `meeting-runner` finished notes; `chase` confirmed a
  commitment; `star-craft` surfaced a decision).
- The user says "capture this to Haven", "save this to the vault", "log this".
- Atlas routes an `atlas`-channel capture that should become a vault note.

## Procedure

### 1. Read the schema

Read `haven/vault/_system/schema.md` for the current controlled lists and naming
rules before writing. Never hard-code the allowed values from memory — the schema
is authoritative and can change.

### 2. Assemble the frontmatter

Build a complete, valid block. This is the whole job — a note is only useful to
Haven if it can file itself.

```yaml
---
created: <now, ISO 8601 with ET offset>   # written once
updated: <same as created on first write>
domain:  <personal | cuzzies | station | project | reference>
type:    <note | meeting | decision | task | reference | entity | log | brief>
status:  <active | parked | done | archived>   # usually active
tags:    [<open list>]
source:  <slack | gmail | monday | drive | voice | claude | manual>
---
```

Rules for choosing values:
- **Never guess a controlled field.** If `domain`, `type`, or `status` cannot be
  determined confidently, do not fabricate one — see step 5.
- `source` reflects where the capture originated (the calling skill's input),
  not "claude" by default. A starred-email capture is `gmail`; a Slack drop is
  `slack`; a manual note is `manual`.
- `tags` is open — add whatever connects the note (business, project, entity
  slugs). Link entities in the body with `[[wiki-links]]`, don't retype them.

### 3. Choose a filename

`kebab-case.md`, per the schema:
- Time-bound note → lead with the date: `2026-07-03-harvest-moon-invoice.md`.
- Stable thing → a slug: `q3-hiring-plan.md`.
Write it into `haven/vault/00-Inbox/`. If the name collides, append a short
disambiguator; never overwrite an existing Inbox note.

### 4. Write the body

Start with an `# H1 title`, then the substance: context, the decision or fact,
and any open questions. Base the body on the appropriate template in
`_templates/` (note / meeting / decision / entity / daily) when it fits. Keep it
portable — plain Markdown, no tool-specific syntax.

### 5. Handle uncertainty honestly

If you cannot confidently fill a controlled frontmatter field, still write the
note to `00-Inbox`, but **omit the uncertain field**. That deliberately makes the
note un-fileable, so `vault-keeper` will leave it in the Inbox and flag it for a
human to label — which is exactly right. A flagged note beats a mis-filed one.

### 6. Report back to the caller

Return to the calling skill: the path of the note written, its frontmatter, and
whether it is fully fileable or intentionally left for human labeling. Do not
send anything outward — haven-capture only writes to the vault.

## Guardrails

- **Write path only.** haven-capture creates Inbox notes; it does not file them
  (that is `vault-keeper`), send anything, or touch money.
- **Never guess controlled fields** to make a note look complete. Omit-and-flag
  beats mislabel.
- **One fact, one home.** Link to existing entities/decisions instead of copying
  their contents into a new note.
- **Keep Haven portable.** Plain Markdown only — no Claude/Monday/Slack syntax
  inside the note. Platform wiring lives in skills, never in the vault.
