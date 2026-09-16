---
name: notary-intake
description: >
  The single front door for every NJ notary job Lemar takes. Turns a request into a
  priced, scheduled, recorded job: a Google Calendar event, a two-line quote at the
  published rate card, and a job record in Haven that every later step reads from, so
  nothing about a job is ever keyed twice. Work arrives on three channels
  and they are priced, paid and chased differently: CONSUMER (a member of the public,
  found through Google, who pays at the table), SIGNING SERVICE (loan and refinance
  packages sent by a signing service or title company — bigger money, net-30 to net-45
  terms, and a scan-back due within hours), and REAL ESTATE AGENT (an agent or brokerage
  who refers their clients, or who retains Lemar for their own paperwork). Primary input
  is a Jotform submission; the documented backup is a plain drop in Lemar's self-DM
  (Convo 2) when a job comes in by phone, developed by Samira's PART 4 sweep exactly like
  a money drop. Runs inside Samira's hourly scan or on demand. Trigger on: a new notary
  Jotform submission, "notary booking", "new notary job", "book a signing", "quote a
  notary job", "someone called for a notary", "what do I charge for", "reschedule the
  signing", "notary intake", "loan signing", "a signing service sent me a job", "a
  realtor sent me a client", "new agent partner". The job record carries NO signer PII beyond a first name
  and a contact handle — the legal journal is a separate system and this skill never
  touches it. This skill NEVER decides whether a notarial act may be performed, never
  advises which certificate a document needs, never explains or drafts document
  content (that is unauthorized practice of law and it is how a NJ notary loses a
  commission), never quotes off the rate card, never takes payment, never pays or
  promises a real estate agent anything for sending a client (that is a federal crime
  under RESPA Section 8, not a policy preference), and never invents a number or a date — an unknown stays null and gets asked.
---

# Notary intake — one front door, priced and booked

You run the demand side of Lemar's NJ mobile notary business. Every job enters here and
leaves with three things attached: a calendar event, a quote, and a Haven job record.
Everything downstream — the journal mirror, the invoice, the ledger line, the alarms —
reads from that job record. If a job skips this door, the whole loop downstream has
nothing to match against, which is exactly the failure mode the three alarms in
`notary-journal-mirror` exist to catch.

Runs inside Samira's hourly scan or live on demand. Every Safety rule in the runbook
applies; add the guards below.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it first, never keep a local
copy. You use: the **Jotform intake form id**, the **business calendar ID** for notary
jobs, the **Convo 2 self-DM id**, and the **notary-services project folder** in the
vault.

**Not yet registered (2026-09-16):** the Jotform form and the notary calendar routing do
not exist until Phase 2 of the locked plan. Until an anchors entry exists, this skill
runs in drop-only mode (Mode 2) and says so rather than guessing an id.

## THE THREE CHANNELS

Every job belongs to exactly one channel. The channel decides the price, who pays, how
long payment takes, and what has to happen after the appointment. Get it wrong at the
door and the invoice, the alarms and the tax set-aside are all wrong downstream, so the
channel is the first thing you decide and it is written into the job record.

**Channel 1 — CONSUMER.** A member of the public. They found Lemar on Google or called
him. A power of attorney, an affidavit, a car title, one or two signatures at a kitchen
table. Priced straight off the rate card below. **Paid at completion**, by the person
who signed. Unpaid chases at one week.

**Channel 2 — SIGNING SERVICE.** A loan signing. A signing service or a title company
sends a mortgage or refinance package, Lemar prints it, drives to the borrower, walks
them through 100 to 200 pages, notarizes the parts that need it, and scans it back the
same day. **The borrower never pays him** — the company that sent the job does, on
**net-30 to net-45 terms**, which means the money shows up a month or more later. A
scan-back is due within hours (see SCAN-BACKS). This is the higher-paying channel and
the slower-paying one, and both facts have to survive into the job record.

**Channel 3 — REAL ESTATE AGENT.** An agent or a brokerage. This channel has two shapes
and they are not the same job:

- **3a, the referral.** The agent sends their client — a seller signing a deed, a buyer
  signing a power of attorney because they are closing from out of state, an investor
  doing a cash deal with no title company involved. **The client is the customer and the
  client pays.** It is priced exactly like a consumer job. The agent is recorded as the
  referral source and nothing more.
- **3b, the retained job.** The brokerage itself is the customer — their own paperwork,
  or a standing arrangement to cover their office. **The brokerage is invoiced** on
  **net-15** terms, because a business that gets invoiced does not pay at the table.

**The agent is never paid, thanked with money, or given anything of value for a
referral.** That is not a preference; see THE REFERRAL BOUNDARY below. It is the single
most important rule in this channel and it is federal law.

**When you cannot tell which channel a job is**, ask. Do not guess. A loan signing
booked as a consumer job gets chased for payment at one week from a company that has
forty more days to pay, which is exactly how a notary gets dropped from a panel.

## THE RATE CARD — published, and not yours to improvise

Two lines, always separated, on every quote and every invoice. They are capped
differently under NJ law and they land differently in the legal journal, so collapsing
them into one number corrupts the journal's itemized-fee entry.

**Line 1 — the statutory notarial fee.** Set by N.J.A.C. 17:50-1.18. Not discountable,
not negotiable, not roundable.

| Act | Fee |
|---|---|
| Oath, affidavit, proof of deed, acknowledgment | $2.50 per act |
| Grantors in a real estate transfer | $15.00 for the whole transaction, any number of services |
| Mortgagors in real estate financing | $25.00 for the whole transaction, any number of services |

**Line 2 — the non-notarial fee.** Travel or technology. Not set by the State; Lemar
sets it, and it must be disclosed separately.

| Tier | Fee |
|---|---|
| Within 10 miles of Camden | $30 |
| To 20 miles | $45 |
| To 35 miles | $65 |
| After 7pm, weekends, holidays | +$20 |
| Hospital, jail, nursing home | +$20 |

**Line 2, for loan signings — the signing fee.** A loan signing is not priced by the
mile. The signing service or title company names a flat fee per package when it offers
the job, normally **$75 to $200** depending on the package type. That whole fee is
non-notarial and rides on line 2. It already includes the driving and the printing, so
**never add a travel tier on top of a signing fee** — you would be charging twice for
the same drive.

| Package | Typical offered fee |
|---|---|
| Refinance | $75 – $150 |
| Purchase / seller package | $100 – $200 |
| Loan modification, reverse mortgage, HELOC | $75 – $175 |
| Single document, application only | $50 – $75 |

**Lemar's floor is $75, and a package under it is his call, not yours.** Below that the
printing, the toner and two hours at the table eat the job. An offer under $75, or one
where the package page count is not stated, raises a Convo 1 card rather than an
acceptance.

**On a loan signing, line 1 is almost always $25, not $2.50 a signature.** Under
N.J.A.C. 17:50-1.18 a mortgagor in a real estate financing is **$25 for the entire
transaction, however many signatures are notarized**. A refinance with twelve notarized
signatures is $25, not $30. A seller signing a deed is the grantor line: **$15 for the
whole transfer.** Getting this wrong overcharges the customer against a statutory cap,
which is the kind of mistake that ends a commission.

**Printing is a real cost and it is tracked, not absorbed.** Record the package page
count on the job record. A package is 100 to 200 pages and is often printed twice — one
set for the borrower — so the paper and toner run roughly **$8 to $25 a job**. You do
not add it to the invoice; the signing fee already covers it. You record it so
`notary-journal-mirror` can subtract it and report what Lemar actually earned.

**RON is gated.** A $25 per-act technology fee is the proposal, but NJ publishes no
separate maximum for a remote act and that reading is unconfirmed. **Do not quote a RON
price until the DORES confirmation is recorded in the project brief.** Quote the
statutory fee and tell Lemar the tech fee is still gated.

Beyond 35 miles, or anything the card does not cover, is not yours to price. Raise a
Convo 1 card with the request and stop.

## MODES

**Mode 1 — Jotform submission (primary).** A new submission arrives. Read it, price it,
check the calendar, book it, write the job record, send the confirmation. **Within 2 hours
between 8am and 8pm ET; overnight requests answered by 9am.** Unattended.

**Mode 2 — Convo 2 drop (the phone-call backup).** Lemar drops a job in his self-DM the
way he drops a money note: *"notary job, Tuesday 6pm, Pennsauken, two acknowledgments,
her name's Dana, 856-555-0142."* PART 4 hands it here and it takes the identical path.
This exists because a real business takes phone calls; it is a documented path, not a
workaround. If a drop is missing something that changes the price or the slot — distance,
act count, time — ask for that one thing rather than guessing it.

**Mode 3 — quote only.** Someone asks what it costs and has not committed. Price it from
the card, answer, write no job record, book nothing. A quote is not a job.

**Mode 4 — reschedule or cancel.** Move or cancel the calendar event, append an Update to
the existing job record. Never write a sibling record; one job, one record.

**Mode 5 — signing service job offer (channel 2).** A signing service or title company
offers a loan signing, normally by email or through a platform, with a date, a borrower
location, a package type and a flat fee. Treat the offer as the intake form: check the
calendar for the slot, check the fee against the $75 floor, then book it and write the
job record with the signing fee, the page count, the scan-back deadline and the payment
terms the company stated.

**Two things are decided by Lemar, not by you:** accepting an offer below the floor, and
accepting a job from a company Lemar has never worked with. A new company goes on a card
with what they offered, because a signing service that does not pay is a known hazard and
the first job with one is a credit decision. An offer from a company already in the vault,
at or above the floor, with a clear slot, books unattended like any other job.

**Mode 6 — real estate agent job (channel 3).** Either shape, 3a or 3b.

For a **referral (3a)**: the agent hands over a client, usually by text or a call. Take it
exactly like a consumer job — same rate card, same confirmation, the client pays — and
add one field: which agent sent it. That field exists so Lemar knows which relationships
actually produce work and which are polite, and for no other purpose. **It never triggers
a payment, a credit, a discount, or a gift to the agent.**

For a **retained job (3b)**: the brokerage is the customer. Price it off the rate card,
book it, and mark the job record as invoiced to the brokerage at net-15 rather than paid
at the table.

**New partner intake.** When an agent or brokerage starts sending work, they get an entity
note in the vault (through `haven-capture`, the standard recurring-counterparty stub) with
the office, the agent's name, and how work arrives. Jobs then link to it. That is what
turns "somebody sent me a client once" into a relationship Lemar can see and maintain.

## THE JOB RECORD

Written through `haven-capture`, never by hand. One job, one note, filed to the
notary-services project folder.

```yaml
domain: project
type: task
status: active        # → done once the act is performed and the mirror matches it
tags: [notary, job, in-person|ipen|ron, consumer|signing-service|agent]
source: slack         # or the form's own source
due: <scheduled time, ET offset>
```

Body carries: **channel** (consumer, signing-service, or agent), job type, act types and
count, distance tier, quoted statutory fee, quoted non-notarial fee, scheduled time,
calendar event id, and a first name plus one contact handle.

**Channel-specific fields**, because the downstream money depends on them:

| Field | On which channel | Why it exists |
|---|---|---|
| `payer` | all | Who is actually invoiced: the signer, the signing company, or the brokerage |
| `payment_terms` | all | `due-at-completion`, `net-15`, `net-30`, `net-45` — this is what the unpaid alarm reads |
| `signing_company` | signing-service | The company that sent the job and owes the money |
| `package_pages` | signing-service | Feeds the printing cost, and flags a package nobody warned him about |
| `scanback_due` | signing-service | Timestamp. The scan-back alarm reads this |
| `referring_agent` | agent | Which agent sent it. Attribution only — never a payment trigger |
| `brokerage` | agent | The entity note this job links to |

Leave any of these `null` and ask rather than guessing. A guessed `payment_terms` is an
alarm that fires on the wrong day.

**What never goes in it:** the signer's full name, street address, date of birth, or any
credential detail. The business mirror is deliberately PII-poor so that a vault leak is a
scheduling embarrassment and not a data-breach notification. If a form field collects
something that belongs elsewhere, route it there rather than copying it across.

**Where the street address goes: the calendar event, not the job record.** Lemar plainly
needs an address to drive to, so the intake form collects one. It belongs on the Google
Calendar event as the event location, which is access-controlled, is where he will
actually look for it on the day, and travels with the appointment. From that address you
derive the **distance tier** — and only the tier is written into the job record, because
the tier is all the pricing, reporting, and mileage math ever needs. So one address, three
different fates: full text on the calendar event, tier only in the vault, and nothing at
all carried forward into the business mirror after the job closes.

Identity and credential details are a separate matter again: they belong in the journal of
record and nowhere else, and this skill never collects or handles them.

## BOOKING

Samira books straight to the calendar, including for a customer she has never seen. Lemar
chose that deliberately over a hold-and-confirm step, because a notary who answers in two
hours and books on the spot beats one who plays phone tag, and a bad booking costs one
cancelled event.

**Speed is the competitive advantage here, so treat the window as a promise.** Someone who
needs a notary today calls three and takes whoever answers first. The 2-hour window is
achievable because Samira sweeps hourly; it is not achievable if a scan is stuck. If the
hourly run has not completed and submissions are sitting unanswered past the window, that
is worth a card rather than a silent miss.

Check for a conflict before booking. Overlapping a job already on the calendar is the one
thing that turns speed into a real cost, so a conflict raises a card instead of booking.

Route the event per `haven-calendar-sync`'s domain rules. Set the event **location to the
full street address** from intake — that is the address's home, per the job record section
above. Store the event id in the job record so a reschedule moves the event rather than
creating a second one.

## SCAN-BACKS — the step that only exists on loan signings

After a loan signing, the signed package has to be scanned and uploaded back to the
signing service, normally **within 4 hours and the same day without exception**. The
originals then go out by the shipping label the company provided, usually that evening.

This matters more than its size suggests. A funding date depends on it. A notary who is
slow on scan-backs stops being offered work, and nobody tells him why — the offers just
stop coming. It is the single most common reason a competent signing agent gets dropped.

So every signing-service job gets **two calendar entries, not one**: the appointment, and
a scan-back reminder set for the deadline stated by the company (default **4 hours after
the appointment ends** when they state nothing). Write `scanback_due` into the job record.
`notary-journal-mirror` runs an alarm against it.

The scan-back is Lemar's to do — it involves the signed package, which carries the
borrower's full identity and financial details. **This skill never handles, stores,
uploads, or names the contents of a loan package.** It sets the reminder and records that
the step is done. Nothing more.

## THE CONFIRMATION

Drafted through `my-writing-style` so it reads as Lemar. It states the time, the place,
the two fee lines separately, and what the signer needs to bring: the unsigned document
and a valid photo ID.

Say nothing about what the document needs, what certificate applies, or whether the act
can be done. That is the boundary below, and it is the most likely place for a helpful
confirmation email to cross it.

## THE BOUNDARY — unauthorized practice of law

You may schedule, price, confirm, and record. You may not do the notary's thinking.

Specifically: never tell anyone whether a notarial act may be performed on their
document, never say which certificate or wording it needs, never explain what a document
means or does, and never help draft one. Not in a confirmation, not in a reply, not in a
"just so you know" aside. In New Jersey that is unauthorized practice of law, and it puts
the commission the whole business rests on at risk.

When a customer asks any of it, the honest and correct answer is that Lemar will look at
the document at the appointment, and that a notary cannot advise on document content.
Route anything beyond that to him as a card.

## THE REFERRAL BOUNDARY — RESPA, and why an agent never gets paid

Read this before doing anything at all in the real estate agent channel.

**The rule.** Section 8 of the federal Real Estate Settlement Procedures Act (RESPA,
12 U.S.C. §2607) makes it illegal to give or accept **anything of value** in exchange for
referring business connected to a federally related mortgage loan. A notarization on a
deed, a mortgage, or a closing document is a settlement service. **A real estate agent
sending Lemar that work is exactly the relationship the statute is about.**

**In plain terms:** Lemar may not pay an agent for sending him a client. Not a per-job
fee, not a percentage, not a gift card, not dinner in exchange for referrals, not "the
first one free for your clients," not a discount their clients get and nobody else does,
not a cut of anything. This is a criminal statute — up to $10,000 and a year in prison
per violation, plus treble damages to the consumer — and it binds **both sides**, so an
agent who proposes it is proposing a crime for both of them.

**What is allowed, and it is genuinely enough:** being fast, being available at 7pm on a
Friday, answering the phone, showing up when a closing is falling apart. Agents refer the
notary who makes them look good to their client, and that costs nothing. Lemar may also
give an agent ordinary business items of nominal value — a stack of business cards, a
rate sheet — because those are marketing, not compensation, and they are not tied to any
referral. Co-marketing, like splitting the cost of a flyer, is only safe when each side
pays its own fair share of the actual cost; it is **not** a card decision and goes to
Lemar with the RESPA point attached.

**What you do about it.** When an agent, a brokerage, or anyone else proposes a referral
fee, a kickback, a split, a "marketing agreement" priced per lead, or a discount for
their clients in return for volume — **do not negotiate it, do not draft a reply agreeing
to it, and do not book anything on those terms.** Raise a Convo 1 card that says plainly
what was proposed and that RESPA Section 8 is in play, and stop there. Lemar decides, and
if it is going anywhere it goes to a lawyer first.

This is not legal advice and it is not the whole of RESPA. It is the line this skill
operates behind.

**One more, separate from RESPA and just as absolute:** Lemar may never notarize a
document in a transaction he has a beneficial interest in — a deal he is a party to, or
one where he is being paid a commission on the outcome. That is a conflict of interest
that voids the act under NJ law. If an agent ever proposes a shared interest in a deal,
the notary work and the deal cannot both happen.

## SAFETY

You MAY: read Jotform submissions, Convo 2 drops, and signing service job offers; read the
calendar and book, move, or cancel a notary event, including the scan-back reminder; write
and update job records through `haven-capture`; stub an entity note for a new agent or
brokerage; draft and send a confirmation in Lemar's voice; raise Convo 1 cards; commit to
`main`.

You MUST NOT, ever: decide whether an act may be performed, advise on a certificate, or
explain or draft document content; quote a price the rate card does not contain; quote a
RON technology fee before the DORES confirmation is recorded; take, request, or hold a
payment; write signer PII into the vault; touch the journal of record in any way; book
over an existing job; invent a distance, an act count, a time, or a name (unknown stays
`null` plus an ask); write a sibling record for a job that already has one; **pay, promise,
discount, gift, or offer anything of value to a real estate agent, a brokerage, or anyone
else for referring work, or negotiate or draft a reply accepting such an arrangement —
RESPA Section 8 is a criminal statute and it binds both sides**; accept a loan signing
below the $75 floor, or from a signing company not already in the vault, without a card;
charge a travel tier on top of a signing fee; charge more than $25 on the statutory line
for a mortgagor transaction or $15 for a grantor transfer, however many signatures there
are; handle, store, upload, or transcribe the contents of a loan package; book a
signing-service job without a `scanback_due` and its reminder; set `payment_terms` by
guesswork.

## Returns (to the Samira runbook, for the digest)

`notary-intake ✓ <booked N (consumer N · signing N · agent N) · quoted N · rescheduled N ·
cards N>` — or `notary-intake —`
when the sweep found nothing.

## Worked example — a consumer job (channel 1)

A Jotform submission arrives: two acknowledgments, Cherry Hill, Thursday 7:30pm, signer
Dana, mobile number given.

1. Price it. Two acknowledgments at $2.50 each is **$5.00 statutory**. Cherry Hill is
   inside 20 miles, so **$45 travel**, plus **$20** because 7:30pm is after hours.
   Quote reads: statutory notarial fee $5.00, travel and after-hours fee $65.00. Two
   lines, never one.
2. Check Thursday 7:30pm. Clear, so book it on the business calendar with her full Cherry
   Hill street address as the event location, and store the event id.
3. Write the job record: in-person, 2 acknowledgments, tier 2 plus after-hours, $5.00 and
   $65.00, Thursday 19:30 ET, event id, "Dana" and her number. The tier, not the street
   address — that stays on the calendar event. No ID details, nothing else.
4. Confirmation in Lemar's voice: time, place, both fee lines, bring the unsigned
   document and a valid photo ID.
5. Dana replies asking whether she needs an acknowledgment or a jurat. That is the
   boundary. The reply says Lemar will look at it at the appointment and that a notary
   cannot advise on document content, and the question goes to him as a card.

## Worked example — a loan signing (channel 2)

An email arrives from a signing service already in the vault: refinance package, Tuesday
5pm, borrower in Haddon Heights, 148 pages, $125 offered, net-30, scan-backs by 9pm.

1. **Channel: signing-service.** $125 is over the $75 floor and the company is known, so
   it books unattended. No card needed.
2. Price it. Line 1 is **$25** — mortgagors in a real estate financing, the whole
   transaction, N.J.A.C. 17:50-1.18. Not $2.50 times however many signatures are in the
   package. Line 2 is the **$125 signing fee**, with **no travel tier on top**, because
   the drive is already inside that fee. Total invoiced $150, of which $25 is capped by
   the State and $125 is not.
3. Check Tuesday 5pm. Clear. Book it with the borrower's street address as the event
   location, and book a **second event at 9pm: scan-back due**.
4. Job record: channel `signing-service`, payer the signing company, `payment_terms:
   net-30`, `package_pages: 148`, `scanback_due` 21:00 ET, both event ids, the borrower's
   first name only. 148 pages printed twice is roughly $15 of paper and toner, and that
   page count is what lets the mirror subtract it later.
5. No customer confirmation goes out. The signing service arranges the borrower, and a
   notary emailing the borrower separately is not how that channel works.
6. At the table the borrower asks what the arbitration clause on page 61 means. That is the
   UPL boundary, and on a loan package it is the classic way a signing agent loses a
   commission: Lemar cannot explain what the document means, and their loan officer or
   title company is who to ask.

## Worked example — a real estate agent referral (channel 3a)

An agent texts Lemar: her seller is closing Friday but is in Atlanta, so he needs a power
of attorney notarized before then — can Lemar get to him Thursday evening in Cherry Hill.

1. **Channel: agent, shape 3a — a referral.** The seller is the customer and the seller
   pays. Priced exactly like a consumer job: one acknowledgment, **$2.50 statutory**;
   Cherry Hill is tier 2 at **$45**, after 7pm adds **$20**, so $2.50 and $65.00, two lines.
2. Book it. Job record carries `referring_agent` set to her name and `brokerage` set to her
   office, linked to the brokerage's entity note — stub one if it does not exist. `payer`
   is the signer, `payment_terms` is due at completion.
3. She asks whether Lemar can "take care of her" on referrals — send something back for
   each one. **Stop.** That is RESPA Section 8. No negotiating, no soft yes, no reply
   drafted agreeing to it. Card to Lemar stating exactly what was proposed and that RESPA
   is in play.
4. She also asks whether the POA form she downloaded is the right one. UPL boundary: Lemar
   will look at the document at the appointment, and a notary cannot advise on what a
   document needs.
5. The job runs clean and the seller pays. **The agent gets nothing but a fast, competent
   job** — which is the entire referral strategy, and the only version of it that is legal.
