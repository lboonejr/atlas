---
created: 2026-09-06T16:45-04:00
updated: 2026-09-06T16:45-04:00
domain: automation
type: log
status: done
tags: [fixes, gmail, connector, curaleaf, marshall-sterling]
source: slack
---

# Gmail connector — historical threads/drafts invisible for one scan, now resolved

During the 86th scan (2026-09-06 ~19:39 UTC), the Gmail connection could not find three
specific threads Haven records as live (Curaleaf/A.G. Adjustments `19ffb0bb3846886a`,
Marshall & Sterling `1a020b9cd6bd94c0` and `1a020adba88b3efa`), nor the drafts tied to
them, even though other live mail (idscan.net, Gusto, CannaBIZ Collects) was visible
fine in the same pass. Raised as a #fixes card (`C0BV5BRNH5Z`, ts `1788723953.608629`)
rather than guessed at.

Lemar disconnected and reconnected the Google connector between that scan and this one
(2026-09-06 ~20:37 UTC run). This run's Gmail search and drafts list found everything:
all three threads, the full correspondence history, and every draft including the two
relevant to the open Convo 1 cards (Curaleaf, M&S/FIRST). Root cause consistent with a
stale/scoped session on the connector rather than any mail actually being lost or
deleted — nothing was missing once the connector was fresh.

**Outcome:** confirmed fixed. Closed the #fixes card. No further action; will reopen if
Gmail visibility gaps recur.

## Sources
- slack: #fixes `C0BV5BRNH5Z` ts `1788723953.608629`; Convo 1 cards ts
  `1788714813.201089` (Curaleaf), `1788718700.965879` (M&S)
- haven: `20-Cuzzies/2026-08-13-curaleaf-nj-ii-collections.md`,
  `20-Cuzzies/2026-08-20-marshall-sterling-final-cancel-endorsements-return-premium.md`
