# ANCHORS — the single registry of platform IDs

This file is the ONE place every platform-specific identifier lives. Every skill, the
Samira runbook, and any future tool reads this file instead of carrying its own copy.
When a workspace, board, account, or channel changes, edit THIS file and nothing else.

> Rule: no other file in this repo may restate these IDs (quoting one inline while
> doing work is fine; maintaining a second list is not). The memory file
> `shortlist_anchors.md` on Lemar's machine is a pointer to this file, not a copy.

Last verified: 2026-09-06 (**THREE-CONVERSATION RESTRUCTURE** — the per-channel
workflow era ended; Samira now runs three conversations (Convo 1 = her DM `D0BHPKMDNEP`,
the working meeting; Convo 2 = Lemar's SELF-DM `D0BBVV54L5R`, his intake notepad,
reachable only via the personal Slack connector; Convo 3 = private #fixes
`C0BV5BRNH5Z`) and every project channel became an append-only TIMELINE — never swept
for input. #decisions is RETIRING (migration underway), #stormy RETIRED, the Open
Items canvas RETIRED. Card format: `.claude/doctrine/card-format.md`. Lettered PARTs →
numbered (mapping table at the end of the runbook). This restructure was developed on
branch `claude/samira-workflow-restructure-2k3gx5` + PR — a sanctioned one-time
exception to the git-write policy below, because the cutover IS the merge to `main`.)
· 2026-08-31 (PART D found the Gmail label table below stale — the connected
Gmail account had NO `Samira`/`Samira/seen`/`Samira/drafted`/`Samira/sent`/`Samira/investor`
labels at all; `Label_1` in that account is actually a pre-existing unrelated label
"Sweep/Review", not "Samira". Created the five missing labels this run per the
samira-email-loop skill's own "One-time setup" step and recorded their real (long-form)
IDs below. Also discovered two labels in active use by some other routine that were never
recorded here: "Action Needed" and "Finance Bills" — left unrecorded pending Lemar
confirming which routine owns them; do not assume and do not repurpose.) · 2026-08-15
(routine-efficiency review: added the run state file row, closed the Monday gate, codified
the Pulse quiet-pass skip — see CHANGELOG) · 2026-07-16 (added the Voice profile section —
canonical profile moved into the repo) · 2026-07-16 (Dawn rerouted off #daily-brief → now
posts to Lemar's DM, bot IM `D0BJ0JPQD8C`; #daily-brief being archived) · 2026-07-16 (Atlas
capture inbox moved off #atlas → Lemar's DM with Samira's bot, `D0BHPKMDNEP`; #atlas being
archived) · 2026-07-17 (added Stormy the idea-baking engine, REFOLDED into Samira's run as
PART Q per Lemar — no separate trigger/bot/DM; posts via Samira's existing bot to the
private #stormy channel `C0BJ37SU1TL`, created + Samira bot confirmed in-channel
2026-07-17) · 2026-08-13 (Pulse / Money Hub / Morning Brief / Meeting Prep artifact-URL rows
replaced with Drive folder ids — Artifact tool retired for all four, see CHANGELOG).

## Repo / vault

| What | Value |
|---|---|
| Repo | `lboonejr/atlas` |
| Canonical branch | `main` — flipped to the default branch in GitHub Settings → Branches (confirmed live 2026-07-08). Everything reads/writes `main`. |
| Vault root | `haven/vault/` · Inbox `haven/vault/00-Inbox/` · Schema `haven/vault/_system/schema.md` |
| Skills (canonical) | `.claude/skills/` (repo). Local `C:\Users\lemar\.claude\skills\` copies are read-only mirrors. |
| Runbook (live behavior) | `.claude/routines/samira-atlas-executor.md` — the trigger bootstraps into this file; editing it changes the live routine. |
| Run state file | `.claude/state/samira-state.json` — run-lock + per-surface watermarks (runbook PART 0, added 2026-08-15). Written to `main` at run start (lock) and run end (watermarks). The ONE source of "since the last run"; digest prose is no longer a checkpoint. |
| Transport | GitHub MCP connector (cloud). Desktop raw git only when github.com is reachable (home Wi-Fi blocks it — see PORTABILITY.md). |
| **Git write policy** | **Never open a feature branch + pull request for `haven/vault/**`, `.claude/**`, or any routine/skill write.** Every session (hourly Samira scan, Dawn's daily run, or a one-off session) commits and pushes straight to `main` — GitHub MCP connector's `create_or_update_file`/`push_files`, or local git `commit` + `push origin main`. A branch+PR strands that session's work off `main`, where no later run or skill ever sees it (root-caused 2026-07-08: PRs #34/#35 each re-did work already done on `main`, and #35's Gusto Jul 8 note existed nowhere else). Lemar's call 2026-07-08 1:23pm ET: fix this with guidance here rather than flipping repo auto-merge settings. If a direct push to `main` is rejected (someone pushed since your last pull), re-pull and retry the direct write — do not fall back to a branch+PR. |
| Local working clone | `C:\Users\lemar\Haven-repo` (desktop; also what Obsidian reads) |
| DO NOT WRITE | `C:\Users\lemar\Vaults\Haven` — retired reader copy, superseded by the clone |

## Voice profile (Lemar's outbound voice — single source of truth)

Any skill, routine, or agent that drafts language Lemar will send or post reads the
canonical profile first and obeys it. Its header block carries the precedence rule: it
supersedes ALL other style guidance, including guides bundled inside skills.

| What | Value |
|---|---|
| **Canonical profile (authoritative)** | `.claude/voice/voice-profile-lemar-boone-jr.md` (repo). The single source of truth for Lemar's voice; edit it through Obsidian. Opens with a header block (precedence rule) + a Hard-Floor Lint, then the full ~983-line profile verbatim. Supersedes every other style reference. |
| OneDrive copy (NOT authoritative) | `C:\Users\lemar\OneDrive\Desktop\12 Personal\Shared\Lemar Voice Profile\voice-profile-lemar-boone-jr.md` — convenience copy only, kept for desktop reference. If it ever differs from the repo copy, the repo copy governs. Cloud routines cannot reach it; the repo copy is what they read. |
| Wired draft-skills (repo) | `samira-email-loop` (D1 save gate + D3 draft-options), `samira-investor` (I3 outreach), `samira-car-search` (F3 — floors apply except signature floor 7, which yields to the private-buyer identity), `my-writing-style` (general-purpose on-demand drafting/rewriting utility for any channel — invoked live, not part of the hourly runbook). Each reads the profile and runs its Hard-Floor Lint before saving/presenting. |
| Not-yet-wired (not in this repo) | `task-builder`, `Aaron` (aaron-exec), `Chase` (chase-commitments) are anthropic-skills plugin/session skills, not vendored here — they can't be wired via local git yet. Wire them when the pending chat-skills→repo conversion lands them in `.claude/skills/`. Until then, the profile's header-block precedence rule governs any voice they draft. |
| email-responder (retired from send path) | The vendored `anthropic-skills:email-responder` is retired from the send path — `samira-email-loop` owns email drafting. If it ever fires, the canonical profile's header-block precedence rule governs: the profile supersedes email-responder's `references/writing-style.md` (which conflicts, e.g. it permits em dashes; the profile forbids them). Do not blend them. |

## Slack (workspace "Marspace", newworkspace-zlb6313)

| Channel | ID | Role |
|---|---|---|
| **Convo 1 — Samira DM (Lemar)** | `D0BHPKMDNEP` | **"What we're working on now"** (since 2026-09-06) — the working meeting. Every task/project is ONE threaded card (`.claude/doctrine/card-format.md`); worked in PART 3. The only surface that pings Lemar for work decisions. (History: was the Atlas capture inbox 2026-07-16→2026-09-06; captures moved to Convo 2. im:write/im:history/reactions confirmed 2026-07-16.) |
| **Convo 2 — Lemar's SELF-DM** | `D0BBVV54L5R` | **"What I need to work on"** (since 2026-09-06) — Lemar's intake notepad: brain-dumps, deep dives (Stormy mode), quick updates, money drops, skill thoughts, on-button drops. Swept in PART 4. **Reachable ONLY via the personal Slack connector `7faf04c0-5bd6-4237-8430-f80040c482e1`** — a bot cannot enter a self-DM, so Samira's bot never touches this surface. Both sides are authored by Lemar's own user (`U0BC5UTHYG4`); Samira's posts carry the 🌐 prefix (🌐🌩️ in deep-dive mode) — the prefix is the ONLY discriminator and is load-bearing. Read+write smoke-tested 2026-09-06. |
| **Convo 3 — #fixes** | `C0BV5BRNH5Z` | **"Fixes"** (PRIVATE, created 2026-09-06) — anything wrong with Samira herself: bugs, errors, missed runs, inconsistencies, contradictions, STUCK escalations, scanner findings. Card surface, worked in PART 5. Bot membership pending Lemar's `/invite @Samira` (until then, fix items land as 🔧-tagged Convo 1 cards per the migration runbook). |
| #decisions (RETIRING) | `C0BBXA96FFV` | Former decision surface — **retiring 2026-09** (renamed #action-items, same ID). Open cards migrating to Convo 1 per `.claude/routines/migration-2026-09-three-convos.md`; Lemar archives the channel once migration completes. Never post new cards here. |
| #reports | `C0BBZJL85RT` | Silent one-way result log + run digest; never swept for prompts. Unchanged by the restructure. |
| #atlas (RETIRED) | `C0BBWHCJUV9` | Former raw capture inbox — **retired 2026-07-16**, replaced by the Samira capture DM (above). Being archived; never swept, never posted to (the transition-period PART B glance was removed from the runbook 2026-08-15) |
| #admin | `C0BBLUA7JLX` | TIMELINE (2026-09-06) — former staged-prompt channel; the fenced-prompt sweep ended with the restructure. Append-only record only. |
| Dawn DM (Lemar) | `D0BJ0JPQD8C` | **Dawn's output surface since 2026-07-16** — the Dawn bot's direct message with Lemar (`U0BC5UTHYG4`). The bot posts by sending to Lemar's user id, which auto-opens this IM (bot has `im:write`). Dawn's ONLY Slack surface; Samira never posts here. Replaced #daily-brief |
| #stormy (RETIRED) | `C0BJ37SU1TL` | **Retired 2026-09-06** — Stormy's workflow moved to Convo 2 (deep-dive mode inside the self-DM, PART 4). Read-only record; Lemar archives it alongside #decisions once migration completes. (History: private channel created 2026-07-17 as PART Q's surface, chosen because the shared bot's one DM slot was taken.) |
| #daily-brief (RETIRED) | `C0BF73FF56H` | Dawn's former once-a-day surface — **retired 2026-07-16**, Dawn now DMs Lemar (see "Dawn DM" above). Being archived; read-only record, never posted to |
| #car-search | `C0BEC2RFC00` | TIMELINE — car loop retired 2026-07-21; on-demand skill only. |
| #investor-pipeline | `C0BCCUKEUQ2` | TIMELINE (2026-09-06) — investor movements (data rooms, index changes, outreach state) posted by PART 6b; never swept. Investor decision cards live in Convo 1; investor input arrives via the Gmail `Samira/investor` label + Convo 2 drops. |
| #camden-launch | `C0BRZT2V89W` | **PRIVATE** — TIMELINE (2026-09-06) for the Camden Dispensary Launch engagement: artifacts + outcomes posted here; never swept. Engagement questions are Convo 1 cards titled "Camden Launch" (overlay `.claude/projects/camden-dispensary-launch-project-instructions.md` still outranks loop mechanics). Bot confirmed in-channel 2026-08-19. |
| #skills-lab | `C0BBZ5J8805` | TIMELINE (2026-09-06) — record lines for skill-candidate proposals; the proposals themselves are Convo 1 cards, and skill thoughts arrive via Convo 2. |
| #on-button | `C0BEQUW5NPP` | TIMELINE (2026-09-06) — reopening record: page/canvas regeneration notices post here; drops now arrive via Convo 2 (the **on-button-plan** skill's ingest/dedupe rule unchanged; source of truth `haven/vault/40-Projects/on-button-reopen/index.md`, page `on-button-reopen.html`, canvas `F0BEN1167GB`). Tracking only, nothing paid/contacted. |
| #personal-finance | `C0BGLEMH99T` | TIMELINE (2026-09-06) — Money Hub snapshot links + money movement entries post here (standing permission kept); money DROPS now arrive via Convo 2 and are worked in PART 4 via the **money-hub** skill. Source of truth: `haven/vault/10-Personal/Money/money-hub-ledger.md` (+ `income-log-2026.md`). |
| #pitch-deck-pressure-test | `C0BCD7U5X2B` | Recapitalization deck ($500K) pressure-test Q&A thread |
| #cuzzys-brand | `C0BCH2C3GRM` | White-label brand project (recorded 2026-07-12 for Pulse link-outs) |
| #delivery-in-a-box | `C0BDN2KQFD4` | DIB project channel (recorded 2026-07-12 for Pulse link-outs) |
| #comedy-club | `C0BD8LTM1EK` | Comedy-club project channel — PRIVATE (recorded 2026-07-12 for Pulse link-outs) |
| #trading-cards | `C0BGYM1UB4Y` | Sports-cards side hustle (recorded 2026-07-12 for Pulse link-outs) |
| #free-books-partnership | `C0BGCAK0ML3` | TIMELINE — project channel (never swept since 2026-09-06) |
| #booking-agent | `C0BHXTPST52` | TIMELINE — booking-agent scoping project (never swept since 2026-09-06) |
| #random-ideas | `C0BC2A94142` | Resolved via `slack_search_channels` 2026-07-22 12:xx ET scan. Old/quiet channel (last activity ~June 2026) — one long-form idea from Lemar about restructuring Samira into a skills/employees org, not a runnable prompt (no fence, not addressed as an instruction, and not new this scan). No action taken; recorded for future sweeps. |
| #general | `C0BC07YTZJA` | **Access gap** — bot returns `not_in_channel` despite appearing in some channel listings; needs `/invite @Samira` or confirmation it's out of scope. Flagged 2026-07-22, unresolved. |
| Open Items canvas (RETIRED) | `F0BDLSHD8JD` | **Retired 2026-09-06** — write-blocked since 2026-07-25 (3-strike 8/7); parked state now lives on the cards themselves + the Haven open-items note under `70-Automation/samira/`. This closes the standing canvas gap rather than carrying it. |
| #emails (ARCHIVED) | `C0BC1JSCHQW` | Read-only record; never swept, never posted to |
| #to-do (ARCHIVED) | `C0BC30U222K` | Read-only record |

## Monday.com (account l.boonejr@gmail.com, workspace "Main workspace" 16125924)

**Gate CLOSED 2026-08-15 — Monday mirroring is retired.** The gate date (2026-07-11) had
passed a month earlier with no formal review ever run (flagged in the 7/21 journal), and
the "Samira" mirror board returned `not found` on 2026-08-14. Lemar closed it out during
the 2026-08-15 routine-efficiency review: every mirror step is removed from the runbook
and skills; the boards below are read-only history. (The "Off Button" board is separate
live tooling, not part of the retired mirror.)

| Board | ID | Status |
|---|---|---|
| "Samira" (mirror board) | `18418714876` | Parallel notification only — Haven is truth. Status col `color_mm4heh3w`, Item ID col `text_mm4ht4vq`, Type col `color_mm4hegx6` |
| "Car Search" | `18418974601` | Live during cutover. Key `text_mm4pv8vg`, listing link `link_mm4k5qmd`, status `color_mm4k96gz` (New Listing / Contacted / Test Drive Scheduled) |
| "Atlas Registry" | `18419004984` | Voice profiles — car-buyer profile item `12385275557`, Notes col `long_text_mm4kz2gg` |
| "Investor Pitch Tracker" | `18418845084` | RETIRED — replaced by the Haven index note `haven/vault/40-Projects/investor-pipeline/index.md` |
| "Off Button — Vendor Wind-Down & Payoff" | `18424191974` | Cuzzie's (Camden) vendor wind-down + IRS tax payment-plan tracker as the license/location transitions to another operator. One item per obligation, correspondence in that item's Updates feed. Tracking/negotiating-support only — nothing paid or contacted automatically. Identified 2026-08-10 via `monday-com` search after Lemar referred to it verbally as "the off-button Monday board" (distinct from the on-button-reopen tracking, which has no Monday board). Columns: Vendor Category `color_mm5qxtv1` · Contact Name `text_mm5q9s0w` · Contact Email `email_mm5q4zpb` · Contact Phone `phone_mm5qa4sc` · Latest Notice/Bill Date `date_mm5qksv3` · Amount Owed `numeric_mm5qh0zv` · Amount Paid to Date `numeric_mm5qfdq9` · Suggested Payback Amount `numeric_mm5qb3er` · Suggested Payment Plan `long_text_mm5qjfjv` · Payment Plan Start/End `date_mm5q9bm`/`date_mm5qabsd` · Installments Remaining `numeric_mm5qe05b` · Next Payment Due Date `date_mm5qqwhj` · Correspondence Status `color_mm5qjh06` · Resolution Status `color_mm5qekcc` · Collections Agency `text_mm5qhwwj` · Payment Info/Method `long_text_mm5qtcjj` · Source Notes `long_text_mm5qavs1`. Groups: Vendors — Cannabis (Past Due/Open Balance) `group_mm5rxza9` · Vendors — Negotiate (Large Balances) `group_mm5q4d77` · Vendors — Self-Pay (Small Balances) `group_mm5qgxka` · Vendors — New/Unclassified `group_mm5qs8wh` |

## Gmail labels (use IDs, never display names)

**2026-09-06 note (88th scan — supersedes the 2026-08-31/09-05 notes below, which were
wrong):** a fresh `list_labels` call this run returned a table that does NOT match what
was recorded here — the THIRD different version of this table in five weeks, which is
itself a #fixes-worthy pattern (raised there, see the digest). Recording exactly what
the API returned, live, 2026-09-06: `Samira` (parent) = `Label_1` (NOT a "Sweep/Review"
label as the 2026-08-31 note claimed — no label named "Sweep/Review" exists in this
account). `Car-Hunt`, `Car-Hunt/seen`, and `Samira/investor-sent` all EXIST now (with
real traffic — 6, 61, and 9 messages respectively), contradicting the prior "never
created" notes. `Vendor Menus` now carries a short-form `Label_8`, not the long-form id
previously recorded. **Neither "Action Needed" nor "Finance Bills" appears in the label
list at all** — `list_labels` returns every label in the account, so either they were
deleted/renamed since 2026-08-31, or the long-form IDs recorded for them were never
real. Given three consecutive scans have each reported different ground truth for the
exact same six labels, treat any single scan's read (including this one) as provisional
until it holds across two consecutive runs — this table has flipped every time someone
checked.

| Label | ID (live 2026-09-06) |
|---|---|
| Samira (parent) | `Label_1` |
| Samira/seen | `Label_2` |
| Samira/drafted | `Label_3` |
| Samira/sent | `Label_4` |
| Car-Hunt | `Label_5` (exists, 6 msgs/6 threads — car-search loop is retired but the label is live) |
| Car-Hunt/seen | `Label_6` (exists, 61 msgs/59 threads) |
| Samira/investor | `Label_7` |
| Vendor Menus | `Label_8` (short-form now, not the long-form id recorded 2026-08-31) |
| Samira/investor-sent | `Label_9` (exists, 9 msgs/2 threads) |
| Action Needed | NOT FOUND this scan — absent from the full label list; prior long-form id may be stale or the label may be gone |
| Finance Bills | NOT FOUND this scan — same caveat |

## Google Calendar

| What | ID |
|---|---|
| Reminder calendar (calendar-sync target; **personal money only**, never business primary, no external attendees) | `c_205bab62b8bb2c4fe12eec38bbc6725abaf6f5f11b767fe99a542112cf5695d3@group.calendar.google.com` |
| Cuzzie's (Owners) — **business money only** (payroll, commercial insurance, workers' comp, storage, business phone, vendor invoices, entity collections). Business bills never ring on the personal reminder calendar and never enter `daily_targets` (locked 2026-08-10). | `c_5405960d86d1e2152cef29d5cb1ae6a4d7edd8a50f6f7eb3f5d66ab940874f1a@group.calendar.google.com` |

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
| Slack connector (Samira's own bot identity) | connector_uuid `01519dfa-b91a-47eb-beb4-cdc04444144e`, custom connector named "Samira" (bot Slack user id `U0BJQ771LJU`), MCP endpoint `https://samira-two.vercel.app/mcp`. Swapped into this trigger's `mcp_connections` 2026-07-16, replacing the shared personal Slack connector for bot surfaces (fixes the reaction-engine identity gap). Server code: `apps/samira-slack-bot/` in this repo, deployed free on Vercel; bot token lives only in Vercel's environment settings. Bot must stay invited (`/invite @Samira`) in every channel Samira posts/reads: #reports, **#fixes `C0BV5BRNH5Z` (invite pending 2026-09-06)**, #decisions (until archived), and the timeline channels she posts entries to. Convo 1 (`D0BHPKMDNEP`) is a bot DM — no invite needed. |
| **Personal Slack connector (Convo 2 only)** | connector_uuid `7faf04c0-5bd6-4237-8430-f80040c482e1` (the shared personal connector, acting as Lemar `U0BC5UTHYG4`). **Re-attach to trigger `trig_01VGzAWGSadjRbJbKURxCYvG` alongside the bot connector (2026-09 restructure)** — it is the ONLY way to reach Lemar's self-DM `D0BBVV54L5R` (a bot cannot enter a self-DM). Used exclusively for the PART 4 sweep + 🌐-prefixed replies there; every other surface stays on the bot connector. Until it rides the trigger, PART 4 degrades gracefully (one #fixes line, skip). |

## Cloud routine — Daily Brief / "Dawn" (separate from Samira)

Once-a-day 1am ET routine that complements Samira. Thin bootstrap
`.claude/routines/DAILY-BRIEF-TRIGGER.md` → fat runbook `.claude/routines/daily-brief.md`.

| What | Value |
|---|---|
| RemoteTrigger | `trig_01BFg7YLWvhoegvWLCjGYtx3` (created 2026-07-05; daily 1am ET; bootstraps `.claude/routines/DAILY-BRIEF-TRIGGER.md`) |
| Cloud env | `env_01Xatmag93x2WA2Gd84D9iHj` (shared with Samira — same connectors + git access) |
| Cron | `0 5 * * *` UTC (1am EDT) · `0 6 * * *` UTC during EST — revisit at DST |
| Runbook (live behavior) | `.claude/routines/daily-brief.md` — editing on the default branch changes the next run |
| Morning Brief Drive folder | `1bmBv1UZCptF20QgBzb5J-iOBUaG5MLj-` (`ATLAS/Dashboards/Morning Brief`, folder link `https://drive.google.com/drive/folders/1bmBv1UZCptF20QgBzb5J-iOBUaG5MLj-`). **Rendering target changed 2026-08-13** — Artifact tool retired (same reason as Pulse). Every run creates a NEW Doc here, filename `YYYY-MM-DD HHMM ET — Morning Brief`; never edited or deleted. No new notification plumbing needed — Dawn already DMs Lemar one line per run (below); that line now links to the new Doc instead of the old stable artifact URL. |
| Meeting Prep Drive folder | `1oAWUzSzZPs71oBp5ERkLBNe7aSZa2L80` (`ATLAS/Dashboards/Meeting Prep`, folder link `https://drive.google.com/drive/folders/1oAWUzSzZPs71oBp5ERkLBNe7aSZa2L80`). Same 2026-08-13 change. Every run creates a NEW Doc here, filename `YYYY-MM-DD HHMM ET — Meeting Prep`; never edited or deleted. Dawn's existing DM line links to it instead of the old artifact URL. |
| **Output surface** | **Lemar's DM — the Dawn bot IM `D0BJ0JPQD8C` with Lemar `U0BC5UTHYG4` (rerouted off #daily-brief 2026-07-16).** Dawn posts by sending to Lemar's user id, which auto-opens the IM (bot confirmed to have `im:write` — smoke-tested 2026-07-16, `ok:true`). This is Dawn's ONLY Slack surface. |
| Slack connector (Dawn's own bot identity) | connector_uuid `947737c2-a978-4dd1-93bb-cdd55ce14c97`, custom connector named "Slack (Dawn bot)", MCP endpoint `https://dawn-beryl.vercel.app/mcp`. Swapped into this trigger's `mcp_connections` 2026-07-16, replacing the shared personal Slack connector (`7faf04c0-5bd6-4237-8430-f80040c482e1`) for Dawn ONLY — Samira has her own separate bot connector (see above); Basil still uses the personal connector. Same generic server code as Samira's (`apps/samira-slack-bot/` in this repo), deployed as its own separate Vercel project ("dawn") with Dawn's own bot token — purely branding consistency, Dawn is one-way (never reads reactions back). Dawn now **DMs Lemar directly** (bot IM `D0BJ0JPQD8C`) — no channel invite needed (a bot can DM a workspace user without an invite). #daily-brief is being archived. |

## Cloud routine — Inbox Janitor / "Basil" (nightly Gmail cleanup, separate from Samira/Dawn)

Standalone nightly routine (~11pm ET). Thin bootstrap `.claude/routines/INBOX-JANITOR-TRIGGER.md`
→ fat runbook `.claude/routines/inbox-janitor.md`. Acts on Gmail ONLY (the connected account);
Drive is out of scope (connected Drive tools have no move/delete/trash). Ships with `DRY_RUN=true`
in the runbook until Lemar vets one preview run, then flip to false.

| What | Value |
|---|---|
| RemoteTrigger | `trig_01JE6TpvqAnawkETpx64vvX9` (created 2026-07-08 via RemoteTrigger API; enabled; first run 2026-07-09 03:07 UTC = 11:07pm ET) |
| Cloud env | `env_01Xatmag93x2WA2Gd84D9iHj` (shared with Samira + Dawn — Gmail + Slack MCP + git access) |
| Cron | `7 3 * * *` UTC (11:07pm EDT) — switch to `7 4 * * *` UTC during EST. Working branch `claude/inbox-janitor`; durable writes go to `main` per git-write policy. |
| Runbook (live behavior) | `.claude/routines/inbox-janitor.md` — editing on `main` changes the next run |
| Reports to | #reports `C0BBZJL85RT` (reuse; no new channel) |
| Gmail account acted on | `lemar@cuzziesnj.com` (business — confirmed as the connected Gmail account 2026-07-08; winds down mid-2026) |
| Vendor Menus label | `Label_8` (see the corrected Gmail labels table above — this id has changed twice now, verify live before relying on it) |
| Persona | lead `🧹`, sign "— Basil" (placeholder name, rename-able like "Dawn") |

**Trash sweep categories** (PART B): `category:promotions OR category:social OR category:forums`,
`older_than:1y`. `category:updates` is **report-only, never auto-trashed** (it holds invoices,
bank, payroll, insurance/legal receipts mixed with ads — see the runbook).

**Vendor-domain seed list** (PART A archives their *recent* menus out of the inbox; these are NOT
on the allowlist, so their >12-month marketing IS trashable in PART B). Expand as new menu
senders appear:
`qccnj.com` · `verano.com` · `terrascend.com` · `awholdings.com` · `freshcannabis.co` ·
`kivaconfections.com` · `illicitgardens.com` · `harvestmoonfarmsnj.com` · `apextrading.com`
(and `*.apextrading.com` seller subdomains) · `budsgoods.com` · `novafarms.com` ·
`prolificgrowhouse.com` · `parksgrove.com` · `laddsllc.com` · `missgrass.com` ·
`jerseysmooth.com` · `thegardensociety.com` · `arescanna.com` · `1906.shop` · `northlake.supply`

**NEVER-TOUCH allowlist** (PART B hard floor — sender domains never trashed; expand freely).
Seeded from a live-inbox recon on 2026-07-08 that found financial/legal mail routinely
mis-categorized as promotions/updates:
`intuit.com` · `notification.intuit.com` · `notifications.intuit.com` · `quickbooks` (any) ·
`tsheets.com` · `gusto.com` · `parkebank.com` · `fundcanna.com` · `firstinsurancefunding.com` ·
`pactsafe.com` · `docusign` (any) · `crc.nj.gov` and any `*.gov` · `accounts.google.com` and
`no-reply@accounts.google.com` (security alerts) · `headset.io` · `stellaconnect.net` (Metrc).
Plus the rule: never trash the active FundCanna underwriting thread. Anything `is:important` or
`is:starred` is already protected by the Safety floor regardless of this list.

## Idea-baking loop — Stormy (Convo 2's deep-dive mode since 2026-09-06)

**RESTRUCTURED 2026-09-06:** Stormy no longer has a channel. She is the deep-dive mode
of the PART 4 Convo 2 sweep — when a drop in Lemar's self-DM is worth pressure-testing
before it becomes work, Samira runs the Stormy instrument IN THAT THREAD, posting
🌐🌩️-signed via the PERSONAL connector, one message per scan. Graduation posts a
doctrine-format card to Convo 1 (the card's first decision round is the activation
call). The adaptive instrument (eight dimensions, sized question count, note-is-state)
is unchanged; #stormy is retired. The table below is kept as history where superseded.

### (History — the PART Q channel era, 2026-07-17 → 2026-09-06)

Stormy is Lemar's idea-baking engine, ported into the repo 2026-07-17 and — per Lemar the same
day — **folded into Samira's hourly run as PART Q** rather than given her own trigger. Different
lane from Atlas: Atlas captures right-now work; Stormy bakes no-deadline ideas through an
adaptive pressure test — she writes the questions for the specific idea and sizes the count to
its blast radius — until they are ready to launch, then hands off (she never executes).
**Design decisions (Lemar, 2026-07-17):** she runs inside Samira (no separate trigger/bot/
connector), posts through **Samira's existing bot** to a **private #stormy channel** signed
`🌩️ … — Stormy`; graduation is propose-and-confirm (no reaction engine); handoff is a Haven
note → Lemar fires Atlas Gear 2 from his capture DM; the instrument runs as organic
conversation. **Amended 2026-08-15:** the fixed 15-question form is retired — coverage is now
eight fixed dimensions, each closed as ASK / ASSUME / N/A, with 4-7 questions for a small idea,
8-12 medium, 13-20 large. The old form survives as a fallback library at
`.claude/skills/stormy/references/question-library.md`, and the instrument is **single-owner
by default** — the Cuzzie's/Station role and compliance scaffolding is gone, replaced by blast
radius and upkeep; a business-reaching idea is the flagged exception. See CHANGELOG. This **deliberately overrides** the skill's Constraint 7 ("never scheduled") —
documented in the runbook, the PART Q entry, and the skill's runtime banner.

| What | Value |
|---|---|
| Runs as | **PART Q of Samira** — no trigger, env, or connector of its own. Uses Samira's trigger `trig_01VGzAWGSadjRbJbKURxCYvG`, env `env_01Xatmag93x2WA2Gd84D9iHj`, and cadence (`0 12-22 * * *` UTC, hourly 8a–6p ET). |
| Behavior file (PART Q detail) | `.claude/routines/stormy-ideation.md` — Samira invokes it at PART Q. Editing on `main` changes the next run. |
| Skill (method/voice/instrument) | `.claude/skills/stormy/SKILL.md` — also invocable live ("stormy this idea") outside the loop. |
| Surface | **private #stormy channel `C0BJ37SU1TL`** (see the Slack table). Both read and write; excluded from the PART C prompt-sweep. |
| Identity / bot | **Samira's existing bot** (connector `01519dfa-b91a-47eb-beb4-cdc04444144e`, bot user `U0BJQ771LJU`), posts signed `🌩️ … — Stormy`. **No new Slack app, Vercel deploy, or connector** — that whole playbook is skipped because Stormy uses no reactions and only posts signed messages, so the identity-confusion the playbook solves does not apply. |
| Setup status | **Live-ready 2026-07-17:** #stormy created (`C0BJ37SU1TL`), Samira bot invited + confirmed in-channel. Remaining: one supervised PART Q run per `stormy-ideation.md`'s "First supervised run" (drop a seed idea in #stormy, watch one Samira scan bake it). |
| Persona | lead `🌩️`, sign "— Stormy" (placeholder name, rename-able like "Dawn"/"Basil") |

## Samira Loop — build + pressure-test (PT rounds inside PART 3 since 2026-09-06)

**RESTRUCTURED 2026-09-06:** 🧪 PT cards live in **Convo 1** (`D0BHPKMDNEP`), not
#decisions, and are advanced as decision rounds inside the PART 3 Convo 1 pass (same
eight lenses, same control line, same 3-cards-per-scan cap, same lanes and closeout).
Cloud builds are executed by Samira directly or carried on the card — the
`run:admin-3x` staging lane is retired with the PART C sweep; `run:manual` prompts
remain the hand-off format for Lemar's own machine. Rows below are kept as history
where superseded.

### (History — the PART R / #decisions era, 2026-08-19 → 2026-09-06)

Lemar's thread-to-build lane, added 2026-08-19. Anything a Claude thread produces (idea,
doc, deck, spec, page, code) is landed as a Haven note and opened as a **🧪 PT card** in
#decisions; Samira advances that card ONE round of an eight-lens pressure test per scan
until it locks, then either builds it in the cloud or hands Lemar a run-ready `run:manual`
prompt for his machine and runs PM on it. Different lane from Stormy (no-deadline ideas,
#stormy, never executes) and from Atlas Gear 1 (capture and develop): this one is the
same-day build lane.

| What | Value |
|---|---|
| Runs as | **PART R of Samira** — no trigger, env, bot, or connector of its own. Uses Samira's trigger `trig_01VGzAWGSadjRbJbKURxCYvG` and cadence (`0 12-22 * * *` UTC, 11 scans a day, 8a–6p ET). |
| The spec (one file, both halves) | **`.claude/skills/samira-loop/SKILL.md`** — the whole rulebook: cadence, lanes, capture-first, the PT card, the eight lenses, signals, closeout, reports, safety, degraded modes. A live thread invokes it when it builds something; Samira invokes it at PART R. |
| Project rulebooks (thin pointers) | `.claude/projects/samira-loop-project-instructions.md` (pasted into the claude.ai project "Samira's Loop") and `.claude/projects/camden-dispensary-launch-project-instructions.md`. Each is a short always-on wrapper that names the skill — the mechanics live in the skill and are never duplicated into a project box. Moved out of the projects file 2026-08-19, see CHANGELOG. |
| Behavior file (PART R detail) | `.claude/routines/samira-build-loop.md` — invoked at PART R. Editing on `main` changes the next run. |
| Surfaces | **#decisions `C0BBXA96FFV`** (the PT cards + every question — the only channel that pings him) · **#reports `C0BBZJL85RT`** (one line per state change, one-way) · the item's own project channel (cloud builds staged there as `run:admin-3x` for PART C) · Haven (the durable record). |
| Card marker | Parent's first line contains `🧪 PT ·`; last line of the parent is the control line `pt:<slug> · note:<path> · lane:<cloud\|local> · lenses:k/8`. **PART A skips any parent containing `🧪 PT`** so a card is never worked by two PARTs in one scan. |
| State | Reuses the existing `decisions_threads` watermarks in `.claude/state/samira-state.json` — **no new state key**. |
| Reactions | The standard engine, unchanged: ✅ agree · 👀 seen (carry, never re-ask) · ⛔ drop that line · 🫡 on the parent = lock it and build. Samira sets only the headline (🟡 baking · 🔴 needed today · 🟢 build ready · ⏳ waiting). |
| Cap | 3 cards get a round per scan, oldest first; the rest carry and the digest says so. |
| Digest token | `pt: <slug> r3 5/8 · <slug> locked · N carried` or `pt —`. |
| Lanes | **cloud** (Samira builds unattended) · **browser** (Claude in Chrome, in Lemar's own logged-in browser, with him present — reads/fills/captures, never submits, pays, sends, or clicks a binding button) · **local** (his machine). Default order cloud → browser → local. |
| Engagement overlays | A client engagement can layer its own rules on top of the loop: `.claude/projects/camden-dispensary-launch-project-instructions.md` (Camden Dispensary Launch — CRC licensing through inspection clearance). The overlay's engagement rules and safety floor outrank the loop's mechanics wherever they conflict. Its channel and folder ids are recorded below. |

## Camden Dispensary Launch (client engagement — overlay on the Samira Loop)

Lemar advising a client group through NJ CRC licensing to an inspected, cleared facility. He
is the advisor, not the owner. The engagement ENDS at inspection clearance; opening the store
is a separate, unpriced engagement ("opening services"). Rules, gates, and phase deliverables
live in `.claude/projects/camden-dispensary-launch-project-instructions.md`, which outranks
the samira-loop skill wherever the two disagree.

| What | Value |
|---|---|
| Vault index | `haven/vault/40-Projects/camden-dispensary-launch/index.md` — the engagement's note in Haven: the scope line, where everything lives, the six gates, the standing hazards, and what stays unknown. Start here when a Camden item surfaces and you need orientation. |
| Overlay (the rules) | `.claude/projects/camden-dispensary-launch-project-instructions.md` — pasted into the claude.ai project "Camden Dispensary Launch"; also read by any thread working the engagement. |
| Mechanics | the **samira-loop** skill (`.claude/skills/samira-loop/SKILL.md`), unchanged. |
| Questions / decisions | **Convo 1 (`D0BHPKMDNEP`)**, cards titled "Camden Launch" (moved off #decisions 2026-09-06). Never the project channel — same doctrine as every other project. |
| Project channel (timeline) | **#camden-launch `C0BRZT2V89W`** (private). Artifacts + outcome entries, append-only; never swept since 2026-09-06. Bot confirmed in-channel 2026-08-19. |
| Drive root | `1oLwp2UkmXX2AgxcxDO6sEfuxWtQUmBs1` — "Camden Dispensary Launch" (My Drive root, created 2026-08-19) |
| 00 Command Center | `1waKvkdsc9yr2ZAu_BhY8EneONKvtDhcM` — Working Log (read first), project instructions, handoffs, proposal PDF |
| ↳ Working Log | Doc `12JG69I2RWZ9l3rR7AdFZXhyiuM52FEhmqi-52S3OC9Q`. **The engagement's source of truth** for phase, status, milestones, and the decision record. Read before answering anything about where things stand; append to the decision record, never rewrite. |
| 01 Client-Facing | `1SE4aln7I35W0M_NSFA0Mo3sYuEkYRWAv` — everything the group could see; also holds the editable proposal |
| ↳ Phase 00 — Position Audit | `1IQLtHzpwgNMzt1Ko3iDgwmw1imoHcthB` |
| ↳↳ Intake — Documents from the Group | `17tQP09hT1cRcFzZASa32H23yI8Hv2Mc4` — everything they send lands here first |
| ↳ Phase 01 — Site Control and Local Endorsement | `19LZSkEsNPOK-UzU4ltvSg7Hmym9j9Tb_` |
| ↳ Phase 02 — Application Build | `1RPrKOTd36N03JaQRVreU3C806Yw39Z_u` |
| ↳ Phase 03 — Filing and Response | `1GZZg5OU__RLz95CrLUJ7s11FKLGy463g` |
| ↳ Phase 04 — Compliance Build | `1kzhifQen6G6zCCfvZ_a0RWPr57ZazPBR` |
| ↳ Phase 05 — Inspection and Clearance | `1S6HVdIYYx1i6qwu_ewLQwZ02KzgI-ddn` |
| 02 Internal | `13Xa1IbE4DUrTFT4xb04AFRTW1sfXVoay` — fee thinking, assessments of the group, opening-services planning. **Never shared or linked outward.** When unsure whether something is 01 or 02, it is 02. |
| Naming | `[phase]_[what it is]_[YYYYMMDD]`. New versions, never overwrites; the replaced file gets a `Superseded [date]` prefix. Already in practice — see the two superseded instruction/proposal docs in 00. |
| Still unknown (ask, never guess) | the group's name, property address, and contact · the planning board approval's conditions and expiration · whether site control is executed. |

## Pulse dashboard (rendered by Samira — no separate trigger)

Lemar's living one-page personal dashboard. Rendered at the END of every hourly Samira
scan (runbook **PART 8**, formerly PART P) by the **pulse-dashboard** skill (`.claude/skills/pulse-dashboard/`).
**Rendering target changed 2026-08-13** — the Artifact tool is retired for this skill (it
kept re-prompting Lemar for tool approval on his phone, the surface he checks Pulse from
most, and the repo-level permission allow-list couldn't reach that surface). Every render
now creates a NEW Google Doc snapshot in the Pulse Drive folder below; nothing is
re-deployed to a stable URL anymore, and no Slack canvas is involved (canvas creation is
blocked on this workspace's Slack plan). Still writes no vault notes. **Notification
changed 2026-08-13 too**: Pulse now DMs Lemar the new snapshot's link through Convo 1
(`D0BHPKMDNEP` — a 🌐 bot post there is never card input) —
but ONLY when this hour's run actually changed something (any of: a Convo 1 card
closed/opened, a money change, a project-pulse status flip, a new Haven note). A fully
quiet hour skips the render entirely — no Doc, no DM (codified 2026-08-15; this matches
what runs were already doing and stops filling the Drive folder with identical
snapshots). Its status still rides in Samira's digest every hour regardless:
`pulse ✅/⚠️` or `pulse — carried (quiet pass)`.

| What | Value |
|---|---|
| Pulse Drive folder | `1Dj_MZDlqUzHfAyK8TMwwJ57dZhi29omX` (`ATLAS/Dashboards/Pulse`, folder link `https://drive.google.com/drive/folders/1Dj_MZDlqUzHfAyK8TMwwJ57dZhi29omX`). Every render creates a NEW Doc here — filename `YYYY-MM-DD HHMM ET — Pulse` (zero-padded, so name-sort and time-sort agree) — never edited or deleted afterward; history is the point. Primary access is the DM link above; the folder is the archive. |
| Workout plan artifact URL | `https://claude.ai/code/artifact/a723834f-6310-4575-8897-75ae8e30806e` ("Back to the Court — 12-Week Plan"; source-of-truth note `haven/vault/10-Personal/Health/2026-07-07-basketball-fitness-plan.md`, start Mon 2026-07-07). Pulse links out to it; its check-offs live in that page's own localStorage. |
| Sections (Lemar's fixed top-to-bottom order, 2026-07-12: big ideas → details → execution) | quick-capture todo strip · Dawn as North Star (direction, NOT tasks) · calendar roadmap · #decisions respond list · money (Haven budget ledger) · today's workout · Atlas open items · project pulses · Samira + routine health. Single column. EVERY item links to its source thread (Slack permalink) or calendar event (htmlLink). |

## Money Hub (personal financial hub — rendered by the money-hub skill)

Lemar's personal budgeting center. Source of truth: `haven/vault/10-Personal/Money/
money-hub-ledger.md` (bills, plans, goals, the two pockets, the daily ramp) +
`income-log-2026.md` (earnings). The dashboard artifact and reminder-calendar events
are regenerated FROM the ledger by `.claude/skills/money-hub/SKILL.md` — on any live
interaction ("run my week", "new bill: …") and on money drops Samira finds in Convo 2
(the PART 4 sweep of Lemar's self-DM; replaced the #personal-finance sweep 2026-09-06). **Every figure is reported by Lemar — there is no bank connection.**
The Era Context connector was retired 2026-08-10 (kept disconnecting, data was a month
stale, and it covered only 2 accounts, one of them parked).

| What | Value |
|---|---|
| Allocation model | **DUE-DATE ORDER**, locked 2026-08-10 by Lemar. Every dated line sorts into one queue by date; soonest funded first. No priority tiers, no weekly floor, no waterfall. Replaces the Option 3 hybrid floor + waterfall (2026-07-24, RETIRED). |
| Pockets | TWO roles, accounts corrected 2026-08-10: **Spending** = DoorDash Crimson (income lands, gas paid from) and **Set-Aside** = SoFi Checking (recurring bills paid from). One instruction a day — move the set-aside number from Spending to Set-Aside. SoFi Savings and both Cash App accounts are parked, not deleted. Read the live mapping from the ledger's `pockets` block, never from memory. |
| Balances | **Reported, never fetched** (locked 2026-08-10). Each pocket carries `balance` + `balance_as_of`, set only when Lemar states a figure ("Spending has $240"). Unreported renders "not reported", never $0, and is never inferred from the income log. Older than 7 days renders stale with its true date. A reported balance is never adjusted to match what the ledger expected — show both and say so. |
| The one number | `daily_targets[today].total` — the single figure Lemar acts on, and the top of the dashboard. Everything else explains it. |
| Undated lines | A `track: queue` line with no date has no queue position, no event, and no ramp — it is INVISIBLE, not low-priority. Undated lines are a tracked defect class, surfaced in `open_questions`, on the dashboard, and in the money token of the run digest. Never invent a date. |
| Money Hub Drive folder | `1GtoHCj6Os2GDkdVd1nQtqxZr0UyVnZo4` (`ATLAS/Dashboards/Money Hub`, folder link `https://drive.google.com/drive/folders/1GtoHCj6Os2GDkdVd1nQtqxZr0UyVnZo4`). **Rendering target changed 2026-08-13** — replaces the retired Artifact re-deploy (same reason as Pulse, see that section). Every render creates a NEW Doc here, filename `YYYY-MM-DD HHMM ET — Money Hub`; never edited or deleted afterward. **Notification**: unlike Pulse, money-hub already has standing permission to post to **#personal-finance** — whenever a render actually changes the dashboard (the existing "only if something changed" gate), reply in that channel with the new snapshot's link, right where the triggering drop landed. No separate DM (Samira's shared bot has only the one DM slot, already used for capture). Folder is the archive. |
| Weekly view | ON DEMAND ONLY ("run my week", "what's due") — Lemar's call 2026-08-05; no scheduled allocation run. Shows the gap in dollars; never reorders the queue or picks which line slips. |
| Calendar events | Personal money → the reminder calendar; business money → Cuzzie's (Owners) (both in the Google Calendar section). Event ids live in the ledger rows, adopted from the four pre-hub events (Claude / Wispr Flow / Patreon / T-Mobile). Two popups on every new bill event: 7-day (`10080`) + day-of (`0`), locked 2026-08-09. |
| Guards | **OVERLOAD CHECK** (coming week's set-aside vs. trailing 4-week income average — flags the gap, never shrinks the number; dormant until the income log has ≥7 entries) and the **rollover brake** (a contribution rolling 3 days running gets named in #decisions instead of rolling forever). |

## Identity

| What | Value |
|---|---|
| Lemar business | lemar@cuzziesnj.com (Cuzzie's winds down mid-2026 — do not build on it) |
| Lemar personal / durable | l.boonejr@gmail.com · 856-602-0820 (car hunt: private buyer, never a Cuzzie's title) |
| Lemar Slack user id | `U0BC5UTHYG4` (display "Mar" — changed from "Don Frunt" 2026-07-17) |
| Samira Slack posts | lead with 🌐, sign "— Samira" · posts and reacts through her own dedicated bot connector (see Cloud routine — Samira above; bot user `U0BJQ771LJU`) on every surface EXCEPT Convo 2: in Lemar's self-DM (`D0BBVV54L5R`) she posts via the personal connector, always 🌐-prefixed (🌐🌩️ in deep-dive/Stormy mode) — the prefix is the only thing marking those messages as hers. Cards reach her in Convo 1 (`D0BHPKMDNEP`) and #fixes; intake in Convo 2. |
| Dawn (Daily Brief) Slack posts | lead with 🌅, sign "— Dawn" · posts only to Lemar's DM (bot IM `D0BJ0JPQD8C`, user `U0BC5UTHYG4`) — rerouted off #daily-brief 2026-07-16 — through her own dedicated bot connector (see Cloud routine — Daily Brief above), not Lemar's personal Slack account. ("Dawn" is a placeholder persona name — rename freely; it lives only in the two skills + this row.) |
| Basil (Inbox Janitor) Slack posts | lead with 🧹, sign "— Basil" · posts only to #reports `C0BBZJL85RT`. ("Basil" is a placeholder persona name — rename freely; it lives only in the runbook + this row.) |
| Stormy (idea baking) Slack posts | lead with 🌐🌩️, sign "— Stormy" · deep-dive mode of the PART 4 Convo 2 sweep since 2026-09-06: posts ONLY in-thread in Lemar's self-DM (`D0BBVV54L5R`), via the PERSONAL connector (the self-DM is bot-unreachable). Never reads or sets reactions; never posts anywhere else. ("Stormy" is a placeholder persona name — rename freely; it lives only in the skill, the deep-dive behavior file, and this row.) |
