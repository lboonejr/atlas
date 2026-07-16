---
created: 2026-07-16T09:00-04:00
updated: 2026-07-16T09:35-04:00
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
