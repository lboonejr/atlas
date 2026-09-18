# The Workstation — Given Word Notary

Source for the notary business dashboard, published as an Artifact at
https://claude.ai/artifact/5q3G772uieaQFrubGhfqek

`index.html` is the whole page. It is published with the `db` and `user` capabilities, so the
data lives in the artifact's own shared store rather than in this file — editing and
republishing the page never touches the data.

The decision record, and the rule about which surface is the source of truth, is in the vault:
`haven/vault/40-Projects/notary-services/2026-09-18-notary-workstation-dashboard.md`.

## Collections

| Path | Holds | Written by |
|---|---|---|
| `jobs/<id>` | one job: channel, date, fees, pages, payer, terms, paid date, journal entry id | the page's Jobs tab, or `notary-intake` |
| `tasks/<id>` | an open item — a task Lemar owes, or a question out with DORES / BlueNotary / the county clerk | the page's Open items tab |
| `launch/<id>` | one runway step: phase, title, detail, cost label, `deadline`/`queue`/`gate` tag, done | seeded from the Given Word Runway tracker |
| `channels/<id>` | one way work can reach the business: key, name, status, what is blocking it, spend | the page's Marketing tab |
| `activity/<YYYY-MM-DD>` | one document per day holding that day's log entries (capped at 60) | the page, and anything reporting a completed job |
| `meta/config` | `phase` (`prelaunch` or `operating`), entity name | set once |

A job's `source` must match a channel's `key` for the marketing scoreboard to count it.

## Republishing

Edit `index.html`, then publish it with the `url` above. Do not pass `capabilities` unless you
mean to change them — omitting it carries the stored declaration forward.

## Rules baked into the page

- Money is computed from completed jobs only. Printing is estimated at `pages × 2 × $0.055`
  until a receipt figure is entered, and estimates are labelled as estimates.
- The set-aside is 20% on the statutory notarial fee and 35% on everything else. It is a
  reserve policy, not a tax calculation.
- Invoices are chased on the job's own channel terms, never a global one week.
- No signer PII beyond a first name and a town. The legal journal is a separate system.
