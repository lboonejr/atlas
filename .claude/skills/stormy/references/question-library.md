# Fallback question library

**This is not a script.** Stormy's instrument is adaptive (SKILL.md Phase 2): she writes
questions for the specific idea and sizes the count to its blast radius. This file is a
**library of stock wordings** to raid when a dimension is genuinely generic and the stock
phrasing is the clearest way to ask it.

**Rules for using this file**

- Never run it top to bottom.
- Never ask a stock question when a specific version of it exists for the idea at hand.
- Never ask a stock question whose answer is already obvious — record it as an assumption instead.
- Reaching for more than about half of these on one idea is a signal you have not read the
  idea closely enough to find its crux.
- Everything here assumes **one owner: Lemar**. The business-shaped variants at the bottom
  are for the exception case only.

---

## History (why the fixed form is gone)

Retired as a mandatory instrument 2026-08-15. The failure it caused: on
`money-hub-rebalance-steward` — a personal-ledger software change with one owner — four of the
fifteen came back "Lemar only," "none," "no," and "N/A." Four questions, zero information, and
none of them asked the thing that actually mattered (how aggressive the rework logic should
default to).

De-business-ified the same day. The original form asked every idea who the approver was, which
regulated areas it touched, and whether it could be delegated and at what reporting cadence —
scaffolding from a multi-store operation, applied to a tool Lemar builds for himself. Two
dimensions were repointed rather than deleted: **compliance → blast radius & reversibility**,
and **delegation → ownership & upkeep**. Those are the versions of those questions that
actually bite on a personal tool.

---

## Dimension 1 — Problem & payoff

**What does this actually change for you?**
Saves time / removes a recurring annoyance / catches something you keep missing / makes a
decision for you / makes money visible / builds a capability you don't have / scratches
curiosity.

**What do you do today instead, and what does that cost you?**
Short text. The honest answer is often "nothing, I just live with it" — worth knowing, because
it sets the bar the built thing has to clear.

## Dimension 2 — Scope & hardest constraint

**What's IN, what's OUT, and what's the single biggest limiter?**
Two-part short text — scope description plus the real limiter (your time, money, a tool you
don't have, an API that won't cooperate, something upstream that has to change first).

## Dimension 3 — Success & failure

**What does it look like when this is working?**
Short text. Push for something observable, not a feeling.

**Smallest version that would still be worth having?**
Short text. This is the one that most often shrinks a project by two phases.

**What would tell you to pull the plug?**
Short text. If there is no such signal, the idea has no failure mode defined and that is
itself the finding.

## Dimension 4 — Dependencies & risk

**What's most likely to stop this?**
Your attention / a tool or API you don't have / it depends on something else shipping first /
the data isn't there / cost / it turns out to be boring once built.

**Does anything else have to exist first?**
Short text. Usually another skill, a connector, or a piece of the vault that isn't structured yet.

## Dimension 5 — Timing & preconditions

**When do you want this live?**
ASAP / next few weeks / whenever the dependency clears / no rush, bake it and sit on it.

**What has to be true before it can start?**
Short text.

## Dimension 6 — Blast radius & reversibility

*(Replaced the old compliance question. This is the version that matters for a personal tool.)*

**What happens when it gets something wrong?**
You ignore one bad suggestion / you lose a little time / it writes something wrong into the
vault / it moves real money / it sends something outward you can't unsend.

**Does anything leave your control?**
Multi-select: money moves / mail or a message sends / something posts publicly / an existing
note or ledger gets overwritten / a calendar event fires at someone else / nothing, it only
proposes and stops.

**How do you undo it?**
Short text. "It only proposes, so there's nothing to undo" is a complete and very good answer —
and it is the shape most of his tools should have.

## Dimension 7 — Automation & data flow

**What should happen without you touching it?**
Runs on a clock / fires off an event in another skill / only when you ask / never, it's a
one-time build.

**Where does truth live, and where do you see it?**
Short text. Default is Haven for truth and a Slack surface for the view — challenge anything
proposing a second source of truth, and challenge a new dashboard when an existing one has a
place for it.

## Dimension 8 — Ownership & upkeep

*(Replaced the old delegation question. He is the owner; the real question is what runs it.)*

**Who runs it once it exists?**
You by hand / Samira's hourly run / Dawn's daily run / a named skill, fired on demand / it
rides inside a skill that already runs.

**What does it cost to keep alive?**
Nothing, it's inert until called / a slice of an existing run / a new scheduled thing to
maintain / an external dependency that will eventually break.

**How do you find out when it breaks or drifts?**
Short text. Silent failure is the standard way one of these dies — a tool that quietly stops
firing looks exactly like a tool with nothing to report.

---

## The exception case: an idea that reaches a business or an outside party

Rare. Only raid these when the idea genuinely involves Cuzzie's, The Station, or someone
outside — never by default, and never to pad a question count.

**Who besides you has to sign off or be heavily involved?**
Name the role, not the person. Flag it plainly: this puts the idea outside Stormy's usual lane.

**Does it touch a regulated area, and does anyone external have to approve?**
Regulated areas (CRC/state cannabis, vendor contracts, banking, labor, local permits, delivery
zones, data privacy) plus who externally signs off. **This is the only path that engages
`reggie-compliance`.**

**Did you promise anyone money or a deadline?**
The only path that engages `chase-commitments`.

---

## Nested skill-spec questions

Same status: a library, not a script. SKILL.md Phase 4 sizes these 2-6 per skill, asking only
what the locked plan has not already answered.

1. **What does it do?** One sentence.
2. **Trigger + inputs?** What fires it (on-demand / a clock / an event in another skill) and
   what it reads (the vault, Gmail, Slack, Drive, external APIs).
3. **Output + chaining?** Where output lands, which existing skills it chains with.
4. **Gates + owner?** What runs without asking vs. what stops for him, and what runs it.
