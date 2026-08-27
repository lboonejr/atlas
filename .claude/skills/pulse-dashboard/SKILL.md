---
name: pulse-dashboard
description: >
  Pulse — Lemar's living command center, re-rendered by Samira at the end of every
  hourly scan (PART P of the runbook) and published as a NEW timestamped Google Doc
  snapshot in the Pulse Drive folder (2026-08-13: replaced the Artifact tool, which kept
  prompting Lemar for approval on his phone — the surface he checks Pulse from most).
  One page, one column, ordered BIG IDEAS → SMALL DETAILS → EXECUTION: quick todo
  capture on top, then Dawn as the North Star (direction, not tasks), the day's calendar
  roadmap, then execution — #decisions, money, today's workout, Atlas open items,
  project pulses, and routine health at the bottom. EVERY item links back to its source
  (the exact Slack thread or the Google Calendar event). The dashboard is a RENDERING
  like the Open Items canvas — the vault stays the source of truth and this skill writes
  NO Haven notes. Use it on Samira's scan or on demand: "refresh the dashboard", "render
  Pulse", "update my dashboard". It reads everything and writes only the Drive snapshot
  — it DMs Lemar the new link only when this run actually changed something (see
  Notification below), never sets reactions, never edits the vault.
---

# Pulse — the living command center (rendering only, vault stays truth)

You render **Pulse**, Lemar's one-page command center: "one place where I look at every
problem, every event, everything I need to check on — and I execute." Samira invokes
this at the END of her hourly scan, when her context already holds the #decisions state,
project-channel pulses, and this run's tallies — reuse what is already in context
instead of re-reading channels. Run unattended: no one approves anything at runtime, so
every rule is load-bearing.

**This skill is a rendering step.** Unlike morning-brief there is NO "durable note first":
the vault is already the record and the dashboard is a projection of it (same doctrine as
the Open Items canvas). If the render fails, nothing is lost — report the failure in the
run digest and move on.

## The two page laws

1. **Big ideas → small details → execution, top to bottom.** The section order below is
   Lemar's chosen order — do not reshuffle it. One single column (max-width ~820px), so
   the page reads the same on phone and desktop.
2. **Every item links to its source.** Anything that traces to a Slack thread gets that
   thread's permalink (`https://newworkspace-zlb6313.slack.com/archives/<channel_id>/
   p<ts with the decimal removed>`, `target="_blank"`); anything that traces to a
   calendar event gets its Google Calendar `htmlLink`; project rows get their channel
   link. Link-out only, never a write-back — the Doc is static HTML with no
   backend. When an item has no source (a Haven-only note with no thread or event), it
   simply renders unlinked — skip a link rather than guess one; a missing link is fine,
   a dead link is not.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it first. You use the "Pulse
dashboard" section: the **Pulse Drive folder id** (create target) and the **Samira
capture DM id** (notification target), plus the **workout artifact URL** and the
**Morning Brief Drive folder** (for the North Star link-out), the Slack channel IDs, the
reminder calendar ID, and the vault paths you already know from the run.

## Sections — in this exact top-to-bottom order

Every section carries its own small "as of HH:MM ET" stamp. **A section whose source
errors renders a compact ⚠️ chip ("source unreachable this run") instead of blocking
the page — the page always ships.** The routine-health section renders even when others
fail, and lists those failures.

1. **Quick capture → Atlas** (top of page, always in reach). A textarea pre-labeled
   "Atlas, shortlist this: " with a **Copy** button (Clipboard API, fall back to
   select-the-text) and an **Open #atlas** link. Lemar pastes in #atlas; the next scan's
   PART B captures it into Haven. Say exactly that in the helper text so the mechanism
   is honest. Keep this strip compact — one row, not a card the size of a section.
2. **Dawn — the North Star.** Direction, NOT tasks. Since 2026-07-12 Dawn's own brief
   note (`haven/vault/_daily/brief-YYYY-MM-DD.md`) carries the **North Star line** and
   **2–4 directional themes** as first-class sections — lift them verbatim (distill
   yourself only if reading an older five-goals-format note). Never render a task list
   here — execution lives further down in #decisions. Loop tally as a small chip. Link
   out to the Morning Brief Drive folder (anchors, "Daily Brief routine" section) so
   Lemar can open today's full snapshot. If today's note is missing (Dawn failed or
   pre-1am), use yesterday's and flag it stale.
3. **Calendar — today's roadmap.** Today as a timeline (primary + reminder calendar,
   ET), then this week (today+6d) as a compact day strip. All-day items render as
   chips. Every event links to its Google Calendar `htmlLink` (law #2).
4. **Respond — open #decisions.** Execution starts here. From this run's PART A state:
   the open cards waiting on Lemar, most urgent first (🔴 before 🟡, then by age),
   capped at ~10 with a "+N more in #decisions" channel link. Each card: severity dot,
   one-line summary, age ("2d"), and its 💬 thread permalink so one tap opens the exact
   thread to react/reply.
5. **Money.** A ~3-line summary + a link-out to the **Money Hub** Drive folder (id in
   anchors' "Money Hub" section — opens to today's newest snapshot), which owns the full
   picture. The three lines, from
   the ledger `haven/vault/10-Personal/Money/money-hub-ledger.md` (the ONLY money
   source — the Era Context connector was retired 2026-08-10): today's total claim from
   `daily_targets` split into its gas reserve and set-aside halves, the next dated bill or
   installment due, and this week's income vs the target from the ledger's config
   (sum this week's `income-log-2026.md` entries) — never invent a number; an unknown
   renders as its open question. Money renders read-only — Pulse never advises,
   moves, or projects money; detail, plans, and the weekly split live in the Money
   Hub page.
6. **Today's workout.** Source of truth: `haven/vault/10-Personal/Health/
   2026-07-07-basketball-fitness-plan.md` (12 weeks from Mon 2026-07-07; Phase 1 =
   weeks 1–4 Foundation, Phase 2 = weeks 5–9 Conditioning, Phase 3 = weeks 10–12
   Basketball-specific). Prefer the calendar: if today's events include a `Workout: …`
   event, show it as today's session (linked to its event). Otherwise compute Week N
   and show "Week N · <phase> — rest day or session list", each listed session linked
   to its calendar event where one exists. Always show "Week N of 12 · <phase>" and a
   link-out to the workout artifact (its checkboxes live in that page's own
   localStorage — never claim to know completion state). After week 12: "plan complete
   🏀".
7. **Atlas — open items.** **Methodology locked 2026-08-27** (see
   `haven/vault/70-Automation/vault-open-items-audit/2026-08-27-vault-open-items-audit.md`,
   which reconciled a 214-vs-~37 discrepancy): an "open item" is a Haven note that
   carries a **`due`** field AND has `status: active | awaiting-decision | parked`,
   excluding `type: entity` and `_daily/`/`_system/`/`_templates/`. The `due` field is
   REQUIRED for inclusion — it is what makes a note a time-bound thing Lemar needs to
   act on, not just any not-yet-archived note in the vault (most of the vault sits at
   `status: active` by default and is never meant to appear here; a literal scan
   ignoring the `due` requirement inflates the count ~6x, which is exactly the bug this
   audit found and fixed). Sort due-dated oldest first, 🐢 on anything active/waiting
   >14 days past its own `due`, overdue in red. Cap at ~12 with a count of the rest.
   Each item links to its source thread or calendar event when the note records one
   (law #2).
8. **Project pulses.** One line per project channel from this run's PART G pass
   (#investor-pipeline, #car-search, #on-button, #personal-finance, #cuzzys-brand,
   #comedy-club, #delivery-in-a-box, #pitch-deck-pressure-test, #trading-cards): a
   status dot (🟢 moved / ⚪ quiet / 🔴 blocked), the one-line state, and the channel
   link.
9. **Samira & routines** (bottom). Last digest time vs now (>70 min stale inside the
   8a–6p ET window → "⚠️ missed run"), failure notes (`type: log`, `status: active`
   with attempt/error), anything tagged **stuck**, STUCK cards in #decisions, standing
   flags (e.g. Basil awaiting DRY_RUN vetting), each linked to #reports or its thread.
   This section also lists any sections of THIS page that errored this run.

## Output — render and file a new Drive snapshot

Build ONE self-contained HTML page (inline CSS only, no external requests; load the
`artifact-design` skill for calibration — its guidance on layout/typography/color still
applies even though the target is now a Doc, not an Artifact). Single column,
phone-first; keep the markup simple (headings, paragraphs, tables, bold/color text
spans) since Drive's HTML→Doc conversion carries those over but drops CSS grid/flexbox
layout. `<title>Pulse — Personal Dashboard</title>`. Header: "Pulse" masthead, date,
"rendered HH:MM ET · refreshes hourly 8a–6p" line. Write the HTML to a working file,
then create it as a NEW Google Doc via `Google_Drive__create_file`:
- `parentId`: the Pulse Drive folder id (anchors, "Pulse dashboard" section).
- `title`: `"YYYY-MM-DD HHMM ET — Pulse"` (ET, zero-padded).
- `textContent`: the HTML you built; `contentMimeType: "text/html"` (Drive converts it
  to a native Doc — do not set `disableConversionToGoogleType`).
- Every render creates a brand-new Doc. Never edit or delete a prior snapshot — the
  folder is the history.

## Notification — DM only when something changed

Pulse still writes NO Slack message on a quiet hour. BEFORE building the snapshot,
compare this run's signals against what you already know from this same scan: did any
#decisions card open/close, did money change (PART M returned `money ✓ …` not
`money —`), did a project pulse's status dot flip, or is there a new/updated open Haven
note since the last render? If NO signal changed this hour, skip the render entirely —
no Doc, no DM (codified 2026-08-15; a folder of identical snapshots is noise, not
history) — and return `pulse — carried (quiet pass)` for the digest. If YES to any,
render, then send ONE line to the **Samira capture DM** (`D0BHPKMDNEP` — the shared
bot's only DM slot; safe to reuse since PART B only develops messages FROM Lemar, never
the bot's own posts):
`📍 Pulse updated — [1-line summary of what changed]. [Drive doc link] — Samira`

## SAFETY (applies to the whole skill)
You MAY: read every connected tool and the vault; create a new Pulse snapshot Doc in the
Pulse Drive folder; send ONE DM to the Samira capture DM (`D0BHPKMDNEP`), and only when
something changed this run.
You MUST NOT, ever: post to any Slack channel; DM on a quiet hour (nothing changed); send
email or any outreach; set or change Lemar's reactions; write, move, edit, or file any
vault note; touch the calendar; advise on, move, or commit money; run vault-keeper or
calendar-sync; edit or delete a prior Drive snapshot. A render failure must never abort
or degrade the rest of Samira's run.

## Returns (to the Samira runbook, for the digest)
`pulse ✅ <Drive doc URL> · sections OK K/9 · dm sent/skipped · <list any errored sections>`
— or `pulse ⚠️ render failed: <one-line reason>`.
