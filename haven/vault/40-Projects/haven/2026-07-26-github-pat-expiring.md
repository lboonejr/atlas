---
created: 2026-07-26T15:00:00-04:00
updated: 2026-07-26T15:00:00-04:00
domain: project
type: task
status: active
tags: [github, token, infra, samira, haven]
source: gmail
---

# GitHub fine-grained PAT ("Haven / Samira") expiring in 7 days

GitHub notification received 2026-07-26 18:11 UTC (`noreply@github.com`, thread
`19f9f9f97c1fa455`, no Label_2 prior — genuinely new mail this scan): the
fine-grained personal access token named **"Haven / Samira"**
(`https://github.com/settings/personal-access-tokens/16549774`) will expire in
7 days (~2026-08-02).

## Why it matters
Per `.claude/anchors.md`, this repo's GitHub MCP connector is the transport
Samira/Dawn/Basil's cloud routines use to read/write `main` (Haven vault,
skills, routines). If this token isn't regenerated before expiry, every
hourly/scheduled cloud run loses git write access — vault notes, index
updates, and Haven receipts would silently stop landing.

## Action needed (Lemar)
Visit the regenerate link and issue a new fine-grained PAT with the same
scopes before ~2026-08-02:
`https://github.com/settings/personal-access-tokens/16549774/regenerate`

This is a credential-rotation action outside Samira's authority (can't
generate/rotate a GitHub PAT on Lemar's behalf) — flagging for Lemar to
action directly. No reply/draft applicable (system notification, not a
correspondent).

## Sources
- gmail: thread `19f9f9f97c1fa455`, message `19f9f9f97c1fa455`,
  noreply@github.com → lemar@cuzziesnj.com, 2026-07-26T18:11:03Z
