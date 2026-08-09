---
created: 2026-08-09T08:07:00-04:00
updated: 2026-08-09T08:07:00-04:00
domain: project
type: task
status: active
tags: [booking-agent, fruntdesk, status-update, samira-capture]
source: slack
---

# Post a FruntDesk/#booking-agent status update — Lemar wants to push it forward today

Lemar dropped a request in the Samira capture DM: post an update in **#booking-agent**
(`C0BHXTPST52`, informally called #fruntdesk in project notes) on where the FruntDesk
booking-agent project stands, because he wants to start pushing it forward today.

## Where the project actually stands (per the vault, as of this capture)

- [[2026-07-15-booking-agent-barbers-tattoo-artists]] — original scope: booking
  assistant for solo appointment-based operators (barbers, tattoo artists, etc.),
  Basic vs Full-Featured tiers, dogfood pilots.
- [[2026-07-25-phase1-foundations-design]] — account/client/appointment schema, Google
  OAuth wiring plan.
- [[2026-07-27-fruntdesk-operator-onboarding-doc]] — operator welcome/onboarding guide
  drafted (status: active, still pending Lemar's review before it goes out to any
  operator).
- [[2026-08-08-fruntdesk-oauth-verification-kickoff]] — most recent pass (status:
  done, a legwork-only pass). **Current blocker:** the FruntDeskHQ Google OAuth app is
  still in Testing mode (only pre-approved test users can complete consent; operator
  grants expire roughly weekly) — this blocks any wider/Instagram push. That pass
  could not confirm (tool gaps: no Google Cloud Console access, fruntdeskhq.com
  egress-blocked) whether a Privacy Policy / Terms of Service page exists on the live
  site, which is very likely the missing piece for submitting OAuth verification.
  Two open items were kicked back to Lemar directly:
  1. Confirm live whether fruntdeskhq.com has a Privacy Policy + ToS page (write/publish
     if not).
  2. Pull the current OAuth consent screen config from Google Cloud Console
     (FruntDeskHQ account).

## This task

Post a status update to #booking-agent summarizing the above (scope locked, onboarding
doc drafted and awaiting Lemar's review, OAuth verification blocked pending the two
items above) and naming the concrete next step to push forward today: Lemar confirming
the privacy policy/ToS status and pulling the OAuth console config — both need his own
access, not automatable. Staged as a fenced `run:admin-3x` prompt to #booking-agent,
un-reacted (per PART B buffer — not for this run's PART C).

## Sources
- slack: Samira capture DM (`D0BHPKMDNEP`), ts `1786277255.214429` (2026-08-09, Lemar's
  raw capture: "Can you give me an update in the #booking-agent Slack channel about
  where we are in the process? I wanna start pushing that forward today.")
