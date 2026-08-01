---
created: 2026-08-01T10:20-04:00
updated: 2026-08-01T12:00:00-04:00
domain: cuzzies
type: log
status: done
tags: [on-button, progressive-commercial, reopening, insurance]
source: slack
---

# On-Button sweep — Progressive Commercial reclassified Tier 1 → Tier 3, balance reconciled

PART C sweep of `#on-button` (`C0BEQUW5NPP`) found a genuinely new drop per the scanner
rule: Samira's own report at ts `1785164745.763099` (2026-07-27, no ✅/🫡/🚗/⏳ reaction, no
🧹📌📊 tag, not a numbered restatement) carried a figure not yet reflected in the plan
index — Progressive Commercial's confirmed cancellation balance is **$1,107.20**, not the
$2,117.80 previously tracked (that was the pre-cancellation cost to keep the policy
active, now moot since the policy is confirmed cancelled effective 7/3). Lemar's decision
in `#decisions` 2026-07-27: let it lapse — no dispute, no payment.

## What changed
Updated `haven/vault/40-Projects/on-button-reopen/index.md` (the source of truth):
- `progressive` item: `amount` 2117.80 → 1107.20, `status` past-due → lapsed
- **Moved Tier 1 → Tier 3** to match the treatment of `epli-reinstate` — both come from
  the same original 7/2 #decisions call (ts `1783026740.943679`) that decided both
  policies would lapse rather than be paid, so neither is a reopen blocker.
- Tier 1 total: $108,655 → ≈$106,537.20 (−$2,117.80)
- Tier 3 total: $17,081.76 → ≈$18,188.96 (+$1,107.20)
- Snapshot section + `updated_label` bumped to 2026-08-01.

Regenerated `on-button-reopen.html`'s data block to match (same figures/tier move,
`meta.updated` bumped). Both files committed and pushed straight to `main` (git-write
policy — no branch/PR): commits `a028c0e` (index.md) and `4bb681b` (html).

## Canvas refresh — blocked (known tooling gap, not new)
Attempted to refresh the pinned canvas `F0BEN1167GB` (both a full-document `replace` and
an `insert_after` connectivity probe). Both calls returned `restricted_action` /
`invalid_arguments` errors, consistent with the 2026-07-31 finding in the index note's
Update log ("canvas writes appear blocked in this session"). Not attempted further this
run — flagging as a persisting tooling gap, not a business decision. Canvas still shows
`edit_timestamp` 2026-07-15 (stale — now also missing this Progressive Commercial move,
plus the already-known-stale AIQ/PSE&G gaps from 7/31).

Nothing paid or contacted — tracking only, per the on-button-plan skill's guardrails.

## Sources
- slack: #on-button `C0BEQUW5NPP` ts `1785164745.763099` (the drop swept this run)
- vault: `haven/vault/40-Projects/on-button-reopen/index.md` (source of truth, updated)
- vault: `haven/vault/20-Cuzzies/2026-07-04-progressive-commercial-canceled-confirmed.md`
  (full balance/decision history)
- git: `main` commits `a028c0e`, `4bb681b`
