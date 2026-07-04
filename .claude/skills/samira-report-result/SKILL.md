---
name: samira-report-result
description: >
  Samira's result-landing and #reports ritual — the single home for everything that
  records a finished task. "Done = a filed Haven note": every executed task first lands
  an outcome note in the vault (the durable record), THEN posts the two-line #reports
  ping and (until the Monday gate) mirrors to the Samira board. Mode 3 posts the run
  digest to #reports AND appends it to the vault's _daily journal. Use this every time
  Samira finishes (or fails) a task instead of writing the record inline: "land the
  result", "log the result to reports", "record this and report it", "log a failure",
  "post the run digest". It writes to Haven (via haven-capture), the mirror board, and
  #reports/#decisions only; it never sends email, pays, posts externally, or
  deletes/overwrites existing content.
---

# Samira Report & Result Landing (Haven-first)

Every executed task needs a **durable home AND a result line.** The durable home is a
**filed Haven note** — not a Monday row, not a #reports message that scrolls away.
**Done = a filed Haven note.**

Order of operations, every time: **(1) outcome note to Haven → (2) ping #reports →
(3) mirror to Monday until the gate → (4) green-check the source.** The Haven note is
the record; Slack and Monday are notifications about it.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — #reports/#decisions channel IDs, the
mirror board, and the Monday gate date (2026-07-11) are there. Constants:
- Vault: `haven/vault/` on repo `lboonejr/atlas`, default branch. You never hand-write a
  note — call **haven-capture**, which returns the note path.
- DO NOT write the retired local reader copy.

## The outcome note
Call **haven-capture** to land ONE receipt note (it will append an `## Update` to the
matter's existing active note instead, per schema §7 — either way you get a path back).
Stamp only the controlled fields you are sure of; leave the rest UNRESOLVED:
- **`type: log`** for a completed task record — BUT if the outcome records a decision
  Lemar made (an option he picked, an approval he gave), it is **`type: decision`**
  (schema §3's decision rule) so it files to `<domain>/decisions/`.
- **`status: done`** on success · **`status: active`** on a failure/stuck task.
- **`source`** — `slack` (a staged prompt), `gmail`, `monday`, `claude`, or `manual`.
- **`domain`** — stamp only when the task's channel/project makes it unambiguous.
- **`tags`** — `[samira, <skill-or-area>]` plus honest topic tags.
Body: **what ran**, the **skill used** (or "direct"), the **ACTUAL RESULT** (values /
figures / decision / text produced), and file links/IDs in a `## Sources` block
(schema §8). Wiki-link entities. Date-led filename.

## Mode 1 — SUCCESS
1. **Land the outcome note in Haven.** If the vault write fails, the task is NOT landed
   — log a failure (Mode 2); never fake a done.
2. **Post to #reports**, exactly two lines (mobile-first):
   ```
   🌐 ✅ [what ran] — [headline output in a few words]
   [skill, or "direct"] · [Haven note path] — Samira
   ```
3. **Mirror to Monday — only until the gate (2026-07-11, see anchors).** Find the item
   by `task:[project-id]` (or create a Quick item), post an Update with the same record,
   attach any generated file, set Status = Done, record the Haven note path on the item,
   and add the item link as a third #reports line. After the gate passes, this step
   drops entirely and the note path stands alone.
4. **Green-check the source message** — your done-key everywhere EXCEPT the
   reaction-engine surfaces (#decisions, #car-search, #investor-pipeline), where every
   reaction is Lemar's and you set only the headline emoji.

## Mode 2 — FAILURE
1. **Land a failure note in Haven** (`type: log`, `status: active`, the error + attempt
   number in the body). A failure is still a durable record.
2. No green check. Post to #reports:
   ```
   🌐 ⚠️ [what ran] FAILED — [the error in a few words]
   [Haven note path] — Samira (attempt N)
   ```
3. On the **3rd failure** of the same task: react 🚗 on the source (stop retrying), tag
   the Haven note stuck, and post "STUCK — needs Lemar" to #decisions (headline ⏳)
   linking the note.

## Mode 3 — RUN DIGEST (end of run)
1. Post the delta digest to #reports (🌐, "— Samira"), leading with the Haven counts:
   ```
   🌐 Samira · [date time] — C closed · N new · U urgent
   🗄️ Haven: filed F · stuck P · rang +A/~B/-C · notes-written O
   Closed: [one-liners] · 🔴 Send TODAY: […] · 👉 Waiting on you: [n] in #decisions
   🧵 Standing list → Open Items canvas
   ```
2. **APPEND the same digest block to `haven/vault/_daily/YYYY-MM-DD.md`** (create the
   day's note from `_templates/daily.md` if absent; append under `## Log` with a
   timestamp; never edit prior entries; commit `daily: run digest <time>`). The vault is
   the flight recorder — a #reports message scrolls away; the journal does not.

## Inputs this skill expects from the caller
What ran + source link · `task:[project-id]` or "one-off" · skill used or "direct" · the
actual result + files/links · `source` and (if unambiguous) `domain` · for failures: the
error + attempt number · for the digest: the run counts.

## Note on handoffs
A fuller handoff record is still produced by **handoff-builder**, pointed at Haven: the
handoff lands as a Haven note that this skill links; the two-line #reports ping still
points at the note.
