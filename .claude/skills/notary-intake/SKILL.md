---
name: notary-intake
description: >
  The single front door for every NJ notary job Lemar takes. Turns a request into a
  priced, scheduled, recorded job: a Google Calendar event, a two-line quote at the
  published rate card, and a job record in Haven that every later step reads from, so
  nothing about a job is ever keyed twice. Primary input is a Jotform submission;
  the documented backup is a plain drop in Lemar's self-DM (Convo 2) when a job comes
  in by phone, developed by Samira's PART 4 sweep exactly like a money drop. Runs
  inside Samira's hourly scan or on demand. Trigger on: a new notary Jotform
  submission, "notary booking", "new notary job", "book a signing", "quote a notary
  job", "someone called for a notary", "what do I charge for", "reschedule the
  signing", "notary intake". The job record carries NO signer PII beyond a first name
  and a contact handle — the legal journal is a separate system and this skill never
  touches it. This skill NEVER decides whether a notarial act may be performed, never
  advises which certificate a document needs, never explains or drafts document
  content (that is unauthorized practice of law and it is how a NJ notary loses a
  commission), never quotes off the rate card, never takes payment, and never invents
  a number or a date — an unknown stays null and gets asked.
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

## THE JOB RECORD

Written through `haven-capture`, never by hand. One job, one note, filed to the
notary-services project folder.

```yaml
domain: project
type: task
status: active        # → done once the act is performed and the mirror matches it
tags: [notary, job, in-person|ipen|ron]
source: slack         # or the form's own source
due: <scheduled time, ET offset>
```

Body carries: job type, act types and count, distance tier, quoted statutory fee, quoted
non-notarial fee, scheduled time, calendar event id, and a first name plus one contact
handle.

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

## SAFETY

You MAY: read Jotform submissions and Convo 2 drops; read the calendar and book, move, or
cancel a notary event; write and update job records through `haven-capture`; draft and
send a confirmation in Lemar's voice; raise Convo 1 cards; commit to `main`.

You MUST NOT, ever: decide whether an act may be performed, advise on a certificate, or
explain or draft document content; quote a price the rate card does not contain; quote a
RON technology fee before the DORES confirmation is recorded; take, request, or hold a
payment; write signer PII into the vault; touch the journal of record in any way; book
over an existing job; invent a distance, an act count, a time, or a name (unknown stays
`null` plus an ask); write a sibling record for a job that already has one.

## Returns (to the Samira runbook, for the digest)

`notary-intake ✓ <booked N · quoted N · rescheduled N · cards N>` — or `notary-intake —`
when the sweep found nothing.

## Worked example

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
