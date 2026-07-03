# Haven

**Haven is the source of truth.** If Atlas and Semira are people who do jobs,
Haven is the country they live in — the place where everything is, where every
skill reports, and where the truth and the *why* of every thread are kept.

Haven is one vault for every domain: personal, Cuzzie's, The Station, and every
project. It is plain Markdown with YAML frontmatter and nothing else. That is a
deliberate constraint, not a limitation — it is what makes Haven **portable
across models and platforms**.

---

## The portability contract

The whole point of Haven is that it outlives any single tool. If Claude goes
down, or you want to move to a different model or app tomorrow, the brain comes
with you unchanged.

That works because of a hard rule:

> **Nothing platform-specific ever gets written into the vault.**
> No Claude syntax, no Monday IDs, no Slack references, no tool-specific macros
> inside a note's body or frontmatter. The vault is just notes.

Everything that *is* platform-specific — the hourly loop, the Monday board
registration, the Slack channels, the Semira executor wiring — lives in the
**skills** (`../skills/`), never in the vault. The skills are the muscles; Haven
is the memory. Swap the muscles, keep the memory.

### How to rehydrate Haven anywhere
Because the vault is self-describing, any capable agent or app can pick it up
cold:

1. Copy the `haven/vault/` directory to the new platform (git clone, zip export,
   Obsidian Sync, a USB stick — the transport does not matter).
2. Open `vault/_system/schema.md`. It fully defines the folder circuit, the
   frontmatter standard, and the deterministic filing rules. No outside context
   is required to understand or operate the vault.
3. Point whatever new tool you are using at the same rules. Re-implement the
   Inbox sweep (see `../skills/vault-keeper/SKILL.md` for the reference
   procedure) in that tool's own terms.

That is the entire migration. The vault is the asset; the tooling is replaceable.

---

## What is in here

```
haven/
├── README.md              this file — what Haven is and the portability contract
└── vault/                 the portable brain (plain Markdown, no tool lock-in)
    ├── 00-Inbox/          everything lands here first, unfiled
    ├── 10-Personal/       life, finances, housing, vehicles, writing
    ├── 20-Cuzzies/        Cuzzie's ops (meetings/, decisions/)
    ├── 30-Station/        The Station ops (meetings/, decisions/)
    ├── 40-Projects/       cross-cutting or multi-phase work
    ├── 50-Reference/      evergreen reference + Entities/ (canonical, cross-domain)
    ├── 90-Archive/        archived notes, original domain path preserved
    ├── _daily/            one append-only log note per day
    ├── _templates/        note, meeting, decision, entity, daily
    └── _system/           schema (the rulebook), home note, maps of content
```

The `vault/` here is a **seed** — the canonical skeleton, schema, templates, and
example entities. The *live* vault runs through Obsidian's headless Sync client
on the Atlas server (with this git repo as the no-subscription fallback), and
Claude Code reads and writes the `.md` files directly. You read it through the
Obsidian app; routines read and write it through Claude Code on the server.

---

## How Haven connects to Atlas and Semira

- **Atlas orchestrates.** On the hourly loop (8am–6pm, seven days a week) Atlas
  dispatches jobs.
- **Semira executes.** `vault-keeper` is a Semira executor job — the filing
  clerk that sweeps `00-Inbox` each pass and files valid notes by the schema.
- **Every skill reports to Haven.** Any skill that produces something worth
  remembering calls `haven-capture` (`../skills/haven-capture/`) to write a
  properly-framed note into `00-Inbox`. That is the front door; vault-keeper is
  the back office.

```
  skills (star-craft, chase, meeting-runner, …)
        │  haven-capture  (writes note → 00-Inbox)
        ▼
  Haven / 00-Inbox
        │  vault-keeper   (Semira executor, hourly via Atlas)
        ▼
  filed by domain/type/status → the brain fills
```

---

## Open decisions (defaulted — override any of these)

These came from the handoff doc. Each is built to your stated leaning; change the
schema and this note if you want a different call.

1. **Cadence** — vault-keeper runs on the hourly loop **seven days a week**,
   overriding the old "Saturday is silent" rule for this specific job (your
   latest instruction). 
2. **Personal** — kept **flat** (`10-Personal`) for now; not split into
   father's-entities / finance / writing sub-domains yet.
3. **Projects** — kept as a **top-level `40-Projects`**, not nested under each
   business.
4. **Legal** — kept under **`50-Reference/Entities`** for now. Given the two
   active evictions, say the word and it gets promoted to a top-level folder.
5. **Capture wiring** — Atlas routes `atlas`-channel captures into `00-Inbox`
   automatically, frontmatter applied on the way in (via the `haven-capture`
   contract).
6. **Migration order** — not built yet. Suggested sequence for pointing existing
   skills at Haven: narrative-heavy first (`star-craft`, `meeting-runner`), then
   financial (`chase`), then the rest (`reggie`, `scout`, `shortlist`).
7. **Mobile read** — phone reading happens in the Obsidian app (the mobile Drive
   connector cannot read `.md`). Accepted as the phone-first path.
