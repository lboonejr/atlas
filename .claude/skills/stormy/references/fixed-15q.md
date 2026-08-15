# Fallback question library (the retired fixed 15)

**This is not a script.** Stormy's instrument is adaptive (SKILL.md Phase 2): she writes
questions for the specific idea and sizes the count to its blast radius. This file is the
old fixed 15-question form, kept as a **library of stock wordings** to raid when a dimension
is genuinely generic and the stock phrasing is the clearest way to ask it.

Retired as a mandatory instrument 2026-08-15. The failure it caused: on
`money-hub-rebalance-steward` — a personal-ledger software change with one owner — four of
the fifteen came back "Lemar only," "none," "no," and "N/A." Four questions, zero
information, and none of them asked the thing that actually mattered (how aggressive the
rework logic should default to).

**Rules for using this file**

- Never run it top to bottom.
- Never ask a stock question when a specific version of it exists for the idea at hand.
- Never ask a stock question whose answer is already obvious — record it as an assumption instead.
- Reaching for more than about half of these on one idea is a signal you have not read the
  idea closely enough to find its crux.

---

## Dimension 1 — Problem & beneficiary

**Core problem or opportunity this solves?**
Operational efficiency / Revenue growth / Risk mitigation / Learning or experiment / Cost
reduction / Customer experience / Team capability / Other

**Primary beneficiary?**
Cuzzie's / The Station / Both / External partner / Internal team / Customers / All stakeholders

## Dimension 2 — Scope & hardest constraint

**What's IN scope, and what's the hardest constraint?**
Two-part short text — scope description plus the single biggest limiter (budget, timeline,
staffing, vendor, regulatory, tech).

## Dimension 3 — Success & failure

**Primary success metric?**
Revenue/profit impact / Operational metric (speed, accuracy, capacity) / Compliance/safety /
Customer feedback / Team adoption / Learning outcome / Market position / Other

**Minimum viable success — the smallest win that counts?**
Short text.

**Early warning signs of failure — what would make you pivot or pull the plug?**
Short text.

## Dimension 4 — Dependencies & risk

**Most likely blocker?**
Funding/cash / Compliance/legal / Vendor or partner dependency / Staffing / Tech/tools /
Customer adoption / Market conditions / Unknown/TBD / Other

**Who needs to sign off or be heavily involved?**
Multi-select from the Role Config Block (SKILL.md) — CEO / Station ops lead / Inventory lead /
Admin lead / Legal counsel / Compliance officer / Vendor / External partner.

*Note: the old form forbade a "None" option here on the theory that every project has an
approver. That is what produced the empty "Lemar only" answers. A single-owner personal
project has exactly one approver and does not need the question — assume it.*

## Dimension 5 — Timing & preconditions

**When do you want to activate?**
ASAP (within 1 week) / Soon (2-4 weeks) / Next month / Quarterly / When [precondition] is
true / TBD — fully bake first

**Preconditions — what needs to be true before activation?**
Short text. (Funding cleared? Vendor signed? Hire made? Other gate?)

## Dimension 6 — Compliance

**Does this touch regulated areas, and are any third-party approvals needed?**
Two-part. Multi-select for regulated areas (CRC/state cannabis / Vendor contracts /
Banking/financial / Labor law / Local permits/licensing / Delivery zones / Data privacy /
None) plus short-text for who externally needs to sign off (CRC, city, bank, vendor, etc.).

Gates `reggie-compliance`: flagged means Reggie joins at handoff, never proactively.

## Dimension 7 — Automation & data flow

**What workflows need to repeat automatically?**
Daily monitoring/scanning / Weekly reporting/roll-ups / Real-time alerts / Periodic data
sync / Compliance checks / Status updates / Decision gates / None

**Where does the data and status flow?**
Short text. Default assumption is Haven for truth and a Slack channel for the surface —
challenge anything that proposes a new source of truth.

## Dimension 8 — Delegation

**Can this be delegated, and if so to whom?**
Fully — [role] owns end-to-end / Partially — [role] owns Phase X, you own Phase Y / No — you
must lead / Unsure. Roles pull from the Role Config Block.

**If delegated, what decisions come back to you and at what cadence?**
Two-part. Multi-select for what comes back (Budget/spend approvals / Customer comms /
Decision to pivot/abort / Strategy changes / None — full autonomy) plus cadence (Daily
standup / Weekly summary / Bi-weekly / Only if issues / Never).

---

## Nested skill-spec questions (the retired fixed 4)

Same status: a library, not a script. SKILL.md Phase 4 sizes these 2-6 per skill.

1. **What does it do?** One sentence.
2. **Run frequency + data monitored?** How often (real-time / daily / weekly / on-demand) and
   what it reads (the vault, Gmail, Slack, Drive, external APIs).
3. **Output destination + integration?** Where output goes, which existing skills it chains
   with (task-builder, email-responder, chase-commitments, etc.).
4. **Decision gates + owner?** What runs autonomously vs. needs approval, and who owns it.
