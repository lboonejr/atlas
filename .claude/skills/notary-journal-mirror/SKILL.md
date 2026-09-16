---
name: notary-journal-mirror
description: >
  Keeps Lemar's notary business record honest against his legal record. Pulls completed
  notarial acts from the journal of record (BlueNotary), mirrors the non-PII business
  facts into Haven, posts the money-hub notary stream line with an automatic two-rate tax
  set-aside (fees for notarial acts are exempt from self-employment tax, travel fees are
  not), issues the two-line Stripe invoice, hands unpaid invoices to chase-commitments,
  logs declined notarizations that never reach the journal, raises the three alarms the
  moment the two records disagree, and exports the journal monthly against NJ's ten-year
  retention duty. Runs inside Samira's hourly scan or on demand. Trigger on: "run the
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

**Mode 2 — alarms.** Three checks, every sweep. Detailed below.

**Mode 3 — monthly export.** Detailed below.

**Mode 4 — reconciliation on demand.** "Did every signing get logged" — walk a date range
in both records and report every mismatch in both directions without changing anything.

**Mode 5 — refusal log.** Lemar declined to notarize. Record it. Detailed below.

## THE MIRROR ENTRY

Written through `haven-capture`, filed to the notary-services project folder. It carries:
date, act type, act count, medium, statutory fee, non-notarial fee, payment status,
mileage, the job record link, and the journal entry id.

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
wrong. Issue through Stripe, charged at completion rather than after, because a
notarization cannot be undone and a chargeback on a performed act has no clean remedy.

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

## THE THREE ALARMS

**1. Completed event, no journal entry — fires at 2 hours.** A notary calendar event has
passed and no journal entry matches it. Two hours is tight on purpose: the fix is Lemar
opening BlueNotary and entering the act while he still remembers the appointment. At two
weeks he is reconstructing, and a reconstructed journal entry is a worse entry.

**A logged refusal suppresses this alarm.** A declined notarization produces no journal
entry, because no act happened — so without the refusal log this alarm would cry wolf every
single time Lemar correctly turned a job away. Check Mode 5's refusal record before firing.
An alarm that punishes him for doing the right thing is an alarm he learns to ignore, and
then it is useless for the case it exists to catch.

**2. Invoice unpaid — fires at 1 week.** Hand to `chase-commitments` and card Lemar.

**3. Act logged, no payment recorded.** The journal says the work happened and no money
came in. Card it.

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
and send a two-line Stripe invoice; post money-hub ledger lines and the two-rate set-aside;
record refusals through `haven-capture`;
hand unpaid invoices to `chase-commitments`; raise Convo 1 cards; write timestamped
exports to the exports folder; commit to `main`.

You MUST NOT, ever: write to, edit, or amend the journal of record — it is the legal
record and only Lemar amends it, through the journal's own mechanism; decide whether an
act may be performed, advise on a certificate, or explain document content; open a
retroactive job record for an unmatched journal entry; write signer names, addresses, or
credential details into the vault; link the exports folder anywhere; overwrite or delete a
prior export; move money, or contact a customer about payment beyond the invoice and its
chase; collapse the two fee lines into one; apply a single blended set-aside rate across both
lines; characterize a signer's intent, capacity or honesty in a refusal record, or name a
signer in one beyond a first name; present a reserve figure as tax owed; invent a fee, a
date, an act count, or a payment (unknown stays `null` plus an ask); fabricate a run when no
source is configured.

## Returns (to the Samira runbook, for the digest)

`notary-mirror ✓ <acts N · invoiced $X · set-aside $Y (exempt $E / taxable $T) · refusals N ·
alarms N · unmatched N · export ✓/—>` — or `notary-mirror —` when the sweep found nothing.

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
