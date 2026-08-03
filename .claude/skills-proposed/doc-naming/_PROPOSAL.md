mode: new
slug: doc-naming
target: .claude/skills/doc-naming/SKILL.md
spec_note: haven/vault/00-Inbox/2026-08-03-skill-spec-doc-naming.md
card_ts: 1785765953.893389
forged: 2026-08-03
status: pending
trigger: direct-request (Lemar, #skills-lab ts 1783694505.201439, 2026-07-10)
self_check: |
  1. name matches directory, kebab-case, no live collision — PASS
     (roster read 2026-08-03; nothing names or covers document filenames)
  2. description names trigger phrases AND the never-does line — PASS
  3. every step executable with tools Samira has today — PASS
     (it is a pure string function; it needs no tool at all)
  4. SAFETY block present, no broader than Samira's — PASS
     (strictly narrower: it writes nothing anywhere, and explicitly refuses to rename an
     already-delivered document, which would break outcome-note links)
  5. states the digest token — PASS (explicitly none, with the reason: called in-process
     many times per run; the producing tasks already report)
  6. names its Haven writes — PASS (none; it is a naming function)
notes: |
  Forged during the supervised PART H test run Lemar requested 2026-08-03, on branch
  claude/samira-self-skill-creation-0s82up (NOT main — skill-forge is unmerged in PR #46).

  This forge used the DIRECT-REQUEST evidence path, which did not exist when the test run
  started: skill-forge step 2 originally demanded ">=3 dated occurrences, no evidence no
  forge" while also listing "Lemar asked directly" as a valid trigger — contradictory, and
  it would have forced either a refusal or invented occurrences. Fixed in the same session
  before this forge ran; the runbook's PART H floor line was updated to match.

  One open question is deliberately left on the card rather than guessed: whether the date
  should be the document's subject date or its creation date. The proposal defaults to
  subject-date-when-unambiguous and says so; Option 2 on the card is where Lemar changes it.
