---
created: 2026-09-16T11:56-04:00
updated: 2026-09-16T13:40-04:00
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

## Update 2026-09-16 — the critical path, if the plan is "pass and get to market fast"

Speed is the right instinct. The thing that actually decides the launch date is not the work —
it is the **queues**, and they are only partly on the list above.

### The four queues

1. **DORES processing the commissioning application.** Unavoidable, not compressible, starts the
   moment the application goes in after the exam. Nothing here shortens it.
2. **The 90-day county clerk oath.** Not a wait — a deadline. Same-week, not same-quarter.
3. **Google Business Profile verification. This is the hidden one.** It gates the entire demand
   side and it is not on the list above. Google's nominal timeline is up to 5 business days
   (video verification 3–5, postcard 5–14), but real-world waits of several weeks are common, and
   **as of 2025 the notary cannot choose the verification method** — Google assigns it. So GBP
   verification can outlast the commission wait, and it is the one queue that can be entered
   early: the profile can be created and submitted for verification as soon as the **name** is
   settled, without publishing it. Verify first, publish later.
4. **The second DORES filing — the electronic and remote notification.** Separate from the
   commission, required before the first electronic or remote act. RON does not go live when the
   commission does; it goes live when this clears. Budget for it as its own wait.

### What this reorders

**Pick the name this week.** It is the single upstream blocker: trade name certificate, GBP
listing, GBP verification queue, business cards, domain — all of it is downstream of one decision
that costs nothing but a phone call to the county clerk.

**Start the GBP verification the day the name clears**, ahead of the commission. An unverified,
unpublished profile does nothing wrong; a profile that starts verifying on commission day wastes
the wait.

**Check whether E&O needs a commission number before ordering.** If it does, it cannot parallelize
and it moves behind the decision. If it does not, buy it during the wait. One phone call answers it.

### The reframe: the first ten customers already exist

"Get to market" reads as building demand from zero. It is not. Cuzzie's and The Station between
them have staff who need employment paperwork, I-9s and titles notarized, vendors who need
affidavits, and a network around both that needs POAs and transfers. That is the soft-launch ten
jobs from **After the decision** item 7 — no ads, no SEO, no wait on Google. GBP and the booking
form are how job eleven onward finds him; the first ten are a text message.

So the honest launch sequence is: commission → oath → seal → tell the two networks → run those ten
by hand → and let the GBP verification, which started weeks earlier, land whenever it lands.

### The one corner not to cut

**The BlueNotary six-field trial, before any real journal entry exists.** Everything else on this
list is reversible in an afternoon. A journal entry made on the wrong platform is wrong for ten
years, and switching after the first entry means a journal migration plus a fresh DORES
notification. Moving fast everywhere else is fine. Skipping this to save a day is not.

## Update 2026-09-16T13:40-04:00 — name confirmed: Given Word Notary

**The brand name is settled. It is no longer an open item**, and it was the biggest one on this
note — it was holding the Trade Name Certificate, the Google Business Profile, the verification
queue, the business cards and the domain all at once. Full clearance results and the reasoning
live in [[2026-09-15-notary-business-backend-systems]]; three of four checks came back clear and
the fourth is a phone call, not a search.

### What section 1 now says
Strike **the brand name** from the open items. What replaces it is smaller and concrete:

- **Call the Camden County Clerk** — Courthouse (856) 225-5300 or County Store (856) 566-2920 —
  and confirm "Given Word Notary" is available at the county level. No online search exists, so
  this is the only way to check. Call before travelling; no hours are posted.
- Then **file the Trade Name Certificate in person**, $57. All registrants must appear to sign,
  and the certificate itself must be notarized — by another notary, not by Lemar.

The other three open items stand: E&O, the four DORES questions, the three BlueNotary questions.

### What this unblocks, in order
1. **The county call** — today's task, five minutes, no prerequisites.
2. **The Trade Name Certificate** — in person, once the call confirms.
3. **The Google Business Profile, created and submitted for verification.** This is the queue
   from the critical-path update above, and it is now the long pole on the demand side. The
   profile name must match the registered name, so the certificate comes first, but nothing else
   does — the profile goes into Google's queue weeks before the commission exists. Submit it, do
   not publish it.
4. **Business cards**, QR pointed at the profile.
5. **The domain**, `givenwordnj.com` — a nice-to-have, not a gate. `givenwordnotary.com` is parked
   on a marketplace and is not worth buying back.

### Still undecided, and deliberately so
**Trade name vs. LLC.** The recommendation in the brief stands: trade name now, LLC when
signing-agent work starts, because NJ holds the individual notary personally liable for notarial
misconduct regardless of entity and the E&O policy is what actually covers that. Filing the trade
name does not foreclose the LLC later.
