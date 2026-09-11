---
created: 2026-09-11T15:20:00-04:00
updated: 2026-09-11T15:20:00-04:00
domain: automation
type: log
status: done
tags: [on-button, reopen-plan, fix, reconciliation]
source: slack
---

# On-Button page reconciliation — outcome

**Trigger:** #fixes card `C0BV5BRNH5Z:1789136462.053309` (raised earlier this run while
pricing Glass Meadows) flagged `on-button-reopen.html` missing a `glass-meadows-vendor`
entry. Lemar picked Option 1 ("Let's go with option one", ts `1789136782.093499`): run a
full reconciliation, not a one-line patch.

**What was found:** the drift was far larger than the one flagged line. The page's
`reopen-data.items` block was missing the entire "Cannabis vendor arrears" batch — 18
items (`cannabist-company`, `verano`, `sun-extractions`, `green-lightning`,
`prolific-growhouse`, `happy-farmer`, `cookies-harrison`, `hillview-med`,
`garden-society`, `curaleaf-vendor`, `glass-meadows-vendor`, `chew-and-chill`,
`dime-industries`, `hamilton-farms`, `ganja-manja`, `lovegrow-vendor`, `niche-llc`,
`fresh-grow`) that landed in `index.md` on 2026-07-11 but were never added to the page.

**What was done:** added all 18 items to `on-button-reopen.html`'s `reopen-data.items`
array, matching `index.md` field-for-field (id/label/amount/tier/vendor+account/contact/
status). Verified programmatically: the two files' item-id sets now match exactly
(47/47). Updated `meta.updated`. Logged the pass in `index.md`. Left the page's separate
`repay.vendors` JSON block (net/profit/margin per vendor) untouched — Option 2 (ask who
owns it) was not picked.

**Not done:** canvas `F0BEN1167GB` refresh — `canvas_access.writable: false` per the
last check (2026-09-06); not re-attempted since today's first-run recheck already
happened this morning. Known, carried gap.

**Commits (main):** `15ec5238` (page), `1acffafd` (index.md).

**Nothing paid or contacted.**

## Sources
- Slack: #fixes `C0BV5BRNH5Z` thread `1789136462.053309`; #on-button `C0BEQUW5NPP`
  timeline entry ts `1789139889.857809`.
- `haven/vault/40-Projects/on-button-reopen/index.md`
