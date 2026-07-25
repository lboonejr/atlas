---
created: 2026-07-25T08:35:00-04:00
updated: 2026-07-25T09:03:46-04:00
domain: reference
type: log
status: done
tags: [infra, data-integrity, github-api, bugfix]
source: claude
---

# Repaired double-base64-encoded Haven notes (8 notes, main branch)

During this scan's PART D/G work, a note (`haven/vault/60-Legal/2026-07-21-dewalt-v-cuzzies-default-judgment.md`)
was found stored on `main` as a raw base64 blob instead of plain markdown — a prior
write via the GitHub `create_or_update_file` MCP tool had the content base64-encoded
twice (once by the caller, once by the tool/API itself). A full-vault scan for files
not opening with the frontmatter `---` delimiter turned up 7 more affected notes,
ranging from today back to 2026-07-05:

- `haven/vault/60-Legal/2026-07-21-dewalt-v-cuzzies-default-judgment.md`
- `haven/vault/00-Inbox/2026-07-25-slack-payment-failed.md`
- `haven/vault/00-Inbox/2026-07-25-unverified-nj-counsel-solicitation.md` (the
  possible-fraud flag — this one mattered, it would have been unreadable)
- `haven/vault/20-Cuzzies/2026-07-05-leafly-missed-payment.md`
- `haven/vault/20-Cuzzies/2026-07-06-needham-bank-sba-documents-done.md`
- `haven/vault/20-Cuzzies/decisions/2026-07-06-gusto-payroll-shortfall-cancel.md`
- `haven/vault/20-Cuzzies/2026-07-06-parke-bank-nsf-elevate-funding.md`
- `haven/vault/20-Cuzzies/2026-07-14-first-insurance-funding-license-inactive.md`

All 8 decoded cleanly to complete, well-formed notes — nothing was lost, just
mis-encoded on write. Restored the real content on `main` (two commits this scan).

**Root cause, for whoever fixes the tool-calling pattern:** `create_or_update_file`'s
`content` parameter expects raw text; it (or the underlying GitHub API path) handles
base64 encoding internally. Any skill/agent that pre-encodes the content itself before
passing it produces this double-encoding. Worth a note in the skills that write Haven
notes (haven-capture, samira-report-result, etc.) to pass raw text, never pre-encoded.

No #decisions card needed — a repair, not a decision. Logged here + one #reports line.
