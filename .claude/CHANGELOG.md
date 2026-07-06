# CHANGELOG — system history (moved out of the runbook)

The runbook (`.claude/routines/samira-atlas-executor.md`) describes what runs NOW.
History and cutover narratives live here.

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
- **Pending on Lemar**: merge this PR; create the RemoteTrigger (daily 1am ET) pointing at the
  bootstrap and record its id/env in anchors; do one supervised manual run to confirm the
  artifact URL is viewable + re-deployable (else flip the render step to Slack canvas). The
  persona name "Dawn" is a placeholder — rename freely (two skills + one anchors row).

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
