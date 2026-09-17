---
name: notary-journal-mirror
description: >
  Keeps Lemar's notary business record honest against his legal record. Pulls completed
  notarial acts from the journal of record (BlueNotary), mirrors the non-PII business
  facts into Haven, posts the money-hub notary stream line with an automatic two-rate tax
  set-aside (fees for notarial acts are exempt from self-employment tax, travel and signing
  fees are not) net of the paper and toner a loan package actually costs, issues the
  two-line invoice to whoever the job's channel says owes it, chases it on that channel's
  own terms (at completion for consumer work, net-15 for a brokerage, net-30 to net-45 for
  a signing service) instead of one global one-week rule, watches the scan-back clock on
  every loan signing, hands unpaid invoices to chase-commitments,
  logs declined notarizations that never reach the journal, asks for a Google review once a
  job closes cleanly and is paid, raises the four alarms the moment the two records
  disagree, and exports the journal monthly against NJ's ten-year retention duty. Runs inside Samira's hourly scan or on demand. Trigger on: "run the
  journal mirror", "reconcile the notary journal", "did every signing get logged",
  "notary money", "export the notary journal", "what did I make notarizing", "notary
  reconciliation", "had to turn one down", "I refused a notarization", or a
  completed notary calendar event. This skill READS the journal of record and NEVER
  writes to it — BlueNotary is the legal record and only Lemar amends it, through the
  journal's own amendment mechanism. It never decides whether an act may be performed,
  never advises on a certificate, never explains document content, never moves money or
  contacts a customer about payment beyond the invoice and its chase, and never invents
  a number or a date — an unknown stays null and gets asked.
---

# Notary journal mirror — the legal record checked against the business record

Two records exist and they must agree. **BlueNotary is the journal of record**, the
tamper-evident electronic journal NJ requires under N.J.A.C. 17:50-1.11. **Haven is the
business mirror**, PII-poor, holding what the business needs to bill, report, and prove
it did the work. This skill is the loop between them: it reads the legal record, writes
the business record, moves the money, and shouts when the two drift apart.

It exists because the failure mode is silent. A signing that never reaches the journal
looks exactly like a slow week until an audit or a title company asks, and by then it is
years old. The alarms below are the whole point of the skill; the bookkeeping is the
part that pays for itself.

Runs inside Samira's hourly scan or live on demand. Every Safety rule in the runbook
applies; add the guards below.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — read it first, never keep a local
copy. You use: the **BlueNotary source config** (see below), the **Stripe account**, the
**notary-services project folder**, the **money-hub ledger note**, the **business
calendar ID**, and the **`Notary — Journal Exports` Drive folder id**.

**Not yet registered (2026-09-16):** none of these notary anchors exist until Phase 2 of
the locked plan. Until an anchors entry exists, this skill reports that it has no source
configured and stops. It never guesses an id and never fabricates a run.

## THE SOURCE IS PLUGGABLE

BlueNotary is the journal of record, but how you read it was deliberately left open: the
account's API if it exposes one, otherwise the journal CSV export. That choice belongs to
Phase 2, when the account actually exists and someone can look.

So read through one adapter, configured in anchors as `notary_journal_source: api |
export`. Everything downstream works off the same normalized act record either way, and
switching costs a config line rather than a rewrite. Do not scatter source-specific
assumptions through the rest of the skill.

A normalized act carries: act timestamp, act type, act count, medium (in-person, IPEN,
RON), the itemized fees recorded in the journal, and the journal entry id.

## MODES

**Mode 1 — sweep (the hourly default).** Pull acts completed since the last run. For
each: match it to a job record, write the mirror entry, issue the invoice, post the
ledger line and the set-aside. Then run the alarms.

**Mode 2 — alarms.** Four checks, every sweep. Detailed below.

**Mode 3 — monthly export.** Detailed below.

**Mode 4 — reconciliation on demand.** "Did every signing get logged" — walk a date range
in both records and report every mismatch in both directions without changing anything.

**Mode 5 — refusal log.** Lemar declined to notarize. Record it. Detailed below.

**Mode 6 — review request.** A paid job closed cleanly. Ask for the Google review. Detailed
below.

## THE MIRROR ENTRY

Written through `haven-capture`, filed to the notary-services project folder. It carries:
date, act type, act count, medium, **channel** (consumer, signing-service, or agent),
statutory fee, non-notarial fee, **printing cost**, **net after costs**, payment status,
payment terms, due date, mileage, the job record link, and the journal entry id.

**Channel comes from the job record and is never inferred from the fee.** A $125 line
could be a loan signing or an unusually long consumer job, and everything below — who is
invoiced, when the chase starts, whether a review may be asked for — hangs off the channel
rather than the amount.

**It never carries a signer's name, address, or credential detail.** That is not a
preference, it is the design: the journal of record already holds that data under a
ten-year duty and a vendor's access controls, and copying it into a git repo would put
signer PII somewhere it can never fully be deleted. When the source hands you those
fields, drop them.

Mileage comes from the job record's distance tier, so the deduction is captured without
anyone keeping a mileage log by hand.

## THE MONEY

**The two-line invoice.** Statutory notarial fee and non-notarial fee, itemized
separately, always. They are capped differently under NJ law and the journal records an
itemized list of fees charged, so a collapsed single-line invoice makes the legal record
wrong.

**Who gets the invoice, and when the money is due, is decided by the channel — not by
habit.** Read `payer` and `payment_terms` off the job record.

| Channel | Who is invoiced | Terms | Charged |
|---|---|---|---|
| Consumer | the signer | due at completion | Stripe, at the table |
| Agent — referral (3a) | the signer | due at completion | Stripe, at the table |
| Agent — retained (3b) | the brokerage | net-15 | Stripe invoice, emailed |
| Signing service | the signing company or title company | net-30 to net-45, as that company states | their portal or an invoice they request |

For consumer and referral work, charge at completion rather than after: a notarization
cannot be undone and a chargeback on a performed act has no clean remedy.

**A signing service is the opposite case and you do not get to argue with it.** They pay
on their own schedule, through their own system, a month or more later. Record the stated
terms and the resulting due date on the mirror entry at log time. If the company stated no
terms, record `net-30` and card Lemar to confirm — never leave it blank, because a blank
term is what makes alarm 2 fire on the wrong day.

**Never invoice a borrower on a signing-service job.** The borrower is not the customer and
does not owe Lemar anything. Doing it once is the kind of error that ends a panel
relationship.

**The ledger line.** Post to the money-hub notary stream through the `money-hub` skill.
Notary income is a stream inside the existing personal ledger, not a second money system.

**The set-aside — two rates, because the two lines are taxed differently.** Reserve into the
money-hub Set-Aside pocket at log time, automatically. Doing it at log time rather than at
quarter-end is the entire value: the money is reserved before it feels like spendable income.

| Invoice line | Reserve | Why |
|---|---|---|
| Statutory notarial fee | **20%** | Income tax only |
| Non-notarial fee (travel, after-hours, facility, RON technology) | **35%** | Income tax **plus** self-employment tax |

Fees for performing notarial acts are **exempt from self-employment tax** under IRC
§1402(c)(1) and Reg. §1.1402(c)-2(b). Fees for travel, printing, document handling,
administrative work and loan-signing services are **not** — those carry the full 15.3% on top
of income tax. So the two-line invoice is not only a fee-cap rule and a journal-accuracy rule,
it is also the substantiation the exclusion requires. A single blended rate either
over-reserves the exempt line or under-reserves the taxable one.

**Treat the RON technology fee as non-notarial** and reserve it at 35%. It is a convenience
charge for the platform, not a fee for performing the act, so it sits with travel rather than
with the statutory fee. Revisit only if a tax professional says otherwise.

### Cost of goods — the printing, and why ignoring it lies to him

Consumer work has almost no materials cost. A loan signing does: a package is 100 to 200
pages and is usually printed twice, once for the borrower, on both letter and legal paper.
That is roughly **$8 to $25 of paper and toner every time**, and it comes out of Lemar's
pocket before he is paid.

Right now nothing in the system knows that exists, so a $150 signing looks like $150 of
income. It is not. **Record the printing cost on every signing-service job** and post it to
the money-hub notary stream as a cost line against that job.

Estimate it from `package_pages` on the job record when no receipt figure exists:

| Input | Figure |
|---|---|
| Pages printed | `package_pages` × 2 (borrower copy), unless the job record says single-set |
| Cost per page | **$0.055** — about 3.5¢ of toner and 2¢ of paper, blended letter and legal |
| Label it | `estimated` when derived this way, `actual` when it comes from a real receipt |

**Always mark an estimate as an estimate.** A guessed number that looks like a measured one
is worse than no number, because at tax time nobody can tell which is which. Real toner and
paper receipts, when Lemar drops them, replace the estimate on the job and correct the
running total.

**Costs reduce net income, not the set-aside rate.** Keep reserving at 20% and 35% on the
gross invoice lines. Over-reserving is a conservative error that leaves money in the pocket;
under-reserving is a bill in April he did not plan for. The printing cost is a deductible
business expense, tracked so the deduction is claimable and so "what did I actually make on
loan signings" has a true answer. **Never present gross signing fees as earnings once a
printing cost exists on the job** — report the net beside it.

The same applies to the one-time equipment: when the printer is bought, record it as a
notary business asset with its price and date, because it is deductible and because nobody
remembers a purchase date two years later.

**Track the annual split.** Carry a running exempt-versus-non-exempt total for the tax year.
The exemption is claimed by writing "Exempt—Notary" and the amount on Schedule SE, so that
figure has to be producible on demand rather than reconstructed from a year of invoices.

These two rates are a **reserve policy, not a tax calculation.** The right income-tax
percentage depends on Lemar's total household income and his marginal bracket, which this
skill does not know. Flag for a CPA to confirm before the first filing, and never present the
reserve as the amount owed.

Deposits land in the dedicated SoFi checking account, kept distinct from the Set-Aside
pocket so reconciliation stays legible.

**Unpaid invoices** hand to `chase-commitments` once the alarm below fires.

## THE FOUR ALARMS

**1. Completed event, no journal entry — fires at 2 hours.** A notary calendar event has
passed and no journal entry matches it. Two hours is tight on purpose: the fix is Lemar
opening BlueNotary and entering the act while he still remembers the appointment. At two
weeks he is reconstructing, and a reconstructed journal entry is a worse entry.

**A logged refusal suppresses this alarm.** A declined notarization produces no journal
entry, because no act happened — so without the refusal log this alarm would cry wolf every
single time Lemar correctly turned a job away. Check Mode 5's refusal record before firing.
An alarm that punishes him for doing the right thing is an alarm he learns to ignore, and
then it is useless for the case it exists to catch.

**2. Invoice unpaid — fires on the job's own terms, never a global week.** A single
one-week rule was correct when every customer paid at the table. It is wrong now: it would
fire on **every single loan signing**, because signing services pay on net-30 to net-45,
and an alarm that fires on healthy jobs is an alarm that gets ignored on the sick one.

Read `payment_terms` off the job record and fire when the due date passes:

| Terms | Alarm fires |
|---|---|
| `due-at-completion` (consumer, agent referral) | 7 days after the act |
| `net-15` (brokerage) | day 16 |
| `net-30` / `net-45` (signing service) | day 31 / day 46 |

Then hand to `chase-commitments` and card Lemar. **Missing terms are not a reason to skip
the check** — treat a blank as net-30 and say in the card that the terms were never
recorded, because an invoice nobody is watching is how a $150 job silently becomes a
write-off.

**Track signing companies that run late, and say so.** When the same company crosses its
own stated terms more than once, put that in the card. A signing service that pays late
twice is information about whether to take the third job, and it is the only early warning
Lemar gets before a company stops paying altogether.

**3. Act logged, no payment recorded.** The journal says the work happened and no money
came in. Card it. On a signing-service job, read this against the terms too — money that is
not due yet is not money that is missing.

**4. Scan-back overdue — fires at the deadline, signing-service jobs only.** The job record
carries `scanback_due`. When that time passes and the job is not marked scanned, card Lemar
**immediately**, not on the next quiet sweep.

This alarm is about keeping the work, not the money. A signing service tracks scan-back
speed, and a notary who is slow stops being offered jobs without ever being told why. The
package is also sitting in his car with a stranger's full financial life in it until it
ships, which is its own reason not to let the evening slide.

The card says which signing, when it was due, and how late. It never names or describes
anything inside the package.

Alarms surface as Convo 1 cards. An alarm never fixes anything itself, because every fix
lives in a record this skill is not allowed to write.

## THE REFUSAL LOG (Mode 5)

A notary is sometimes obliged to say no: the signer cannot be satisfactorily identified,
appears coerced or does not understand what they are signing, is not present, the document is
incomplete or has blank spaces, or the act would be something the commission does not cover.
Declining correctly is the job working, not the job failing.

**A refusal is not a notarial act, so it never enters the journal of record** — which means
that without this log it leaves no trace anywhere. That is the gap this closes. Recording
date, time and reason is the standard protection everywhere in the profession: it is the
evidence of reasonable care if a complaint, a commission inquiry, or a lawsuit ever arrives,
and the moment it is most needed is years later, when memory is worthless.

**How it arrives.** Lemar drops it in Convo 2 the way he drops a money note: *"had to turn one
down today, lady in Bellmawr, her ID expired last month."* PART 4 hands it here.

**What gets recorded**, through `haven-capture`, filed to the notary-services project folder
as `type: log`:
- date and time
- how the job arrived (job record link where one exists)
- act that was requested
- **the reason, in Lemar's own words** — do not summarize it into a category, because the
  specific fact is what has evidentiary value later
- whether a travel fee was still charged, and what was invoiced if so

**No signer PII beyond a first name**, exactly as everywhere else in this skill. "Her ID was
expired" is the record; her name and licence number are not.

**Never characterize the signer's intent.** Record what was observed and what Lemar decided,
not a conclusion about fraud or capacity. "Signer could not produce unexpired ID" is a fact.
"Signer was attempting fraud" is an accusation sitting in a file that may one day be read by
the person it names.

**A travel fee is still earned on a refusal** when he made the trip. Invoice it as a
non-notarial line, reserve it at 35%, and note it on the refusal record — there is no
statutory fee line, because no act was performed.

## THE REVIEW REQUEST (Mode 6)

Reviews are the compounding asset of a local service business. They are roughly a fifth of
Google's local ranking weight, and **recency counts for more than volume** — three reviews
this month beat twelve from two years ago. A steady per-job trickle is therefore worth more
than a launch-day burst, which is exactly what asking automatically produces.

**When.** Same day as the act, a few hours after payment clears, while the relief is fresh
and before the day blurs. Not at the table — Lemar is packing up and it is an awkward ask in
person. Not a week later, when they have forgotten who he was.

**Where.** To the single contact handle already on the job record. A text lands far better
than an email for this, so prefer the phone handle when intake captured one.

**What.** Two or three sentences through `my-writing-style`, in Lemar's voice, with the
Google review short link and nothing else. No attachments, no second ask, no marketing.

**Only consumer and agent-referral jobs are eligible, and this is a new restriction.**

- **Consumer (channel 1):** ask. They chose Lemar and their review is what feeds the next
  customer.
- **Agent referral (3a):** ask the client, who is the customer and who signed. Never ask the
  agent — the agent is not the customer, and a review request pointed at a referral source
  reads as pressure on the relationship.
- **Signing service (channel 2): never ask anyone.** The borrower did not hire Lemar, did
  not pay him, and often did not choose him. Asking a stranger mid-refinance to review the
  notary who showed up at their house is at best odd and at worst a complaint to the signing
  service. There is no version of this that is worth a review.
- **Brokerage retained (3b):** never automatically. A standing business relationship is
  Lemar's to ask in his own words if he wants to. Card it, do not send it.

**Gate it on a clean close.** Send only when the act is in the journal, the invoice is paid,
and no alarm fired on the job. Asking someone to praise you while you are still chasing their
invoice is the fastest way to earn the review you deserve rather than the one you want.

### The never-clauses, and these are compliance, not taste

- **Never offer anything for a review.** No discount, no credit, no free act. Incentivised
  reviews violate Google's policies and the FTC's rules on endorsements, and the penalty
  lands on the profile the whole business depends on.
- **Never gate or filter.** Do not ask "how did it go?" and route only the happy answers to
  Google. Review gating is explicitly prohibited and is grounds for removal.
- **Never ask twice for the same job**, and never ask the same person more than once a
  quarter even across different jobs. A repeat customer who keeps getting asked stops being
  a repeat customer.
- **Never ask after a refusal.** He turned them away; that is not a review invitation.
- **Never ask when the invoice is unpaid or the payment failed.**
- **Never mention a rating, a star count, or what to say.** Ask for the review, not the
  verdict.
- **Never chase it.** One ask, then silence. `chase-commitments` handles invoices, never
  reviews.

**Blocked until the Business Profile exists.** The ask needs the Google review short link,
which does not exist until the profile is live and verified — which is itself gated on the
Trade Name Certificate. Until that anchor is registered, this mode reports that it has no
review link configured and sends nothing. It never improvises a link.

## THE UNMATCHED JOURNAL ENTRY

A journal entry with no matching job record is what a genuine walk-up looks like: someone
caught Lemar in person, he did the act, and no intake ever happened.

**Card him. Never open a retroactive job record on your own.** The temptation is to
quietly synthesize the missing record so the numbers tie out, and that is exactly wrong —
a fabricated job record is indistinguishable from a real one a year later, and it would
paper over the signal that the intake door is being bypassed. Card it, let him confirm
what happened, and write the record from his answer.

## THE MONTHLY EXPORT

Once a month, aligned to the monthly reconciliation, export the journal and write it to
the `Notary — Journal Exports` Drive folder: one timestamped file, never overwriting a
prior export, retained on a rolling ten-year basis to match the retention duty under
N.J.A.C. 17:50-1.11.

**This folder is never linked.** Not from Pulse, not from a #reports line, not from a
Convo 1 card, not from a dashboard. Every other surface in Lemar's system links back to
its source by design, and this is the one deliberate exception, because this export is
the only artifact in the system carrying signer PII outside the vendor and a link is the
leak path. Report `export ✓` and the count. Say where it went once, in the vault, and
never render a clickable path to it.

The export is also the insurance: if the vendor disappears, the ten-year duty still has
to be met, and this folder is what meets it.

## SAFETY

You MAY: read the journal of record; write mirror entries through `haven-capture`; issue
and send a two-line invoice to the payer the job record names, on that channel's terms;
post money-hub ledger lines, cost-of-goods lines, and the two-rate set-aside;
record refusals through `haven-capture`; send one review request per cleanly closed job;
hand unpaid invoices to `chase-commitments`; raise Convo 1 cards; write timestamped
exports to the exports folder; commit to `main`.

You MUST NOT, ever: write to, edit, or amend the journal of record — it is the legal
record and only Lemar amends it, through the journal's own mechanism; decide whether an
act may be performed, advise on a certificate, or explain document content; open a
retroactive job record for an unmatched journal entry; write signer names, addresses, or
credential details into the vault; link the exports folder anywhere; overwrite or delete a
prior export; move money, or contact a customer about payment beyond the invoice and its
chase; collapse the two fee lines into one; apply a single blended set-aside rate across both
lines; invoice a borrower on a signing-service job, or any payer other than the one the job
record names; fire the unpaid alarm on a global one-week rule instead of the job's own
terms; report gross signing fees as earnings when a printing cost exists on the job;
present an estimated printing cost as a measured one; ask for a review on a
signing-service job, or ask a referring agent for one, or send a brokerage review request
automatically; let a scan-back deadline pass without a card; name or describe the contents
of a loan package anywhere; characterize a signer's intent, capacity or honesty in a refusal record, or name a
signer in one beyond a first name; offer anything of value for a review, filter or gate who
gets asked, ask twice for one job, ask at all on a refused or unpaid job, or chase a review; present a reserve figure as tax owed; invent a fee, a
date, an act count, or a payment (unknown stays `null` plus an ask); fabricate a run when no
source is configured.

## Returns (to the Samira runbook, for the digest)

`notary-mirror ✓ <acts N (consumer N · signing N · agent N) · invoiced $X · costs $C · net
$N · set-aside $Y (exempt $E / taxable $T) · refusals N · reviews asked N · alarms N
(scan-back N) · unmatched N · export ✓/—>` — or `notary-mirror —` when the sweep found nothing.

## Worked example

Hourly sweep. The source returns one act completed 3 hours ago: two acknowledgments,
in-person, journal entry id `BN-4471`, fees recorded $5.00 and $65.00.

1. Match it to Thursday's job record for Dana. Match found on time and act count.
2. Write the mirror entry: date, 2 acknowledgments, in-person, $5.00 statutory, $65.00
   travel and after-hours, unpaid, 14 miles from the tier, links to the job record and to
   `BN-4471`. No name, no address, no ID details.
3. Issue the Stripe invoice, two lines: statutory notarial fee $5.00, travel and
   after-hours fee $65.00.
4. Post $70.00 to the money-hub notary stream and reserve **two rates, not one**: $1.00 on
   the $5.00 statutory line (20%, income tax only) and $22.75 on the $65.00 travel line (35%,
   income tax plus self-employment tax). $23.75 total to Set-Aside. Add $5.00 to the year's
   exempt running total and $65.00 to the non-exempt total.
5. Alarms: the event has a matching entry, so alarm 1 is clear. The invoice is minutes
   old, so alarm 2 is not due. Payment is pending, not missing, so alarm 3 is clear.
6. Flip the job record to `done`.

Same sweep, second finding: journal entry `BN-4472`, one oath, $2.50, no job record
anywhere. That is a walk-up. Card Lemar asking what it was, and write nothing until he
answers.

## Worked example — a loan signing through the mirror

Same refinance from the `notary-intake` example: journal entry `BN-5012`, Tuesday 5pm,
148-page package, $25 statutory and $125 signing fee, net-30, sent by a signing service.

1. Match it to the job record. Channel is `signing-service`, so everything below follows
   that channel and not the consumer default.
2. Mirror entry: date, mortgagor acknowledgments, in-person, channel `signing-service`,
   $25 statutory, $125 signing fee, **printing $16.28 estimated** (148 pages × 2 × $0.055),
   **net $133.72**, payment terms net-30, due 30 days out, mileage from the tier, links to
   the job record and `BN-5012`. No borrower name, no address, nothing about what the loan
   is.
3. Invoice **the signing company**, not the borrower, through their process. Two lines,
   still separated: statutory $25.00, signing fee $125.00.
4. Post to the money-hub notary stream: $150.00 income and a **$16.28 cost line** against
   the same job. Reserve $5.00 on the statutory line (20%) and $43.75 on the signing fee
   (35%) — $48.75 to Set-Aside, computed on the gross, not the net. Add $25.00 to the year's
   exempt total and $125.00 to the non-exempt total.
5. Alarms. Entry matched, so alarm 1 is clear. **Alarm 2 is not due for 30 days**, which is
   the whole point of the change — the old one-week rule would have fired on a perfectly
   healthy job. Payment pending on terms, so alarm 3 is clear. **Alarm 4 is live**: the
   scan-back is due at 9pm, so if the job is not marked scanned by then, Lemar gets a card
   that evening.
6. **No review request.** Signing-service jobs never get one.
7. Flip the job record to `done` once the scan-back is marked and the act is mirrored —
   payment stays open on its own clock.
