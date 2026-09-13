---
created: 2026-09-13T23:07-04:00
updated: 2026-09-13T08:04:00-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup]
source: claude
---

# Basil — Inbox Janitor run — 2026-09-13 (LIVE)

Account: lemar@cuzziesnj.com. Executed per `.claude/routines/inbox-janitor.md` (main,
`DRY_RUN=false`).

## PART A — vendor menu archiving

- Query: `in:inbox has:attachment (subject:menu OR subject:availability OR subject:"live menu" OR subject:"price sheet" OR subject:drop OR subject:"in stock")`, paginated fully (8 pages, 351 threads reviewed — Gmail's `resultCountEstimate` under-reported the true total).
- **Archived: 321 threads** — labeled "Vendor Menus" (`Label_8`), removed `INBOX` label. Never trashed.
- **Left alone: 30 threads**:
  - 24 matched a pre-vetted exclusion list built from manual review (real order-placement/negotiation/agreement/collections/account-setup correspondence, or false keyword matches — an employee shift-availability request, a Dropbox link, a Canva notification).
  - 6 more caught by the same judgment rule on new candidates (genuine vendor back-and-forth about an order, inventory, discount, or a signed supply agreement): Garden Greens "Last Menu Of The Week" (`198610644b1a80c3`), OGeez! "Inventory & Latest Menu" (`197fa45aa72b20ff`), Grön Edibles "Fresh Menu" discount discussion (`197563c92397080a`), Panda Farms supply-agreement signing (`19722b4c984d27cf`), Neptune's Garden May Menu order (`196fdeb7f512f200`), plus one more surfaced during review.
  - 1 flagged ambiguous, left in inbox for Lemar: thread `198377f4ee828baa` ("Cannabist x Old Pal July Wholesale Giveaway, mid-week menu update, NEW SKUS RELOADED!!" from Andrew.Moyer@cannabistcompany.com) — mostly a routine menu blast, but a second message in the same thread announces a **banking-info change**. Left untouched rather than risk burying a banking notice — **needs a human look**.
- One transient tool error on thread `19837ac6f0c682ad`, succeeded on retry — no lingering issue.

## PART B — trash sweep (old, clearly unnecessary mail)

- Query: `older_than:1y (category:promotions OR category:social OR category:forums) -is:starred -is:important`. Full result set: 26 candidate threads (well under the 200/run cap and the 3000-scan safety bound).
- **Trashed: 4 threads** (recoverable in Gmail Trash for 30 days). Full audit list:

  | threadId | subject | sender | date |
  |---|---|---|---|
  | `1993e0d1336ca1bc` | Act Now: RI Social Equity Applicant Status Certification Now Open | michelle-thinkcanna.com@cannaadvisors.ccsend.com | 2025-09-12T13:10:52Z |
  | `1993e19afbd00378` | Authorized Dealer has Friday deals for you! | sales-authorizeddealernj.com@shared2.ccsend.com | 2025-09-12T13:24:51Z |
  | `1993e3a13208ae63` | Become a Flowhub Certified Budtender 🎓 | hello@flowhub.com | 2025-09-12T14:00:16Z |
  | `1993f438ad8330e1` | Protect your stack without writing more code | team@m.ngrok.com | 2025-09-12T18:50:14Z |

- Left for next run due to cap: 0.
- Rejected candidates: 22 of 26 — 3 for a starred/important message elsewhere in the thread (Gmail thread-vs-message label quirk, caught by checking real `labelIds` rather than trusting the query alone); 19 for the NEVER-TOUCH allowlist (11 `*.gov`/NJ CTA newsletter threads, 8 `parkebank.com` threads).
- Self-check passed: none of the 4 trashed threads were starred/important, none carried a protective label, all were >12 months old, none matched the allowlist.

## Report-only (no action taken) — `category:updates older_than:1y`

Rough count: ~201 threads. Sample sender domains for Lemar to review by hand: `google.com` (Google Voice), `jotformsign.com`/`jotform.com`, `fedex.com`, `nytimes.com`, `checkr.com`, `headset.io`, `readyrefresh.com`, `theathletic.com`, `redditmail.com`, `sos.nj.gov`, `linqapp.com`, `revelrysupply.com`, `messaging.squareup.com`, `distru.com`, `surfside.io`.

## Items for Lemar to double check

- Thread `198377f4ee828baa` (Cannabist banking-info-change addendum inside a menu thread) — left in inbox, may need action on the new banking info.
- The three Part B important/starred catches were correctly protected; worth tightening the search query itself in a future tuning pass, since `-is:important` alone isn't sufficient given Gmail's thread-vs-message label behavior.

## Sources
- gmail: live sweep of lemar@cuzziesnj.com, run 2026-09-13 ~11pm ET
