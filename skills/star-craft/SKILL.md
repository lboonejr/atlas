---
name: star-craft
description: Scan newly starred Gmail threads and draft replies grounded in the full thread context. Triggers when the user says things like "run star craft", "process my starred emails", "draft replies to starred", or otherwise asks to handle recently starred mail.
---

# Star Craft

A workflow for triaging newly starred Gmail threads. The skill **always reads the entire thread** before drafting anything — the starred message is rarely self-contained, and replies that ignore the preceding messages tend to repeat questions that have already been answered or miss context the sender assumes you have.

## When to run

Run when the user asks you to process starred mail (e.g. "run star craft", "draft responses for what I starred", "scan my new stars"). Default scope is *new* stars — threads starred since the last run — unless the user specifies a different window.

## Procedure

### 1. Find newly starred threads

Use the Gmail search tool to list starred threads in scope.

- Default query: `is:starred newer_than:1d`
- If the user gave a window ("today", "this week", "since Monday"), translate it into a Gmail `newer_than:` / `after:` query.
- Use `search_threads` (do NOT page through individual messages — we want thread IDs).

If the result is empty, tell the user "no new starred threads" and stop.

### 2. Pull the FULL thread for each result

For every thread ID returned, call `get_thread` to retrieve **every message in the thread**, not just the starred one. This is the core of the skill — context lives in the messages that came before.

For each thread, build a working summary that captures:

- Participants and their roles (who is asking what of whom)
- The chronological exchange — what was asked, answered, promised, or left open
- Any attachments, links, or references already shared
- The specific message that is starred (usually the most recent, but verify) and what it is actually asking for

Do not draft a reply based only on the starred message's body. Always reconcile it against the earlier messages in the thread.

### 3. Identify the response needed

Re-read the most recent starred message with the thread context in hand and decide:

- Is there an explicit question or request? What is it actually asking, given prior context?
- Has any part of it already been addressed earlier in the thread? (If so, the reply should reference that, not re-answer.)
- Is information missing that the user (not Claude) needs to supply? Flag it rather than inventing.
- Is no reply needed (FYI, automated notification, thank-you)? Say so and skip drafting.

### 4. Draft the reply

When a reply is warranted, use `create_draft` to create a Gmail draft on that thread. The draft should:

- Address the most recent starred message specifically
- Reflect facts and commitments from earlier in the thread (don't contradict prior messages)
- Match the tone of the existing exchange
- Leave clearly-marked placeholders (`[TODO: ...]`) for anything that requires the user's input or judgment rather than guessing

### 5. Report back

After processing all threads, summarize for the user:

- How many threads were scanned
- For each: a one-line summary, what the starred message needed, and what you did (drafted reply / flagged for user / skipped because no action needed)
- Anything you couldn't resolve and why

## Guardrails

- **Never send mail.** This skill only creates drafts. Sending is the user's call.
- **Never unstar or relabel** threads as part of processing — the user manages star state.
- If a thread is long (>20 messages), summarize the older portion but still read it; do not skip messages.
- If you find a thread where the starred message is *not* the most recent message, call that out explicitly in the report — it usually means the user starred something mid-thread for a reason.
