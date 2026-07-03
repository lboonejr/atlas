---
created: 2026-07-03T00:00-04:00
updated: 2026-07-03T12:00-04:00
domain: project
type: brief
status: active
tags: [haven, handoff, save-point, atlas, samira, integration]
source: claude
---

# Handoff: Haven ↔ Atlas & Samira integration (save point)

**Date:** 2026-07-03 ET
**Project:** Haven (the source of truth)
**This save point covers:** locking how Haven changes the way Atlas and Samira
work, *before* any existing skills are rerouted into it.
**Prior save point:** Google Doc handoff "Obsidian Second Brain (vault-keeper)
into Atlas and Samira", 2026-07-02
(https://docs.google.com/document/d/1rs_AJHHVi_t6QfrpbwolRpshOe-myD2iNUPLg4R2Spk/edit)

---

## Purpose

Freeze the current state of Haven and define the **one thing to settle next**:
how Haven interacts with Atlas and Samira. Lemar's call — this is a big change,
so we design the Atlas/Samira integration first and reroute the skills after.
Nothing outward-facing gets wired without approval.

---

## The mental model (locked)

- **Haven** is the country — the source of truth. Plain Markdown + YAML, no tool
  lock-in, so it is portable across models and platforms.
- **Atlas** is the orchestrator (the boss who dispatches jobs on the hourly loop).
- **Samira** is the executor (the worker who does them).
- **Skills report to Haven.** The write path is `haven-capture`; the filing is
  `vault-keeper`.
- **Surfaces (revised 2026-07-03):** Haven owns truth, *why*, **and** live status
  (via the `status` field). **Google Calendar** is the alarm clock — the only
  thing that fires timed alerts. **Monday is being retired.** Drive owns binaries.

---

## What is built so far (state at this save point)

In the `atlas` repo, branch `claude/haven-knowledge-system-4tp4sa`, draft **PR #25**:

- **`haven/vault/`** — the portable seed vault: folder circuit
  (`00-Inbox` … `90-Archive`, `_daily`, `_templates`, `_system`), the
  authoritative schema (`_system/schema.md`), five templates, home note, two
  domain maps, and seeded entities (Cuzzie's, The Station, Harvest Moon, Dutchie).
- **`haven/README.md`** — the portability contract + defaulted open questions.
- **`skills/vault-keeper/SKILL.md`** — Samira executor; hourly Inbox sweep, files
  by frontmatter, flags what it cannot file. Files + internal status only.
- **`skills/haven-capture/SKILL.md`** — shared write path; any skill/source drops
  a properly-framed note into `00-Inbox`.
- **Live demo note** — `30-Station/dutchie-account-transfer.md` (pulled from the
  Samira board, item 12331860092) plus `50-Reference/Entities/dutchie.md`, proving
  a cross-domain item sleeps in one folder while linking to both stores + the
  shared vendor.

**Not built / not wired yet:** live Obsidian Sync on the Atlas server, Monday
board registration, the `atlas`-channel → Inbox capture wiring, and any migration
of existing skills into Haven.

---

## Decisions locked this session (2026-07-03)

- **Monday: demote, then retire (staged).** Leave it running as-is now; build the
  Haven-native replacements, prove they work, migrate the live items, then turn
  Monday off. No cold cutover, no gap.
- **Notifications reroute to Google Calendar.** Calendar becomes the alarm clock:
  time-bound work gets put on the calendar, which fires native 24/7 phone alerts
  independent of Claude and the loop. This closes the "alerts stop when the system
  is down" gap that dropping Monday would otherwise open.
- **The live board moves into Haven.** An Obsidian Dataview query over the `status`
  field (`active / parked / done / archived`) rebuilds the at-a-glance board
  inside the vault, replacing the Monday board view.
- **Consequence:** the old vault↔Monday sync problem dissolves. There is no second
  source of truth to reconcile — only a one-way push from Haven to Calendar for
  anything time-bound.

**Proposed schema addition (confirm before building):** add an optional `due`
field (ISO 8601 ET) to the frontmatter standard. Notes with a `due` are what the
loop pushes onto Google Calendar. Optional and additive — it does not touch the
controlled lists.

---

## The decision for this leg: Atlas/Samira integration FIRST

Settle these before rerouting any skills. These are the real integration
questions — each one changes how Atlas and Samira behave day to day:

1. **Where the live vault physically runs.** Stand up Obsidian headless Sync on
   the Atlas server (git repo as fallback) so the worker and Lemar's phone share
   one always-current vault. *Needs Lemar's hands* (install, Sync login, billing).
2. **Registration.** Register `vault-keeper` on the Atlas Skills & Accounts
   Registry board (`18419004984`) as a Samira executor. Confirm the Samira
   operational board (`18418714876`) is where its status is tracked.
3. **The capture path.** Confirm Atlas routes `atlas`-channel captures into
   `00-Inbox` as `.md` with frontmatter applied on the way in, via the
   `haven-capture` contract. Define who stamps `domain`/`type` at capture time.
4. **Calendar push (replaces the old Monday-sync question).** Define the one-way
   path: which notes get a Google Calendar event (proposal: any note with a `due`
   field), who creates/updates it, and how a note and its event stay matched
   (e.g. store the event id back in the note). One direction only — Haven → Calendar.
5. **Cadence.** Confirm the hourly loop runs the vault pass **seven days a week**,
   overriding the old Saturday-silent rule for this job (Lemar's latest lean = yes).
6. **Status surfaces.** Confirm `vault-keeper` posts internal status to `#decisions`
   / the Open Items canvas, and never outward.
7. **Monday retirement plan.** Sequence the wind-down: build the Dataview board +
   Calendar alerts, verify, migrate the ~25 live Samira-board items into Haven,
   then switch Monday off.

---

## Then (next leg, not now): reroute the skills

Once the above is locked, point existing skills at Haven via `haven-capture`.
Suggested order (unchanged from prior handoff):
1. Narrative-heavy first — `star-craft`, meeting notes.
2. Financial — `chase`.
3. The rest — `reggie`, `scout`, `shortlist`.

Each skill keeps its current job and simply *also* drops a Markdown record into
`00-Inbox`. That is the migration; it is deliberately after the integration is settled.

---

## Guardrails (carry forward)

- `vault-keeper` and `haven-capture` never send email, never post publicly, never
  touch money. Files + internal status only.
- Never guess frontmatter to force a note out of the Inbox. A stuck note is the
  system working.
- Keep the vault portable — no Claude/Monday/Slack syntax inside vault notes.
  All platform wiring lives in the skills.
- Monday keeps the timed alerts and scans. The vault does not replicate them.

---

## References

- Repo / branch: `atlas` · `claude/haven-knowledge-system-4tp4sa` · draft PR #25
- Boards: Atlas Skills & Accounts Registry `18419004984`; Samira operational
  `18418714876`
- Slack: `atlas` (input), `decisions` (action). Samira Slack ID `U0BC5UTHYG4`
- Schema (authoritative): `haven/vault/_system/schema.md`
- Portability contract: `haven/README.md`
- Prior save point: the 2026-07-02 Google Doc handoff (linked above)

---

## Open / pending (still unanswered from the prior handoff)

- **Personal** — keep `10-Personal` flat, or split (father's entities / finance /
  writing)? Currently flat.
- **Projects** — top-level `40-Projects`, or nest under each business? Currently
  top-level.
- **Legal** — keep under `50-Reference/Entities`, or promote to a top-level folder
  given the two active evictions? Currently under Entities.
- **Mobile read** — confirmed path is the Obsidian app (mobile Drive connector
  cannot read `.md`). Accepted.
