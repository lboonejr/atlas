---
created: 2026-07-30T23:07-04:00
updated: 2026-08-03T07:56-04:00
domain: automation
type: log
status: done
tags: [inbox-janitor, basil, gmail-cleanup, automation, vendor-menus]
source: claude
---

# Basil — Inbox Janitor run — 2026-07-30

Live run (`DRY_RUN=false`), continuing from [[2026-07-29-basil-inbox-janitor-run]] and
[[2026-07-28-basil-inbox-janitor-run]] — not a first run. Account: `lemar@cuzziesnj.com`
(the only connected Gmail account; Drive out of scope). Archived 99 vendor-menu threads
out of the inbox and trashed 188 old promotional/social/forum threads (all recoverable
in Gmail Trash for 30 days). Both actions stayed under their per-run caps and respected
the NEVER-TOUCH allowlist and the starred/important floor from `.claude/anchors.md`.

## PART A — Vendor menus archived (99)

Query: anchors vendor-domain seed list AND subject containing an explicit menu signal
(`menu`, `"price sheet"`, `"live menu"`), restricted to `in:inbox`, with `-is:important
-is:starred` applied at the query level (Gmail's thread-level exclusion is imperfect —
each returned thread was individually re-checked for any IMPORTANT/STARRED message
before acting, since a thread with a later unstarred reply can still surface even when
an earlier message in it was starred). 4 pages, ~102 domain+subject matches; 99 qualified
and were labeled `Vendor Menus` (`Label_8`) then had `INBOX` removed. 2 threads were
skipped despite matching: one contained a STARRED sent message buried in the thread, one
contained an IMPORTANT-flagged reply — both left untouched per the hard floor.

Senders spanned the full anchors seed list and ran from 2024-08-05 through 2026-07-29:
illicitgardens.com (largest single contributor, ~25 threads — weekly menu blast going
back over a year), prolificgrowhouse.com (~25 threads, same pattern), terrascend.com,
awholdings.com, harvestmoonfarmsnj.com, freshcannabis.co, apextrading.com subdomains,
northlake.supply, qccnj.com. No new non-seed-list vendor domains were surfaced tonight
(the query was seed-list-only, unlike 2026-07-29's broader has:attachment cross-search).

**Note on the account's scale:** this batch reached back to August 2024 — the inbox
still holds a very long tail of weekly vendor blasts (illicitgardens.com and
prolificgrowhouse.com alone sent one nearly every week for ~18 months). Expect several
more nights before Part A converges on "just this week's menus."

## PART B — Trash sweep (188 threads)

Query: `older_than:1y (category:promotions OR category:social OR category:forums)
-is:starred -is:important` plus explicit `-from:` exclusions for every allowlist domain
that has a stable sender address — **run without an `in:inbox` restriction**, matching
the runbook's own example query verbatim. This differs from the 2026-07-28/07-29 runs,
which both added `in:inbox` to the query on their own initiative; without it, tonight's
sweep also reached old promotional mail that had already been archived out of the inbox
by other automation (Samira labels, etc.) but never trashed. That's the most likely
reason tonight's catch (188) is much larger than 07-29's (5) — not a sign anything was
missed or double-counted; re-running the identical query just now (post-trash) returns
only the 10 already-known floor exclusions, confirming the 188 are actually gone from
active mail and nothing new is hiding behind the same filter.

4 pages, ~349 raw candidates scanned. Excluded 10 threads: all 7 `CTA@sos.nj.gov`
(`*.gov` allowlist), a Dutchie implementation-survey thread and a Hamilton Farms
menu/order-minimum thread (each carrying an IMPORTANT-flagged message even though the
head message matched), and one ICIC.org thread (IMPORTANT). Remaining 188 trashed,
dated 2022-07-14 through 2025-07-29 — well past the 12-month cutoff. Under the 200/run
cap, so nothing carries over to tomorrow from tonight's candidate set.

Recurring senders swept (bulk marketing/newsletter noise, not vendor or business
correspondence): `engage.canva.com`, `hootsuite.com`, Microsoft Start/Copilot/Windows
engagement mail, `mg.homedepot.com`, `email.adobe.com`, `email.bing.com`,
`ce.angi.com`, `send.calendly.com`, `heartland.us`/`ccsend.com` (Heartland Payment
Systems marketing), `marketing@dutchie.com`, `marketing@leaflink.com`,
`email.salesforce.com`, `foundershield.com`, `thinkcanna.com`, `covasoftware.com`,
`420njevents.com`, `alpharoot.com`, `blindspotfinancial.com`, `sherwin-williams.com`,
`emeraldintel.ai`, `necann.com`, plus a small number of now->12mo-old vendor-marketing
threads (`verano.com`, `terrascend.com`) — trashable here per anchors since only
*recent* vendor menus are protected by Part A.

Full per-thread audit (thread ID · sender · date) for all 188 was captured during the
run and is recoverable via Gmail search `in:trash` filtered by sender/date if a mistake
needs undoing; not reproduced as a 188-row table here to keep this note readable — ask
Basil/re-run the search transcript for the exact list if needed. This matches the
2026-07-28 note's convention (that night's 184-trash batch also used a narrative summary
rather than a full table; only nights with small batches, like 07-29's 5, got a table).

## Report-only: `category:updates` (never auto-trashed)

~200+ threads older than 12 months in `category:updates` — not touched, per the
runbook. Sample sender domains: `ngrok.com`, `voice-noreply@google.com` (Google Voice
notifications — very high volume, same pattern flagged 07-29), `aiq.com`,
`jotform.com`/`jotformsign.com`, `readyrefresh.com`, `nytimes.com` breaking news,
`headset.io` and `notification.intuit.com` (both already allowlisted). Lemar may want
to clear these by hand or adjust notification settings upstream (Google Voice in
particular keeps coming up as the single biggest contributor across all three nights).

## Next run

`DRY_RUN` stays `false`. Part A still has a long tail (illicitgardens.com and
prolificgrowhouse.com weekly blasts going back to mid-2024) — expect several more nights
before it converges. Part B's candidate pool looked exhausted under tonight's exact
query (re-check returned only the 10 known floor-exclusions), but ordinary nightly
accumulation plus the `in:inbox`-vs-not distinction means tomorrow's run may still find
a few. Suggest the operator pick one query convention (with or without `in:inbox`) and
keep it stable across nights so batch-size trends are comparable.

## Sources
- gmail: `lemar@cuzziesnj.com` inbox, live sweep 2026-07-30
- related: [[2026-07-29-basil-inbox-janitor-run]] (previous night's run)
- related: [[2026-07-28-basil-inbox-janitor-run]] (first live run)
