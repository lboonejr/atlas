---
name: samira-report-result
description: >
  Samira's result-landing and #reports ritual — the single home for everything that
  records a finished task. Under Haven, "done = a filed Haven note": every executed task
  first lands an outcome note in the vault (the durable record), THEN posts the two-line
  #reports ping and (during cutover) mirrors to the Monday "Samira" board (18418714876).
  Use this every time Samira finishes (or fails) a task in PART A or PART C instead of
  writing the record inline: "land the result", "log the result to reports", "post the
  result line", "record this and report it", "log a failure to reports", "post the run
  digest". It guarantees an outcome note per task, the exact two-line mobile-first #reports
  format, and that no output ever survives as a bare checkmark. It writes to Haven (via
  haven-capture), the Samira board, and #reports/#decisions only; it never sends email,
  pays, posts externally, or deletes/overwrites existing content.
---

# Samira Report & Result Landing (Haven-first)

Every executed task needs a **durable home AND a result line.** Under Haven the durable home
is a **filed Haven note** — not a Monday row, not a #reports message that scrolls away.
**Done = a filed Haven note.** This skill is the one place that record-and-report format
lives. It runs the same for a one-off as for a project task.

Order of operations, every time: **(1) write the outcome note to Haven → (2) ping #reports →
(3) mirror to Monday during cutover → (4) green-check the source.** The Haven note is the
record; Slack and Monday are notifications about it.

## HAVEN VAULT ANCHORS
```
Repo:  lboonejr/atlas  ·  branch: claude/haven-knowledge-system-4tp4sa  ·  draft PR #25
Vault (canonical):  haven/vault/     Inbox:  haven/vault/00-Inbox/     Schema:  haven/vault/_system/schema.md
Transport:  GitHub connector — you never hand-write a note; you call the haven-capture skill,
            which pulls → writes the .md to 00-Inbox → commits → pushes and returns the note path.
DO NOT write the local reader copy at C:\Users\lemar\Vaults\Haven (no .git, may drift).
Report feed:  Slack #reports  C0BBZJL85RT  (one-way ping; never swept for prompts)
Escalations:  Slack #decisions  C0BBXA96FFV
Monday "Samira" board  18418714876  (parallel notification during the ~2-wk cutover; being retired)
```

## The outcome note (what "done = a filed Haven note" means)
When a task completes, call the **`haven-capture` skill** to land ONE receipt note in
`haven/vault/00-Inbox/`. It is a dated record of what ran and what it produced.
`haven-vault-keeper` files it on the next sweep; `haven-capture` returns the note path, which
becomes the link in the #reports line and on the Monday mirror.

Stamp only the controlled fields you are sure of; leave the rest **UNRESOLVED** (never guess —
a stuck note is the system working, and Lemar labels it in one tap):
- **`type: log`** — a completed task is a dated record. (Sure.)
- **`status: done`** on success · **`status: active`** on a failure/stuck task (still open).
- **`source`** — where the task came from: `slack` (a staged prompt), `gmail` (email loop),
  `monday`, `claude`, or `manual`. (Almost always known.)
- **`domain`** — stamp it only when the task's channel/project makes it unambiguous
  (`cuzzies` · `station` · `personal` · `project` · `reference`); otherwise leave UNRESOLVED.
- **`tags`** — `[samira, <skill-or-area>]` plus honest topic tags. Never blocks filing.
- Add a **`due`** only if the record itself implies a follow-up date; otherwise omit.

Body of the note: **what ran**, the **skill used** (or "direct"), the **ACTUAL RESULT** (the
value / figures / decision / text produced, or a 2-line "here is what I did"), and any
**file links / IDs**. Link the source and any entity with `[[wiki-links]]`. Name the file
date-led (`2026-07-03-<what-ran>.md`) since it is a dated record.

## Mode 1 — SUCCESS (a task ran and produced output)
1. **LAND THE OUTCOME NOTE IN HAVEN (the record).** Call `haven-capture` with the frontmatter
   and body above (`type: log`, `status: done`). Keep the returned note path. If the Haven
   write fails, the task is not landed — stop and log a failure (Mode 2), do not fake a done.
2. **POST A RESULT to #reports** as a TWO-LINE block (mobile-first), exactly this shape:
   ```
   🌐 ✅ [what ran] — [headline output in a few words]
   [skill, or "direct"] · [Haven note path] — Samira
   ```
   Example:
   ```
   🌐 ✅ Filed CRC monthly report — submitted, conf #48213
   reggie-compliance · haven/vault/20-Cuzzies/2026-07-03-crc-monthly-report.md — Samira
   ```
   #reports is a RESULT FEED, not a status log — "ran task X ✅" is not enough; the headline
   output (line 1) and the note path (line 2) are both required.
3. **MIRROR to Monday (cutover only — a notification, not the truth).** During the ~2-week
   proving window, still land the output on the **Samira board 18418714876** as before:
   find the item by `task:[project-id]` (or CREATE a lightweight Quick item for a one-off),
   post an **Update** with the same record, attach any generated file, set **Status = Done**,
   and record the **Haven note path** on the item. Add the Monday item link as a third line on
   the #reports block during cutover. When Haven has proven out with zero discrepancies, this
   step drops and the note path stands alone. (Adding an update or status is allowed; wiping a
   brief or deleting a row is not.)
4. **Green-check the source message** (the staged prompt, or — in PART A — the #atlas capture,
   per the calling step). The green check is your done-key everywhere EXCEPT the reaction-engine
   channels **#decisions** and **#car-search**, where every reaction is Lemar's and you only
   ever set the headline emoji.

## Mode 2 — FAILURE (a task ran but errored)
1. **LAND A FAILURE NOTE IN HAVEN.** Call `haven-capture` with `type: log`, `status: active`
   (still open), the error and the attempt number in the body. A failure is still a durable
   record — it is how a stuck task stays visible in the vault, not just in a scrolling channel.
2. Do NOT add the green check. Log a failure to #reports as the matching TWO-LINE block:
   ```
   🌐 ⚠️ [what ran] FAILED — [the error in a few words]
   [Haven note path] — Samira (attempt N)
   ```
3. Check #reports for prior failures of the same message: on the **3rd failure**, react 🚗 on
   the source (stop retrying), set the Haven note's tags to flag it stuck, and post a
   "STUCK — needs Lemar" ask to #decisions (headline ⏳) linking the Haven note.

## Mode 3 — RUN DIGEST (end of run)
After all per-task result lines are posted, post the one-line run-summary DIGEST to #reports
(globe emoji, "— Samira") — the count line that FOLLOWS the result lines. It leads with the
Haven line (from the standing vault-keeper + calendar-sync jobs) and now also tallies the
outcome notes this skill wrote:
```
🌐 Run digest — 🗄️ Haven filed F · stuck P · rang +A/~B/-C · notes-written O · swept N channels ·
answers H · captures G · staged-for-later L · found X · ran Y · done Z · failed Fl · waiting W ·
deferred D · skipped S · emails summarized E · drafts saved R · email-threads closed Cl ·
email-tasks staged T — Samira
```
The per-task result lines carry the actual outputs + note paths; the digest is just the tally.

## Inputs this skill expects from the caller
- What ran (short label) and the source message link.
- `task:[project-id]` if present, else "one-off".
- Skill used, or "direct".
- The actual result (values / figures / decision / text), and any files/links/IDs to attach.
- The `source` and (if unambiguous) the `domain` for the outcome note.
- For failures: the error in a few words and the attempt number.
- For the digest: the run counts (including `notes-written` = outcome notes landed this run).

## Note on handoffs
A fuller handoff record (when a task needs one) is still produced by the **handoff-builder**
skill — now pointed at Haven: the handoff lands as a Haven note (the durable record) that this
skill links, rather than a Monday Update or a Google Doc. The two-line #reports ping still
points at the note.
