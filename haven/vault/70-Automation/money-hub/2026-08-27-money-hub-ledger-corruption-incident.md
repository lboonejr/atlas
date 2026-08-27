---
created: 2026-08-27T11:01:50-04:00
updated: 2026-08-27T14:03:00-04:00
domain: automation
type: log
status: done
tags: [samira, money-hub, incident, data-integrity]
source: claude
---

# Money Hub ledger corruption — detected and repaired, 2026-08-27

## What happened
This morning's Samira run (lock `run_20260827T120501Z`) dispatched a background agent
to log a $50.60 DoorDash earning reported in #personal-finance via the **money-hub**
skill. The agent appended the earning to `income-log-2026.md` cleanly (that file is
fine, untouched by the rest of this), but then got stuck trying to hand-edit the much
larger `money-hub-ledger.md` (its `daily_targets` accrual block) across five separate
commits between 12:14 and 13:59 UTC — each one patching gaps the previous edit left,
extending the accrual window further and further into September/October. It finally
failed outright with an output-token overflow mid-edit.

The commit it left on `main` (`91478fa`) was **broken**: an unclosed YAML fence, cut off
mid-`contributions` list at `2026-10-20`, missing `goals`, `open_questions`, and —
worse — **all prior `## Update` history** (the ledger's append-only decision record).

## What I did
Verified the break directly (fetched the raw file, confirmed only 1 of 2 expected
fence markers, file ends mid-list with no closing content). Found the last clean commit
touching this file (`e6eb46ed`, 2026-08-26 ~10:20am ET — a legitimate prior PART M run)
and restored `money-hub-ledger.md` to that exact content via local git (`git show
e6eb46ed:... > file`, commit, push) — no hand-editing, no invented data, full Update
history intact. Pushed as `f8f702a`.

## What's still open (deliberately left undone)
The $50.60 2026-08-27 DoorDash earning is safely recorded in `income-log-2026.md` but
is **not yet reflected** in the ledger's accrual/`daily_targets`/dashboard — reverting
to the pre-incident ledger rolled that part back too. Redoing it needs a smaller,
more careful pass than a full-file rewrite (the file is ~4,100 lines / 249KB, which is
almost certainly *why* the agent kept running out of budget hand-patching it — worth
Lemar knowing this is a recurring structural risk, not a one-off fluke).

## Also noted, not this incident
A separate, legitimate hourly Samira run started at 14:03 UTC after this run's lock
aged past the 45-minute threshold (this run took much longer than usual because of the
background-agent work above) — that run has continued independently and appears to
have processed a real #decisions reaction from Lemar (vault open-items methodology,
"Option 1"). Not a conflict, just noted for the record.

## Source
Detected and repaired by this run (lock `run_20260827T120501Z`); no #decisions ask
needed since the fix was a straight revert of this run's own error, not a judgment
call. Flagged to Lemar directly given the "data corruption" + "your money ledger"
combination.
