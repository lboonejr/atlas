# Migration — three-conversation restructure (2026-09)

Self-retiring sub-runbook. PART 0 invokes this after PART 3 on every run while
`migration.decisions_migration_complete` is false in the state file. When step 4
reports zero remaining, set the flag true; this file then stops running (leave it in
place as history).

Context: #decisions (`C0BBXA96FFV`) is retiring; its open cards move to Convo 1
(`D0BHPKMDNEP`) in the doctrine card format. #stormy retires (the workflow moved to
Convo 2). The frozen `decisions_threads` map in the state file is the migration's
worklist — do not add to it, and stop reading it for anything else.

## Step 0 — one final legacy sweep (first migration run ONLY)
Run the retired PART C sweep once, exactly as the pre-restructure runbook defined it
(fenced `===ATLAS PROMPT START … run:admin-3x` prompts + named "Samira, …"
instructions, across the formerly swept channels, from their last stored watermarks):
- A staged-but-unrun prompt that is still due → run it now, outcome via
  samira-report-result, ✅ on the source.
- A prompt that can't run now → repost it as a Convo 1 card (Context links the
  original message) and react 🚗 on the original (retired-surface marker).
Record `migration.legacy_sweep_done: true` when finished; never repeat it.

## Step 1 — triage open #decisions cards (~15 per run, oldest first)
For each open thread in the frozen `decisions_threads` map (no 🫡, no "✅ CLOSED"
parent edit), read the full thread — reactions AND replies — then:
- **Still live** (an open question, undone work, a real pending decision) → post a
  doctrine-format card to Convo 1: fresh Headline; Context rundown written from the
  whole thread's state, with `Sources of truth:` linking the original #decisions
  permalink + the Haven note; carry the freshest decision round forward (don't make
  Lemar re-answer anything he already answered — a prior ✅/reply carries over as a
  recorded answer in Context). Reply "→ migrated to our DM: [permalink]" on the
  original. The Convo 1 card is now the ONLY worked copy.
- **Stale / superseded / duplicate** (overtaken by events, a duplicate batched card,
  answered-and-done) → close it out: record via samira-report-result (one Haven note
  can cover a batch of closures), edit the parent to `✅ CLOSED — migrated out
  ([reason])`.
- **The known backlog batches**: the ~34 past-due active notes and the 5 stuck Inbox
  notes from the 2026-09-05 repo audit become ONE batched Convo 1 triage card EACH
  (not 39 cards) — same batching rule as the vault-keeper's Inbox card.
Remove each handled thread from `decisions_threads` and update
`migration.cards_remaining`.

## Step 2 — announcements (first migration run ONLY, after step 1's first batch)
- Post the system-change announcement as the FIRST doctrine-format card in Convo 1
  (Headline: "New system — three conversations"; Context: what changed and why;
  Decisions: one round asking Lemar to ✅ that the new format reads well on his phone —
  this doubles as his live test of the engine on the new surface).
- Seed each timeline channel with one 🌐 entry: "This channel is now an append-only
  timeline — I post what moved here; talk to me in our DM (work) or drop thoughts in
  your self-DM (intake)."
- One #reports line: "🌐 Restructure live — three conversations active, #decisions
  migration underway — Samira".
Record `migration.announcements_done: true`.

## Step 3 — #fixes readiness check (every migration run until it passes)
Verify your bot can read + post in #fixes. If not (Lemar hasn't run `/invite @Samira`
yet), nudge ONCE per day at most via a reply on the setup card in Convo 1. Until the
bot is in, #fixes-bound items (STUCK escalations, scanner findings) go to Convo 1
cards tagged 🔧 as the interim home; move nothing retroactively once #fixes opens —
just start using it.

## Step 4 — completion
When `decisions_threads` is empty AND announcements are done AND the legacy sweep is
done:
1. Set `migration.decisions_migration_complete: true`; delete the `decisions_threads`
   key and the watermark entries for every retired swept channel (keep #reports).
2. Post a final Convo 1 card: "Ready to archive — #decisions and #stormy" — Decisions
   round asks Lemar to archive both channels himself in Slack (you cannot archive; his
   ✅/🫡 closes the card once done). Archiving is deliberately his hand, deliberately
   last.
3. Log the migration outcome via samira-report-result (Haven note under
   `70-Automation/samira/`), one #reports line, and note it in the digest.
