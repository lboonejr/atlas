---
created: 2026-07-03T00:00-04:00
updated: 2026-07-03T00:00-04:00
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
- **Monday** is being retired. It is no longer a source of truth; do not write
  new truth to it. It stays running only until the Haven-native board and the
  Calendar alerts are proven, then it is switched off.

### Conflict resolution
- Disagreement about **anything** → the vault wins. Downstream surfaces
  (Calendar, and Monday while it lingers) are renderings; the next sync corrects
  them to match Haven.

---

## 2. The folder circuit

```
00-Inbox        everything lands here first, unfiled
10-Personal     life, finances, housing, vehicles, writing
20-Cuzzies      Cuzzie's ops, with meetings/ and decisions/ subfolders
30-Station      The Station ops, with meetings/ and decisions/ subfolders
40-Projects     cross-cutting or multi-phase work, one subfolder each
50-Reference    evergreen reference, plus Entities/
   Entities/    businesses, vendors, people, accounts, legal (canonical, cross-domain)
90-Archive      anything archived, original domain path preserved
_daily          one log note per day, YYYY-MM-DD, append-only
_templates      note, meeting, decision, entity, daily
_system         this schema, the home note, and the maps of content
```

**Principle: folders are for humans, frontmatter is for the machine.**
Cross-domain objects — a vendor serving both stores, a person, a legal matter —
live in `50-Reference/Entities`, never trapped under one business.

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
| `domain` | `personal`, `cuzzies`, `station`, `project`, `reference` |
| `type`   | `note`, `meeting`, `decision`, `task`, `reference`, `entity`, `log`, `brief` |
| `status` | `active`, `parked`, `done`, `archived` |
| `source` | `slack`, `gmail`, `monday`, `drive`, `voice`, `claude`, `manual` |

### Optional fields

These are **not** part of the six required fields — a note files itself without
them, and their absence never sends a note to the human. They exist so the note
can drive downstream projections.

| field              | meaning |
|--------------------|---------|
| `due`              | ISO 8601 with ET offset. Present only when the note is time-bound. Any note with a `due` is picked up by `haven-calendar-sync` and projected onto Google Calendar. Truth lives here; the calendar is only a rendering of it. |
| `calendar_event_id`| Machine-managed. Written back by `haven-calendar-sync` after it creates the event, so the same note is never double-booked. Do not set it by hand. |

A note with **complete, valid** frontmatter files itself. A note **missing or
malformed** frontmatter stays in `00-Inbox` until a human fixes it. That gap is
the enforcement mechanism, not a bug — never guess a label to move a note out.

---

## 4. The filing rules (deterministic)

Applied to every note in `00-Inbox` that has complete, valid frontmatter:

1. **File by `domain`:**
   - `personal`  → `10-Personal/`
   - `cuzzies`   → `20-Cuzzies/`
   - `station`   → `30-Station/`
   - `project`   → `40-Projects/<project>/`
   - `reference` → `50-Reference/` (if `type: entity`, → `50-Reference/Entities/`)
2. **Inside a business domain (`cuzzies`, `station`), sort by `type`:**
   - `meeting`  → `<domain>/meetings/`
   - `decision` → `<domain>/decisions/`
   - anything else → the domain root
3. **Anything `status: archived`** → `90-Archive/`, **domain path preserved**
   (e.g. an archived Cuzzie's meeting lands at `90-Archive/20-Cuzzies/meetings/`).
4. **Touch `updated`** on any note you changed.
5. **Never move `_daily` notes.** They are append-only.

A note missing or failing frontmatter validation is **left in `00-Inbox`** and
surfaced to a human. No guessing, ever.

---

## 5. Naming

- Files: `kebab-case.md`. Lead with a date when the note is time-bound
  (`2026-07-03-harvest-moon-invoice.md`); otherwise a stable slug
  (`cuzzies.md`, `the-station.md`).
- Daily notes: `_daily/YYYY-MM-DD.md`, one per day, append-only.
- Entities: one canonical file per real-world thing in `50-Reference/Entities`.
  Everything else links to it; it is never duplicated under a business folder.

---

## 6. Links, not copies

Reference an entity or decision by wiki-link (`[[cuzzies]]`, `[[2026-07-03-...]]`)
rather than pasting its contents. One fact, one home. This keeps Haven consistent
and keeps the graph navigable in Obsidian.
