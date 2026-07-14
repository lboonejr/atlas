# --- YAML frontmatter ---
---
created: 2026-07-14T23:07:00-04:00
updated: 2026-07-14T12:00:00-04:00
domain: personal
type: log
status: done
tags: [inbox-janitor, basil, gmail, dry-run, cleanup]
source: gmail
---

# 2026-07-14 Inbox Janitor (Basil) — DRY RUN preview

First supervised run of the Inbox Janitor routine (`.claude/routines/inbox-janitor.md`,
`DRY_RUN = true`). No Gmail mutations were performed — no archiving, no labeling, no
trashing. Everything below is a preview for Lemar to vet before flipping
`DRY_RUN = false` in the runbook.

## PART A — vendor menus (would archive)

- Query: inbox threads from the 20-domain vendor-menu seed list in anchors.md.
- Gmail estimate: ~201 matching threads currently in the inbox.
- Manually reviewed ~190 of the 201 in detail.
- **Would archive** (label `Vendor Menus` [`Label_8`], remove `INBOX`): **~194**.
- Excluded **7 threads** that matched a seed domain but are genuine active
  correspondence (Lemar replied, or the thread is starred) — not weak menu blasts,
  real dialogue, so left alone:
  1. Thread `19ef5a3dac10b873` — thegardensociety.com (ar@) — Lemar sent a reply 2026-06-23.
  2. Thread `19ed1ecbcaa738ee` — verano.com (Andrew.Pallottie@) — Lemar replied 2026-06-16;
     thread includes a delivery-failure bounce notice.
  3. Thread `19eb246b48bf09fa` — harvestmoonfarmsnj.com (allanf@) — Lemar replied 2026-06-10;
     ongoing multi-message exchange through 2026-06-17.
  4. Thread `19eb27b65b1411e5` — prolificgrowhouse.com (maylissa@) — Lemar replied 2026-06-10.
  5. Thread `19ead8aa48036015` — thegardensociety.com (ar@) — **STARRED**, and Lemar
     replied 2026-06-10.
  6. Thread `19ea884575d02d16` — harvestmoonfarmsnj.com (brett@) — Lemar replied
     2026-06-08/09.
  7. Thread `19e74bfe0239675b` — illicitgardens.com — multi-party deal negotiation
     involving markony@thestationnewarknj.com, Lemar cc'd, active back-and-forth
     2026-05-29 to 06-01.

**Recommendation:** the domain-seed-list signal alone isn't sufficient precision when a
vendor rep also does direct 1:1 business with Lemar. Worth adding a rule that skips
archiving any thread containing a `SENT` message from lemar@cuzziesnj.com, regardless of
domain match.

## PART B — trash sweep (would trash, oldest >12mo, promotions/social/forums)

- Query: `in:inbox older_than:1y (category:promotions OR category:social OR
  category:forums) -is:starred -is:important`
- Sampled 7 pages / ~340 threads (dates 2025-05-14 through 2025-07-13 — the newest end
  of the qualifying set). Gmail's `resultCountEstimate` stayed pinned at "201"
  throughout, which appears to be an approximate/capped estimate rather than a true
  count — the real qualifying population is materially larger than 201 and almost
  certainly exceeds the per-run 200 cap once a live run walks the full mailbox history.
- Content was overwhelmingly genuine disposable marketing: SaaS newsletters
  (Salesforce, Canva, Vangst, Dutchie, Zapier), retail/vendor deals (Best Buy,
  Sherwin-Williams, Home Depot Pro, WebstaurantStore), conference/event marketing
  (NECANN, Benzinga, Treez, FASTSIGNS), surveys (ADT, Grainger, Zebra, Microsoft), a
  Reddit digest, and >12-month-old vendor-menu blasts from the same seed-list domains
  (trashable here per the runbook once aged out — separate from PART A's recent-menu
  archiving).
- **Important finding — allowlist gap:** the PART B Gmail query has no way to exclude
  NEVER-TOUCH allowlist domains at the query level (Gmail search doesn't know about
  anchors.md). Manually checking the sample against the allowlist turned up real hits
  that the raw query would otherwise queue for trash:
  - `CTA@sos.nj.gov` (a `*.gov` sender, on the allowlist) — **7 instances** found in the
    sample alone (NJ Cannabis Training Academy newsletters).
  - `parkebank@parkebank.com` (explicitly on the allowlist) — **1 instance** found.
  - **Recommendation before going live:** add explicit `-from:` exclusions for every
    allowlist domain directly into the PART B search query, or add a hard per-thread
    allowlist check against the sender domain before calling
    `apply_sensitive_thread_label`, so this can't slip through on a live run.
- No genuine user-applied filing labels seen on any candidate in the sample (only
  `INBOX`/`UNREAD`/`IMPORTANT`-excluded-by-query).

## PART B note — category:updates (report-only, never auto-trashed)

- Query: `in:inbox older_than:1y category:updates`
- Sampled 2 pages / ~40 threads; confirms the runbook's stated rationale for keeping
  this bucket manual — it mixes genuinely disposable notices with financial/operational
  mail:
  - Disposable-looking: jotform.com / jotformsign.com (Cuzzie's staff time-off-request
    workflow, including several stray `(TEST)` template emails that look safe to clear
    by hand), noreply@redditmail.com (r/gardening digest), notifications@adtcontrol.com,
    ads-noreply@google.com / sc-noreply@google.com,
    refreshment@youraccount.readyrefresh.com, no-reply@glueupmail.com.
  - Financial/operational — must NOT be swept: `quickbooks@notification.intuit.com`
    (Intuit, allowlisted) and `info@headset.io` (allowlisted analytics reports) both
    appeared in this bucket, confirming the routine's warning that invoices/financial
    notices hide in `category:updates`.

## Actions taken tonight

None — `DRY_RUN = true`. No Gmail label, archive, or trash calls were made. No
`Vendor Menus` label creation was needed (`Label_8` already exists).

## Recommendation for Lemar

1. Vet the 7 PART A exclusions and the allowlist gap found in PART B above.
2. Consider hardening the PART B query/logic with explicit allowlist exclusions before
   flipping `DRY_RUN=false`, since the raw category query alone would have queued a
   `*.gov` sender and Parke Bank for trash.
3. Once comfortable, flip `DRY_RUN = false` in `.claude/routines/inbox-janitor.md` on
   `main` to go live on the next run.

## Sources
- gmail: search `in:inbox {vendor-domain-seed-list}` (PART A candidate set)
- gmail: search `in:inbox older_than:1y (category:promotions OR category:social OR
  category:forums) -is:starred -is:important` (PART B candidate set)
- gmail: search `in:inbox older_than:1y category:updates` (report-only bucket)
