---
created: 2026-08-03T00:00-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-03

Live run (`DRY_RUN=false`), continuing from [[2026-08-02-basil-inbox-janitor-run]],
[[2026-08-01-basil-inbox-janitor-run]], [[2026-07-31-basil-inbox-janitor-run]],
[[2026-07-30-basil-inbox-janitor-run]], and [[2026-07-29-basil-inbox-janitor-run]].
Account: `lemar@cuzziesnj.com` (the only connected Gmail account; Drive out of scope).
Archived 45 vendor-menu threads out of the inbox and trashed 1 old promotional thread
(recoverable in Gmail Trash for 30 days). Both stayed well under their per-run caps and
respected the NEVER-TOUCH allowlist and the starred/important floor from
`.claude/anchors.md`.

## PART A — vendor menus archived (45)

Query: `in:inbox` combined with the vendor-domain seed list (201 estimated matches),
then narrowed with `has:attachment` plus a subject/snippet menu-signal filter (menu,
price sheet, live menu, availability, "full menu", "current menu", "updated menu").
Worked through the first page of that narrowed result set. Each candidate was checked
against the thread content and excluded if it was really a payment/relationship
negotiation from a vendor domain rather than a one-way menu/promo blast. All 45
qualifying threads were labeled `Vendor Menus` (`Label_8`) then had `INBOX` removed —
recoverable in All Mail under that label, nothing was trashed.

Senders included: TerrAscend, Jersey Smooth, Nova Farms, Harvest Moon Farms, Garden
Society, AW Holdings, Fresh Cannabis/Fresh Grow, Verano, Parks Grove, and Prolific
Growhouse — recurring one-way wholesale menu/price-sheet/promo mailings.

Excluded on purpose (left in inbox, untouched — mixed menu content with real business
correspondence): `199a6b63230ce362` (freshcannabis.co — "Fresh Grow Check In," a
relationship check-in, not a menu blast), `19784a0fdc96260e` (freshcannabis.co — "Fw:
Fresh Wholesale," an active pricing confirmation with Lemar/Joshua), `1973718381615071`
(northlake.supply — "North Lake Supply Inventory," includes a remittance-info request),
`1963567a0c6cc3c4` (prolificgrowhouse.com — "2025 Partnership," live sample-delivery
scheduling). A large residual backlog of vendor-domain mail remains in the inbox by
design — the rest of the 201-estimate search pool (further pages) plus AR statements,
past-due notices, and other financial correspondence that are not menus and should stay
visible. Future runs will keep working through the backlog.

Archived thread IDs:
19fa562475f81775, 19e88f2be9d22afe, 19e6f65c3055c31e, 19e64f79639ebc05, 19e64f4897312160,
19e50dd00bb67795, 19e4b9d362eafe4b, 19e4187f1b2a8412, 19e3bdd71c8f2b09, 19e2c8ac4d3cf48b,
19de3bb0a8ef8ae5, 19dda85677cc66bc, 19dbaf7dbe616b89, 19d8793d579e535d, 19d77e12d0b6696b,
19d6e0ec2079a1cd, 19d654ccce0c5e54, 19d5f38202bfce2d, 19d359e3ceec0987, 19d24de1bef39c5b,
19cf848975d80bc5, 19cd8cb0928a81ae, 19caea32c319e815, 19c342c2dc7cc13a, 19aeaa174eb6d4a2,
19ab6a315185a3f1, 197f03193989a612, 199c5d8ce1520bff, 196a23b516c2b097, 196a0c034ddc7309,
1968d468a866cbbf, 1966d68bcc87c5fa, 1966874e7a82fbd5, 1965937023ec8116, 19644ae1482ac5af,
19635e7cedc3b837, 1962005d7f23f07e, 1961151efe2b6889, 195fc8245d3dc278, 195d87640dd54def,
195b48df59d55ca8, 195a51f769111449, 1959070c03349453, 1958b587a438d89d, 19585d43bdd99ac0,
1955c868c10fe9e2.

## PART B — trash sweep (1 trashed, recoverable 30 days)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)
-is:starred -is:important`. 18 threads matched. Reviewed every one individually because
Gmail's thread-matching still surfaces threads containing an IMPORTANT-flagged message
even under `-is:important`. Only 1 passed every gate.

| # | Thread ID | Subject | Sender | Date |
|---|---|---|---|---|
| 1 | 1986c52f84e7dc74 | "Last weekend to save big during the Best Buy Outlet Event" | BestBuy@email.bestbuy.com | 2025-08-02 |

Skipped (17): 6 threads from `CTA@sos.nj.gov` (protected — `*.gov` allowlist entry), 6
threads from `parkebank@parkebank.com` (protected — `parkebank.com` allowlist entry), 1
`surveys@dutchie.com` thread (contains IMPORTANT-flagged messages), 1
`sales@hamiltonfarms.com` "Hamilton Farm's Weekly Menu & Go2 8ths release!" thread
(contains an IMPORTANT-flagged reply — live order-terms correspondence with Donte
Bronaugh, not disposable), 1 `iccc@icic.org` thread (contains an IMPORTANT-flagged
message), and 1 `Gunter_Greenhalgh@intuit.com` thread (protected — `intuit.com`
allowlist entry). 0 threads hit the 200/run cap.

## `category:updates` — report-only (never auto-trashed)

~201 threads (estimate, capped) older than 1 year sit in `category:updates` in the
inbox. Per the runbook this category is never swept. Sample sender domains seen:
`voice-noreply@google.com`, `no-reply@accounts.google.com`, `payments-noreply@google.com`,
`notification.intuit.com` / `notifications.intuit.com` (QuickBooks — allowlisted),
`headset.io` (allowlisted), `jotform.com` / `jotformsign.com`, `no-reply.ecommerce@fedex.com`,
`breakingnews-noreply@nytimes.com`, `noreply@redditmail.com`, `messaging.squareup.com`,
`mcafee.com`, `invoicing@found.com`, `readyrefresh.com`, `hamiltonfarms.com`,
`adtcontrol.com`, `cannazipbags.com`, `linqapp.com`, `theathletic.com`. Worth a hand
pass if Lemar wants this folder thinned — none of it was touched tonight.

No email was sent or drafted. No Trash was emptied, no Spam applied. No account other
than `lemar@cuzziesnj.com` was touched. Nothing starred/important/user-labeled or newer
than 12 months was archived or trashed.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox — search_threads / label_thread / unlabel_thread /
  apply_sensitive_thread_label, run 2026-08-03
