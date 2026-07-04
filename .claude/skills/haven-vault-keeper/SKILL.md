---
name: haven-vault-keeper
description: >
  The vault's filing clerk — standing job #1 in Samira's hourly loop, run before
  calendar-sync and before any of her Slack/email work. It sweeps Haven's 00-Inbox,
  and for every note with complete, valid frontmatter it files the note
  deterministically by domain/type/status per the schema's filing rules, and stubs an
  entity note for any recurring counterparty that lacks one. Any note with a missing,
  blank (UNRESOLVED), or out-of-list controlled field it LEAVES in the Inbox and
  surfaces to Lemar — it never guesses a label to move a note out. Use it whenever the
  Inbox needs clearing: Samira's scheduled scan, or on demand ("file the inbox", "run
  vault-keeper", "what's stuck in Haven?"). It files and reports only — it never edits
  note bodies, never touches the calendar, never sends.
---

# haven-vault-keeper — the filing clerk

Notes land in `00-Inbox` from `haven-capture`. This skill is the sweep that moves each
valid one to its home and leaves each invalid one exactly where it is, flagged. It is
the enforcement half of "capture-first".

The single rule it never breaks:

> **A note files itself only when its frontmatter is complete and valid. A note that
> is missing, blank, or out-of-list on any controlled field stays in the Inbox and is
> surfaced to a human. Never guess a label to move a note out.**

A stuck note is the system working. The gap is the enforcement mechanism (schema §3/§4).

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it at the start of a run
(#decisions channel ID for the stuck-notes card lives there). Constants:
- Vault: `haven/vault/` on repo `lboonejr/atlas`, default branch. Rulebook:
  `haven/vault/_system/schema.md` — it wins over this file if they ever disagree.
- Transport: GitHub connector. Pull → move/rename + touch `updated` → commit → push.
- DO NOT write the retired local reader copy `C:\Users\lemar\Vaults\Haven`.

---

## The sweep, step by step

1. **Pull** the latest `haven/vault/`. List every `*.md` in `haven/vault/00-Inbox/`.
   (Ignore any seeded `*-example-*` note.)

2. **Validate** each note's frontmatter. It is FILE-READY only if ALL six required
   fields are present and every controlled field holds an allowed value:

   | field    | must be one of |
   |----------|----------------|
   | `created`| present, ISO 8601 |
   | `updated`| present, ISO 8601 |
   | `domain` | `personal` · `cuzzies` · `station` · `project` · `reference` · `legal` |
   | `type`   | `note` · `meeting` · `decision` · `task` · `reference` · `entity` · `log` · `brief` |
   | `status` | `active` · `parked` · `done` · `archived` · `awaiting-decision` |
   | `tags`   | present (may be empty `[]`) |
   | `source` | `slack` · `gmail` · `monday` · `drive` · `voice` · `claude` · `manual` |

   Any field absent, blank, still marked `# UNRESOLVED`, or out-of-list → the note is
   **NOT file-ready.** Do not fix it, do not guess. It stays.

3. **File the ready notes** by the deterministic rules (schema §4), in this order:

   a. **`status: archived`** → `90-Archive/`, **preserving the domain path** it would
      otherwise take.

   b. Otherwise **file by `domain`:**
      - `personal`  → `10-Personal/`, and if `area` is set → `10-Personal/<Area>/`
        (capitalized). Missing `area` is NOT a gap — file to the root.
      - `cuzzies`   → `20-Cuzzies/`
      - `station`   → `30-Station/`
      - `project`   → `40-Projects/<project>/` (from the note's project tag/slug; if no
        project is named, leave it and surface — "which project?" is a controlled gap)
      - `reference` → `50-Reference/`, and if `type: entity` → `50-Reference/Entities/`
      - `legal`     → `60-Legal/`

   c. **Inside a business domain** (`cuzzies`, `station`), sort by `type`:
      `meeting` → `<domain>/meetings/` · `decision` → `<domain>/decisions/` · else root.

   d. **Touch `updated`** on any note you moved. Never touch `created`. Never edit the body.

   e. **Never move `_daily` notes.**

4. **Stub missing entities** (schema §6). While filing, when a note's body or tags name a
   recurring counterparty — a vendor, lender, bank, service, or person — that has no note
   in `50-Reference/Entities/`, CREATE a stub there from `_templates/entity.md`: two lines
   (Kind, which domains it serves, what it is) is enough; `domain: reference`,
   `type: entity`, `status: active`. Never edit the referring note's body to add the link
   — the stub existing is what makes future `[[wiki-links]]` resolve. Skip one-off names;
   stub things that will recur.

5. **Commit and push**: `vault-keeper: filed N, parked M (+E entities)`.

## What vault-keeper must NOT do
- Never set, change, or guess a controlled field to make a note filable.
- Never edit a note's body or its `created`. Never delete a note (archiving = moving to
  `90-Archive`, driven by a `status: archived` that a human/Atlas set).
- Never write the local reader copy; never touch the calendar, Monday, or Slack beyond
  the one surfacing card.

---

## Surfacing the stuck notes (the human hand-off)

Everything left in the Inbox after a sweep is either brand-new (fine) or **stuck on a
controlled gap**. Post/refresh **ONE** #decisions card titled
`🟡 Haven Inbox — N notes need a label`, one line per stuck note: the title + the
exactly-one thing missing (`domain?`, `type?`, `which project?`) + its repo path. Update
the existing card in place; never one ping per note; never escalate a long-stuck note
beyond the card — it is simply waiting on Lemar.

## Report (for Samira's digest)
Return `filed F · parked/stuck P · new-this-scan N · entities-stubbed E`, naming the
parked notes for the card.

## Worked example
Inbox holds three notes: a valid `domain: cuzzies, type: task` invoice note → files to
`20-Cuzzies/` (and "Harvest Moon" gets an entity stub if missing); a valid
`domain: station, type: meeting` → `30-Station/meetings/`; one with blank `domain` →
stays, listed on the card as `confirm-count-before-paying-2425 · domain?`.
Result: `filed 2 · stuck 1 · new 0 · entities 1`. Lemar taps a domain; next sweep files
it. No guessing anywhere.
