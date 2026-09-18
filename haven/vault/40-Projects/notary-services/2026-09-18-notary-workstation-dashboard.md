---
created: 2026-09-18T09:40:00-04:00
updated: 2026-09-18T18:40:00-04:00
domain: project
type: decision
status: active
tags: [notary, dashboard, workstation, surfaces]
source: claude
---

# The notary workstation — what it is, and the rules it runs under

The notary business now has one place to be run from: a dashboard called **The Workstation**,
published at https://claude.ai/artifact/5q3G772uieaQFrubGhfqek. The page source lives in this
repo at `apps/notary-workstation/index.html`.

Related: [[2026-09-15-notary-business-backend-systems]] (the locked plan),
[[2026-09-20-notary-exam-day-checkpoint]] (the open items it loaded from),
[[2026-09-16-notary-b2b-acquisition-tracks]].

## What it is

One surface that changes shape as the business changes phase, not two dashboards.

Right now it is in **pre-commission** mode: nothing operational exists, so the top of the page
leads with the next deadline, how many launch steps are done, how many items are open, and an
honest `$0` for money. The moment the first job is entered it flips to **operating** mode, and
the same four tiles become jobs on the book, alarms, money owed to Lemar, and what he keeps.
Nothing is faked to fill space in the meantime.

Seven tabs: **Today** (what's going on, the next seven days, and a running log of what got done)
· **Rules** · **Jobs** · **Money** · **Marketing** · **Launch** · **Open items**.

## Three decisions, recorded

**1. It is its own surface, not a panel inside Pulse.** Pulse is Lemar's personal command
center across everything. This is one business, run end to end, with its own money and its own
alarms. Putting it inside Pulse would bury it.

**2. It absorbed the Given Word Runway tracker.** All 43 steps from the five-phase runway
(https://claude.ai/artifact/YFaq1Kcgh9xUzk2EZvDC4e) are now the Launch tab, with their costs,
their deadline and queue and gate markers, and their tick state. The old tracker still opens,
but it is no longer the place to work from. Two trackers competing over the same checklist is
exactly the failure this avoids.

**3. It is writable, and the vault is still the record.** The page carries a small shared
database so Lemar — and Samira, and any automation — can add a job, close an item, tick a
launch step, or drop a line in the log without opening a repo. That makes it usable on a phone,
which is the whole point.

The rule that keeps this honest: **anything typed into the page is a capture, not the record.**
Haven stays the source of truth, and what lands in the page gets swept back into the vault the
same way a Convo 2 drop does. If the two ever disagree, the vault wins.

## What it computes, rather than asks for

- **The four alarms** from `notary-journal-mirror` — no journal entry, invoice unpaid on its own
  terms, act logged with no fee, scan-back overdue — are derived from the job board and shown in
  a red band at the top of every tab. An appointment that has passed with the job still open is
  flagged too.
- **The money picture** is computed from completed jobs only: billed, minus what the printing
  actually cost (`pages × 2 × $0.055` when no receipt exists), minus the set-aside at 20% on
  the statutory line and 35% on everything else, leaving what Lemar keeps. The exempt-versus-
  taxable split for Schedule SE is a row, not a reconstruction job in April.
- **Payment chasing** runs on each channel's own terms — 7 days for consumer and agent-referral
  work, day 16 for a brokerage, day 31 or 46 for a signing service. A loan signing is not late
  at one week.
- **Marketing** scores each channel on jobs and billed revenue from the job board itself, beside
  its current state and what is blocking it. No second place to key an attribution.

## What it deliberately does not hold

No signer full names, addresses, dates of birth, or credential details — same PII-poor rule as
the job record. The journal of record holds that, under its own access controls and a ten-year
duty, and a copy in a shared page could never be fully deleted. First name and a town is all
the board needs.

It also does not decide anything legal. It never says whether an act may be performed, never
prices outside the published card, and the RESPA line — never pay an agent for a referral — is
printed on the Marketing tab where the temptation actually lives.

## What it was loaded with, on 2026-09-18

43 launch steps across the five phases · 15 open items (the four DORES questions, the three
BlueNotary questions, the three county-counter questions, the Monday exam, the county clerk
call, the platform research, and the CPA and RESPA-attorney calls) · 5 marketing channels,
each with what is blocking it · 0 jobs, which is correct until the commission exists.

## Sources
- claude: Claude Code session, 2026-09-18

## Update 2026-09-18T11:05-04:00 — the Rules tab

Lemar asked for the NJ notarial rules to live here too, as the thing he pulls up when he is
standing at a kitchen table and is not sure what he is allowed to do. It is the second tab, not
the last, so it is reachable with a thumb without scrolling the tab strip.

**It opens with a decision path, not a rule list.** Seven questions in order — can I be sure who
this is, is the signer actually here, do they seem willing and aware, is the document complete,
am I being asked to explain it, do I have a stake in this, and still unsure? The last one
answers itself: do not do it, say you will confirm and come back.

Below that, 33 rules in eight groups, each carrying its citation, searchable by plain words
(fee, journal, blank, remote, seal, RESPA). The groups: the lines you do not cross · saying no
and how to record it · the journal · what you may charge · remote and electronic acts · the
commission itself · if the seal or journal goes missing · asking for reviews.

**The eighth group is the one that matters most for honesty: four things that are not
confirmed** — whether NJ caps a remote act's fee separately, whether the journal is open to
inspection, whether the full credential number may be recorded, and the exact NJ mechanics for
reporting a lost seal. They are marked in amber and they say plainly not to rely on them. They
are the same four questions sitting in the Open items tab with DORES. When an answer comes back,
it moves out of that group and into a real one.

The page states its own authority: the NJ Notary Public Manual and DORES are the authority, and
when the page and the manual disagree the manual is right and the page needs fixing. The DORES
and county clerk phone numbers sit at the bottom of the tab, where you would look for them.

**Sources for the rules**, all already in this vault: the NJ law research in
[[2026-09-15-notary-business-backend-systems]] (N.J.A.C. 17:50-1.11 journal contents, one-journal
rule, ten-year retention, 17:50-1.18 fee caps, RON since 2021-10-22 and its notification and
recording duties), [[2026-09-16-notary-seal-journal-loss-playbook]] (the six steps),
[[2026-09-16-notary-commission-lifecycle]] (the five-year term, the 90-day oath, renewal), and
the UPL, RESPA, refusal-log and review never-clauses from the `notary-intake` and
`notary-journal-mirror` skills.

Nothing here was written from memory. If a rule is not in the vault, it is not on the page.

## Update 2026-09-18T11:50-04:00 — restyled to the QuickPay reference

Lemar sent a fintech app UI as the direction and asked for the workstation to look like it. His
words win on visual direction, so the page was restyled to match rather than argued with.

**What changed.** Near-black ground (`#08070C`) with a soft violet glow behind the masthead ·
electric violet accent (`#7C4DFF`) · big soft-cornered cards (24px) · Plus Jakarta Sans
throughout, tight and heavy, replacing the Newsreader serif, which did not belong in this world ·
pill-shaped tab strip with the active tab filled violet, replacing the underline tabs ·
rounded-square icon tiles on every list row, the way the reference marks each line of recent
activity · money coloured green coming in and coral going out · rounded checkboxes and pill
inputs.

**The one structural change: the hero card.** The headline number now sits on a full-width violet
gradient card, the way the balance card sits at the top of the reference. Pre-commission that is
the next deadline; operating it is what Lemar actually keeps after costs and the set-aside. The
other three figures are dark tiles underneath. One number worth seeing from across the room, three
supporting it.

**It is now single-theme by design.** The earlier build carried a full light palette and a dark
one. A fintech surface like this is a committed look, so the light theme was dropped and every
colour is painted explicitly, which is the documented way to do that. Anyone opening the page in
a light system theme still gets the dark page, which is the intent.

**The three channel colours survived the change** — teal, violet, ochre — re-validated against the
new near-black card surface: all three pass the lightness band, the chroma floor, colour-blind
separation and contrast. The status colours (green, amber, coral) stay reserved for state and are
never reused as a series.

One layout bug was caught by rendering the page and looking at it: the stat row was ragged because
the track count floated. The row is now pinned to hero-plus-three, stacking to two and then one
on narrow screens.

## Update 2026-09-18T12:30-04:00 — the Launch page, the step dialog, and a calendar

Three asks, all built into the same artifact rather than a second one. Lemar's standing
requirement is that the whole notary business lives on one surface, so "its own page" was read as
a dedicated full page inside the workstation, not a separate link. If he wants it split out later
that is a small change; splitting it now would split the data too.

### The Launch page

It no longer opens on a flat checklist. It opens on the ONE step that is actually next, on the
violet hero card, with the overall progress bar underneath — the best thing the old Runway
tracker did, brought across. Three tiles beside it: how many steps are in progress, how many are
blocked, how many have been written up.

### The step dialog — the real ask

Every step now opens a dialog. It carries four things:

1. **Where it stands** — not started, in progress, waiting on someone else, blocked, done. A step
   can now be honestly "waiting on the county clerk to call back" rather than a box that is either
   ticked or not.
2. **A date**, optional. A dated step appears on the calendar.
3. **What happened** — free text. This is the point of the whole feature.
4. **Every prior update**, newest first, each stamped with its date and the status at the time.

Saving appends the note to the step's `updates[]`, sets the status, and drops a line in the Today
log. So the plan updates itself as it is worked: the row on the Launch page now shows the latest
update underneath the step, and the full story is one tap away.

The checkbox still means done. The dialog is where the story goes. Those are deliberately
separate — ticking something is one gesture, explaining it is another, and requiring the second to
do the first would mean steps quietly stop getting ticked.

### The calendar

A month grid with a coloured dot per item, a day view under it, and a thirty-day run-up list.
Four sources land on it, colour-coded: **jobs** (violet — who, where, what it pays), **open
items**, **dated launch steps**, and **hard deadlines** in red.

**The four State deadlines are computed, never stored.** Enter the commission issue date and the
LLC formation date on that tab and the page works out: the 90-day oath deadline, the continuing
education course at expiry minus 120, the renewal window at expiry minus 90, and the annual report
in the anniversary month. Expiry is taken from the packet when recorded, otherwise five years from
issue. A blank date means the deadline does not appear — nothing is guessed, which is the same
rule the commission lifecycle note already states.

That closes the single largest risk in the plan in the place Lemar will actually look. The 90-day
oath deadline cancels the commission if missed, and until now it lived only in a note that cannot
ring until someone types a date into it.

### One date was added to the plan

`File Given Word Notary LLC` is now dated **2026-09-20**, with the reason recorded on the step
itself. That is the vault's own recommendation — file it before Monday, independently of the exam,
because no LLC means no EIN, no EIN means no W-9, and no W-9 means no signing service registration.
Encoding an existing recommendation as a date is not the same as inventing one.

## Update 2026-09-18T18:40-04:00 — the audit, and the tap-first rework

Lemar's ask, in his words: one page to know everything going on in the business, usable in front
of a customer, short ideas not paragraphs, mostly buttons, and keep it clean. He pointed at the
handoff doc, which lists four artifacts. The audit came out like this:

**The four artifacts.** The Workstation is the one that stays. The other three are now retired
with a banner at the top pointing to the Workstation: the Given Word Runway (its 43 steps already
live on the Launch tab; its own tick state was empty), the Launch Board / open-items page (its
tasks and questions already live on the Open items tab; its ticks only ever lived in one browser),
and the Notary Loop explainer (still a fair picture of the loop, but its 30% set-aside and its
one-week-for-everyone invoice alarm are both out of date against the 20% / 35% split and the
per-channel terms). Nothing was deleted; each still opens.

**What changed on the Workstation.** Every capture on the page now goes through one of three
buttons fixed at the bottom of the screen — Job, Refused, Note — and each opens a sheet that is
chips and steppers, with the price computing on every tap. The only typed field is a first name.

- *Job.* Channel → what (acknowledgment, oath, deed, mortgage; a stepper for how many signatures)
  → travel tier and the two +$20 extras → when (now, later today, tomorrow, pick a day, with a
  time) → first name → how they found you → and, when it is happening now, "Done · paid" so the
  whole job is one sheet. For a signing service the chips change: package, the fee the company
  named, pages (which sets the printing cost), the company. The quote at the bottom shows both
  lines and what he keeps after the set-aside.
- *Refused.* The stop-path questions as reason chips, whether the trip was made (the travel fee is
  still earned), first name. This is the refusal log the journal-mirror skill requires and the page
  never had a way to write.
- *Note.* One line and a kind.
- *Closing out a job is buttons on the row*, on Today and on Jobs alike: Done · paid, Done, Paid,
  Journal # (a one-field sheet for the BlueNotary entry number), Scan-back sent.
- *Jobs now carry a time.* The "appointment passed" alarm fires when the time has passed, not at
  the start of the day. A signing-service job gets its scan-back deadline set to the appointment
  plus four hours, which is the intake skill's default.
- *Today shows what to do next* without leaving the tab: anything overdue, then the single next
  runway step with its tick and its Update button, then the week's jobs with their buttons.
- *Copy every job for taxes* on the Money tab puts a CSV on the clipboard — one line per job, both
  fee lines kept apart. Clipboard rather than a download because the viewer blocks downloads, and
  it needs no new permission, so the store was never at risk.
- Open items has a + Item sheet (kind, who, by-when as chips). The launch step dialog's status is
  chips too. The three big inline forms are gone.

**Not changed, on purpose.** Same URL, same store, same capabilities, same look. The rate card is
still a page constant, now in one place that both the quote and the Money tab read. Nothing is
invented: travel starts unselected, a signing fee has to be tapped, and a blank date still means
no deadline.

**Still open from the handoff.** The Haven sweep-back (a job typed here still exists only here
until Samira's PART 4 learns to read the store) and the Google Calendar link (a job booked here
does not ring his phone) are both routine changes, not page changes, and were not touched.

Verified once at phone width with three sample jobs: a $32.50 consumer job nets $21.50 after the
$11 set-aside; the sheet quotes $2.50 + $65 with $23.25 set aside for two signatures at the
≤20-mile tier after 7pm. Sample jobs were never written to the live store.

## Update 2026-09-18T19:40-04:00 — two rules corrected from the statute read

The 2026-09-15 statute read (recorded in `10-Personal/2026-09-12-become-a-notary-nj.md`) landed on
main after the rework above. Two things on the Rules tab followed from it. The remote-signer
identity rule no longer says "two of three methods" as the only route: §19d(1) gives three routes
(personal knowledge, a credible witness, or at least two types of identity proofing), and the page
now says so with the citation. The 45-day journal transmittal duty (§27f) was added to the
"not confirmed" group beside the open DORES question it belongs to, because the vault records the
number but not what starts the clock or who receives the journal. Nothing else on the tab was
touched; the seal-not-always-required point has no matching rule on the page to correct.
