---
name: doc-naming
description: >
  The one naming authority for every document Samira produces — docx, xlsx, pptx, pdf,
  data-room files, prep docs, exports. Returns a single standardized filename,
  `YYYY-MM-DD-subject-in-kebab-case.ext`, so a document sorts and reads exactly like the
  Haven note that records it (schema §5). Call it in-process before writing any document,
  in PART C, the investor data-room builds, and meeting-prep; also on demand: "what should
  this file be called", "name this doc", "rename convention". It returns a string and
  nothing else — it never writes, moves, renames, or deletes a file, never renames a
  document that has already been delivered or linked, and never touches Slack, email, or
  the vault.
---

# Doc naming — one filename rule, borrowed from the vault

Lemar's ask, verbatim: *"every doc that Samira creates [gets] a clean, easy to reference
file name. The name should include the subject and the date in a standardized format."*

The vault has had exactly this rule since day one (schema §5: `kebab-case`, date-led when
time-bound). Documents never inherited it, so every filename has been improvised. You are
that rule, carried across the boundary. **You invent no second convention.**

## ANCHORS
Platform IDs live in **`.claude/anchors.md`**. The naming convention itself lives in
`haven/vault/_system/schema.md` §5 — that file is the authority; if it changes, you change
with it and this skill is what needs revising.

## SAFETY — inherits Samira's SAFETY block; this skill's own floor

You MAY: read the pending document's subject and the task that produced it; return a
filename string.

You MUST NOT, ever: write, move, rename, or delete any file; **rename a document that has
already been delivered, attached, or linked** — outcome notes and mirror items point at
those names, and breaking a link is the "never overwrite existing content" rule wearing a
different hat; post anywhere; touch the vault; put an SSN, ID number, bank number, or any
full account identifier into a filename (filenames leak into previews, Slack unfurls, and
Drive listings — treat every one as public); silently truncate a name so far that two
different documents collide.

## The format

```
YYYY-MM-DD-subject-in-kebab-case.ext
```

- `2026-08-03-parke-bank-returned-items-summary.pdf`
- `2026-07-31-garden-society-past-due-ar.xlsx`
- `2026-08-04-gusto-w2c-review-agenda.docx`

Rules, in order:
1. **Date first, ISO, always.** Sorting a folder by name sorts it by time. That is the
   whole reason the vault leads with dates.
2. **Which date**: the document's **subject date** when it is unambiguous (the meeting's
   date, the invoice period, the deadline being prepped for) — an invoice from July filed
   in August reads as July, because that is what someone searching will remember.
   Otherwise the **creation date**. Never both.
3. **Subject in kebab-case**: lowercase, hyphens, no spaces, no underscores, no camelCase.
4. **Name the counterparty when there is one** — `parke-bank`, `garden-society`. That is
   the word Lemar will actually search for.
5. **3–7 words.** Under three is unsearchable; over seven is a sentence.
6. **No status words** — no `final`, `v2`, `latest`, `updated`, `FINAL-final`. The date
   already carries recency and the words rot immediately.
7. **ASCII only**, plus the hyphen and the extension dot. No `&`, `/`, `:`, `#`, `%`, or
   emoji — they break URLs, shell paths, and Drive search in different ways each.
8. **Extension matches the real format.** A spreadsheet is `.xlsx`, never `.doc`.

## Collisions

If the name you would return already exists in the destination, **do not overwrite and do
not silently append a number.** Add the distinguishing word that actually differs —
`-part-2`, `-camden`, `-station`, `-revised-terms`. If nothing distinguishes them, they
are the same document and the second one should not be written; say so rather than
inventing a suffix that carries no meaning.

## Procedure

1. Take the subject from the task that is producing the document, not from its first line
   of content.
2. Pick the date per rule 2. If the subject date is genuinely ambiguous, use creation date
   — do not stall a document over a filename.
3. Assemble, apply rules 3–8, check length and collisions.
4. **Return the string.** You are done. The caller writes the file.

## What you return for the digest

Nothing. You are called in-process many times per run and have no digest line of your own;
the documents you name are already reported by the tasks that produce them.

## Vault writes

**None.** You are a naming function.
