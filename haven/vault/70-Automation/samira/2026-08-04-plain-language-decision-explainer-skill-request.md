---
created: 2026-08-04T16:20:00-04:00
updated: 2026-08-04T16:20:00-04:00
domain: automation
type: task
status: active
tags: [skill-request, skills-lab, samira]
source: slack
---

# Skill request — "plain-language decision explainer" — approved for a dedicated build session

Lemar posted in #skills-lab (2026-08-03, ts `1785765580`): he wants a skill that
restates any technical Samira output in plain language, with the decision it's asking
him to make made explicit.

Samira flagged the shape as a #decisions card (parent ts `1785773313.507069`,
`🟡 Skill request — "plain-language decision explainer" — needs your call`). Lemar
reacted ✅ on that card.

Per the standing safety floor ("never create skills mid-run"), this is not built inside
an hourly scan — it needs a dedicated build session. Logging it here so the approval
isn't lost between scans.

**Shape (for the build session):** a translator layer that takes any technical Samira
output (Slack card, #reports line, Haven note excerpt) and restates it as: what
happened, in plain language + what decision it's asking for, in one or two lines.

## Sources
- slack: #skills-lab, Lemar's original ask (ts `1785765580`)
- slack: #decisions (C0BBXA96FFV), card ts `1785773313.507069`, Lemar's ✅
  (approved a dedicated build session)
