# CHANGELOG — system history (moved out of the runbook)

The runbook (`.claude/routines/samira-atlas-executor.md`) describes what runs NOW.
History and cutover narratives live here.

## 2026-08-15 — Stormy goes adaptive and single-owner (the fixed 15 questions are retired)
Lemar asked that Stormy stop asking the same questions every bake and instead decide both the
questions and how many of them from what is actually being presented. The evidence was the
`money-hub-rebalance-steward` bake finished the same day: on a personal-ledger software change
with one owner, four of the fifteen mandatory questions came back "Lemar only," "none," "no,"
and "N/A" — and none of the fifteen asked the thing that actually mattered, which was how
aggressive the rework logic should default to.

What changed, in `.claude/skills/stormy/SKILL.md` and `.claude/routines/stormy-ideation.md`:
- **Coverage is fixed, questions are not.** Eight dimensions (problem/beneficiary, scope/
  constraint, success/failure, dependencies/risk, timing, compliance, automation, delegation)
  must each be closed before a plan can lock, but closing one means recording a verdict:
  **ASK** (write a question in this idea's own vocabulary), **ASSUME** (the answer is obvious —
  state it on the note and in the batch message so a wrong one gets corrected in a line), or
  **N/A** (with the reason). Silence on a dimension blocks the lock, so the instrument stays a
  pressure test rather than becoming a vibe check.
- **Count scales to blast radius.** 4-7 questions for a small idea (one surface, one owner,
  reversible), 8-12 medium, 13-20 large (multi-party, regulated, real spend, hard to unwind).
  Stormy states the size call up front and offers the tighter/deeper fork. Skill specs move
  from a fixed 4 per skill to 2-6.
- **Crux rule.** At least a third of the asks must be questions the old form would never have
  produced, and the first batch leads with one.
- **Re-verdicting mid-bake.** An answer that settles a planned question flips it to ASSUME and
  it goes unasked; an answer that opens a hole earns a follow-up over the band; a corrected
  assumption sends its dimension back to ASK. "Stop asking, just bake it" closes every open
  dimension as a stated assumption rather than an unstated one.
- **The note carries the plan.** A new `## Pressure test plan` section records all eight
  verdicts, which is what makes the bake auditable and — in the hourly loop, where a bake spans
  days of scans — resumable. Resume now picks up at the first open dimension, not "the last
  answered question."
- The retired form is kept as a **fallback wording library** at
  `.claude/skills/stormy/references/question-library.md`. Raid it for a genuinely generic
  dimension; never run it top to bottom.

**Same day, second pass — Stormy is single-owner now.** Lemar: *"strip the Cuzzie's of it all,
this is a tool for me and will most likely only involve me."* The instrument was carrying
scaffolding from a multi-store operation into ideas he builds for himself. Removed the Role
Config Block (CEO, station ops lead, inventory lead, admin lead, counsel, both accountants) and
replaced it with an **Owners** list whose default is Lemar and whose only other entries are his
own agents — Samira's run, Atlas Gear 2, Dawn's run, a named skill. Two dimensions were
repointed rather than deleted, since the business version of each has a sharper personal
version:
- **Compliance → Blast radius & reversibility.** What happens when it misfires, whether
  anything leaves his control (money moved, mail sent, something posted, a vault note
  overwritten), and how he undoes it. "It only proposes, so there is nothing to undo" is now a
  first-class answer, and it is the shape most of his tools should have.
- **Delegation → Ownership & upkeep.** Not *who else could run this* — nobody else will — but
  whether he runs it by hand or it runs itself, what it costs to keep alive, and how he finds
  out when it breaks. Silent failure is how these actually die.

Dimension 1 moved from "problem & beneficiary" (the beneficiary is always him) to "problem &
payoff," which also asks what he does today instead. The size bands are re-cut around personal
blast radius, with a note that small and medium are the normal case and large is not something
to talk an idea into. Reggie and Chase are now explicitly **exception gates** — a personal tool
trips neither. The business-shaped questions survive in a clearly marked exception section of
the question library, for the rare idea that genuinely reaches a store or an outside party;
Stormy flags those and sizes them up a band rather than assuming them.

Touched with both passes: the runbook's PART Q summary and the two anchors rows describing the
instrument. Nothing about Stormy's surfaces, identity, capture-first law, the no-`due` rule, or
the bake/execute line moved.

## 2026-08-15 — Routine-efficiency overhaul (run lock, watermarks, integrity cadence, dead-weight removal)
Lemar asked for a review of where Samira's hourly routine wastes work; the July–August
`_daily` journals supplied the evidence (ten passes on 8/14 alone). Changes, in one PR:
- **PART 0 (new): run lock.** The overlapping-trigger-fire bug (recurring since at least
  7/29) had concurrent passes duplicating #decisions cards, double-capturing facts, and
  making wrong-premise calendar writes. A run now claims a lock in the new state file
  `.claude/state/samira-state.json` and a second fire inside 45 minutes exits silently.
- **PART 0 (new): per-surface watermarks.** The state file stores last-read Slack `ts`
  per channel, per-thread latest-reply `ts` for open #decisions cards (a Lemar reply sat
  unseen two scans on 8/15), the capture-DM `ts`, and a Gmail `after:` epoch. Passes
  stop reconstructing "since the last run" from digest prose and stop re-reading full
  histories. samira-email-loop D2 now runs ONE canonical query off the epoch.
- **Integrity cadence** (schema §4.5 amended): full whole-vault pass once per day;
  hourly passes go incremental via `git diff` since the last recorded scan commit. Was
  4–5 full ~500-note passes a day, almost always zero-yield.
- **PART G merged into PART C.** Every journal since early August said "covered inside
  PART C's sweep" — the spec now matches; project channels are read once. G is a
  tombstone like F.
- **Monday gate formally closed.** The 7/11 gate passed a month ago with no review ever
  run; the mirror board returned `not found` on 8/14. All mirror steps removed from the
  runbook + samira-report-result; boards are read-only history in anchors.
- **Dead text removed:** the #atlas transition glance (channel archived,
  `not_in_channel` for weeks), the completed v5 pre-flight section, the retired car
  count in the digest spec.
- **Canvas refresh conditional:** while the bot lacks editor access (standing gap since
  7/25), the step is skipped entirely; access re-checked once a day and recorded in the
  state file.
- **Batch renders:** PART M applies all of a pass's ledger changes (recompute included —
  money-hub now locks "never deferred") then renders once; Pulse's quiet-pass skip
  (no Doc, no DM when nothing changed) is codified in anchors + skill, replacing "a
  quiet hour still creates the Doc."
- **Slim `_daily` entries:** digest block + short delta list; the long per-PART
  narrative is retired since checkpoints now live in the state file.
- **Local-clone preference** codified in the runbook intro (faster than GitHub-API
  roundtrips, first observed 8/14).

## 2026-08-13 — Pulse, Money Hub, morning-brief, meeting-prep move off the Artifact tool to Drive snapshot Docs
- **The problem.** Lemar flagged (first on 2026-07-13, again on 2026-08-13) that the
  Artifact tool kept prompting him for approval on his phone — the surface he checks
  Pulse from most. A repo-level `.claude/settings.json` allow-list fix landed for the
  Artifact tool, but it can only reach sessions that load this repo's project settings;
  a phone session apparently doesn't (or didn't at the time). Rather than keep chasing a
  permission-prompt fix, Lemar chose a different mechanism entirely.
- **The new mechanism.** All four skills that used to publish/re-deploy a claude.ai
  Artifact now write a **new, timestamped Google Doc into a dedicated Drive folder on
  every render** — `ATLAS/Dashboards/{Pulse, Money Hub, Morning Brief, Meeting Prep}`
  (folder ids in `.claude/anchors.md`). A prior snapshot is never edited or deleted;
  the folder is the history. The HTML each skill already built for its Artifact is
  reused verbatim as `textContent` with `contentMimeType: "text/html"` — Drive's
  HTML→Doc conversion keeps headings/bold/color/tables but drops CSS grid/flexbox, so
  the skills were told to keep markup simple.
- **Two ruled-out alternatives, for the record.** A Drive **shortcut** file that gets
  repointed to the newest snapshot (a stable one-bookmark link) isn't buildable — the
  connected Google Drive tools have no shortcut-create/retarget primitive, only
  create-new-file, copy, and read. A **Slack canvas** pointer, updated in place per
  render, was the next choice, but canvas *creation* via API is blocked on this
  workspace's Slack plan (`not_supported_free_team`) — the two existing pinned canvases
  (Open Items, on-button) were created by hand through the Slack UI, not by a bot, and
  *editing* an existing canvas still works fine. Lemar chose not to hand-create four
  canvases and instead settled on the notification design below.
- **How "latest" gets surfaced, per dashboard:**
  - **Morning brief / meeting prep** — no new plumbing. Dawn already DMs Lemar one line
    per daily run; that line now links to the new Doc instead of the old stable
    artifact URL.
  - **Pulse** — previously posted nothing to Slack by design (hourly, 8a–6p ET). Now
    DMs the new snapshot link through the Samira capture DM (`D0BHPKMDNEP` — the shared
    bot's only DM slot), but ONLY when the hour actually changed something (a
    #decisions card opened/closed, money changed, a project pulse flipped, a new Haven
    note). A quiet hour still creates the Doc for the record, just skips the DM.
  - **Money Hub** — already had standing permission to post to #personal-finance; now
    replies there with the new snapshot's link whenever a render changes something
    (reusing the existing "only if changed" gate), in the same channel the triggering
    drop landed in.
- **Files touched:** `.claude/anchors.md` (Pulse/Money Hub/Morning Brief/Meeting Prep
  Drive folder ids replace the four artifact-URL rows), the four skills' `SKILL.md`,
  `.claude/routines/samira-atlas-executor.md` (PART P, PART M wording), and
  `.claude/routines/daily-brief.md` (PART 1/2, SAFETY, pre-flight section rewritten for
  the new mechanism — the old Artifact-viability pre-flight is superseded, not deleted
  from history; see the 2026-07-05 entry below for that original bootstrap).

## 2026-08-03 — Integrity pass: vault-keeper now repairs broken frontmatter vault-wide
- **The hole this closes.** Filing only ever looked at `00-Inbox`, so once a note was filed
  (or landed outside the Inbox by hand) nothing re-examined it. Malformed notes accumulated
  exactly where the enforcement mechanism could not see them, and stayed broken
  indefinitely. Four were found this way — none in the Inbox.
- **New schema §4.5, executed as vault-keeper step 0**: every sweep reads the frontmatter
  block of every note in the vault (block only, not bodies — cheap) and repairs the
  mechanical defects same-day.
- **Container vs. value — the distinction that makes this safe.** A broken *container* (stray
  line above the `---` opener, missing opener, base64-encoded file, CRLF) has exactly one
  correct repair and no judgment in it. A missing or out-of-list *value* (`domain`, `type`,
  `status`, `source`) is a judgment call and still waits for a human, unchanged. Repairing a
  container grants no licence to fill in a value.
- **The lossless gate on base64 decodes**: decode only if the bytes are valid UTF-8, AND
  re-encoding reproduces the file byte-for-byte, AND the result starts with valid
  frontmatter. Any failure means flag and write nothing — a partial decode that silently
  drops bytes is worse than the corruption.
- **Prior decisions stand.** If a note records that a previous run or a human examined a
  defect and chose to leave it, that decision is not relitigated. This rule exists because
  `_daily/2026-08-01.md` contains exactly such a note — Samira found the corruption, tested
  the decode, found bytes unrecoverable, and deliberately left it. An eager repair pass
  would have bulldozed that.
- **`_daily` carve-out, narrow and deliberate** (amends the old absolute "never touch
  `_daily`"): the frontmatter block may be repaired, **not one line below the closing `---`**
  may be touched, and the file is still never moved. The append-only law protects the day's
  logged entries; a broken block is the container around them, not an entry.
- **Synthesized precision must be visible as synthesized.** On a `_daily` reconstruction the
  controlled fields come from `_templates/daily.md` and the date from the filename, but the
  times are not recoverable — so they are set to `00:00` ET and disclosed as synthesized in
  YAML comments inside the block itself (keeps it discoverable at the top while touching
  zero body lines).
- **No hourly re-escalation.** An unrepairable defect never goes away, so surfacing it every
  sweep is noise — and digest fatigue is what let these hide. New/changed defects report in
  full; known-and-accepted ones carry as a bare count (`repaired 0 · known 1`). The line is
  never omitted, so a quiet pass and a skipped pass can't be confused.
- **Values are validated vault-wide too, and only ever flagged.** Field validation used to
  run only on Inbox notes, so a filed note could sit for months missing required fields or
  holding a value in no controlled list. The pass now checks all six fields present, every
  controlled field in-list, and `domain` consistent with the note's actual location — and
  fixes none of it: never invent a `created`, never map an out-of-list value onto the nearest
  legal one, never re-file to match `domain` (a mismatch means the frontmatter or the
  location is wrong, and which is a judgment call). This immediately caught a fifth note,
  `40-Projects/delivery-in-a-box/2026-07-10-status-briefing.md` — missing `created`/`updated`/
  `tags`, `type: project` and `source: samira-atlas-executor-part-g` both outside the
  controlled lists, and `domain: cuzzies` contradicting its `40-Projects/` location. Left for
  Lemar, as the rule requires.
- **Applied to the four found**: `20-Cuzzies/2026-07-31-garden-society-past-due-ar-followup.md`
  decoded from base64 (gate passed byte-perfect); `_daily/2026-07-15.md` missing `---` opener
  inserted; `_daily/2026-07-07.md` frontmatter reconstructed and disclosed;
  `_daily/2026-08-01.md` left alone — lossy decode, prior decision stands. Verified across
  all 401 notes: 1 remaining defect, correctly the protected one.

## 2026-08-03 — New `automation` domain; Basil categorizes its own run logs
- **Root cause fixed, not the symptoms.** Basil's PART C told it to file a Haven note via
  haven-capture but never said what `domain` to stamp, so every nightly log landed in
  `00-Inbox` with `domain:` UNRESOLVED and waited on Lemar. Seven had piled up (7/28–8/03)
  and the count grew by one a night. Basil now stamps its own frontmatter.
- **New controlled domain `automation` → `70-Automation/<routine>/`** (Lemar's call over
  reusing `project`): the bots doing unattended workspace admin get their own domain, one
  subfolder per routine. `70-Automation/inbox-janitor/` is Basil's.
- **The boundary that keeps filing deterministic:** a routine reporting *its own run* is
  `automation`; work on *building or fixing* a routine stays `project` → `40-Projects/`.
  A run log never changes domain based on what the run touched — a night of all-Cuzzie's
  vendor menus is still `automation`, not `cuzzies`. Written into schema §3, and into
  vault-keeper as "never re-read a run log's contents to reclassify it."
- **Unlike `project`, a missing routine slug is not a gap** — `automation` files to the
  `70-Automation/` root rather than sticking in the Inbox, so a run log always has a home
  and this class of note can never block on a human again.
- **Schema propagated** to every place the controlled list is enumerated: `_system/schema.md`
  (§2 folder circuit, §3 table + the new automation rule, §4 filing rules), `haven/README.md`,
  `_system/home.md`, `haven-capture` (both domain lists + the per-field certainty guidance),
  `haven-vault-keeper` (validation table + filing rules).
- **Backfilled all 27 historical janitor logs** into `70-Automation/inbox-janitor/`, restamped
  `domain: automation`. They had been filed three different ways — 16 `cuzzies`, 3 `personal`,
  1 `project`, 7 unfiled — which is what the missing instruction produced. `created` preserved,
  `updated` touched, bodies untouched. Wiki-links are filename-only so they still resolve;
  stale paths inside `_daily` digests were deliberately left alone (append-only zone, and they
  are accurate records of where a note sat that day).
- **Two Inbox items resolved with it** (Samira's card ts `1785679499.204679`): the Camden city
  council note → `domain: personal` → `10-Personal/`; the duplicate Cannabist Company AR
  statement merged into the already-filed `20-Cuzzies/` original per schema §7 and the Inbox
  copy deleted. `00-Inbox` is now empty.

## 2026-07-05 — Daily Brief routine (persona "Dawn") added
- **Second cloud routine**, separate from Samira: a once-a-day **1am ET** routine that gives
  Lemar the executive read Samira's hourly loop doesn't. Thin bootstrap
  `.claude/routines/DAILY-BRIEF-TRIGGER.md` → fat runbook `.claude/routines/daily-brief.md`,
  same thin-bootstrap/fat-runbook pattern as Samira.
- **Two new skills**: `morning-brief` — closes yesterday's open loops and sets today's top 5
  goals, synthesized from the Marspace activity cluster (#decisions + #atlas + #reports +
  #admin + email, weighted as ONE group) held SEPARATE from the project channels, plus
  Calendar and Gmail; and `meeting-prep` — one combined prep doc for today's calls, with Haven
  context (entity notes, prior meetings, prep scripts) pulled per meeting.
- **Living visual artifacts**: each skill renders a self-contained HTML page via the Artifact
  tool and re-deploys it to a stable URL every run (fulfils the 2026-07-03 "HTML/visual
  digests allowed; not yet designed" note). Fallback if headless artifacts prove unstable:
  a Slack canvas updated in place — a render-step swap only, everything else unchanged.
- **New channel** `#daily-brief` `C0BF73FF56H` — both brief links land here; Dawn posts here
  and only here (never #reports, Samira's feed).
- **Haven-first preserved, no collision with Samira**: briefs land as `type: brief` notes
  written directly into `_daily/` FIRST (the append-only zone vault-keeper never touches);
  Dawn is otherwise read-only on the vault and never runs vault-keeper or calendar-sync.
- **Pending on Lemar**: create the RemoteTrigger (daily 1am ET) pointing at the bootstrap and
  record its id/env in anchors; do one supervised manual run to confirm the artifact URL is
  viewable + re-deployable (else flip the render step to Slack canvas). The persona name
  "Dawn" is a placeholder — rename freely (two skills + one anchors row).

## 2026-07-04 — System hardening (this PR)
- **One anchors registry**: `.claude/anchors.md` replaces the four mirrored ANCHORS
  blocks (memory `shortlist_anchors.md`, atlas SKILL.md, atlas chat-project doc, the
  runbook). Gmail label IDs recorded for the first time.
- **Thin-bootstrap trigger**: the RemoteTrigger prompt becomes ~10 lines that pull the
  repo and execute the runbook. The runbook file in git is now the live source of truth
  for Samira's behavior; the 53KB design-doc/live-prompt split is gone.
- **Runbook slimmed** ~53KB → ~17KB: PARTS V/S/B/D/E/F now invoke their skills instead
  of restating them; safety stated once; history moved here.
- **`main` branch created** at the head of `claude/star-crash-thread-context-2npbr`.
  Lemar flips the GitHub default branch to `main` at trigger-swap time; stale branches
  (`claude/haven-knowledge-system-4tp4sa` + merged `claude/*`) deleted after one clean run.
- **Recordkeeping tightened**: done = a filed Haven note enforced in PARTS C/D/F via
  samira-report-result; run digest appended to `_daily/` (the vault's flight recorder);
  decision-typing rule; thread-update convention (append, don't fragment); `## Sources`
  provenance convention; entity stubs for recurring counterparties; investor index moved
  from the (empty) Google Sheet into `40-Projects/investor-pipeline/index.md`.
- **Monday gate set**: mirror runs through **2026-07-11**; gate = 7 clean days (every
  #reports line has a matching Haven note, zero discrepancies), then the mirror drops in
  one pass and the boards go read-only.
- **Obsidian re-point**: desktop Obsidian reads the git clone `C:\Users\lemar\Haven-repo\haven\vault`
  (pull-only via the Obsidian Git plugin); the git-less copy `C:\Users\lemar\Vaults\Haven` retired.

## 2026-07-03 — Haven rework (Tasks 1 & 2) + finalize
- Haven became the source of truth; capture-first law. Standing jobs PART V
  (haven-vault-keeper) and PART S (haven-calendar-sync) added ahead of all Slack work.
- Skills moved to repo `.claude/skills/` for cloud discovery (PR #25); Skill tool added
  to the trigger's allowed_tools; v4 trigger deployed.
- Schema edits landed: `legal` domain + `60-Legal/`; `10-Personal` split into
  Money/Health/Home/Family via optional `area`; `awaiting-decision` status.
- Live notes consolidated from the old feature branch onto the default branch.
- Plain-text-only output rule lifted (HTML/visual digests allowed; not yet designed).

## 2026-06-26 — Two-channel redesign
- #action-items renamed **#decisions** (same ID `C0BBXA96FFV`) — the ONE surface that
  pings Lemar; he decides by reacting (✅ 👀 ⛔ 🫡; Samira sets only headline emoji).
- #emails `C0BC1JSCHQW` and #to-do `C0BC30U222K` archived (kept as litigation/creditor/
  CRC paper trail). Open Items canvas `F0BDLSHD8JD` replaced #to-do. Email loop moved
  into #decisions with Gmail-label state.
- No bulk seed of old board items (Lemar's call): #decisions populates organically.
- Bespoke car cursors (💬/🗃️/📆) dropped; one reaction engine everywhere.

## 2026-06-21 — Shortlist → Monday
- Shortlist folded into Atlas as its Capture gear; storage moved from the Google Drive
  ledger to the personal Monday board `18418714876`. Drive ledger kept as read-only
  backup. (The one-time Drive→Monday data migration was never run and is now moot —
  Haven superseded Monday before it happened.)
