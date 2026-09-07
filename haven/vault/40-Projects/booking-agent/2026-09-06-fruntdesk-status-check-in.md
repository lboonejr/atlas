---
created: 2026-09-06T13:40-04:00
updated: 2026-09-06T15:25-04:00
domain: project
type: task
status: active
tags: [fruntdesk]
source: slack
---

# FruntDesk — "where am I, what's next" check-in

Lemar dropped this in Convo 2 (self-DM, ts `1788716400.631049`, 13:40 ET 2026-09-06):
"I need to get back on my FruntDesk journey, I need to know where I'm at and what I
need to do next."

Found prior FruntDesk material under `haven/vault/40-Projects/booking-agent/`
(FruntDesk = the operator-facing name for the booking-agent project). Most recent
touch was 2026-08-09 — summarized in the Convo 1 card rather than re-derived here.
Standing blocker as of that date: the fruntdeskhq.com Privacy Policy page is
live-broken (`Cannot GET /privacy.html`) and there's no Terms of Service page —
that's what's holding up Google OAuth verification (the app is stuck in Testing mode,
which caps it to pre-approved test users and expires operator grants weekly).

## Update 2026-09-06T20:58-04:00 — Chrome session ran the two-item prompt; site is down, OAuth picture was wrong

Lemar ran the Claude-in-Chrome prompt from the Convo 1 card (ts `1788719413.067149`)
and handed back a status doc (Google Doc, "Handoff — FruntDesk Privacy Policy, ToS
Draft, and Google OAuth Verification Status", 2026-09-06 17:48 ET). Three findings,
none acted on yet:

1. **fruntdeskhq.com is fully down**, not just missing a privacy page — Railway shows
   zero active deployments. Root cause: the Neon Postgres database went unreachable
   ~Sep 1 7:04pm UTC, the app retried for 24+ hours without recovering, and Railway
   stopped/removed the container ~Sep 2 9:04pm UTC. Neon's own console shows the
   project healthy (not deleted, not over quota) but compute "last active 4 days ago"
   — reads as a free-tier compute that scaled to zero and didn't wake on Railway's
   retry schedule, not data loss. Fix looks like: confirm Neon compute is awake, then
   trigger a Railway redeploy. Neither done — needs a go-ahead.
2. **The OAuth picture was wrong.** The app (Google Cloud project "Booking Agent",
   booking-agent-503620 — not "FruntDeskHQ") is already "In production" (2/100 users),
   NOT stuck in Testing as previously assumed. But it has zero scopes declared on the
   Data Access page — the Calendar scope the app actually requests at runtime isn't
   registered, so verification isn't required YET, but will be the moment it's added.
   Branding section (home page, privacy/ToS links, authorized domain) is blank because
   Google won't let it save without a live privacy policy URL first.
3. **Privacy Policy + Terms of Service drafts are written** (Google Docs, same
   Handoffs folder as the status doc; contact email fruntdeskhq@gmail.com, note the
   business is unincorporated). Still open: payment processor name (presumably
   Stripe, unconfirmed), any analytics tool, real pricing/tier text, and an attorney
   pass on the liability/disclaimer sections before anything goes live. Nothing
   published.

**Three things need Lemar's call before this moves further** (posted in-thread):
(1) confirm the exact Google Calendar OAuth scope from source (gates Data Access
verification timing), (2) decide whether to trigger the Neon/Railway redeploy now,
(3) review/approve the two drafts (payment processor, analytics, pricing, attorney
pass). Nothing published, redeployed, or submitted for verification by Samira or the
Chrome session — all still drafts/pending.

## Sources
- slack: Convo 2 (self-DM) drop, ts `1788716400.631049`, 2026-09-06 13:40 ET
- slack: Convo 1 card ts `1788719413.067149`, Chrome handoff reply ts `1788731478.422759`
- gdrive: "Handoff — FruntDesk Privacy Policy, ToS Draft, and Google OAuth
  Verification Status" (doc id `19wI-oFu2zPY4t4D29gRVBQ2Tlt--7fRi6j7jNyOD0ZE`)
- vault: haven/vault/40-Projects/booking-agent/2026-08-08-fruntdesk-oauth-verification-kickoff.md
- vault: haven/vault/40-Projects/booking-agent/2026-08-09-booking-agent-status-update-request.md
