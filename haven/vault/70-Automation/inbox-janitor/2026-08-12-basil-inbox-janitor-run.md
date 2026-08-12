---
created: 2026-08-12T00:07-04:00
updated: 2026-08-12T09:06-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

**Mode:** Live (DRY_RUN=false)
**Account:** lemar@cuzziesnj.com

## PART A — vendor menus archived: 7

Applied `Vendor Menus` label (`Label_8`) and removed from INBOX. The domain-based candidate
search surfaced ~200 threads from vendor-seed-list domains, but the large majority were AR
statements, collections notices, overdue-invoice threads, banking-info-change notices, event
invites, and onboarding correspondence — **not** menu blasts. Per the runbook's "precision
over recall" rule, only unambiguous single-message bulk menu broadcasts (no active Lemar
correspondence in-thread, not starred) were archived:

1. `19ff291943594226` — allanf@harvestmoonfarmsnj.com — "🔥 Fresh Drops Are Live – It's Time to Rock" (2026-08-11)
2. `19ff248579fb6aa2` — Kathy@freshcannabis.co — "Fresh Grow Menu | Summer Sale – Beach Walkers Buy 2, Get 1 Free!🌴" (2026-08-11)
3. `19ff1d2ba6f7efe4` — tj@arescanna.com — "Hillview Menu - Best Blue Dream Flower in Jersey" (2026-08-11)
4. `19fecc79173c4949` — jshort@stashhousedistro.com — "New Victory & Stash House Menu 8.10" (2026-08-10)
5. `19fec9dcaf6bd576` — Sidney.Jenkins@ianthus.com — "MPX Monday Menu - RAINBOW BELTS 3.0 IS BACK! 🎉" (2026-08-10)
6. `19a0d9bfbb224809` — tj@nextlevelbrands.net — "Nxt Lvl Wholesale Menu - 10.22" (2025-10-22)
7. `19a0d1601c2fa46b` — Andrew.Moyer@cannabistcompany.com — "Mid Week Menu Update" (2025-10-22)

## PART B — trash sweep: 5 threads trashed (>12mo old, category:promotions/social/forums)

Reviewed 100 candidate threads across two pages of
`older_than:1y (category:promotions OR category:social OR category:forums)`. The
overwhelming majority (~95/100) were excluded because they carry Gmail's auto-applied
`IMPORTANT` label or `STARRED` flag, or the sender domain is on the NEVER-TOUCH allowlist
(verano.com, apextrading.com subdomains, fundcanna.com, parkebank.com, sos.nj.gov,
intuit.com, and stellaconnect.net all showed up repeatedly as IMPORTANT-tagged or
allowlisted and were skipped). Only 5 threads cleanly passed every gate (not starred, not
important, no genuine filing label, sender domain not on allowlist):

1. `1989b431e56875f3` — wholesale@verano.com — "National Wellness Month" (2025-08-11)
2. `1989aa22c15a9d9f` — BestBuy@email.bestbuy.com — "👍 GOOD news - drumroll please, Best Buy Tech Fest is here!" (2025-08-11)
3. `1989a47d76322059` — refreshment@hello.readyrefresh.com — "Your Summer BOGO Just Arrived" (2025-08-11)
4. `1989a0550224ed02` — andrew@northlake.supply — "Let's Talk Value - August Deals to Keep Products Affordable" (2025-08-11)
5. `19899d40cbd7646e` — sales@hamiltonfarms.com — "Hamilton Farms Weekly Menu & Huge Announcement!" (2025-08-11)

All 5 recoverable from Gmail Trash for 30 days from tonight. Well under the 200/run cap —
no threads left over.

Skipped-for-protection counts (approximate, from the 100 reviewed): ~85 skipped for
`is:important`, ~3 for `is:starred`, ~7 for NEVER-TOUCH allowlist domain (fundcanna.com,
parkebank.com, sos.nj.gov, intuit.com, stellaconnect.net).

### category:updates (report-only, never auto-trashed)

~201 old `updates`-category threads exist. Sender domains worth a manual look:
`voice-noreply@google.com` (Google Voice missed-call notices), `noreply@mail.hellosign.com`
(Dropbox Sign signed-doc receipts), `nytimes.com` (news digests), `noreply@jotformsign.com`
(signed-form receipts), `no-reply@email.figma.com` (Figma invites). `info@headset.io` also
appears here but is on the NEVER-TOUCH allowlist, so left untouched regardless.

## Note for Lemar

The vendor-domain seed list produces heavy false-positive noise for PART A (mostly
AR/collections/invoice threads, not menus). Worth tightening PART A's search query to
explicitly exclude subjects containing "invoice", "past due", "AR statement",
"collections", "overdue" if this keeps happening, to reduce manual review overhead on
future runs.

## Sources
- gmail: lemar@cuzziesnj.com inbox, live sweep 2026-08-12
