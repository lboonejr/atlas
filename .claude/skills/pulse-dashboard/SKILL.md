---
name: pulse-dashboard
description: >
  Pulse — Lemar's living command center, re-rendered by Samira at the end of every
  hourly scan (PART P of the runbook) and re-deployed to ONE stable claude.ai artifact
  URL. One page, one column, ordered BIG IDEAS → SMALL DETAILS → EXECUTION: quick todo
  capture on top, then Dawn as the North Star (direction, not tasks), the day's calendar
  roadmap, then execution — #decisions, money, today's workout, Atlas open items,
  project pulses, and routine health at the bottom. EVERY item links back to its source
  (the exact Slack thread or the Google Calendar event). The dashboard is a RENDERING
  like the Open Items canvas — the vault stays the source of truth and this skill writes
  NO Haven notes. Use it on Samira's scan or on demand: "refresh the dashboard", "render
  Pulse", "update my dashboard". It reads everything and writes only the artifact (plus
  the one-time URL write-back to anchors) — it never posts to Slack, never sends
  anything, never sets reactions, never edits the vault.
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
   link. Link-out only, never a write-back — the artifact is static HTML with no
   backend. When an item has no source (a Haven-only note with no thread or event), it
   simply renders unlinked — skip a link rather than guess one; a missing link is fine,
   a dead link is not.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it first. You use the "Pulse
dashboard" section: the **living Pulse artifact URL** (re-deploy target), the **workout
artifact URL**, the **Dawn brief artifact URL**, plus the Slack channel IDs, the reminder
calendar ID, and the vault paths you already know from the run.

## Sections — in this exact top-to-bottom order

Every section carries its own small "as of HH:MM ET" stamp. **A section whose source
errors renders a compact ⚠️ chip ("Era Context unreachable this run") instead of blocking
the page — the page always ships.** The routine-health section renders even when others
fail, and lists those failures.

1. **Quick capture → Atlas** (top of page, always in reach). A textarea pre-labeled
   "Atlas, shortlist this: " with a **Copy** button (Clipboard API, fall back to
   select-the-text) and an **Open #atlas** link. Lemar pastes in #atlas; the next scan's
   PART B captures it into Haven. Say exactly that in the helper text so the mechanism
   is honest. Keep this strip compact — one row, not a card the size of a section.
2. **Dawn — the North Star.** Direction, NOT tasks. Distill today's
   `haven/vault/_daily/brief-YYYY-MM-DD.md` into: one **North Star line** (what
   direction is today pointing?) and 2–4 **directional themes** (the big storylines the
   day serves — e.g. "resolve the wind-down", "open the Newark door", "bring personal
   systems online"), each one line with why-it-matters. Do NOT render the five goals or
   any task list here — execution lives further down in #decisions. Loop tally as a
   small chip. Link out to the full Dawn brief artifact. If today's note is missing
   (Dawn failed or pre-1am), use yesterday's and flag it stale.
3. **Calendar — today's roadmap.** Today as a timeline (primary + reminder calendar,
   ET), then this week (today+6d) as a compact day strip. All-day items render as
   chips. Every event links to its Google Calendar `htmlLink` (law #2).
4. **Respond — open #decisions.** Execution starts here. From this run's PART A state:
   the open cards waiting on Lemar, most urgent first (🔴 before 🟡, then by age),
   capped at ~10 with a "+N more in #decisions" channel link. Each card: severity dot,
   one-line summary, age ("2d"), and its 💬 thread permalink so one tap opens the exact
   thread to react/reply.
5. **Money.** Era Context connector: month-to-date income/spending/net
   (`insights__get_daily_financial_summary`) and active recurring items
   (`transactions__list_recurring_charges`), plus the draft budget table from
   `haven/vault/10-Personal/Money/2026-07-11-personal-finance-dashboard-project.md`
   (render its confirmed figures and its TBD blockers as-is — never invent a number;
   link each TBD to the thread/decision that blocks it). Money-relevant events this
   week (e.g. a payment due) link to their calendar event. If the Era connector is
   absent in this environment, render the ⚠️ chip and the Haven budget alone. Money
   renders read-only — Pulse never advises, moves, or projects money.
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
7. **Atlas — open items.** Open Haven notes (frontmatter `status: active |
   awaiting-decision | parked`, excluding `type: entity` and `_daily/`/`_system/`),
   due-dated and oldest first, 🐢 on anything active/waiting >14 days, overdue in red.
   Cap at ~12 with a count of the rest. Each item links to its source thread or
   calendar event when the note records one (law #2).
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

## Output — render and re-deploy

Build ONE self-contained HTML page (inline CSS only, no external requests; load the
`artifact-design` skill for calibration). Single column, phone-first; light/dark via
`prefers-color-scheme` AND `:root[data-theme="dark"]`/`[data-theme="light"]` overrides;
`<title>Pulse — Personal Dashboard</title>`. Header: "Pulse" masthead, date, "rendered
HH:MM ET · refreshes hourly 8a–6p" line. Write the HTML to a working file, then publish
with the **Artifact** tool:
- If anchors holds a real Pulse URL → pass it as `url` to **re-deploy the same page**
  (keep the same `title` and favicon 📍 so it stays the same tab/page).
- If it's still a placeholder → publish fresh, capture the returned URL, and record it in
  `.claude/anchors.md` under "Pulse dashboard" (one-time write, direct to `main` per the
  git-write policy).

## SAFETY (applies to the whole skill)
You MAY: read every connected tool and the vault; publish/re-deploy the Pulse artifact;
do the one-time anchors URL write-back.
You MUST NOT, ever: post to any Slack channel (Samira's digest carries your status);
send email or any outreach; set or change Lemar's reactions; write, move, edit, or file
any vault note; touch the calendar; advise on, move, or commit money; run vault-keeper or
calendar-sync. A render failure must never abort or degrade the rest of Samira's run.

## Returns (to the Samira runbook, for the digest)
`pulse ✅ <artifact URL> · sections OK K/9 · <list any errored sections>` — or
`pulse ⚠️ render failed: <one-line reason>`.
