---
created: 2026-09-15T16:09-04:00
updated: 2026-09-16T08:49-04:00
domain: project
type: brief
status: awaiting-decision
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
