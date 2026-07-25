---
created: 2026-07-25T11:20:00-04:00
updated: 2026-07-25T18:15:00-04:00
domain: project
type: note
status: active
tags: [booking-agent, phase1, design, schema, oauth]
source: slack
---

# Booking Agent — Phase 1 (Foundations) design pass

Executed the run:admin-3x prompt staged in #admin (ts `1784989035.005839`), following
Lemar's "Let's go with phase 1" kickoff in #booking-agent (2026-07-25) on the six-phase
build-sequencing outline from
`haven/vault/40-Projects/booking-agent/2026-07-15-booking-agent-barbers-tattoo-artists.md`
(2026-07-25 update). Scope locked earlier in that same note: solo operators, full
feature set (calendar sync, reminders, deposits/no-show fees, client history), build not
buy, Google Calendar as the sync provider, payment processor deferred to
fastest/cheapest (Stripe or similar), dogfood with the tattoo-artist friend.

This pass covers Phase 1 only — account model, client/appointment schemas, and the
Google OAuth wiring approach at a plan level. **No code, no accounts, no live OAuth app
or credentials created** — design/plan artifact only, per the prompt's explicit
instruction and the standing safety floor (no external-party actions, no live
credentials).

## Account model (single-operator, v1)

One account = one solo operator (barber, tattoo artist, etc.) — no multi-staff/shop
model in v1, matching the "solo operators first" scope decision.

```
Account
├── account_id (uuid, pk)
├── owner_name
├── business_name (optional — many solo operators trade under their own name)
├── contact_email
├── contact_phone
├── timezone (IANA, e.g. "America/New_York" — needed for calendar sync + reminders)
├── booking_slug (unique, used in client-facing booking link — v2 surface, not built yet)
├── calendar_connection_id (fk → CalendarConnection, nullable until OAuth completed)
├── payment_connection_id (fk → PaymentConnection, nullable — Phase 4)
├── created_at
└── status (enum: onboarding | active | paused)
```

## Client record schema

```
Client
├── client_id (uuid, pk)
├── account_id (fk → Account)
├── name
├── phone (primary contact channel — reminders are SMS-first per "tech-averse friend"
│         dogfood bar; email secondary)
├── email (optional)
├── notes (freeform — preferences, allergies/sensitivities if relevant to the service,
│         standing requests)
├── created_at
├── last_appointment_at (denormalized for quick lookup — updated on appointment
│                         completion)
└── source (enum: manual | booking-link | import — how the client record was created)
```

Client history (Phase 5 feature) will read off the Appointment table below rather than
duplicating data on the Client record — keeps one source of truth for past services.

## Appointment schema

```
Appointment
├── appointment_id (uuid, pk)
├── account_id (fk → Account)
├── client_id (fk → Client)
├── service_name (freeform in v1 — no service-catalog table yet; add one if solo
│                 operators need fixed price/duration presets during dogfood)
├── start_time (UTC, rendered in account timezone)
├── end_time
├── status (enum: requested | confirmed | completed | cancelled | no-show)
├── calendar_event_id (nullable — set once synced to the operator's Google Calendar,
│                       Phase 2)
├── deposit_amount (nullable — Phase 4)
├── deposit_status (enum: none | pending | paid | refunded — Phase 4)
├── reminder_sent_at (nullable — Phase 3)
├── notes
└── created_at
```

## Google OAuth wiring — plan only, not registered

**This section is a plan for how OAuth will be wired in Phase 2 (calendar sync core).
No OAuth app, client ID/secret, or credential of any kind was created or requested this
pass** — that step needs Lemar's direct setup with a Google account he controls (a new
Google Cloud project under his own account, likely separate from the Cuzzie's/Station
Google Workspace given this is an independent side project), which is an external-party
account action outside what Samira/admin executes unilaterally.

Planned flow (standard OAuth 2.0 authorization-code flow, Google Calendar API):

1. **Google Cloud project + OAuth consent screen** — Lemar creates a new Google Cloud
   project (recommend a dedicated one, not reusing Cuzzie's Workspace project, since
   this app will eventually request calendar access from third-party operators'
   personal Google accounts, not just Lemar's). Configure the OAuth consent screen
   (External user type, since operators are outside any single Workspace domain).
2. **Scopes** — request the minimum viable scope for v1:
   `https://www.googleapis.com/auth/calendar.events` (create/read/update/delete events)
   rather than the broader `calendar` scope, unless calendar-list management is needed
   later.
3. **Credentials** — Lemar (or whoever owns the eventual app's Google Cloud project)
   generates an OAuth 2.0 Client ID (Web application type) and stores the client
   secret in the app's server-side environment/secrets store — never in client code or
   checked into a repo.
4. **Per-operator connection flow** — each Account (operator) goes through the OAuth
   consent flow once during onboarding: redirect to Google's consent screen → operator
   grants calendar access → callback exchanges the authorization code for an access
   token + refresh token → tokens stored server-side, associated with that Account's
   `calendar_connection_id`, encrypted at rest.
5. **Token refresh** — access tokens expire (~1hr); the app uses the stored refresh
   token to mint new access tokens server-side as needed, no repeated operator
   interaction required unless the refresh token itself is revoked (operator
   disconnects, or Google forces re-auth).
6. **Two-way sync (Phase 2 scope, not this pass)** — once a token is live: push
   Appointment creates/updates to the operator's Google Calendar as events
   (`calendar_event_id` on the Appointment record links them), and poll/webhook for
   changes made directly on the operator's calendar (reschedules, cancellations) to
   flag conflicts back into the Appointment record.

**Flagged for Lemar's direct action (not executable by Samira/admin):** creating the
Google Cloud project, configuring the OAuth consent screen, and generating the
Client ID/secret. These require a Google account he controls making live changes in
Google Cloud Console — an external credential-creation action outside the safety floor
for unsupervised execution.

## Not done this pass (later phases, per the 2026-07-25 sequencing outline)

- Phase 2: actual two-way Google Calendar sync implementation, timezone/conflict
  handling
- Phase 3: reminder scheduling + confirm/reschedule/cancel client-facing link
- Phase 4: payment processor integration (deposits/no-show fees)
- Phase 5: client history surface (reads off Appointment records per schema above)
- Phase 6: dogfood pilot with the tattoo-artist friend

## Update — 2026-07-25 18:15 ET: formal spec docx produced

Executed the follow-up run:admin-3x prompt staged in #admin (ts `1785010138.314099`,
`task:booking-agent-phase1-spec`): repackaged this pass's three schemas + the OAuth plan
as a standalone docx design doc and posted the link back to #booking-agent (this project
is worked directly in-channel, no #decisions lift needed per the 2026-07-16 call).
Nothing new designed or decided — same content as above, formatted as a deliverable.

Doc: [Booking Agent — Phase 1 (Foundations) Design Spec](https://drive.google.com/file/d/1tMJ6VqgahomcdWbquI5I06okFvY-pk5m/view?usp=drivesdk)
(Google Drive, docx)

## Sources
- slack: #admin (C0BBLUA7JLX), ts `1784989035.005839` (2026-07-25, run:admin-3x prompt,
  original design pass)
- slack: #admin (C0BBLUA7JLX), ts `1785010138.314099` (2026-07-25, run:admin-3x prompt,
  docx spec build)
- slack: #booking-agent (C0BHXTPST52), ts `1784985333.569689` (2026-07-25, Lemar: "Let's
  go with phase 1")
- haven: `haven/vault/40-Projects/booking-agent/2026-07-15-booking-agent-barbers-tattoo-artists.md`
  (scope decisions + 2026-07-25 build-sequencing outline)
- drive: `1tMJ6VqgahomcdWbquI5I06okFvY-pk5m` (Phase 1 Design Spec docx)
