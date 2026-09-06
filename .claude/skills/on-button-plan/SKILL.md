---
name: on-button-plan
description: >
  The reopening-plan builder for the on-button project. Maintains the ONE structured
  source of truth — the Haven note haven/vault/40-Projects/on-button-reopen/index.md —
  and regenerates the two surfaces rendered from it: the interactive page
  on-button-reopen.html (repo root, served via githack) and the pinned Slack canvas
  F0BEN1167GB. Use it whenever a new past-due bill / figure / screenshot arrives via
  Convo 2 (Samira's PART 4 sweep of Lemar's self-DM hands the drop over — the #on-button
  channel sweep retired 2026-09-06; #on-button is now the TIMELINE where regeneration
  notices post), when Lemar edits a tier or an amount, or on demand ("run
  on-button-plan", "update the reopen plan", "rebuild the on-button page", "add this to
  the reopening plan"). It codifies the scanner/dedupe rule and the index → page →
  canvas regeneration. This skill NEVER pays or contacts anyone, never sends email or
  outreach, and never posts outside the #on-button timeline + #reports + a Convo 1 card
  when a decision is needed; it updates the vault, regenerates the page/canvas, commits
  to main, and logs. Returns counts for the digest.
---

# On-Button Reopen-Plan Builder

The on-button plan is Cuzzie's reopening command center; `#on-button` is its append-only
TIMELINE (since 2026-09-06) — regeneration notices post there, drops arrive via Convo 2.
The plan is tiered so any investment
amount maps to a concrete reopening path (Tier 1 bare-bones → Tier 2 nice-to-have →
Tier 3 edge), with the ~$110K sales/local tax held out as a separate **gate** and the
~$31.2K/mo **carry** as the runway denominator. This skill keeps that plan current and
regenerates what everyone looks at. Every Safety rule in the runbook applies; add the
guards below. **Tracking & planning only — nothing paid or contacted.**

## ANCHORS
All IDs live in **`.claude/anchors.md`**: the `#on-button` timeline `C0BEQUW5NPP`, its
pinned canvas `F0BEN1167GB`, **Convo 1** `D0BHPKMDNEP` (decision cards), and the
git-write policy (commit straight to `main`). Vault writes go through **haven-capture**;
results are logged through **samira-report-result**.

## THE SOURCE OF TRUTH — one Haven note, one data block
**`haven/vault/40-Projects/on-button-reopen/index.md`** holds the plan in a single fenced
`yaml` block (`constants`, `tax_gate`, `items`, `carry`). This is the ONLY place plan data
changes — like the [[investor-pipeline]] index, editing this block + touching `updated` is a
sanctioned machine write; git history preserves every prior state. Field rules live at the
top of that note (amounts are plain numbers; `amount: null` = TBD; `tier` ∈ 1|2|3|gate|carry;
dedupe by `id`). Never invent figures — an unknown stays `null`.

## THE TWO RENDERED SURFACES (regenerated FROM the note, never hand-edited)
1. **`on-button-reopen.html`** (repo root, served at
   `https://raw.githack.com/lboonejr/atlas/main/on-button-reopen.html`). Self-contained
   single file. Its data lives in one `<script id="reopen-data" type="application/json">`
   block near the bottom. The page also has a client-side **tier-shuffle** (per-line Tier
   menu) that is a browser-only what-if; its "Apply to plan →" button emits a
   `Samira, update the on-button reopen plan — apply these tier moves:` instruction. When you
   see that instruction (Lemar pastes it into Convo 2, his self-DM — the PART 4 sweep hands
   it over; was pasted into #on-button until 2026-09-06), apply each listed move by changing
   the item's `tier` in the note, then regenerate — that is the loop that makes a shuffle
   durable.
   **To regenerate: translate the note's `yaml` block into that JSON
   (constants → `constants`; `tax_gate` → `gate.items`; `items` → `items` with the same
   `id/label/amount/tier` plus a flattened `vendor`/`contact`/`status` string for the detail
   table; `carry` → `carry`) and set `meta.updated`.** Do not touch the markup, CSS, or the
   allocator `<script>` logic below the data block — only the JSON payload and the visible
   "Last updated" text. Keep Tier 1's `inventory-restock` last in its group so the per-item
   fill reads intuitively (cheap critical reactivations light up before the big line).
2. **Slack canvas `F0BEN1167GB`** — the glanceable in-Slack list. Refresh it from the note
   too (read section IDs, replace per section, never the whole canvas): the three tier
   subtotals + headline (Tier 1 to open ≈ $X, carry ≈ $31.2K/mo, tax gate ≈ $110K separate),
   then the line items grouped by tier. The canvas is a summary; the page is the interactive
   tool; both trace to the note → **no double-entry.**

## THE SCANNER / DEDUPE RULE (was homeless — now codified)
Drops arrive from Samira's PART 4 sweep of Convo 2 (Lemar's self-DM), which hands each
on-button drop to this skill — the same discipline that governed the retired #on-button
channel sweep applies to what is handed over:
- A **drop** is a genuinely new bill/notice/screenshot/figure (a forwarded email, a PDF, a
  screenshot, or Lemar naming an amount). Extract: amount, vendor, account/reference,
  contact, and which tier it belongs to (default new past-due operating items to **Tier 1**
  if they block opening, else Tier 2; ask via a Convo 1 card only if the tier is genuinely
  ambiguous and material).
- **IGNORE restatements:** any message prefixed 🧹 📌 📊, led by a bare list number, or that
  is your own render/summary. These are not drops.
- **Dedupe against `index.md` by `id`/vendor+account:** if the matter already has an item,
  UPDATE it (keep the latest figure; annotate, don't duplicate — e.g. Regus clear-out is the
  same acct #16605480, not a new line). Only create a new item for a genuinely new matter.
- Cannabis-vendor arrears stay grouped as such; ones that gate resupply/testing (e.g. Little
  Leaf Labs) belong in Tier 1, the rest in Tier 2.
- Never delete an item — a resolved one goes `status: paid`/`settled`; a dropped one
  `status: parked`.

## PROCEDURE (each run / invocation)
1. **Read** `index.md`'s data block (current state) and ingest the drops PART 4 handed
   over (or the drop given on a live invocation) per the scanner rule.
2. **Update the note:** add/edit items in the `yaml` block, keep latest figures, touch
   `updated`. If a drop needs a decision (ambiguous tier, a figure to confirm), post ONE
   Convo 1 card and leave the item `status: tbd` — never guess a material number.
3. **Regenerate `on-button-reopen.html`** — rewrite only the JSON data block + "Last updated"
   text from the note.
4. **Refresh the canvas** `F0BEN1167GB` from the note (per-section replace).
5. **Commit both files to `main`** in one commit (`on-button-plan: <what changed>`) via the
   GitHub MCP `push_files`/`create_or_update_file`, or local `git commit` + `push origin main`
   — never a branch+PR (anchors git-write policy). The githack URL auto-reflects; the Slack
   pin never goes stale.
6. **Post the regeneration notice to the `#on-button` timeline** — one append-only line
   (what changed, page + canvas refreshed, links). Never edit or delete a prior entry,
   and never read the timeline as input.
7. **Log** via **samira-report-result**: a Haven outcome note (what changed in the plan) →
   the two-line #reports block. Done = a filed Haven note.

## GUARDS
- **No payments, no contact, ever** — this is a planning tracker. Do not email, call, or
  message any vendor/lender named here.
- **Never fabricate a figure.** Unknown = `null` (renders TBD) + a Convo 1 card ask if it's
  material to opening.
- **The tax gate is never funded by the allocator** — it stays in `tax_gate`, shown as a
  separate license-risk condition.
- **Rent and payroll are carry, not one-time** — keep them in `carry`, never as Tier 1
  one-time lines (double-counting inflates the reopen number and understates runway).
- Full internal detail is fine here (this is an internal tool): vendor names, contacts,
  account refs. But never put full SSNs/ID numbers anywhere (runbook Safety).

## What to return
**New drops ingested · items updated · page regenerated (y/n) · canvas refreshed (y/n) ·
timeline entry posted (y/n) · Convo 1 cards raised · Haven outcome note O.** Each
regeneration also gets a one-line #reports note.
