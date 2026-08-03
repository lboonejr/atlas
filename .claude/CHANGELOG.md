# CHANGELOG — system history (moved out of the runbook)

The runbook (`.claude/routines/samira-atlas-executor.md`) describes what runs NOW.
History and cutover narratives live here.

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
