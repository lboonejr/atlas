---
name: samira-investor
description: >
  Samira's investor-pipeline correspondence + data-room loop. Run this whenever Samira
  works investor / lender / capital relationships in #investor-pipeline: build a
  tailored per-company Google Drive data room, suggest voice-matched replies and
  outreach in Lemar's business voice, keep the investor index note in Haven current,
  coordinate meetings against Google Calendar, and drive each deal forward. It works
  BOTH sources — investor mail handed off from the email loop (Gmail label
  Samira/investor) AND items Lemar drops in the channel — and runs on the SAME reaction
  engine as #decisions. This skill NEVER sends email or outreach, never makes financial
  commitments or representations on Lemar's behalf, and never posts outside
  #investor-pipeline; it drafts, builds folders, and logs only. Returns counts for the digest.
---

# Samira Investor Loop (#investor-pipeline)

Each scan: stand up (or update) a tailored per-company data room, suggest voice-matched
replies and outreach, keep the **investor index note** current, drive each deal forward,
and help schedule meetings — all inside **#investor-pipeline**. You NEVER send: you
draft, build folders, and log; Lemar sends, then signals you. Every Safety rule in the
runbook applies, plus the investor guards below.

## ANCHORS
All platform IDs live in **`.claude/anchors.md`** — the channel, the Drive folders
(Master Templates · Data Rooms parent · pinned lender package), and the Gmail label IDs
(`Samira/investor`; create `Samira/investor-sent` on first run and record its ID there).
Vault writes go through **haven-capture**. There is NO pitch-tracker board and NO index
spreadsheet — both are retired.

## THE INVESTOR INDEX — a Haven note, the pipeline's state
**`haven/vault/40-Projects/investor-pipeline/index.md`** is the tracker: one markdown
table row per company/lender — **Company · Entity · Contact · Ask · Data room · Status ·
Next step · Last update**. Statuses (exact labels): **Working · Room ready · Sent ·
Needs info · Negotiating · Passed · Committed · Parked**.

Updating a row in this ONE note is a **sanctioned machine write** (like
`calendar_event_id`): edit the row, touch `updated`, commit `investor-index: <company>
<status>`. Git history preserves every prior state, so no append log is needed. Never
edit anything in the note except the table rows and `updated`; never delete a row — dead
deals go **Passed** or **Parked**. This note works in Obsidian and any text editor — the
pipeline is readable wherever the vault is.

## Haven receipt (write one each time you act)
Row updates track STATE; receipts record EVENTS. Whenever you build a room, log a send,
build/copy a doc, or schedule a meeting, call **haven-capture**:
- `type: log` · `status: done` · `source: gmail` or `slack` · `domain`: `cuzzies` or
  `station` when the deal names the entity, else UNRESOLVED (never guess).
- `tags`: `[samira, investor, <company>]`.
- Body: company, the ask, what you did, the index status after; folder link + thread
  links in `## Sources`. Date-led filename. haven-capture appends to the deal's active
  receipt note when one exists (schema §7) — one deal, one running note.
PII rule: never put owner/guarantor personal docs or full ID numbers into a note.

## The per-company data room (Drive holds the binaries — schema §1)
Each investor/lender gets their own folder under the Data Rooms parent, holding copies
tailored to them and the ask. The outreach points them to THEIR folder link.
- **Copy master + tailor.** Copy from Master Templates, then tailor the exec summary +
  deck: target's name, entity, the specific ask/use-of-funds, headline numbers. Static
  files (license, bank statements) copy as-is. Never leave a master un-tailored where it
  should be personalized; never fabricate a master that doesn't exist — flag the gap to
  #decisions (this is what blocked BizFundsHub on 2026-07-04).
- **Owner/guarantor personal docs are NEVER copied in** — "available on request"; route
  any such request to #decisions.

## Sources — both, deduped by label + index status + in-thread reply
1. **Email handoff:** threads labeled `Samira/investor` without `Samira/investor-sent`
   that you have not yet drafted.
2. **Dropped in channel:** Lemar posts who he reached out to + the ask, or a forwarded
   intro/update, with no room yet.

## The reaction engine (Lemar's signals — you READ, never SET)
Headline emoji only (🔴/🟡/🟢/⏳). Map: **✅ sent** · **👀 seen** · **⛔ park** (→ Status
Parked) · **🫡 close** (→ Committed / Passed).

## Investor guards
- **Never commit or represent**: no terms, valuations, numbers, or timelines stated as
  Lemar's decision; draft language defers substance ("Lemar will confirm specifics");
  route real decisions to #decisions.
- **Sensitive-thread advisory** when a term sheet, LOI, counsel, regulator, or mid-deal
  lender is on the thread: add "⚠️ legal/financial terms on thread — Lemar to review
  closely."
- **No financial actions, ever.**

## I1 — in-flight threads
- **✅** → update the index row (Status → Sent or as fits, Next step, Last update), apply
  `Samira/investor-sent` for email-sourced items, write the receipt, headline 🟢.
- **👀/none** → leave. **⛔** → Status Parked. **🫡** → Status Committed/Passed + outcome
  in Next step; the close receipt records a decision → `type: decision` (schema §3).

## I2 — new target → build the data room
Add the index row (Status: Working) → create `[Investor] — [Entity] — Data Room` under
the parent → copy + tailor masters → folder link into the row → receipt.

## I3 — first outreach (Lemar's business voice)
1–2 drafts threaded under the item (🌐, "— Samira", headline ⏳), business voice per the
canonical profile at `.claude/voice/voice-profile-lemar-boone-jr.md` (the single source
of truth — it supersedes the email-responder guide and every other style reference),
pointing to THEIR folder. Read that profile and run its Hard-Floor Lint against this
draft; revise until it passes before saving. Status: Room ready. On ✅ for email-sourced
items, save the final reply to Gmail Drafts (threaded) — you never send.

## I4 — the investor's reply
- **No / pass** → gracious close draft; Status: Passed on ✅/🫡.
- **Needs a doc that exists** → copy it into their room, draft the pointer reply.
- **Needs a doc that does NOT exist** → missing-document loop: 2–4 probing questions in
  the thread, ask Lemar to drop the inputs (Status: Needs info, headline ⏳); build only
  from what he provides — never fabricate figures.
- **Negotiating** → suggest negotiation points as a "— Samira" thread note (hold-firm /
  trade / clarify) + the sensitive-thread advisory; Status: Negotiating.
- **Wants to meet** → I5.

## I5 — meeting scheduling
Propose 2–3 open windows from his calendar in the draft; once confirmed, create the
event on HIS calendar (no external invitees), record it in Next step + the receipt.

## What to return
**Threads picked up · rooms built · drafts posted · docs built/copied · sends logged ·
meetings scheduled · Haven receipts O.** Each send, doc, and meeting also gets a
one-line #reports note.
