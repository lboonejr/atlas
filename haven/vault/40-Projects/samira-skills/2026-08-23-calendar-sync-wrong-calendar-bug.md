---
created: 2026-08-23T10:35:00-04:00
updated: 2026-08-23T10:35:00-04:00
domain: automation
type: log
status: done
tags: [samira, calendar-sync, bug]
source: claude
---

# haven-calendar-sync — wrong-calendar duplicate bug (22 Cuzzie's/Station notes), reverted

## What happened

Today's PART S haven-calendar-sync run (~14:xx UTC, commit
`33f3fd3880aa376284b839bab78a92eb17ac9891` on `main`) misdiagnosed 22 live,
correctly-placed business-calendar events as "deleted." All 22 notes carry
`domain: cuzzies` or `domain: station`, and per the locked policy
(`.claude/anchors.md`, Google Calendar section, and the money-hub skill —
"business bills never ring on the personal reminder calendar") their
`calendar_event_id` pointed at events that had been intentionally left on the
**Cuzzie's (Owners)** business calendar
(`c_5405960d86d1e2152cef29d5cb1ae6a4d7edd8a50f6f7eb3f5d66ab940874f1a@group.calendar.google.com`)
during a 2026-08-16 correction pass. The run recreated fresh events for all 22
on the **personal reminder calendar**
(`c_205bab62b8bb2c4fe12eec38bbc6725abaf6f5f11b767fe99a542112cf5695d3@group.calendar.google.com`)
and overwrote each note's `calendar_event_id` to point at the new wrong-calendar
duplicate instead of the correct, still-live business-calendar event.

Two of the 22 correct business-calendar events were personally verified live and
confirmed via `mcp__Google-Calendar__get_event` before this revert began.

**Likely root cause:** for `domain: cuzzies` / `domain: station` notes, the RECREATE
check only looked up the id on the personal reminder calendar (the calendar this
skill is scoped to for personal notes) rather than checking the Cuzzie's (Owners)
calendar first — the calendar these business notes are actually projected onto.
Finding no matching event on the calendar it checked, it concluded "deleted" and
recreated, when the event was live all along, just on the other calendar.

## Second occurrence today

This is the **second time today** this exact failure mode has occurred. The 8:03am
run already had to fix two similar false-positive "recreate deleted event" cases —
Regus/IWG (`2026-08-20-regus-iwg-collections-legal-threat.md`) and Gusto payroll
(`2026-08-21-gusto-payroll-aug9-aug22-due-aug24.md`) — where a duplicate was created
on the *same* (Cuzzie's Owners) calendar and then cleaned up a few hours later (see
those notes' 08:08/13:07 calendar-sync updates, and `.claude/state/samira-state.json`
lock note history). This run's failure is the same core bug (list/lookup missing a
live event and recreating a duplicate) but landed on the wrong calendar entirely
instead of duplicating on the right one — a more serious variant, since it also
violates the business-bills-never-ring-personal policy.

## Fix applied (this note)

1. Reverted all 22 notes' `calendar_event_id` back to the correct, live Cuzzie's
   (Owners) business-calendar event id (table below). Only the `calendar_event_id`
   and `updated` frontmatter lines were touched in each file — no body/prose edits.
2. Deleted all 22 wrong-calendar duplicate events from the personal reminder
   calendar. The correct events on the Cuzzie's (Owners) calendar were left
   untouched throughout — never queried for deletion, never modified.

## Recommendation

`haven-calendar-sync` needs a fix so that for `domain: cuzzies` / `domain: station`
notes, the "does this event still exist" check looks up the id on the **Cuzzie's
(Owners)** calendar (not just the personal reminder calendar) before concluding an
event was deleted and recreating it. The RECREATE rule as currently implemented
appears to assume every note's event lives on the personal reminder calendar, which
is false for business-domain notes that have already been correctly routed to the
Owners calendar (per the 2026-08-10 lock policy). This is the same underlying gap
behind both of today's incidents.

## All 22 reverted files (old/new event ids)

| # | File | Wrong (deleted, personal calendar) | Correct (restored, Cuzzie's Owners) |
|---|---|---|---|
| 1 | `haven/vault/20-Cuzzies/2026-07-05-jarred-jerzeygrown-business-call.md` | `peib0nqgjld5lvvhgms1g893js` | `6drq9vh1b29kjnqbbbn6hbf9h8` |
| 2 | `haven/vault/20-Cuzzies/2026-07-10-gusto-jun28-jul11-payroll-due.md` | `u91d745feq1km94dk28at1sd3s` | `0gi4ohhuaqe2anbi7n4bb3fhm0` |
| 3 | `haven/vault/20-Cuzzies/2026-07-13-greenbooks-cpa-records-meeting.md` | `u38dl92gek6e4qmspi36nqctl4` | `okad6h26cjeqsjqr84hvj5lhik` |
| 4 | `haven/vault/20-Cuzzies/2026-07-15-liquidibee-good-faith-payment-missed.md` | `slkrrs30gadb9sbjd9p2k61l5c` | `4u73fa8egqk8u5g5teof08v0nk` |
| 5 | `haven/vault/20-Cuzzies/2026-07-17-friday-followups-george-greenbooks-jason.md` | `91850qvh3fqncqhs6bumm1m614` | `lpdo2u87kml6stpto6fl5pleq4` |
| 6 | `haven/vault/20-Cuzzies/2026-07-18-cuzzies-mail-pickup-reroute.md` | `00d86os4u1gpv417lo15o22hf4` | `tlmuo8hdjt8vomi2ile1gdlt1g` |
| 7 | `haven/vault/20-Cuzzies/2026-07-23-google-cloud-2sv-enforcement.md` | `ojv1d35go2lpdsro77icr3420s` | `uivdom9g3509043lsk88op55vk` |
| 8 | `haven/vault/20-Cuzzies/2026-07-24-gusto-jul12-jul25-payroll-due.md` | `k9272phtlsotuktvd9q34uger4` | `r99cafdgphtqf15l6g54bq03s0` |
| 9 | `haven/vault/20-Cuzzies/2026-07-28-crum-forster-workers-comp-premium-due.md` | `elgf1i9ob9mcgf22ud0p225e7g` | `ng06l9u7b64dc213or610cr90k` |
| 10 | `haven/vault/20-Cuzzies/2026-07-30-gusto-final-payroll-closeout.md` | `o1r5t034nm6omfcn02vuhahkuo` | `77r5jovbnr8mllc6iut76o4p9k` |
| 11 | `haven/vault/20-Cuzzies/2026-07-31-liquidibee-forbearance-ends.md` | `9k3gpf0hmfes1a3lnc5e16f0kk` | `02bg33r2b7pu4kosmhk3kb2r74` |
| 12 | `haven/vault/20-Cuzzies/2026-08-01-tbt-barter-monthly-statement.md` | `amqaoehl3g50krbb44v5m90ai8` | `0iih2d9gdu5h5i5tgeof9s1fic` |
| 13 | `haven/vault/20-Cuzzies/2026-08-06-google-play-developer-verification.md` | `152j23hupralj22gvg9n8lj458` | `quacha11n86g0s0tosf8mtbcuo` |
| 14 | `haven/vault/20-Cuzzies/2026-08-07-crc-hemp-beverage-deadline.md` | `r5krjrt8us97esjivhll7e9duc` | `qrg5ef3socj6us3h69e6a0cqq8` |
| 15 | `haven/vault/20-Cuzzies/2026-08-11-greenbooks-cpa-invoice-7500.md` | `tcad0g0bij0i0oro6l6mkl9kbs` | `a9uokh12kt06f3ac4a701ooie4` |
| 16 | `haven/vault/20-Cuzzies/2026-08-14-mca-forbearance-plans-ahead-of-sale.md` | `aqdbcb77904ff0aj41golt6go0` | `gtp95qq1vki3ce9lopij5v4be4` |
| 17 | `haven/vault/20-Cuzzies/2026-08-14-usps-cuzzies-change-of-address.md` | `604m2oakteouapd652vrmji2d4` | `kqm31edso6ah8aieob46sle9t8` |
| 18 | `haven/vault/20-Cuzzies/2026-08-20-regus-iwg-collections-legal-threat.md` | `48dimg5eevaop1nso5d4ctp0n8` | `ebc79d4jj3niuos29u9g4jmfjc` |
| 19 | `haven/vault/20-Cuzzies/2026-08-21-gusto-payroll-aug9-aug22-due-aug24.md` | `vo1l561sua6vlg9p3s7m56e9es` | `v5kjoasoqugfg34n10glv8834c` |
| 20 | `haven/vault/20-Cuzzies/meetings/2026-07-05-eddie-happy-eddie-license-call.md` | `hht8j736k9v4gcq8k9b8479eh4` | `qmrshvdhut6apntu904ul8aa20` |
| 21 | `haven/vault/20-Cuzzies/meetings/2026-08-18-jamil-east-camden-dispensary-meeting.md` | `7086ra9fucsnnotbh5grkb3j18` | `na455usns0mu7pn8jfla1l0co4` |
| 22 | `haven/vault/30-Station/2026-07-11-station-agent-job-letter-meeting.md` | `brk6qbr9qq7ksg1desr6t22afk` | `vgi54ndm6cd727169khflpvjdc` |

## Commits

- `19bb70d7d2611ba1fca4a58268834fce877bd2b3` — revert 1–6
- `3c670987bf0b5bc9153fa71efd75345d350d1bb9` — revert 7–12
- `72056e51d8b97edae73f9bd9681804362b8c23ed` — revert 13–18
- `61fff7819f636811d0055dcfd14dcd99e632d19b` — revert 19–22

All 22 duplicate events confirmed deleted (cancelled) from the personal reminder
calendar. No events on the Cuzzie's (Owners) calendar were touched.

## Sources
- github: `lboonejr/atlas` commit `33f3fd3880aa376284b839bab78a92eb17ac9891` (the bug)
- github: `lboonejr/atlas` commits above (the fix)
- `.claude/anchors.md` — Google Calendar section (business bills never ring on the
  personal reminder calendar)
- `.claude/state/samira-state.json` — lock note history (8:03am run's Regus/Gusto
  false-positive fixes, same day)
