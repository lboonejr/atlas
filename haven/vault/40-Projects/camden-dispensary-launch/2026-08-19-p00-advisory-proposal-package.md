---
created: 2026-08-19T12:14-04:00
updated: 2026-08-19T13:05-04:00
domain: project
type: brief
status: awaiting-decision
tags: [samira-loop, camden-launch, phase-00, pressure-test, proposal]
source: claude
---

# P00 Advisory proposal package

## What this is

The advisory proposal for the Camden engagement, taken from "built but unsent with six
placeholders" to a send ready package in one thread. Three things happened, in order:

1. The proposal was surfaced for final review and the blockers were enumerated.
2. The planning board approval was moved from SECURED to TO CONFIRM, then swept a second
   time when the first pass left the assumption sitting in six other places.
3. The placeholders were filled, the milestone labels were corrected, and the PDF and web
   versions were built.

The engagement is still pre-engagement. Nothing signed, no money moved.

## State

Built and waiting on Lemar to send. Three surfaces now exist and agree:

- Editable Doc: "Camden Dispensary Launch — Advisory Proposal (editable) 20260819v3 FILLED",
  Drive `1PJ4Ix_dizeptAKHBq__G5prlUooQ2A2BVtDFsZbfCms`, in 01 Client-Facing.
- PDF: `Camden_Advisory_Proposal_20260819.pdf`, nine pages, delivered to Lemar in the thread.
  NOT yet in 00 Command Center (see Handoff). Superseded by the designed version, see Update.
- Web: rebuilt from the same HTML source as the PDF, delivered to Lemar for review. The old
  claude.ai artifact still carries the 2026-08-18 text and must not be shared.

Superseded and renamed in 01 Client-Facing, so nobody works from them:
- Superseded 2026-08-19 — Advisory Proposal (planning board stated as secured)
- Superseded 2026-08-19 — Advisory Proposal (v1, residual approval language)
- Superseded 2026-08-19 — Advisory Proposal (v2, unfilled placeholders)

## Phase

Pre-engagement, feeding Phase 00. Tagged phase-00 because the proposal's first ask (the
planning board resolution and whatever site control exists) is the Position Report's first
two inputs.

## Build lane

CLOUD for everything that landed: the Drive docs, this note, the PDF and HTML build, the
Slack card. Three slices are LOCAL and are named as such rather than left to stall:

- Dropping the PDF binary into 00 Command Center. The Drive connector takes inline content
  only, and a 155KB base64 payload is not safely reproducible in a message. Lemar drags it
  in, or connects a folder and it goes over the device bridge.
- Retiring or rebuilding the old claude.ai web artifact. Not reachable from a cloud session.
- Appending the decision record to the Working Log.

## Pressure test

Round 1 ran live in the thread rather than as a posted card, because the item was already
being shipped. `PT deferred — shipped first` per samira-loop section 4.1. Coverage against
the eight lenses plus the engagement's six gates:

- Lens 3 accuracy ✓ · gate 4 fact ✓ · gate 5 approvals ✓ — the whole planning board sweep.
  Ten spots changed. The document now claims only that the group has been in front of the
  board, which is what we actually know.
- Lens 4 gaps ✓ — found the PDF that the handoff said was in 00 Command Center and never
  was, and found the web version still carrying the old scope.
- Lens 2 reader ✓ — the milestone labels named phases that did not match their triggers
  (milestone 2 labeled Phase 01 while the Position Report is Phase 00; milestone 3 labeled
  Phase 02 while submission happens in Phase 03). Relabeled by trigger, numbered 1 to 5,
  with one sentence explaining why milestones and phases are not the same count. No amount
  and no trigger changed.
- Lens 8 fit ✓ — gate 6 placement: new versions created, prior ones prefixed Superseded.
- Gate 1 scope ✓ — nothing in the document crossed into opening services.
- Gate 2 authority ✓ — the not legal, tax, or accounting advice clause stands.
- Gate 3 outcome ✓ — no sentence promises or implies a license or an inspection result.
- Lens 1 premise, lens 5 failure modes, lens 6 edge, lens 7 execution — OPEN. These run
  against what actually goes out, once it goes out.

Lenses 4/8 covered. Gates 6/6 covered.

## Open questions

1. The proposal is addressed to Jamil Tyson personally because no entity was named. Forming
   the entity is already a Phase 00 item. Does he countersign as an individual, or do we
   wait for the entity before anyone signs anything?
2. The PDF is not in 00 Command Center. Drag it in, or connect a folder so it can be written
   over the device bridge?
3. The Project Instructions (section 4) still say the group holds the planning board
   approval. That is the governing rule set and it now contradicts today's decision. It
   needs correcting in the Drive doc and in the claude.ai project custom instructions.
4. The old claude.ai web artifact still carries the 2026-08-18 through-opening-era text.
   Retire it, or rebuild it from the new HTML?
5. Opening services still has no scope and no price. Not blocking the send, but better built
   well before inspection than under pressure.

## Locked

Not locked. Waiting on the send and on the five questions above.

## Handoff

Three LOCAL slices, listed under Build lane.

Transport note, worth keeping because it cost an hour. This note was refused twice from a
Cowork session with 403 `Resource not accessible by integration`. Cause: there are two
Anthropic GitHub apps, and only one was installed. "Claude" (the Claude Code app) was
installed with write on code, which is why Samira's cloud runs commit to `main` all day.
"Claude Github MCP Connector" — the app every Cowork and claude.ai surface actually uses —
was authorized but never installed, so it could read this public repo and write nothing.
Installing it on `lboonejr/atlas` (installation `154975254`, read and write on code) fixed
it. The claude.ai callback threw `state: Field required` on the way back because the install
was started from GitHub's app page rather than from Claude's connect flow; that error is
cosmetic and the installation completed.

## Working Log entry

The decision record text was delivered to Lemar in thread
(`approval_language_sweep_20260819.md`). It has not been appended to the Working Log yet,
and it needs one addition covering the filled placeholders, the milestone relabel, and the
PDF build.

## Update 2026-08-19

Two things closed after the note first landed.

**Superseded copies trashed.** Lemar's call, and he did it himself rather than having it
done for him. Moved to Drive trash (recoverable for thirty days, permanently deleted after):

- 00 Command Center — Superseded 2026-08-18 — Project Instructions (old through-opening scope)
- 01 Client-Facing — Superseded 2026-08-18 — Advisory Proposal (old through-opening scope)
- 01 Client-Facing — Superseded 2026-08-19 — Advisory Proposal (planning board stated as secured)
- 01 Client-Facing — Superseded 2026-08-19 — Advisory Proposal (v1, residual approval language)
- 01 Client-Facing — Superseded 2026-08-19 — Advisory Proposal (v2, unfilled placeholders)

So the three titles listed under State no longer resolve, and neither does the pre-scope-cut
proposal. The reasoning survives here and in the Working Log decision record; the documents
themselves do not. Worth being deliberate about that: the 2026-08-18 through-opening version
was the only artifact showing what the engagement looked like before the scope was cut to
inspection, and it is now recoverable only until roughly 2026-09-18.

Still in place, not trashed: "Superseded 2026-08-18b — Project Instructions (before working
log)" and `handoff_camden-dispensary-launch_20260818-2205`.

**A designed proposal exists.** The nine page PDF was a typographic pass on flowing HTML.
Lemar asked for a real design pass, unbranded and signed in his own name rather than
Cuzzie's, on the reasoning that Cuzzie's winds down mid-2026 and this engagement runs ten
months. Built as an eleven page fixed canvas document (US Letter), authored through the
Adobe visual design skill: Source Serif 4 for reading, Acumin Pro for structure and figures,
a deep green accent used only on the cover band, section rules, status chips, and the
milestone numerals. Cover page, status chips on the Where You Stand board, a set milestone
table, and a proper signature block. Content is identical to the v3 filled Doc, word for
word. Source HTML and the PDF both live in the session, delivered to Lemar; neither is in
Drive yet, which folds into open question 2.

## Sources

- drive: https://docs.google.com/document/d/1PJ4Ix_dizeptAKHBq__G5prlUooQ2A2BVtDFsZbfCms/edit (proposal, v3 filled)
- drive: https://docs.google.com/document/d/12JG69I2RWZ9l3rR7AdFZXhyiuM52FEhmqi-52S3OC9Q/edit (Working Log)
- drive: folder 1SE4aln7I35W0M_NSFA0Mo3sYuEkYRWAv (01 Client-Facing)
- drive: folder 1waKvkdsc9yr2ZAu_BhY8EneONKvtDhcM (00 Command Center, where the PDF belongs)
- slack: https://app.slack.com/archives/C0BRZT2V89W/p1787156572068829 (staged prompt, superseded by this note)
- slack: https://app.slack.com/archives/C0BBXA96FFV/p1787157130471099 (PT card)
