---
created: 2026-08-07T23:12-04:00
updated: 2026-08-07T23:12-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Inbox Janitor run — 2026-08-07 (second run, same night)

Basil's nightly Gmail cleanup, run live (`DRY_RUN = false`) against `lemar@cuzziesnj.com`.

**Anomaly:** this is a **second Inbox Janitor run on the same calendar night.** A prior run
already landed as `haven/vault/70-Automation/inbox-janitor/2026-08-07-inbox-janitor-run.md`
(captured 2026-08-06T23:13-04:00, filed by vault-keeper the morning of 2026-08-07). This run
started at 2026-08-07T23:12-04:00 — only minutes after the prior run's own timestamp pattern,
suggesting the nightly `RemoteTrigger` (`trig_01JE6TpvqAnawkETpx64vvX9`) may have fired twice
for the same night, or fired on a schedule that lands two nights in close succession. No
overlap occurred in practice — every thread this run touched was independently re-verified
in Gmail as still `INBOX`/not-yet-trashed immediately before acting, so nothing was
double-processed — but the trigger cadence is worth Lemar checking.

## PART A — Vendor Menus (archived out of inbox)

5 threads archived to the `Vendor Menus` label (`Label_8`) and removed from `INBOX`,
each verified against domain + subject/snippet menu signal + attachment or in-body menu
content, none starred/important:

1. Thread `19fde0d4e1fe0ec0` — "Fresh Grow Menu | Infused Pre-Rolls Coming Soon + Beach Walkers Restocked 🔥" — Kathy@freshcannabis.co — 2026-08-07
2. Thread `19fddb8e4f7523a0` — "Fresh Drops Have Landed – Check Out the New Parks Grove Menu" — kellie@parksgrove.com — 2026-08-07
3. Thread `19fdc8c28f35dfb7` — "Updated Ascend Menu | New RSO Gummies + Sativas!" — nbonsanto@awholdings.com — 2026-08-07
4. Thread `196fd55b747a29fe` — "Fresh Ascend Drops Just Landed – Let's Get You Stocked Up" — nbonsanto@awholdings.com — 2025-05-23
5. Thread `19fdcc36a812f5a2` — "Bud's Goods / New Strains Just Dropped — Bud's Flower Is Stacked 🌿🔥" — bsantos@budsgoods.com — 2026-08-07

A broad domain+keyword scan returned ~201 loose matches; narrowed to these 5 on attachment
or clear in-body menu content. Everything else scanned (wholesale-agreement negotiations,
onboarding threads, invoice/WSA correspondence, promo teasers without an actual menu, a
starred vendor-menu-process thread) was skipped as only weakly matching the menu signal —
precision over recall, per the runbook.

## PART B — Trash sweep (older_than:1y, promotions/social/forums)

Base candidate query (`older_than:1y AND (category:promotions OR social OR forums)`)
returned **~201 threads**. Narrowing to `NOT is:important NOT is:starred` at the query
level dropped that to **23** — the rest were already excluded by Gmail's own IMPORTANT/
STARRED marks. Of those 23, **6 threads passed every remaining gate and were trashed**
(recoverable in Gmail Trash for 30 days):

1. Thread `19886db69b93fa5a` — "Everyone deserves a gateway: AI frontend builders, local APIs... and you" — team@m.ngrok.com — 2025-08-07
2. Thread `198866382c3f92c0` — "Bits BOGO!" — wholesale@verano.com — 2025-08-07
3. Thread `1988621c8843934f` — "🔥 Introducing the High / Culture Collection..." — info@fernway.com — 2025-08-07
4. Thread `19885782b479ab07` — "ZapConnect 2025: Your cheat sheet for scaling AI" — events@send.zapier.com — 2025-08-07
5. Thread `19884d0727c15f58` — "Thanks for choosing Extra Space Storage!" — extra_space@birdeye.com — 2025-08-07
6. Thread `1988469ba1213afc` — "Sydney Sweeney's American Eagle ad is just her latest controversial project" — fromthetimes-noreply@nytimes.com — 2025-08-07

**17 of the 23 skipped**, all for hard-floor reasons — none trashed:
- 7 threads from `parkebank@parkebank.com` — on the NEVER-TOUCH allowlist.
- 7 threads from `CTA@sos.nj.gov` — `*.gov` is on the NEVER-TOUCH allowlist.
- 3 threads (dutchie.com implementation-survey thread `19644c6a0e498f47`, Hamilton Farms
  weekly-menu/order-minimum thread `196110a96c91e798`, ICCC/icic.org mini-MBA thread
  `1826944b41c19b7a`) — each carries at least one message labeled `IMPORTANT`, even though
  a different message in the same thread matched the promo/social/forums search. Hard
  floor: never touch a thread that contains a starred/important message anywhere in it.

0 threads hit the 200/run cap — nothing left over for tomorrow.

`category:updates` is report-only per the runbook (never auto-trashed): **~201 threads**
older_than:1y in `category:updates` were counted but not touched. Sample sender domains for
Lemar to clear by hand if he wants: `mail.hellosign.com`, `e.progressive.com` (Progressive
Commercial), `box.com`, `jotform.com`/`jotformsign.com`, `monday.com` notifications,
`email.extraspace.com`, `e1.theathletic.com`, `trustaltus.com`. (`notification.intuit.com`,
`headset.io`, and `pactsafe.com` also appear here but are on the NEVER-TOUCH allowlist and
were never candidates for trashing.)

## Recovery

Everything trashed tonight sits in Gmail Trash for 30 days and can be restored via the
6 thread IDs listed above.

## Sources
- gmail: 5 threads archived (Vendor Menus), 6 threads trashed — IDs listed above
- prior run tonight: `haven/vault/70-Automation/inbox-janitor/2026-08-07-inbox-janitor-run.md`
