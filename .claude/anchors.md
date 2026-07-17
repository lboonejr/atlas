# ANCHORS — the single registry of platform IDs

This file is the ONE place every platform-specific identifier lives. Every skill, the
Samira runbook, and any future tool reads this file instead of carrying its own copy.
When a workspace, board, account, or channel changes, edit THIS file and nothing else.

> Rule: no other file in this repo may restate these IDs (quoting one inline while
> doing work is fine; maintaining a second list is not). The memory file
> `shortlist_anchors.md` on Lemar's machine is a pointer to this file, not a copy.

Last verified: 2026-07-16 (added the Voice profile section — canonical profile moved into the repo) · 2026-07-16 (Dawn rerouted off #daily-brief → now posts to Lemar's DM, bot IM `D0BJ0JPQD8C`; #daily-brief being archived) · 2026-07-16 (Atlas capture inbox moved off #atlas → Lemar's DM with Samira's bot, `D0BHPKMDNEP`; #atlas being archived) · 2026-07-17 (added Cloud routine — Stormy: the idea-baking DM routine; runbook `.claude/routines/stormy-ideation.md` + trigger live, but her bot connector, RemoteTrigger id, and DM id are PENDING the 8-step Slack-bot-identity playbook — marked TBD below).

## Repo / vault

| What | Value |
|---|---|
| Repo | `lboonejr/atlas` |
| Canonical branch | `main` — flipped to the default branch in GitHub Settings → Branches (confirmed live 2026-07-08). Everything reads/writes `main`. |
| Vault root | `haven/vault/` · Inbox `haven/vault/00-Inbox/` · Schema `haven/vault/_system/schema.md` |
| Skills (canonical) | `.claude/skills/` (repo). Local `C:\Users\lemar\.claude\skills\` copies are read-only mirrors. |
| Runbook (live behavior) | `.claude/routines/samira-atlas-executor.md` — the trigger bootstraps into this file; editing it changes the live routine. |
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
| Wired draft-skills (repo) | `samira-email-loop` (D1 save gate + D3 draft-options), `samira-investor` (I3 outreach), `samira-car-search` (F3 — floors apply except signature floor 7, which yields to the private-buyer identity). Each reads the profile and runs its Hard-Floor Lint before saving. |
| Not-yet-wired (not in this repo) | `task-builder`, `Aaron` (aaron-exec), `Chase` (chase-commitments) are anthropic-skills plugin/session skills, not vendored here — they can't be wired via local git yet. Wire them when the pending chat-skills→repo conversion lands them in `.claude/skills/`. Until then, the profile's header-block precedence rule governs any voice they draft. |
| email-responder (retired from send path) | The vendored `anthropic-skills:email-responder` is retired from the send path — `samira-email-loop` owns email drafting. If it ever fires, the canonical profile's header-block precedence rule governs: the profile supersedes email-responder's `references/writing-style.md` (which conflicts, e.g. it permits em dashes; the profile forbids them). Do not blend them. |

## Slack (workspace "Marspace", newworkspace-zlb6313)

| Channel | ID | Role |
|---|---|---|
| #decisions | `C0BBXA96FFV` | THE decision surface — only channel that pings Lemar (renamed #action-items, same ID) |
| #reports | `C0BBZJL85RT` | Silent one-way result log; never swept for prompts |
| Samira capture DM (Lemar) | `D0BHPKMDNEP` | **Atlas capture inbox since 2026-07-16** — Lemar↔Samira bot IM. Lemar drops brain-dumps here; Samira sweeps them in PART B (im:write/im:history/reactions all confirmed via smoke test 2026-07-16) and reacts ✅ for her sweep-dedup. Replaced #atlas. Excepted from PART C (capture surface, not a prompt source) |
| #atlas (RETIRED) | `C0BBWHCJUV9` | Former raw capture inbox — **retired 2026-07-16**, replaced by the Samira capture DM (above). Being archived; during the transition Samira still glances here in PART B for stray top-level captures, but never posts here |
| #admin | `C0BBLUA7JLX` | Staged run:admin-3x prompts |
| Dawn DM (Lemar) | `D0BJ0JPQD8C` | **Dawn's output surface since 2026-07-16** — the Dawn bot's direct message with Lemar (`U0BC5UTHYG4`). The bot posts by sending to Lemar's user id, which auto-opens this IM (bot has `im:write`). Dawn's ONLY Slack surface; Samira never posts here. Replaced #daily-brief |
| Stormy DM (Lemar) | **TBD** — `D-STORMY-TBD` | **Stormy's ONLY surface** — the Stormy bot's direct message with Lemar (`U0BC5UTHYG4`), where he drops raw no-deadline ideas and she bakes them hourly. Bot posts by sending to Lemar's user id, which auto-opens this IM (needs `im:write`). Fill in the real IM id after the bot is installed (mirrors how Dawn's `D0BJ0JPQD8C` was captured). Samira/Dawn never post here; Stormy never posts anywhere else. See "Cloud routine — Stormy" below |
| #daily-brief (RETIRED) | `C0BF73FF56H` | Dawn's former once-a-day surface — **retired 2026-07-16**, Dawn now DMs Lemar (see "Dawn DM" above). Being archived; read-only record, never posted to |
| #car-search | `C0BEC2RFC00` | Car loop (samira-car-search); never swept in PART C |
| #investor-pipeline | `C0BCCUKEUQ2` | Investor loop (samira-investor) |
| #skills-lab | `C0BBZ5J8805` | Skill-candidate proposals |
| #on-button | `C0BEQUW5NPP` | Reopening command center — drop past-due bills/screenshots here. The **on-button-plan** skill ingests drops into the ONE source of truth `haven/vault/40-Projects/on-button-reopen/index.md`, then regenerates the interactive page `on-button-reopen.html` (githack: `https://raw.githack.com/lboonejr/atlas/main/on-button-reopen.html`) and the pinned canvas `F0BEN1167GB`. Tracking only, nothing paid/contacted. |
| #personal-finance | `C0BGLEMH99T` | Personal bills/budget dashboard project (created 2026-07-11 from an #atlas capture). Source of truth: `haven/vault/00-Inbox/2026-07-11-personal-finance-dashboard-project.md` (files to 10-Personal/Money once complete). |
| #pitch-deck-pressure-test | `C0BCD7U5X2B` | Recapitalization deck ($500K) pressure-test Q&A thread |
| #cuzzys-brand | `C0BCH2C3GRM` | White-label brand project (recorded 2026-07-12 for Pulse link-outs) |
| #delivery-in-a-box | `C0BDN2KQFD4` | DIB project channel (recorded 2026-07-12 for Pulse link-outs) |
| #comedy-club | `C0BD8LTM1EK` | Comedy-club project channel — PRIVATE (recorded 2026-07-12 for Pulse link-outs) |
| #trading-cards | `C0BGYM1UB4Y` | Sports-cards side hustle (recorded 2026-07-12 for Pulse link-outs) |
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
| Samira/investor-sent | `Label_9` — created in an earlier investor-loop run; recorded here 2026-07-10 (was previously marked NOT YET CREATED even though the label already existed in Gmail) |
| Vendor Menus | `Label_8` (created 2026-07-08 for the Inbox Janitor routine) |

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
| Slack connector (Samira's own bot identity) | connector_uuid `01519dfa-b91a-47eb-beb4-cdc04444144e`, custom connector named "Samira", MCP endpoint `https://samira-two.vercel.app/mcp`. Swapped into this trigger's `mcp_connections` 2026-07-16, replacing the shared personal Slack connector (`7faf04c0-5bd6-4237-8430-f80040c482e1`) for Samira ONLY — Dawn and Basil still use the personal connector. Fixes the reaction-engine identity gap (Samira's posts/self-tag reactions were previously indistinguishable from Lemar's real reactions since both came from his own Slack account). Server code: `apps/samira-slack-bot/` in this repo, deployed free on Vercel; bot token lives only in Vercel's environment settings. Bot must stay invited (`/invite @Samira`) in every channel Samira posts/reads: #decisions, #reports, #atlas (until archived), #admin, #car-search, #investor-pipeline, plus active project channels. **Captures now arrive in Samira's DM with Lemar (`D0BHPKMDNEP`) — a DM needs no invite; the bot swept it fine in the 2026-07-16 smoke test.** |

## Cloud routine — Daily Brief / "Dawn" (separate from Samira)

Once-a-day 1am ET routine that complements Samira. Thin bootstrap
`.claude/routines/DAILY-BRIEF-TRIGGER.md` → fat runbook `.claude/routines/daily-brief.md`.

| What | Value |
|---|---|
| RemoteTrigger | `trig_01BFg7YLWvhoegvWLCjGYtx3` (created 2026-07-05; daily 1am ET; bootstraps `.claude/routines/DAILY-BRIEF-TRIGGER.md`) |
| Cloud env | `env_01Xatmag93x2WA2Gd84D9iHj` (shared with Samira — same connectors + git access) |
| Cron | `0 5 * * *` UTC (1am EDT) · `0 6 * * *` UTC during EST — revisit at DST |
| Runbook (live behavior) | `.claude/routines/daily-brief.md` — editing on the default branch changes the next run |
| Living brief artifact URL | `https://claude.ai/code/artifact/125d4d13-c1ae-4f9c-8861-e173b56635e5` — first published 2026-07-05 (manual dry run). morning-brief re-deploys to THIS same URL each run (pass it as `url`). |
| Living meeting-prep artifact URL | `https://claude.ai/code/artifact/b0143e64-a665-44e1-af48-33db2f88457e` — first published 2026-07-08 (first day with a qualifying call). meeting-prep re-deploys to THIS same URL each run (pass it as `url`). |
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
| Vendor Menus label | `Label_8` |
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

## Cloud routine — Stormy (idea-baking DM routine, separate from Samira/Dawn/Basil)

Hourly ideation routine on Samira's cadence (8a–6p ET). Thin bootstrap
`.claude/routines/STORMY-TRIGGER.md` → fat runbook `.claude/routines/stormy-ideation.md`. Her
method, voice, and 15-question instrument live in the skill `.claude/skills/stormy/SKILL.md`.
Lemar drops raw no-deadline ideas in the Stormy DM; she bakes each through the pressure test
across successive hourly scans, then hands the locked brief to Atlas Gear 2 (she never creates
a channel or executes). **Design decisions (Lemar, 2026-07-17):** dedicated DM surface;
propose-and-confirm graduation (no reaction engine); Haven note → Samira/Atlas Gear 2 handoff
fired by Lemar; the 15-Q instrument runs as organic conversation. This routine **deliberately
overrides** the skill's Constraint 7 ("never scheduled") per Lemar — documented in both the
runbook and the skill's runtime banner.

| What | Value |
|---|---|
| RemoteTrigger | **TBD — not yet created.** Create hourly `0 12-22 * * *` UTC (8a–6p ET during EDT; DST-shift like Samira/Dawn), bootstrapping `.claude/routines/STORMY-TRIGGER.md`. **Do not create until Stormy's bot connector exists** — an hourly trigger firing into a bot-less DM errors every hour. Record the `trig_...` id here once created. |
| Cloud env | `env_01Xatmag93x2WA2Gd84D9iHj` (shared with Samira/Dawn/Basil — same connectors + git access) |
| Cron | `0 12-22 * * *` UTC (hourly 8a–6p EDT) · shift the same way Samira/Dawn do at the DST switch |
| Runbook (live behavior) | `.claude/routines/stormy-ideation.md` — editing on `main` changes the next run |
| Skill (method/voice/instrument) | `.claude/skills/stormy/SKILL.md` |
| Output/input surface | **Stormy DM with Lemar** (bot IM `D-STORMY-TBD`, user `U0BC5UTHYG4`) — her ONLY surface, both read and write. Fill in the real IM id after the bot is installed. No channel invite needed (a bot DMs a workspace user without one). |
| Slack connector (Stormy's own bot identity) | **TBD** — run the 8-step Slack-bot-identity playbook (same as Samira/Dawn): create a Slack app "Stormy", deploy the generic `apps/samira-slack-bot/` server as its own Vercel project with Stormy's bot token, register a claude.ai custom connector at its `/mcp` endpoint, then swap that connector_uuid into this trigger's `mcp_connections` (replacing the shared personal connector `7faf04c0-5bd6-4237-8430-f80040c482e1`). Record connector_uuid + endpoint + Vercel project name here once live. |
| Bot Token Scopes (minimal — DM-only, propose/confirm graduation, no reactions) | `chat:write`, `im:write`, `im:history`, `users:read`. (Subset of the full playbook scope list — she watches only her own DM and never reads/sets reactions, so `channels:*`, `groups:*`, and `reactions:*` are not needed.) |
| Persona | lead `🌩️`, sign "— Stormy" (placeholder name, rename-able like "Dawn"/"Basil") |

## Pulse dashboard (rendered by Samira — no separate trigger)

Lemar's living one-page personal dashboard. Rendered at the END of every hourly Samira
scan (runbook **PART P**) by the **pulse-dashboard** skill (`.claude/skills/pulse-dashboard/`)
and re-deployed to ONE stable artifact URL. Rendering only — writes no vault notes, posts
nothing to Slack; its status rides in Samira's digest as `pulse ✅/⚠️`. Fallback if the
Artifact re-deploy breaks headless: a Slack canvas updated in place, or the githack
pattern used by on-button-reopen.

| What | Value |
|---|---|
| Living Pulse artifact URL | `https://claude.ai/code/artifact/6838142e-852c-44a5-8778-b584be1316d4` — first published 2026-07-12 (desktop session, v1). PART P re-deploys to THIS same URL each run (pass it as `url`; keep title "Pulse — Personal Dashboard" + favicon 📍). |
| Workout plan artifact URL | `https://claude.ai/code/artifact/a723834f-6310-4575-8897-75ae8e30806e` ("Back to the Court — 12-Week Plan"; source-of-truth note `haven/vault/10-Personal/Health/2026-07-07-basketball-fitness-plan.md`, start Mon 2026-07-07). Pulse links out to it; its check-offs live in that page's own localStorage. |
| Sections (Lemar's fixed top-to-bottom order, 2026-07-12: big ideas → details → execution) | quick-capture todo strip · Dawn as North Star (direction, NOT tasks) · calendar roadmap · #decisions respond list · money (Era Context + Haven budget note) · today's workout · Atlas open items · project pulses · Samira + routine health. Single column. EVERY item links to its source thread (Slack permalink) or calendar event (htmlLink). |

## Identity

| What | Value |
|---|---|
| Lemar business | lemar@cuzziesnj.com (Cuzzie's winds down mid-2026 — do not build on it) |
| Lemar personal / durable | l.boonejr@gmail.com · 856-602-0820 (car hunt: private buyer, never a Cuzzie's title) |
| Lemar Slack user id | `U0BC5UTHYG4` (display "Mar" — changed from "Don Frunt" 2026-07-17) |
| Samira Slack posts | lead with 🌐, sign "— Samira" · posts and reacts through her own dedicated bot connector (see Cloud routine — Samira above), not Lemar's personal Slack account. Captures reach her via the Samira capture DM `D0BHPKMDNEP` (PART B). |
| Dawn (Daily Brief) Slack posts | lead with 🌅, sign "— Dawn" · posts only to Lemar's DM (bot IM `D0BJ0JPQD8C`, user `U0BC5UTHYG4`) — rerouted off #daily-brief 2026-07-16 — through her own dedicated bot connector (see Cloud routine — Daily Brief above), not Lemar's personal Slack account. ("Dawn" is a placeholder persona name — rename freely; it lives only in the two skills + this row.) |
| Basil (Inbox Janitor) Slack posts | lead with 🧹, sign "— Basil" · posts only to #reports `C0BBZJL85RT`. ("Basil" is a placeholder persona name — rename freely; it lives only in the runbook + this row.) |
| Stormy (idea baking) Slack posts | lead with 🌩️, sign "— Stormy" · posts and reads ONLY the Stormy DM with Lemar (bot IM `D-STORMY-TBD`, user `U0BC5UTHYG4`) through her own dedicated bot connector (see Cloud routine — Stormy above), not Lemar's personal Slack account. Never reads or sets reactions; never posts to any channel. ("Stormy" is a placeholder persona name — rename freely; it lives only in the skill, the runbook, and this row.) |
