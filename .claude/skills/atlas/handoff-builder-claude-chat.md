# Handoff Builder — DEPRECATED (handoffs now live as Monday item Updates)

As of 2026-06-21, Atlas storage moved off Google Drive to a personal **Monday** board, and
**handoffs are no longer separate Google Docs.** A handoff is now a dated **Update on the relevant
Monday item** (board "Samira" `18418714876`). There is no handoff-builder step — Atlas writes the
handoff straight onto the item during Gear 2.

Do not create handoff Google Docs anymore. Keep the structure below; just post it as an **Update**
on the item instead of saving a Doc.

## Handoff Update format (post as a Monday Update on the item)

```
Handoff — [Title]
Date: [YYYY-MM-DD HH:MM ET]
Item: [Item ID]   (the Monday item this Update is on)
Moving: [from] to [to]   (e.g. Claude to Slack, Slack to Gmail)

Purpose
  [Why this handoff exists. One or two lines.]

Context
  [What has happened, decisions made, current state. Plain English. Quote key facts.]

The ask / next action
  [Exactly what the receiver should do: the single concrete outcome, written so they can act with
  no extra context.]

References
  [Doc/board IDs, channel IDs, prior message links, attachments the receiver needs.]

Open / pending
  [Anything unresolved, awaiting a decision, or a risk to flag. Or "none."]
```

## Principles (unchanged)
One handoff, one clear next action. Self-contained: the receiver should never have to ask "what did
you mean." Capture context, do not invent it; if a fact is missing, flag it under Open/pending
rather than guessing. Never send the handoff anywhere outward yourself; you write the Update,
Lemar (or Atlas) sends. Voice: no em dashes, "we" by default, no medical claims, no competitor
names, no ALL CAPS.

Note: the bundled Anthropic `handoff-builder` skill writes Google Docs and is no longer used by
Atlas — leave it unused, or repurpose it later if needed. See [[atlas-orchestrator]],
[[shortlist-anchors]].
