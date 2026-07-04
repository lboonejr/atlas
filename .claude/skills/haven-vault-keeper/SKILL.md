---
name: haven-vault-keeper
description: >
  The vault's filing clerk — standing job #1 in Samira's hourly loop, run before
  calendar-sync and before any of her Slack/email work. It sweeps Haven's 00-Inbox,
  and for every note with complete, valid frontmatter it files the note
  deterministically by domain/type/status per the schema's filing rules. Any note with
  a missing, blank (UNRESOLVED), or out-of-list controlled field it LEAVES in the Inbox
  and surfaces to Lemar — it never guesses a label to move a note out. Vault writes
  (moving/renaming notes inside the vault, touching `updated`) are allowed unattended.
  Use it whenever the Inbox needs clearing: Samira's scheduled scan, or on demand
  ("file the inbox", "run vault-keeper", "what's stuck in Haven?"). It files and reports
  only — it never edits note bodies, never touches the calendar, never sends.
---

# haven-vault-keeper — the filing clerk

Notes land in `00-Inbox` from `haven-capture`. This skill is the sweep that moves each
valid one to its home and leaves each invalid one exactly where it is, flagged. It is
the enforcement half of "capture-first": capture writes fast and loose into the Inbox;
vault-keeper is the deterministic gate that keeps the rest of the vault clean.

The single rule it never breaks:

> **A note files itself only when its frontmatter is complete and valid. A note that
> is missing, blank, or out-of-list on any controlled field stays in the Inbox and is
> surfaced to a human. Never guess a label to move a note out.**

A stuck note is the system working. The gap is the enforcement mechanism (schema §3/§4).

## HAVEN VAULT ANCHORS

```
Repo:            lboonejr/atlas   ·   branch: claude/star-crash-thread-context-2npbr   ·   PR #25 merged 2026-07-03
Vault (canonical):  haven/vault/          Schema (rulebook):  haven/vault/_system/schema.md   Skills (canonical): .claude/skills/
Transport:          GitHub connector. Pull latest → move/rename notes + touch `updated` → commit → push.
DO NOT WRITE the local reader copy at C:\Users\lemar\Vaults\Haven (no .git, may drift).
Surface stuck notes to Lemar in Slack #decisions  C0BBXA96FFV  (one card, batched — see "Surfacing").
```

Read `haven/vault/_system/schema.md` at the start of a sweep if anything about the
rules is unclear — that file wins over this one if they ever disagree.

---

## The sweep, step by step

1. **Pull** the latest `haven/vault/`. List every `*.md` in `haven/vault/00-Inbox/`.
   (Ignore the seeded `*-example-*` note if it is still present — it is documentation.)

2. **Validate** each note's frontmatter. It is FILE-READY only if ALL six required
   fields are present and every controlled field holds an allowed value:

   | field    | must be one of |
   |----------|----------------|
   | `created`| present, ISO 8601 |
   | `updated`| present, ISO 8601 |
   | `domain` | `personal` · `cuzzies` · `station` · `project` · `reference` · `legal` |
   | `type`   | `note` · `meeting` · `decision` · `task` · `reference` · `entity` · `log` · `brief` |
   | `status` | `active` · `parked` · `done` · `archived` |
   | `tags`   | present (may be empty `[]`) |
   | `source` | `slack` · `gmail` · `monday` · `drive` · `voice` · `claude` · `manual` |

   Any field absent, blank, still marked `# UNRESOLVED`, or carrying a value not in its
   list → the note is **NOT file-ready.** Do not fix it, do not guess. It stays.

3. **File the ready notes** by the deterministic rules (schema §4), in this order:

   a. **`status: archived`** → `90-Archive/`, **preserving the domain path** it would
      otherwise take (an archived Cuzzie's meeting → `90-Archive/20-Cuzzies/meetings/`).
      Archived is checked first because it overrides domain placement.

   b. Otherwise **file by `domain`:**
      - `personal`  → `10-Personal/`, **and if the optional `area` is set** (`money`/`health`/
        `home`/`family`) → `10-Personal/<Area>/` (capitalized). A `personal` note with NO
        `area` files to the `10-Personal/` root — missing `area` is NOT a gap; never park a
        personal note for lacking one.
      - `cuzzies`   → `20-Cuzzies/`
      - `station`   → `30-Station/`
      - `project`   → `40-Projects/<project>/`  (use the note's project tag/slug for
        `<project>`; if no project subfolder is named, leave the note in the Inbox and
        surface it — "which project?" is a controlled gap, not a guess to make)
      - `reference` → `50-Reference/`, **and if `type: entity`** → `50-Reference/Entities/`
      - `legal`     → `60-Legal/`

   c. **Inside a business domain** (`cuzzies`, `station`), sort by `type`:
      - `meeting`  → `<domain>/meetings/`
      - `decision` → `<domain>/decisions/`
      - anything else → the domain root

   d. **Touch `updated`** to now (ET offset) on any note you moved. Never touch
      `created`. Never edit the body.

   e. **Never move `_daily` notes** — they are append-only and live outside the Inbox
      anyway; if one somehow appears in the Inbox, leave it and flag it.

4. **Commit and push** the moves: `vault-keeper: filed N, parked M`.

## What vault-keeper must NOT do
- Never set, change, or guess a controlled field to make a note filable. Its job is to
  move notes the schema can already place, not to complete them.
- Never edit a note's body or its `created`.
- Never delete a note. (Archiving = moving to `90-Archive`, driven by `status: archived`
  that a human/Atlas set — vault-keeper only *acts on* that status, never sets it.)
- Never write the local reader copy; never touch the calendar (that is the next standing
  job) or Monday/Slack beyond the one surfacing card.

---

## Surfacing the stuck notes (the human hand-off)

Everything left in the Inbox after a sweep is either brand-new (arrived this scan, fine)
or **stuck on a controlled gap**. For the stuck ones, surface them to Lemar so he can
resolve each with one tap — but do it quietly and batched, never one ping per note.

- Post/refresh **ONE** `#decisions` card (`C0BBXA96FFV`) titled e.g.
  `🟡 Haven Inbox — N notes need a label`, listing each stuck note as a line: the note
  title, and the exactly-one thing missing (`domain?`, `type?`, `which project?`). Link
  each note by its repo path. This follows Samira's #decisions contract — one parent,
  Lemar answers by editing the note (or telling Samira the value) and the next sweep
  files it. Do not spam a card if the same notes were already surfaced and nothing
  changed; update the existing card in place.
- A note that has sat stuck across **many** sweeps is not an error to retry louder — it
  is simply waiting on Lemar. Keep it on the card; do not escalate beyond the one card.

## Report (for Samira's digest)
Return counts so Samira can fold them into her run digest:
`filed F · parked/stuck P (needing a label) · new-this-scan N`. Name the parked notes so
they show up on the #decisions card, not buried in a tally.

---

## Worked example
Inbox holds three notes at sweep time:

1. `2026-07-03-harvest-moon-invoice-2425.md` — `domain: cuzzies`, `type: task`, all six
   valid → files to `20-Cuzzies/` (task is not meeting/decision, so domain root), touch
   `updated`, commit.
2. `2026-07-03-station-vendor-meeting.md` — `domain: station`, `type: meeting`, valid →
   files to `30-Station/meetings/`.
3. `confirm-count-before-paying-2425.md` — `domain:` is blank/UNRESOLVED → stays in
   `00-Inbox`, added to the "Haven Inbox — needs a label" card as
   `confirm-count-before-paying-2425 · domain?`.

Result: `filed 2 · stuck 1 · new-this-scan 0`. The card shows the one note; Lemar taps a
domain; next sweep files it. No guessing anywhere.

---

## Scope note (schema edits — now landed 2026-07-03)
The previously-deferred schema edits are now in `haven/vault/_system/schema.md` and active
above: the `legal` domain + top-level `60-Legal/` folder + filing rule, and the split of
`10-Personal` into `Money`/`Health`/`Home`/`Family` via the optional `area` field. vault-keeper
now files against **six** domains (`personal`, `cuzzies`, `station`, `project`, `reference`,
`legal`) and routes personal notes by `area` when present. `area` is OPTIONAL — a personal note
without it is never stuck; it just files to the `10-Personal/` root. Still NOT in scope here:
the done=filed-note cutover for the loop skills, the Haven Dataview board, and the Monday
switch-off. Do not pre-implement rules the schema does not yet state.
