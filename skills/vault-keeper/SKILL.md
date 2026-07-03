---
name: vault-keeper
description: Sweep the Haven Inbox and file each note into the vault by its frontmatter, following the Haven schema. Triggers when the user says things like "run vault-keeper", "file the inbox", "sweep Haven", "file my notes", or when Atlas dispatches the hourly vault pass. A Samira executor job.
---

# Vault Keeper

The filing clerk for **Haven** (the source of truth). Each pass, vault-keeper
reads `00-Inbox`, files every note that has complete, valid frontmatter into its
proper folder, and leaves everything else in the Inbox for a human to fix. It
moves files and posts internal status only — it never sends anything outward.

This is a **Samira executor** job. **Atlas** dispatches it on the hourly loop
(8am–6pm, seven days a week — this job overrides the Saturday-silent rule). It is
not a standalone system; it is one recurring job on the existing orchestrator.

The rulebook is the vault's own `_system/schema.md`. If this file and the schema
ever disagree, **the schema wins** — read it first (`haven/vault/_system/schema.md`).

## When to run

Run when Atlas dispatches the hourly vault pass, or when the user asks directly
("run vault-keeper", "file the inbox", "sweep Haven"). Default scope is every
note currently in `00-Inbox`.

## Procedure

### 1. Read the schema, then the Inbox

Read `haven/vault/_system/schema.md` so you are filing against the current rules
(controlled lists and folder mappings can change there without touching this
file). Then list every note in `haven/vault/00-Inbox/`.

If the Inbox is empty, post "Inbox clear, nothing to file" to the internal status
surface and stop.

### 2. Validate frontmatter on each note

A note is **fileable** only if its YAML frontmatter has all of:

- `created`, `updated` — present, ISO 8601 with ET offset.
- `domain` — one of `personal`, `cuzzies`, `station`, `project`, `reference`.
- `type` — one of `note`, `meeting`, `decision`, `task`, `reference`, `entity`,
  `log`, `brief`.
- `status` — one of `active`, `parked`, `done`, `archived`.
- `source` — one of `slack`, `gmail`, `monday`, `drive`, `voice`, `claude`,
  `manual`.

If any controlled field is missing or holds a value outside its list, the note is
**not fileable**. Do not guess a value to make it move. Never invent labels.

### 3. File each fileable note (deterministic)

Apply the schema's filing rules exactly:

1. **By `domain`:**
   - `personal`  → `10-Personal/`
   - `cuzzies`   → `20-Cuzzies/`
   - `station`   → `30-Station/`
   - `project`   → `40-Projects/<project>/` (subfolder named for the project; use
     a `project` tag or the note's stated project — if none is resolvable, treat
     the note as **not fileable** and flag it)
   - `reference` → `50-Reference/` (if `type: entity`, → `50-Reference/Entities/`)
2. **Inside `cuzzies` / `station`, by `type`:**
   - `meeting`  → `<domain>/meetings/`
   - `decision` → `<domain>/decisions/`
   - anything else → the domain root
3. **If `status: archived`** → `90-Archive/`, **preserving the domain path**
   (an archived Cuzzie's meeting → `90-Archive/20-Cuzzies/meetings/`). This rule
   takes precedence over the domain destination.
4. **Touch `updated`** (current ET timestamp) on every note you move or change.
5. **Never touch `_daily`.** Those notes are append-only and never move.

Move by relocating the file (preserve its name). Do not rewrite the body.

### 4. Leave and flag anything not fileable

For each note that failed validation in step 2 (or an unresolvable project in
step 3), **leave it in `00-Inbox`** and record: the filename and the specific
reason (which field is missing or invalid). These go to the human — see step 6.

### 5. Refresh navigation

After filing, update the maps of content and the Open Items so navigation stays
current:

- `_system/maps/20-Cuzzies.md` and `_system/maps/30-Station.md` — refresh the
  "Recent meetings" and "Open decisions" lists from what you just filed.
- The Open Items canvas / decisions surface — reflect newly-flagged notes.

Only edit the generated list sections; leave hand-written content alone.

### 6. Report internally only

Post a concise status to the internal surface (the `decisions` channel or the
Open Items canvas) — never outward:

- How many notes were filed, and where each went (`file → destination`).
- Every note left in the Inbox, with the exact reason it could not be filed, so
  the human can fix the labels. This flag list is the point of the whole pass.
- Any archive moves and any maps refreshed.

## Guardrails

- **Never send email, never post publicly, never touch money.** Files and
  internal status only.
- **Never guess frontmatter** to force a note out of the Inbox. A stuck note is
  the system working, not failing.
- **Never move `_daily` notes.**
- **Do not replicate Monday.** Timed alerts and scheduled scans stay in Monday;
  the conflict rule holds — truth and *why* live in Haven, current status lives
  in Monday.
- **Keep the vault portable.** Never write Claude-, Monday-, or Slack-specific
  syntax into a vault note. Platform wiring lives in this skill, not in Haven.

## Registration & wiring (operational, not part of the vault)

- Register vault-keeper on the **Atlas Skills and Accounts Registry** board
  (`18419004984`) as a **Samira executor** skill.
- Samira operational board: `18418714876`. Samira Slack ID `U0BC5UTHYG4`.
- Two-channel Slack: `atlas` for input, `decisions` for action. Samira owns
  execution.
- Dispatch: Atlas hourly loop, 8am–6pm, seven days a week.
