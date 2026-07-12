---
name: pulse-dashboard
description: >
  Pulse — Lemar's living personal dashboard, re-rendered by Samira at the end of every
  hourly scan (PART P of the runbook) and re-deployed to ONE stable claude.ai artifact
  URL. One page, phone-first: today's workout (Back-to-the-Court 12-week plan), a
  condensed Dawn brief, open #decisions cards with one-tap thread links, #reports open
  items + Samira health, personal finance (Era Context + the Haven budget note), Google
  Calendar today + this week, the open Atlas items list with a copy-for-Atlas todo
  composer, and one-line project-channel pulses. The dashboard is a RENDERING like the
  Open Items canvas — the vault stays the source of truth and this skill writes NO Haven
  notes. Use it on Samira's scan or on demand: "refresh the dashboard", "render Pulse",
  "update my dashboard". It reads everything and writes only the artifact (plus the
  one-time URL write-back to anchors) — it never posts to Slack, never sends anything,
  never sets reactions, never edits the vault.
---

# Pulse — the living personal dashboard (rendering only, vault stays truth)

You render **Pulse**, Lemar's one-page cockpit. Samira invokes this at the END of her
hourly scan, when her context already holds the #decisions state, project-channel pulses,
and this run's tallies — reuse what is already in context instead of re-reading channels.
Run unattended: no one approves anything at runtime, so every rule is load-bearing.

**This skill is a rendering step.** Unlike morning-brief there is NO "durable note first":
the vault is already the record and the dashboard is a projection of it (same doctrine as
the Open Items canvas). If the render fails, nothing is lost — report the failure in the
run digest and move on.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it first. You use the "Pulse
dashboard" section: the **living Pulse artifact URL** (re-deploy target), the **workout
artifact URL**, the **Dawn brief artifact URL**, plus the Slack channel IDs, the reminder
calendar ID, and the vault paths you already know from the run.

## Sections — what you read and what each renders

Every section carries its own small "as of HH:MM ET" stamp. **A section whose source
errors renders a compact ⚠️ chip ("Era Context unreachable this run") instead of blocking
the page — the page always ships.** The Samira-health section renders even when others
fail, and lists those failures.

1. **Today's workout** — source of truth: `haven/vault/10-Personal/Health/
   2026-07-07-basketball-fitness-plan.md` (12 weeks from Mon 2026-07-07; Phase 1 =
   weeks 1–4 Foundation, Phase 2 = weeks 5–9 Conditioning, Phase 3 = weeks 10–12
   Basketball-specific). Prefer the calendar: if today's primary-calendar events include
   a `Workout: …` event, show that as today's session (time + description). Otherwise
   compute Week N from the start date and show "Week N · <phase name> — rest day or
   session list". Always show "Week N of 12 · <phase>" and a link-out to the workout
   artifact (its checkboxes live in that page's own localStorage — never claim to know
   completion state). After week 12: render a "plan complete 🏀" state.
2. **Dawn's brief, condensed** — today's `haven/vault/_daily/brief-YYYY-MM-DD.md`:
   the Status paragraph, the five goals (title + next action only), and the loop tally.
   Link out to the Dawn brief artifact. If today's note is missing (Dawn failed or
   pre-1am), use yesterday's and flag it stale.
3. **Respond: open #decisions** — from this run's PART A state: the open cards waiting
   on Lemar, newest first, capped at ~10 with a "+N more in #decisions" link. Each card:
   headline emoji, one-line summary, age ("2d"), and a 💬 permalink deep-link
   (`https://newworkspace-zlb6313.slack.com/archives/<channel_id>/p<ts with the decimal
   removed>`, `target="_blank"`) so one tap opens the exact thread to react/reply.
   Link-out only, never a write-back — the artifact is static HTML with no backend. Skip
   a bubble rather than guess a ts; a missing bubble is fine, a dead link is not.
4. **#reports open items + Samira health** — from this run's tallies + today's
   `_daily/YYYY-MM-DD.md` `## Log`: last digest time (if the previous digest is >70 min
   old inside the 8a–6p ET window, flag "⚠️ missed run"), any failure notes (`type: log`,
   `status: active` with an attempt/error), anything tagged **stuck**, STUCK cards in
   #decisions, and standing flags (e.g. Basil awaiting DRY_RUN vetting). This is the
   section that also lists any sections of THIS page that errored.
5. **Money** — Era Context connector: month-to-date income/spending/net
   (`insights__get_daily_financial_summary`) and active recurring items
   (`transactions__list_recurring_charges`), plus the draft budget table from
   `haven/vault/10-Personal/Money/2026-07-11-personal-finance-dashboard-project.md`
   (render its confirmed figures and its TBD blockers as-is — never invent a number).
   If the Era connector is absent in this environment, render the ⚠️ chip and the Haven
   budget alone. Money renders read-only — Pulse never advises, moves, or projects money.
6. **Calendar** — today as a timeline (primary + reminder calendar, ET), this week
   (today+6d) as a compact day strip beneath it. All-day items render as chips. Each
   event links to its `htmlLink`.
7. **Atlas open items + todo composer** — open Haven notes (frontmatter
   `status: active | awaiting-decision | parked`, excluding `type: entity` and
   `_daily/`/`_system/`), grouped by status, oldest first, 🐢 on anything active/waiting
   >14 days, `due` dates flagged (overdue in red). Cap at ~12 with a count of the rest.
   Below it the **todo composer**: a textarea pre-labeled "Atlas, shortlist this: " with
   a **Copy** button (Clipboard API, fall back to select-the-text) and an **Open #atlas**
   link (`https://newworkspace-zlb6313.slack.com/archives/C0BBWHCJUV9`). Lemar pastes in
   #atlas; the next scan's PART B captures it into Haven. Say exactly that in the helper
   text so the mechanism is honest.
8. **Project pulses** — one line per project channel from this run's PART G pass
   (#investor-pipeline, #car-search, #on-button, #personal-finance, #cuzzys-brand,
   #comedy-club, #delivery-in-a-box, #pitch-deck-pressure-test): a status dot
   (🟢 moved / ⚪ quiet / 🔴 blocked), last-activity age, and a channel deep-link.

## Output — render and re-deploy

Build ONE self-contained HTML page (inline CSS only, no external requests; load the
`artifact-design` skill for calibration). Phone-first: single column at narrow widths,
two-column grid on desktop; light/dark via `prefers-color-scheme` AND
`:root[data-theme="dark"]`/`[data-theme="light"]` overrides; `<title>Pulse — Personal
Dashboard</title>`. Header: "Pulse" masthead, date, "rendered HH:MM ET · refreshes hourly
8a–6p" line. Write the HTML to a working file, then publish with the **Artifact** tool:
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
`pulse ✅ <artifact URL> · sections OK K/8 · <list any errored sections>` — or
`pulse ⚠️ render failed: <one-line reason>`.
