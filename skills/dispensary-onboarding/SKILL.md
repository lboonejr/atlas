---
name: dispensary-onboarding
description: Onboard a new dispensary hire end to end — create their employee folder, generate and send onboarding documents, schedule training, set up HR/payroll, and open a tracking record so every step is traceable to a target start date. Triggers when the user says things like "onboard a new employee", "hire someone at the dispensary", "set up a new hire", "I need onboarding docs and a new employee folder", or otherwise asks to bring a new dispensary employee on board.
---

# Dispensary Onboarding

A workflow for bringing a chosen dispensary hire fully on board. The skill produces **one auditable trail per hire**: a dedicated employee folder, the onboarding and compliance documents that belong in it, a training schedule, HR/payroll setup, and a single tracking record that ties every step back to the hire and the target completion date. Nothing should live only in someone's head or inbox — if it's part of onboarding, it lands in the folder or the tracker.

This is a regulated retail context (cannabis dispensary). Treat compliance documents (age/ID verification, background-check authorization, state-mandated training acknowledgment) as **required, not optional**, and never mark onboarding "complete" while any of them is outstanding.

## When to run

Run when the user asks to onboard, hire, or set up a new dispensary employee — the person has already been chosen and the user now needs the paperwork, training, folder, and tracking. Typical phrasings: "onboard our new budtender", "I'm hiring someone at the station dispensary, set them up", "get the new hire's onboarding docs and folder going", "I want them fully onboarded by Friday".

If the user only wants a *piece* (e.g. "just make the employee folder" or "just send the offer letter"), do that step and skip the rest — but still write what you did to the tracking record so the trail stays complete.

## Inputs to gather first

Before touching any tool, confirm you have what each downstream step needs. Ask the user for anything missing rather than inventing it — onboarding data is real and partly legal, so guessing is worse than asking.

- **Identity & contact:** full legal name, preferred name, personal email, phone, home address.
- **Role & terms:** job title (budtender, keyholder, inventory associate, shift lead, etc.), employment type (full/part-time), compensation (rate + basis), reporting manager, work location.
- **Dates:** target **start date** and the user's desired **fully-onboarded-by date** (the deadline). If the user said something relative like "next Friday", resolve it to a concrete calendar date and confirm it back. Every scheduled item and the tracker's due date key off these.
- **Eligibility flags specific to a dispensary:** confirmation the hire is 21+ (or the state's minimum), and whether a state badge/registration or background check is required for this role and location.

If the deadline is tight relative to today, say so up front and flag which steps (e.g. background check, state badge) have lead times that may not fit — don't silently promise a date the dependencies can't meet.

## Procedure

### 1. Open the tracking record

Create the single source of truth **first**, so every later step has somewhere to record its result. Use the project/task tracker (monday.com) to create one onboarding item for this hire.

- Create (or reuse, if one exists) an "Onboarding" board, and add an item named for the hire and start date.
- Capture: hire name, role, manager, start date, **onboarded-by deadline**, and a status of `In progress`.
- Add a checklist mirroring the steps below (folder, documents, training, HR/payroll, access, confirmation) so progress is visible at a glance.
- Keep this item's link handy — every subsequent step appends its outcome here (folder link, doc links, calendar invites, Gusto record).

If a tracker isn't available, fall back to a tracking doc in the employee folder (step 2) and note that the structured tracker was unavailable.

### 2. Create the employee folder

Create a dedicated, well-structured folder in Drive so all of this hire's onboarding and documents are traceable in one place.

- Create a top-level folder named `<Last, First> — <Start Date>` (or append to an existing "Employees" / "Onboarding" parent if one exists; search first, don't duplicate).
- Inside it, create consistent subfolders so the trail is predictable for every hire:
  - `01 Offer & Agreements` — offer letter, signed acceptance, NDA/confidentiality, arbitration if any.
  - `02 Compliance & Eligibility` — I-9 + supporting ID, W-4/state withholding, age/ID verification, background-check authorization, state badge/registration.
  - `03 Policies & Handbook` — employee handbook, dispensary SOPs, signed acknowledgments.
  - `04 Training` — training plan, completion certificates, sign-offs.
  - `05 Payroll & Benefits` — direct deposit form, benefits enrollment, pay-rate confirmation.
- Set permissions deliberately: the hiring manager and HR get edit access; do **not** broaden access to the whole org — these are sensitive records. Note in the tracker who was granted access.
- Record the folder link on the tracking item.

### 3. Generate and send the onboarding documents

Produce the documents the hire must review and sign, file copies in the folder, and route signables to the hire. Prefer the forms/e-sign tool (Jotform) for anything that needs a signature so completion is captured; use Drive for static documents and Gmail to deliver/notify.

Standard dispensary onboarding packet:

- **Offer letter / employment agreement** — role, comp, start date, manager, at-will language. File the draft in `01 Offer & Agreements`; send for signature.
- **Compliance & eligibility set** — I-9, W-4 / state withholding, age & ID verification, background-check authorization, and any state cannabis-worker registration/badge form. These gate the start date; flag any that have processing lead time.
- **Policies & acknowledgments** — employee handbook, dispensary SOPs (security, product handling, sales limits, ID-checking), and signed acknowledgment forms.
- **Payroll setup** — direct deposit authorization and pay-rate confirmation (feeds step 5).

For each document: file the blank/draft in the correct subfolder, send the signable version to the hire's personal email (via the e-sign form or a Gmail message linking it), and add a checklist line on the tracker with status `Sent → awaiting signature`. As signed copies come back, save them to the folder and flip the line to `Complete`. **Leave a clear `[TODO]` for anything that needs the user's review or a real signature — never fabricate a signature or a completed form.**

### 4. Schedule training

Lay out the training plan as concrete calendar events between the start date and the deadline, and drop the plan into `04 Training`.

- Build a short training plan document (orientation, compliance/responsible-vendor training, POS/register system, product knowledge, security & ID-check procedures, shadow shifts) sized to fit the start-date→deadline window.
- For each session, create a Google Calendar event with the hire, the manager, and any trainer; title it clearly (e.g. "Onboarding — POS Training: <Name>") and attach or link the relevant material.
- Where a session has a completion artifact (e.g. responsible-vendor certificate), note in the training plan that the certificate gets filed in `04 Training` and checked off on the tracker.
- Record each scheduled session and its date on the tracking item so training progress is visible.

If the connected calendar/training tools can't reach the trainer or the hire, schedule what you can, and list the gaps as `[TODO]` items on the tracker rather than skipping silently.

### 5. Set up HR & payroll

Create the employee in the HR/payroll system (Gusto) so pay, tax, and work records exist and tie back to the folder.

- Add the employee with their identity, work address/location, job title, and compensation per the confirmed terms.
- Trigger the system's own onboarding flow (self-setup for tax forms / direct deposit) where available, so the hire completes I-9/W-4/banking in the system of record; mirror copies into the folder for the audit trail.
- Confirm the start date and pay schedule match what the offer letter states — reconcile any mismatch with the user before finalizing.
- Note the Gusto employee record (and that payroll setup is started/complete) on the tracker. **Do not run payroll or finalize irreversible HR actions without the user's explicit go-ahead.**

### 6. Provision access & welcome

Get the hire ready to actually work on day one.

- Request/note the operational accounts the role needs (POS login, scheduling app, email/Slack if applicable) — create what you safely can and list the rest as `[TODO]` for the manager.
- If the team uses Slack, prepare a welcome message/intro for the hire's first day (draft, don't blast) and note the channels they should be added to.
- Record provisioning status on the tracker.

### 7. Confirm and report back

Only after the steps above, reconcile the tracker against the deadline and report to the user:

- The hire, role, start date, and the **fully-onboarded-by date**, with a clear on-track / at-risk call.
- The employee folder link and what's filed in it.
- Documents: sent / signed / outstanding (name the outstanding ones).
- Training: sessions scheduled with dates, and anything still unscheduled.
- HR/payroll: record created, what the hire still needs to complete in-system.
- Access/welcome: what's provisioned, what's pending.
- Every open `[TODO]` and who owns it, so the user knows exactly what's left to hit the deadline.

Mark the tracker `Complete` **only** when documents are signed, compliance items are satisfied, training is scheduled (or done), and HR/payroll is set up. Otherwise leave it `In progress` with the remaining items visible.

## Guardrails

- **Never fabricate signatures, completed forms, IDs, or compliance attestations.** Create drafts and capture real completions; mark everything else as outstanding.
- **Compliance items are gating.** Don't declare onboarding complete with age/ID verification, background-check authorization, I-9, or required state registration outstanding.
- **Sensitive data, least access.** The employee folder holds PII and legal records — grant access only to the hiring manager and HR, never the whole org, and never paste SSNs/IDs into chat, tasks, or messages.
- **No irreversible HR/payroll actions without explicit approval.** Creating drafts, folders, and calendar holds is fine; running payroll, sending an offer to the candidate, or finalizing tax filings needs the user's explicit go-ahead.
- **One trail per hire.** Everything routes back to the folder and the tracking record; if a step can't complete, log it as a visible `[TODO]` rather than dropping it.
- **Respect the deadline honestly.** If lead-time dependencies can't meet the requested date, say so when you set it up — don't promise a date the dependencies can't hit.
