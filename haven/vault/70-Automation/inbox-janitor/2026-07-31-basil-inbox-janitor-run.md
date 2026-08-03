---
created: 2026-07-31T23:07-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-31

Live run (`DRY_RUN=false`), continuing from [[2026-07-30-basil-inbox-janitor-run]],
[[2026-07-29-basil-inbox-janitor-run]], and [[2026-07-28-basil-inbox-janitor-run]].
Account: `lemar@cuzziesnj.com` (the only connected Gmail account; Drive out of scope).
Archived 43 vendor-menu threads out of the inbox and trashed 1 old promotional thread
(recoverable in Gmail Trash for 30 days). Both stayed under their per-run caps and
respected the NEVER-TOUCH allowlist and the starred/important floor from
`.claude/anchors.md`.

## PART A — vendor menus archived (43)

Query: `in:inbox -label:Label_8 has:attachment` combined with (a) the anchors
vendor-domain seed list and (b) a broader subject/content menu-signal search (`menu`,
`drop`, `wholesale`, fresh pricing) to also catch vendor blasts from domains not yet on
the seed list. Each candidate was individually reviewed and excluded if it carried a
STARRED message, or if the thread showed an active back-and-forth (a `SENT` reply from
Lemar) rather than a one-way vendor blast — those read as live conversations worth
keeping visible, not disposable menu noise, even though the runbook doesn't explicitly
gate on that signal. 43 of the reviewed candidates qualified and were labeled
`Vendor Menus` (`Label_8`) then had `INBOX` removed.

13 senders that qualified are **not yet on the anchors.md vendor-domain seed list**
(matched purely by content signal): `ianthus.com`, `culture-craft.com`,
`hillviewmed.com`, `cannabistcompany.com`, `greenlightningcannabis.com`,
`hamiltonfarms.com`, `kushilabs.com`, `ggcann.com`, `sussexcultivation.com`,
`stashhousedistro.com`, `nextlevelbrands.net`, `pancann.com`, `ogeezbrands.com`.
Flagging for Lemar to consider adding — Basil does not self-edit anchors per the
runbook's tuning note ("widen them there, never here, as Lemar names more senders").

Full thread ID / subject / sender / date (all recoverable — labeled, not trashed):

| # | Thread ID | Subject | Sender | Date |
|---|---|---|---|---|
| 1 | 19fb3c7056fbc6e1 | TerrAscend Menu - Last Call! | ndesiderio@terrascend.com | 2026-07-30 |
| 2 | 19fae2cedafcdcc8 | QCC NJ Menu 7.29.26 - NEW Promo Unit Incentives | kbreiner@qccnj.com | 2026-07-29 |
| 3 | 19fae3f66f26d6d7 | Re: MPX Menu Re-Fresh | Sidney.Jenkins@ianthus.com | 2026-07-29 |
| 4 | 19faa21836c0e662 | Fresh Drop Alert: Green Crack x Baja Blast | info@culture-craft.com | 2026-07-28 |
| 5 | 19fa893b711467ad | Hillview NEW PRICING NEW DROP SUPER RUNTZ | Chris@hillviewmed.com | 2026-07-28 |
| 6 | 19fa46cb435973fb | FRESH DROP: Local Skunk | Sidney.Jenkins@ianthus.com | 2026-07-27 |
| 7 | 19fa3fb4d8c650c7 | Hillview NEW PRICING NEW DROP (dup send) | Chris@hillviewmed.com | 2026-07-27 |
| 8 | 19c29f09debb3327 | Cannabist Menu - Don't Let the Cold Temps Keep You Down | chelsey.shindler@cannabistcompany.com | 2026-02-04 |
| 9 | 19c28d7138cea674 | Green Lightning Menu: Black Cherry Gelato & Chimax | miles@greenlightningcannabis.com | 2026-02-04 |
| 10 | 19c2476884aba20c | Kushi Labs: Building Bigger Baskets This Winter x Fresh Menu | sales@kushilabs.com | 2026-02-03 |
| 11 | 19c23fed5d5509e9 | NEW Back on the Menu Alert! Super Boof / Blue Lobster | Chris@hillviewmed.com | 2026-02-03 |
| 12 | 19c204a6fb9f726a | Cannabist Menu - Groundhog Day! | chelsey.shindler@cannabistcompany.com | 2026-02-02 |
| 13 | 19c2031e92f9fe4b | Victory Natural Farms & Stash House Menu * NEW REP ALERT | ncohen@stashhousedistro.com | 2026-02-02 |
| 14 | 19c1f35acb76389d | Garden Greens Official Price Drop + Suggested MSRP | loudpacklu@ggcann.com | 2026-02-02 |
| 15 | 19c1ebfcca602a9a | iAnthus 2/2 Menu | Sidney.Jenkins@ianthus.com | 2026-02-02 |
| 16 | 19c1e817502c7773 | Green Lightning Menu: Black Maple & Sour Diesel | miles@greenlightningcannabis.com | 2026-02-02 |
| 17 | 19c101e89fccd45b | Green Lightning Weekend Menu | miles@greenlightningcannabis.com | 2026-01-30 |
| 18 | 19c0fd3ac6f15357 | OGeez! Feb Menu, Promos, Big Sativa RSO Pre-orders | mtomasetto@ogeezbrands.com | 2026-01-30 |
| 19 | 19c0f95e0af632d2 | HF Fresh Menu 1.30.26 | gcorchado@hamiltonfarms.com | 2026-01-30 |
| 20 | 19c0bb3690c9fbeb | Garden Greens Final Menu of the Week | loudpacklu@ggcann.com | 2026-01-29 |
| 21 | 19c0a64feea3dfa5 | New ONYX Menu Drop! | pdemuro@sussexcultivation.com | 2026-01-29 |
| 22 | 19c066781b1359d2 | Cannabist Menu - Don't Let the Winter Make You Blue | chelsey.shindler@cannabistcompany.com | 2026-01-28 |
| 23 | 19c057fd221cf820 | Garden Greens Updated Menu | loudpacklu@ggcann.com | 2026-01-28 |
| 24 | 19c04b8409eff1a7 | Green Lightning Menu: Leiffa Rosin & Strike Vape Restock | miles@greenlightningcannabis.com | 2026-01-28 |
| 25 | 19c02279d76328a0 | Hillview Menu - 1.27 | TJ@hillviewmed.com | 2026-01-28 |
| 26 | 19c0052c23d2c9bd | HUGE NEW ONYX DROP! | pdemuro@sussexcultivation.com | 2026-01-27 |
| 27 | 19c000040ee6f28b | Kushi Labs: Winter 2026 Menu Update + Delivery Availability | sales@kushilabs.com | 2026-01-27 |
| 28 | 19bfb7c676a2877a | Cannabist Menu - Enjoy the snow day! | chelsey.shindler@cannabistcompany.com | 2026-01-26 |
| 29 | 19bfb69592ef254a | Garden Greens Menu | loudpacklu@ggcann.com | 2026-01-26 |
| 30 | 19bfb47a30c7ee57 | Victory Natural Farm & Stash House Menu 1/26/26 | ncohen@stashhousedistro.com | 2026-01-26 |
| 31 | 19bfb3d7e5b9c108 | HF Fresh Menu 1.26.26 | gcorchado@hamiltonfarms.com | 2026-01-26 |
| 32 | 19bfafee62afb205 | 1.26 Menu: Gorilla Glue Rosin, Hashburger & Shatter | Sidney.Jenkins@ianthus.com | 2026-01-26 |
| 33 | 19bfafe5b585b04d | Humble Camp Menu - Edie P and Revelry/Field Trip | julien@humblecamp.com | 2026-01-26 |
| 34 | 19bfa9ab33b77410 | Green Lightning SNOW DAY Menu | miles@greenlightningcannabis.com | 2026-01-26 |
| 35 | 19bebae22f1b1a83 | 1.23 MPX Menu: FRÜTFUL Launch + Shatter Re-Stocked | Sidney.Jenkins@ianthus.com | 2026-01-23 |
| 36 | 19beb05c6aa25aab | Green Lightning Weekend Menu: Pre-Rolls Are Back! | miles@greenlightningcannabis.com | 2026-01-23 |
| 37 | 19be671a810469bd | Garden Greens End Of Week Menu | loudpacklu@ggcann.com | 2026-01-22 |
| 38 | 19be0f40cff77e9f | Green Lightning Menu: Ridiculous GRUV Rosin Promo! | miles@greenlightningcannabis.com | 2026-01-21 |
| 39 | 19bdd5bf1eed1b24 | Next Level Brands Wholesale Menu - 1.20 | tj@nextlevelbrands.net | 2026-01-20 |
| 40 | 19bdd52163d27ed2 | PanCann Wholesale Menu - 1.20 (GUMMIES & VAPES) | tj@pancann.com | 2026-01-20 |
| 41 | 19bdd4bca3f92265 | Hillview Wholesale Menu - 1.20 | TJ@hillviewmed.com | 2026-01-20 |
| 42 | 19bd798187bcf87e | Garden Greens Menu - Wholesale Rep | loudpacklu@ggcann.com | 2026-01-19 |
| 43 | 19bd73a9e1724d92 | OGeez! Latest Menu & January Promos | mtomasetto@ogeezbrands.com | 2026-01-19 |

## PART B — trash sweep (1 thread)

Query (matching the runbook's literal example, no `in:inbox` restriction, per the
convention [[2026-07-30-basil-inbox-janitor-run]] established): `older_than:1y
(category:promotions OR category:social OR category:forums) -is:starred -is:important`
plus explicit `-from:` exclusions for the allowlist domains. Confirmed via a post-trash
re-run of the same query that the candidate pool is otherwise exhausted — only 3 threads
remained, all correctly excluded (see below) — so tonight's yield was genuinely just the
one new item that accumulated since 07-30's sweep cleared the backlog.

Trashed (recoverable in Gmail Trash for 30 days):
1. `1985c1228f163266` · "Unlock new business opportunities" · noreply@mail.lendistry.com · 2025-07-30

Skipped despite matching the category/age filter — each contains an `is:important`
message elsewhere in the thread even though the query's own `-is:important` didn't
catch it (Gmail's thread-level exclusion is imperfect, so every candidate is individually
re-checked before acting):
- `19644c6a0e498f47` · surveys@dutchie.com implementation survey
- `196110a96c91e798` · sales@hamiltonfarms.com weekly menu / order-minimum thread
- `1826944b41c19b7a` · iccc@icic.org "mini-MBA" program pitch

0 threads over the 200/run cap.

## Report-only: `category:updates` (never auto-trashed)

~201 threads older than 12 months in `category:updates` — not touched, per the runbook.
Dominant sender: `voice-noreply@google.com` (Google Voice missed-call/voicemail
notices — very high volume, flagged on every prior run too). Also present:
`jotform.com`/`jotformsign.com` operational-form receipts, `breakingnews-noreply@nytimes.com`,
`headset.io` and `quickbooks@notification.intuit.com` (both already allowlisted),
`redditmail.com`, `theathletic.com`, `readyrefresh.com`, `no-reply@accounts.google.com`
(allowlisted security alerts). Lemar may want to clear these by hand or tune upstream
notification settings — Google Voice in particular keeps coming up as the single
biggest contributor across every run so far.

## Next run

`DRY_RUN` stays `false`. Part A still has more of the seed-list backlog to work through
(tonight's batch pulled mostly from January–February 2026 vendor blasts); Part B's
candidate pool is confirmed exhausted under the current query, so future nights should
mostly reflect ordinary daily accumulation rather than a large backlog catch-up.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox, live sweep 2026-07-31
- related: [[2026-07-30-basil-inbox-janitor-run]] (previous night's run)
- related: [[2026-07-29-basil-inbox-janitor-run]]
- related: [[2026-07-28-basil-inbox-janitor-run]] (first live run)
