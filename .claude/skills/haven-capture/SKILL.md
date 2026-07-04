---
name: haven-capture
description: >
  The one mechanism every capture uses to write a note into Haven, the source of
  truth. Given a thought, a decision, a task, a meeting, or any raw input, it writes
  a single Markdown note with valid YAML frontmatter to the vault's 00-Inbox — the
  law is "capture-first: the vault is written before anything downstream." It stamps
  ONLY the controlled fields it is sure of (domain, type, status, source) and leaves
  any it is unsure of blank and marked UNRESOLVED, so vault-keeper parks the note in
  the Inbox for Lemar to resolve rather than guessing a label. If the matter already
  has an active note in the vault, it APPENDS an Update section to that note instead
  of creating a duplicate. Use it whenever Atlas or Samira catches something that
  belongs in Haven. It writes the note and nothing else — it never files, never
  touches the calendar, never sends.
---

# haven-capture — the front door of the vault

Haven is the source of truth (see `haven/vault/_system/schema.md`). This skill is the
**only** sanctioned way to put new content into it. Its whole job is: take a captured
thing and land it as one valid Markdown note (or one Update section on the matter's
existing note). Filing, ringing the calendar, and mirroring are other jobs — not this one.

The rule this skill enforces, above all others:

> **Capture-first is law. The vault is written before Monday, before Slack,
> before anything downstream.** If the vault write fails, nothing downstream runs.

## ANCHORS
All platform IDs live in ONE file: **`.claude/anchors.md`** at the repo root — read it at
the start of a run; never keep a local copy of it. Constants for this skill:
- Vault: `haven/vault/` · Inbox `haven/vault/00-Inbox/` · schema `haven/vault/_system/schema.md`
  · templates `haven/vault/_templates/` — on repo `lboonejr/atlas`, **default branch**.
- Transport: git — pull latest → write the .md → commit → push (see "The write").
- DO NOT write the retired local reader copy `C:\Users\lemar\Vaults\Haven`.

If you have no way to commit to the repo on your surface, STOP and say so — do not fall
back to the reader copy, and do not skip the vault write and go straight to Monday. The
vault write is the capture; without it there is no capture.

---

## Step zero: does this matter already have a note? (schema §7)

One matter, one note. Before writing anything, SEARCH the vault (filed folders +
`00-Inbox`) for an existing **active** note on the same matter — same invoice number,
same deal, same dispute, same thread.

- **Found, and still `active`/`awaiting-decision`** → do NOT create a sibling. APPEND to
  that note:
  ```markdown
  ## Update 2026-07-04
  [what changed / what was done / what is now blocked or next]
  ```
  Touch `updated`, add any new `## Sources` lines, commit `update: <slug>`. Appending an
  Update section is the one sanctioned body edit — it never rewrites existing content.
- **Found but `done`/`archived`** → new matter: write a new note and wiki-link the old one.
- **Not found** → write a new note (below).

## What you produce: one note

A Haven note is plain Markdown with a YAML frontmatter block. Every note carries the
**six required fields** plus optional `due`:

```yaml
---
created: 2026-07-03T14:32-04:00    # ISO 8601 with ET offset. Set once, at capture, never changed.
updated: 2026-07-03T14:32-04:00    # Same as created at capture time.
domain: cuzzies                     # controlled — personal | cuzzies | station | project | reference | legal
type: note                          # controlled — note | meeting | decision | task | reference | entity | log | brief
status: active                      # controlled — active | parked | done | archived | awaiting-decision
tags: [invoice, harvest-moon]       # open list — connect ideas freely
source: slack                       # controlled — slack | gmail | monday | drive | voice | claude | manual
# due: 2026-07-08T09:00-04:00       # OPTIONAL — add ONLY when the note is time-bound; calendar-sync will ring it
# area: money                       # OPTIONAL, personal notes only — money | health | home | family
---
```

Start from the matching file in `_templates/` (`note`, `meeting`, `decision`,
`entity`, `daily`) so the body shape is consistent, then fill the frontmatter per the
rules below.

### Timestamps
`created` and `updated` are both set to **now**, in ISO 8601 with the Eastern offset
(`-04:00` during EDT, `-05:00` during EST). They are identical at capture. Do not
back-date; do not leave them blank — these two are always known.

---

## The core discipline: stamp only what you're sure of

Four fields are controlled: **domain, type, status, source.** For each, you either
**know** it or you **leave it UNRESOLVED**. You never guess a controlled value to make
a note look complete — a guessed `domain` files the note into the wrong place silently,
which is worse than a note that sits in the Inbox waiting for one answer.

Emit an unresolved controlled field as the key with an empty value and an inline
comment naming the choices, so it is obvious in Obsidian and to vault-keeper:

```yaml
domain:    # UNRESOLVED — set one of: personal | cuzzies | station | project | reference | legal
```

A note with any UNRESOLVED (or absent, or out-of-list) controlled field **cannot be
filed deterministically**, so vault-keeper leaves it in `00-Inbox` and surfaces it to
Lemar. That stuck note is the system working, not failing.

### How sure is "sure" per field

- **source** — almost always known: it is *where this capture came from*. Atlas from a
  chat = `claude`. From #atlas or any Slack message = `slack`. From the email loop =
  `gmail`. A voice note = `voice`. A human typing directly = `manual`. Stamp it.
- **status** — default `active`. Use `done` only if the captured thing is already
  finished, `parked` if explicitly on hold, `awaiting-decision` when it sits on a
  #decisions card. Rarely unresolved.
- **type** — infer from shape, and stamp when the shape is unambiguous. **The decision
  rule (schema §3): anything recording a choice Lemar made — an option picked, an
  approval given — is `type: decision`, never `log`.** Otherwise: `meeting` (notes from
  a meeting), `task` (a concrete to-do), `brief` (a worked-up project brief),
  `reference`/`entity` (evergreen facts / a business, vendor, person, account),
  `log` (a dated record of what happened), else `note`. When genuinely torn, prefer
  `note` — it files to the domain root and is safe.
- **domain** — the field most often unresolved, because it has no safe default. Stamp it
  only when the note clearly belongs to one: `cuzzies` (Camden), `station` (Newark),
  `personal`, `project`, `reference`, `legal` (an active legal matter). If it could
  plausibly be two, or you're inferring rather than reading it, **leave it UNRESOLVED.**

`tags` is open — add a few honest tags; never blocks filing. **`area`** is OPTIONAL and
personal-only (`money`/`health`/`home`/`family`): stamp it only when obvious.

---

## Naming the file

`kebab-case.md`, per schema §5: time-bound → date-led (`2026-07-03-harvest-moon-invoice.md`);
evergreen → stable slug (`the-station-liquor-license.md`). Land it in `haven/vault/00-Inbox/`.
If the name already exists in the Inbox, append a short disambiguator — never clobber an
unfiled note.

## The body

Fill the template body with the substance: what this is, the context, any decision or
open question. The note must stand on its own if every link dies — amounts, dates,
names, and outcomes go in the body. Link entities and threads with `[[wiki-links]]`
instead of pasting their contents (one fact, one home — schema §6); if a recurring
counterparty has no entity note yet, note it — vault-keeper will stub it.

End the note with the provenance block (schema §8):

```markdown
## Sources
- slack: <permalink> (what it is)
- gmail: thread <id> (what it is)
```

Platform links belong HERE, as provenance — never as load-bearing state in prose.

---

## The write (the only side effect)

The loop is always the same — pull → write the `.md` into `00-Inbox` (or append the
Update) → commit `capture: <slug>` (or `update: <slug>`) → push — but **how** you run
git depends on the surface:

### Cloud (Samira's routine, claude.ai) — the normal path
Use the GitHub MCP connector (`get_file_contents` / `create_or_update_file` /
`push_files`) against the default branch. This is the proven, always-available path.

### Desktop (Claude Code on Lemar's machine)
⚠️ github.com is network-blocked on home Wi-Fi — prefer the GitHub MCP connector here
too. Raw git against the working clone `C:/Users/lemar/Haven-repo` works only when
github.com is reachable (hotspot, or after the router fix):

```bash
REPO="C:/Users/lemar/Haven-repo"; BR="$(git -C "$REPO" symbolic-ref --short refs/remotes/origin/HEAD | cut -d/ -f2)"
git -C "$REPO" fetch -q origin "$BR" && git -C "$REPO" checkout -q "$BR" && git -C "$REPO" pull -q --ff-only origin "$BR"
# write the note into $REPO/haven/vault/00-Inbox/<slug>.md, then:
git -C "$REPO" add -A && git -C "$REPO" commit -q -m "capture: <slug>" && git -C "$REPO" push origin "$BR"
```

If the push fails, STOP and say so — the capture is not real until it is pushed.

### claude.ai phone/web without a commit path
If your surface cannot commit, you cannot land the capture — say so plainly and route
the raw thought to #atlas so the hourly routine lands it. Never claim a capture
succeeded when no note was committed.

### Return value
Return the note's repo path (and "created" vs "updated") to the caller so it can be
linked downstream (Slack card, #reports line, mirror item).

You do NOT: move/file notes (vault-keeper), create calendar events (calendar-sync),
write to Monday/Slack/Gmail, or guess a controlled field.

## Worked example

Lemar: *"Shortlist this — Harvest Moon sent invoice 2425 for the Camden delivery,
$1,840, I think it's due next week, need to confirm the count before we pay."*

Step zero: no active note on invoice 2425 exists → new note. Sure of: `domain: cuzzies`,
`type: task`, `status: active`, `source: claude`. Due is unconfirmed — leave `due` off.

`haven/vault/00-Inbox/2026-07-03-harvest-moon-invoice-2425.md`:

```yaml
---
created: 2026-07-03T14:32-04:00
updated: 2026-07-03T14:32-04:00
domain: cuzzies
type: task
status: active
tags: [invoice, harvest-moon, accounts-payable]
source: claude
---

# Harvest Moon invoice 2425 — confirm count before paying

Harvest Moon billed invoice **2425**, **$1,840**, for the Camden delivery.
Confirm the received count against the invoice before releasing payment.

- Amount: $1,840 · Vendor: [[harvest-moon]]
- Due: believed next week — CONFIRM, then add `due:` so calendar-sync rings it.

## Sources
- claude: Atlas chat capture, 2026-07-03
```

Two days later the count is confirmed — that is the SAME matter, so step zero finds the
active note and appends `## Update 2026-07-05: count confirmed (matches), due confirmed
Jul 16 — due: added`, touches `updated`. One matter, one note.

And if Lemar had named no vendor and no store: `domain:` stays UNRESOLVED, vault-keeper
parks it, Lemar labels it in one tap. Working as designed.
