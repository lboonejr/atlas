---
name: haven-vault-keeper
description: >
  The vault's filing clerk — standing job #1 in Samira's hourly loop, run before
  calendar-sync and before any of her Slack/email work. It sweeps Haven's 00-Inbox,
  and for every note with complete, valid frontmatter it files the note
  deterministically by domain/type/status per the schema's filing rules, and stubs an
  entity note for any recurring counterparty that lacks one. Any note with a missing,
  blank (UNRESOLVED), or out-of-list controlled field it LEAVES in the Inbox and
  surfaces to Lemar — it never guesses a label to move a note out. It also runs a
  whole-vault integrity pass every sweep (schema §4.5), repairing mechanically broken
  frontmatter — stray lines above the opener, a missing opener, losslessly-decodable
  base64 — anywhere in the vault, so format defects get fixed same-day instead of
  accumulating outside the Inbox where nothing was checking them. Use it whenever the
  Inbox needs clearing: Samira's scheduled scan, or on demand ("file the inbox", "run
  vault-keeper", "what's stuck in Haven?", "check the vault for broken notes"). It
  files, repairs containers, and reports — it never rewrites prose, never fills in a
  controlled value, never touches the calendar, never sends.
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

That rule is about **values**, not containers. A note can also be broken *mechanically* —
a stray line above the `---` opener, a missing opener, a base64-encoded file — and those
have one correct repair with no judgment in them. Step 0 repairs those across the whole
vault (schema §4.5). Repairing a container never licenses filling in a value.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it at the start of a run
(#decisions channel ID for the stuck-notes card lives there). Constants:
- Vault: `haven/vault/` on repo `lboonejr/atlas`, default branch. Rulebook:
  `haven/vault/_system/schema.md` — it wins over this file if they ever disagree.
- Transport: GitHub connector. Pull → move/rename + touch `updated` → commit → push.
- DO NOT write the retired local reader copy `C:\Users\lemar\Vaults\Haven`.

---

## The sweep, step by step

0. **Integrity pass — the WHOLE vault, not just the Inbox** (schema §4.5). Filing only
   ever looks at `00-Inbox`, so a note that got past this sweep once was never checked
   again and stayed broken forever. Read the frontmatter block of **every** `*.md` under
   `haven/vault/` (the block only — not the whole body; this is cheap).

   Flag a note as mechanically broken when any of these hold:
   - line 1 is not `---` (stray content above the opener, or the opener is missing)
   - the file's content is base64 rather than Markdown
   - the frontmatter block uses CRLF line endings
   - there is no frontmatter block at all

   Then repair **only** what is uniquely determined:

   | Defect | Repair |
   |--------|--------|
   | Stray lines above the opener | Delete them so `---` is line 1 |
   | Opener missing, fields + closing `---` intact | Insert `---` at line 1 |
   | Base64 file | Decode in place — **only past the lossless gate below** |
   | `_daily` note with no block at all | Rebuild from `_templates/daily.md`, dated from the filename, disclosure comment in the body |
   | CRLF in the block | Normalize to LF |

   **The lossless gate (base64).** Decode only if ALL THREE hold: decoded bytes are valid
   UTF-8, re-encoding reproduces the file byte-for-byte, and the result starts with a valid
   frontmatter block. Any failure ⇒ the decode is lossy ⇒ **flag it and write nothing.** A
   partial decode that silently drops bytes is worse than the corruption it "fixed."

   **Then validate values on every note too — flag, never fix.** Field validation used to
   run only on Inbox notes (step 2), so a *filed* note could sit for months missing required
   fields or holding a value in no controlled list, and nothing noticed. On every note in the
   vault, check: all six required fields present · every controlled field in-list · `domain`
   consistent with where the note actually sits. Never invent a missing `created`, never map
   an out-of-list value onto the nearest legal one (a `source: gdrive` that "obviously means
   `drive`" is still Lemar's call), and **never re-file a note to match its `domain`** — a
   mismatch means either the frontmatter or the location is wrong, and which is a judgment
   call.

   **Skip `_templates/` for value checks** — its `{{domain}}`/`{{source}}` placeholders are
   correct by design and would otherwise be reported out-of-list every sweep. Check their
   containers normally. Skip seeded `*-example-*` notes entirely. A check that cries wolf
   hourly teaches the reader to ignore it, which is how these defects survived.

   **Do NOT repair — flag and leave:**
   - a missing / blank / `UNRESOLVED` / out-of-list **controlled value** (unchanged law)
   - a **required field absent entirely** on a filed note, or a `domain`/location mismatch
   - base64 that fails the lossless gate
   - **a note that already records a decision not to repair it** — if the body says a prior
     run or a human examined the defect and chose to leave it, that decision stands. Do not
     relitigate it and do not overwrite what it protected.
   - a missing block **outside** `_daily`, where values can't be derived from a template
   - anything with more than one plausible repair

   **`_daily` is a narrow carve-out.** Its frontmatter block may be repaired; **not one
   line below the closing `---` may be touched**, and the file is still never moved. The
   append-only law protects the day's logged entries — a broken block is the container
   around them, not an entry. On a reconstruction, set `created`/`updated` to the filename
   date at `00:00` ET and disclose it with an HTML comment stating the block was
   reconstructed, when, and that the times are nominal. Never pass synthesized precision
   off as recovered.

   **Every repair gets logged** (step 5) — file, defect, action. A silent repair is
   indistinguishable from corruption. Never change `created`; never touch prose.

1. **Pull** the latest `haven/vault/`. List every `*.md` in `haven/vault/00-Inbox/`.
   (Ignore any seeded `*-example-*` note.)

2. **Validate** each note's frontmatter. It is FILE-READY only if ALL six required
   fields are present and every controlled field holds an allowed value:

   | field    | must be one of |
   |----------|----------------|
   | `created`| present, ISO 8601 |
   | `updated`| present, ISO 8601 |
   | `domain` | `personal` · `cuzzies` · `station` · `project` · `reference` · `legal` · `automation` |
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
      - `automation`→ `70-Automation/<routine>/` (routine slug from the note's tags —
        e.g. `inbox-janitor` → `70-Automation/inbox-janitor/`). Unlike `project`, a
        missing slug is **NOT** a gap: file to the `70-Automation/` root and move on.
        Never re-read a run log's contents to reclassify it into a business domain.

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

5. **Commit and push**: `vault-keeper: filed N, parked M, repaired R (+E entities)`.

   **Itemize every repair** in the digest and the `_daily` run journal — one line each:
   file · defect · what was done. Never let a repair count stand in for the list; a silent
   repair is indistinguishable from corruption.

   **Escalate only what's new.** An unrepairable defect (lossy decode, prior decision
   stands) never goes away, so re-flagging it every hour is noise — and digest fatigue is
   what let these defects hide in the first place. Report new-or-changed defects in full;
   carry everything already known and accepted as a bare count:

   ```
   integrity: 401 notes · repaired 0 · known 1 (_daily/2026-08-01.md, lossy b64, decided 8/1)
   ```

   Never omit the line entirely — a quiet pass and a skipped pass must not look the same in
   the journal.

## What vault-keeper must NOT do
- Never set, change, or guess a **controlled value** to make a note filable. Step 0's
  container repairs grant no licence here — a repaired container with a missing `domain`
  is still a stuck note.
- Never edit a note's **prose**, or its `created`. Never delete a note (archiving = moving
  to `90-Archive`, driven by a `status: archived` that a human/Atlas set).
  - The sanctioned exceptions, and the only ones: the step-0 container repairs (frontmatter
    block and file encoding), and appending an `## Update` section per schema §7.
- Never write a base64 decode that fails the lossless gate — flag it instead.
- Never overwrite what a documented prior decision chose to protect, and never relitigate
  that decision because this run would have judged it differently.
- Never touch a line below the closing `---` in a `_daily` note, and never move one.
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
