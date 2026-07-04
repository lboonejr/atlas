---
name: haven-capture
description: >
  The one mechanism every capture uses to write a note into Haven, the source of
  truth. Given a thought, a decision, a task, a meeting, or any raw input, it writes
  a single Markdown note with valid YAML frontmatter to the vault's 00-Inbox — the
  law is "capture-first: the vault is written before anything downstream." It stamps
  ONLY the controlled fields it is sure of (domain, type, status, source) and leaves
  any it is unsure of blank and marked UNRESOLVED, so vault-keeper parks the note in
  the Inbox for Lemar to resolve rather than guessing a label. Use it whenever Atlas
  or Samira catches something that belongs in Haven: "shortlist this", a brain-dump,
  a meeting note, a decision, an email-derived task, a captured idea. It writes the
  note and nothing else — it never files, never touches the calendar, never sends.
---

# haven-capture — the front door of the vault

Haven is the source of truth (see `haven/vault/_system/schema.md`). This skill is the
**only** sanctioned way to put a new note into it. Its whole job is: take a captured
thing and land one valid Markdown note in `00-Inbox`. Filing it, ringing it on the
calendar, and mirroring it to Monday are other jobs — not this one.

The rule this skill enforces, above all others:

> **Capture-first is law. The vault note is written before Monday, before Slack,
> before anything downstream.** If the vault write fails, nothing downstream runs.

## HAVEN VAULT ANCHORS (shared across haven-capture, haven-vault-keeper, haven-calendar-sync, Atlas, Samira)

```
Repo:            lboonejr/atlas   ·   branch: claude/star-crash-thread-context-2npbr   ·   PR #25 merged 2026-07-03
Vault (canonical):  haven/vault/          Skills (canonical):  .claude/skills/
Inbox:              haven/vault/00-Inbox/
Schema (rulebook):  haven/vault/_system/schema.md
Templates:          haven/vault/_templates/   (note · meeting · decision · entity · daily)
Transport:          git — pull latest → write the .md → commit → push. That is the whole loop.
                    HOW the git happens depends on the surface you are running on (see "The write" below).
Desktop working clone: C:\Users\lemar\Haven-repo  (full clone of lboonejr/atlas on the branch above;
                    Git Credential Manager supplies the GitHub token, so `git push` just works — no MCP GitHub tool needed).
DO NOT WRITE the local reader copy at C:\Users\lemar\Vaults\Haven (no .git, may drift — read-only for humans in Obsidian).
Reminder calendar (calendar-sync target):
    c_205bab62b8bb2c4fe12eec38bbc6725abaf6f5f11b767fe99a542112cf5695d3@group.calendar.google.com
```

If you have no way to commit to the repo on your surface, STOP and say so — do not fall
back to writing the local reader copy, and do not skip the vault write and go straight to
Monday. The vault write is the capture; without it there is no capture.

---

## What you produce: one note

A Haven note is plain Markdown with a YAML frontmatter block. Every note carries the
**six required fields** plus optional `due`:

```yaml
---
created: 2026-07-03T14:32-04:00    # ISO 8601 with ET offset. Set once, at capture, never changed.
updated: 2026-07-03T14:32-04:00    # Same as created at capture time.
domain: cuzzies                     # controlled — personal | cuzzies | station | project | reference | legal
type: note                          # controlled — note | meeting | decision | task | reference | entity | log | brief
status: active                      # controlled — active | parked | done | archived
tags: [invoice, harvest-moon]       # open list — connect ideas freely
source: slack                       # controlled — slack | gmail | monday | drive | voice | claude | manual
# due: 2026-07-08T09:00-04:00       # OPTIONAL — add ONLY when the note is time-bound; calendar-sync will ring it
# area: money                       # OPTIONAL, personal notes only — money | health | home | family (files into 10-Personal/<Area>/)
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
Lemar. That stuck note is the system working, not failing. Never resolve the gap by
guessing — resolving it is Lemar's one-tap job.

### How sure is "sure" per field

- **source** — almost always known: it is *where this capture came from*. Atlas from a
  chat = `claude`. From #atlas or any Slack message = `slack`. From the email loop =
  `gmail`. A voice note = `voice`. A human typing directly = `manual`. Stamp it.
- **status** — default `active`. Use `done` only if the captured thing is already
  finished (a record of something closed), `parked` if explicitly on hold. Rarely
  unresolved.
- **type** — infer from shape, and stamp when the shape is unambiguous:
  `meeting` (notes from a meeting), `decision` (a choice made, with reasoning to
  preserve), `task` (a concrete to-do), `brief` (a worked-up project brief),
  `reference`/`entity` (evergreen facts / a business, vendor, person, account, legal
  matter), `log` (a dated running log), else `note`. When genuinely torn between two,
  prefer `note` — it files to the domain root and is safe. Leave `type` UNRESOLVED only
  when you cannot tell what *kind* of thing this even is.
- **domain** — the field most often unresolved, because it is the one with no safe
  default. Stamp it only when the note clearly belongs to one:
  `cuzzies` (Cuzzie's, Camden), `station` (The Station, Newark), `personal` (Lemar's
  life, money, home, family, vehicles), `project` (cross-cutting/multi-phase work),
  `reference` (evergreen or a cross-domain entity), `legal` (an active legal matter —
  an eviction, a filing, a counsel thread). If the input could plausibly be two
  domains, or you're inferring rather than reading it, **leave `domain` UNRESOLVED.**

`tags` is open — add a few honest tags from the content; never blocks filing.
`created`/`updated` are always stamped. **`area`** is an OPTIONAL personal-only field
(`money`/`health`/`home`/`family`): stamp it only when the note is clearly `personal` AND
the sub-area is obvious; otherwise leave it off — its absence just files the note to the
`10-Personal/` root, never sends it to Lemar.

---

## Naming the file

`kebab-case.md`, per schema §5:
- **Time-bound** (has or will have a `due`, or is tied to a date/event) → lead with the
  date: `2026-07-03-harvest-moon-invoice.md`.
- **Evergreen / stable** → a stable slug: `the-station-liquor-license.md`, `cuzzies.md`.
- Keep it short, lowercase, hyphen-separated, no spaces. Land it in `haven/vault/00-Inbox/`.

If a note with that name already exists in the Inbox, append a short disambiguator
(`-2`, or a keyword) rather than overwriting — never clobber an unfiled note.

---

## The body

Fill the template body with the substance: what this is, the context, any decision or
open question. Link entities and threads with `[[wiki-links]]` (`[[cuzzies]]`,
`[[2026-07-03-...]]`) instead of pasting their contents — one fact, one home (schema §6).
Capture enough that the note stands on its own later; don't pad.

---

## The write (the only side effect)

The loop is always the same — pull → write the `.md` into `00-Inbox` → commit `capture: <slug>`
→ push — but **how** you run git depends on the surface. Pick the one that matches where you are:

### Desktop (Claude Code, this machine) — prefer the GitHub MCP connector

⚠️ On Lemar's machine, direct `git` traffic to **github.com is network-blocked** (only the
raw.githubusercontent.com CDN and the cloud-routed GitHub MCP connector get through). So the
raw-git clone below often fails at `push`. **Preferred desktop path: use the GitHub MCP tools**
(`get_file_contents` / `create_or_update_file` / `push_files`) to commit the note straight to the
branch — that is what works from here. The raw-git clone is a fallback for when github.com is
reachable (e.g. on a phone hotspot).

Raw-git fallback (only when github.com is reachable), against the persistent clone:

```bash
REPO="C:/Users/lemar/Haven-repo"; BR="claude/star-crash-thread-context-2npbr"
# 1. Ensure the clone exists and is current (self-heals if it was removed):
[ -d "$REPO/.git" ] || git clone --branch "$BR" --single-branch https://github.com/lboonejr/atlas.git "$REPO"
git -C "$REPO" fetch -q origin "$BR" && git -C "$REPO" checkout -q "$BR" && git -C "$REPO" pull -q --ff-only origin "$BR"
# 2. Write the note file into  $REPO/haven/vault/00-Inbox/<slug>.md  (use the Write tool).
# 3. Commit and push:
git -C "$REPO" add -A && git -C "$REPO" commit -q -m "capture: <slug>" && git -C "$REPO" push origin "$BR"
```

If `git push` fails (network, auth), STOP and tell Lemar — the capture is not real until it
is pushed. Do not write the reader copy, do not go to Monday.

### claude.ai (phone/web Atlas Project) — write path PENDING a connector test

A claude.ai Project has no shell, so it cannot run the git above. Whether the account's GitHub
connector can itself **commit** to the repo is being tested. Until that is resolved:
- If your surface exposes a way to commit a file to `lboonejr/atlas` on the branch, use it to
  write the note into `00-Inbox` and confirm the commit.
- If it does not, you **cannot** land the capture from here — say so plainly and route the raw
  thought to the capture intake (`#atlas`) so the hourly cloud routine (Samira, PART V/B) lands
  it in Haven instead. Never claim a capture succeeded when no note was committed.

### Return value

Return the note's repo path (`haven/vault/00-Inbox/<slug>.md`) and the branch to the caller so
it can be linked downstream (Slack card, Monday mirror, #reports line).

That is the entire skill. You do **not**:
- move or file the note (that is `haven-vault-keeper`, on the hourly loop),
- create a calendar event (that is `haven-calendar-sync`),
- write to Monday, Slack, Gmail, or the local reader vault,
- guess any controlled field to avoid a stuck note.

## Worked example

Lemar, in an Atlas chat: *"Shortlist this — Harvest Moon sent invoice 2425 for the
Camden delivery, $1,840, I think it's due next week, need to confirm the count before
we pay."*

Sure of: it's Cuzzie's (`domain: cuzzies`), it's a concrete to-do (`type: task`), it's
open (`status: active`), it came from a chat (`source: claude`), it's time-bound (a due
is coming but the exact date is unconfirmed — leave `due` off until confirmed, don't
invent it). File name is time-bound → date-led.

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
Lemar wants the received count confirmed against the invoice before we pay.

- Amount: $1,840
- Vendor: [[harvest-moon]]
- Open question: does the delivered count match 2425? Confirm, then release payment.
- Due: believed next week — CONFIRM the exact date, then add a `due:` and let
  calendar-sync ring it.
```

Contrast — same capture, but Lemar just says *"shortlist this: confirm the count before
we pay 2425"* with no vendor and no store named. Now `domain` is a guess, so:

```yaml
domain:    # UNRESOLVED — set one of: personal | cuzzies | station | project | reference | legal
type: task
status: active
tags: [invoice, accounts-payable]
source: claude
```

vault-keeper will leave this one in `00-Inbox` and surface it; Lemar sets the domain in
one tap and the next sweep files it. Working as designed.
