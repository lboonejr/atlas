---
created: 2026-09-16T11:48-04:00
updated: 2026-09-17T14:10:00-04:00
domain: project
type: reference
status: active
tags: [notary, journal, records-request, subpoena, compliance, unresolved-legal]
source: claude
---

# Playbook — somebody wants a copy of the journal

Ten years of retention makes this a matter of when, not if. A title company checking a signing,
a lawyer in a dispute, a party who claims a signature is not theirs, or a court. Related:
[[2026-09-15-notary-business-backend-systems]] and
[[2026-09-16-notary-seal-journal-loss-playbook]].

## Read this first — the legal question is genuinely unresolved

**Who may compel a copy of a NJ notary journal, and on what terms, could not be established
from public sources.** N.J.A.C. 17:50-1.11 sets what the journal must contain and that it is
kept ten years. It does not, in anything findable, say who may inspect it, what must be
redacted, or what may be charged.

That is not a gap in the research effort, it is a gap in what is published. So this playbook
covers the **operational** response, which is sound regardless, and stops short of the legal
question, which is not mine to answer.

**Before the first request arrives, ask DORES:** is the journal subject to inspection or copy
requests, by whom, must anything be redacted, and may a fee be charged. Record the answer in
this note and this warning comes out.

## The one distinction that governs everything

**A request is not a subpoena.**

- **A request** is someone asking. Lemar may say yes, no, or not yet. Nothing compels him and
  nothing is urgent.
- **A subpoena or court order** compels. It has a deadline, and ignoring it has consequences
  that requests do not carry.

Treat them as two different events with two different clocks. Sorting an incoming ask into the
right bucket is the first move, before drafting a single word of reply.

## If it is a request

1. **Do not hand anything over the same day.** There is no deadline. Nothing is gained by speed
   and a lot can be lost.
2. **Write down who asked, when, for which entries, and why.** That log is itself a record worth
   having, and it goes in this note as an Update.
3. **Give the narrowest thing that answers the question.** One entry beats a page; a page beats
   the book. A journal is a chronological record of *other people's* business — handing over a
   whole page exposes unrelated signers who never consented to anything.
4. **Check with DORES or a NJ attorney before a first-of-its-kind request**, and record what
   they say so the second one is easy.

## If it is a subpoena or a court order

1. **Note the deadline immediately** and treat it as real.
2. **Talk to a lawyer before responding.** This is the one place in the whole notary operation
   where "figure it out myself" is the wrong instinct. A commission is not a law licence.
3. Produce what is ordered, no more, and keep a copy of exactly what went out and when.

## The thing most people miss: the vendor holds it too

The journal of record lives in **BlueNotary**, not in a drawer. So:

- A subpoena may go to the **platform** rather than to Lemar, and he may learn about it late or
  not at all. Worth knowing what the vendor's policy is on notifying a notary when their records
  are subpoenaed — a question for BlueNotary at signup, in Phase 2.
- If the vendor account ever lapses, the **monthly export in the Drive folder is the only copy
  that answers a request**. Another reason that export never slips.

## What Samira may and may not do

**May:** log that a request arrived and its details, draft a holding reply in Lemar's voice
("received, I will come back to you"), set a reminder against a subpoena deadline, and retrieve
the relevant export from the Drive folder for him to review.

**May not:** send journal contents to anyone, decide what is producible, redact anything,
characterize the request's legitimacy, or answer a legal question about it. **Never attach or
paste journal contents into a Slack message, an email draft, or a card** — the whole design
keeps signer PII out of those surfaces, and a records request is exactly the pressure that would
break it.

## Sources
- claude: Claude Code session, 2026-09-16 — N.J.A.C. 17:50-1.11 confirms journal contents and
  ten-year retention; inspection, redaction and fee rules were searched for and **not found** in
  public sources, and are flagged unresolved above
