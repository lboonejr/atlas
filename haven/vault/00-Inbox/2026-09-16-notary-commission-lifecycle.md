---
created: 2026-09-16T11:48-04:00
updated: 2026-09-16T11:48-04:00
domain: project
type: task
status: active
tags: [notary, commission, renewal, admin, blocked]
source: claude
---

# Notary commission lifecycle — renewal, education, and the admin that keeps it alive

The commission is the single point of failure for the whole venture. Every skill, every
automation, every dollar of notary income depends on it being current. It runs **five years**
and it does not renew itself.

This note is the thing that stops it lapsing. Related:
[[2026-09-15-notary-business-backend-systems]].

## ACTIVATE ON DAY ONE — this note cannot ring yet

**It carries no `due` because the commission does not exist yet.** There is no expiry date to
count back from, and inventing one would put a fictional date on a real calendar.

**On the day Lemar is sworn in, do this and nothing else matters more:**

1. Record the **commission number**, the **swearing-in date**, and the **expiry date** in this
   note.
2. Set `due` to **expiry minus 90 days**. `haven-calendar-sync` will then project it onto the
   reminder calendar automatically, and the lapse risk is closed.
3. Create a second note for the continuing-education course, `due` at **expiry minus 120 days**,
   so the course is finished before the renewal window rather than during it.

Ninety days is deliberate. Renewal involves a course, an exam, an application and a county
clerk visit — the same chain as the original commission. Thirty days is not enough runway for
a chain with four links and a government office in it.

## What renewal actually requires

- A **3-hour continuing education course** (the first-time requirement is 6 hours).
- An **updated exam**.
- The renewal application through DORES.
- The oath again at the County Clerk.

Budget the same calendar patience the first commission took, not less.

## The other admin that has to keep up

**Address or name change.** A move or a name change must be reported to DORES. Easy to forget
in the middle of moving, which is exactly when it happens. If Lemar moves, this note gets an
Update and the notification goes out in the same week.

**Trade name certificate.** If the business trades under a brand rather than his legal name, a
Trade Name Certificate is filed with the county clerk in **each county where the business
operates** — so expanding the service area is a filing event, not just a pricing decision.
Currently **blocked on the brand name**, which is also blocking the Google Business Profile.

**E&O insurance renewal.** Once a policy exists, its own renewal date joins this note. A lapsed
policy is worse than no policy, because it feels like cover and is not.

## Supplies — small, but a dead pen costs a whole trip

Keep on hand, checked when the calendar reminder for renewal fires:

- Spare **seal**, stored locked and separate from the journal (see the loss playbook — one loss
  should never be both).
- Spare **journal**, so a damaged one never stops work.
- Ink, and pens that actually work. Two of them.
- Anything a mobile signing needs that a hospital room will not have.

The whole list costs less than one travel fee. A signing abandoned because nothing would write
costs the fee, the trip, and the review.

## Ownership

`lemar` owns the day-one activation above — nobody else can supply a commission number.
`samira` owns it afterwards: once the `due` exists, the reminder rings, and she surfaces it like
any other dated note.

**Samira must never guess or infer a commission date.** An unknown stays blank and gets asked.

## Sources
- claude: Claude Code session, 2026-09-16 — NJ renewal requirements (five-year term, 3-hour
  continuing education, updated exam) from the project brief's earlier research pass
