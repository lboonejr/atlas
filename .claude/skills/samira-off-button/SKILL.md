---
name: samira-off-button
description: >
  Samira's vendor wind-down scanner (PART O of the routine). Maintains the ONE structured
  source of truth — the Haven note haven/vault/40-Projects/off-button/index.md — for every
  Cuzzie's (Camden) vendor payable, tax liability and collections matter, and regenerates
  the monday.com board "Off Button — Vendor Wind-Down & Payoff" (18424191974) as a
  rendering of it. Runs in two modes: a cheap per-scan pass that classifies vendor and
  collections mail PART D already read, and one full reconciliation per day. Use it on
  Samira's scan or on demand ("run the off button scan", "update the off button board",
  "any new vendor bills?", "what's escalating on the wind-down"). It NEVER pays anyone,
  NEVER contacts or replies to a vendor, and never posts outside #reports + #decisions; it
  updates the vault, regenerates the board, and logs. Returns counts for the digest.
---

# Off-Button Vendor Wind-Down Scanner (PART O)

Cuzzie's ceased operations **2026-06-13**. This skill keeps the wind-down ledger current:
what is owed, to whom, who moved last, and what is about to escalate. Every Safety rule in
the runbook applies; add the guards below.

**Tracking and negotiating-support only — nothing is ever paid, and no vendor is ever
contacted.** Drafting a reply is PART D's job, and only into Drafts.

## ANCHORS
All IDs live in **`.claude/anchors.md`** — board `18424191974` with its full column and
group IDs. Vault writes go through **haven-capture**; results are logged through
**samira-report-result**.

## THE SOURCE OF TRUTH — one Haven note, one data block
**`haven/vault/40-Projects/off-button/index.md`** holds the ledger in a single fenced
`yaml` block (`meta`, `items`). This is the ONLY place ledger data changes — like the
[[on-button-reopen]] and [[investor-pipeline]] indexes, editing this block and touching
`updated` is a sanctioned machine write; git history preserves every prior state.

**The monday.com board is a RENDERING.** This is what resolves the Monday cutover gate
(mirroring ended 2026-07-11, boards go read-only): the ledger lives in the vault, and the
board is refreshed from it for as long as Lemar still looks at it. When the board is
finally retired, delete PART O step 4 and nothing else changes.

Field rules live at the top of that note. The three that matter most:
- **`amount: null` means unknown and MUST stay null.** Never guess. Never substitute a
  partial figure that understates exposure. Put where the figure lives in `blocked_on`.
- **Dedupe by `id`.** A new notice UPDATES an entry; it never creates a second one.
- **Corrections are explicit**, never silent rewrites.

## TWO MODES

### Mode 1 — per-scan triage (every run, cheap)
Runs immediately after **PART D**, over the mail PART D has already read. **Do NOT open a
second Gmail sweep** — that is the whole point of the placement.

From what PART D surfaced, pull anything that is a vendor/creditor/tax/collections
communication about Cuzzie's (or The Station, see Scope). For each, decide:
- **Matches an existing `id`** → update that entry's `correspondence`, `last_notice`,
  `amount` (only if a NEW figure is explicitly stated), `resolution`, and append one line
  to `note`.
- **New obligation** → add an entry. If the amount is not explicitly stated, `amount: null`.
- **Neither** → ignore. See the noise rule.

If nothing matched, write nothing and return `off-button: 0 changes`. Silence is a valid
result; do not touch the note or the board to prove you ran.

### Mode 2 — daily reconciliation (first scan on or after 06:00 ET)
Everything in Mode 1, plus:
1. Re-read the whole `ledger` block.
2. Run a genuine Gmail sweep over the window since `meta.last_scan` (minus 3 days of
   overlap, to catch anything that landed mid-scan). Suggested searches — run several, not
   one:
   - `after:YYYY/MM/DD ("past due" OR invoice OR "statement of account" OR collection OR "amount due" OR "payment reminder" OR balance)`
   - `after:YYYY/MM/DD (collections OR "demand letter" OR "final notice" OR "legal action" OR delinquent OR "turned over")`
   - `after:YYYY/MM/DD -in:sent -in:draft (outstanding OR overdue OR settle OR "payment plan" OR unpaid OR "account balance")`
   - a `from:` sweep across the domains already in the ledger, to catch updates on existing
     entries that use none of those words.
3. **Check SENT mail.** The single most common historical error in this ledger was an entry
   marked `waiting_on_us` when a reply had already gone out, or a note claiming "no reply
   sent" when one was. Verify the direction of every `correspondence` value you touch.
4. Regenerate the board (below).
5. Set `meta.last_scan` and `meta.scan_window_start`, and touch `updated`.

## THE NOISE RULE (read this before writing anything)
Cannabis vendors send **constant** weekly menu and promo blasts — Verano, Glass Meadows,
Hamilton Farms, Bud's Goods, Northlake, QCC, Kiva, TerrAscend and others mail every few
days. **Marketing is not correspondence.** It must never become a `last_notice`, never
flip a `correspondence` value, and never appear in a digest.

A message counts as ledger activity only if it concerns money owed: a statement, invoice,
past-due notice, payment-plan discussion, collections letter, or a reply in either
direction about any of those. When unsure, skip — a missed item surfaces again next scan;
a false one corrupts the ledger.

Two further exclusions learned 2026-08-13: a vendor that **retracts** a balance is not a
liability (Kushi Labs billed $0.17 then withdrew it — do not add), and **lien/debt-relief
solicitations are advertising** (Fresh Start 4B — do not add).

## SCOPE — what belongs here
IN: Cuzzie's vendor payables, tax/government liabilities, bank and lender balances tied to
the wind-down, and any collections placement against them.

OUT — **flag to Lemar, never auto-add**: MCA / merchant-cash-advance obligations (Novus
Capital, Liquidibee / Elevate Funding, Nomas Recovery) and active litigation (DeWalt v.
Cuzzie's, CAM-L-1339-26). Lemar confirmed 2026-08-13 these stay off. If activity appears,
it goes in the digest as a flag — one line, no item, no #decisions parent unless it is
genuinely time-critical.

BORDERLINE: **The Station (Newark)** obligations. Two are already on the ledger
(`primo-brands`, `canopy-usa`) carrying `entity: the_station`. Keep flagging; never
unilaterally move or delete them. If Lemar rules Off Button is Cuzzie's-only, both move
together.

## REGENERATING THE BOARD (from the note, never hand-edited)
Board `18424191974`. Map each ledger entry to one item:

| ledger field | column |
|---|---|
| `vendor` | item name |
| `category` | `color_mm5qxtv1` — cannabis → "Cannabis Vendor", non_cannabis → "Non-Cannabis Vendor", tax_government → "Tax-Government" |
| `contact.name` | `text_mm5q9s0w` |
| `contact.email` | `email_mm5q4zpb` |
| `contact.phone` | `phone_mm5qa4sc` |
| `last_notice` | `date_mm5qksv3` |
| `amount` | `numeric_mm5qh0zv` — **omit the key entirely when null; never write 0** |
| `correspondence` | `color_mm5qjh06` |
| `resolution` | `color_mm5qekcc` |
| `collections_agency` | `text_mm5qhwwj` |
| `note` + `blocked_on` + `threads` | `long_text_mm5qavs1` (Source Notes) |

`group` maps to: cannabis → `group_mm5rxza9`, negotiate → `group_mm5q4d77`, self_pay →
`group_mm5qgxka`, unclassified → `group_mm5qs8wh`.

Rules:
- **Never delete a board item.** If an entry leaves the ledger, say so in the digest and
  leave the row for Lemar.
- **Append to Source Notes, never overwrite.** Add a headed
  `UPDATE <date> scan -- <what changed>` block beneath the existing text.
- Only push items whose ledger entry actually changed this run.

### Two API traps (both hit on 2026-08-13)
1. **`email_mm5q4zpb` requires an object**, not a string:
   `{"email":"x@y.com","text":"x@y.com"}`. A plain string fails with `ColumnValueException`.
2. **`update_items` rejects oversized payloads** with an opaque
   "Invalid content from server" error. Send **at most 3 items per call** when Source Notes
   are long.

## ESCALATION — what earns a #decisions parent
Post ONE #decisions parent (never a ping per vendor) when any of these appear. Everything
else rides the #reports digest.
- A **hard deadline inside 14 days**: a final demand with a stated window, a dispute window
  closing, a scheduled collections-transfer date, a service-suspension date.
- A **new third-party collections placement** (an agency, not the creditor's own dunning).
- A **legal threat** — suit, judgment, attorney fees, or a lien.
- Anything touching the **CRC license or state notification** — a vendor threatening to
  notify the state is a licensing risk, not just a debt.
- An amount that **moved materially** against expectation (a balance growing while a plan
  was supposedly running).

Never guess a material number, never pay, never contact anyone. If a task would require
any of that, draft what you safely can, raise the ONE parent, and move on.

## OUTCOMES
Success or failure, ALWAYS via **samira-report-result**: outcome note in Haven first, then
the two-line #reports block, then the Monday mirror (until the gate), then the digest line.
Never a bare checkmark.

## Returns (to the Samira runbook, for the digest)
`off-button: U updated · N new · D deadlines<14d · F flagged`

Where `F` counts out-of-scope activity (MCA, litigation), Station scope questions, and
entries left `null` because the figure was locked in an unopened attachment. If all four
counters are zero, return `off-button: 0 changes` and write nothing.
