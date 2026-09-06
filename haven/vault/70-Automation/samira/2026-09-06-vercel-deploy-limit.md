---
created: 2026-09-06T13:44-04:00
updated: 2026-09-06T15:25-04:00
domain: automation
type: task
status: active
tags: [vercel, infra, samira-slack-bot]
source: slack
---

# Vercel deploy limit — hitting it, want to cut down and fix

Lemar dropped this in Convo 2 (self-DM, ts `1788716656.786379`, 13:44 ET 2026-09-06):
"I keep hitting the limit on my Vercel deploys. Just trying to figure out how we can
cut down on these and fix this."

Most likely source: the Samira/Dawn Slack bot apps (`apps/samira-slack-bot/` in this
repo), each deployed as its own free Vercel project (Samira, Dawn). Every commit to
`main` that touches the bot code (or possibly the whole repo, if the Vercel project's
root/ignored-paths aren't scoped) triggers a production redeploy — with the volume of
Haven vault writes + routine edits happening on `main` multiple times an hour, that
adds up fast on a free-tier deploy quota.

Advisory only — nothing changed, this is Lemar's Vercel account.

## Suggestions
1. **Scope the Vercel project's "Ignored Build Step"** to only redeploy when files
   under `apps/samira-slack-bot/**` (or the relevant bot dir) actually change — a
   vault-only or routine-doc-only commit shouldn't trigger a redeploy at all. This is
   likely the single biggest win, since haven/vault writes vastly outnumber bot code
   changes.
2. **Batch commits** before triggering a redeploy where possible, instead of pushing
   many small commits in a row.
3. **Use a preview-branch workflow** for bot changes (push to a branch, preview
   deploy, merge to main only when ready) instead of every commit going straight to
   production.
4. **Check CI/webhook config** — confirm nothing else (a GitHub Action, a webhook) is
   triggering redundant redeploys beyond Vercel's own git integration.
5. If usage is genuinely growing (more routines, more traffic), Vercel's paid Pro tier
   raises the deploy/build-minute caps — worth it only if the above scoping doesn't
   solve it.

## Sources
- slack: Convo 2 (self-DM) drop, ts `1788716656.786379`, 2026-09-06 13:44 ET
