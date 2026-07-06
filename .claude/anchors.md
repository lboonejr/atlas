# ANCHORS — the single registry of platform IDs

This file is the ONE place every platform-specific identifier lives. Every skill, the
Samira runbook, and any future tool reads this file instead of carrying its own copy.
When a workspace, board, account, or channel changes, edit THIS file and nothing else.

> Rule: no other file in this repo may restate these IDs (quoting one inline while
> doing work is fine; maintaining a second list is not). The memory file
> `shortlist_anchors.md` on Lemar's machine is a pointer to this file, not a copy.

Last verified: 2026-07-05.

## Repo / vault

| What | Value |
|---|---|
| Repo | `lboonejr/atlas` |
| Canonical branch | `main` — created 2026-07-04 at the head of `claude/star-crash-thread-context-2npbr`. **Until Lemar flips the default branch to `main` in GitHub Settings → Branches (one click, do it at trigger-swap time), the running default is still `claude/star-crash-thread-context-2npbr`.** After the flip, everything reads/writes `main`. |
| Vault root | `haven/vault/` · Inbox `haven/vault/00-Inbox/` · Schema `haven/vault/_system/schema.md` |
| Skills (canonical) | `.claude/skills/` (repo). Local `C:\Users\lemar\.claude\skills\` copies are read-only mirrors. |
| Runbook (live behavior) | `.claude/routines/samira-atlas-executor.md` — the trigger bootstraps into this file; editing it changes the live routine. |
| Transport | GitHub MCP connector (cloud). Desktop raw git only when github.com is reachable (home Wi-Fi blocks it — see PORTABILITY.md). |
| Local working clone | `C:\Users\lemar\Haven-repo` (desktop; also what Obsidian reads) |
| DO NOT WRITE | `C:\Users\lemar\Vaults\Haven` — retired reader copy, superseded by the clone |

## Slack (workspace "Marspace", newworkspace-zlb6313)

| Channel | ID | Role |
|---|---|---|
| #decisions | `C0BBXA96FFV` | THE decision surface — only channel that pings Lemar (renamed #action-items, same ID) |
| #reports | `C0BBZJL85RT` | Silent one-way result log; never swept for prompts |
| #atlas | `C0BBWHCJUV9` | Raw capture inbox; never hosts a decision |
| #admin | `C0BBLUA7JLX` | Staged run:admin-3x prompts |
| #daily-brief | `C0BF73FF56H` | Dawn's once-a-day brief + meeting-prep links (1am ET routine). Dawn posts here and ONLY here; Samira never posts here |
| #car-search | `C0BEC2RFC00` | Car loop (samira-car-search); never swept in PART C |
| #investor-pipeline | `C0BCCUKEUQ2` | Investor loop (samira-investor) |
| #skills-lab | `C0BBZ5J8805` | Skill-candidate proposals |
| #on-button | `C0BEQUW5NPP` | "Reopen Checklist" — drop past-due bills/screenshots here; Samira extracts amount/account/contact into the pinned canvas each scan. Tracking only, nothing paid/contacted. Canvas: `F0BEN1167GB` |
| Open Items canvas | `F0BDLSHD8JD` | State only: ⏳ Waiting · ⚙️ In motion · ⛔ Parked |
| #emails (ARCHIVED) | `C0BC1JSCHQW` | Read-only record; never swept, never posted to |
| #to-do (ARCHIVED) | `C0BC30U222K` | Read-only record |

## Monday.com (account l.boonejr@gmail.com, workspace "Main workspace" 16125924)

**Cutover gate: Monday mirroring runs through 2026-07-11.** Gate = 7 consecutive days in
which every #reports result line has a matching Haven note and no discrepancies. After the
gate, the mirror steps drop from the runbook + skills and the boards go read-only.

| Board | ID | Status |
|---|---|---|
| "Samira" (mirror board) | `18418714876` | Parallel notification only — Haven is truth. Status col `color_mm4heh3w`, Item ID col `text_mm4ht4vq`, Type col `color_mm4hegx6` |
| "Car Search" | `18418974601` | Live during cutover. Key `text_mm4pv8vg`, listing link `link_mm4k5qmd`, status `color_mm4k96gz` (New Listing / Contacted / Test Drive Scheduled) |
| "Atlas Registry" | `18419004984` | Voice profiles — car-buyer profile item `12385275557`, Notes col `long_text_mm4kz2gg` |
| "Investor Pitch Tracker" | `18418845084` | RETIRED — replaced by the Haven index note `haven/vault/40-Projects/investor-pipeline/index.md` |

## Gmail labels (use IDs, never display names)

| Label | ID |
|---|---|
| Samira | `Label_1` |
| Samira/seen | `Label_2` |
| Samira/drafted | `Label_3` |
| Samira/sent | `Label_4` |
| Car-Hunt | `Label_5` |
| Car-Hunt/seen | `Label_6` |
| Samira/investor | `Label_7` |
| Samira/investor-sent | NOT YET CREATED — create with `create_label` on first investor-loop run and record the ID here |

## Google Calendar

| What | ID |
|---|---|
| Reminder calendar (calendar-sync target; personal, never business primary, no external attendees) | `c_205bab62b8bb2c4fe12eec38bbc6725abaf6f5f11b767fe99a542112cf5695d3@group.calendar.google.com` |

## Google Drive (binary files only — Drive owns PDFs/images/spreadsheet exports per schema §1)

| What | ID |
|---|---|
| Investor Master Templates folder | `1w2Uo4dpxpY5y4FCjROL4_WZpQ-Yf-Ho6` |
| Investor Data Rooms parent | `1U7GFTuA5Tj6TMD0CWgfZhWwSbwWKWDfF` |
| Lender doc package (Cuzzie's, pinned in #investor-pipeline) | `1_9m1krzrkoyKPbOZTREvaWc6pZow_a6z` |
| Legacy /Shortlist/ (read-only backup until sunset) | `1OsPmyZErkiYZAomNfmCgG1go2Pcq76XV` |
| ~~Investor Index Google Sheet~~ | RETIRED 2026-07-04 — replaced by `haven/vault/40-Projects/investor-pipeline/index.md` (was `1QJZNznjRGY-74wprJH_ehdv0VKvJRb4gZHzhais1AwA`, never populated) |

## Cloud routine — Samira (Claude-specific — see PORTABILITY.md for what replaces this elsewhere)

| What | Value |
|---|---|
| RemoteTrigger | `trig_01VGzAWGSadjRbJbKURxCYvG` (v4 → v5 thin bootstrap, see `.claude/routines/TRIGGER-PROMPT.md`) |
| Cloud env | `env_01Xatmag93x2WA2Gd84D9iHj` |
| Cron | `0 12-22 * * *` UTC (hourly 8a–6p ET) |
| Disabled trigger (folded into v4) | `trig_0145zp6gHsouqBAKa9JkhJRk` |

## Cloud routine — Daily Brief / "Dawn" (separate from Samira)

Once-a-day 1am ET routine that complements Samira. Thin bootstrap
`.claude/routines/DAILY-BRIEF-TRIGGER.md` → fat runbook `.claude/routines/daily-brief.md`.

| What | Value |
|---|---|
| RemoteTrigger | NOT YET CREATED — create with a daily 1am ET cron pointing at the bootstrap, then record the `trig_…` id here |
| Cloud env | fill in on creation (may reuse Samira's `env_01Xatmag93x2WA2Gd84D9iHj` or a fresh env) |
| Cron | `0 5 * * *` UTC (1am EDT) · `0 6 * * *` UTC during EST — revisit at DST |
| Runbook (live behavior) | `.claude/routines/daily-brief.md` — editing on the default branch changes the next run |
| Living brief artifact URL | `https://claude.ai/code/artifact/125d4d13-c1ae-4f9c-8861-e173b56635e5` — first published 2026-07-05 (manual dry run). morning-brief re-deploys to THIS same URL each run (pass it as `url`). |
| Living meeting-prep artifact URL | NOT YET CREATED — meeting-prep publishes on the first day with calls and records the stable URL here, then re-deploys to it each run |

## Identity

| What | Value |
|---|---|
| Lemar business | lemar@cuzziesnj.com (Cuzzie's winds down mid-2026 — do not build on it) |
| Lemar personal / durable | l.boonejr@gmail.com · 856-602-0820 (car hunt: private buyer, never a Cuzzie's title) |
| Lemar Slack user id | `U0BC5UTHYG4` (display "Don Frunt") |
| Samira Slack posts | lead with 🌐, sign "— Samira" |
| Dawn (Daily Brief) Slack posts | lead with 🌅, sign "— Dawn" · posts only to #daily-brief `C0BF73FF56H`. ("Dawn" is a placeholder persona name — rename freely; it lives only in the two skills + this row.) |
