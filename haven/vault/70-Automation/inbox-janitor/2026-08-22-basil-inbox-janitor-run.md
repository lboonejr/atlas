---
created: 2026-08-22T23:07-04:00
updated: 2026-08-22T23:25-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-22

## Run summary
- Date: 2026-08-22 (~11pm ET scheduled run)
- Mode: LIVE (`DRY_RUN = false`)
- Account acted on: lemar@cuzziesnj.com
- Scope: Gmail only. Google Drive out of scope (no move/delete/trash tools connected).

## PART A — Vendor menus archived (53)
Candidate generation via domain-only matching pulled in a lot of noise tonight (AR statements,
collections notices, invoices, event invites — all from vendor domains but not menus), so the
search was tightened to require an explicit menu/price-sheet/availability/live-menu signal in
the subject or snippet, each confirmed to carry an attachment, before archiving (labeled
`Vendor Menus`, removed from `INBOX`):

1. `1a025afd2063936d` novafarms.com — "Step Into a World of Sweet Savings🍫" — 2026-08-21
2. `1a01a93a65ba64cd` harvestmoonfarmsnj.com — "🔥 Mid-Week Wholesale Update" — 2026-08-19
3. `1a010a5a6bae0e80` novafarms.com — "The Sweetest deal in NJ" — 2026-08-17
4. `1a0253f936fa5de2` kushilabs.com — "Kushi Labs: Levia Seltzers... Plus This Week's Menu" — 2026-08-21
5. `1a024f0ce3167640` harvestmoonfarmsnj.com — "🔥 Friday Wholesale Menu" — 2026-08-21
6. `1a024bb9bf837516` kivaconfections.com — "Kiva Camino/Lost Farm Menu" — 2026-08-21
7. `1a0248b63b564f45` awholdings.com — "Ascend Updated Menu" — 2026-08-21
8. `1a02489be9494c12` budsgoods.com — "Bud's Goods Menu" — 2026-08-21
9. `1a01001f018e87d0` brutesroots.com — "Fresh Menu! 8/17" — 2026-08-17
10. `19ff61e30ee93e86` canopy-usa.com — "Wana x Botanist x Superflux Menu" — 2026-08-12
11. `19fec00ff0109df2` (personal gmail sales rep) — "New Contract: Triple G Labs... 30% Off menu" — 2026-08-10
12. `19c4898632fba687` eatgron.com — "Grön Edibles Fresh Menu" — 2026-02-10
13. `19bec22f99248bc0` hamiltonfarms.com — "HF Fresh Menu 1.23.26" thread — 2026-01-23
14. `19bd729bb62378a3` mb1flower (gmail) — "Delight & KAI signed WSA and menu" thread — 2026-01-19
15. `19bb2eb1f280d474` cannabistcompany.com — "Cannabist menu - Limited Amount of $10 8ths!" — 2026-01-12
16. `19b242cb11714dd3` humblecamp.com — "Its Cold outside but our Menu is Hottt!!!!" — 2025-12-15
17. `19afefe335306724` eatgron.com — "Grön Edibles Fresh Menu" — 2025-12-08
18. `19ac1fe348800314` sunextractions.com — "Meeting Recap- Menu Info" — 2025-11-26
19. `19a0bf4d394bac67` greenlightningcannabis.com — "Green Lightning Menu: New Rosin Strains" — 2025-10-22
20. `19a07db4b08602c0` mbcannabisco.com — "Mudd Brothers Menu 10.21.25" — 2025-10-21
21. `19a07746b4df9a2b` ogeezbrands.com — "OGeez! Halloween Orders... Latest Menu" — 2025-10-21
22. `19a0760caa55e746` eatgron.com — "Grön Edibles Fresh Menu" — 2025-10-21
23. `19a02b094ab28ff5` cannabistcompany.com — "Monday Menu, New Strains" — 2025-10-20
24. `19a026570e6d896a` sunextractions.com — "Live Menu" — 2025-10-20
25. `19a023fc44efa3c6` stashhousedistro.com — "Monday Menu!!" — 2025-10-20
26. `19a02318176daf12` stashhousedistro.com — "Victory Flower is About to Hit the Menu!" — 2025-10-20
27. `19a0205119f9f91f` hamiltonfarms.com — "Hamilton Farm's Weekly Menu & Strain Releases" — 2025-10-20
28. `19a02020d6591415` ianthus.com — "MPX Monday Menu" — 2025-10-20
29. `19a0183ce6689ccd` greenlightningcannabis.com — "Green Lightning Menu: Spritzer is Back!" — 2025-10-20
30. `199f7ed86ee37f1c` sussexcultivation.com — "ONYX Menu 10.18.25" — 2025-10-18
31. `199f2b8919955628` greenlightningcannabis.com — "Green Lightning Weekend Edition Menu" — 2025-10-17
32. `199ede1bc78190a2` sussexcultivation.com — "ONYX Menu 10.16.25" — 2025-10-16
33. `199eda362f9bfbd7` stashhousedistro.com — "Victory Flower is About to Hit the Menu!" — 2025-10-16
34. `199ed95c236224da` ggcann.com — "Garden Greens Menu" — 2025-10-16
35. `199e7df2a1a94644` greenlightningcannabis.com — "Green Lightning Menu: Rosin, Shake, Sugar" — 2025-10-15
36. `199e32fae60539bb` nextlevelbrands.net — "Next Level Brands Menu" — 2025-10-14
37. `199e309352f3d336` hamiltonfarms.com — "Hamilton farms Weekly Menu & Strain drops!" — 2025-10-14
38. `199e302ba30a3839` mbcannabisco.com — "Mudd Brothers Menu 10.14.25" — 2025-10-14
39. `199de5d1feb3e010` sussexcultivation.com — "ONYX Menu 10.13.25" — 2025-10-13
40. `199de0c73dfdb845` ianthus.com — "10.13 MPX Menu" — 2025-10-13
41. `199dda1975c1e84e` greenlightningcannabis.com — "Green Lightning Menu: Big Bud 3.5g SALE" — 2025-10-13
42. `199ceb04d081f545` sussexcultivation.com — "ONYX Menu 10.10.25" — 2025-10-10
43. `199c4aa8d5f39da5` sussexcultivation.com — "ONYX Menu 10.8.25" — 2025-10-08
44. `199c402f5ed85509` eatgron.com — "Fresh Menu From Grön Edibles" — 2025-10-08
45. `199c3fdee2e2286e` greenlightningcannabis.com — "Green Lightning Menu: 7g Popcorn Tiered Pricing" — 2025-10-08
46. `199c01c8f8e193fc` hamiltonfarms.com — "Hamilton Farms Weekly Menu & Strain release" — 2025-10-07
47. `199becda84e7fb8d` mbcannabisco.com — "Mudd Brothers Menu 10.07.25" — 2025-10-07
48. `199ba8bc3a57ff44` sussexcultivation.com — "ONYX Menu 10.6.25" — 2025-10-06
49. `199ba645df679e61` gtigrows.com — "GTI Menu Highlights & DEALS!!" — 2025-10-06
50. `199b9dcf70130edf` greenlightningcannabis.com — "Green Lightning Menu: SAVE THE DATE" — 2025-10-06
51. `199aae5f4bb77b1c` hamiltonfarms.com — "Hamilton Farm's New Release Menu" — 2025-10-03
52. `199aa35909d8340c` sussexcultivation.com — "ONYX Menu 10.3.25" — 2025-10-03
53. `199a5fdf8fca0fb4` ggcann.com — "Garden Greens End of week Menu" — 2025-10-02

Explicitly left alone (same domains, not menus): AR/collections statements and past-due notices
(Verano, Garden Society, Prolific Growhouse, QCC), invoices and payment-instruction threads
(Bud's Goods, Jersey Smooth, Illicit Gardens delivery notices), OOO notices, event/pop-up
invitations, onboarding/intro emails, and banking-info-change notices. A much larger pool of
vendor-domain hits remains in the inbox for future nightly runs — tonight's batch was capped at
a manageable size given the scale of this backlog (21,789 inbox threads, 11,259 unread).

## PART B — Trash sweep (5 threads)
All older than 12 months, `category:promotions`, no starred/important/genuine-filing-label
protection, sender not on the NEVER-TOUCH allowlist. Recoverable from Gmail Trash until
~2026-09-21 (30-day window).

1. `198cec1ccdbddeed` — "Lemon Cherry Pie & More!" — wholesale@verano.com — 2025-08-21
2. `198ce3e3a569624a` — "NJ: Millville Applications About To Drop For Dispensary Licenses" — Julian@cd.cdre.co — 2025-08-21
3. `198cdc373eb3554e` — "Nimbus Got the 1g Disposables You Need!" — andrew@northlake.supply — 2025-08-21
4. `198cd5d1c7a31041` — "🚨 New Minnesota Adult-Use Licenses Now in Emerald Intel" — jenny@emeraldintel.ai — 2025-08-21
5. `198cd32ae9e5fe79` — "Is Your Cannabis Coverage Ready for the Second Half of 2025?" — info@alpharoot.com — 2025-08-21

No threads hit the 200/run cap.

### Skipped candidates (20 of the 25 initial matches) — allowlist/important tuning record
- 9 threads from `CTA@sos.nj.gov` — skipped, `*.gov` is on the NEVER-TOUCH allowlist
- 8 threads from `parkebank@parkebank.com` — skipped, `parkebank.com` is on the NEVER-TOUCH allowlist
- 1 thread (dutchie.com implementation survey, `19644c6a0e498f47`) — skipped, thread carries IMPORTANT-labeled messages
- 1 thread (Hamilton Farms Go2 8ths release → real correspondence with Donte re: order terms, `196110a96c91e798`) — skipped, genuine business correspondence plus IMPORTANT-labeled messages present
- 1 thread (ICIC mini-MBA program, `1826944b41c19b7a`) — skipped, thread carries an IMPORTANT-labeled message

Same pattern as recent nights — the allowlist and the IMPORTANT-guard are both catching real
cases every run since these senders keep sending. No changes needed to either list tonight.

## category:updates — report only, never auto-trashed
201+ threads older than 12 months sit in `category:updates`. Per the runbook this category is
never swept automatically (invoices/bank/payroll/legal mixed with ads). Sender domains worth a
manual look if Lemar wants to clear some by hand: `nytimes.com` (breaking-news/from-the-times
alerts, high volume), `jotform.com`/`jotformsign.com` (form/sign notifications), `voice-noreply@
google.com` (Google Voice notices), `headset.io` (scheduled reports, allowlisted), `notification.
intuit.com`/`intuit.com` (QuickBooks, allowlisted), `notifications@monday.com`, `theathletic.com`,
`redditmail.com`, `adt.com`, `pseg.com`, `paymentus.com`.

## Notes
- No sends, replies, or drafts — Basil never takes an outward-facing action.
- Nothing starred, marked important, or user-labeled was touched.
- PART A's candidate query needed tightening mid-run (see above) — future runs should keep the
  subject/snippet menu-signal requirement rather than relying on vendor-domain match alone, which
  produces too many false positives (invoices, AR statements) to be precise.

## Sources
- gmail: 53 threads archived to `Vendor Menus` (Label_8), 5 threads trashed — thread IDs above
