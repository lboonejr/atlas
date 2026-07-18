---
created: 2026-07-16T09:00-04:00
updated: 2026-07-18T08:15-04:00
domain: project
type: log
status: awaiting-decision
tags: [samira, investor, pipeline, housekeeping]
source: slack
---

# Investor pipeline — stale cold leads + unlabeled Drive folder routed to #decisions

PART E (2026-07-16 scan) found two groups of items that have been carried forward
silently in #investor-pipeline for 5+ scans (since 2026-07-11) without ever reaching
Lemar in #decisions, plus one new unlabeled Drive folder. Consolidated into one
#decisions card rather than re-flagging separately.

## 1. Two cold-lead data rooms — revive or close?

- **Bobby Lee (Emirates Investment)** and **Sweet Leaf Finance** — both had a data
  room + Gmail outreach draft built 2026-06-27. Neither ever got a Lemar reaction
  (no ✅/🫡). As of this scan their Drive folders no longer resolve (search/metadata
  errors) — may have been deleted or moved outside the Data Rooms parent.
- No index row was ever added for either (never reached "Sent").

## 2. Four cold leads — never got a room or a close

Ian Lindemann (Lead Funding), Mickey Wills, Meyer Goldman, Alfonso Rodrigo — all
surfaced as inbound cold contacts, none built into a data room, none closed out.
Carried forward unresolved since 2026-07-11.

## 3. NEW — unlabeled "Data Room" folder under the Investor Data Rooms parent

Drive folder `Data Room` (id `1nHEYc0FdIY4Kn-Q9ffkS5n66y0R5s43h`), created
2026-07-15 22:39–22:47 ET, sits directly under the Investor Data Rooms parent
(`1U7GFTuA5Tj6TMD0CWgfZhWwSbwWKWDfF`) with no company name and no matching index
row. Contents: Elevate Funding / Novus Capital / Liquidibee MCA agreements, Parke
Bank statements, the Cuzzie's cannabis license, and a Deposit History Exhibit whose
own text says it "supports the Reopening & Stabilization Plan" — this reads like
on-button-reopen backup material, not a per-investor room. Not referenced in any
Gmail thread or #investor-pipeline message found this scan. Left completely
untouched (not renamed, moved, or added to the index) since the target is unknown.

## 4. Stray empty "George" folder

Drive folder `George` (id `1uNfI-UHH53F1mFSAL1dEjYEoK9aQ_OF3`), created 2026-07-10,
empty — looks like a duplicate/abandoned folder superseded by the already-indexed
"George Irwin — A Green Roof — Data Room". Low-stakes cleanup, flagged alongside
the above rather than a separate card.

## Sources
- slack: #investor-pipeline C0BCCUKEUQ2 (carried-forward notes 2026-07-11 through
  2026-07-15 18:08 ET; none ever reached #decisions)
- drive: https://drive.google.com/drive/folders/1nHEYc0FdIY4Kn-Q9ffkS5n66y0R5s43h (unlabeled Data Room)
- drive: https://drive.google.com/drive/folders/1uNfI-UHH53F1mFSAL1dEjYEoK9aQ_OF3 (stray George folder)
- drive: https://drive.google.com/drive/folders/1U7GFTuA5Tj6TMD0CWgfZhWwSbwWKWDfF (Investor Data Rooms parent)

## Update — 2026-07-16, PART E (~09:30 ET)

Lemar replied in the #decisions thread at 08:25:48 ET (message ts
`1784204748.573089`) — a plain-text reply, not an emoji reaction, so it was missed
by the two automated passes that ran at 08:22 and 09:14 ET (both only checked for
an emoji signal). Picked up and actioned this pass:

1. **Bobby Lee** — "We can close out Bobby Lee." Added an index row, Status:
   Parked. Sweet Leaf Finance was bundled in the original question but NOT named
   in Lemar's reply — treated as still open rather than assumed closed; re-asked
   in #decisions.
2. **Four cold leads (origin reminder requested)** — answered in #decisions with
   what's on file: Ian Lindemann/Lead Funding (bridge loan, Josh 6/29, email never
   confirmed) · Mickey Wills/Mickey Mix Consult LLC (debt/equity, intro via Amir
   Armstrong, 19-yr cannabis operator background, Josh sent outreach 6/27, no
   reply) · Meyer Goldman (replied positively 6/29 "looking forward to speaking,"
   ball was in Lemar's court for a call, never scheduled) · Alfonso Rodrigo
   (equity, LinkedIn-only, context marked Unknown, generic intro drafted 6/25,
   never confirmed sent). Revive-or-close decision on these four is still Lemar's
   — re-asked, not assumed.
3. **Joey (new)** — "through a friend, we found a high-net-worth individual that
   might want to be a part of this so his name is Joey. We could change the name
   of the folder to that but basically that's what that folder is for." This
   resolves item 3 above: the unlabeled Data Room folder is Joey's room. Added an
   index row (Status: Working). Could NOT rename the Drive folder — no
   rename/move tool available in this session — flagged to Lemar to rename
   manually or supply a full name. Still need Joey's full name, contact info, and
   the specific ask before any exec summary tailoring or outreach draft.
4. **George duplicate folder** — "We can delete the George folder." Could NOT
   delete it — no Drive delete tool available in this session. Flagged back to
   Lemar to delete manually: https://drive.google.com/drive/folders/1uNfI-UHH53F1mFSAL1dEjYEoK9aQ_OF3

Index updated (Bobby Lee, Joey rows added) — commit `investor-index: Bobby Lee
Parked, Joey Working`. Reply posted in the #decisions thread with the origin
recap, the Sweet Leaf / four-cold-lead re-ask, the Joey info request, and the
George-folder tooling limitation.

## Update — 2026-07-16, PART E (~12:15 ET)

No new activity this pass in Gmail (`label:Samira/investor` minus
`Samira/investor-sent` — 0 threads) or #investor-pipeline (0 new messages since
the 10:15:52 ET status post). The #decisions thread also has no new reply since
Lemar's 10:15:25 ET follow-up questions (Sweet Leaf close-or-keep, revive-or-close
on the 4 cold leads) — both still awaiting his answer, left untouched.

A routine Drive audit of the Investor Data Rooms parent this pass turned up a
**second** mystery folder, separate from items 1–4 above: **"Jason Klein — Data
Room"** (id `1DHm0MXPAfqvE2ewBXyO4IX-tKAENulSk`), created 2026-07-10, last
modified 2026-07-13, sitting directly under the Data Rooms parent with no index
row. Checked who Jason Klein is: Gmail shows he is **not** an investor/lender —
he's Jason@Cann.Dev, an M&A broker who has been shopping the Camden space to
buyers/operators for a lease takeover (~$150K–$250K) since 2026-06-18 ("Camden
dispensary for sale" thread, cc joshua@cuzziesnj.com). The actual diligence room
Lemar sent him 2026-06-19 is a completely different folder
(`.../folders/1Ax3qCt34RYAZeIjxZcyX4Dt99pg63M-I`), and a separate,
correctly-parented "Cann.Dev — Jason Klein (M&A)" folder also exists outside the
investor tree. So this folder's presence under the Investor Data Rooms parent
looks misfiled — its contents (Elevate/Novus/Liquidibee MCA agreements, Parke
Bank statements, the Cuzzie's license, a Deposit History Exhibit) are generic
Cuzzie's financial materials, not anything built for or sent to Jason Klein.

Left completely untouched: no index row added (Jason Klein is a business-sale
broker, not an investor/lender — adding a row would misrepresent the
relationship), nothing renamed/moved/deleted. Flagged as item 5 in the open
#decisions thread rather than guessed at.

## Sources (cont.)
- gmail: thread `19eda7545ffe62f0` ("Re: Camden dispensary for sale") — confirms
  Jason Klein is Cann.Dev M&A, not an investor
- drive: https://drive.google.com/drive/folders/1DHm0MXPAfqvE2ewBXyO4IX-tKAENulSk (stray "Jason Klein — Data Room" folder)
- drive: https://drive.google.com/drive/folders/1Ax3qCt34RYAZeIjxZcyX4Dt99pg63M-I (actual buyer diligence room sent to Jason Klein 6/19)
- drive: https://drive.google.com/drive/folders/1OCHc9iAYCf-4dK7i7ZqJskNHuIO73nU5 (correctly-parented "Cann.Dev — Jason Klein (M&A)" folder)

## Update — 2026-07-16, PART E (~15:55 ET)

Read this thread fresh (all 3 replies) before doing anything else, per this pass's
instruction. Confirmed nothing new beyond what the 09:30 and 12:15 ET passes already
logged above: Lemar's only reply (08:25 ET) was fully actioned — Bobby Lee Parked,
Joey identified and given an index row, George-folder deletion request relayed back
to him (no Drive delete tool available), Jason Klein folder investigated and left
untouched. **Two items in Lemar's answer remain open and unresolved by him**: Sweet
Leaf Finance (close it too, or keep open?) and the 4 cold leads — Ian
Lindemann/Lead Funding, Mickey Wills, Meyer Goldman, Alfonso Rodrigo (revive or
archive?). No reaction or further reply on the card since the 12:15 ET check. Per
this pass's guardrail against re-nudging an already-answered-and-actioned card, left
untouched — not re-posted.

Also swept this pass: Gmail `label:Samira/investor` minus `Samira/investor-sent` — 0
threads. #investor-pipeline — 0 new messages since the Prompt Working Capital inbound
flag (13:13 ET, logged separately at
`haven/vault/20-Cuzzies/2026-07-16-prompt-working-capital-mca-flag.md`). Panther
Group email thread (`19ed22a918463463`) checked directly — Michael has not yet named
a specific day/time for the "middle of next week" call, so nothing to schedule; index
row unchanged. Index note (`index.md`) verified accurate against all of the above —
no row edits needed this pass. Prompt Working Capital's own #decisions card
(`p1784230607851799`, posted 15:36 ET) also checked — no reply yet, left alone.

Quiet pass: 0 rooms built, 0 drafts, 0 sends, 0 meetings scheduled, 0 index rows
changed.

## Update — 2026-07-17, PART E (~12:35 ET)

Full verification pass across both sources before touching anything, per this pass's
instruction to check what's already handled today.

**Gmail `label:Samira/investor` (11 threads total, checked each for `Samira/investor-sent`
and read content):**
- **George Irwin** (both addresses) — already fully closed this morning: nudge sent
  09:12 ET, #decisions card ✅'d and verified 09:35 ET (see
  [[2026-07-10-george-irwin-investor-lead]]). No new reply from George. No action.
- **Panther Group** — already carries `Samira/investor-sent`; thread re-checked
  directly (`19ed22a918463463`, 6 messages) — no message since Lemar's own 7/15
  17:15 ET reply. Michael still hasn't named a day/time. No action.
- **BizFundsHub** (`19f3d593797e09db`) — Lemar replied directly 7/7; nothing since.
  No action.
- **FundCanna** (`19f42d51ae61c0c0` the 7/8-7/14 application thread, and
  `19f616dbaabdc60f` the 7/14 4:19pm "Next Steps & Positioning" recap) — read in
  full; both are the already-logged 7/14 call outcome (declined, revisit criteria
  given, "coming months"). Fully captured in the index row already (Parked,
  informational only). No reply warranted — Sal's email is a recap, not a question.
  No action.
- **Suite420** (`19f29b5e55c3f621`, Josh's 7/3 forward) — same content already
  logged in [[2026-07-03-suite420-solutions-lender-docs-needed]]; Josh corresponds
  directly, not a Samira draft. No action.
- **Willow Financial / Colton Marshall** (`19f3ec18b012a73d`, "36 Month Terms") —
  already decided: Lemar passed 🫡 on 2026-07-08 (see
  [[2026-07-08-willow-financial-pass]]), no room, no draft, no index row by design.
  Confirmed still no reply needed (cold pitch has a self-serve decline). No action.
- Two automated notifications (Drive share, Plaid/Magenta) — not correspondence, no
  action.
- Also spot-checked the separate **Willow Capital** (Lucas White) thread
  (`19f66bc8923ab429`, general-email-loop territory, intentionally not on the
  investor index) — still just the one inbound message, draft already sitting in
  Gmail Drafts from the 7/15 scan. No new reply. No action.

**#investor-pipeline** — 0 new messages since the 7/16 16:13 ET scan post; no new
contact drop from Lemar.

**#decisions** — only investor-related item today is the George Irwin card above,
already ✅'d and closed. Prompt Working Capital's 7/16 15:36 ET pursue/decline card
(`p1784230607851799`) re-checked — still no reply/reaction; correctly left alone
per the open-decision guardrail. Sweet Leaf Finance and the 4 cold-lead
revive-or-close questions from this note also still unanswered — left untouched
(no re-nudge on an already-surfaced card).

**Index note** (`index.md`) verified accurate against all of the above — no row
edits needed this pass (nothing changed status).

Quiet pass: 0 rooms built, 0 drafts, 0 sends, 0 meetings scheduled, 0 index rows
changed. Posted a short status line to #investor-pipeline for the record.

## Update — 2026-07-18, PART E (~08:1x ET)

Full verification pass across both sources; nothing to redo — this scan picks up
right behind the 7/17 ~17:2x ET post that already logged the Suite420 nudge, the
7/17 Fundwell backfill, and the 7/17 ~5:20pm ET George Irwin re-check (all three
already reflected in `index.md`).

**Gmail `label:Samira/investor -label:Samira/investor-sent`** — 0 threads (nothing
un-actioned). Direct spot-checks for the three names most likely to have moved
overnight — George Irwin (both addresses), Dave Miesner/Suite420, Michael
Teller/Panther Group — `newer_than:2d` — 0 new messages from any of them. George's
last word remains his 7/13 "let me digest"; Suite420's last word remains Dave's
7/17 4:02pm ET nudge (already logged); Panther still hasn't named a day/time for
the "middle of next week" call.

**#investor-pipeline** — 0 new messages since Samira's own 7/17 ~17:2x ET status
post (ts `1784323125.099269`); no new contact drop from Lemar.

**#decisions** — checked the last 15 messages; no new investor-pipeline card.
Sweet Leaf Finance (close-or-keep) and the 4 cold-lead revive-or-close question
(Ian Lindemann, Mickey Wills, Meyer Goldman, Alfonso Rodrigo) remain unanswered —
left untouched per the no-re-nudge guardrail. Prompt Working Capital's
pursue/decline card also still unanswered — left alone. Nothing else in
#decisions today touches an investor/lender thread (today's new cards — Liquidibee
lawsuit bank-statement ask, GreenBooks nudge, National Secure Transport invoice,
Regus, Parke Bank secure message — are all Cuzzie's ops/collections items, not
investor-pipeline).

**Index note** (`index.md`) verified accurate against all of the above — no row
edits needed this pass (no status changed).

Quiet pass: 0 rooms built, 0 drafts, 0 sends, 0 meetings scheduled, 0 index rows
changed.
