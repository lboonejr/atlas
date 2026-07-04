# Haven

**Haven is the source of truth.** If Atlas and Samira are people who do jobs,
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
with you unchanged. (The full rescue plan for everything AROUND the vault — the
executor loop, the signals, the schedulers — is `../PORTABILITY.md`.)

That works because of a hard rule:

> **Nothing platform-specific is ever load-bearing inside the vault.**
> No Claude syntax, no tool-specific macros, and no platform ID that the reader
> must dereference to understand a note. Platform references ARE allowed as
> **provenance** — links in a note's `## Sources` section (schema §8) — because a
> record that cites where it came from is a better record. The test: delete every
> link and the note must still stand on its own.

Everything that *is* platform-specific — the hourly loop, the Slack channels, the
board/label/calendar IDs — lives in the **skills** (`../.claude/skills/`) and the
**one anchors registry** (`../.claude/anchors.md`), never in the vault. The skills
are the muscles; Haven is the memory. Swap the muscles, keep the memory.

> **Skills live in `../.claude/skills/`, not `../skills/`.** The Claude Code cloud
> runtime only auto-discovers project skills under `.claude/skills/<name>/SKILL.md`.
> (`../skills/` retains only `star-craft`, inherited from an earlier branch.)

### How to rehydrate Haven anywhere
Because the vault is self-describing, any capable agent or app can pick it up
cold:

1. Copy the `haven/vault/` directory to the new platform (git clone, zip export,
   a USB stick — the transport does not matter).
2. Open `vault/_system/schema.md`. It fully defines the folder circuit, the
   frontmatter standard, and the deterministic filing rules. No outside context
   is required to understand or operate the vault.
3. Point whatever new tool you are using at the same rules. Re-implement the
   loop per `../PORTABILITY.md` (the platform-neutral spec) in that tool's terms.

That is the entire migration. The vault is the asset; the tooling is replaceable.

---

## What is in here

```
haven/
├── README.md              this file — what Haven is and the portability contract
└── vault/                 the portable brain (plain Markdown, no tool lock-in)
    ├── 00-Inbox/          everything lands here first, unfiled
    ├── 10-Personal/       life & family (Money/ Health/ Home/ Family/ via `area`)
    ├── 20-Cuzzies/        Cuzzie's ops (meetings/, decisions/)
    ├── 30-Station/        The Station ops (meetings/, decisions/)
    ├── 40-Projects/       cross-cutting or multi-phase work
    ├── 50-Reference/      evergreen reference + Entities/ (canonical, cross-domain)
    ├── 60-Legal/          active legal matters (domain `legal`)
    ├── 90-Archive/        archived notes, original domain path preserved
    ├── _daily/            one append-only log note per day + Samira's run digests
    ├── _templates/        note, meeting, decision, entity, daily
    └── _system/           schema (the rulebook), home note, maps of content
```

### The headless worker is transport-agnostic

The autonomy of Atlas and Samira does **not** depend on Obsidian. The headless
worker is nothing more than **file reads and writes on the `.md` files**:
`git pull` → read/write markdown → `git commit` → `git push`. Git is the
transport, and because the vault is just versioned text, every change is
auditable and revertible.

**Obsidian is the human's reader** — a window onto the same files:

- **Desktop:** Obsidian opens the vault folder INSIDE the git clone
  (`C:\Users\lemar\Haven-repo\haven\vault`), with the **Obsidian Git** community
  plugin set to pull-only on an interval. Samira writes, the desktop reads — no
  merge conflicts. The old copied vault at `C:\Users\lemar\Vaults\Haven` is
  retired: it had no `.git` and could only drift.
- **Phone:** Obsidian mobile on the same repo via a mobile git client (Working
  Copy on iOS, GitSync on Android), or any git-synced folder.
- Obsidian Sync remains an optional paid alternative transport; nothing about the
  worker changes either way.

```
  Server (headless worker) ── git pull/push ──┐
                                              ├──►  the Haven repo  ◄── canonical
  Human's Obsidian (desktop/phone) ─ git pull ┘        (git = transport)
```

---

## How Haven connects to Atlas and Samira

- **Atlas orchestrates.** On the hourly loop (8am–6pm, seven days a week) the
  runbook (`../.claude/routines/samira-atlas-executor.md`) dispatches jobs.
- **Samira executes.** `vault-keeper` files the Inbox; `calendar-sync` rings due
  notes; every finished task lands an outcome note (**done = a filed Haven note**);
  every run appends its digest to `_daily/`.
- **Every skill reports to Haven.** Any skill that produces something worth
  remembering calls `haven-capture` to write a properly-framed note into
  `00-Inbox`. That is the front door; vault-keeper is the back office.

```
  skills (atlas, email/investor/car loops, report-result, …)
        │  haven-capture  (writes note → 00-Inbox)
        ▼
  Haven / 00-Inbox
        │  vault-keeper   (hourly)
        ▼
  filed by domain/type/status → the brain fills
```
