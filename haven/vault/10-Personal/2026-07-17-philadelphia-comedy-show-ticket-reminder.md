---
created: 2026-07-17T08:25-04:00
updated: 2026-07-17T12:17-04:00
domain: personal
type: note
status: active
due: 2026-09-09T09:00-04:00
tags: [event, comedy, philadelphia, ticket-reminder]
source: slack
calendar_event_id: 62mngnbidcnrj2uae08sf52sic
---

# Philadelphia comedy show — ticket reminder

Lemar wants to go see a comedian's show in Philadelphia and asked to have it on his
event calendar so he remembers to buy tickets about one month before the show.

He posted a flyer/screenshot (Slack file `F0BHVCRDANP`, `IMG_1945.png`) with the
comedian, venue, and date — Samira cannot read image contents, so those specifics are
not captured here yet. Flagged to #decisions to get the comedian name + show date in
text so a `due` can be set and calendar-sync can ring the one-month-before reminder.

## Update 2026-07-17 (2) — show date received, comedian/venue still unknown

Lemar reacted ✅ and replied in the #decisions thread (message ts `1784290803.224659`):
"October 9th and 10th is the date of the Philly show." That gives the show date but
not the comedian name or venue, so the reminder title stays generic for now. Setting
`due` to 2026-09-09 (~1 month before the earlier of the two dates) so
`haven-calendar-sync` can pick this note up and render the ticket-buying reminder on
the calendar. If Lemar supplies the comedian name/venue later, update this note (and
the resulting calendar event title) rather than filing a new one.

## Sources
- slack: Samira capture DM (D0BHPKMDNEP), ts 1784290340.445549, 2026-07-17 08:25:40 ET (image attached: `IMG_1945.png`)
- slack: #decisions message ts `1784290606.402879` (parent, probe card) / `1784290803.224659` (Lemar's reply — show date)
