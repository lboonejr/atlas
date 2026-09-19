---
created: 2026-09-19T00:00:00-04:00
updated: 2026-09-19T00:00:00-04:00
domain: project
type: decision
status: active
tags: [notary, pain-points, operations, workstation, differentiation]
source: claude
---

# Where the notary business will hurt, and what got built about it

Nothing is live yet — no exam, no LLC, no jobs — so none of this comes from experience.
It comes from two places: walking the eight-step loop on paper, and reading what working
notaries actually complain about online. Then everything got ranked by **how often it
happens per job**, not by how big it sounds.

Related: [[2026-09-18-notary-workstation-dashboard]] (the page and its rules),
[[2026-09-15-notary-business-backend-systems]] (the locked plan),
[[2026-09-20-notary-exam-day-checkpoint]] (the open items and queues).

## The short version

Seven pain points. Six of them now have something on the page that catches them.

| # | The pain | How often | Built? |
|---|---|---|---|
| 1 | The wasted trip — bad ID, missing signer, blank document | every job is at risk | Confirm sheet + a text you can send |
| 2 | Miles driven never written down, so the deduction is lost | every job | miles counter + a mileage line on Money |
| 3 | Signing companies that pay slow or never pay | every loan job | company scorecard + a warning before you accept |
| 4 | Calls that never turn into jobs, and no idea why | more often than jobs | "Didn't happen" sheet + a close rate |
| 5 | Money spent printing before you are paid | every loan job | Printed button, cost shown on the row |
| 6 | The price argument at the table | most consumer jobs | a script you can read or paste |
| 7 | Typing the journal twice (BlueNotary + here) | every job | not fixed — it is the law, see below |

## The seven, with the reasoning

### 1. The wasted trip is the most expensive thing that can happen

**The plain point:** you drive 20 minutes, and the job dies at the table. You earned
nothing, or just the travel fee, and you burned an hour.

The reasons it dies are always the same short list, and every one of them is knowable
on the phone before you leave:

- their photo ID is expired, or the name on it does not match the document
- a second signer is not going to be there
- the document has blank spaces in it
- they already signed it before you arrived
- they think the whole thing costs $2.50

Working notaries handle this by confirming the appointment and stating a cancellation
policy up front — some charge $100 for a no-show or an unprepared signer, with a
four-hour notice rule.

**What got built:** a **Confirm** button on every booked job. It opens six tap-checks
you run down while you have them on the phone. It also puts a ready-to-send text on your
clipboard — what to have out, who needs to be there, what it costs, and that the travel
fee stands if nobody is home. The job then shows a green "confirmed" chip. Any job inside
24 hours that has not been confirmed raises an alarm on Today. There is also a **No-show**
button that closes the job keeping the travel fee, so a wasted trip is still recorded
income instead of a hole.

### 2. Every mile you drive is money you are throwing away unrecorded

**The plain point:** the IRS lets you deduct a set amount for every business mile you
drive. At roughly 70 cents a mile, a 24-mile round trip to Cherry Hill is about **$17 off
your taxable income** — on a job that might only bill $32.50. Nobody reconstructs that in
April from memory.

The page tracked the travel *tier* ($30 / $45 / $65) but never the actual miles, so the
deduction did not exist anywhere.

**What got built:** a miles counter in the job sheet and the refusal sheet, stepping by 5,
that pre-fills from the travel tier you tapped. The Money tab now shows total miles and
the estimated deduction, and miles are a column in the tax export. It is labelled an
estimate and a deduction — never income.

### 3. Getting paid is the loan channel's whole problem

**The plain point:** signing services pay you 30 to 45 days after the job. Some pay late.
Some do not pay at all. This is the single loudest complaint in the notary trade, and the
advice is always the same: check the company before you accept, get the terms in writing,
and keep your own record of who pays and how fast.

Warning signs from other notaries: "we pay when escrow closes", net-60 terms, any company
that wants money from you up front.

**What got built:** a **Who pays, and how fast** table on the Money tab, built from your
own jobs — per company: how many jobs, how much billed, how much still owed, and the
average number of days they actually took to pay. Two taps mark a company **Slow** or
**Do not work for**, and that flag then shows as a red line in the job sheet the next time
that company's name comes up, *before* you save the job. The company is a chip now, not a
typed field, so the name is spelled the same way every time and the table does not split
into three versions of the same company.

### 4. The calls you lose tell you more than the jobs you win

**The plain point:** most people call two or three notaries and hire whoever answers first
and sounds sure. If you lose those calls and never write down why, you cannot tell whether
your problem is your price, your hours, or that your phone went to voicemail.

**What got built:** the dock's middle button is now **Didn't happen**, and it asks one
question first — *why?* Two paths:

- **I turned it down** — the same six stop-path reasons as before, saved exactly as it was
  (a job with `refused: true`, travel fee kept if you made the trip). Nothing about the
  refusal log changed.
- **They didn't book me** — price, timing, I missed the call, they went elsewhere, or it
  was just a question. Saved as a lead, not a job, so it never touches the money or the
  journal alarms.

Marketing now shows the close rate — jobs booked against calls that came in — and the
lost reasons ranked. If "I missed the call" is the top reason, answering the phone is worth
more than any marketing spend. If it is "price", that is a different conversation.

### 5. You pay to print before anyone pays you

**The plain point:** a 150-page loan package printed twice is about **$16.50** of paper
and toner, plus 20 minutes at the printer, spent 30 to 45 days before the money arrives.
And the scan-back — the copy the company needs back — has a four-hour clock on it.

**What got built:** a **Printed** button on a loan job. The row then shows the cost as
already spent and the time you spent it. The scan-back countdown got louder: the hours
remaining show on Today, not just the Jobs tab. If a job dies after you printed it, the
record shows the print cost was real.

### 6. The $2.50 argument, settled before it starts

**The plain point:** New Jersey caps the notary fee at $2.50 per act — one of the lowest
in the country — so someone who googled it will tell you your $32.50 is a rip-off. It
is not: $2.50 is the State's fee for the act, and the rest is your travel and your time,
which the State does not cap.

**What got built:** a short script on the Money tab, just above the rate card, with a Copy
button. Three sentences you can read at the table or paste into a text.

### 7. The journal really does get typed twice, and that stays

BlueNotary is the legal record: six fields, the signer's real details, and it is the one a
court would subpoena. The Workstation is the business record: no signer details beyond a
first name. They are deliberately separate systems, so the entry happens twice at the
table. The page cannot fix this and should not try — what it does is take the BlueNotary
entry number in one field and then alarm loudly if a completed job has no number against
it.

## What sets the business apart, weighed

Ranked by what a customer would actually notice, and what it costs to do:

1. **Answering the phone, evenings and weekends.** Costs nothing. It is the single most
   common reason people pick one notary over another, and the lost-lead log will prove it
   within a month.
2. **Confirming the appointment before driving out.** Costs one phone call. Nobody else
   does it, and it is the difference between a customer who is ready and one who wastes
   both your afternoons.
3. **Same-day scan-backs on loan work.** Costs nothing but discipline. Slow scan-backs are
   how a signing agent quietly stops getting offered work.
4. **Remote signings for out-of-state sellers.** Needs a platform whose identity check
   satisfies the two-types route in section 19d(1). Real money, and most local notaries
   cannot do it.
5. **The first ten customers are already inside Cuzzie's and The Station.** Staff
   paperwork, I-9s, vendor affidavits, POAs. Free, warm, and they generate the first
   Google reviews.

## What is deliberately not built

- **No link to Google Calendar.** A job booked on the page still does not ring the phone.
  That is a design call, not a bug, and it is still open.
- **No sweep back into Haven.** A job typed on the page lives only on the page until
  Samira's PART 4 sweep learns to read the store. Still open.
- **No invoicing.** The page tells you who owes what and when it is late. Sending the
  invoice is the journal-mirror skill's job.
- **The mileage rate is a page constant.** Confirm the current year's figure with a CPA
  each January. The 20% / 35% set-aside is still a reserve policy, not a tax calculation.

## Sources read

Notary trade forums and trade press on signing-service non-payment and how to vet a
company (Notary Stars, Notary Cafe, Professional Notary Services); 2026 mobile-notary
business write-ups on rising costs and the admin load (JKC Mobile Notary, QuoteIQ,
NotaryStyle); appointment-confirmation and no-show practice (Closewise, SignDocsToday,
24-Hour Mobile Notary); New Jersey fee cap and remote notarization rules (NJ Treasury
notary law page, Docusign and eNotaryOnCall New Jersey guides, Kulzer & DiPadova).
