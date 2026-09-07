# #decisions migration — step 1 batch 2 closures

Part of the three-conversation restructure migration
([[migration-2026-09-three-convos]]). Step 1 triaged the next 15 oldest open
#decisions threads (channel `C0BBXA96FFV`), oldest first. 9 were still live and
migrated to fresh doctrine-format cards in Convo 1 (`D0BHPKMDNEP`); the 6 below
were stale/superseded/done and closed out here instead of getting individual
Haven notes, per the runbook's batching rule.

Tool note: Samira has no message-edit capability, so each original thread got a
threaded reply reading "✅ CLOSED — migrated out (...)" in place of the
runbook's "edit the parent" instruction.

## Closed threads

| Original ts | Topic | Reason closed |
|---|---|---|
| `1787231683.266619` | Curaleaf/AGA collections notice, $25,601.41 | Duplicate of the canonical 8/13 Curaleaf/AGA thread (`1786631846.014899`) — Samira self-corrected same day, consolidated onto `haven/vault/20-Cuzzies/2026-08-13-curaleaf-nj-ii-collections.md` |
| `1787238798.497049` | GTI AR (Mindy) account review, reply drafted | Superseded by the 8/21 follow-up thread (`1787314456.900919`) on the same matter, which is itself already closed |
| `1787314456.900919` | GTI AR review — "saved" draft wasn't actually in Gmail Drafts | Already resolved in-thread 8/21: Lemar reached out to Mindy directly himself, Samira logged it and replied "Done ✅ — closed" |
| `1787401047.824359` | #reports "waiting on you" count unreconciled since 8/15 | Resolved and logged 8/22 — Lemar picked Option 1, Samira ran the full #decisions backlog audit (31 cards tracked, 6 functionally closed but unreacted, 25 genuinely open) and reconciled the digest count. See `haven/vault/40-Projects/samira-skills/2026-08-22-decisions-backlog-audit.md` |
| `1787408466.876989` | AI-sent emails on Station's CRC license renewal (Eden Estates disclosure) | Closed in-thread 8/22 — Lemar picked Option 3, confirmed the exchange was authorized/known, false alarm, no action taken. See `haven/vault/30-Station/2026-08-22-eden-estates-disclosure-ai-sent-emails-incident.md` |
| `1787495798.327079` | haven-calendar-sync recurring bug — wrong-calendar false positives | Already resolved 8/23 — Lemar picked Option 1, Samira patched the sync logic (domain-based calendar resolution) and logged the fix. See `haven/vault/70-Automation/haven-calendar-sync/2026-08-23-patched-wrong-calendar-recreate-bug.md` |

## Sources
- slack: https://newworkspace-zlb6313.slack.com/archives/C0BBXA96FFV (original #decisions threads, tss above)
- repo: `.claude/routines/migration-2026-09-three-convos.md` (governing runbook, step 1)
