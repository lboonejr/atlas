---
created: 2026-07-27T23:07:00-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, vendor-menus, trash-sweep]
source: claude
---

# Basil — Inbox Janitor run 2026-07-27 (live)

Nightly Gmail cleanup on `lemar@cuzziesnj.com`, run live (`DRY_RUN=false`). Repo
`.claude/routines/inbox-janitor.md` executed top-to-bottom per anchors.

## Summary

- **PART A — vendor menus archived:** 200 threads. Matched on vendor-domain-seed-list
  AND an explicit menu-signal in the subject (menu/drop/price sheet/availability/live
  menu/in stock), scoped to the inbox. Labeled `Vendor Menus` (`Label_8`) and removed
  from `INBOX`. Nothing was trashed in this part.
- **PART B — old disposable mail trashed:** 164 threads. Gate: `older_than:1y` AND
  `category:promotions/social/forums` AND NOT `is:starred`/`is:important` AND sender
  domain NOT on the NEVER-TOUCH allowlist. All recoverable from Gmail Trash for 30 days.
  Well under the 200/run cap — no overflow.
- **`category:updates` (report-only, never auto-trashed):** roughly 200+ old threads,
  dominated by `info@headset.io` (Metrc-adjacent, allowlisted), `notification.intuit.com`
  (allowlisted), `no-reply@accounts.google.com` (allowlisted), plus high volumes of
  `noreply@jotform.com`/`jotformsign.com`, `breakingnews-noreply@nytimes.com`,
  `noreply@redditmail.com`, `TheAthletic@e1.theathletic.com`, `voice-noreply@google.com`,
  `workspace-noreply@google.com`, `feedback@slack.com`. Left untouched per the runbook —
  noted here as "old updates you may want to clear by hand."

## Notable finding for the operator

The PART A vendor-menu search matched a **backlog well beyond 200** — genuine vendor
menu/drop emails go back past 2025-07 in the inbox, likely because Cuzzie's operations
paused (temporarily closed 2026-06-13, per thread content found this run) and nobody was
clearing the inbox by hand before Basil started. Tonight's run capped PART A archiving
at 200 threads (newest-first) to avoid an unbounded first-catch-up sweep in one night; a
large remainder is still sitting in the inbox and will keep surfacing on subsequent
nightly runs. Recommend leaving the cap as-is and letting it drain over several nights
rather than raising it — there's no urgency constraint on archiving.

Also notable: on this account, nearly every message Gmail files under
`category:promotions/social/forums` also carries the `IMPORTANT` label (Gmail's
importance heuristic is very liberal here), so the "never touch important" hard floor
protects the large majority of that category automatically — only roughly 15-20% of
`older_than:1y` promotions/social/forums mail was actually trash-eligible tonight. This
is expected/correct behavior given the safety floor, not a bug — noting it so future
digests aren't a surprise when the trash count runs well below the archive count.

## Trash audit (PART B — recoverable from Gmail Trash for 30 days)

164 threads trashed, date range 2024-09-04 through 2025-07-26 (all `older_than:1y` from
run date). Representative senders/domains trashed tonight: `mail@email.adobe.com` /
`mail.adobe.com` (Photoshop/Acrobat tips + surveys), `microsoft.start@email2.microsoft.com`
(MSN "Start Daily" news digest), `email@mail.salesforce.com` (Dreamforce/Slack promo),
`marketing@leaflink.com`, `marketing@leaftrade.com`, `hello@flowhub.com`,
`marketing@engage.canva.com`, `contact@zapier.com` / `events@send.zapier.com` /
`learn@send.zapier.com`, `easyautopa@alstspecials.com` (Easy Auto car offers),
`HomeDepotCustomerCare@mg.homedepot.com` / `homedepotpro@mg.homedepot.com`,
`update@dotcards.net`, `peter@heartlandpayments.ccsend.com`,
`main-palmestatesco.com@shared1.ccsend.com` (small-biz funding spam),
`jenna@newjerseycannabusinessassociation.ccsend.com`,
`michelle-thinkcanna.com@cannaadvisors.ccsend.com`, `news@onfleet.com`,
`email@em.sherwin-williams.com`, `emily@supernormal.com`, `dayna@covasoftware.com`,
`2115@fastsigns.com`, `conceptsinconcrete-verizon.net@shared1.ccsend.com`,
`lewis@jotform.com` (non-important instances only), `BestBuy@email.bestbuy.com`.

Zero starred, important, or allowlisted-domain threads were trashed — each candidate was
checked against the NEVER-TOUCH allowlist and the `is:starred`/`is:important` hard floor
before the trash action. Full 164-thread ID list is in this run's tool-call transcript,
not duplicated here.

## Next steps for future runs

- PART A vendor-menu archiving has a large remaining backlog (pre-2025-07 menus still
  sit in the inbox) — expect continued high archive counts on the next several nightly
  runs until it drains.
- PART B trash-eligible volume should stay modest per run given how much of this
  account's promotions/social/forums mail is marked IMPORTANT.
- No allowlist or safety-floor issues encountered; no repo/tool errors this run.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox, live run 2026-07-27
