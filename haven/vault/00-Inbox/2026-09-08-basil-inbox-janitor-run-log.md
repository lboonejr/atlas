---
created: 2026-09-08T23:15:00-04:00
updated: 2026-09-08T23:15:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run log — 2026-09-08 (LIVE, DRY_RUN=false)

## Summary
- Vendor menus archived: **33**
- Threads trashed: **0**
- Threads over the trash cap: **0**

## PART A — vendor menus archived (labeled `Vendor Menus`, removed from `INBOX`)

Searched the inbox for the vendor-domain seed list (qccnj.com, verano.com, terrascend.com,
awholdings.com, apextrading.com subdomains, novafarms.com, northlake.supply,
thegardensociety.com, 1906.shop, etc.) plus menu-signal subjects carrying attachments.
Applied precision-first filtering: **excluded** collections notices, banking-info-change
notices, AR statements, and live back-and-forth conversation threads (e.g. the Hillary
King / laddsllc.com thread about the Camden closure, the Jersey Smooth "Net-60 Terms"
thread, the Garden Society collections notices) even though they matched a vendor domain,
because those are real business correspondence, not menu drops.

33 threads archived:

1. `1a07cb101db6af96` — little-leaf-labs.apextrading.com — "THE GROWFATHER IS BACK — 2G Vapes + Moonrock Pre-Rolls"
2. `1a07c7db07f321f9` — kbreiner@qccnj.com — "QCC NJ Menu 9.7.26"
3. `1a07c21a613438be` — nbonsanto@awholdings.com — "Ascend Updated Menu"
4. `1a063fe5d2e3a407` — maggie.boyd@verano.com — "End of Summer Savings!"
5. `1a062a2d56467829` — sfranco@1906.shop — "1906 Labor Day Stock Up"
6. `1a05d5d827736374` — the-happy-farmer-llc.apextrading.com — "Happy Farmer: Day Dreaming?"
7. `1a0595ae7d045a2b` — marketing.us@terrascend.com — "Kind Tree Pre-Roll 3-Packs"
8. `1a05951357707bef` — garden-state-exotix.apextrading.com — "A Sale in Paradise!"
9. `1a0588cedc82b043` — dan@northlake.supply — "Stock Up for Labor Day — New Drops"
10. `1a057972785e5d2e` — high-grass-farms.apextrading.com — "2G Rosin, new flower strains, now live"
11. `1a054d5c6c9f838b` — canfections-nj-llc.apextrading.com — "A Rare Sunday Night APEX Update!"
12. `1a0491a4bf9b184a` — bbreslow@novafarms.com — "Stashie: Hashables Mylar Moves & More"
13. `1a043b76ac692d4d` — garden-state-exotix.apextrading.com — "$3 Prerolls Now Available!"
14. `1a03ebbedfdaf28a` — njwholesale@thegardensociety.com — "Labor Day Offer: Buy 2 Get 1 Free"
15. `1a03e9bee6ea7cbd` — garden-state-exotix.apextrading.com — "Labor Day Deals Are Live!"
16. `1a038f8d95279c08` — marketing.us@terrascend.com — "Feel the Spectrum — NEW RSO Syringe"
17. `1a03577c858b4bfb` — bbreslow@novafarms.com — "Stashie: Gummy Power Play"
18. `1a03542c06afb883` — marketing.us@terrascend.com — "Cuue Meets Campfire — NEW S'mores"
19. `1a02466070c8aca6` — canfections-nj-llc.apextrading.com — "APEX Update! Test results: 61% THC"
20. `1a01c0cc5086d441` — maggie.boyd@verano.com — "Short Lifts are back!"
21. `1a01b30dbf828f5b` — dan@northlake.supply — "We just made ordering simpler"
22. `1a01afc9f58b14a0` — info@1906.shop — "One last chance at Bliss"
23. `1a0164342938e531` — sfranco@1906.shop — "Summer Sparkle with 1906"
24. `1a01564ad3fa8c7b` — the-happy-farmer-llc.apextrading.com — "Happy Farmer: Always Fresh!"
25. `19ffcd1f865bc897` — maggie.boyd@verano.com — "Essence Flower Sale!"
26. `19ff84ecb74ac5fc` — sfranco@1906.shop — "Stay Sharp with 1906"
27. `19ff0df34f939e6f` — marketing.us@terrascend.com — "Dessert is Served — Georgia Pie"
28. `19feb4ca99a21fab` — canfections-nj-llc.apextrading.com — "Monday morn' APEX Updates!"
29. `19fe9ddf315bbb6a` — info@1906.shop — "Better sleep changes everything"
30. `1a062a2b6f8f1296` — Sidney.Jenkins@ianthus.com — "Midweek MPX Menu"
31. `1a058db992c02389` — jshort@stashhousedistro.com — "Victory & Stash House Menu 8.31.26"
32. `1a04e92d1417d576` — charlie@day1distro.com — "EG Glass BACK IN STOCK"
33. `1a03581c8adb35a3` — jshort@stashhousedistro.com — "New Victory Menu 8.24"

**Flag for Lemar:** hundreds of older (>1yr) vendor-domain menu threads from 2025 are
still sitting in the inbox (sussexcultivation.com ONYX menus, stashhousedistro.com,
greenlightningcannabis.com, cannabistcompany.com, hamiltonfarms.com, and more, going
back to at least September 2025). They weren't archived tonight — PART A is scoped to
current/recent menus — and they didn't surface in tonight's PART B trash-candidate
query either, because Gmail apparently doesn't categorize most of them as
promotions/social/forums (likely `category:primary` or `category:updates`). Neither
part of the routine currently reaches this backlog. Worth a look: a future rule change
that searches the vendor-domain list directly + `older_than:1y` (regardless of
category) and archives those to `Vendor Menus` rather than trashing them.

## PART B — trash sweep

Query: `older_than:1y (category:promotions OR category:social OR category:forums)
-has:userlabels -is:starred -is:important`

Result: 22 candidate threads total (fully enumerated — no further pages). Every single
one was protected:
- 14 threads from `CTA@sos.nj.gov` — NEVER-TOUCH allowlist (`*.gov`)
- 6 threads from `parkebank@parkebank.com` — NEVER-TOUCH allowlist (`parkebank.com`)
- 1 thread (`surveys@dutchie.com`, "How was your implementation experience with
  dutchie?") — thread carries IMPORTANT-labeled messages, protected by the hard floor
- 1 thread (`sales@hamiltonfarms.com` / `dontebronaugh@gmail.com` /
  `breali@hamiltonfarms.com`, "Hamilton Farm's Weekly Menu & Go2 8ths release!") —
  thread carries IMPORTANT-labeled messages (active back-and-forth on order terms),
  protected
- 1 thread (`iccc@icic.org`, "Apply Now for the ICCC Program") — carries an
  IMPORTANT-labeled message, protected

**Result: 0 threads trashed.** No audit list needed — nothing moved to Trash tonight.
This is a correct outcome of the safety floor, not a bug: every disposable-category
candidate over 12 months old also happened to be either allowlisted or flagged
important.

## PART B (report-only) — old `category:updates` mail

`older_than:1y category:updates` returns 200+ threads (estimate capped at 201). This
category is explicitly report-only per the runbook — it mixes real financial/
operational mail with disposable notices, so it is never auto-trashed. Sender domains
Lemar may want to clear by hand: `jotform.com` / `jotformsign.com` (register-float
approvals & signed-form receipts — hundreds of threads), `headset.io` (scheduled
inventory/vendor reports), `softtouchpos.co` (POS batch/password notices),
`nytimes.com` / `theathletic` (news digests), `voice-noreply@google.com` (Google Voice
call/voicemail/text notifications), `notification.intuit.com` (old paid QuickBooks
invoices), `redditmail.com`, `checkr.com`, `weedmaps.com`, `mailva.evite.com`. No
action taken on any of these.

## Safety notes
- `DRY_RUN` was `false` — this was a live run.
- Nothing outside Gmail was touched. No email sent, replied to, or drafted.
- Nothing permanently deleted; Trash and Spam untouched.
- Per-run trash cap (200) not approached — 0 threads trashed.

## Sources
- gmail: 33 archived thread IDs listed above (account `lemar@cuzziesnj.com`)
- gmail: PART B candidate query, 22 threads evaluated, 0 trashed
