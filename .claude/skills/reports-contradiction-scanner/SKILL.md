---
name: reports-contradiction-scanner
description: >
  Scans #reports for internal contradictions — the same fact reported two different
  ways across entries, an unresolved self-correction, or a claim that's gone stale
  against the vault — checks the cited Haven note as ground truth for each one, then
  posts EVERY finding (proposed fixes AND open questions alike) as a #fixes card
  (doctrine format, worked by PART 5's standard card engine, same as any other card).
  Use it whenever Lemar asks to "scan #reports for contradictions", "check the reports
  log for conflicting numbers", "did we say two different things about X", "audit the
  reports channel", or on the skill's own scheduled run (PART 6c). It never rewrites or
  deletes a prior #reports message (append-only, per doctrine) and it never executes a
  fix on its own — a confirmed fix is staged as a normal card option and only runs once
  Lemar ✅s it on the #fixes card, same as every other Samira task.
---

# Reports Contradiction Scanner (Haven-first, hands off through #fixes)

#reports is a one-way log — nothing there is ever corrected in place, so contradictions
between entries (a figure restated differently, a self-correction that never says what
happened to the original claim, a status that's quietly gone stale) can sit unnoticed
indefinitely. This skill's only job is to catch those and surface them; it never edits
history and never executes a fix itself. The Haven note behind each entry is the ground
truth this skill checks against — #reports is a rendering of what happened, not the
record of it.

This was originally proposed by Samira as a skill candidate
(`haven/vault/40-Projects/samira-skills/2026-08-14-reports-contradiction-scanner-skill-request.md`)
and routed to #skills-lab per the hard floor that Samira/Atlas never build skills
mid-run. Lemar picked it up from there and had it built.

## ANCHORS
Read `.claude/anchors.md` first for the live IDs. This skill touches:
- **#reports** (`C0BBZJL85RT`) — read-only source; NEVER post a correction by editing an
  old message, only by adding a new one.
- **#fixes** (`C0BV5BRNH5Z`, Convo 3) — where EVERY finding goes as a card
  (`.claude/doctrine/card-format.md`; findings are defects in Samira's own reporting —
  that is Convo 3's subject). Standard card engine: 🔴/🟡 headline; ✅ on an option =
  Lemar's pick, and a plain reply is an equal signal (on conflict the reply wins).
  PART 5 of the runbook already executes whatever a picked option says, so this skill
  does not need its own execution logic — it only has to word the option so it's
  directly actionable.
- Vault writes go through **haven-capture** (never hand-written); do not write the
  retired local reader copy.
(Until 2026-09-06 the routing was a summary DM'd to the Samira capture DM plus
#decisions cards for open questions; both surfaces retired for this — the #fixes card
IS the notification now.)

## What counts as a contradiction
Only flag things that are genuinely inconsistent, not just incomplete:
- **Conflicting figures/status for the same fact** — two #reports entries state a
  different number, date, or outcome for what is clearly the same task or matter.
- **Unresolved self-correction** — a later entry says "actually / correction / meant to
  say X" but no entry (or the linked Haven note) ever confirms the original claim was
  fixed.
- **Stale claim** — a #reports entry states something as current that the Haven note it
  links to (or the matter's active note, if findable) shows has since changed.
Two entries that simply cover different time periods, or a figure that legitimately
changed over time with no unresolved gap, are not contradictions — skip them.

## R1 — scan
Read #reports since the last scan. Bookmark progress in this skill's own running log
note (see R4) so re-runs don't re-flag the same pair twice: on a first-ever run, or if
no bookmark is found, default to the last 7 days. Group entries by the matter/task they
describe (the Haven note path or task name each line already carries is the grouping
key) so you're comparing like against like, not scanning line-by-line.

## R2 — detect
Within each group, compare the stated figures/status across entries and check for the
three shapes above. Quote the exact conflicting lines (with dates) for anything you flag
— a finding without the source text is not verifiable later.

## R3 — check ground truth
For each candidate, open the Haven note(s) the entries cite. If a fact and its vault
note agree, and the "old" #reports line is simply outdated, that's a stale claim with an
obvious fix (its card proposes the fix directly — see R6). If the vault itself is silent
or the entries disagree with each other and the vault doesn't resolve it, that's a
genuinely open question. Either way the finding becomes a #fixes card.

## R4 — land the running log note (Haven-first)
Before posting anything, call **haven-capture** to append an `## Update` to this skill's
log note (create it on the first run: `type: log`, `domain: project`,
`tags: [samira, reports-contradiction-scanner]`, `status: active` if anything is open,
`done` if the scan was clean). Body: the range scanned, every contradiction found (quoted
lines + Haven ground truth), and which ones are open questions vs. obvious fixes. This is
the durable record — the #fixes cards are notifications about it, same as every other
Samira skill.

## R5 — post the findings as #fixes cards
Every finding gets ONE #fixes card (doctrine format: Headline ~5 words · Context with
the quoted conflicting lines, the Haven ground truth, and the log note path in Sources
of truth · Decisions per R6). Batch only if there are many from the same scan, same
pattern as the batched Haven Inbox card. A clean scan posts nothing — no card, no
notification (same non-spam rule pulse-dashboard follows on a quiet render); the
2026-09-06 restructure retired the separate capture-DM summary, so the card is the
whole notification.

## R6 — obvious fixes vs. open questions (both are #fixes cards)
- **Obvious fix** (vault ground truth is clear) → the card's decision round proposes the
  correction directly — there's only one sensible option, so word it as a single-action
  parent or a one-option round. The correction itself is still staged as an un-reacted
  append: a one-line #reports entry (new message, never an edit) restating the correct
  fact and pointing back at the two conflicting lines, plus an `## Update` on the
  relevant Haven note if it needs a current-state correction. It EXECUTES from Lemar's
  ✅ on the #fixes card — the PART C sweep that used to pick up un-reacted staged
  corrections ended 2026-09-06 — never inline as part of this scan.
- **Open question** (vault silent or entries disagree and there's no tiebreaker) → the
  card's decision round offers directly executable options — e.g. "Option 1 — Treat
  [figure A] as correct" / "Option 2 — Treat [figure B] as correct" / "Option 3 —
  Neither, here's what actually happened: ___", one reply per option. Link the quoted
  lines and the Haven note path. Once Lemar reacts ✅ (or replies — an equal signal;
  on conflict the reply wins), PART 5 already executes it (posts the #reports
  correction line, updates the Haven note) and records the outcome via
  samira-report-result — this skill does not need a separate handoff mechanism.

## Inputs this skill expects
A time range or "since last run" (default). Nothing else — it reads #reports and the
vault directly.

## What to return
`scanned: [range]` · `found: N` · `open: O` (posted to #decisions) · `fixed-noted: F`
(obvious fixes staged for a later PART C pass) · the log note path. Zero found →
`clean scan`, no DM, one line in the run digest.

## Note on scheduling
This skill is also invokable on demand ("scan #reports for contradictions") outside its
scheduled run. It runs unattended as **PART T** of the hourly loop
(`.claude/routines/samira-atlas-executor.md`), after PART M (money) and before the
canvas refresh — Lemar's call, made explicitly, the same way Stormy was folded in as
PART Q. (Originally slotted as PART R; relettered to PART T when an unrelated,
concurrently-merged change claimed PART R for the separate samira-loop build/
pressure-test feature.)
