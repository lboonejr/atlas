---
created: 2026-07-03T14:45-04:00
updated: 2026-07-03T14:45-04:00
domain: project
type: brief
status: active
tags: [haven, handoff, save-point, atlas, samira, framework, migration]
source: claude
---

# Handoff: rework the Atlas & Samira framework around Haven, then reroute all skills

**Date:** 2026-07-03 ET
**Project:** Haven (the source of truth)
**This save point sets up the NEXT leg:** change the Atlas/Samira framework so
Haven is the backbone, then point every existing skill at Haven.
**Prior save point:** [[2026-07-03-haven-atlas-samira-integration-handoff]]

---

## Where we are now (done this session)

- **Haven is built and pushed** — draft **PR #25** on branch
  `claude/haven-knowledge-system-4tp4sa` in `lboonejr/atlas`.
- **The vault** (`haven/vault/`): folder circuit, authoritative schema
  (`_system/schema.md`) incl. the optional `due` + `calendar_event_id` fields,
  templates, home, maps, seeded entities, and a real cross-domain demo note.
- **Three Haven skills**, all registered on board `18419004984`:
  - `vault-keeper` (item 12440663110) — files the Inbox. Samira executor.
  - `calendar-sync` (item 12440657496) — projects `due` notes to Google Calendar.
    Samira executor. **Verified working 2026-07-03** (test event fired to the
    Haven calendar).
  - `haven-capture` (item 12440680395) — the shared write path into `00-Inbox`.
- **Connectors:** GitHub ✅ (PR reads restored), Google Calendar ✅ (Haven
  calendar `c_383bbf77…935549@group.calendar.google.com` is the write target,
  logged on the registry).
- **Decisions locked:** Monday demote→retire; Google Calendar is the alarm clock;
  the Haven-native board is a Dataview over `status`; conflict rule = the vault
  always wins.

The plumbing exists. The next leg is about the **framework and the skills**, not
new infrastructure.

---

## The goal of the next leg

Make Haven the literal backbone of how Atlas and Samira operate — not a system
that sits beside them, but the ground they stand on. Two ordered phases:

### Phase 1 — Rework the Atlas/Samira framework to fit Haven (do first)

The framework changes, each of which needs a decision before building:

1. **Capture-first becomes law.** Every capture Atlas takes from the `atlas`
   channel writes to Haven `00-Inbox` first (as `.md` with frontmatter, via
   `haven-capture`), *before* it becomes a Monday item or anything else. Define
   who stamps `domain`/`type` at capture time and what happens when they're
   unknown (answer: omit → vault-keeper flags it).
2. **Atlas's dispatch list gains two standing jobs.** The hourly loop now always
   runs `vault-keeper` and `calendar-sync` alongside existing routines. Confirm
   ordering (file the Inbox *before* syncing the calendar, so new `due` notes get
   picked up the same pass).
3. **Samira's definition of "done" moves into Haven.** A job isn't done when it
   posts to Slack; it's done when its outcome is a filed Haven note. Slack/Monday
   become notifications *about* Haven, not the record itself.
4. **The board of record flips.** Stand up the Dataview `status` board inside the
   vault; begin reading operational state from Haven, not the Monday Samira board.
5. **Monday wind-down begins.** Once 1–4 hold and are trusted, migrate the ~25
   live Samira-board items into Haven and switch Monday off (staged, no gap).
6. **Registry stays truthful.** Board `18419004984` remains the map of skills,
   accounts, and IDs — keep it in sync as skills are rerouted.

### Phase 2 — Reroute every skill to report to Haven (do second)

Each existing skill keeps its current job and *additionally* writes a Markdown
record into Haven via `haven-capture`. That is the migration. Full inventory and
proposed order below.

---

## Skill inventory (from registry board `18419004984`) + rerouting order

All of these are registered skills that must eventually report to Haven. Proposed
sequence — narrative/decision-heavy first (highest memory value), then financial,
then operational:

**Wave 1 — narrative & decisions (richest to remember):**
- `star-craft` — starred Gmail triage
- `meeting-runner` — meeting lifecycle
- `shortlist` — capture & process ledger
- `handoff-builder` — cross-platform handoff docs (note: overlaps Haven's own
  handoff pattern — decide whether it writes *into* Haven or is replaced by it)
- `stormy` — idea-baking engine

**Wave 2 — money & commitments:**
- `chase-commitments` — outbound commitments tracker
- `po-payment-recorder` — PO & payment logger
- `order-builder` — menu picks → order
- `inventory-needs` — weekly inventory needs

**Wave 3 — comms & ops:**
- `email-responder` / `samira-email-loop` — reply drafting
- `samira-investor` — investor pipeline
- `samira-car-search` / `Scout` — car hunt
- `samira-report-result` — result landing & #reports
- `task-builder` — admin task composer
- `aaron-exec` — executive assistant
- `reggie-compliance` — compliance officer (evictions/legal — high value)
- `mitch` — dealmaker / promo builder
- `menu-auditor`, `menu-poster` — menu QA & distribution
- `atlas` — the orchestrator skill itself (updates last, once the pattern is set)

For each skill the reroute is small and identical: at the point it produces
something worth remembering, call `haven-capture` with a framed note (domain,
type, source = that skill's channel, and a `due` if time-bound). Don't
deduplicate across skills — each owns its own note.

---

## Open decisions for the framework rework

1. **Capture stamping** — does Atlas stamp `domain`/`type` on the way into
   `00-Inbox`, or does it drop a partial note and let a human/vault-keeper resolve?
2. **`handoff-builder` vs Haven** — Haven now holds handoffs natively (this file
   is one). Retire `handoff-builder`, or keep it as the *generator* that writes
   into Haven?
3. **Board flip timing** — how long do Haven's Dataview board + Calendar run in
   parallel with Monday before we trust them enough to migrate and switch off?
4. **Write-approval at go-live** — calendar/Monday writes need the connector
   healthy; confirm the loop runs where those writes are permitted.
5. **Carry-over structure questions** (still open): Personal flat vs split;
   Projects top-level vs nested; Legal promoted to top-level (given evictions).

---

## Guardrails (carry forward)

- Every capture writes to the vault first. Haven is the source of truth; Calendar
  and Monday are downstream renderings.
- Keep the vault portable — no Claude/Monday/Slack/Google syntax inside vault
  notes. All platform wiring lives in skills and on the registry board.
- Skills that touch money/email/public posts keep their existing approval gates;
  reporting to Haven never bypasses them.
- Never guess controlled frontmatter to force a note out of the Inbox.

---

## References

- Repo / branch: `lboonejr/atlas` · `claude/haven-knowledge-system-4tp4sa` · draft PR #25
- Registry board: `18419004984` (skills, accounts, IDs). Samira operational board:
  `18418714876` (being retired).
- Slack: `atlas` (input) `C0BBWHCJUV9`, `decisions` (action) `C0BBXA96FFV`. Samira
  Slack ID `U0BC5UTHYG4`. Open Items canvas `F0BDLSHD8JD`.
- Haven calendar: `c_383bbf77e22b75080885c4eb36e5e7e005e59c17a17bff751ece8e0e23935549@group.calendar.google.com`
- Schema (authoritative): `haven/vault/_system/schema.md`
- Portability contract: `haven/README.md`
- Prior save point: [[2026-07-03-haven-atlas-samira-integration-handoff]]
