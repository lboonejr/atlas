# The rework — Teams seats for individual work, Tag for collaboration, Haven as truth

Lemar's calls, 2026-08-27, in order: rework the infrastructure through a Claude Teams
plan and Tag → simplify further (retire Samira's machinery, keep the Haven vault
current) → structure it for cost: **Tag for collaborative work, the Team workspace
(seats) for individual work.** This file is the resulting target architecture and
migration plan. It amends `decisions.md` (see its Amendment section) and, once merged,
drives the build.

The governing idea, refined for cost: **seats are flat-rate, Tag channel work is
metered.** So the seats are the workhorse and Tag is the coordination layer, used
where shared context in the channel is the point. Haven stays the source of truth;
the laws (capture-first, done = a filed Haven note, the send-gate, no invented facts)
survive — the machinery goes.

## 1. The one-line law

**Build in your seat, coordinate in the channel.**

- The output is a THING (a document, draft, research, call script, spreadsheet,
  page) → made in a **seat**, inside a shared org Project so both humans can see it.
  Flat-rate, no marginal cost.
- The output is SHARED AWARENESS (a status answer, a handoff, an approval, a
  follow-up nudge, lead triage, a daily to-do post) → **Tag, in the channel.**
  Metered org spend, kept small on purpose.
- A private quick question to Tag goes in a **DM with Tag** — it bills the
  individual's seat, not the org, so it rides the flat rate too.

## 2. Target architecture (three pieces + one job)

| Piece | Role | Cost profile |
|---|---|---|
| **Haven** (`haven/vault/`) | Source of truth, unchanged: capture-first, done = a filed Haven note, Slack/Drive/Calendar are renderings | Free |
| **Teams seats** (Lemar Premium, Arianna Standard) | The individual work engine: shared org Projects per major task, Claude Code, Claude-in-Chrome tasks, all drafting and building | Flat ~$120–150/mo |
| **Tag in Marspace** | The collaboration layer only: live status answers in project channels, handoffs between Lemar and Arianna, approvals in-thread, accountability follow-ups (ambient mode, tightly scoped), lead triage in the 3-way DM, a small set of scheduled posts | Metered; capped (section 4) |
| **One daily housekeeping job** | The only scheduled backbone left: file the vault Inbox (vault-keeper), sync `due` notes to the calendar, drop a short daily digest | One run/day |

**Samira's machinery retires at end state** — the hourly 15-part runbook, the custom
Vercel bot apps, the reaction-emoji engine, watermarks/locks/state file, staged fenced
prompts. Samira's *job* is absorbed: the live half by Tag, the build half by the
seats, the vault half by the housekeeping job. Approvals become conversation ("yes,
send it" in the thread) with the Haven note as the record. Dawn/Basil/Stormy collapse
the same way: a scheduled post, an on-demand ask, or retirement — each closed out
individually during migration.

## 3. Standing rules

1. **Access bundle = the safety floor, enforced.** Tag's org credential bundle
   (claude.ai/admin-settings/claude-tag): read + draft scopes only — Gmail drafts yes
   / send no; Drive read-write inside project folders; Calendar without external
   invitees; **GitHub connector included** so Tag files Haven notes. No payment or
   social credentials, ever — those stay human.
2. **Haven writes are still the finish line.** Seat work and Tag work alike: anything
   durable lands a Haven note (the seat sessions via the existing capture flow, Tag
   via the GitHub connector) or it is not done.
3. **Ambient mode is scoped, not global.** Follow-ups on in a small set of channels
   (start: #camden-launch and the 3-way DM). Every channel added is a deliberate call,
   because ambient attention is metered attention.
4. **Scheduled Tag jobs stay few and small.** Posts and nudges, yes; heavy renders and
   long documents, no — those are seat work.
5. **Persona continuity is optional now.** Tag posts as "Claude"; keep a "— Samira"
   sign-off only if the continuity feels worth it. The personas were plumbing-era
   artifacts; the simplified system does not need them.
6. **Lemar's existing personal claude.ai account is not merged, moved, or closed**
   until the last routine on it has a proven replacement. Accounts cannot merge into
   a Teams org; triggers and connector auths do not migrate — every move is a rebuild,
   so the old system keeps running until its replacement is verified.

## 4. Cost controls

- **Org spend cap** set from day one, sized to a starting monthly budget; per-channel
  caps on the ambient channels. Caps hard-decline work when hit — review the cap
  monthly against actual usage rather than guessing high.
- **Seat mix** reviewed after one month of real usage: Lemar Premium + Arianna
  Standard to start; drop or raise tiers based on who actually hits limits.
- **The routing law is the main cost control.** Every task pushed to a seat instead of
  a channel is marginal-cost-free. When in doubt, seat.
- Watch item: the Vercel free-plan deploy quota is currently burned by Samira's hourly
  commits (three connected projects deploy on every `main` push). Retiring the hourly
  loop fixes this as a side effect; until then it is a known noise source on CI.

## 5. Migration phases

**Phase 0 — Stand up (nothing live changes).**
Create the Teams org (Lemar Premium, Arianna Standard) · verify Tag's seat minimum on
a 2-seat org BEFORE paying (gate V1) · install Tag (Slack owner account) · configure
the access bundle per rule 1 · set spend caps · invite Tag to the pilot channels only
(#camden-launch, the 3-way DM). Exit: Tag answers a status question correctly and
files a test Haven note through the GitHub connector.

**Phase 1 — Two-week pilot of the split.**
Arianna onboards; her individual work runs in her seat inside shared org Projects; the
collaborative layer (handoffs, approvals, follow-ups, lead triage) runs through Tag in
the pilot channels; ambient mode on there only. Samira's hourly loop keeps running
everything else — one lane rule keeps them apart: Tag does not act on #decisions
cards. Exit: two weeks of the routing law holding, no missed Haven filings, spend
inside the cap.

**Phase 2 — Absorb and retire, one piece at a time.**
Each Samira PART either moves (to a seat habit, a Tag behavior, or the housekeeping
job) or retires, one #decisions card per change: capture DM → captures happen in seat
projects or via Tag anywhere; email/investor loops → seat work on demand; PT cards →
in-project pressure-testing; money hub → a seat interaction (its ledger stays in
Haven); Pulse/digest → the housekeeping digest + asking Tag "where are we". The
housekeeping job (vault-keeper + calendar-sync + digest) is built and verified FIRST —
as a Tag scheduled task if gates V2/V4 prove out, else as the one surviving slim
RemoteTrigger routine (an acceptable permanent home).

**Phase 3 — Decommission.**
The hourly Samira trigger disabled; Dawn/Basil triggers closed out or folded into the
housekeeping job; the Vercel bot apps retired; anchors updated with tombstones (the
PART F pattern); CHANGELOG entry. Only then is Lemar's personal account consolidated
or kept as personal-only.

## 6. Verification gates (tests, not assumptions)

- **V1 — Tag seat minimum** on a 2-seat Team org (sources conflict: 2 vs 5 seats;
  ~$120–150/mo vs ~$300+/mo). Confirm before paying.
- **V2 — GitHub connector in the Tag bundle** writes to `lboonejr/atlas` reliably.
  This is the keystone: the simplified system's one hard requirement is that the
  vault stays current, and that depends on this gate. If it fails, all Tag output
  routes through the housekeeping job instead.
- **V3 — Housekeeping fidelity.** A scheduled job (Tag or slim trigger) runs
  vault-keeper + calendar-sync correctly for a week straight.
- **V4 — Ambient behavior and spend.** Follow-ups fire usefully in the pilot channels
  and the metered spend for a normal week is acceptable.
- **V5 — Private-channel boundary** verified in #camden-launch (client-confidential)
  before ambient mode is enabled there.

## 6a. Pending amendment — the parent-company / rooms merge

Lemar's organizational-infrastructure idea (a parent company as a building, each business a
room) was reconciled against this architecture on 2026-08-27. The finding: the two designs
answer different questions and do not conflict — seats scale with **humans**, rooms scale with
**businesses**, and Haven stays under both. The merge record, its ten flaws-and-fixes, the room
template, and the six calls it needs from Lemar live in **`org-infrastructure-merge.md`**
(visual: `org-infrastructure-map.html`). Its closing section lists the specific edits queued for
this file — including the landlord / superintendent split that resolves rule 5, two new standing
rules (scheduled jobs at the parent layer only; Slack for humans, git for machines), and a sixth
gate **V6 (restore drill)**. Those edits are held until Lemar makes the calls, so this file stays
the record of what is decided rather than what is proposed.

## 7. What this changes in the design package

- `prompt-v2.md` section 4: the target infrastructure is now this file's three
  pieces + one job; design output should be the Phase 2 absorb-or-retire map, not
  runbook diffs to a system being kept.
- The question bank's answers stand; the mechanisms shift: accountability = Tag
  ambient; Arianna's to-dos = Tag daily post + her seat; #decisions-style approvals =
  in-thread conversation with the Haven note as the record.
- The reviewer routine (F37–F40) shrinks to match the smaller system: housekeeping-job
  health, Tag ambient health, spend vs. cap, vault Inbox not accumulating — and lives
  in the housekeeping job itself rather than a separate Dawn PART.
