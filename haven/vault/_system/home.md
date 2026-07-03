---
created: 2026-07-03T00:00-04:00
updated: 2026-07-03T00:00-04:00
domain: reference
type: reference
status: active
tags: [haven, home, moc]
source: manual
---

# Haven — Home

Welcome to Haven, the source of truth. If Atlas and Semira are people who do
jobs, Haven is the country they live and work in. Everything flows through here.

## Start here
- [[schema]] — the rulebook: folders, frontmatter, filing rules
- The Inbox (`00-Inbox`) is where everything lands before it is filed.

## Domains
- [[20-Cuzzies]] — Cuzzie's operations
- [[30-Station]] — The Station operations
- `10-Personal` — life, finances, housing, vehicles, writing
- `40-Projects` — cross-cutting or multi-phase work
- `50-Reference/Entities` — canonical businesses, vendors, people, accounts, legal

## How the brain fills
1. A capture is written to `00-Inbox` as a Markdown note with frontmatter.
2. `vault-keeper` (a Semira executor, dispatched by Atlas on the hourly loop)
   reads the Inbox and files each valid note by its `domain`/`type`/`status`.
3. Notes that are missing frontmatter stay in the Inbox and get flagged.
4. The maps of content and Open Items stay refreshed so navigation is current.
