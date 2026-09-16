---
created: 2026-09-16T11:56-04:00
updated: 2026-09-16T11:56-04:00
domain: project
type: task
status: active
due: 2026-09-20T08:00-04:00
tags: [notary, exam, milestone, checkpoint]
calendar_event_id: t1rtn54jbd05921udlho63jqjo
source: claude
---

# Exam day — where the notary business stands and what happens next

Sunday 2026-09-20 is the NJ notary exam. This note is the checkpoint: what is still open,
what to do during the wait, and what to do the moment the commission lands.

Rendered to the reminder calendar as an 8:00 AM ET event. Related:
[[2026-09-15-notary-business-backend-systems]] (the locked plan),
[[2026-09-16-notary-commission-lifecycle]], [[2026-09-16-notary-journal-request-procedure]],
[[2026-09-16-notary-seal-journal-loss-playbook]].

**Reading of "the decision":** DORES processing the commissioning application after the exam.
If Lemar meant a different decision, the lists below still hold — only the label changes.

## Where it stands

The backend is built and merged. Two skills (`notary-intake`, `notary-journal-mirror`), four
vault notes, a booking form built but unpublished, and a workflow page. Nothing runs until the
commission exists. **Everything outstanding is external.**

## 1. Open items

- **The brand name.** Blocks the Trade Name Certificate and the Google Business Profile, which
  together are the entire front end. Biggest single blocker.
- **E&O insurance.** $100,000 through a bar-association or group plan, roughly $75/year.
- **Four questions for DORES:** lost-seal reporting mechanics · whether the journal is subject
  to inspection or copy requests, and on what terms · whether NJ caps the fee for a remote act
  separately · what happens to the journal if a commission lapses or is resigned.
- **Three questions for BlueNotary at signup:** does a Manual Session entry capture all six
  N.J.A.C. 17:50-1.11 fields · API or CSV export · do they notify the notary when records are
  subpoenaed.

## 2. While waiting for the decision

Everything here is doable without a commission. In rough order of value:

1. **Pick the brand name.** Then file the Trade Name Certificate with the county clerk in the
   county of operation. Note the certificate itself must be notarized — by someone else.
2. **Open the SoFi checking account**, kept separate from the Set-Aside pocket.
3. **Provision the Google Voice number** forwarding to the cell. That number, not the cell, is
   what goes public.
4. **Send DORES the four questions.** They are slow; asking now means answers arrive about when
   they are needed.
5. **Open the BlueNotary account and run the six-field trial.** This is the fallback gate — if a
   Manual Session cannot carry all six NJ fields, switch to NotaryCentral **before** any real
   journal entry exists. After the first entry it means a migration and a fresh DORES
   notification.
6. **Buy E&O.** Check whether the carrier needs a commission number first; if so this moves to
   the after-list.
7. **Draft the Google Business Profile copy**, ready to publish the moment the name and the
   commission are both settled.

Do not publish the booking form or the profile yet. Taking a booking that cannot legally be
performed is worse than having no front end at all.

## 3. After the decision

**First, and time-boxed: take the Commission Packet to the County Clerk and swear the oath
within 90 days.** Miss that window and the whole process restarts. Put it on the calendar the
day the packet arrives — do not rely on remembering.

Then, in order:

1. **Get the seal.** Store it locked and separate from the journal.
2. **Activate the commission lifecycle note** — record the commission number and expiry date,
   set its `due` to expiry minus 90 days, and create the continuing-education note at expiry
   minus 120 days. That one step closes the lapse risk for five years.
3. **File the DORES electronic and remote notification naming BlueNotary.** Required *before*
   the first electronic or remote act, and re-filed on any platform change.
4. **Register the anchors** in `.claude/anchors.md`: the BlueNotary source config and whether it
   is `api` or `export`, Stripe, the `Notary — Journal Exports` Drive folder, the Jotform id,
   and the business calendar routing. Until these exist both skills correctly refuse to run.
5. **Link Stripe to SoFi checking** and confirm a payout actually lands.
6. **Publish the booking form and verify the Google Business Profile.**
7. **Soft launch: the first ten jobs walked end to end by hand** — intake, calendar, act,
   journal, invoice, payment, mirror, ledger — to prove the chain before trusting it.

## Ownership

`lemar` owns every item above; none can be supplied by anyone else. `samira` owns nothing here
until the anchors exist, which is the point at which the business starts running itself.

## Sources
- claude: Claude Code session, 2026-09-16
