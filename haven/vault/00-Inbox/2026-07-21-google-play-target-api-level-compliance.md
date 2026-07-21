---
created: 2026-07-21T18:15-04:00
updated: 2026-07-21T18:15-04:00
domain: cuzzies
type: task
status: active
tags: [app, google-play, compliance, android, technical-debt]
source: gmail
due: 2026-08-31T00:00-04:00
---

# Google Play — target API level compliance for the Cuzzie's app

Google Play Console sent an automated (no-reply) compliance notice: the Cuzzie's
Android app ("Cuzzie's Disp. and Delivery") targets an old Android API level. Google
Play requires all apps to meet target API level requirements **before Aug 31, 2026**
or risk removal/restriction from the Play Store. The fix is a technical app update
(target the latest Android version), not an email reply — there's no person to
respond to.

Flag: Cuzzie's business is slated to wind down mid-2026 (per `.claude/anchors.md`
Identity section — "do not build on it"). The Aug 31, 2026 deadline falls after that
window, so this may already be moot. Surfacing to Lemar rather than silently
dropping it or guessing whether it's worth actioning, since there's no clear
execution owner in scope (no app-dev channel/role) and it touches the winddown
timeline call.

## Sources
- gmail: thread `19f869c28d894371` — "[Action required] Your app is affected by
  Google Play's target API level requirements", no-reply-googleplay-developer@google.com,
  2026-07-21 21:36 UTC
