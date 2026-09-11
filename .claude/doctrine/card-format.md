# The card format — one definition for every conversation

This file is the ONE definition of a task card. The runbook and every skill point here;
no other file may restate the format (same single-source rule as `.claude/anchors.md`
for IDs). A "card" is how any task, project, fix, or open matter lives on a
conversation surface.

## Where cards live

Cards exist on exactly two surfaces (IDs in anchors):
- **Convo 1 — "What we're working on now"** — the Samira DM. Work between Lemar and
  Samira: tasks, projects, decisions, follow-ups.
- **Convo 3 — "Fixes"** — the private #fixes channel. Same mechanics; the subject is
  Samira herself (bugs, errors, missed runs, inconsistencies, contradictions).

One card = ONE threaded parent message. Everything about the matter happens in that
thread. Project channels are append-only timelines and NEVER host a card. Convo 2 (the
self-DM) is intake, not a card surface — work there graduates into a Convo 1 card.

## The four elements

Every card carries these four elements, in this order.

### 1. Headline (the parent message)
`[headline emoji] [topic emoji] *[~5-word summary]*` — optimized for scanning and
finding it later. The far-left headline emoji is Samira's status render (🔴 decide now
· 🟡 decide soon · 🟢 ready to send · ⏳ waiting), updated by editing the parent. **This
is the "status from the parent" mechanism** (locked 2026-09-06, per Lemar): scanning
the channel's list of parent messages — without opening any thread — tells him what's
live. ⏳ specifically means "Samira is waiting on you" on that card; 🔴/🟡/🟢 mean the
ball is in Samira's court (still deciding, drafting, or ready). Keep this emoji current
every pass a card is touched — a stale headline defeats the whole point.

Right after the headline emoji, a **topic emoji** (adopted 2026-09-07, per Lemar) names
the card's subject at a glance without opening the thread — e.g. 💰 money, ⚖️ legal, 🔧
build/automation, 🏛️ admin/filing, 🏗️ project/launch. Samira picks the closest fit per
card; it never changes the signal meaning of the headline emoji, it's purely a topic
label. Examples: `🔴 💰 *Curaleaf collections — $25,601.41*`, `🟡 🏗️ *Camden Launch —
client intake system*`.

If a subheading is needed, it is the FIRST reply in the thread, before Context.

### 2. Context (one reply)
Two parts, one message:
1. An explain-like-I'm-13 rundown, **600–900 characters**, covering the who, what,
   where, when, and why of the situation. Plain words, no jargon.
2. A `Sources of truth:` block — the Haven note path (always), plus any files, due
   dates, contact info, and relevant links. Omit lines that don't apply; a genuinely
   unknown item is written as unknown, never invented. If nothing is known yet, the
   block stays blank.

### 3. Decisions (one reply per option, as many rounds as it takes)
Samira proposes what should be done next. Each option is its OWN thread reply so it
can be reacted to individually. Multiple rounds are normal — if the first round
surfaces nuance, the next round narrows it. Pressure-test rounds (the samira-loop
eight lenses, a Stormy-graduated question set) are decision rounds under this same
element — same thread, same signals.

**Every card gets a real option reply — including single-action cards** (locked
2026-09-06, resolving a collision with the parent-headline status render above): a
card with only one thing to do still gets an `↳ [Action] ✅ to pick` reply, exactly
like a multi-option card. Bare ✅-on-the-parent-message is NEVER read as "execute" —
the parent is reserved for the headline status emoji, never an action trigger. This
retires the older "single-action-parent ✅=execute" shortcut everywhere it appears.

**Computer-action options get a paired Claude-and-Chrome prompt** (locked 2026-09-11,
per Lemar — Convo 2 thread ts `1789134644.637969`). Whenever an option is something
Samira cannot do herself — it requires Lemar's own logged-in session (a government
portal, a bank/vendor account, anything gated behind credentials Samira doesn't hold)
— that option's reply is paired with a ready-to-paste Claude-in-Chrome prompt (the
loop's "browser lane": Lemar's own logged-in browser, him present, never submits,
pays, sends, or clicks a binding button on its own). The prompt is a direct, runnable
instruction — what to check/do, what to report back, explicit that it reads/reports
rather than submits unless Lemar says otherwise — so he can act on it immediately
instead of waiting for a future pass. This does not change what Samira does
unattended; it only means a "you'll need to do this yourself" option always ships
with the exact prompt to do it, instead of a bare description of the blocker.

**Signals — reactions AND replies.** The emoji engine is unchanged: reactions are
LEMAR'S signals, Samira reads them and never sets them — ✅ choose/execute/sent ·
👀 seen (no nudge) · ⛔ park · 🫡 close · 🔔 revisit next run (added 2026-09-07, per
Lemar — "reads like 👀 for now, but ALSO surfaces the card again on Samira's next
Convo 1 pass instead of going quiet, a standing nudge until cleared with
✅/⛔/🫡"). But a plain REPLY from Lemar is an equal, first-class
signal read every pass: a reply can add nuance to an emoji, override an option, or
answer a question with no reaction at all. When a reply and a reaction conflict, the
reply wins (it carries more information); when in doubt, ask in-thread rather than
guess.

**Reaction key, for quick reference:**
| Reaction | Meaning |
|---|---|
| ✅ | choose this option / execute / confirmed sent |
| 👀 | seen — no action, no nudge |
| ⛔ | park this line/card |
| 🫡 | close the card |
| 🔔 | revisit on Samira's next Convo 1 pass — a standing nudge until cleared |

**When a plan locks**, Samira executes what she safely can, in-thread:
- Anything with a **due date** → an event on Google Calendar (routed per the
  haven-calendar-sync domain rule).
- Any **call to be made** → a calendar event with the call script attached to the
  event, so the conversation's purpose is in hand when it rings.
- Any **document or email needed** → drafted (Drafts only, never sent), with a link
  posted back in the thread. Everything made gets a link — nothing invisible.
- Any **open items only Lemar can do** → an HTML to-do list artifact, linked in the
  thread, so he can track what's on him.

### 4. Follow Up (after lock, or after prolonged silence)
Once decisions are locked — or when a card has sat with no decision for a while
(2-day rule) — Samira checks in, in-thread: did it get sent? did it move forward? was
the call made? was the document signed? She nudges the open items that are Lemar's,
reads his replies for anything she can continue working, files what needs filing,
verifies the Haven note is fully updated, and then closes out: record the outcome via
samira-report-result, then post a `✅ CLOSED — [outcome]` reply as the thread's last
message (locked 2026-09-11, per Lemar — no tool in either Slack connector can edit a
message, so "edit the parent" was never actually achievable; every prior close attempt
landed only as an unmarked thread reply, which a headline-only scan can't see, so
closed cards kept re-surfacing as open for weeks). **A card counts as closed when its
thread's last message is a `✅ CLOSED — [outcome]` reply** — check the thread's latest
message when scanning, not the parent text. **The instant that close reply posts,
Samira also reacts 🫡 on the parent message herself** (locked 2026-09-11, per Lemar —
Convo 2 thread ts `1789135557.913319`): the close-reply text is what makes a card
closed, the 🫡 on the parent is purely a visual marker so a headline-only glance down
the channel shows closed cards too, without opening every thread. Samira sets this
reaction herself as part of closing — it is not a signal from Lemar and never read
back as one (the reaction-reading rule — reactions are Lemar's signals, Samira never
sets them — applies to every OTHER reaction on a card; this one specific case, a
self-set 🫡 immediately following her own close reply, is the sole exception, and only
on a parent she just closed this same action). Both card surfaces trend toward empty;
the durable record lives in Haven + #reports.

## Identity per surface

- **Convo 1 and #fixes**: Samira posts 🌐-signed via her bot; Lemar posts as himself.
  Author IDs disambiguate.
- **Convo 2 (the self-DM)**: BOTH sides are authored by Lemar's own user (the bot
  cannot enter a self-DM; Samira posts there via the personal Slack connector). The
  🌐 prefix is therefore the ONLY discriminator and is load-bearing: 🌐 = Samira
  (🌐🌩️ when in deep-dive mode), un-prefixed = Lemar. Samira NEVER treats a
  🌐-prefixed message as input.

## Idempotency

Samira's done-keys are her own in-thread "Done ✅ …" replies + stored state (Haven
note, calendar_event_id, watermarks) — never Lemar's reactions. In Convo 2 the keys
are watermarks + her own threaded 🌐 replies only: a reaction set via the personal
connector is indistinguishable from Lemar's, so reactions are never used for dedupe
there. The one place ✅ is Samira's own mark: the capture-dedup ✅ on a Convo 2
message she has fully developed into a card.
