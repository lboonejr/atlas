---
created: 2026-08-09T10:31-04:00
updated: 2026-08-09T10:31-04:00
domain: project
type: reference
status: active
tags: [account-manager, rolodex, contacts, index, samira, build-ladder]
source: claude
---

# Account Manager (the Rolodex) — build ladder

**This note is the build's state.** The `yaml` block below is the ONE place ladder state
changes — editing a step's `status`/`commit`/`note` and touching `updated` is a sanctioned
machine write, exactly like [[on-button-reopen]]'s index and the investor-pipeline index;
git history preserves every prior state.

> **Read this block first, every time.** Any scan can resume the build with zero prior
> context by reading the ladder, finding the first step that is not `done`, and acting on
> it. Nothing about the build lives in anyone's memory.

## What is being built

A rolodex Samira maintains: every person and every account, in Haven, mirrored to two
Monday boards so Lemar can find anyone the moment a problem hits. Haven is the source of
truth; Monday is the rendering. The plan of record is the approved implementation plan —
this note carries the executable ladder derived from it.

The end state:

- Six new optional frontmatter fields make entity notes machine-queryable.
- Every human gets their own `entity_kind: person` note, `company:` wiki-linking the org.
- A new `account-manager` skill runs as **PART R**, right after the email loop, reusing the
  threads PART D already fetched.
- Two Monday boards — **Contacts** and **Accounts** — rendered from the vault.
- Ask Samira "who do I call about the ADT account?" and get a real answer.

## How this ladder runs

The build drives itself through machinery that already exists — **no runbook change is
needed until step 13**, so the entire vault phase carries zero risk to the live loop.

- PART C already sweeps `#skills-lab` and runs any un-reacted fenced prompt there.
- `BUFFER: nothing staged in this run's PART B may run in this run's PART C` — stage and run
  are always at least one scan apart. That is the pacing.
- *"A message is a RUNNABLE PROMPT only if: no ✅/🫡/🚗/⏳ reaction"* — a staged step runs on
  the next scan **unless Lemar vetoes it** with ⏳ or ⛔.

**Each step's staged prompt ends by staging the next one.** That is what makes the ladder
self-propagating.

### The rules it obeys

1. **One step staged per scan.** Never stage two.
2. **One commit per step**, to `main`, message `account-manager: step N — <what changed>`.
3. **A failed step HALTS the ladder.** Record the failure via `samira-report-result`
   Mode 2, set the step `failed`, do **not** stage the next step, raise ONE #decisions
   parent. Never build on top of a failed step.
4. **A vetoed step (⏳/⛔) pauses the ladder** there — set it `held` and stage nothing.
5. **At a `gate: hard` step**, post ONE #decisions parent carrying the exact proposed diff
   and stage nothing. PART A reads the ✅ on a later scan; the ladder resumes.
6. **At a `gate: content` step**, produce the report and block the same way — the report is
   the deliverable, the write happens in the following step.
7. Every step's outcome lands via `samira-report-result`: Haven note → #reports → ✅ on the
   staged prompt.
8. The existing 3-strike rule stands: third consecutive failure → 🚗 on the source and
   "STUCK — needs Lemar" in #decisions.

### The fence to stage

Staged into `#skills-lab` (`C0BBZ5J8805`), un-reacted:

```
===ATLAS PROMPT START
run:admin-3x — account-manager build, step <N>
Read haven/vault/40-Projects/account-manager/index.md first. Execute step <N>
(<title>) exactly as its `does` field specifies, and nothing beyond it.
Then: set the step's status/commit/note in the ladder, touch `updated`, log via
samira-report-result, and stage step <N+1> un-reacted here — unless step <N+1> is a
gate, in which case post its #decisions parent instead and stage nothing.
===ATLAS PROMPT END===
```

## Guards on the whole build

- **Never store a password, passphrase, PIN, security answer, or 2FA seed** anywhere in the
  vault, a board, or a message. Account numbers, portal URLs, and login usernames are fine
  (existing on-button precedent). Never a full SSN or ID number (runbook Safety).
- **Never delete** a note, a board item, or a board column at any step. Archiving is the
  only sanctioned removal, and only where a step says so.
- **Never guess a controlled value** to move something along — the gap is the enforcement
  mechanism.
- **Off Button (`18424191974`) is a live crisis tool.** Step 22 writes three contact columns
  and the board description. It touches nothing else, ever.

## The ladder

```yaml
harness:
  channel: skills-lab            # C0BBZ5J8805 — see .claude/anchors.md
  pace: one-step-per-scan
  default_gate: veto             # staged steps run next scan unless ⏳/⛔
  on_failure: halt
  commit_prefix: "account-manager: step "

# status: pending | staged | done | held | failed | gated
# gate:   none | hard | content

steps:
  # ---- Phase 1 — Vault (zero risk to the live loop) ----
  - id: 0
    title: "Bootstrap the ladder"
    does: "Create this ledger note. Then stage step 1's #decisions gate card."
    status: done
    gate: none
    commit: null
    note: null

  - id: 1
    title: "Rulebook — schema §1, §3, §4.5 + PORTABILITY"
    does: >
      schema.md §1: replace the "Monday is being retired" bullet (lines 33-35) with the
      rendering-surface bullet and drop "while it lingers" from conflict resolution
      (lines 38-40). schema.md §3: append the six optional fields (entity_kind, serves,
      company, last_contact, last_contact_direction, monday_item_id) to the Optional
      fields table. schema.md §4.5: add entity_kind and serves to the vault-wide
      controlled-value check, stating all six are optional — absence is never a defect,
      an out-of-list value is flagged never fixed. Mirror the field table into
      haven-vault-keeper/SKILL.md and haven-capture/SKILL.md. Update PORTABILITY.md's
      Monday line. Two commits — §1+PORTABILITY, then §3+§4.5+the two skills.
    status: pending
    gate: hard
    commit: null
    note: null

  - id: 2
    title: "Entity template — optional fields + ## Account block"
    does: >
      _templates/entity.md — add the six new fields as commented optional lines, and add
      the '## Account' section with fixed labelled lines (Account # · Portal · Login ·
      Billing owner · Support) plus the never-a-password warning. The template's
      hardcoded controlled values stay untouched.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 3
    title: "Field backfill — batch 1 (30 notes)"
    does: >
      Populate entity_kind and serves on the first 30 notes in 50-Reference/Entities/,
      alphabetically, from their existing prose Kind:/Serves: lines. Map sprawling Kind
      variants to the nearest controlled value and LEAVE THE PROSE LINE UNTOUCHED — it
      carries detail the controlled list drops. Never invent a value; if Kind is absent
      or genuinely ambiguous, leave the field off and list the note in the outcome.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 4
    title: "Field backfill — batch 2 (30 notes)"
    does: "Same as step 3, notes 31-60."
    status: pending
    gate: none
    commit: null
    note: null

  - id: 5
    title: "Field backfill — batch 3 (remaining 22)"
    does: "Same as step 3, notes 61-82. Report any note left without entity_kind."
    status: pending
    gate: none
    commit: null
    note: null

  - id: 6
    title: "First 5 person/company splits"
    does: >
      32 entity notes are company notes with a person's contact info buried in the body.
      Split the FIRST FIVE only — each human gets their own entity_kind:person note with
      company: wiki-linking the org; the company note keeps terms, account refs, and
      relationship facts. Post the five proposed notes to #decisions and stop. Known
      cases include madin-law (Monica + Marco Di Stefano) and jerzey-grown (Jarred
      Freeman). This gate exists so the SHAPE is right before the other 27 run.
    status: pending
    gate: hard
    commit: null
    note: null

  - id: 7
    title: "Person splits — batch 2 (~14)"
    does: "Apply the approved shape from step 6 to the next ~14 company notes."
    status: pending
    gate: none
    commit: null
    note: null

  - id: 8
    title: "Person splits — batch 3 (remaining ~13)"
    does: "Finish the split. Report any company note deliberately left unsplit and why."
    status: pending
    gate: none
    commit: null
    note: null

  - id: 9
    title: "Normalize drifted entity notes"
    does: >
      sun-extractions.md and irs.md abandoned the template body shape (no bold labels, no
      Summary/Key facts/Related headings). Restore the shape WITHOUT rewriting their
      prose. Add the missing 'entity' tag to the ~5 notes lacking it.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 10
    title: "Catch-up stub sweep"
    does: >
      Stub the recurring counterparties named in note filenames but absent from
      50-Reference/Entities/ — Eddie Osefo, Sauchelli/CRC, Jessica Karbon, Dhaval Joshi,
      Jason Klein, PSEG, Karbon, Crum & Forster, Waste Management, and the rest. Two
      lines each is enough (schema §6). Skip one-offs; stub what will recur.
    status: pending
    gate: none
    commit: null
    note: null

  # ---- Phase 2 — Skill and PART R ----
  - id: 11
    title: "Write account-manager/SKILL.md"
    does: >
      Author .claude/skills/account-manager/SKILL.md in house format. File only — it is
      not wired into the runbook, so nothing executes. Five modes (sweep, backfill,
      lookup, manual add/edit, account reconcile), the scanner/dedupe rule, the SAFETY
      block, and the returns contract. See the approved plan for the full spec.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 12
    title: "Register in anchors"
    does: >
      Add a '## Rolodex — Contacts & Accounts' section to .claude/anchors.md with a
      'Runs as | PART R of Samira' row. Board and column IDs are filled in at steps
      19-20; leave them null here rather than inventing them.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 13
    title: "PART R goes live"
    does: >
      Runbook run-order line 72 becomes V → S → A → B → C → D → R → E → Q → G → H → M →
      canvas refresh → P → digest. Add the PART R stanza after PART D in house shape.
      Add the rolodex token to the Digest tally list. Add the PART B guard — a lookup
      question in the capture DM ("who do I call about…", "who's our contact at…") is
      NOT a capture; route it to account-manager lookup mode. The #decisions parent
      carries the SKILL.md and the stanza text for review.
    status: pending
    gate: hard
    commit: null
    note: null

  - id: 14
    title: "Backfill run 1 — report only"
    does: >
      12-month sweep of lemar@cuzziesnj.com plus Google Calendar attendees. Report the
      contacts with 5+ exchanges: count, the full candidate list grouped by proposed
      category, and what was skipped and why. WRITE NOTHING. Post to #decisions and stop.
    status: pending
    gate: content
    commit: null
    note: null

  - id: 15
    title: "Backfill run 1 — execute"
    does: "Write the approved run-1 contacts to the vault. Category Unclassified where undetermined."
    status: pending
    gate: none
    commit: null
    note: null

  - id: 16
    title: "Backfill run 2 — report only"
    does: "Same as step 14 for the 2-4 exchange tail. WRITE NOTHING."
    status: pending
    gate: content
    commit: null
    note: null

  - id: 17
    title: "Backfill run 2 — execute"
    does: "Write the approved tail to the vault."
    status: pending
    gate: none
    commit: null
    note: null

  # ---- Phase 3 — Boards (veto window, per Lemar's gate selection) ----
  - id: 18
    title: "Archive the two dead boards"
    does: >
      Archive 18418845084 (Investor Pitch Tracker — anchors records it RETIRED, replaced
      by the investor-pipeline index) and 18418974601 (Car Search — PART F sunset
      2026-07-21). Archive only; reversible; never delete. This frees board slots on the
      free tier, which caps at 3 and currently holds 5.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 19
    title: "Create the Contacts board"
    does: >
      Groups: Cuzzie's · The Station · Personal · Projects · Unclassified. Columns per the
      approved plan. Define every status column's labels EXPLICITLY at creation and remove
      Monday's Working on it/Done/Stuck defaults. Board description carries the doctrine.
      Record the board and column IDs in anchors.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 20
    title: "Create the Accounts board"
    does: >
      Groups: Utilities & Services · Financial & Lenders · SaaS & Software · Government &
      Regulatory. Columns per the approved plan — Login Username holds a username only,
      never a password. Same label discipline and description doctrine. Record IDs in
      anchors.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 21
    title: "Populate the boards from the vault"
    does: >
      Push every entity note to its board — entity_kind:person to Contacts, anything with
      an '## Account' section to Accounts — and write monday_item_id back to each note.
      Idempotent: a note that already carries monday_item_id is updated, never re-added.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 22
    title: "Off Button reconciliation"
    does: >
      Refresh Off Button's three contact columns (text_mm5q9s0w Contact Name,
      email_mm5q4zpb Contact Email, phone_mm5qa4sc Contact Phone) from the rolodex, and
      note the split in the board description — its debt columns stay canonical there.
      COLUMN VALUE WRITES ONLY. Never touch an item's other fields, never delete an item,
      never delete a column. This board is a live crisis tool.
    status: pending
    gate: none
    commit: null
    note: null

  - id: 23
    title: "Verify and close the ladder"
    does: >
      Run the full verification list from the approved plan. Add a CHANGELOG.md entry.
      Set this note status: done. Report the close in #reports.
    status: pending
    gate: none
    commit: null
    note: null
```

## Open items carried from the design

- **Steps 18-22 run on the veto window**, per Lemar's gate selection — archiving two boards
  and writing to Off Button happen without a blocking approval. Mitigated by construction:
  archives are reversible and step 22 is column-writes-only. Flagged, not overridden.
- **Board creation may still be refused** at 4 boards on the free tier. Fallback: ONE
  combined "Rolodex" board with Record Type as a status column and groups by category.
  Nothing else in the ladder changes.
- **`## Account` body parsing** is the one place the skill reads prose rather than
  frontmatter — a deliberate consequence of the lean 6-field set. If it proves brittle,
  promote `account_ref`/`portal_url` to frontmatter.
- **Personal contacts will be thin** on day one: the agreed sources are
  `lemar@cuzziesnj.com` and Calendar, not personal Gmail. Manual add covers the gap.

## Related

- [[on-button-reopen]] — the index → rendering pattern this ladder copies
- `.claude/routines/samira-atlas-executor.md` — PART C is the engine that runs the ladder
- `.claude/anchors.md` — `#skills-lab` `C0BBZ5J8805`; Off Button `18424191974`

## Sources

- claude: approved implementation plan, 2026-08-09 (design session with Lemar, 20 decisions)
- monday: account tier verified `free`, 1 seat, 5 boards, 2026-08-09
