# The merge — the productivity loop meets the parent-company building

The handoff (`Handoff... Productivity Loop System design session`, 2026-08-27 16:25 ET)
asked the next thread to put the productivity-loop design next to Lemar's separate
organizational-infrastructure idea and work the merge: where the two overlap, which one
owns each layer, and what changes in `teams-tag-architecture.md` as a result. This file
is that answer. The visual companion is `org-infrastructure-map.html`.

## The building idea, as described

A parent company is the building. It houses every business except Cuzzie's: side
projects and anything Lemar starts. Each business is a room — a shared Project holding
everything about that business, its own account on the team plan with its own email
address, its own Slack channel with its own users and workflows, its own Drive and Docs
maintained on both the individual accounts and the main account. Samira sits at the
parent layer keeping the system healthy and portable — she keeps the lights on. Slack is
the comms fabric for people and agents alike. Claude Tag is the collaborative meeting
tool: go into the right channel and convene when something needs the group.

## The finding

**The two designs do not conflict. They answer different questions, and the plan reads as
tangled because one axis absorbed the other.**

The loop answers *who works*: people, and people carry seats. The building answers *what
the work is for*: businesses, and businesses are containers. Haven answers *where truth
lives*, and predates both.

The plan as described assumes a single stack — one business = one account = one project =
one channel = one folder = one team. Five of those six scale with the business. The
account does not: accounts scale with humans, because a human is what logs in, holds
credentials, gets billed, and can be held to an approval. Separating the two axes is the
whole reconciliation, and it is also the efficiency win: a new business becomes four
containers cut from a template, at zero marginal cost.

## Layer ownership (the handoff's actual question)

| Layer | Owned by | The rule |
|---|---|---|
| People | The loop | One seat per human. Two today. Tracks headcount, nothing else. |
| Businesses | The building | One room per business: Project + channel + Drive folder + vault folder. Zero accounts. |
| Source of truth | Neither — it predates both | Haven, unchanged. Rooms are folders in it; Drive/Slack/Calendar stay renderings. |
| Surfaces | The building | One workspace, one channel per room, one Drive tree per room, one naming convention across all three. |
| Scheduled jobs | The loop | One housekeeping job at the parent layer. A room never gets its own cron. |
| Collaboration | The loop | Tag, in the room's channel, convened for a question and closed with a note. |
| Money and legal | The building | Parent holds software + domain. Each room that takes money gets its own books. |

## Ten flaws, ordered by cost

1. **A business cannot hold a seat.** Seats are licensed to people. A business seat needs a
   human to log into it: shared credentials, no per-person attribution, no honest answer to
   "who approved this send," and cost that grows with ambition instead of headcount. It also
   blows past the two-seat org gate V1 is built around. *Fix: seats are people, Projects are
   businesses.* A shared Project already provides the folder, instructions, knowledge, and
   members.
2. **The building is rooted on an account with an end date.** Cuzzie's is excluded from the
   building and paying for it in the same breath — commingling on the one entity with
   regulators, a vendor wind-down, an IRS plan, and a license moving to another operator. And
   `lemar@cuzziesnj.com` winds down mid-2026, against the standing rule that nothing new gets
   built on it. *Fix: root the building on the durable neutral identity (`l.boonejr@gmail.com`
   today, the holdco domain later), per the same reasoning that already picked it as org owner.
   Cuzzie's is a tenant with its own books, or it is outside the building. Never the landlord.*
3. **Samira cannot be the admin, and this package already retired her.** An org owner is a
   human account with billing, recovery, and seat approval attached (which is why transfer is
   a support ticket). Separately, `teams-tag-architecture.md` retires Samira's machinery, so
   two live documents currently point opposite directions. *Fix: split the name from the job.
   Lemar is the landlord and holds the deed; "Samira" is the superintendent — a label for the
   housekeeping function, not the 15-part runbook, and not an owner.*
4. **An address is cheap, an account is expensive.** A business that receives mail needs an
   address, not a licensed Workspace user with a password, MFA, and a recovery path per room.
   *Fix: aliases and groups (`hello@room.holdco.com` → shared inbox) until a room has a
   customer who writes to it.*
5. **Agent-to-agent traffic in Slack is the most expensive line in the plan.** Channel work is
   metered, seat work is flat. Two agents exchanging state in a channel is marginal-cost spend
   with no human reading it, and with ambient mode on it can answer itself into a loop.
   *Fix: Slack is for humans, git is for machines. Agents hand off through the vault; an agent
   posts to a channel only when a human needs to see or act.*
6. **Rooms accumulate and nothing evicts them.** The anchors channel list is already the
   symptom (#comedy-club, #trading-cards, #free-books-partnership, #booking-agent,
   #delivery-in-a-box, #cuzzys-brand, #random-ideas — mostly quiet). *Fix: three tiers with a
   bar between each — an **idea** is a vault note and nothing else; a **room** opens when there
   is a counterparty or a date; a **business** gets an entity, address, and books when it takes
   money. Quiet for a quarter → dormant → archive → tombstone row (the existing PART F pattern).*
7. **Per-room workflows rebuild the runbook that was just retired.** If every room gets its own
   scheduled workflow, job count grows with rooms and the 15-part hourly loop reassembles under
   a new name, with the same watermarks, locks, and failure modes spread wider. *Fix: scheduled
   jobs live at the parent layer only. Rooms get habits and templates, not cron.*
8. **Files kept in two places are files kept in no place.** "Maintained on the individual
   accounts and the main account as well" is duplication — the same failure the voice-profile
   OneDrive copy already needed a tie-break rule for. *Fix: one owner per file, everyone else
   gets a link. Room folders owned by the building (Shared Drive once the domain exists);
   people get access, not copies. Offboarding stops being a recovery operation.*
9. **A meeting tool with no convening rule becomes a second inbox.** The Tag instinct and its
   economics are right; what is missing is how a session ends. *Fix: treat it like a real
   meeting — convened with a stated question, adjourned with a decision or an artifact, outcome
   filed as a Haven note. No question, no session. Anything that produces a thing moves to a seat.*
10. **Portability is asserted, never rehearsed.** `PORTABILITY.md` is strong but describes a
    restore nobody has performed, and the real fragility is the identity layer (connectors,
    triggers, bot apps) that standing rule 6 already says must be rebuilt rather than migrated.
    *Fix: put the drill in the janitor's job — monthly export, quarterly re-point one anchor and
    prove the loop still runs. Doctrine: the vault is portable, the plumbing is disposable and
    documented.*

## What the building idea got right (do not over-correct)

- **The metaphor for containers.** Room → Project + channel + folder maps cleanly. It fails only
  at identity, because rooms do not carry ID.
- **One comms fabric.** A single workspace matches the standing law that exactly one surface
  pings Lemar. Splitting per business would break it.
- **A parent layer owning health and portability.** Rarely built, and the reason the system
  survives an outage. It needs a human landlord above it, not a different design.
- **One vault under everything.** This is what makes multiple businesses viable at all — and the
  vault is *already* a building with rooms (`10-Personal`, `20-Cuzzies`, `30-Station`,
  `40-Projects`), which is why the analogy fit when Lemar reached for it.

## The room template (the efficiency payoff)

Opening a business is four containers from a template, ~10 minutes, zero marginal cost:

| Container | Example | Note |
|---|---|---|
| Vault folder | `41-licensing/` | Truth first, same as every capture. |
| Shared org Project | `41 · Licensing` | Instructions, knowledge, members. This is the room. |
| Slack channel | `#41-licensing` | Coordination only. Tag invited when the room is live. |
| Drive folder | `41 Licensing` | Owned by the building, not a person. Binaries only. |
| anchors row | four ids | The one place ids live. The room becomes addressable. |
| *Nothing else* | — | No seat, no mailbox until a customer writes, no cron, no connector, no bot. |

One room code, four surfaces, the same string in all of them — convention replaces the lookup
table, and anchors stops growing with every idea.

## Cost, at four rooms (PR #84's own ranges; estimates, not quotes)

| Line | As described | Reconciled |
|---|---|---|
| Human seats (2) | $120–150 | $120–150 |
| Business seats (4) | $80–100 | $0 |
| Mailboxes | $50–90 | $15–30 |
| Tag, capped | $50+ | $50 |
| **Total** | **$300–390** | **$185–230** |
| Room five | $27–47/mo | $0 |

Seat pricing carries the same uncertainty as gate **V1**, still unverified: confirm the seat
minimum on a two-seat org before paying. The meaningful row is the last one.

## Open calls (blocking, in order)

1. **The holdco name** — already blocks domain, email, website, socials (decisions D24). Under the
   building model it now also blocks every room's address scheme, lengthening the critical path.
   The unlock: *a holdco name does not need to be good.* Nobody markets a holdco. Pick a neutral
   one and let each room carry the brand that sells.
2. **Cuzzie's: tenant or outside the building** — it cannot be both excluded and paying. Then move
   the billing identity off the account that winds down mid-2026.
3. **Room numbering** — the vault uses 10/20/30/40 for domains and 50/60/70 for Reference, Legal,
   Automation. New businesses collide with that range. Nest rooms under `40-Projects` or renumber
   deliberately, once, before there are rooms to migrate.
4. **What earns a room** — write the bar down (counterparty, date, or money), or every idea becomes
   infrastructure.
5. **Where outsiders meet you** — per room: Slack Connect into the room's channel, or a shared Drive
   folder only. Private channels hide content, not the member directory.
6. **Which document wins on Samira** — amend `teams-tag-architecture.md` with the landlord /
   superintendent split so the next session does not relitigate it.

## Resulting changes to `teams-tag-architecture.md`

Recorded here rather than applied, because each is a call for Lemar (items 1–6 above):

- **§2** gains a fourth row: rooms as containers, and an explicit line that seats are per-human.
- **§3** gains two standing rules: *scheduled jobs live at the parent layer only*, and *Slack is for
  humans, git is for machines*.
- **§3 rule 5** (persona continuity) resolves into the landlord / superintendent split.
- **§4** cost controls gain the room template as the third lever (a room's marginal cost is zero).
- **§5 Phase 0** gains the durable-identity call (flaw 2) before any org is created.
- **§6** gains **V6 — restore drill**: re-point one anchor and prove the loop runs.
