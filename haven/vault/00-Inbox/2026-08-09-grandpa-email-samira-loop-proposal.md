---
created: 2026-08-09T09:12:00-04:00
updated: 2026-08-09T09:12:00-04:00
domain: personal
type: task
status: awaiting-decision
tags: [family, grandpa, samira-capture, new-surface, voice-profile]
source: slack
area: family
---

# Grandpa's affairs — proposal to create an email address and loop it into Samira

Lemar dropped a request in the Samira capture DM: his grandfather is getting older and
will need help with his affairs (applying for things, making sure accounts are
straight, getting information he needs). Lemar's idea: create an email address for his
grandfather, loop it into Samira so she receives the emails and helps with the needed
tasks, and have Samira draft the emails in Lemar's voice profile but under his
grandfather's name.

## Why this surfaces a decision rather than developing unattended

This is a request for a **new automation surface** (a new inbox Samira monitors,
possibly a new voice profile/identity distinct from Lemar's own, a new Gmail account
that only Lemar can actually create — Samira has no ability to create Google accounts).
It also touches an unattended-AI-acting-as-a-third-party's identity question (drafting
as the grandfather, not as Lemar) that the safety floor and voice-profile doctrine don't
currently cover. This is architecturally similar in shape to how Dawn/Basil/Stormy each
got their own bot identity and connector — not something to wire up mid-scan without
Lemar's explicit direction on scope, safety limits, and how much autonomy Samira should
have over a family member's affairs.

## Open questions for Lemar (options to pick from in #decisions)

1. Should this be built at all right now, or parked until after other priorities
   (Cuzzie's sale, the funding close, etc.)?
2. If yes: what's the email account (Lemar creates it — Samira cannot create Google
   accounts) and does Samira only **draft** for grandpa's review, or eventually send
   with a lighter touch than the current "never send" floor allows?
3. Does this need its own voice profile (grandpa's own voice, not Lemar's), and does it
   run inside Samira's existing hourly scan or as its own separate persona/routine
   (the Dawn/Basil/Stormy pattern)?

## Sources
- slack: Samira capture DM (`D0BHPKMDNEP`), ts `1786277537.216249` (2026-08-09, Lemar's
  raw capture: "My grandfather is getting older and is going to need help with his
  affairs... I think a lot of his problems would be solved with an email address...
  loop it into Samira... She'll even draft the emails for him using my voice profile
  but his name. Can we work out a system for this?")
