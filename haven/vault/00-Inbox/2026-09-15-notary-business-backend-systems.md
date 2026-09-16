---
created: 2026-09-15T16:09-04:00
updated: 2026-09-16T10:48-04:00
domain: project
type: brief
status: active
tags: [stormy, notary, recordkeeping, money]
source: slack
---

# Notary business — backend systems (recordkeeping + money management)

Lemar (Convo 2 self-DM, 2026-09-15 15:59 EDT): "I want to start making the backend to
my notary business now, I want to see how notaries usually structure their workflow
and try to build out a recordkeeping system and money management system."

## What this is
A raw idea, dropped while he's mid-way through the 7-day notary bootcamp curriculum
(hasn't taken the exam or been sworn in yet — see [[notary-services]] and the
become-a-notary-NJ note). He wants the operational backend — how a notary logs acts
and tracks money — designed and built now, ahead of his first paid signing, rather
than scrambled together later.

Related: [[notary-services]] (`40-Projects/notary-services/2026-07-13-notary-services-project.md`)
already settled the venture direction (standalone side income, standard NJ notary
commission as the prerequisite either way, mobile/signing-agent path optionally on top)
but left footprint and timeline open. This note is a new lane on the same venture — the
systems layer, not the licensing layer — so it gets its own brief rather than an Update
on that note (different note type, different phase).

Context pulled: NJ notary law requires a journal (paper or electronic) logging every
notarial act, plus a seal/stamp — noted in the notary-services project note from the
7/14 research pass. No existing recordkeeping or money-tracking system for this venture
exists yet. The personal `money-hub` skill/ledger exists and is explicitly personal-only,
two-pocket (Spending/Set-Aside), due-date-order allocation — worth checking whether
notary income folds into it or needs its own ledger (see pressure test plan, dimension 7).

## Pressure test plan

Size: **medium** — two systems (recordkeeping + money), real money once signings start,
something new to maintain long-term, awkward to unwind once his journal-of-record has
real entries in it. ~8 questions.

1. **Problem & payoff** — ASSUME: the idea states it plainly — he wants the
   recordkeeping + money-tracking infrastructure ready as the operational backend for
   the notary business, not itself a source of revenue. Payoff is being ready on day
   one instead of scrambling once signings start.
2. **Scope & hardest constraint** — ASK (crux), 2 parts:
   a. NJ notary law requires a journal of notarial acts with specific fields (date,
      type of act, fee charged, signer info, etc.). Do you want this system built to
      specifically satisfy that legal journal requirement, or something more general/
      informal that you'd still keep a separate paper journal alongside?
   b. Is this running as you personally (sole notary, SSN), or are you setting up a
      DBA/LLC for it? That decides whether the money side lives inside your personal
      Money Hub ledger or needs to stay separate.
3. **Success & failure** — ASK: what does "working" look like on day one — being able
   to produce a complete journal on request, knowing net notary income at a glance, or
   both? What's the smallest version that counts as shipped, versus what can wait?
4. **Dependencies & risk** — ASK (crux): you haven't taken the exam or been sworn in
   yet. Building the system's structure now risks assuming details (seal format,
   required journal fields, NJ's fee caps per notarial act) that could still shift
   until you're actually commissioned and trained. Build the structure now and fill in
   specifics once commissioned, or wait until after the exam?
5. **Timing & preconditions** — ASSUME: no rush, no deadline — this rides alongside
   exam prep, ready before the first paid signing. No `due` on this note.
6. **Blast radius & reversibility** — ASSUME: internal recordkeeping/tracking, nothing
   leaves your control, no outside party's money moves. The real risk is professional/
   legal (an incomplete or inaccurate journal if ever audited or requested by a title
   company), not financial exposure — flagged, not a Reggie-compliance gate (Reggie
   covers Cuzzie's/Station cannabis compliance, not NJ notary law).
7. **Automation & data flow** — ASK (crux): does notary income/fees become a new
   stream inside the existing `money-hub-ledger.md` (picked up by its due-date-order
   allocation and the Convo 2 money-drop sweep), or does it need its own separate
   ledger/system entirely, since Money Hub is currently scoped personal-only?
8. **Ownership & upkeep** — ASK: do you want to log each signing yourself (in Haven,
   a spreadsheet, wherever), or should this route through a Convo 2 drop pattern like
   money-hub's existing sweep, so Samira logs it for you as you report each signing?

Asks: 6 (3 crux — 2a, 4, 7). Assumed: 3 dimensions (1, 5, 6). N/A: none.

## Sources
- slack: Convo 2 self-DM (`D0BBVV54L5R`), ts `1789502352.375749`, 2026-09-15 15:59 EDT

## Update 2026-09-16T08:49-04:00 — all 6 asks answered; scope expanded to the whole business; re-sized to LARGE

**Lemar's answers to the first batch** (Convo 2 thread, 2026-09-15 17:09 EDT):
1. **(2a) Legal journal** — build it to satisfy the NJ legal journal requirement **to a T**,
   not a looser parallel system.
2. **(2b) Entity** — start as a **sole notary** (himself, SSN), expand the structure as the
   business grows.
3. **(4) Timing vs. commission** — **build the skeleton now**, fill in commissioned-only
   specifics (seal, exact fee caps, final journal fields) once sworn in.
4. **(7) Money** — notary income becomes a **new stream inside the existing money-hub
   ledger**, not a separate system.
5. **(8) Logging** — **drop-it-in**: he reports each signing into Convo 2 and Samira logs it,
   same pattern as a money drop.
6. **(3) Day one "working"** — **both**: produce a clean, complete journal on request AND
   know net notary income at a glance.

**Scope expansion** (Convo 2, 2026-09-16 08:32 EDT): "I think we need to think about payment
processing and front end as well how we reach the customers, how we perform the transaction,
and recordkeeping associated with it." Plus, this session: make it the most efficient and
automated business possible, with **Samira overseeing operations**.

That is no longer a backend brief. It is the whole business: demand generation, booking,
the at-the-table transaction, money in, the legal record, and the ops layer that runs it.

### Re-size: MEDIUM → **LARGE**
It now reaches outside parties (paying customers), moves real money through a third-party
processor, handles signer PII and ID data under a statutory recordkeeping duty, and is hard
to reverse once live (a processor account tied to his SSN, a public brand, a journal of
record with real entries in it). Target 13-20 asks. Lemar said "we have enough runway,
flesh out everything," so the bake runs deep rather than tight.

### Re-verdicted pressure test plan (v2)

1. **Problem & payoff** — CLOSED. Unchanged from v1, now widened: the payoff is a notary
   business that runs on rails Samira operates, not a side gig he hand-manages.
2. **Scope & hardest constraint** — REOPENED, ASK (crux). 2a/2b answered, but the hardest
   constraint moved: it is now **which customer the business actually serves**. Walk-up
   consumer acts are capped by statute at a few dollars per act (the money is in the travel
   fee), while loan-signing work from title companies and signing services pays per package
   on net-30 invoice terms. Those are two different businesses with two different front ends
   and two different money rails. Also open: is **RON (remote online notarization)** in scope,
   since NJ permits it with separate registration and it is the single biggest automation
   lever available.
3. **Success & failure** — PARTIALLY CLOSED (both, per his answer). ASK remaining: the
   numbers — signings per month that makes this worth running, and the tell that it is not.
4. **Dependencies & risk** — REOPENED, ASK (crux). New hard dependency: **whether a digital
   journal can be the journal of record at all.** A paper journal captures the signer's wet
   signature in the book; an electronic journal only satisfies "to a T" if it captures an
   equivalent. If it cannot, the architecture is a paper book as the legal record plus a
   searchable Haven mirror, which changes every downstream automation.
5. **Timing & preconditions** — ASSUME: still no deadline; skeleton now, live once
   commissioned. No `due` on this note. But the front end and processor cannot go live before
   the commission exists, so the plan phases around the swearing-in.
6. **Blast radius & reversibility** — REOPENED, ASK (crux). Three new exposures that did not
   exist in v1: (a) **signer PII and ID data** would live in a git repo — Haven's storage
   posture has to be settled before a single real journal entry is written; (b) **chargebacks**
   on a notarial act cannot be undone, the notarization is already performed and possibly
   recorded; (c) a **processor account and public brand under his own SSN** is not cheaply
   unwound. Still not a Reggie gate (Reggie is cannabis compliance, not NJ notary law), but
   this is now genuine professional and financial exposure, not internal tooling.
7. **Automation & data flow** — REOPENED, ASK. v1 settled money-hub as the money home. Open
   now: the **single intake point**. The efficient design is one booking/intake form that fans
   out to calendar event, journal entry, invoice, and ledger line, so nothing is ever
   hand-keyed twice. That only works if every job, referrals included, is forced through it.
8. **Ownership & upkeep** — REOPENED, ASK. Samira overseeing operations has to be specified:
   what she does unattended, what needs his gate, and how a missed journal entry or an unpaid
   invoice surfaces before it becomes a problem.

Batch 2 asks are recorded in the next Update once posed. Status stays `awaiting-decision`.

### Sources (this update)
- slack: Convo 2 self-DM (`D0BBVV54L5R`), 2026-09-15 17:09 EDT reply and 2026-09-16 08:32 EDT
- claude: Claude Code session, 2026-09-16

### Batch 2 — the 19 asks (posed 2026-09-16)

**A. What business this actually is (dim 2)**
1. CRUX — Which customer is the business: consumer mobile notary (acts + travel fee), loan
   signings for signing services and title companies (per package, net-30), or both with one
   named as the lead? Two different front ends, two different money rails.
2. CRUX — Is RON (remote online notarization) in scope now, later, or never? It is the biggest
   automation lever available and it changes the whole front end.
3. Service area radius from Camden, and how travel is priced (flat, tiered by distance, by
   time of day, after-hours premium).

**B. The journal of record (dims 4, 6)**
4. CRUX — Is the legal record a bound paper journal with a Haven mirror for search and
   reporting, or an electronic journal standing as the record itself? Turns on whether NJ
   requires the signer's own signature in the book.
5. CRUX — Where does signer PII live? Journal entries carry names, addresses, and ID details.
   Haven is a git repo; that has to be settled before the first real entry exists.
6. Capture ID images or thumbprints at all, or fields only (type, issuing state, expiry)?
7. Retention period, and who can lawfully request a copy of the journal.

**C. Money (dim 7)**
8. CRUX — Enforce a two-line invoice on every job, statutory notarial fee separate from travel
   or convenience fee? They are capped differently and recorded differently in the journal.
9. Processor: Square, Stripe, or peer-to-peer. Tap-to-pay at the table is the deciding feature.
10. Separate business checking account even as a sole prop, or run it through personal?
11. Auto tax set-aside at a fixed percentage into the money-hub Set-Aside pocket at log time?
12. Who chases net-30 invoices from signing services, and does `chase-commitments` own it?

**D. Front end and reach (dims 2, 7)**
13. CRUX — One intake point: is every job, referrals and repeat clients included, forced
    through the booking form so nothing is ever hand-keyed twice?
14. Public surface: brand name, Google Business Profile plus a one-page booking site, or
    profile and phone only?
15. Which marketplaces and directories to list on for signing work.
16. Response-time promise, which decides whether Samira may auto-confirm a booking or must
    always wait for his gate.

**E. Samira's oversight (dims 8, 3)**
17. CRUX — What may Samira do unattended versus what needs his check: confirm a booking, send
    a quote, send an invoice, reply to a customer, write the journal entry, post the ledger line.
18. Alarms: completed calendar event with no journal entry within N hours, invoice unpaid past
    N days, a signing logged with no payment recorded.
19. Volume that makes this worth running, and the number that says pull the plug.

Asks: 19 (7 crux — 1, 2, 4, 5, 8, 13, 17). Assumed: dims 1 and 5 closed. N/A: none.

**Details to confirm from the source, not guessed here:** current NJ statutory maximum fee per
notarial act; the exact journal fields and retention period NJ requires; whether NJ accepts a
fully electronic journal for in-person acts and whether the signer must sign it; NJ RON
registration requirements; whether E&O insurance or a bond is required or merely expected by
title companies.

## Update 2026-09-16T09:40-04:00 — batch 2 answered, NJ law researched, journal architecture corrected

### Lemar's answers (batch 2)
1. **Customer** — consumer mobile notary first, grow into signing work later.
2. **RON** — in scope now.
3. Pricing — asked for suggestions.
4. **Journal** — wants electronic; asked whether the signer's wet signature is required.
5. **PII** — proposed an Excel sheet.
6. **ID capture** — wants ID images or thumbprints captured.
7. **Retention** — base it on the notary laws.
8. **Two-line invoice** — yes.
9. **Processor** — Stripe.
10. **Banking** — personal, but a dedicated account for the business.
11. **Tax set-aside** — yes, automatic at log time.
12. AR chasing — wire into Samira's responsibilities.
13. **Intake** — one intake point, with a manual backup flow for phone-call walk-ups.
14. **Front end** — profile and phone first, booking site later.
15. Directories — asked for a rephrase.
16. **Response time** — within one business day.
17. **Samira's authority** — she can do all of it if the parameters are set properly: letter of
    the law, his voice, NJ-compliant notary best practices.
18. **Alarms** — all three.
19. Volume — asked for a suggestion.

### NJ law research (2026-09-16) — N.J.A.C. 17:50-1.11, 1.14, 1.16, 1.18

**Journal (N.J.A.C. 17:50-1.11).** Required entries per notarial act: date and time; type of
act; name and address of each person the act is performed for; if identity rests on personal
knowledge, a statement to that effect; if on satisfactory evidence, a brief description of the
method of identification and the credential presented; and an itemized list of all fees charged.

- **The signer's signature is NOT among the required entries in NJ.** (Unlike CA, FL and others.)
  This is the finding that unblocks a fully electronic journal with no paper book.
- Journal may be tangible or electronic. Tangible means a permanent bound register with
  consecutively numbered lines and pages. **Electronic means a "permanent, tamper-evident
  electronic format."**
- **Only ONE journal at a time**, covering both tangible and electronic records.
- **Retention: 10 years after the last notarial act.**

**Fees (N.J.A.C. 17:50-1.18).** $2.50 per act for oaths, affidavits, proofs of deed and
acknowledgments. $15.00 for grantors in a real estate transfer regardless of the number of
services in the transaction. $25.00 for mortgagors in a real estate financing regardless of
number. Travel and other non-notarial fees are not set by the State; the notary sets them and
they must be separate and disclosed.

**RON.** Permanently authorized in NJ since 2021-10-22. Notify the State Treasurer through the
DORES notary portal identifying the communication technology platform before the first remote
or electronic act, and again whenever the platform changes. Identity proofing requires at least
two of credential analysis, knowledge-based authentication, or biometric verification, run by
the platform. The full session including identity verification must be audio-video recorded.
**AV recordings retained 10 years.**

**Not confirmed, do not rely on until verified against the manual or the reg text:** whether NJ
sets a separate maximum fee for a remote act; whether and how the journal is subject to
inspection or copy requests; whether NJ restricts recording a credential's full ID number.

### Architecture correction — the journal of record is NOT Haven and NOT Excel

His answer 5 (Excel) and the working assumption that Haven holds the record both fail the
regulation. "Permanent, tamper-evident electronic format" is a product property. An .xlsx file
is freely editable with no audit trail. A markdown note in a git repo is rewritable by a force
push and is not a recognized tamper-evident journal. He asked for the legal journal satisfied
**to a T**, so this cannot be fudged.

**Corrected design, three layers:**
1. **Journal of record** — a commercial tamper-evident electronic journal, or the RON
   platform's built-in journal, holding the six required fields. Because NJ allows only one
   journal at a time, the same product must carry in-person acts and remote acts both. This is
   the single biggest platform decision in the project and it now gates the build.
2. **Business mirror** — Haven holds the non-PII operational record: date, act type, act count,
   fee split, travel fee, payment status, mileage. Drives reporting and money-hub. No signer
   names, addresses, or credential details.
3. **PII overflow, if any** — access-controlled Google Drive, never the git repo, never a
   spreadsheet synced to a personal machine. Preference is to hold no PII outside the journal
   of record at all.

**ID images and thumbprints (his answer 6):** NJ requires only a brief description of the method
and the credential presented, not an image and not a thumbprint. Capturing and storing
government ID images creates real breach exposure under NJ's breach-notification law for zero
statutory benefit on consumer work. Recommendation: record credential type, issuing state and
expiry, not a stored image and not the full credential number. For RON the platform holds the
credential analysis inside the mandatory AV recording, which is where it belongs. Recommend
against thumbprints for consumer work; revisit only if signing services demand it later.

**Samira's hard boundary (his answer 17):** she may run intake, scheduling, confirmations,
invoicing, payment reconciliation, AR chasing, mirror entries and reporting. She may **never**
decide whether a notarial act may be performed, never advise on which certificate a document
needs, and never explain or draft document content. That is unauthorized practice of law and it
is the fastest way a NJ notary loses a commission. The notarial judgment and the journal entry
in the record stay with Lemar at the table.

### New asks opened by this round
20. CRUX — Which single platform is the journal of record, given NJ's one-journal rule and that
    it must cover both in-person and RON acts?
21. Confirm the corrected three-layer design replaces the Excel plan.
22. Public phone number: his personal cell, or a separate business line, given it goes on a
    public Google Business Profile?
23. Which dedicated account is "the specific account" for answer 10?
24. Stripe under his SSN as a sole prop: confirm, and confirm the 1099-K lands where he expects.
25. Confirm the recommendation to skip stored ID images and thumbprints, or override it.

Asks answered: 19. New asks: 6 (1 crux). Status stays `awaiting-decision`.

### Sources (this update)
- claude: Claude Code session, 2026-09-16, with web research on N.J.A.C. 17:50-1.11, 1.14,
  1.16 and 1.18 and NJ RON law (A4250, effective 2021-10-22)

## Update 2026-09-16T10:25-04:00 — platform research, pricing revised down, asks 21-25 answered

### Answers
- **21** Three-layer design confirmed; the Excel plan is dead.
- **22** Public number is his personal cell.
- **23** Deposit account is his **SoFi savings account**.
- **24** Stripe under his SSN as a sole prop, 1099-K to him personally, confirmed.
- **25** Confirmed: no stored ID images, no thumbprints. Credential type, issuing state and
  expiry only, per N.J.A.C. 17:50-1.11's "brief description of the method of identification
  and the identification credential presented."
- **3** Travel pricing to come down slightly to promote volume (revised below).
- **20** Platform decision deferred pending this research.

### Platform research (2026-09-16) — the one-journal rule is the deciding constraint

NJ allows only one journal at a time covering tangible and electronic records both. That makes
"which platform" a single decision, not two. It is compounded by the DORES rule that the notary
must notify the State Treasurer of the communication technology platform **before** the first
electronic or remote act **and again whenever the platform changes** — so switching later costs
paperwork. Pick once.

**Option 1 — NotaryCentral (Business Suite + Digital e-Journal).** Its e-Journal is documented
as covering both RON and in-person acts, and entries are hash-locked on save so later alteration
breaks the hash, which is a direct answer to "permanent, tamper-evident." Listed at $119.95 +
$19.95 billed annually ($139.90), plus roughly $1.50 ID verification and biometrics and $1.50
notarization in per-session credits. Cleanest fit to the one-journal rule. API surface unverified.

**Option 2 — BlueNotary as both RON platform and journal.** Roughly $5 platform fee per session
covering KBA, ID check and video storage, about $4 per signer, Notary Pro at $297/year. It keeps
a journal with bulk export, and advertises audit trails and API access. Best automation surface
of the three, which is what lets Samira pull the mirror instead of Lemar retyping. Open question:
whether its journal accepts manually entered in-person acts carrying all six NJ fields.

**Option 3 — NotaryAct as journal of record plus a separate RON platform.** Cheapest journal at
$49.99/year under 60 acts a year, $9.99/month above that, with ID scanning and journal printing.
But pairing it with a RON platform that keeps its own journal raises the two-journal question
under 17:50-1.11. Only viable if RON acts are also entered in NotaryAct and the platform's record
is treated purely as the supporting AV recording, and that reading should be confirmed with DORES
before relying on it.

**Ruled out for this use case:** Proof at roughly $50 for comparable multi-signer work and
OneNotary at $25 per session with business plans from $65/month are priced for volume or
enterprise, not a solo notary bringing his own clients. Secured Signing is noted publicly as a
DORES-trusted RON and IPEN provider and is worth a look if Options 1 and 2 both fail the
in-person-entry test.

**Recommendation: Option 2 if BlueNotary's journal accepts manual in-person entries with all six
NJ fields; otherwise Option 1.** The API and export are the difference between Samira maintaining
the business mirror automatically and Lemar keying every act twice, which is the entire
efficiency thesis of this project.

All prices are vendor or secondary sources as of 2026-09-16 and must be confirmed at signup.

### Revised pricing (his answer 3: slightly cheaper for volume)

Statutory fees are unchanged and not discountable: $2.50 per act for oaths, affidavits, proofs of
deed and acknowledgments; $15.00 for grantors in a real estate transfer; $25.00 for mortgagors in
a real estate financing, each regardless of the number of services in the transaction.

Travel fee, revised down roughly 13 percent from the first proposal:

| Tier | Was | Now |
|---|---|---|
| Within 10 miles of Camden | $35 | **$30** |
| To 20 miles | $50 | **$45** |
| To 35 miles | $75 | **$65** |
| After 7pm, weekends, holidays | +$25 | **+$20** |
| Hospital, jail, nursing home | +$25 | **+$20** |

RON: $25 per act technology and convenience fee remains the proposal, still gated on confirming
whether NJ caps remote act fees separately. Do not publish a RON price before that check.

**Volume targets revised for the lower prices** (average job now roughly $38 to $50):
floor 15 jobs a month, target 30 by month six, pull the plug under 6 a month by month four with
a verified Google Business Profile live throughout.

### Two flags on his answers, not blockers
- **Cell on a public profile (22).** Once it is on a Google Business Profile it is permanent and
  public, and it attracts lead-gen spam. A Google Voice number forwarding to the same cell gives
  the same reachability, a number he can hand to Samira for logging, and one he can cut off.
- **SoFi savings as the Stripe payout account (23).** Some banks reject ACH credits to savings
  accounts, and a savings account already doing set-aside duty muddies the two-pocket model.
  Confirm Stripe will pay out to it before launch, and keep the notary deposit target distinct
  from the money-hub Set-Aside pocket.

### Still open
20. The platform call, pending the BlueNotary in-person-entry check.
26. Whether NJ caps the fee for a remote act separately.
27. Whether to put a Google Voice number in front of the cell.

Status stays `awaiting-decision`.

### Sources (this update)
- claude: Claude Code session, 2026-09-16, web research on NJ e-journal and RON platforms

## Update 2026-09-16T09:30-04:00 — PLAN LOCKED. Platform decided, last asks closed, status → active

### Closing answers
- **20 Platform** — BlueNotary checks out, so per Lemar's standing instruction the call is
  **Option 2: BlueNotary as both RON platform and journal of record.**
- **23 Bank** — **SoFi checking**, not savings. Resolves the ACH-to-savings risk and keeps the
  notary deposit clear of the money-hub Set-Aside pocket.
- **26 NJ remote fee cap** — see finding below.
- **27 Google Voice** — yes. A Google Voice number forwards to his cell and is what goes public.

### Why BlueNotary passes the one-journal test
It carries all three act types in a single journal:
- **RON** sessions, journaled automatically with the mandatory AV recording.
- **IPEN** (in-person electronic notarization), a first-class product on the platform for
  in-person signers using electronic documents and an electronic seal.
- **Manual Session** entries for ordinary in-person wet-ink acts, enterable in the journal and
  bulk-importable by CSV, including from a Notary Gadget export.

Plus journal export, audit trails, and an API, which is what lets Samira maintain the business
mirror without Lemar keying anything twice.

**Verification limit, stated honestly:** BlueNotary's helpdesk and API reference pages could not
be fetched directly from this environment (egress-blocked), so the field-level confirmation that
a Manual Session entry captures all six N.J.A.C. 17:50-1.11 fields comes from secondary sources.
**Lemar must confirm the six fields in a live trial entry before the first real act.** If a field
is missing, fall back to Option 1 (NotaryCentral) before any journal entry exists, not after.

### Finding on 26 — NJ sets no separate RON fee cap
No published separate maximum for a remote act could be found in N.J.A.C. 17:50-1.18 or in NNA's
2026 state fee data. The defensible reading: **17:50-1.18 caps the notarial act itself regardless
of medium, so $2.50 applies to a remote act too**, and anything charged above it must be a
separate, disclosed, non-notarial technology and convenience fee. That is structurally identical
to the travel fee and it drops straight into the two-line invoice already approved at ask 8.
This is a reading, not a confirmed published cap. Confirm with DORES before publishing a RON
price.

---

# LOCKED PLAN — NJ mobile notary business

## Mission
Stand up a one-person NJ notary business that serves consumer mobile and remote clients, whose
legal record is correct to the letter of N.J.A.C. 17:50, and whose entire operational loop
(intake, scheduling, invoicing, payment, reconciliation, reporting) runs through Samira so that
Lemar's only manual work is the notarial act itself. Day one means both: a complete journal
producible on request, and net notary income visible at a glance.

## Success criteria
- **Metric:** jobs per month, and net notary income visible in money-hub without a manual step.
- **Minimum viable win:** 15 jobs a month, every one of them with a compliant journal entry and
  a reconciled payment, and zero acts keyed by hand into two places.
- **Target:** 30 jobs a month by month six.
- **Pull the plug:** under 6 a month by month four, with a verified Google Business Profile live
  the whole time.

## Timing & preconditions
No deadline; this is a Stormy project and carries no `due`. Hard sequence: nothing customer-facing
goes live before the commission exists. The DORES platform notification must be filed **before**
the first electronic or remote act, and re-filed on any platform change, so the platform choice
is effectively one-way once filed.

## Phases

**Phase 1 — Get commissioned.** Owner: `lemar`. Finish the bootcamp, pass the NJ exam, file the
Commissioning Application and the Notary Public Registration Application, swear the oath at the
County Clerk within 90 days, obtain the seal. Output: an active five-year commission. Depends on:
nothing. Everything else depends on this.

**Phase 2 — Stand up the rails.** Owner: `lemar`, with `samira` on setup capture. Open the
BlueNotary account and run the six-field Manual Session trial entry (the Option 1 fallback gate).
File the DORES platform notification naming BlueNotary. Open Stripe under his SSN as a sole prop.
Open the SoFi checking account and confirm Stripe pays out to it. Provision the Google Voice
number forwarding to his cell. Create and verify the Google Business Profile. Output: every
external account live and linked. Depends on: Phase 1.

**Phase 3 — Build the automation.** Owner: a new skill (see below), with `samira` running it.
One intake form as the single entry point, with a documented manual backup path for phone calls.
The Haven business mirror (no PII). The money-hub notary stream with the automatic tax set-aside
at log time. The two-line invoice template. The three alarms. Output: the loop runs unattended.
Depends on: Phase 2, because the mirror pulls from BlueNotary's export or API.

**Phase 4 — Soft launch.** Owner: `lemar`. First ten jobs at the published prices. Every one gets
walked end to end by hand to verify the chain: intake to calendar to act to journal to invoice to
payment to mirror to ledger. Output: a proven loop and a corrected one. Depends on: Phase 3.

**Phase 5 — Scale the front end.** Owner: `samira`. Booking site, directory listings, RON
promotion once the fee question is settled with DORES. Output: demand that fills the calendar.
Depends on: Phase 4.

## Risks
- **The journal is wrong and nobody notices for months.** Mitigation: the Phase 2 six-field trial
  entry, and the alarm for a completed calendar event with no journal entry.
- **Two journals by accident**, if a second tool ever starts keeping its own record. Mitigation:
  BlueNotary is the single journal by policy, written into the skill, and no second journal
  product gets adopted without re-checking 17:50-1.11.
- **Platform lock-in.** Switching means a new DORES notification and a journal migration.
  Mitigation: verify the six fields before the first act; export the journal on a schedule so
  the data is never only in the vendor.
- **Chargebacks on performed acts**, which cannot be undone. Mitigation: charge at the table on
  completion, not after; keep the two-line invoice so the disputed portion is identifiable.
- **Unauthorized practice of law**, the classic way a NJ notary loses a commission. Mitigation:
  the hard boundary below, written into the skill as a refusal, not a guideline.

## Blast radius
Real, and outside his control in three places: customer money moves through Stripe, signer PII
sits with a vendor under a 10-year retention duty, and a public brand carries his name and number.
The undo is uneven. A bad invoice is refundable. A bad journal entry is correctable only by the
journal's own amendment mechanism, never by editing history. A published profile and a filed DORES
notification are slow to unwind. Not a `reggie-compliance` gate: Reggie is Cuzzie's and Station
cannabis compliance, not NJ notary law.

## Automation map

**Runs unattended (Samira):** intake triage, calendar booking and confirmations within one
business day, quote generation at the published rates, two-line invoice issuance, Stripe payment
reconciliation, AR chasing via `chase-commitments`, the Haven business mirror, the money-hub
notary stream line, the automatic tax set-aside at log time, mileage capture from the intake
address, and all three alarms (completed event with no journal entry within N hours, invoice
unpaid past N days, job logged with no payment recorded).

**Needs Lemar, always:** the notarial act, the journal entry in the record, and any judgment about
whether an act may be performed.

**Hard boundary, written as a refusal:** Samira never decides whether a notarial act may be
performed, never advises which certificate a document needs, and never explains or drafts document
content. That is unauthorized practice of law.

**Sources of truth:** BlueNotary is the journal of record. Haven is the business record and holds
no signer PII. money-hub-ledger.md is the money record. Nothing gets a fourth.

## Ownership & upkeep
`samira` owns the loop after launch, running it on her existing hourly cadence, so there is no new
routine to maintain. Standing costs: BlueNotary (roughly $5 per session plus about $4 per signer,
or $297/year on Notary Pro), Stripe processing, and the five-year commission renewal with its
continuing-education course. Drift shows up through the three alarms; a silent stop shows up as a
month with journal entries and no ledger lines, which the monthly reconciliation catches.

## Skills to spec (Stormy Phase 4, not yet run)
- **`notary-intake`** — one intake point to calendar, quote, and job record.
- **`notary-journal-mirror`** — pulls BlueNotary's export or API into the Haven business mirror,
  posts the money-hub line and the tax set-aside, and raises the three alarms.

Both are net-new and both touch money and an outside party, so each earns the full six-question
spec when Phase 4 runs.

## Assumptions carried into this plan
- `Assumed:` no deadline, no `due`, launch gated on the commission (dimension 5).
- `Assumed:` money-hub remains the money home with notary as a new stream (his ask 4).
- `Assumed:` Haven remains the only source of truth for the business record, no new database.
- `Assumed:` BlueNotary's Manual Session captures all six NJ fields, pending the Phase 2 trial.

**Status → `active`. Next: Lemar confirms or revises this plan, then Stormy Phase 4 specs the two
skills, then the Phase 5 activation call (A / B / C / D).**

### Sources (this update)
- claude: Claude Code session, 2026-09-16, web research on BlueNotary IPEN and journal features
  and on NJ remote act fees

## Update 2026-09-16T09:37-04:00 — plan confirmed, Stormy Phase 4 skill specs

Lemar: "The plan stands for now" and spec both skills now. Noted that he overrode the
suggestion to hold `notary-journal-mirror` until after the Phase 2 platform trial; the spec
below absorbs that by making the data source pluggable rather than assuming one.

Roster checked (`.claude/skills/`): neither skill exists, and nothing on the roster covers this.
No duplicate risk.

---

## Skill spec — `notary-intake`

**1. What it does**
One intake point for every notary job. Takes a request, produces a priced, scheduled, recorded
job: a calendar event, a quote at the published rates, and a job record in Haven that every
later step reads from. Nothing about a job is ever keyed twice.

**2. Trigger and inputs**
- *Primary:* a submission on the public intake form.
- *Backup:* a plain drop in Convo 2 when a job arrives by phone, developed by Samira's PART 4
  sweep exactly like a money drop. (`Inherited` from ask 13's manual backup and ask 5's
  drop-it-in pattern.)
- Reads: the form or drop, Google Calendar for availability, the published rate card, and the
  Haven business record for a repeat client.

**3. Output and chaining**
- A Google Calendar event on the business calendar, routed per the `haven-calendar-sync`
  domain rules.
- A `type: task` job record written through `haven-capture`, carrying job type (in-person,
  IPEN, RON), act count, distance tier, quoted statutory fee, quoted travel or technology fee,
  and scheduled time. **No signer PII beyond a first name and contact handle.**
- A confirmation to the customer in Lemar's voice via `my-writing-style`.
- Hands off to `notary-journal-mirror` after the job, which matches the journal entry back to
  this record.

**4. Gates and owner**
- Owner: `samira`, on her existing hourly run. No new routine.
- Runs unattended: triage, availability check, quoting at published rates, booking, and the
  confirmation, all within one business day. (`Inherited` from asks 16 and 17.)
- Never: decides whether a notarial act may be performed, advises which certificate a document
  needs, or explains document content. Written as a refusal, not a guideline.
- Never: quotes off the rate card. An out-of-area or unusual request goes to Lemar as a card.

**Open asks for this skill**
A. Which form tool is the intake point: **Jotform** (already connected, so Samira can read
   submissions directly), a Google Form, or wait and build it into the Phase 5 booking site?
B. Deposit policy: payment at completion is the plan's chargeback mitigation, but a no-show on
   a 35-mile job costs the whole trip. Take a deposit on the top distance tier, or absorb it?
C. May Samira book an unfamiliar customer straight onto the calendar, or hold the slot and put
   a one-line card to Lemar first?

---

## Skill spec — `notary-journal-mirror`

**1. What it does**
Keeps the business record honest against the legal record. Pulls completed notarial acts from
BlueNotary, mirrors the non-PII business facts into Haven, posts the money to money-hub with
its tax set-aside, and raises an alarm the moment the two records disagree.

**2. Trigger and inputs**
- Runs on Samira's hourly scan.
- **Source is pluggable, decided at Phase 2, not now:** BlueNotary's API if the account exposes
  it, otherwise its journal CSV export. The skill reads through one adapter so the choice is a
  config line and not a rewrite. This is the direct consequence of the unverified-at-spec-time
  platform detail.
- Also reads: the `notary-intake` job records, Google Calendar completed events, and Stripe
  payment status.

**3. Output and chaining**
- The Haven business mirror: date, act type, act count, fee split, travel or technology fee,
  payment status, mileage. **Never a signer name, address, or credential detail.**
- A money-hub notary stream line through the `money-hub` skill, plus the automatic tax
  set-aside into the Set-Aside pocket at log time.
- A two-line invoice through Stripe, statutory fee and non-notarial fee itemized separately,
  as required to keep the journal's itemized fee entry accurate.
- Unpaid invoices handed to `chase-commitments`.
- Results landed through `samira-report-result`.
- **Three alarms**, per ask 18: a completed calendar event with no journal entry after N hours;
  an invoice unpaid past N days; a job logged with no payment recorded.
- A periodic journal export to durable storage, so the ten-year retention duty never depends
  on the vendor staying in business.

**4. Gates and owner**
- Owner: `samira`, on her existing hourly run.
- Runs unattended: the mirror, the ledger line, the set-aside, the invoice, the reconciliation,
  the chase, the alarms, the export.
- Never writes to the journal of record. BlueNotary is the legal record; this skill reads it and
  never edits it. A discrepancy raises an alarm for Lemar to correct in the journal himself,
  using the journal's own amendment mechanism.
- Never invents a number or a date. An unknown stays null and gets asked.

**Open asks for this skill**
D. Tax set-aside percentage. Ask 11 said yes to automatic, but never set the number.
E. Alarm thresholds: how many hours after a completed event before the missing-journal-entry
   alarm fires, and how many days before the unpaid-invoice alarm fires?
F. Reconciliation direction when a journal entry has no matching job record, which is what a
   true walk-up looks like: open a retroactive job record automatically, or raise it as a card?
G. Where the periodic journal export lands: Google Drive in an access-controlled folder, or
   somewhere else? It is the one artifact that carries signer PII outside the vendor.

---

Seven open asks across the two specs, all of them things the locked plan genuinely did not
settle. Everything else above is inherited from the plan or assumed and marked as such.
Next after these close: the Phase 5 activation call, A / B / C / D.

### Sources (this update)
- claude: Claude Code session, 2026-09-16

## Update 2026-09-16T10:48-04:00 — all seven spec asks closed; both specs are handoff-ready

### Answers
- **A Form tool** — **Jotform.** Already a connected surface, so Samira reads submissions directly
  with no scraping or polling layer to build.
- **B Deposit** — **none at first.** Lemar absorbs the no-show risk on the far tier. Revisit only
  if no-shows actually show up in the numbers.
- **C Booking autonomy** — **Samira books straight to the calendar**, including an unfamiliar
  customer. No hold-and-card step.
- **D Tax set-aside** — **30%**, applied automatically at log time into the money-hub Set-Aside
  pocket.
- **E Alarm thresholds** — missing journal entry fires **2 hours** after a completed calendar
  event. Unpaid invoice fires **1 week** out.
- **F Walk-up reconciliation** — a journal entry with no matching job record **cards Lemar**,
  never opens a retroactive record on its own.
- **G Journal export destination** — recommendation below, pending his call.

### Recommendation on G — where the journal export lands

This is the one artifact in the whole system that carries signer PII outside the vendor, so it
gets designed deliberately rather than dropped wherever is convenient.

**Recommendation:** a dedicated Google Drive folder, `Notary — Journal Exports`, owned by Lemar's
account, **sharing restricted to him alone, link sharing off**. It matches the pattern the rest of
his system already uses (timestamped snapshots in a purpose-built Drive folder, as with Money Hub,
Pulse, and Meeting Prep) so there is nothing new to learn or maintain.

Four rules that come with it:

1. **Monthly cadence**, aligned to the monthly reconciliation already in the plan. One timestamped
   file per export, never overwritten, in whatever format BlueNotary emits.
2. **This folder is never linked.** Every other surface in Lemar's system links back to its source
   — Pulse does it by design, #reports does it, the dashboards do it. This folder is the
   deliberate exception, because a link in a Slack message or a rendered dashboard is exactly the
   leak path. The skill writes the file and says nothing more than "export completed."
3. **Ten-year retention**, matching the journal duty under N.J.A.C. 17:50-1.11. Exports age out on
   a rolling ten-year basis, never sooner, and the folder is what makes the duty survivable if the
   vendor ever disappears.
4. **No encryption layer.** A zipped, password-protected archive sounds safer and is worse in
   practice: it defeats search, and a password he loses in year seven turns a compliance asset
   into a dead file. Drive access control restricted to one account is the right level here.

**Not researched, flag only:** NJ likely has rules on what happens to a journal if a commission is
resigned, revoked, or allowed to expire mid-term. That folder is the artifact those rules would
govern, and possibly the artifact an estate would need. Worth confirming with DORES before the
first renewal, not before launch.

### Spec amendments from these answers

`notary-intake`: trigger is a **Jotform submission**, Convo 2 drop remains the manual backup. No
deposit logic in v1. Samira books to the calendar unattended, within one business day.

`notary-journal-mirror`: **30% set-aside** at log time. Alarm thresholds **2 hours** and **1 week**.
An unmatched journal entry raises a card, and the skill never opens a retroactive job record. Export
destination per G once Lemar confirms.

Both specs now cover all four skill-creator points with no open questions except G's confirmation.

**Next: the Phase 5 activation call — A build-first, B parallel, C execute-now, or D park.**

### Sources (this update)
- claude: Claude Code session, 2026-09-16
