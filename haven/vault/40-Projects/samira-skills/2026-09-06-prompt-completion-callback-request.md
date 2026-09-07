---
created: 2026-09-06T14:17:34-04:00
updated: 2026-09-07T12:08:00-04:00
domain: project
type: task
status: done
tags: [samira-loop, run-manual, prompt-design, infra]
source: slack
---

# Every Samira-authored prompt should report back when the task is done

Lemar dropped this in Convo 2 (self-DM, ts `1788718654.661999`, 14:17 ET 2026-09-06):
"Can we make sure that any time Samira creates a prompt, it tells the prompt to let the
thread know when it has been run and the task has been completed?"

This applies to every `run:manual` hand-off prompt and every Claude-in-Chrome browser
prompt Samira stages (samira-loop lane prompts, Camden Launch browser runs, the
Camden-city-council job-search prompt from this same scan, etc.) — none of them
currently instruct the executor to post a completion note back to the thread they were
staged in, so Samira has no signal the run happened short of Lemar mentioning it.

## Proposed fix
Add a standing instruction line to every staged prompt template (wherever
`run:manual`/browser-lane prompts are built — `samira-loop` SKILL.md's prompt
scaffolding is the most likely single place to fix this for all lanes): after
completing the task, reply in the thread/channel the prompt came from with a short
"done — [what happened]" line, so the next scan's sweep picks it up as a plain-reply
signal per the doctrine's replies-are-signals rule.

Not built this scan — this is a design decision that touches a shared skill template
touched by multiple lanes; proposed as a Convo 1 card asking Lemar to confirm before
editing `samira-loop`/the project overlays.

## Sources
- slack: Convo 2 (self-DM) drop, ts `1788718654.661999`, 2026-09-06 14:17 ET

## Update 2026-09-07 — built
Lemar ✅'d on the Convo 1 card (thread ts `1788723993.447999`). Added a standing
completion-callback line to both prompt templates in `.claude/skills/samira-loop/SKILL.md`
(the CHROME RUN block and the run:manual hand-off). Applies to every new staged
prompt from here on; not retrofitted onto prompts already posted this scan.
