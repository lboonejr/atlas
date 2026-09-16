---
created: 2026-09-16T17:05-04:00
updated: 2026-09-16T17:05-04:00
domain: project
type: brief
status: active
tags: [notary, acquisition, signing-agent, real-estate, respa, blocked]
source: claude
---

# Notary B2B acquisition — the two tracks Google does not reach

Everything written about getting customers so far assumes one path: a person needs a
notary, searches Google, finds the Business Profile, calls. That path is real and it is
already planned for.

**It does not reach the two channels that pay the most.** Loan signings come from signing
services and title companies. Real estate work comes from agents who already have the
client. Neither of them will ever find Lemar on Google Maps, because neither of them looks
there.

This note is the plan for the two of them. It is the piece the scope change flagged as
unspecced.

## Why this matters more than it sounds

The consumer channel has a ceiling. A person needs a notary maybe twice in their life, so
every consumer job starts from zero and has to be won again.

A signing service that likes Lemar sends work every week. An agent who trusts him sends
their clients for years. **Both channels are relationships rather than transactions** — the
first job is hard and the twentieth is automatic. That is the whole reason to do the work
of getting in.

It also cuts both ways. A relationship takes months to build and one bad job to lose. That
is why the standing advice is still to run the first ten *consumer* jobs by hand first: to
make the cheap mistakes where they are cheap.

---

# TRACK 1 — Signing services and title companies

## The vendor packet — build it once, send it fifty times

Every signing service asks for **the same four things** at registration. Assembling them
each time is wasted effort, so they get built once, kept in one Drive folder, and sent as
a set.

| Item | What it is | Where it comes from | Cost |
|---|---|---|---|
| **W-9** | The tax form saying who to pay and under what tax number | Lemar fills it out; the name on it must match the entity he actually registers | free |
| **E&O certificate** | Proof of the errors-and-omissions insurance policy — the paper, not just the policy | The insurer, once the $100,000 policy is bought | policy cost |
| **Background screening result** | A current background check, normally NNA-branded or Sterling | The screening vendor, renewed yearly | ~$60–100/yr |
| **Certification certificate** | Proof of passing a signing agent exam | NNA or an equivalent, renewed yearly | in the NNA package |

Add to the same folder, because platforms ask for them next: a copy of the **commission
certificate**, a **photo of the seal impression**, and the **trade name or LLC filing**.

**One folder, and it is not the journal exports folder.** These are business credentials
with no signer PII in them, so they may be linked and shared freely — the opposite of the
export folder rule. Keeping them apart is deliberate.

**The name on the W-9 is a dependency, not a detail.** It has to match the entity that is
actually registered. That is the LLC decision, and it is why the decision genuinely moved
to now: fixing the name on file at a dozen platforms later is worse than deciding once.

## Certification and screening — start the queue early

**NNA packages start at $199.** The exam is 45 questions and needs 80% to pass. The
background screening repeats every year.

**None of it is legally required in New Jersey.** In practice almost nobody hires an
uncertified signing agent, because the signing service's own contract with the lender
requires screened notaries. So it is optional the way a driving licence is optional.

**Treat it like the Google verification queue: a waiting line, entered early.** Certification
can be studied for and taken while the commission is still in processing. The screening is
a turnaround time nobody controls. Both belong in the wait that is already happening, not
stacked on top of commission day.

**Sequence:** study and pass the certification exam during the commission wait → order the
background screening → buy E&O → assemble the packet → register with platforms. Registration
is last because the platforms ask for the earlier items.

## Which platforms to register with

Not researched yet — this is the honest state. **No platform has been evaluated and this is
the next real piece of work on this track.** What is known going in:

- Registration is normally free. A platform charging a meaningful fee to join is the first
  thing to be suspicious of.
- **Volume and pay rate are the two things to compare**, and they trade off. A platform with
  constant work at $75 a signing is a different business from one with occasional work at
  $150.
- **Payment reliability matters more than rate.** A $150 signing from a company that pays in
  90 days, or argues, is worse than a $100 signing that lands on day 30.
- Direct **title company** relationships pay better than platforms because nobody is taking a
  cut, but they are earned after a track record exists, usually from being the notary a
  platform kept sending and a title company noticed.

**A new company's first job is a credit decision, not a scheduling decision.** `notary-intake`
already cards it rather than booking it unattended. Confirm any new company against notary
community feedback before the first job, and keep the first one small.

---

# TRACK 2 — Real estate agents

This is the new track. It is not a smaller version of track 1 — it works differently, pays
differently, and carries a legal rule that track 1 does not.

## What an agent actually brings

An agent does not hire a notary for the closing itself; the title company handles that. What
they bring is **everything around the closing that has to be notarized and nobody planned
for**:

- **A seller who cannot make the closing.** Deed, affidavit of title, and a power of attorney,
  signed early or signed remotely.
- **An out-of-state buyer or seller.** Exactly the case RON was built for — Lemar's own remote
  session at his own rate, no platform taking a cut.
- **Cash deals and investor clients.** No lender, often no title company doing the legwork; the
  deed and affidavits still need a notary and somebody has to arrange it.
- **Estate and family sales.** Powers of attorney, executor paperwork, affidavits of heirship.
- **Property managers and landlords.** Leases and landlord affidavits, repeating monthly.
- **The brokerage's own paperwork.** Independent contractor agreements, commission disbursement
  authorizations.

The pattern underneath all of it: **an agent has a deal about to close and one signature in the
way.** They are not price-shopping. They need someone who answers and shows up. That is the
whole pitch, and it is the same pitch that wins urgent consumer work — which is why the
2-hour response promise serves both channels at once.

## The two shapes, and they are different jobs

**Shape A — the referral.** The agent hands over their client. **The client pays**, at the
normal rate card, like any consumer job. The agent is recorded as the referral source and
that is all. This will be the large majority.

**Shape B — retained.** The brokerage is the customer and gets invoiced on net-15. Their own
paperwork, or a standing arrangement to cover their office.

`notary-intake` Mode 6 handles both, and the job record keeps `referring_agent` and
`brokerage` so Lemar can see which relationships actually produce work.

## THE RULE THAT GOVERNS THIS WHOLE TRACK — RESPA Section 8

**Read this before contacting a single agent.**

Section 8 of the federal Real Estate Settlement Procedures Act (12 U.S.C. §2607) makes it
illegal to give or accept **anything of value** in exchange for referring business connected
to a federally related mortgage loan. Notarizing a deed or a mortgage document is a settlement
service. An agent referring that work is precisely the arrangement the law is about.

**In plain terms: Lemar can never pay an agent for sending him a client.** Not a fee per job,
not a percentage, not a gift card, not dinner traded for referrals, not "your clients get 20%
off," not a cut of anything.

**The penalty is criminal** — up to $10,000 and a year in prison per violation, plus treble
damages to the consumer — and it applies to **both sides**, so an agent who proposes it is
proposing a crime for both of them. Agents sometimes propose it casually because arrangements
like this are common in their world, so it will probably come up, and the answer is a polite
no.

**What is allowed, and it is genuinely enough to win this channel:**

- Answering the phone, being available evenings and weekends, showing up when a closing is
  about to fall apart. Agents refer whoever makes them look good to their client.
- Business cards and a one-page rate sheet left at an office. Ordinary marketing, nominal
  value, not tied to any referral.
- Doing a good job on the first one.
- **Being able to do RON**, which solves the out-of-state seller problem an agent hits
  regularly and most notaries cannot help with.

**Co-marketing is the grey area** — splitting the cost of a flyer or an event is only safe when
each side pays its own fair share of the real cost. That is not a Samira decision. It goes to
Lemar with the RESPA point attached, and if it is going anywhere it goes to a lawyer first.

**Separately, and just as absolute:** Lemar can never notarize in a transaction he has an
interest in. A deal he is a party to, or one where he is paid on the outcome, voids the act
under NJ law.

## How to actually get the first agent

Not by advertising. By being useful to a small number of people.

1. **Start with agents Lemar already knows.** One honest conversation beats fifty cold emails:
   *"I'm a notary now — if you ever have a seller who can't make closing or a client out of
   state, call me."*
2. **The one-page leave-behind.** Name and "Notary Public, State of New Jersey," the Google
   Voice number, the service area, "Mobile · Remote (RON)," the response promise, and the rate
   card. It goes on a desk and stays there. It is marketing, not an inducement, and it never
   offers the agent anything.
3. **Brokerage offices are where several agents sit in one room.** Sales meetings are the
   standard way in — worth asking to be introduced rather than walking in cold.
4. **Title companies and real estate attorneys are adjacent and worth the same conversation.**
   An estate attorney with an out-of-state client is a natural RON referral.
5. **Every agent who sends one client gets an entity note** in the vault, so the relationship
   is visible rather than remembered. Two referrals from the same agent is a relationship worth
   maintaining; Lemar should be able to see that without trying to recall it.

**What to promise, since it is the only thing being offered:** a two-hour response, evening and
weekend availability, mobile across the service area, remote for out-of-state signers, and
never guessing at a document. That is the offer. It costs nothing and it is legal.

---

## Open questions on both tracks

- **Which signing service platforms.** Nothing evaluated yet. The next real work item here.
- **The entity name for the W-9.** Blocked on the LLC decision, which blocks platform
  registration.
- **NNA versus an equivalent certification.** Only NNA pricing has been checked ($199+).
- **Whether any NJ title company relationships are reachable through people Lemar already
  knows.** Not explored.
- **RON pricing for agent-referred out-of-state signers** is still gated on the DORES answer
  about whether NJ caps a remote act separately.

## What this depends on

Everything here waits on the commission, except the parts that are deliberately queue-jumping:
certification study, the background screening, and the first conversations with agents Lemar
already knows. Those three can start now.

Nothing on either track may be *sold* before the commission exists. Telling an agent "call me
when you need a notary" while the commission is in processing is fine and honest. Taking the
booking is not.

## Sources
- claude: Claude Code session, 2026-09-16 — picks up the scope-change delta in
  `2026-09-15-notary-business-backend-systems.md` (Update 2026-09-16T15:10-04:00), items 4
  and 5, and adds the real estate agent track Lemar asked for in the same session.
- Not legal advice. The RESPA question is worth a short call with a real estate attorney
  before any arrangement with an agent goes beyond ordinary marketing.
