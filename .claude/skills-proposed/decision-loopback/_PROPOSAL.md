mode: new
slug: decision-loopback
target: .claude/skills/decision-loopback/SKILL.md
spec_note: haven/vault/00-Inbox/2026-08-03-skill-spec-decision-loopback.md
card_ts: 1785765937.619699
forged: 2026-08-03
status: pending
self_check: |
  1. name matches directory, kebab-case, no live collision — PASS
     (roster read 2026-08-03: atlas, haven-calendar-sync, haven-capture, haven-vault-keeper,
     meeting-prep, morning-brief, on-button-plan, pulse-dashboard, samira-car-search,
     samira-email-loop, samira-investor, samira-report-result, skill-forge, stormy)
  2. description names trigger phrases AND the never-does line — PASS
  3. every step executable with tools Samira has today (slack_read_channel,
     slack_read_thread, slack_send_message) — PASS
  4. SAFETY block present, no broader than Samira's — PASS
     (posting to a project channel is already permitted; PART G already directs this
     exact message, so the skill claims no new capability)
  5. states the digest token — PASS (`loopback: N posted · M skipped` / `loopback idle`)
  6. names its Haven writes — PASS (explicitly none, with the schema §7 reason)
notes: |
  Forged during the supervised PART H test run Lemar requested 2026-08-03, on branch
  claude/samira-self-skill-creation-0s82up (NOT main — skill-forge itself is still
  unmerged in PR #46). Promotion must wait until that PR merges, otherwise the promoted
  skill would land on a branch the executor does not read.
