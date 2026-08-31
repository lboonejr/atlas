# Productivity Loop System — design package

Three files that turn Lemar's 2026-08-27 brainstorm (the three-party consulting/licensing
productivity loop: Lemar the visionary, Arianna the admin, Samira the organizer) into a
prompt that can actually be run, plus everything needed to dial it in.

| File | What it is |
|---|---|
| `prompt-v2.md` | The improved prompt, ready to paste into a Claude project (or run through Stormy). Rewritten to name the real system it lands on, carry its constraints, and demand a build plan expressed as diffs to what already runs. |
| `question-bank.md` | The dial-in questions — every open decision the brainstorm leaves unanswered, grouped by theme, each with why it matters. This is the "ask as many questions as possible" half of the request, pre-asked so a design session starts at round two instead of round zero. |
| `org-infrastructure-merge.md` | The merge with Lemar's parent-company / rooms model (2026-08-27): layer ownership, ten flaws with fixes, the room template, cost comparison, and the resulting edits queued for `teams-tag-architecture.md`. |
| `org-infrastructure-map.html` | The visual companion to the merge — the building cross-section, the seat-per-business collision, and the routing law. |
| This README | The integration map: what the brainstorm asks for that already exists, what is genuinely new, and where it directly conflicts with current doctrine. |

## Why the original prompt needed the rewrite

The brainstorm describes a system to be designed from scratch. But most of it already
exists and is live: Samira runs 11 scheduled scans a day against a written runbook
(`.claude/routines/samira-atlas-executor.md`), Haven (`haven/vault/`) is the source of
truth with "done = a filed Haven note" as law, #decisions is the one reaction-driven
decision surface, the samira-loop PT cards already do the pressure-testing the brainstorm
describes, and the first client is already onboarded as the Camden Dispensary Launch
engagement with its own overlay, Drive tree, private channel, and fee schedule.

A design session run on the original prompt would re-invent all of that and produce a
plan that collides with it. The v2 prompt instead frames the job as an **integration**:
one genuinely new element (Arianna as a second human), one new business wrapper (the
licensing consultancy as a legitimate, repeatable, client-facing company), and a set of
deliberate doctrine changes that each need a yes from Lemar.

## Integration map

### Already exists — map, don't build

| Brainstorm ask | What already covers it |
|---|---|
| "Samira knows every project, keeps the timeline, pressure-tests my vision" | The runbook + the samira-loop skill (PART R): eight-lens pressure test, one round per scan, PT cards in #decisions |
| "Spread multi-step prompts over remaining daily runs" | PART R cadence already reads the scan index and sizes batches by scans left in the day |
| "To-do list for me lives in #decisions" | Live today: #decisions is the only channel that pings Lemar; reactions are the engine |
| "Suggested project titles / instructions / files for each Claude project" | The samira-loop naming rule (8.0 in the Camden overlay) + `.claude/projects/` thin-pointer rulebooks are the existing pattern to extend |
| "Every session relays back to Samira at the end" | The samira-work-summary skill is exactly this handoff, from any live thread |
| "Consistent file structure, clean docs, always referenceable" | Haven schema + vault-keeper (PART V) for notes; the Camden Drive tree (00/01/02, phase folders, naming + supersede convention) is the client-file template to generalize |
| "Daily health scan of the whole thing" | Partially: run digests + `_daily` journal, Pulse's routine-health section, the reports-contradiction-scanner (PART T). A true reviewer-of-the-whole-loop is new (below) |
| "Licensing our first client, the Camden Group" | The Camden Dispensary Launch engagement: overlay, six gates, Working Log, milestone billing — already live |
| "Concise messages, context in replies, links to docs, call scripts on calendar events" | Mostly current doctrine (parent + threaded options, source links required). Call-script-attached calendar events are a small new rule, not a new system |

### Genuinely new — design work

1. **Arianna as a second human in the loop.** The entire current system is single-owner:
   the reaction engine reads only Lemar's signals, the capture DM is his, the browser
   lane assumes *he* is the human present. Adding an admin touches the runbook, anchors,
   the reaction engine, and the safety floor. This is the core of the design job.
2. **The consultancy as a company.** EIN, entity, name, domain, website, socials, ads,
   vendor-partnership economics. None of this exists; some of it (public posting, paying
   for ads) is currently on Samira's MUST-NOT list, so it lands on humans or a new lane.
3. **The reviewer routine.** A meta-monitor over Samira/Dawn/Basil + both humans'
   follow-through, with a governance question attached (can it self-modify the runbook,
   or does every change still go through a #decisions card?).
4. **Templating the client playbook.** Turning the Camden engagement into the repeatable
   product: template docs, phase checklists, a "new client" spin-up procedure, and
   eventually the Virginia variant.

### Direct conflicts — each needs an explicit call, not a quiet override

| Brainstorm | Current doctrine | The call to make |
|---|---|---|
| Samira "checks to make sure things are done and follows up" with both humans | "Never re-post or nudge" (#decisions law); items age out via the canvas, not via pings | Define a bounded accountability ping (e.g. one confirmation ask per open commitment per day, in the right surface) or keep no-nudge and accept slippage |
| Admin sends emails, makes calls, runs Facebook ads; system is client-facing | Safety floor: never send email, never pay, never post publicly, never send outreach | Keep the floor for Samira and route all outward actions through a human send-gate (Arianna clicks after Lemar's ✅) — the floor becomes "AI never sends; humans send what the loop staged" |
| 3-way DM as a shared status surface | Routing law: every output goes to exactly ONE place; summaries live in project channels / #reports | Either the 3-way DM replaces per-project summary drops (and gets an anchors row + sweep rules), or it's dropped in favor of the existing surfaces |
| Admin's Claude "cleans up all the files," dedupes, organizes | Connected Drive tools have no move/delete/trash (documented in the Basil runbook); vault-keeper never deletes | File cleanup is a *local* job on Arianna's machine (Claude Code with filesystem access), not a cloud routine — design it as such |
| Health scan "throws changes into Samira so she can make the changes herself" | Routine changes are Lemar-gated (#decisions), and editing the runbook on `main` changes live behavior immediately | Recommended: reviewer proposes diffs as #decisions cards; Lemar's ✅ merges them. Self-modifying autonomy is a real safety decision, not a default |
| "Getting people licensed" + ops services as one pipeline | Camden overlay hard-stops at inspection clearance; ops work is a separate, unpriced "opening services" engagement | The business vision is fine, but the engagement template needs the same two-engagement split so scope creep stays impossible |

## Constraints any design must carry (from the live system)

- Haven is the source of truth; capture-first; done = a filed Haven note.
- All platform IDs live in `.claude/anchors.md` and nowhere else.
- Samira's cadence is 11 scans/day (8a–6p ET); every design that says "Samira will…"
  spends scan budget.
- One bot DM slot per user: Arianna gets her *own* DM with the Samira bot (fine), but
  nothing else can share Lemar's capture DM.
- The git-write policy: durable vault/routine writes go straight to `main` (this docs/
  package rides a review branch precisely because it is a draft, not live state).
- lemar@cuzziesnj.com winds down mid-2026 — nothing new gets built on it; the new
  business needs its own domain and mail from day one.
