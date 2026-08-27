# Productivity Loop System — the question bank

The dial-in questions the design session works through, grouped into the eight themes the
v2 prompt sequences (A–H). Each question carries why it matters. Forks are offered where
a recommendation exists; the bank is a floor, not a ceiling — the session should add its
own wherever an answer opens a new seam.

---

## A. Arianna — the second human

The whole current system assumes one owner. This theme decides what changes.

1. **Name and identity.** The brainstorm spells her both "Ariana" and "Arianna" — which
   is correct? (It becomes her Slack handle, Haven entity note, folder names, and every
   template; get it right once.)
2. **Employment shape.** Is Arianna an employee, a contractor, or informal help for now?
   How many hours a week is realistic? (Sizes how much the loop can route to her per day
   and whether payroll/1099 belongs in workstream 2.)
3. **Accounts.** Does she get: her own Marspace Slack account? Her own Claude
   account/plan (which tier — Claude in Chrome needs a paid plan)? A business email on
   the new domain? A Google account inside a business Workspace or her personal one?
4. **Her DM with Samira.** The bot can hold one DM per user, so Arianna's own
   Samira DM is available. Confirm: her daily to-do list, context, files, and
   Chrome-run prompts all land there (as the brainstorm says), and that DM gets its own
   anchors row and its own PART-B-style sweep watermark?
5. **Reactions.** Today the reaction engine reads only Lemar's signals. Does Arianna get
   her own signal set in her DM (✅ done · ⏳ blocked · 👀 seen), read by Samira on each
   scan? And in shared channels, whose ✅ is authoritative — Lemar-only everywhere except
   her DM?
6. **Trust boundaries.** Which surfaces can Arianna see and which stay Lemar-only?
   Specifically: the 02 Internal folders (fee thinking, client assessments)?
   #investor-pipeline? Anything money-related (#personal-finance, #on-button)? The Haven
   vault itself, or only Drive renderings? Recommendation: default-deny, grant per
   surface, record the grants in anchors.
7. **Her computer.** The "fresh computer": who buys it, what's on it (Claude Desktop +
   Claude Code + Chrome + Drive for Desktop?), and does it get a clone of the atlas repo
   with push rights to `main`, or does she work only in Drive/Slack with no repo access?
   (Repo access = she can break the live runbook; no repo access = her file-hygiene job
   is Drive-only.)
8. **Absence.** When Arianna is out, do her queued tasks fall back to Lemar, wait, or
   age to a #decisions card? After how long?
9. **Client contact.** Is Arianna client-facing from day one (emails signed by her,
   calls made by her) or internal-only until some milestone? Does she send as herself,
   or as a shared business identity (e.g. admin@)?
10. **Voice.** Client-facing sends from Arianna: her own professional voice, or drafted
    by the loop in Lemar's voice profile and sent under the company's name? (The voice
    profile currently only defines Lemar's voice.)

## B. The send-gate — what "execution" actually means now

Samira's floor is never-send/never-pay/never-post-publicly. The business needs sends,
payments, and public posts. The clean resolution: the AI stages, a human sends.

11. **The gate itself.** Confirm the rule: nothing outward (email, DM to a client,
    social post, ad spend, filing) ever moves without Lemar's ✅ on a #decisions card,
    and the *sending* is always a human (usually Arianna). Any exceptions ever (e.g.
    routine appointment confirmations)?
12. **Two-step or one-step.** Brainstorm flow is: Samira → Lemar review → thumbs-up →
    admin finalizes and sends. Does every send need both humans (Lemar approves,
    Arianna sends), or can Lemar's ✅ alone trigger *his own* send for things only he
    can send?
13. **Email sending.** Approved drafts sit in Gmail Drafts today. Does Arianna get
    delegated access to the business mailbox to press send, her own mailbox, or does
    Lemar keep all sending? (Delegation changes the Gmail account design in A3.)
14. **Calls.** For "make the call" tasks: calendar event + attached call script is the
    staged artifact (existing pattern). Confirm the confirmation loop: Arianna reacts ✅
    in her DM after the call and drops a 2-line outcome that Samira captures to Haven?
15. **Payments.** Ads, domain, hosting, filing fees: who holds the card, and what's the
    approval threshold above which it's a #decisions card vs. just-do-it? (Recommend:
    every recurring commitment is a card; one-off under $X is Arianna's discretion.)
16. **Claude in Chrome.** The browser lane currently assumes *Lemar* present and never
    submitting. With Arianna running Chrome tasks: does the never-submit/never-pay rule
    hold for her sessions too (she stops at the last screen and clicks as herself only
    after Lemar's ✅), and which logins is she allowed to hold (business socials yes,
    CRC portal ?, Lemar's Gmail ?)?
17. **Social posting.** Who presses post on IG/Facebook — Arianna always? Is there a
    standing weekly content approval (one card approving a batch) instead of per-post
    cards?

## C. Accountability vs. the no-nudge law

The brainstorm's core is follow-up ("Samira checks that things are done… confirmation
that emails were sent, calls made, meetings had"). Current doctrine says never re-post,
never nudge.

18. **Nudge budget.** What's the bounded follow-up rule? Recommendation: each open
    commitment gets ONE confirmation ask per day, in its home surface (Lemar's items
    ride the existing Pulse/#decisions surfaces; Arianna's get one daily digest in her
    DM), and a commitment unconfirmed for 2 days escalates to one #decisions line. Yes/no?
19. **Lemar's own accountability.** Does Lemar want Samira confirming *his* actions too
    ("did the 2pm call happen?"), and where — a line in the Pulse respond-list, or a DM
    ask? How hard should she push before it becomes noise he ignores?
20. **Commitment registry.** Where does "who owes what by when" live? Recommendation:
    Haven notes with `due` (already ring via calendar-sync) plus a per-person section on
    the Open Items canvas / Pulse. Or does this warrant a dedicated tracker note per
    person? (Note: the chase-commitments skill exists for external promises — reuse its
    pattern internally, or keep external/internal separate?)
21. **Meeting confirmations.** After a calendar event passes, should Samira
    automatically ask "did it happen, what came of it?" for every business event, or
    only events the loop created?
22. **The 3-way surface.** Does the shared status view live in (a) each project's
    channel as a pinned/refreshed summary, (b) a new 3-way group DM (needs a new
    surface + sweep + anchors row and cuts against one-place routing), or (c) the Pulse
    doc extended with a per-person lane? Pick one.

## D. Making the business legitimate

23. **Entity.** LLC (single-member? Lemar + partners?) — and in which state, given NJ
    operations and VA ambitions? Who is the registered agent? (Not legal advice; the
    loop stages the research and paperwork, a professional or Lemar files.)
24. **Name.** What's the business name? Does "I can get you licensed" become the brand
    line? (Blocks EIN, domain, socials, templates — this is the first decision.)
25. **Ownership + disclosure.** Any partners or revenue-share (Arianna? former
    vendors?)? NJ CRC scrutinizes financial interests around licensees — the Camden
    overlay deliberately holds no equity in clients. Does the consultancy adopt that as
    a standing rule?
26. **Vendor kickbacks.** The vendor-discount/referral idea: structured as disclosed
    referral fees, marketing partnerships, or margin on resold services? Who checks
    what NJ/VA cannabis rules say about consultants taking vendor compensation tied to
    a licensee's purchasing? (Flag: this one can poison the "legitimate business" goal
    if it's undisclosed — needs a real compliance read, not a guess.)
27. **Banking + books.** Which bank (cannabis-adjacent friction is real), and does
    bookkeeping ride QuickBooks from day one? Who reconciles — Arianna monthly?
28. **Insurance.** Professional liability / E&O for a licensing consultant: get quotes
    now or after client #2?
29. **The offer.** Is the Camden fee ($30k across five milestones, then $2k/mo) the
    standard offer, or Camden-specific pricing? What does the VA offer cost?
30. **Contracts.** Who turns the Camden proposal into a reusable engagement-letter
    template, and which attorney reviews it once?

## E. Templating the client playbook

31. **The template source.** Confirm: the Camden structure (00 Command Center / 01
    Client-Facing with six phase folders / 02 Internal, naming convention, Working Log,
    six gates, milestone billing) IS the template — each new client is a copy with
    state-specific content swapped?
32. **Where templates live.** A "Client Playbook — NJ" master folder in Drive plus a
    Haven reference note per state? Who may edit masters (Lemar-only)?
33. **Spin-up procedure.** A "new client" checklist the loop can run: create Drive tree,
    Working Log from template, private Slack channel, Haven index note, anchors row,
    overlay file from the template. Should this become a skill (it recurs by design), and
    does PART H's 3-occurrence rule get waived to build it now?
34. **Two-engagement split.** Confirm the Camden doctrine generalizes: licensing
    engagement ends at inspection clearance; ops services (delivery stand-up, virtual
    GM, vendor plug-ins) is always a separately-priced engagement. What's the standard
    hand-off moment to pitch it?
35. **Document hygiene.** The "scheduled tasks that keep everything organized and delete
    duplicates": cloud tools can't delete Drive files, so is this a weekly local job on
    Arianna's machine (Claude Code with Drive for Desktop), and what are its rules
    (supersede-prefix instead of delete? report-only for anything destructive)?
36. **Records retention.** Client files after an engagement ends: archived where, kept
    how long, and who may access them?

## F. The reviewer routine

37. **Scope.** What does "healthy" mean, concretely? Candidate checks: all three
    routines fired on schedule; no stale lock; watermarks advancing; no #decisions card
    silent >N days; no Haven note stuck in Inbox >N days; both humans' overdue
    confirmations; Drive folders matching the template; digest anomalies. Which of
    these make the v1 list?
38. **Placement.** A new PART in Dawn's 1am run (she already reads everything daily), a
    fourth standalone persona, or an extension of the reports-contradiction-scanner?
    Recommendation: Dawn hosts it — no new trigger, and the finding lands in the
    morning brief Lemar already reads.
39. **Governance.** Confirm the reviewer *proposes* runbook/anchors changes as
    #decisions cards and never self-applies (the brainstorm's "throws it into Samira so
    she can make the changes herself" would mean an unattended routine editing the live
    runbook on `main` — recommend against). Is there any class of change small enough
    to self-apply (e.g. correcting a dead channel ID)?
40. **Failure alerting.** If Samira's runs stop entirely, nothing inside the system can
    say so. Does the reviewer (on a different trigger) own "Samira hasn't completed a
    run in X hours → one line to Lemar's DM"?

## G. The customer-facing build

41. **Website.** Scope of v1: a one-page credibility site (who we are, the one-liner,
    Camden proof, contact form) or a funnel with intake? Built and hosted where —
    Vercel is already in the stack; who owns the build (a staged local/cloud build
    through the samira-loop)?
42. **Domain + mail.** Domain name (follows D24), and Google Workspace on it from day
    one so nothing new touches cuzziesnj.com?
43. **Lead intake.** Where do inquiries land? Recommendation: a form → business mailbox
    → the email loop triages → a #decisions card per qualified lead, and a
    "prospect" section in a new pipeline index note (mirroring the investor-pipeline
    pattern). Agree?
44. **Instagram/Facebook.** Cannabis-adjacent accounts get restricted or banned
    routinely, and ad policy for cannabis *services* is narrow even where the service
    is legal. Who owns researching platform policy before spending (staged research
    task), and is the ads goal lead-gen for the consultancy (services, not product)?
45. **Content engine.** Who produces posts — the loop drafts weekly batches in Lemar's
    voice, Arianna schedules them after one batch-approval card? What cadence?
46. **Physical media.** What does "physical advertising media" mean concretely for v1 —
    business cards, a one-pager/leave-behind for municipal meetings, event banners?
    Printed via whom, designed via the existing design tooling?
47. **Proof.** What can be publicly claimed about Camden/The Station/the current client
    (names, numbers, outcomes) without breaching client confidentiality or promising
    results? (The overlay's never-promise-outcomes rule should govern marketing copy
    too.)

## H. Virginia, and what comes after

48. **Timing.** Is VA research a now-workstream (standing weekly research task) or
    parked until Camden hits a milestone (which one — application filed? license
    issued?)?
49. **The research product.** What does "understand VA" produce — a state playbook note
    in Haven (rules, timeline, fees, local-approval mechanics, key dates) mirroring an
    NJ playbook written from what Lemar already knows? Who maintains it as VA
    rulemaking moves?
50. **Network.** The "necessary network" per state (attorneys, architects, security
    vendors, realtors): tracked as Haven entity notes with a per-state index? Does
    building the VA list start now via staged outreach drafts?
51. **Qualification.** What makes a group "qualified" (capital floor, site status,
    background eligibility)? Turn it into a written intake scorecard so the one-liner
    ("I can get you licensed") carries a straight-faced screen behind it?
52. **Success metrics.** For the whole system, what are the 90-day numbers Lemar wants
    on Pulse: Camden phase gate hit, entity formed, site live, N qualified leads, N
    hours/week of Lemar's time saved? Pick the 3–5 that define "this worked."

---

## Sequencing note

Theme D24 (the name) and A1 (Arianna's spelling) block the most downstream work; B (the
send-gate) and C18 (the nudge rule) are the two doctrine changes that touch the live
runbook and should be decided before any runbook diff is drafted. Everything in G can
wait until D is done without stalling Camden.
