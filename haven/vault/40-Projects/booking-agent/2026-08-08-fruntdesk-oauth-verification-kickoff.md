---
created: 2026-08-08T09:25:00-04:00
updated: 2026-08-08T10:07:00-04:00
domain: project
type: log
status: done
tags: [samira, booking-agent, fruntdesk, oauth, google, compliance]
source: slack
---

# FruntDesk — Google OAuth verification kickoff (legwork pass)

Executed the run:admin-3x prompt staged in #admin (ts `1786140910.703069`,
`task:20260807_fruntdesk-oauth-verification-kickoff`). Context: the FruntDeskHQ Google
OAuth app is still in Testing mode — the launch blocker flagged in the 2026-08-03
#fruntdesk update (anyone outside the test-user list gets blocked by Google on the
bio/signup link, and operator grants expire roughly weekly).

**Legwork only, as instructed — nothing submitted to Google, no privacy policy or ToS
drafted, no Instagram push.**

## What this pass could and couldn't do

Two of the requested checks hit tool gaps this session:

1. **Google Cloud Console (OAuth consent screen config)** — no connected tool/MCP gives
   this session access to Google Cloud Console. Pulling the current consent-screen
   config (app name, scopes requested, current verification status) needs Lemar signed
   into the dedicated FruntDeskHQ Google account directly.
2. **Live site check (fruntdeskhq.com)** — attempted to fetch `fruntdeskhq.com`,
   `/privacy`, and `/terms` via WebFetch to check for an existing privacy policy / ToS
   page. All three calls failed with `EGRESS_BLOCKED` (network policy blocks this
   domain from this session) — could not confirm live site content either way.

What follows is general, not a live read of FruntDesk's actual config or site.

## What Google's OAuth verification flow requires (general, well-established for
`calendar.events` scope apps)

- **App name + logo** on the OAuth consent screen (shown to users during consent).
- **Homepage URL** — must be a live, publicly reachable page describing what the app
  does (fruntdeskhq.com's landing page should satisfy this if it's live and describes
  the product — unconfirmed this pass, see gap above).
- **Privacy Policy URL** — required for any app requesting non-basic scopes; must be
  hosted at a live, publicly reachable URL, not just a document link.
- **Terms of Service URL** — recommended, sometimes required depending on scope
  sensitivity; `calendar.events` typically falls in Google's "sensitive scope" tier,
  which usually requires both a privacy policy and, in some review flows, a ToS.
- **Scope justification** — a written explanation of why the app needs
  `calendar.events` specifically (read/write calendar events) rather than a broader
  scope, and how it's used in-product. FruntDesk's existing design note already has
  this justification in substance (two-way sync to prevent double-booking) — it would
  need to be written up for the verification form itself.
- **Demo video** — for sensitive-scope apps, Google often requests a short screen
  recording walking through the OAuth consent flow and how the requested scope is used
  once granted. Not always required at first submission, but common as a follow-up ask.
- **Verification timeline** — typically days, not same-day; can extend to weeks if
  Google requests changes or additional evidence. Confirms the original flag that this
  needs to start well before any Instagram push.

## What's missing / blocking submission (best-effort, pending live confirmation)

Given the tool gaps above, this can't be stated with certainty — but the FruntDesk
project notes to date (`2026-07-15`, `2026-07-25`, `2026-07-27` notes in this folder)
never mention a privacy policy or ToS page being built or published. Working
assumption: **a privacy policy and ToS page are the most likely missing pieces**, since
nothing in this project's history shows either being drafted. This needs Lemar to
confirm directly (either by checking the live site himself or granting a tool access
path) before treating it as fact.

**Per the prompt's explicit instruction: no privacy policy or ToS was drafted this
pass** — that's a live product/legal commitment and needs Lemar's own review, not
something to originate unsupervised.

## Not done this pass (flagged back, not submitted)

- OAuth consent screen config was not pulled (no tool access).
- Live site content (privacy/ToS pages) was not confirmed (egress blocked).
- No privacy policy or ToS was drafted.
- Verification request was **not** submitted — per instruction, this stays
  ready-to-submit-pending-Lemar until he confirms the consent-screen state and either
  supplies or approves privacy policy / ToS content.

## Next action (for Lemar, not automatable this pass)

1. Confirm live: does fruntdeskhq.com currently have a Privacy Policy and Terms of
Service page? If not, those need to be written and published first.
2. Pull the current OAuth consent screen config from Google Cloud Console
   (FruntDeskHQ account) to see exactly what Google is asking for on this app
   specifically.
3. Once both are in hand, verification can be submitted (by Lemar, or by a future
   Samira pass if given the missing pieces).

## Sources
- slack: #admin (C0BBLUA7JLX), ts `1786140910.703069` (2026-08-08, run:admin-3x prompt)
- slack: #fruntdesk (C0BHXTPST52), ts `1785760498.492629` (2026-08-03, FruntDesk live
  update flagging OAuth Testing mode as the launch blocker)
- haven: `haven/vault/40-Projects/booking-agent/2026-07-25-phase1-foundations-design.md`
  (OAuth wiring plan, flagged Google Cloud Console setup as Lemar's direct action)
