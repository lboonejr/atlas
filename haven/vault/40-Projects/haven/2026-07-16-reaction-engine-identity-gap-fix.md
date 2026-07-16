---
created: 2026-07-16T16:12-04:00
updated: 2026-07-16T16:12-04:00
domain: project
type: decision
status: done
tags: [samira, infra, slack, identity-gap, decision]
source: slack
---

# Reaction-engine identity gap — Option 1 picked (dedicated Slack bot for Samira)

Samira's #decisions card (2026-07-16, thread ts `1784211568.458679`) flagged that every
Samira post/reaction was going through Lemar's own Slack account (`U0BC5UTHYG4`), making
her self-tag reactions (the card's own headline emoji) indistinguishable from Lemar's
real picks. Two options were offered:

- **Option 1 (picked, ✅)** — invite a dedicated Slack bot/app user for Samira to post
  and react through, so her identity is distinguishable from Lemar's going forward.
- Option 2 — leave it as-is, keep inferring from context.

Lemar reacted ✅ on Option 1. This was executed the same day: a custom Slack connector
named "Samira" (connector_uuid `01519dfa-b91a-47eb-beb4-cdc04444144e`, bot user
`U0BJQ771LJU`, app `A0BHSG2CA7P`, MCP endpoint `https://samira-two.vercel.app/mcp`) was
swapped into the hourly trigger's `mcp_connections`, replacing the shared personal Slack
connector for Samira only (Dawn and Basil are unaffected — they still use the personal
connector). Verified live with a smoke-test post in #decisions the same afternoon. Full
detail recorded in `.claude/anchors.md` under "Cloud routine — Samira".

This note is the closing receipt for the #decisions thread — the fix was already live by
the time of this scan, so this run posted a "Done ✅" catch-up reply and is filing this
record now rather than executing anything new.

Going forward: any reaction from `U0BC5UTHYG4` on a card posted by the new bot identity
(`U0BJQ771LJU` / `A0BHSG2CA7P`) is unambiguously Lemar's — no more self-tag inference
needed on new cards. Older cards (posted via the old identity, `A08SF47R6P4`) still need
the headline-emoji-vs-offered-option-emoji inference rule.

## Sources
- slack: #decisions thread `1784211568.458679` (card + Option 1/Option 2 replies)
- repo: `.claude/anchors.md` — "Cloud routine — Samira" section, "Last verified: 2026-07-16"
