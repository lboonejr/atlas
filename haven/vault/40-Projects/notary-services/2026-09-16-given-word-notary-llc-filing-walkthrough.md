---
created: 2026-09-16T22:00-04:00
updated: 2026-09-17T14:10:00-04:00
domain: project
type: reference
status: active
tags: [notary, llc, entity, filing, walkthrough]
source: claude
---

# Filing `Given Word Notary LLC` — the walkthrough

Everything needed to stand the entity up, in order, with the decisions that have to be made
before starting. **Roughly 30–45 minutes of actual typing** for steps 1 through 3.

**Do it yourself on the state's own site.** Formation services charge $200–300 to type the same
form into the same portal. There is nothing in this that needs a middleman.

---

## BEFORE YOU START — four things to have decided and to hand

**1. The name, exactly as it will be typed:** `Given Word Notary LLC`
NJ requires a designator, and "LLC" is one. The portal runs its own availability check during the
filing, so this is also where the name is finally confirmed — the state search on 2026-09-16 was
clear, but the filing is what settles it.

**2. The registered agent, and this one has a real decision in it.**
Every NJ LLC needs a registered agent with a **New Jersey street address** — a real address where
legal papers can be handed to someone during business hours. **A PO box does not qualify.**

Lemar can be his own registered agent. It is free and it is what most single-owner businesses do.

**The catch: the registered agent's address becomes public record.** Anyone can look it up. For a
business run from home, that means a home address on a searchable state database, attached to a
notary who will also be publishing a Google Business Profile.

| Option | Cost | Trade-off |
|---|---|---|
| Be your own agent | free | Home address is public and searchable |
| Registered agent service | ~$50–150/yr | Their address is public instead; they forward the mail |

**This is worth two minutes of thought, not a reflex.** It is annoying to change later, and the
same privacy logic already applied to using a Google Voice number instead of the cell.

**3. The business address.** Can be the same as the registered agent address.

**4. A card or bank account for the fees.** Total out of pocket today: **$100**.

---

## STEP 1 — Certificate of Formation ($100, ~15 minutes)

**Where:** the state's Business Formation portal, `njportal.com` → Business Formation.
**Do not use a third-party site that looks like it.**

**Fee: $100.** New Jersey lowered this from $125 on **1 July 2026**, so older notes and guides
still say $125. If the portal shows something different, the portal is right.

What it asks for:

| Field | Answer |
|---|---|
| Business type | **Domestic Limited Liability Company** — "domestic" means formed in NJ, nothing to do with home |
| Business name | `Given Word Notary LLC` |
| Registered agent name + NJ street address | per the decision above |
| Main business address | can match the agent address |
| Purpose / NAICS code | notary / legal support services — the portal offers a picker, and it is not binding on what the business can do |
| Duration | perpetual, unless there is a reason otherwise |
| Effective date | today, unless there is a reason to delay |
| Member / manager | Lemar |

**What comes out: the Certificate of Formation, and an Entity ID number.** Save both. The
certificate is one of the documents the vendor packet needs, and the Entity ID is required for
step 3.

---

## STEP 2 — EIN from the IRS (free, ~10 minutes, same day)

**Where:** `irs.gov`, "Apply for an EIN Online." **It is free and it is instant.**

**Never pay for an EIN.** There are sites that charge $50–300 for this exact free form, and they
rank well in search. The only real one is irs.gov.

**This is the step that matters most for the notary business.** The EIN is what goes on the W-9
instead of Lemar's Social Security number — and that W-9 goes to **every signing service he ever
registers with**. Without it, his SSN is sitting in a dozen vendor systems he does not control.

Requires the LLC to exist first, so it follows step 1 the same afternoon.

---

## STEP 3 — NJ-REG, the tax registration (free, ~15 minutes, within 60 days)

**This is a separate filing from the formation, and it is the one people miss.** Forming the LLC
creates the entity; NJ-REG registers it with the Division of Taxation. **Required within 60 days
of formation**, and before doing business.

Needs the **Entity ID** from step 1 and the **EIN** from step 2, which is why it goes third.

**What it produces: the Business Registration Certificate (BRC).** Keep it — it is the document
other businesses ask for when they want proof the entity is registered. Another one for the
vendor packet.

**Do it the same day if there is time.** Sixty days is a deadline, not a plan, and this is the
kind of thing that gets remembered on day 61.

---

## STEP 4 — Operating agreement (free, not filed with anyone)

NJ does not require one and does not want a copy. **Write one anyway**, because the bank will
likely ask for it when opening the business account, and because a single-member LLC with no
operating agreement is easier to argue against if the entity is ever challenged.

For a single-member notary LLC it is short: who owns it (Lemar, 100%), who manages it (Lemar),
what happens to it if he stops. A template is fine. Keep it in the vendor packet folder.

---

## STEP 5 — The business bank account

The dedicated SoFi checking account was already in the plan. **It becomes the LLC's account**, and
opening it needs: the **Certificate of Formation**, the **EIN letter**, the **operating
agreement**, and photo ID.

**Keep notary money out of the personal account from the very first dollar.** Mixing personal and
business money in an LLC's account is the classic way the entity stops being treated as separate —
and separation is most of what the LLC is being bought for. The Set-Aside pocket stays distinct
from this account too, exactly as `notary-journal-mirror` already assumes.

---

## STEP 6 — Calendar the annual report

**$75 a year, due in the anniversary month of formation.** File it late and the state eventually
revokes the LLC.

**Put it in Haven with a `due` the moment the certificate comes back**, so calendar-sync rings it
every year. This is precisely the kind of quiet recurring deadline the vault exists to catch, and
it is the same pattern already used for the commission renewal.

---

## The order, and why it is this order

1. **Formation** → gives the Entity ID
2. **EIN** → needs the LLC to exist
3. **NJ-REG** → needs both of the above
4. Operating agreement → any time, but the bank wants it
5. Bank account → needs 1, 2 and 4
6. Annual report reminder → the moment 1 lands

**None of this depends on the exam, the commission, or the seal.** That is the whole point of
doing it today: it runs in parallel with DORES processing the commissioning application, for free.

## What it unblocks

**No LLC → no EIN → no W-9 → no signing service registration.** The entity is the first domino on
the entire B2B side of this business, and Snapdocs cannot be started without it.

It also unblocks the **Google Business Profile**, which needs the registered name and then sits in
the longest queue in the plan.

## Running total

| Item | Cost |
|---|---|
| Certificate of Formation | $100 |
| EIN | free |
| NJ-REG | free |
| Operating agreement | free |
| **Today** | **$100** |
| Annual report | $75/yr, starting next year |

**The $57 Camden County trade name filing is not on this list on purpose** — a county clerk
registers trade names for individuals and partnerships, not LLCs. Still confirm that with the
clerk before treating it as cancelled.

## Sources
- claude: Claude Code session, 2026-09-16 — NJ LLC formation steps, the 1 July 2026 fee change
  from $125 to $100, registered agent requirements, NJ-REG's 60-day window, and the annual report.
- Prior: [[2026-09-16-notary-llc-printer-platforms]], [[2026-09-20-notary-exam-day-checkpoint]].
- Not legal or tax advice. How the LLC is taxed, and whether an S-corp election ever makes sense,
  are CPA questions — not urgent at this revenue, but worth one call in the first year.
