---
created: 2026-07-03T00:00-04:00
updated: 2026-07-04T12:00-04:00
domain: reference
type: reference
status: active
tags: [haven, schema, system, rulebook]
source: manual
---

# Haven Schema — the rulebook

This is the single source of truth for how Haven is structured. Every routine,
every skill, and every human that touches the vault obeys this file. If a rule
lives anywhere else and contradicts this file, this file wins.

Haven is deliberately plain: folders and Markdown with YAML frontmatter, nothing
else. Any tool that can read a text file can read Haven. That is the whole point
— see `../../README.md` for the portability contract.

---

## 1. The one rule that makes it real

**Every new capture writes to the vault first.** Everything else is downstream.

- **Haven owns** truth, context, decisions, the narrative of every thread, **and
  live status** (via the `status` field).
- **Google Calendar** is the alarm clock — the only thing that fires timed alerts.
  It is a one-way *projection* of any note that carries a `due` date, never a
  source of truth. (See `haven-calendar-sync`.)
- **Drive owns** binary files: PDFs, invoices, Excel menus, images.
- **Monday is being retired — gate reviews 2026-07-11.** It is not a source of
  truth; do not write new truth to it. The mirror runs only until the gate (7 clean
  days: every result has a matching Haven note, zero discrepancies), then it drops.

### Conflict resolution
- Disagreement about **anything** → the vault wins. Downstream surfaces
  (Calendar, and Monday while it lingers) are renderings; the next sync corrects
  them to match Haven.

---

## 2. The folder circuit

```
00-Inbox        everything lands here first, unfiled
10-Personal     life & family, with Money/ Health/ Home/ Family/ sub-areas (see `area` below)
20-Cuzzies      Cuzzie's ops, with meetings/ and decisions/ subfolders
30-Station      The Station ops, with meetings/ and decisions/ subfolders
40-Projects     cross-cutting or multi-phase work, one subfolder each
50-Reference    evergreen reference, plus Entities/
   Entities/    businesses, vendors, people, accounts (canonical, cross-domain)
60-Legal        active legal matters (evictions, filings, counsel threads) — domain `legal`
70-Automation   run logs from unattended routines (Basil the Inbox Janitor, and any
                future bot doing workspace admin) — domain `automation`, one subfolder
                per routine. Append-only operational records, not business content.
90-Archive      anything archived, original domain path preserved
_daily          one log note per day, YYYY-MM-DD, append-only — ALSO the run journal:
                Samira appends her run digest here at the end of every scan
_templates      note, meeting, decision, entity, daily
_system         this schema, the home note, and the maps of content
```

**Principle: folders are for humans, frontmatter is for the machine.**
Cross-domain objects — a vendor serving both stores, a person, an account —
live in `50-Reference/Entities`, never trapped under one business. (An active
legal *matter* is its own domain, `legal` → `60-Legal/`; the counsel or
counterparty behind it can still have a canonical entity note in Entities.)

---

## 3. The frontmatter standard

Every note carries this block. This is what lets notes file themselves.

```yaml
---
created: 2026-07-03T14:32-04:00   # ISO 8601 with ET offset. Written once, never changed.
updated: 2026-07-03T14:32-04:00   # Touched on every edit.
domain: cuzzies                    # controlled — see below
type: note                         # controlled — see below
status: active                     # controlled — see below
tags: []                           # open list, connect ideas freely
source: manual                     # controlled — see below
due: 2026-07-08T09:00-04:00        # OPTIONAL. Present only when the note is time-bound.
---
```

`domain`, `type`, and `status` are **controlled lists** so filing is
deterministic. `tags` stays **open** so ideas connect freely. `source` records
where the note came from.

| field    | allowed values |
|----------|----------------|
| `domain` | `personal`, `cuzzies`, `station`, `project`, `reference`, `legal`, `automation` |
| `type`   | `note`, `meeting`, `decision`, `task`, `reference`, `entity`, `log`, `brief` |
| `status` | `active`, `parked`, `done`, `archived`, `awaiting-decision` |
| `source` | `slack`, `gmail`, `monday`, `drive`, `voice`, `claude`, `manual` |

**The automation rule:** a note whose substance is *an unattended routine reporting its
own run* — what Basil archived last night, what a future bot swept — is
**`domain: automation`**, and the routine stamps it itself. These are the bots doing
workspace admin; their run logs are not Cuzzie's content, not personal content, and not
project work. Draw the line by **who the note is about**: the routine's own execution →
`automation` → `70-Automation/<routine>/`. Work on *building or fixing* a routine (a
design decision, a bug, a handoff) is still `project` → `40-Projects/<project>/`. An
automation note that surfaces a business item worth acting on does not change domain —
it stays `automation`, and the actionable item gets its own note in the right domain.

**The decision rule:** any note whose substance is a decision Lemar made — an option he
picked, an approval he gave, a direction he chose — is **`type: decision`**, never `log`
or `note`. It files to `<domain>/decisions/` and is the record future-you searches for.
A `log` records what happened; a `decision` records what was CHOSEN and why. When a
single event contains both, the decision wins the type.

### Optional fields

These are **not** part of the six required fields — a note files itself without
them, and their absence never sends a note to the human. They exist so the note
can drive downstream projections.

| field              | meaning |
|--------------------|---------|
| `due`              | ISO 8601 with ET offset. Present only when the note is time-bound. Any note with a `due` is picked up by `haven-calendar-sync` and projected onto Google Calendar. Truth lives here; the calendar is only a rendering of it. |
| `calendar_event_id`| Machine-managed. Written back by `haven-calendar-sync` after it creates the event, so the same note is never double-booked. Do not set it by hand. |
| `area`             | **Personal notes only.** One of `money` · `health` · `home` · `family`. When present, vault-keeper files the note into `10-Personal/<Area>/` (capitalized). When absent, the note files to `10-Personal/` root — its absence never sends a note to a human. Ignored on non-`personal` domains. |

A note with **complete, valid** frontmatter files itself. A note whose frontmatter is
**missing a value a human must choose** stays in `00-Inbox` until that human chooses it.
That gap is the enforcement mechanism, not a bug — never guess a label to move a note out.

**Distinguish the container from the values** (this is what §4.5 acts on). A broken
*container* — a stray line above the `---` opener, a missing opener, a base64-encoded
file — has exactly one correct repair and no human judgment in it; the integrity pass
repairs those. A missing or out-of-list *value* — `domain`, `type`, `status`, `source` —
is a judgment call and always waits for a human. Repairing a container is never licence
to fill in a value.

---

## 4. The filing rules (deterministic)

Applied to every note in `00-Inbox` that has complete, valid frontmatter:

1. **File by `domain`:**
   - `personal`  → `10-Personal/` (if `area` is set → `10-Personal/<Area>/`, i.e. `Money`/`Health`/`Home`/`Family`; if `area` is absent, the domain root is a valid home — do NOT treat missing `area` as a gap)
   - `cuzzies`   → `20-Cuzzies/`
   - `station`   → `30-Station/`
   - `project`   → `40-Projects/<project>/`
   - `reference` → `50-Reference/` (if `type: entity`, → `50-Reference/Entities/`)
   - `legal`     → `60-Legal/`
   - `automation`→ `70-Automation/<routine>/` (routine slug from the note's tags, e.g.
     `inbox-janitor`; unlike `project`, a missing slug is NOT a gap — file to the
     `70-Automation/` root, because a run log always has a valid home)
2. **Inside a business domain (`cuzzies`, `station`), sort by `type`:**
   - `meeting`  → `<domain>/meetings/`
   - `decision` → `<domain>/decisions/`
   - anything else → the domain root
3. **Anything `status: archived`** → `90-Archive/`, **domain path preserved**
   (e.g. an archived Cuzzie's meeting lands at `90-Archive/20-Cuzzies/meetings/`).
4. **Touch `updated`** on any note you changed.
5. **Never move `_daily` notes.** They are append-only.

A note whose frontmatter is missing a **value** a human must choose is **left in
`00-Inbox`** and surfaced to a human. No guessing, ever.

---

## 4.5 The integrity pass (whole-vault, every sweep)

Filing only ever looks at `00-Inbox`, so for a long time nothing re-examined a note once
it was filed. Malformed notes therefore accumulated *outside* the Inbox — where the
enforcement mechanism could not see them — and stayed broken indefinitely. The integrity
pass closes that hole: **every sweep checks every note in the vault**, not just the Inbox,
and repairs the mechanical defects same-day.

Cost is small — it reads the frontmatter block of each note, not the whole body.

### Repairable (mechanical, uniquely determined, verifiable)

Apply these silently, then report them in the digest:

| # | Defect | The one correct repair |
|---|--------|------------------------|
| R1 | Stray content above the `---` opener (e.g. a `# --- YAML frontmatter ---` comment) | Delete the stray lines so `---` is line 1 |
| R2 | Opening `---` missing, but the fields and the closing `---` are present and well-formed | Insert the `---` opener at line 1 |
| R3 | File content is base64 rather than Markdown | Decode in place — **only if** the decode is provably lossless (see the gate below) |
| R4 | A `_daily` note with no frontmatter block at all | Rebuild it from `_templates/daily.md`, dated from the filename (see the `_daily` rule below) |
| R5 | CRLF line endings in the frontmatter block | Normalize to LF (whitespace only, never a content change) |

**The lossless gate on R3.** Decode only when all three hold: the decoded bytes are valid
UTF-8, re-encoding them reproduces the file byte-for-byte, and the result begins with a
valid frontmatter block. If any check fails the decode is lossy — **flag it, never write
it.** A partial decode that silently drops bytes is worse than the corruption.

### Also check values vault-wide — flag, never fix

Container checks alone are not enough. Field validation historically ran **only** on Inbox
notes, so a filed note could sit for months missing required fields or holding a value that
is not in any controlled list, and nothing would notice. The integrity pass therefore also
validates, on every note in the vault:

- all six required fields **present** (`created`, `updated`, `domain`, `type`, `status`,
  `tags`, `source`)
- every controlled field holding an **in-list** value
- `domain` **consistent with where the note actually sits** (a `domain: cuzzies` note living
  in `40-Projects/` is one or the other being wrong)

All three are **value** problems: **flag them, never fix them.** Do not invent a missing
`created`, do not map an out-of-list value onto the nearest legal one (a `source: gdrive`
that "obviously means `drive`" is still a human's call, and the discipline is the point),
and do not re-file a note to match its `domain` — a mismatch means either the frontmatter
or the location is wrong and which one is a judgment call. Report and let a human decide.

**Exempt from value validation: `_templates/`.** Template files carry `{{domain}}` /
`{{source}}` placeholders that are correct by design and would otherwise be reported as
out-of-list on every single sweep. Check their *containers* like any other file, but never
their values. (Seeded `*-example-*` notes are likewise skipped, as in step 1.) A check that
cries wolf every hour trains the reader to ignore it — which is how the original defects
survived in the first place.

### Never repairable — flag and leave

- A missing, blank, `UNRESOLVED`, or out-of-list **controlled value**. Unchanged law: the
  note waits for a human. Repairing containers grants no new licence here.
- **Base64 that fails the lossless gate.** Report it and move on.
- **A note that already records a decision not to repair it.** If the body explains that a
  previous run or a human examined the defect and chose to leave it, that decision stands —
  do not relitigate it, and do not overwrite what it protected. Appending is still allowed.
- **A missing frontmatter block outside `_daily`**, where the correct values cannot be
  derived from a template. Flag it.
- **Anything with more than one plausible repair.** Ambiguity means flag, not pick.

### The `_daily` rule (a narrow, deliberate carve-out)

`_daily` notes are append-only and are never moved. The append-only law exists to protect
**the day's logged entries** from being rewritten — a broken frontmatter block is not an
entry, it is the container around them. So inside `_daily`:

- The frontmatter block **may** be repaired (R1, R2, R4, R5).
- **Not one line below the closing `---` may be touched**, ever — not reordered, not
  reworded, not deleted. Appending is the only sanctioned body write, as everywhere else.
- The file is still never moved.

**R4 reconstruction, specifically.** A daily note's controlled fields are fixed by
`_templates/daily.md` (`domain: personal`, `type: log`, `status: active`, `tags: [daily]`,
`source: manual`) and its date is in its filename, so the block is derivable. The *times*
are not: set `created`/`updated` to the filename date at `00:00` ET and **disclose the
synthesis** with an HTML comment in the body recording that the block was reconstructed,
on what date, and that the times are nominal. Synthesized precision must always be visible
as synthesized — never passed off as recovered.

### Hard limits on every repair

- **Never change `created`.** Never invent a controlled value.
- A repair may only touch the frontmatter block or the file's encoding — **never the
  meaning of any prose.**
- **Log every repair** in the sweep digest and the `_daily` run journal: file, defect,
  what was done. A silent repair is indistinguishable from corruption.
- Repairs are idempotent by construction: a repaired note is valid, so it will not
  re-trigger on the next sweep.

### Don't re-escalate what cannot be fixed

An unrepairable defect — a lossy base64 block, a note protected by a prior decision — stays
broken forever, so a pass that runs hourly would surface it hourly. That noise is precisely
what let the original defects hide in plain sight. So:

- A defect already carrying a **recorded decision to leave it** is counted as
  **known/accepted** — a bare tally in the digest, not a fresh escalation.
- **A defect shared by 3+ notes is one pattern, not N findings.** Report it as a single
  line naming the shape and the count (e.g. "6 notes `domain: cuzzies` inside
  `40-Projects/` — one policy call, not 6 repairs"). A pattern almost always means a
  convention needs deciding, not that six notes each need fixing, and listing it six
  times per hour buries the one decision that would clear all six.
- Escalate prominently only what is **new since the last sweep**, or what has changed.
- The tally must never drop to silence, though: `integrity: repaired 0 · known 1` keeps a
  standing problem visible without pretending it is urgent every hour.

---

## 5. Naming

- Files: `kebab-case.md`. Lead with a date when the note is time-bound
  (`2026-07-03-harvest-moon-invoice.md`); otherwise a stable slug
  (`cuzzies.md`, `the-station.md`).
- Daily notes: `_daily/YYYY-MM-DD.md`, one per day, append-only.
- Entities: one canonical file per real-world thing in `50-Reference/Entities`.
  Everything else links to it; it is never duplicated under a business folder.

## 6. Links, not copies

Reference an entity or decision by wiki-link (`[[cuzzies]]`, `[[2026-07-03-...]]`)
rather than pasting its contents. One fact, one home. This keeps Haven consistent
and keeps the graph navigable in Obsidian.

When a note names a recurring counterparty (a vendor, lender, bank, service) that has
no entity note yet, create a stub in `50-Reference/Entities/` (from `_templates/entity.md`,
even two lines is enough) and wiki-link it — a link that resolves is worth ten that dangle.

## 7. Threads: update, don't fragment

One matter, one note. When new information arrives on a matter that already has an
**active** note (same invoice, same deal, same dispute), **append to that note** instead
of creating a sibling:

```markdown
## Update 2026-07-04
[what changed, what was done, what is now blocked/next]
```

Touch `updated` (this is the one sanctioned body edit — appending an Update section
never rewrites existing content). Create a NEW note only for a genuinely new matter, or
when the old one is `done`/`archived` (then wiki-link the old one). Capture tools must
search for an existing active note on the matter before writing a new one.

## 8. Provenance: the `## Sources` section

Platform references — a Slack permalink, a Gmail thread id, a Drive folder link, a
Monday item (while it lasts) — are welcome **as provenance, never as load-bearing
state**. They go in a `## Sources` section at the bottom of the note, one per line:

```markdown
## Sources
- slack: https://…/archives/C0BBXA96FFV/p1783… (decision thread)
- gmail: thread 19f24ea3bd41fa12 (invoice PDF attached)
- drive: https://drive.google.com/… (data room)
```

The note must stand on its own if every link dies: amounts, dates, names, and outcomes
live in the body, not behind the links. Never put an ID in prose that the reader must
dereference to understand the note.
