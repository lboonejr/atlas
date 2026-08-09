---
created: 2026-07-27T08:25-04:00
updated: 2026-08-09T18:45:00-04:00
domain: project
type: reference
status: active
tags: [booking-agent, fruntdesk, onboarding, docs]
source: slack
---

# FruntDesk — Operator Welcome & Onboarding Guide

Welcome to FruntDesk. This guide will get you from "I just signed up" to "my calendar is
protected and I'm approving my first bookings," in plain terms — no tech background
needed.

## What is FruntDesk?

FruntDesk is a booking assistant built for solo, appointment-based operators — barbers,
tattoo artists, independent mechanics, and similar one-person businesses. It doesn't
replace you and it doesn't book anything without your say-so. Its job is to:

- Catch booking requests wherever your customers already reach you (email, the form in
  your bio, and soon Instagram DM).
- Check your real calendar so you never get double-booked.
- Propose times back to the customer.
- Ask **you** to approve or decline before anything is final.

There is no separate app your customers have to download. They message you the same way
they always have — FruntDesk just reads that message and does the calendar legwork
behind the scenes.

## How the booking flow works, day to day

Here's what a typical request looks like once you're set up:

1. **A request comes in.** A customer emails your business address, fills out the
   booking form linked in your social bio, or (once Instagram DM support is live) DMs
   you on Instagram.
2. **FruntDesk reads it and checks your calendar.** It figures out what the customer is
   asking for and looks at your actual Google Calendar to find times that work — it
   won't propose a time that conflicts with something already on your calendar,
   including stuff you added yourself by text or phone call.
3. **FruntDesk proposes times.** It responds to the customer with a couple of options
   that fit your schedule.
4. **You get an approval prompt on your phone.** Before anything is locked in, you get a
   notification asking you to approve or decline the proposed booking. Nothing goes on
   your calendar without your tap.
5. **You tap Approve or Decline.**
   - **Approve** — the appointment is confirmed, it's added to your Google Calendar, and
     the customer is notified.
   - **Decline** — the request is turned down (or you can suggest different times,
     depending on what's supported in your version).

This is called **approve-first**: you are always the last check before a booking is
final. Nothing ever auto-books itself onto your calendar without you tapping approve.

A note on your version: FruntDesk ships in two tiers. The **Basic tier** covers calendar
sync, client and appointment tracking, and reminders — no payment collection. The
**Full-Featured tier** adds deposit/no-show fee collection and deeper client history on
top of that. Your invite will tell you which tier you're on.

## Getting started — onboarding steps

### 1. Connect your Google Calendar

FruntDesk needs read/write access to your Google Calendar so it can see what's already
booked and add new appointments once you approve them.

- You'll get a link to Google's standard consent screen. Sign in with the Google account
  that holds your real calendar and click through to grant access.
- **If you're one of our early pilot operators:** the app is currently running in
  Google's "testing mode." That means only a short, pre-approved list of test users
  (you and the FruntDesk team) can complete this consent screen. If you get a warning
  that the app isn't verified, that's expected during the pilot — it does not mean
  anything is broken. Full public verification happens later, once FruntDesk opens
  beyond the pilot.
- Once connected, FruntDesk will keep reading and writing to that calendar
  automatically — you don't need to reconnect it unless you revoke access on Google's
  side.

### 2. Set up your intake channels

This is how customers reach you and how FruntDesk catches the request.

- **Business email** — the email address you already use for customer inquiries. Make
  sure it's the one you give FruntDesk, since that's the inbox it will monitor.
- **Bio form** — a simple booking-request form we'll give you a link to. Put that link
  in your Instagram/social bio in place of (or alongside) your usual "DM me to book"
  text.
- **Instagram DM (coming soon)** — a fast-follow after launch. It needs its own approval
  from Instagram's business messaging platform, so it isn't available on day one. We'll
  let you know the moment it's ready — no action needed from you until then.

You only need email and the bio form live to start taking real bookings through
FruntDesk.

### 3. What to expect in your first week

- Your first few requests will come in exactly like any other week — customers email
  you or use the bio form like normal.
- You'll start getting phone approval prompts instead of having to manually check your
  calendar and reply. Get in the habit of checking those promptly so customers aren't
  left waiting.
- Keep using your calendar normally for anything booked outside FruntDesk (walk-ins,
  phone calls, texts) — FruntDesk reads those too, so it won't double-book over them.
- If a proposed time doesn't work, decline it — don't just ignore the prompt. That keeps
  the customer from being left hanging.
- It's normal for the first week to feel like you're double-checking FruntDesk's work.
  That's expected — once you've seen it get your schedule right consistently, most
  operators relax into just tapping approve.

### 4. Who to contact with issues

If anything looks wrong — a proposed time that conflicts with something on your
calendar, a missed request, a customer saying they never heard back, or the Google
consent screen giving you trouble — reach out directly to Lemar. Don't wait on it;
early pilot feedback is exactly what shapes the next round of fixes.

---

*This is a draft for Lemar's review before it goes out to any operator. Flag anything
that needs a tone change, missing step, or correction.*

## Update — 2026-08-09
Ran the staged admin-3x prompt (`task:20260809_booking-agent-onboarding-guide-link`,
posted in #admin per Lemar's ask in #booking-agent, "Can you surface the operator
onboarding guide as a link via Google Docs?"). A Google Doc with this note's exact text
already existed in Drive (`FruntDesk — Operator Welcome & Onboarding Guide`, doc id
`15V42U3b4HmQmXRMn7hfNGdgzfizw4BJLImUa618ZrMg`, created earlier today) but its link had
never been posted anywhere. Posted the link to #booking-agent (ts `1786306503.409249`),
still flagged as a draft awaiting Lemar's review — nothing sent to any operator.

## Sources
- slack: #booking-agent (C0BHXTPST52), ts `1785153440.871199` (2026-07-27, Lemar's
  project update + the two asks — official FruntDesk name, approve-first flow
  confirmation, intake channels, OAuth testing-mode note); ts `1786290984.451329`
  (2026-08-09, Lemar's ask to surface the doc link); ts `1786306503.409249` (link posted)
- slack: #admin (C0BBLUA7JLX), ts `1786299308.546229` (staged admin-3x prompt, ✅'d)
- drive: doc `15V42U3b4HmQmXRMn7hfNGdgzfizw4BJLImUa618ZrMg` (FruntDesk operator
  onboarding guide, matches this note's text verbatim)
- haven: `haven/vault/40-Projects/booking-agent/2026-07-15-booking-agent-barbers-tattoo-artists.md`
  (product scope, tiered Basic/Full-Featured plan, dogfood pilots)
- haven: `haven/vault/40-Projects/booking-agent/2026-07-25-phase1-foundations-design.md`
  (account/client/appointment schema, Google OAuth wiring plan, scope decisions)
