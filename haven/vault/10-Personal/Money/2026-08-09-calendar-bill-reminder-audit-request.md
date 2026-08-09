---
created: 2026-08-09T08:11:00-04:00
updated: 2026-08-09T09:45:00-04:00
domain: personal
type: task
status: active
tags: [calendar, bills, money-hub, samira-capture]
source: slack
area: money
---

# Audit reminder calendar for 1-week-before bill/expense notifications

Lemar dropped a request in the Samira capture DM: use Google Calendar to make sure he's
paying off any expenses or bills a week before they're due. Specifically he wants every
current Google Calendar entry that's about paying a bill or an expense to carry a
notification a week before it's due.

## Context (per the vault)

The **money-hub** skill already projects dated bills from
`haven/vault/10-Personal/Money/money-hub-ledger.md` onto the reminder calendar
(`c_205bab62b8bb2c4fe12eec38bbc6725abaf6f5f11b767fe99a542112cf5695d3@group.calendar.google.com`),
and **haven-calendar-sync** rings notes carrying a `due` field. Neither is documented as
guaranteeing a specific "1 week before" notification lead time on every bill/expense
event, and Lemar's ask is about auditing what's already sitting on the calendar
(including anything predating the money-hub build) — not just what's created going
forward. That's a gap worth checking, not assumed already covered.

## This task

Audit every existing event on the reminder calendar whose title/description reads as a
bill or expense payment (cross-check against `money-hub-ledger.md` line items and any
`due`-bearing Haven note) and confirm/add a 7-day-before popup notification on each.
Report what was checked, what was added, and flag (via one #decisions parent, never a
guess) any event that's ambiguous as a bill/expense. Staged as a fenced `run:admin-3x`
prompt to #admin, un-reacted (per PART B buffer — not for this run's PART C).

## Sources
- slack: Samira capture DM (`D0BHPKMDNEP`), ts `1786241654.146999` (2026-08-09, Lemar's
  raw capture: "Okay so basically I want to use my Google Calendar to make sure that I'm
  paying off any expenses or bills a week before they're due. I need to make sure that
  all the current Google Calendar entries that have to do with paying a bill or an
  expense, a week before, give me a notification that it needs to be paid")

## Update 2026-08-09 (calendar audit — PART C)

Audited the reminder calendar
(`c_205bab62...@group.calendar.google.com`)
for a window of the past month through the next six months (2026-07-09 through
2027-02-09). **83 calendar entries** were returned and classified by title/description
(cross-checked against `money-hub-ledger.md`'s `bills:`/`plans:` `calendar_event_id`
fields and, where no id matched, against explicit payment language in the event
itself). No event was created, deleted, or recreated — only `update_event` (adding a
reminder override) was used, and only on confirmed bill/expense events.

**Confirmed bill/expense events — 20** (grouped by base event id; recurring monthly
series counted once, all instances share the series' reminders):
1. `7djf895pc8is0illrr8bcrra20` — Haven: Claude (Anthropic) $100/mo (ledger match)
2. `e7d9muku31setk1b10le3bf3ak` — Haven: Wispr Flow $15/mo (ledger match)
3. `lf7pne54rrtcnrvekhq0fecec4` — Patreon $25/mo (ledger match)
4. `pg0a92rgg01l09mg3tatcfb3mk` — Haven: T-Mobile bill payment 1 of 2 — $265 (ledger match)
5. `q36k3ogoblpe3i5amktigav8ig` — Bill: METRC — $40 (ledger match)
6. `ue8jtslgpl89qlmhdra710h13k` — Bill: Cleaning supplies — $30 (ledger match)
7. `jfh8548cet84pcqo3o697fkbq8` — Bill: Comedy show tickets — $50.28 (ledger match)
8. `ptacguksk2rsf3md3403gljtes` — Bill: Travel to The Station — $50 (ledger match)
9. `kli8jm1vlal3ntffr2lqdkpmuk` — Set aside today: $253.61, 8/10 (ledger `daily_targets`/plan installment 1 match)
10. `2orriv7cr3cnb71vsc9vhnqjsc` — Set aside today: $83.33, 8/11 (plan installment 2 match)
11. `36p3d0st3kgcq2pdcgs2nf39b8` — Set aside today: $83.33, 8/12 (plan installment 3 match)
12. `ctorpublicelukjo77eve3cipc` — Set aside today: $83.33, 8/13 (plan installment 4 match)
13. `rgklgnofffcr2m4lb7cd4l4gis` — Set aside today: $83.33, 8/14 (plan installment 5 match)
14. `8cdo5givjtcjvc93hjd2os03a8` — Set aside today: $83.35, 8/15 (plan installment 6 match)
15. `3mlurpnt5oejqpc55n6jbd8o1c` — Haven: Gusto — payroll due Mon Jul 13 (explicit "payroll due")
16. `474nemh5ki2hj3k81211pfouvo` — Haven: Gusto — payroll due Mon Jul 27 (explicit "payroll due")
17. `ao3bovihps93v48ksiti9rrsnc` — Haven: Liquidibee — $500 good-faith forbearance payment not received (explicit payment amount/due)
18. `320jv5tahe27hl54d56irpdrt8` — Haven: T-Mobile — Cherry Hill Mall: pay bill (explicit "pay bill")
19. `f6usr0gdlgoqcfgceaar0rs03c` — Haven: Extra Space Storage — unit 3003 past due (explicit "past due")
20. `uio9tr78osfv3l5bn551m6dge4` — Haven: Crum & Forster — Workers' Comp premium installment due $805 (explicit premium amount/due)

**Reminders added — 20 of 20** confirmed events lacked a 7-day-before (10080-minute)
popup and got one added via `update_event`, with every existing reminder on that event
preserved alongside it (no event's other reminders were removed; no event was deleted
or recreated):
- Items 1, 2, 15, 16, 18, 19, 20 kept their existing popup (540/30/10/30/10 min) and
  gained a second popup at 10080 min.
- Items 4–14, 17 kept their existing day-of popup (0 min) and gained a second popup at
  10080 min.
- Item 3 (Patreon) had no per-event reminder override (it was inheriting the
  calendar's default reminders) — it now carries an explicit 10080-min popup override.
  Note: this means Patreon no longer inherits whatever the calendar-level default
  reminder was — only the 7-day popup is now explicit on it.
- Note on items 4, 15–17, 19: their due dates (8/3, 7/13, 7/27, 7/15, 7/15) have
  already passed relative to today (8/9), so the newly-added 7-day-before popup fires
  in the past and produces no future notification for those specific occurrences —
  added anyway per the audit rule (recurring series like Claude/Wispr Flow benefit
  going forward; the one-time past-due items are flagged here as already-elapsed so
  Lemar isn't surprised a popup didn't fire).
- Note on items 9-14 ("Set aside today" daily aggregate events): these represent the
  money-hub daily set-aside RAMP, not a single bill's due date — the event's own start
  date is a savings-day, not a due date, so a "7-days-before-this-event" popup is a
  slightly different semantic than the due-date events above. Included per this task's
  explicit instruction to match the "Set aside today: $X" title pattern; flagging the
  nuance rather than silently deciding it didn't apply.

**Ambiguous events flagged (not decided, not modified) — 3:**
- `kce9ibkh596d6srmk0fupd03dc` — "Haven: Gusto Final Payroll Deadline — Complete
  Employee Close-Out (all 8 employees)" (7/31) — payroll-adjacent but phrased as an
  administrative deadline, not an explicit payment amount/due statement.
- `o6tdpp801lmchgtfhvcqu83c` — "Haven: Liquidibee — forbearance ends 8/1, ACH
  payments resume" (8/15) — signals recurring ACH debits resuming rather than a single
  bill/expense payment with an amount.
- `joj8fqaktfuj8v0n4gvsgl08ps` — "Haven: TBT Barter — monthly statement arrived
  (Cuzzie's, July activity)" (8/7) — a statement-arrival notice, not stated as a
  payment being due.

All other events in the 83-entry window (haircuts, calls/meetings/errands, Harrison
move-out days, compliance deadlines, comedy-show *ticket* reminders with no dollar
figure, walks, etc.) read clearly as non-financial or non-payment reminders and were
left untouched, not flagged.

**Does money-hub's own projection already guarantee a 7-day lead time for bills added
going forward? No — this is a real gap, not assumed-covered.** Per
`.claude/skills/money-hub/SKILL.md`'s CALENDAR section, per-bill due-date events are
created with "popup reminder on" but no specified lead time, and the four bill events
newly created by money-hub today (METRC, cleaning supplies, comedy tickets, station
travel) were in fact created with a **day-of popup (`minutes: 0`)**, not a 7-day-before
popup — confirmed directly from each event's stored reminders before this audit's
fix. Separately, the DAILY CALENDAR "set aside today" aggregate events are explicitly
specified in the skill as `minutes: 0` popups too — by design a same-day "here's what
to set aside today" nudge, not a 7-day advance warning. The daily set-aside RAMP is a
different mechanism entirely (an escalating even-split savings target spread across
the days *before* a due date) — it changes how much money accumulates ahead of a bill,
but it does not, by itself, put a 7-day-before popup on the calendar. **Flag: unless
the money-hub skill is updated to add a 10080-minute popup override alongside its
existing day-of reminder whenever it creates or updates a bill event, every new bill
money-hub adds going forward will need this same manual audit/fix — it does not
self-guarantee the 7-day lead time Lemar asked for.**

Nothing paid, nothing contacted, no calendar event deleted or recreated, no money
commitment created, no figure guessed. One #decisions parent posted for the 3
ambiguous events above.

### Sources (this update)
- Google Calendar: reminder calendar `c_205bab62...@group.calendar.google.com`,
`list_events` 2026-07-09→2027-02-09 (83 entries), `get_event`/`update_event` on the
20 confirmed bill/expense events listed above.
- `haven/vault/10-Personal/Money/money-hub-ledger.md` (bills/plans `calendar_event_id`
cross-reference).
- `.claude/skills/money-hub/SKILL.md` (CALENDAR + DAILY CALENDAR sections, for the
lead-time gap finding).
- Staged prompt: #admin `C0BBLUA7JLX` ts `1786277488.682039`.
