---
created: 2026-08-09T08:11:00-04:00
updated: 2026-08-09T09:04:00-04:00
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
