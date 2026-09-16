---
created: 2026-09-16T11:56-04:00
updated: 2026-09-16T18:35-04:00
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

## Update 2026-09-16T17:05-04:00 — two more queues for the wait list, and two decisions that moved to now

The business now runs three channels, not one: consumer, signing service (loan signings), and
real estate agents. See [[2026-09-15-notary-business-backend-systems]] (Updates of
2026-09-16T15:10 and 17:05) and [[2026-09-16-notary-b2b-acquisition-tracks]].

**The critical path does not change.** Exam, commission, oath, seal — identical. Everything
below is either a queue that runs in parallel with the wait already happening, or a purchase.
That is the whole reason both new channels could be added without moving the launch date.

### What section 2 gains — three things to start during the wait

8. **Study for and take the signing agent certification exam.** NNA packages from $199, 45
   questions, 80% to pass. Not legally required in NJ, effectively mandatory in practice — the
   signing services' own contracts require screened, certified notaries. Doable now, with no
   commission.
9. **Order the annual background screening** (~$60–100/yr). A turnaround nobody controls, so it
   is a waiting line like the Google verification, entered early rather than on commission day.
10. **Have the first conversations with agents Lemar already knows.** One honest line — "I'm
    becoming a notary; if you ever have a seller who can't make closing or a client out of
    state, call me" — costs nothing and starts the slowest-building channel first.

**The limit on item 10, and it matters:** telling an agent to call when they need a notary is
honest. **Taking the booking is not**, until the commission exists. Same rule as the unpublished
booking form.

### The vendor packet — build it once during the wait

Every signing service asks for the same four things: **W-9, E&O certificate, background screening
result, certification certificate.** Assemble them in one Drive folder alongside the commission
certificate, a seal impression photo, and the entity filing.

**This folder may be linked and shared freely** — business credentials, no signer PII. It is the
opposite of the journal exports folder rule, and keeping the two apart is deliberate.

### Two decisions promoted from "later" to "now"

- **LLC vs. trade name.** No longer theoretical. **The name on the W-9 must match the registered
  entity**, and that W-9 goes to every signing service. Deciding after registering at a dozen
  platforms means correcting it at a dozen platforms.
- **Which printer.** A loan package is 100–200 pages on both letter and legal, usually printed
  twice. A dual-tray laser (Brother HL-L6210DWT ≈ $330) is the reference point; single-tray means
  swapping paper mid-package.

### One new open question, replacing nothing

**Which signing service platforms to register with has not been researched at all.** No platform
evaluated, no title company relationship exists. It is the largest unknown left on the plan and
the next real piece of work. Registration is normally free; **payment reliability matters more
than rate**, and a new company's first job is a credit decision rather than a scheduling one.

### The standing sequencing advice is unchanged
Run the first ten **consumer** jobs by hand. A botched acknowledgment costs a redo; a botched loan
package costs a funding delay and a title company that never calls again. Prove the chain where
the mistakes are cheap.

## Update 2026-09-16T18:10-04:00 — LLC name picked, printer picked, platform order set. The county trip may be off.

Full reasoning in [[2026-09-16-notary-llc-printer-platforms]]. Three of the open decisions are
now answered.

### 1. The LLC: `Given Word LLC` — Lemar's call, recorded
Very likely available: the 2026-09-16 clearance searched the state business name database for
"Given Word" and got nothing, and that is the same database an LLC name is checked against.
Confirmed only at filing.

**This changes section 2 of this checkpoint.** A NJ county clerk registers trade names for
**individuals and partnerships only** — LLCs and corporations register with DORES in Trenton.
So forming the LLC **replaces** the $57 Camden County counter trip rather than adding to it.

**Do not cancel the county trip until the clerk confirms it.** It is a five-minute call against
a step that was already researched, scheduled, and has a call script written for it
([[2026-09-16-camden-county-clerk-call-script]]).

Because the brand ("Given Word Notary") differs from the entity ("Given Word LLC"), the LLC also
files a **Registration of Alternate Name**, $50, valid five years. Using the trade name before
registering it costs $50 plus a $50 penalty per year of use. **The Google Business Profile name
must match the registered name**, so the alternate name is a front-end dependency too.

Revised filing sequence: **LLC ~$125 → alternate name $50 → EIN (free, and it keeps Lemar's SSN
off a dozen W-9s) → annual report $75/yr.**

### 2. The printer: `Brother HL-L5210DWT`, ~$300–350
The working default for signing agents. Two trays, letter and legal both loaded, so a 150-page
package prints in one pass. The HL-L6210DWT is the same thing a size up, worth buying if the
volume arrives, not before.

Three things that matter: **two trays**, **laser not inkjet** (county recorders can refuse to
record inkjet), and **high-yield toner from day one**. Confirm the tray capacities on the exact
listing — Brother's model numbers in this family differ by a letter.

Add a **sheet-feed scanner** if the printer is not an all-in-one. Scan-backs are due within
hours, and a flatbed will not do 150 pages.

### 3. Platforms: Snapdocs first, then direct registrations
Highest order volume in most markets, free, and many signing services schedule through it.

**"Snapdocs Verified" is the status that gets work, and it needs exactly the vendor packet:**
commission, bond if applicable, **the full background check report** (not the NNA certificate),
E&O policy, verified ID. Building the packet *is* the registration.

Two gotchas: they want the **actual report PDF**, and the **name, email and phone on the NNA
profile must match the Snapdocs profile exactly**.

Then register directly with the signing services — Amrock, ServiceLink, Coast2Coast, Signature
Closers, Mortgage Connect, Rocket Close — several of which also source through Snapdocs, so it
overlaps rather than replaces. Most Snapdocs work lands **$75–$150**; title companies posting
directly often pay **$125–$200+**. Net-30 is the normal term.

### What is left open
Nothing on this list. The remaining open items are unchanged: the four DORES questions, the three
BlueNotary questions, E&O, and the exam itself.

## Update 2026-09-16T18:35-04:00 — entity name LOCKED: `Given Word Notary LLC`

Lemar reversed the `Given Word LLC` + alternate name plan from the update above. **The entity and
the brand are now one name: `Given Word Notary LLC`.** Full reasoning in
[[2026-09-16-notary-llc-printer-platforms]].

**What drops off this checkpoint:**
- The **$50 alternate name filing** — not needed, entity name and trade name are the same string
- Its five-year renewal
- The risk of the Business Profile name not matching the registered name

**What stands up the entity: ~$125 and a free EIN.** Get the EIN — it keeps Lemar's Social
Security number off a dozen signing service W-9s.

**The county trade name trip is still to be confirmed, not yet cancelled.** A NJ county clerk
registers trade names for individuals and partnerships; LLCs register with DORES. Call the clerk
([[2026-09-16-camden-county-clerk-call-script]]) before dropping a step that is already planned.

**Platform decision: Snapdocs first, and only Snapdocs until it is working.** Direct registrations
come after one real verification has been through.

**One name everywhere from here on.** Bank account, Stripe, Google Business Profile, W-9, NNA
profile, Snapdocs: `Given Word Notary LLC`, spelled the same way each time. Name mismatches are a
known cause of Snapdocs verification stalling.

**The W-9 cannot be filled out until the LLC and EIN exist**, and every platform wants the W-9 —
so the entity filing is now the first domino on the whole B2B side.
