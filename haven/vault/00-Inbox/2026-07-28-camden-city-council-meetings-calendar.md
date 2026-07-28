---
created: 2026-07-28T13:15-04:00
updated: 2026-07-28T14:15-04:00
domain:    # UNRESOLVED — set one of: personal | cuzzies | station | project | reference | legal
type: task
status: active
tags: [camden, city-council, calendar, research]
source: slack
---

# Camden city council meetings — search + add to Google Calendar

Lemar asked Samira to search for all Camden, NJ city council meetings
and pre-meetings (caucus/agenda sessions) for the remainder of 2026 and
add them to his Google Calendar.

- Ask, verbatim: "Samira Can you do a search of all of the Camden city
  council meetings and pre-meetings for the rest of the year and put them on
  my google calendar?"
- No dates confirmed yet — the research itself was the first step.
- Scope: remainder of 2026 (from capture date 2026-07-28 through 2026-12-31).
- `domain` left UNRESOLVED: could be `cuzzies` (Cuzzie's is in Camden — city
  council may touch zoning/licensing relevant to the business) or `personal`
  (Lemar tracking civic matters generally). Not stated explicitly either way.
- Staged as an admin-3x prompt to #admin for a later Samira scan to execute
  (buffer rule — not run the same scan it was captured in): find the official
  Camden city council meeting schedule (cityofcamden.org or NJ municipal
  notice postings), then create one reminder-calendar event per confirmed
  meeting/pre-meeting, no external attendees.

## Update — 2026-07-28 (1:26 PM ET) — research pass (PART C)

Researched the official City of Camden, NJ council meeting schedule
(camdennj.gov / ci.camden.nj.us — NOTE: `cityofcamden.org` (named in the
original ask) is actually Camden, South Carolina, a different municipality;
the correct NJ domain is `camdennj.gov`).

**Findings:**
- Confirmed recurring pattern from the city's own "City Council Meeting
  Dates" page and 3 actual published 2026 agendas: Pre-Meeting Conference
  on the 1st Tuesday of each month, Regular Meeting on the 2nd Tuesday of
  each month at 5:00 PM, "unless otherwise indicated."
- Verified against real 2026 agenda PDFs: Jan 13, 2026 (2nd Tue), Mar 10,
  2026 (2nd Tue), Apr 14, 2026 (2nd Tue) — all match the stated pattern.
  All three are already in the past relative to today (2026-07-28), so none
  fall in the requested remainder-of-2026 window.
- Could NOT independently confirm specific Regular Meeting or Pre-Meeting
  Conference dates for Aug–Dec 2026: the camdennj.gov and ci.camden.nj.us
  domains return HTTP 403 to automated fetch tools (Cloudflare/bot
  protection blocks direct page/PDF retrieval), and no agenda PDFs or an
  annual schedule notice for Aug–Dec 2026 are indexed/searchable yet
  (they likely post closer to each meeting date, consistent with council
  practice of posting agendas ~1 week out). No August-recess or
  holiday-adjustment notice was found either way.
- Per the "do not guess dates" instruction, NO calendar events were created
  this pass — projecting the 1st/2nd-Tuesday pattern onto Aug–Dec without
  a posted agenda or annual notice would risk wrong dates the city itself
  may override ("unless otherwise indicated").

Recommended next step: re-run this research closer to each month (agendas
typically post about a week ahead), or call the City Clerk (856-757-7115 /
CityCouncil@camdennj.gov) for the confirmed remainder-of-2026 schedule in
one shot.

Status: left `domain` UNRESOLVED (vault-keeper's call). Research pass
complete; calendar action deferred pending confirmable dates.

## Sources
- slack: DM with Samira bot (D0BHPKMDNEP), ts 1785256869.114089
- web: https://www.ci.camden.nj.us/city-council-meeting-dates/ (“City
  Council Meeting Dates” page — recurring pattern statement)
- web: https://www.camdennj.gov/wp-content/uploads/2026/01/01-13-2026-revised-3-1.pdf
  (2026-01-13 agenda)
- web: https://www.camdennj.gov/wp-content/uploads/2026/03/03-10-2026-Revised-6.pdf
  (2026-03-10 agenda)
- web: https://www.camdennj.gov/wp-content/uploads/2026/04/04-14-2026-Revised-2.pdf
  (2026-04-14 agenda)
