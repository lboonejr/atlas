---
created: 2026-09-05T00:00:00-04:00
updated: 2026-09-05T00:00:00-04:00
domain: automation
type: log
status: active
tags: [samira, repo-audit, triage, open-items]
source: claude
---

# Repo audit 2026-09-05 — open items needing Lemar's call

This note collects everything the 2026-09-05 vault repo audit found that needs a human
decision. The audit's mechanical repairs (the 2026-08-01 daily-journal reconstruction,
the Regus/IWG duplicate-note merge, three deterministic filing moves, and the recovered
`created` field on the ops-admin-lane note) are in the same commit as this note; nothing
below was fixed, because each item needs Lemar's judgment.

## URGENT — fires 2026-09-11 (6 days out)

**Google Voice cancellation decision.** The Google Voice subscription on the
cuzziesnj.com domain is scheduled for cancellation **2026-09-11**. The inbox note
`00-Inbox/2026-08-12-google-voice-subscription-cancellation.md` is stuck with no
`domain` picked and — critically — **no `due` date**, so calendar-sync will never
project it and **nothing will ring before the cancellation fires**. Needs two things
from Lemar right now: pick the domain, and set a due date (something before 9/11).

## On-Button plan drift (index vs. page)

The on-button reopen page and index have drifted; needs Lemar to confirm provenance of
each figure, then run `on-button-plan` to regenerate the page/canvas from the index:

- Page shows **confirmed** amounts for 4 vendors the index still marks **tbd**:
  Curaleaf 23,774.81 · Lovegrow 18,630.67 · Chew & Chill 3,350.35 · Ganja Manja 1,266.56.
- `buds-goods` and `little-leaf-labs` are each listed **twice** on the page.
- `regus-iwg` shows 2,451.80 in the index/page vs. **2,607.61** current demand per the
  collections notes (`20-Cuzzies/2026-08-20-regus-iwg-collections-legal-threat.md`).
- `loud-labs` is tbd in one surface vs. "past due" in the other.

## 34 notes past their due date, still active / awaiting-decision

Every note below carries a `due` in the past with `status: active` or
`awaiting-decision`. Each needs one of: mark done, re-date, or park.

| Note | Due | Status |
|---|---|---|
| `20-Cuzzies/meetings/2026-07-05-eddie-happy-eddie-license-call.md` | 2026-07-06T14:30-04:00 | active |
| `20-Cuzzies/2026-07-05-jarred-jerzeygrown-business-call.md` | 2026-07-06T15:30-04:00 | active |
| `10-Personal/2026-07-05-honda-civic-financing-plan.md` | 2026-07-06T18:00-04:00 | awaiting-decision |
| `10-Personal/Family/2026-07-09-extra-space-storage-account-transfer.md` | 2026-07-09T09:30-04:00 | active |
| `10-Personal/2026-07-05-tmobile-cherry-hill-visit.md` | 2026-07-09T10:00-04:00 | active |
| `40-Projects/daily-brief/2026-07-12-samira-brief-refresh-incorporation.md` | 2026-07-12T09:00-04:00 | active |
| `30-Station/2026-07-11-station-agent-job-letter-meeting.md` | 2026-07-13T09:00:00-04:00 | active |
| `20-Cuzzies/2026-07-10-gusto-jun28-jul11-payroll-due.md` | 2026-07-13T19:00-04:00 | active |
| `20-Cuzzies/2026-07-13-greenbooks-cpa-records-meeting.md` | 2026-07-14T13:45-04:00 | active |
| `10-Personal/Family/2026-07-09-extraspace-storage-past-due.md` | 2026-07-15T09:00-04:00 | active |
| `20-Cuzzies/2026-07-15-liquidibee-good-faith-payment-missed.md` | 2026-07-15T23:59-04:00 | active |
| `20-Cuzzies/2026-07-17-friday-followups-george-greenbooks-jason.md` | 2026-07-20T15:00-04:00 | active |
| `10-Personal/Family/2026-07-05-moms-apartment-move.md` | 2026-07-20T17:00-04:00 | active |
| `20-Cuzzies/2026-07-18-cuzzies-mail-pickup-reroute.md` | 2026-07-21T09:00:00-04:00 | active |
| `10-Personal/2026-07-25-buy-court-clothes-reminder.md` | 2026-07-29T09:00-04:00 | active |
| `20-Cuzzies/2026-07-24-gusto-jul12-jul25-payroll-due.md` | 2026-07-29T19:00:00-04:00 | active |
| `20-Cuzzies/2026-07-30-gusto-final-payroll-closeout.md` | 2026-07-31T09:00:00-04:00 | active |
| `10-Personal/Health/2026-07-15-brothers-sisters-in-nature-walk.md` | 2026-08-02T09:30-04:00 | active |
| `20-Cuzzies/2026-07-28-crum-forster-workers-comp-premium-due.md` | 2026-08-04T09:00:00-04:00 | active |
| `20-Cuzzies/2026-08-01-tbt-barter-monthly-statement.md` | 2026-08-07T09:00-04:00 | active |
| `20-Cuzzies/2026-08-11-greenbooks-cpa-invoice-7500.md` | 2026-08-11T09:00:00-04:00 | active |
| `10-Personal/2026-07-17-kevonstage-comedy-show-ticket-reminder.md` | 2026-08-14T09:00-04:00 | active |
| `20-Cuzzies/2026-08-14-usps-cuzzies-change-of-address.md` | 2026-08-14T09:00:00-04:00 | active |
| `20-Cuzzies/2026-07-31-liquidibee-forbearance-ends.md` | 2026-08-15T09:00-04:00 | active |
| `20-Cuzzies/2026-08-14-mca-forbearance-plans-ahead-of-sale.md` | 2026-08-17T09:00-04:00 | active |
| `60-Legal/2026-07-21-dewalt-v-cuzzies-default-judgment.md` | 2026-08-17T10:00:00-04:00 | active |
| `20-Cuzzies/meetings/2026-08-18-jamil-east-camden-dispensary-meeting.md` | 2026-08-18T17:00-04:00 | active |
| `20-Cuzzies/2026-08-20-regus-iwg-collections-legal-threat.md` | 2026-08-23T09:00-04:00 | awaiting-decision |
| `20-Cuzzies/2026-08-21-gusto-payroll-aug9-aug22-due-aug24.md` | 2026-08-24T19:00-04:00 | awaiting-decision |
| `40-Projects/camden-dispensary-launch/2026-08-24-jamil-meeting-reschedule.md` | 2026-08-25T17:00:00-04:00 | active |
| `10-Personal/2026-07-11-claude-certification-learning-plan.md` | 2026-08-31T09:00:00-04:00 | active |
| `10-Personal/2026-07-07-trading-cards-side-hustle.md` | 2026-09-01T10:00:00-04:00 | active |
| `30-Station/2026-09-01-gusto-station-payroll-aug13-aug26-due-sep2.md` | 2026-09-02T19:00:00-04:00 | awaiting-decision |
| `20-Cuzzies/2026-09-01-gusto-cuzzies-payroll-aug23-sep5-due-sep4.md` | 2026-09-04T09:00:00-04:00 | awaiting-decision |

## 4 other Inbox notes stuck on a domain pick

Besides the Google Voice note above, these sit in `00-Inbox/` waiting on a controlled
value only Lemar can set (per schema: never guess a label):

1. `00-Inbox/2026-08-07-dib-template-theme-decision-closeout.md` — **badly malformed:
   5 of 7 frontmatter fields defective** (no `created`, no `updated`, blank `domain`,
   out-of-list `type: outcome-note`, blank `status`, out-of-list
   `source: samira-part-g`, no `tags`). Needs a full frontmatter rebuild plus the
   domain pick.
2. `00-Inbox/2026-08-24-caine-weiner-progressive-collections.md` — Caine & Weiner /
   Progressive commercial policy, $1,107.20 — domain unresolved.
3. `00-Inbox/2026-08-29-rootwurks-assignment-log-legal-sensitivity.md` — personnel
   matter with litigation-defense framing — genuinely `cuzzies` or `legal`, Lemar's
   call.
4. `00-Inbox/2026-09-02-veriscan-idscan-security-incident.md` — ID-scan vendor
   security incident — could touch Cuzzie's, Station, or both.

## Money hub stalled since 08-29

- Pockets/cash are stale — cash `as_of` 08-11.
- Daily set-aside targets unfunded since 08-25.
- Calendar not projected past 08-28.
- **6 bills + 3 Liquidibee installments + 3 car-goal installments are past their
  dates with paid/missed unknown.**
- Needs a "run my week" plus fresh balances from Lemar to re-true the ledger.

## Standing infrastructure gaps

- **Open Items canvas write-blocked since 07-25** — bot lost editor access; repair
  needed before the standing list can render again.
- **#general access gap** flagged 07-22, still unresolved.
- **"One supervised PART Q run"** still unrecorded.
- **DST cron revisit** due November 2026.
- **Basil mid-2026 wind-down** date has passed with no follow-up recorded.

## Skipped by this audit (items it was asked to fix but did not)

- **Gusto Jun28–Jul11 `calendar_event_id`** (`20-Cuzzies/2026-07-10-gusto-jun28-jul11-payroll-due.md`):
  the body's 08-16 update says the id should move to `h8312ahaekl4g7hkenrlvklfls`
  (personal reminder calendar), but the 08-23 wrong-calendar bug revert
  (`70-Automation/haven-calendar-sync/2026-08-23-calendar-sync-wrong-calendar-bug.md`,
  row 2) re-established `0gi4ohhuaqe2anbi7n4bb3fhm0` on the Cuzzie's (Owners) business
  calendar as the correct id per the locked 2026-08-10 routing policy (business notes
  never ring the personal calendar). Changing the frontmatter to the 08-16 value would
  contradict the later revert, so it was left as-is. If the note should ring at all
  anymore (payroll period long past), that is a status call, not a sync fix.
- **2026-08-01 daily journal — prior decision on record.** The corrupted journal WAS
  reconstructed by this audit (losslessly, from git history: commits 762f4009 and
  7be64f31), but note that
  `70-Automation/samira/2026-08-09-corrupted-daily-log-2026-08-01-decision.md` records
  Lemar's 8/9 call to "leave it flagged." That call predates the discovery that git
  history held the plaintext; the restore is disclosed in the file's header comment.
  Flagging here so Lemar can veto the reconstruction if he wants the 8/9 decision to
  stand literally.
