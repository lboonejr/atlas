---
domain: project
type: decision
status: active
source: claude
tags: [samira-loop, camden-launch, phase-00]
---

# Ops ADMIN lane and Ariana

## What this is

A fourth lane in the loop (ADMIN) and the person who runs it. Ariana joins the engagement
as the human who does everything that needs a human and does not need Lemar's authority:
calls, chasing, scheduling, filing, records, and status. Two artifacts built, both in
02 Internal.

The goal behind it is that Lemar issues instructions to two places only (Samira for
anything a machine builds, Ariana for anything a human does) and touches nothing else.
The design target as written is not zero touches, because signing, submitting, paying,
advising, and any logged-in portal session are irreducibly his. The target is that every
touch of his arrives pre-staged to one sentence or one click.

## State

Built, not locked. Landed in Drive 02 Internal, both files verified by read-back.

- Ops_ADMIN lane operating model_20260819
  https://docs.google.com/document/d/12PqKbqWjH2Tn5xX_4GHzEzFlgINaTWkYIsvYI9y4QBw
  Verified at 9,085 bytes.
- Ops_Ariana onboarding packet_20260819
  https://docs.google.com/document/d/1-qPiZncn0SAFCdJ-jUa68RzwdL2rxjeLpsOJpTLYMKU
  Verified at 8,204 bytes.

## Phase

Not phase-bound. Filed against Phase 00 because that is where the engagement sits.
The engagement reads pre-engagement as of the Working Log's 2026-08-18 23:00 ET stamp:
nothing signed, no money moved, proposal built and not sent.

## Build lane

Mixed.

CLOUD, done. Both documents drafted and landed in Drive 02 Internal.
BROWSER, outstanding. This Haven note has to be uploaded to the vault through GitHub's web
upload, because the GitHub connector returned 403 on writes in a Cowork session on
2026-08-19 while reads worked. Upload the file, do not paste it. A paste taken from a
rendered preview strips the frontmatter and the headings and the vault reads the result as
a broken container.
LOCAL, outstanding. Ariana's account creation, the 02 Internal carve-out, and the folder
and channel permissions are Lemar's to do in the admin consoles.
ADMIN, not yet live. It switches on when the access checklist clears.

The seam: nothing posts to Slack until this note lands in the vault. Per section 8.3 the
capture comes first, so no card was posted on 2026-08-19 and none should be claimed.

## Pressure test

Round 1 run 2026-08-19. Six gates plus the eight lenses.

Scope gate. Held, with one correction made during the build. "Everything related to the
project" would have swept in vendor management, hiring, floor training, and the client's
own business admin. Section 4 of the operating model names each of those as out, and the
client's own entity filings and bookkeeping as not ours at all.

Authority gate. Held. Ariana's never-list covers legal, tax, and accounting, including
paraphrasing counsel. Her own engagement terms, pay, and worker classification are named
as Lemar's questions for his counsel and accountant, and are not answered anywhere in
either document.

Outcome gate. Held. Her call script uses "working toward" and the phrase "applying for" is
deliberately excluded. Rule 3 and escalation trigger 2 both cover outcome questions.

Fact gate. This is where the real risk of the lane sits and it is addressed twice. A human
on a phone creates facts that never touch a document. The rule written into both files:
what somebody says on a call is a lead, not a fact of record, until we hold the document,
resolution, or rendered page that says the same thing. Call records file as call records
and never source a client-facing artifact. The script carries one required question, "is
that on a document I can pull," which is what converts a lead.

Approvals gate. Held, and hardened. The planning board site plan approval and the City
resolution of local support are separately named in both documents, with an explicit
instruction to ask about them by full name separately on any City call, because phone
conversations blur them in both directions.

Placement gate. Both files in 02 Internal, correct, since they name our lanes, our
internal boundaries, and a recommendation about restricting a folder. The naming prefix
"Ops_" is new and unblessed. The convention is [phase]_[what it is]_[date] and neither
document is phase-bound. Open question 4 below.

Lenses. Premise: the premise as stated (Lemar touches nothing) does not survive contact
with the signing and advising acts, and the document says so rather than working around
it. Reader: written for three readers, Ariana as the operator, Lemar as the person
approving the boundaries, and a future reader in month seven asking why it was built this
way. Gaps: the biggest is that no client-facing half can switch on pre-engagement, handled
with the two-stage design. Failure modes: the top one is a phone-sourced fact reaching the
Position Report, addressed above. Edge: an office asking to put Ariana down as contact of
record, named as prohibited. Execution: the access checklist is the critical path and none
of it is done. Fit: matches the existing card, channel, and folder conventions without
adding a surface.

## Open questions

1. The 02 Internal carve-out. Recommendation is a "Principal only" subfolder for fee
   thinking, the assessment of the group, and opening services planning, moved before her
   access is granted rather than after. Decide, then move, then grant.
2. The client-facing send split. Starting position is that Ariana sends routine logistics
   and Lemar sends anything carrying substance, a date, a number, or a judgment. Worth
   revisiting after a month of real traffic.
3. Her introduction to the group at signing. It should say plainly what she handles and
   what still comes to Lemar, so a routed question is not a surprise in month four.
4. The "Ops_" prefix. Either bless it as a convention extension for engagement operations
   documents, or move both files somewhere outside the phase naming.
5. The Google Docs conversion left literal markdown headings and renumbered the seven
   rules list as 1,1,1 with visible list artifacts. Cosmetic, and worth a cleanup pass
   before the packet is handed to Ariana.

## Round 1 answers (2026-08-20, PART R)

Lemar answered all five in #decisions (ts 1787187401):

1. The 02 Internal carve-out — **no need.** Grant the folder as it stands; no
   "Principal only" subfolder split before Ariana's access.
2. The GitHub connector write permission (asked alongside the open questions, not one
   of the five numbered above) — **yes, grant the app Contents write** on
   `lboonejr/atlas`. Not something Samira can do herself — it's a GitHub App
   installation-permission change, made in GitHub's own admin UI (Settings → GitHub
   Apps → this app → Permissions), not exposed through any connected tool. Lemar's to
   do directly; the browser/local lane stays the fallback until then.
3. The client-facing send split — **run it as written** for the first month (Ariana:
   routine logistics; Lemar: anything carrying substance, a date, a number, or a
   judgment). Revisit after a month of real traffic, per the open question as written.
4. The "Ops_" prefix — **blessed** as a convention extension for engagement-operations
   documents that aren't phase-bound deliverables.
5. Her introduction to the group at signing — **make it an assignment from her**, not
   something Samira drafts now; it's on Ariana to produce at signing.

Not asked as a numbered question but flagged in the original list (item 5, the cosmetic
Docs-conversion cleanup on the onboarding packet): carried, not yet done — cosmetic only,
waits until the access checklist and the Contents-write grant land.

## Locked

Round 1 closed 2026-08-20 — all five open questions answered, nothing reopened. Lens
coverage was already posed 8/8 at round 1 (this ran as a single-round card, unlike the
two-round split on other Camden Launch cards). Remaining before the ADMIN lane goes
live: the GitHub Contents-write grant (Lemar, GitHub admin UI), the access checklist
(Lemar, Workspace/Slack admin), and the cosmetic cleanup pass on the onboarding packet.

## Handoff

BROWSER: upload this file to the vault at
haven/vault/40-Projects/camden-dispensary-launch/ops-admin-lane-and-ariana.md on main.
Upload, do not paste.

LOCAL: the access checklist in the onboarding packet, and the 02 Internal carve-out, in
Workspace and Slack admin.

Nothing posts to Slack until the vault write succeeds.

## Working Log entry

Drafted and placed. See the entry dated 2026-08-19 in the decision record, plus two new
open items (Ariana access checklist, 02 Internal carve-out) and the note that the log's
last stamp predates both the intake system and this item.

## Sources

Camden Dispensary Launch — Working Log, last updated 2026-08-18 23:00 ET.
Camden Dispensary Launch — Project Instructions, last set 2026-08-18.
Phase00_Intake open items register_20260819, 02 Internal.
P00 client intake system, project doc, 2026-08-19, for the GitHub connector constraint.
Four decisions recorded in the 2026-08-19 Cowork thread with Lemar: Ariana as day to day
contact, ADMIN as a new fourth lane, the business build parked with harvest as we go, and
the deliverable set as the operating model plus the onboarding packet.
