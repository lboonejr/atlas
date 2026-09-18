# The Workstation — Given Word Notary

Source for the notary business dashboard, published as an Artifact at
https://claude.ai/artifact/5q3G772uieaQFrubGhfqek

`index.html` is the whole page. It is published with the `db` and `user` capabilities, so the
data lives in the artifact's own shared store rather than in this file — editing and
republishing the page never touches the data.

The decision record, and the rule about which surface is the source of truth, is in the vault:
`haven/vault/40-Projects/notary-services/2026-09-18-notary-workstation-dashboard.md`.

## Collections

| Path | Holds | Written by |
|---|---|---|
| `jobs/<id>` | one job: channel, `date` + `time` (HH:MM, local), fees, `acts`, pages, payer, terms, `paidOn`, `journalEntryId`, `scanbackDue`/`scanbackDone` (signing service), `refused`/`refusalReason` for a logged refusal | the Job and Refused buttons in the dock, or `notary-intake` |
| `tasks/<id>` | an open item — a task Lemar owes, or a question out with DORES / BlueNotary / the county clerk | the + Item button on the Open items tab |
| `launch/<id>` | one runway step: phase, title, detail, cost label, `deadline`/`queue`/`gate` tag, `status`, optional `due`, `updates[]`, done | seeded from the Given Word Runway tracker; `status`/`due`/`updates` written by the step dialog |
| `channels/<id>` | one way work can reach the business: key, name, status, what is blocking it, spend | the page's Marketing tab |
| `activity/<YYYY-MM-DD>` | one document per day holding that day's log entries (capped at 60) | every save on the page, the Note button, and anything reporting a completed job |
| `meta/config` | `phase` (`prelaunch` or `operating`), entity name, and the three dates the State counts from: `commissionDate`, `commissionExpiry`, `llcFiledOn` | the Calendar tab |

A job's `source` must match a channel's `key` for the marketing scoreboard to count it.

An `updates[]` entry is `{date, text, status}`, appended by the Launch step dialog and capped at 40
per step. Arrays replace wholesale on an `update` write, so read the current array, append, and
write the whole thing — never patch an index.

## The calendar's four computed deadlines

Nothing about them is stored. They are derived at render time from `meta/config`, so a blank date
means the deadline simply does not appear:

| Deadline | Derived from |
|---|---|
| Last day to swear the oath | `commissionDate` + 90 days |
| Start the continuing education course | expiry − 120 days |
| Start the commission renewal | expiry − 90 days |
| NJ annual report ($75) | the anniversary of `llcFiledOn`, this year and next |

Expiry is `commissionExpiry` when it is recorded, otherwise `commissionDate` + 5 years.

The **Rules** tab holds no data — the rules are constants in `index.html` (`STOP_PATH` and
`RULES`), so changing one is a page edit and a republish. That is deliberate: a legal reference
that any viewer could edit in place is worse than no reference. Every rule carries its citation,
and four of them sit in a "not confirmed" group that says so on its face; when DORES answers one,
move it out of that group and update the matching item in `tasks`.

## How things get recorded (2026-09-18 rework)

The page is tap-first. A fixed dock at the bottom carries three buttons — **Job**, **Refused**,
**Note** — and each opens a sheet (a dialog that slides up on a phone). Anything with a known set
of answers is a chip; a count is a stepper; the only typed field is a first name (a town is
optional). The job sheet's quote recomputes on every tap from the same constants the Money tab's
rate card prints (`ACTS`, `TRAVEL`, `EXTRAS`, `SIGNING_FEES`, `PAGE_PRESETS`), so the two cannot
disagree. A refusal is written as a job with `refused: true`, a zero statutory line, and the travel
fee if the trip was made; the "no journal entry" alarm skips it, and the marketing scoreboard does
not count it.

Closing a job out is buttons on its row, on Today and on Jobs alike: **Done · paid** (one tap for
at-the-table channels), **Done**, **Paid**, **Journal #** (a one-field sheet for the BlueNotary
entry number), **Scan-back sent**. A signing-service job gets `scanbackDue` set to the appointment
plus `SCANBACK_HOURS` (4) at save time, matching the intake skill's default.

Jobs carry a `time`. "Appointment passed" fires when the time has passed, not at the start of the
day; the calendar's day view and the Today list sort by it.

**Copy every job for taxes** on the Money tab puts one CSV line per job on the clipboard (both fee
lines kept apart, printing, set-aside, paid date, journal id, refused flag, source). It uses the
clipboard because the viewer sandbox blocks downloads, and it needs no extra capability.

## Republishing

Edit `index.html`, then publish it with the `url` above. Do not pass `capabilities` unless you
mean to change them — omitting it carries the stored declaration forward.

## Rules baked into the page

- Money is computed from completed jobs only. Printing is estimated at `pages × 2 × $0.055`
  until a receipt figure is entered, and estimates are labelled as estimates.
- The set-aside is 20% on the statutory notarial fee and 35% on everything else. It is a
  reserve policy, not a tax calculation.
- Invoices are chased on the job's own channel terms, never a global one week.
- No signer PII beyond a first name and a town. The legal journal is a separate system.
