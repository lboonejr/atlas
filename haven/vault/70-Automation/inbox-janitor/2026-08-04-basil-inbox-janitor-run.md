---
created: 2026-08-04T00:15-04:00
updated: 2026-08-04T00:15-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-08-04

Live run (`DRY_RUN=false`), continuing from [[2026-08-03-basil-inbox-janitor-run]].
Account: `lemar@cuzziesnj.com` (the only connected Gmail account; Drive out of scope).
Archived 51 vendor-menu threads out of the inbox and trashed 1 old promotional thread
(recoverable in Gmail Trash for 30 days). Both stayed well under their per-run caps and
respected the NEVER-TOUCH allowlist and the starred/important floor from
`.claude/anchors.md`.

## PART A — vendor menus archived (51)

Query: `in:inbox` + subject contains a menu signal (menu / price sheet / live menu /
menu drop / wholesale menu) + `has:attachment`, restricted to the vendor-domain seed
list (53 matches). Excluded 2 threads that matched the search but were genuine business
correspondence, not recurring vendor blasts: `1953984f582708f1` ("Update on Vendor Menu
Submissions" — contains a STARRED message, a WSA/onboarding exchange with TerrAscend's
Nikki Desiderio) and `18bba3d6fdd56769` ("Current wholesale menu?" — a live onboarding
price negotiation with Ascend/awholdings from the pre-CRC-approval period).

All 51 qualifying threads were labeled `Vendor Menus` (`Label_8`) then had `INBOX`
removed — recoverable in All Mail under that label, nothing was trashed. Senders
included: Verano, Harvest Moon Farms, Bud's Goods, TerrAscend, QCC NJ, Kiva
Confections/Camino/Lost Farm, Ascend/AW Holdings, Fresh Cannabis/Fresh Grow, and
Prolific Growhouse — recurring one-way wholesale menu/price-sheet mailings spanning
2024-05 through 2026-08-03.

Archived thread IDs:
19fc9bbaba02044d, 19fc8e4eb4b1b266, 19fc8b603bd2066c, 19fc8911c1b391c2, 19fc83dd7bbb4f8f,
19fc8105c18636fb, 19fc8094fdba62e1, 19fc7fc18f749981, 1954ced195582bfa, 1953ecdcb710f264,
19538794a338260f, 194cd3abbc009c26, 194b848f266497ca, 194a868ff69d7c27, 19489e7dfbbdd87f,
1946168e2d96be8f, 194421b0e3267f77, 193db3cb55d291f4, 193acf349401e63b, 1938846c49d45700,
193655e43b00462e, 19325ca834c0c8a4, 192f8737675c6a9a, 192c490d8bc70220, 192a0cc08e1094d0,
19257ffe3b74a8d9, 1924d236a7f5e1aa, 19243e194804ba8a, 1922fb81351686ad, 191d7225e630117d,
191c74ba524b26be, 191a35f982e3ccc9, 1919932819a9379d, 191753d9ebd010a0, 1916b2315df68b4c,
191512b8538be5a8, 19147fb30a38bb77, 1912376c8f85c78f, 19103e7e3c0d3f1b, 190db1832e09b002,
190b6ebea88c6535, 19092d14ccf50277, 1906f077dbefd12a, 1904b29f58597a5d, 1902711fd5a575eb,
1900373351489f32, 18fdeb2a7fd4137a, 18fc02881431b9da, 18f731852c04d7ae, 18f4f83e04989b65,
18f2fd45c0d00df5.

A residual backlog of vendor-domain mail remains in the inbox by design — plenty of
non-menu vendor correspondence (promos without "menu" in the subject, deal announcements,
one-off asks) stayed untouched intentionally, precision over recall. Future runs will
keep picking off the backlog with wider phrasing.

## PART B — trash sweep (1 trashed, recoverable 30 days)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)` — 201
estimated candidates. 183 were shielded by Gmail's `is:important`/`is:starred` (Gmail's
algorithmic Important label covers a large share of this inbox, including most vendor
marketing). Re-running with `-is:important -is:starred` narrowed it to 18; each was
checked individually because Gmail can still surface a thread under that filter if only
*some* of its messages are important. Only 1 passed every gate.

| # | Thread ID | Subject | Sender | Date |
|---|---|---|---|---|
| 1 | 1986fcea63180acb | "The bull market for economists is over. It's an ominous sign for the economy." | fromthetimes-noreply@nytimes.com | 2025-08-03 |

Skipped (17): 6 threads from `CTA@sos.nj.gov` (protected — `*.gov` allowlist entry), 6
threads from `parkebank@parkebank.com` (protected — `parkebank.com` allowlist entry), 1
`surveys@dutchie.com` thread (contains IMPORTANT-flagged messages), 1
`sales@hamiltonfarms.com` "Hamilton Farm's Weekly Menu & Go2 8ths release!" thread
(contains an IMPORTANT-flagged reply — live order-minimum negotiation with Donte
Bronaugh, not disposable), 1 `iccc@icic.org` thread (contains an IMPORTANT-flagged
message). 0 threads hit the 200/run cap.

## `category:updates` — report-only (never auto-trashed)

~201 threads (estimate) older than 1 year sit in `category:updates` in the inbox. Per
the runbook this category is never swept. Sample sender domains seen: `jotform.com` /
`jotformsign.com` (register-float approvals), `headset.io` (scheduled analytics
reports, allowlisted), `voice-noreply@google.com` (missed-call notices),
`sc-noreply@google.com` (Search Console), `no-reply@accounts.google.com` (security
alerts, allowlisted), `nytimes.com`, `theathletic.com`, `noreply@redditmail.com`,
`linqapp.com`. Worth a hand pass if Lemar wants this folder thinned — none of it was
touched tonight.

No email was sent or drafted. No Trash was emptied, no Spam applied. No account other
than `lemar@cuzziesnj.com` was touched. Nothing starred/important/user-labeled or newer
than 12 months was archived or trashed. Google Drive untouched (out of scope).

## Sources
- gmail: `lemar@cuzziesnj.com` inbox — search_threads / label_thread / unlabel_thread /
  apply_sensitive_thread_label, run 2026-08-04
