# PORTABILITY — how this system survives any platform, including Claude

Haven (the vault) is plain Markdown + git: it needs no rescue plan. This file is the
rescue plan for everything AROUND the vault — the executor loop, the decision surface,
the notifications — so that a capable engineer or any strong AI model can rebuild the
working system on new tools in about a day, using only this repo.

## What lives where (the 30-second map)

| Layer | Today | Portable because |
|---|---|---|
| Truth + records | `haven/vault/` (Markdown + YAML, this repo) | Self-describing: `_system/schema.md` is the complete rulebook |
| Behavior | `.claude/skills/*/SKILL.md` + `.claude/routines/samira-atlas-executor.md` | Plain-English procedures — they are prompts, readable by any model |
| Platform IDs | `.claude/anchors.md` — the ONLY place IDs live | One file to re-point |
| Scheduling | claude.ai RemoteTrigger (hourly 8a–6p ET) | Replaceable by any scheduler (see below) |
| Decision surface | Slack #decisions, reactions | An abstract 4-signal protocol (see below) |
| Alarms | Google Calendar (one-way projection) | Rebuilt from notes' `due` fields at any time |
| Binary files | Google Drive folders | Linked from notes' `## Sources`; IDs in anchors.md |

## The loop, platform-neutral (what any replacement must do hourly)

```
1. SYNC the vault (git pull).
2. FILE: every Inbox note with complete valid frontmatter → its folder (schema §4).
   Incomplete notes stay; ask the human for the missing label — never guess.
3. RING: every note with a `due` → ensure exactly one reminder alarm exists
   (write the alarm id back into the note; vault wins on any disagreement).
4. READ SIGNALS: pick up the human's approve/seen/park/close signals on open items
   and advance each accordingly.
5. INGEST: new raw captures (chat drops, email triage) → write vault notes FIRST,
   then stage any resulting work, unstarted, for the NEXT cycle (the buffer).
6. EXECUTE: work staged on an EARLIER cycle that is due now. Never outward-facing
   actions (send/pay/post/delete) without an explicit approval signal.
7. RECORD: every finished (or failed) task → an outcome note in the vault, THEN a
   short result ping. Done = a filed note, never just a checkmark.
8. JOURNAL: append the run digest to _daily/YYYY-MM-DD.md.
```

## The signal protocol (today: Slack emoji — but they are just a rendering)

| Abstract signal | Today's emoji | Meaning |
|---|---|---|
| APPROVE / EXECUTE | ✅ | run the chosen option / confirm sent |
| SEEN | 👀 | acknowledged, still deciding — do not nudge |
| PARK | ⛔ | stop driving it; hold on the standing list |
| CLOSE | 🫡 | done — record the outcome and clear the card |

Rules that must survive any port: exactly ONE surface pings the human; the human
decides by signaling, not typing; the executor never sets the human's signals; the
executor's own idempotency key is its written confirmation + stored state, never the
human's signals.

## Replacing each platform

- **Claude → another AI**: the skills and runbook are plain-English prompts — feed them
  to the new model. Replace the Skill tool with "read and follow the named file."
- **RemoteTrigger → anything**: a GitHub Action on cron, a VPS cron job, or any agent
  scheduler. It must: run the model with the bootstrap prompt
  (`.claude/routines/TRIGGER-PROMPT.md`), with credentials for git, Slack-equivalent,
  email (draft-only), and calendar.
- **Slack → Discord/Teams/SMS/anything with reactions or replies**: re-map the 4
  signals; update anchors.md; keep the one-pinging-surface rule.
- **Gmail → any mail API**: needs search, read, save-draft, and labels (or any
  equivalent seen/drafted/sent state store). The system NEVER needs send scope.
- **Google Calendar → any calendar**: needs create/update/delete events + an id the
  vault can store in `calendar_event_id`.
- **Monday**: being retired 2026-07-11 — nothing to port.
- **GitHub → any git host**: `git remote set-url`. The vault is the repo; nothing else
  moves. If git itself must go, the vault is just files — any synced folder works, at
  the cost of history.

## Backups (hosting can fail too)

Monthly runbook task: export a zip of the repo (or `git bundle`) to Google Drive and to
the desktop. Git history is the version control; the export covers a lost GitHub
account. The desktop clone `C:\Users\lemar\Haven-repo` and every Obsidian device are
additional live copies of the vault.

## Phone-first operation (already true — keep it true)

- **Decide**: Slack mobile → #decisions, react with the 4 signals.
- **Capture**: drop a thought in #atlas (Samira lands it in the vault within the hour),
  or talk to Atlas in the Claude app.
- **Read the brain**: Obsidian mobile on the same repo (via a mobile git client such as
  Working Copy on iOS or GitSync on Android), or GitHub mobile in a pinch.
- The desktop is never required. Any new surface must preserve this.
