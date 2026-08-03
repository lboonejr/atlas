---
created: 2026-07-25T23:07-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail, cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-25 (LIVE, DRY_RUN=false)

Nightly Gmail cleanup on the connected account (`lemar@cuzziesnj.com`), executed per
`.claude/routines/inbox-janitor.md`. First live run (DRY_RUN flipped to false).

## Summary

- **Mode:** LIVE
- **PART A (vendor menus):** archived **190** vendor-menu threads out of the inbox —
  labeled `Vendor Menus` (`Label_8`), removed `INBOX`. Selected on subject containing
  "menu"/"price sheet"/"in stock" combined with a vendor-domain sender from the seed
  list in anchors.md. Never trashed.
- **PART B (trash sweep):** trashed **69** threads that were `older_than:1y`, in
  `category:promotions`/`social`/`forums`, not `is:important`, not `is:starred`, and
  whose sender domain is not on the NEVER-TOUCH allowlist. Per-run cap of 200 was not
  reached.
- **Skipped from archiving (PART A):**
  - `19b8eacc72ca13b3` — "Bud's Goods Menu - Week of 1.5" — STARRED, left alone
  - `19b6bd13917342e8` — "⛽️🔥 Illicit Menu -📉 20% off 7G" thread — contains a nested
    overdue-balance/collections conversation ($3,360.07 past due, payment-plan
    negotiation) — left alone out of caution even though the thread subject reads as
    a menu
- **Skipped from trashing (PART B):** the large majority of `promotions`/`social`/
  `forums` candidates examined were protected — most frequent-vendor marketing mail in
  this inbox is auto-flagged `IMPORTANT` by Gmail, and a smaller set were shielded by
  the NEVER-TOUCH allowlist (`parkebank.com`, `fundcanna.com`, `intuit.com` /
  `notification.intuit.com`, `stellaconnect.net`, `sos.nj.gov` / `*.gov`). This is worth
  Lemar knowing: the IMPORTANT-guard is catching almost everything, which is why the
  live trash count (69) is much smaller than the vendor-menu archive count (190).
- **`category:updates` (report-only, never auto-trashed):** large recurring volume of
  NYT breaking-news alerts (`breakingnews-noreply@nytimes.com`), Jotform/JotformSign
  signature notifications, Slack system notifications, Reddit mail, and Distru
  menu-portal mail, mixed in with legitimate DocuSign/Intuit/FedEx/Headset.io records.
  Flagged here for Lemar to clear by hand if he wants to — not touched by this routine.

## Trash audit — recoverable in Gmail Trash for 30 days (thread ID · subject · sender · date)

| Thread ID | Subject | Sender | Date |
|---|---|---|---|
| 1983eac0888f3405 | 🏆 Each Week, New Ways to Win. | info@fernway.com | 2025-07-24 |
| 1983e56bf0a1c9c7 | ⏳ Croptober is just 6 weeks away — Are you fully staffed? | marketing@vangst.com | 2025-07-24 |
| 192fcdb0f73d04bb | Explore Small Business Programs Now Available | main-palmestatesco.com@shared1.ccsend.com | 2024-11-05 |
| 192fcc04b55483a6 | Full Spectrum, High Tech, Great Flavor | marketing@leaftrade.com | 2024-11-05 |
| 192fcae34b55e550 | Election Day 2024: Live results and analysis | microsoft.start@email2.microsoft.com | 2024-11-05 |
| 192f9259afdcf2eb | Camden Apothecary | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-11-04 |
| 192f9087b871bb4d | You don't want to miss out! | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-11-04 |
| 192f87c66023d93d | Take full advantage of your membership | mail@email.adobe.com | 2024-11-04 |
| 192f80d7ebaf9ffa | Updated Inventory - North Lake Supply | dan@northlake.supply | 2024-11-04 |
| 192f809ca59d134b | Vote for Cannabis | hello@flowhub.com | 2024-11-04 |
| 192f7eebf187aa21 | This expires on November 11... Big savings are here | email@em.sherwin-williams.com | 2024-11-04 |
| 192f7daa895f16a3 | Your custom dot.cards are 30 days away – order now! | update@dotcards.net | 2024-11-04 |
| 192f7b317caa518a | 🎄 Create custom gifts they'll love this holiday season | marketing@engage.canva.com | 2024-11-04 |
| 192f7b0d0f4b2bbd | Don't Let Crime Threaten Your Cannabis Business | info@alpharoot.com | 2024-11-04 |
| 192f77ccc628fd91 | Introducing Effin' Edibles! | marketing@leaftrade.com | 2024-11-04 |
| 192f54dc854ab3dd | [Nov 13 Office Hours] Learning about ngrok | team@m.ngrok.com | 2024-11-04 |
| 192ecdb4c4667a5c | GET READY FOR FALL CLEANUP SEASON | salexander-vhrrental.com@voorheeshardware.ccsend.com | 2024-11-02 |
| 192eab18287cc9c8 | Get a head start on the holidays | mail@email.adobe.com | 2024-11-02 |
| 192e9ec7fa4da830 | Sesh Together is HERE. | info@fernway.com | 2024-11-01 |
| 192e94d9b6bce333 | You don't want to miss out! | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-11-01 |
| 192e8081e0b7e021 | Small Business Programs Available Now | main-palmestatesco.com@shared1.ccsend.com | 2024-11-01 |
| 192e5109c575a8a8 | What do you hope to get out of VeriScan? | hello@idscan.net | 2024-11-01 |
| 192e406a87f0970b | Your next great idea? Find it here | no-reply@announce.fiverr.com | 2024-10-31 |
| 192e33b33809bdd0 | What's New in Supernormal: October 2024 | emily@supernormal.com | 2024-10-31 |
| 192e31d71847ca27 | Stay Ahead: Cannabis Consumer Preferences Unveiled | areiman@newfrontierdata.com | 2024-10-31 |
| 192e2b6e4cf0bae0 | Supreme Court's conservative justices leave in place Virginia's purge | microsoft.start@email2.microsoft.com | 2024-10-31 |
| 192deeeb8d0f7ff6 | Killing it in the Dispensary Game: The Monster House Story | dayna@covasoftware.com | 2024-10-30 |
| 192dee0350391dd1 | Time to get personal… recommendations! | no-reply@announce.fiverr.com | 2024-10-30 |
| 192dedc91e1fb93f | Don't Let Payment Disruptions Cost You Revenue | marketing@treez.io | 2024-10-30 |
| 192dea4663de1624 | what we're most excited about MJBizCon 2024 | hligon@idscan.net | 2024-10-30 |
| 192de9ee46a17df0 | Managing too many tools? Slack has everything you need | email@mail.salesforce.com | 2024-10-30 |
| 192de8886fadfa72 | Missed It? AlphaRoot's Referral Program Is Here! | info@alpharoot.com | 2024-10-30 |
| 192de64e1b628459 | [Webinar invitation] Build your business command center with Zapier | events@send.zapier.com | 2024-10-30 |
| 192ddf68d494e819 | Unlock More Before Your Spend Resets | homedepotpro@mg.homedepot.com | 2024-10-30 |
| 192dd7d5bcb8dd53 | You recently bought Southwire... Tell us about it! | HomeDepotCustomerCare@mg.homedepot.com | 2024-10-30 |
| 192dd36aeacfd7e6 | Happy Diwali from Spokes Digital! | leeza.thomas@spokesdigital.us | 2024-10-30 |
| 192d9e3aeae74541 | Your custom dot.cards are 30 days away – order now! | update@dotcards.net | 2024-10-29 |
| 192d9b9caab23e17 | Leave the freelancer hiring and execution to us. | no-reply@announce.fiverr.com | 2024-10-29 |
| 192d982ec06cd517 | What's New with Cannabis and Hemp in New Jersey? | jdallis@cannabizalerts.com | 2024-10-29 |
| 192d97f437b9177f | Updates and More! | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-29 |
| 192d97e4353de78f | Track changes with suggestion mode | marketing@engage.canva.com | 2024-10-29 |
| 192d8ac86113a404 | Check Out These Tools You'll Use From Start To Finish | email@em.sherwin-williams.com | 2024-10-29 |
| 192d8946d82ea274 | Small Business Programs Available Now | main-palmestatesco.com@shared1.ccsend.com | 2024-10-29 |
| 192d870893fa6984 | Israel bans UNRWA, the U.N. relief agency for Palestinian refugees | microsoft.start@email2.microsoft.com | 2024-10-29 |
| 192d5145eca5fb91 | Elevate Your Halloween Marketing with 10 Spooktacular AIQ Segments | noreply@alpineiq.com | 2024-10-28 |
| 192d49365b593c21 | Work with reliable, vetted freelancers. | no-reply@announce.fiverr.com | 2024-10-28 |
| 192d4167e3465c39 | Industry Updates and More! | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-28 |
| 192d35322005055d | 2024 election updates: Trump concludes MSG rally | microsoft.start@email2.microsoft.com | 2024-10-28 |
| 192d352c4ce409b0 | Hey You! Saddle Up for Marketing Success | brittanie@thrivepop.com | 2024-10-28 |
| 192d33a739aaa5c3 | Enhance Your Dispensary's Inventory Efficiency | marketing@treez.io | 2024-10-28 |
| 192cf6cfe80ccf4c | Get access to vetted freelancers & expert guidance. | no-reply@announce.fiverr.com | 2024-10-27 |
| 192ce262212ffbf1 | Harris regains slight lead nationally yet Electoral College holds the cards | microsoft.start@email2.microsoft.com | 2024-10-27 |
| 192ca0ffc9b5577b | Complete your order today | no-reply@announce.fiverr.com | 2024-10-26 |
| 192c8f7f0dd75977 | D.A. backs resentencing Menendez brothers | microsoft.start@email2.microsoft.com | 2024-10-26 |
| 192c57fa03f9a31a | This Sunday In Atlantic City NJ: Sustainability & Spirits | local@localcontent.com | 2024-10-25 |
| 192c4a3c0c7be676 | Surprise: $15 off Your Next Purchase to Get You Closer to Bronze | homedepotpro@mg.homedepot.com | 2024-10-25 |
| 192c3ff0666dc396 | Small Business Programs Available Now | main-palmestatesco.com@shared1.ccsend.com | 2024-10-25 |
| 192c3dcff6c6d790 | D.A. backs resentencing Menendez brothers (dup) | microsoft.start@email2.microsoft.com | 2024-10-25 |
| 192c054e754943a2 | Animation and resizing made easy | mail@email.adobe.com | 2024-10-24 |
| 192c01cbe688c920 | You don't want to miss out! | jenna@newjerseycannabusinessassociation.ccsend.com | 2024-10-24 |
| 192bf75041a49412 | If You Only Vote for One POS This Year, Make it Cova! | dayna@covasoftware.com | 2024-10-24 |
| 192bf127354e904c | Grow in-store sales with integrated retail solutions | marketing@dutchie.com | 2024-10-24 |
| 192bec49d2a3943e | Free trial—Chrome extension for cannabis industry data | john@emeraldintel.ai | 2024-10-24 |
| 192beb64f3622651 | Harris slams Trump as a 'fascist' during town hall | microsoft.start@email2.microsoft.com | 2024-10-24 |
| 192beae905b5f112 | BOGO 25% Off Verano Gummies! | marketing@leaftrade.com | 2024-10-24 |
| 192be76bb16f49fc | [2025 Trends] Marketing Tricks & Treats | brittanie@thrivepop.com | 2024-10-24 |
| 192bafb3e4deb176 | Delivered Digest: This email contains a prize | news@onfleet.com | 2024-10-23 |
| 192ba9337ce4298c | More than 200,000 organizations rely on Slack for greater productivity | email@mail.salesforce.com | 2024-10-23 |
| 192ba5e47e0397c7 | Last Chance: See how Jardín is driving 50-100% higher AOV with TreezPay | marketing@treez.io | 2024-10-23 |
| 192b9e95cd3edf90 | Discover the Secrets to Retail Success \| FASTSIGNS | 2115@fastsigns.com | 2024-10-23 |

## Notes for next run

- Roughly ~30 more vendor-menu threads (subject:menu, matching vendor domains) remain
  further back in the inbox (older than mid-October 2025) — left for a future nightly
  run rather than exhausting the search tonight.
- The IMPORTANT-guard is doing a lot of protective work in this inbox; if Lemar wants a
  more aggressive trash sweep, the tunable lever is the allowlist / IMPORTANT-guard
  discussion in the runbook, not this note.

## Sources
- gmail: 190 archived threads (Vendor Menus / Label_8), 69 trashed threads (see audit
  table above) — connected account lemar@cuzziesnj.com
- claude: automated nightly Basil routine run, `.claude/routines/inbox-janitor.md` on
  `lboonejr/atlas`, 2026-07-25

## Update 2026-07-26 — filed by vault-keeper
Lemar answered the Haven Inbox card ("I guess I would say this is personal", #decisions
ts `1785093845.026949`), resolving the blank `domain` field. Filed to `10-Personal/`
per that answer.
