# Board Configuration Reference

This file maps Monday.com boards Lemar references in conversation to their concrete IDs, group structure, column inventory, and accepted values. Keep it in sync — when a new board is encountered (see "Unknown Boards" at bottom), add it here so future runs don't have to re-discover.

---

## Canonical Strings (use exactly)

- **Cuzzie's** / Cuzzies / Camden → always use `"Cuzzie's Dispensary & Delivery"` (with apostrophe and ampersand) for the Dispensary dropdown value.
- The other location is `"The Station"` (capital T).

---

## Board Name Resolution Table

Match Lemar's phrasing (case-insensitive, fuzzy) against this table to pick a target board.

| Lemar says…                                              | Resolves to     | Board ID       |
|----------------------------------------------------------|-----------------|----------------|
| "admin", "admin board", "for admin", "tell my admin"     | Admin Board     | `18324306759`  |
| "operations", "ops", "ops board", "add to ops"           | Operations      | `18396190103`  |
| "Ken", "Ken's", "Ken's board", "design board"            | Ken's Board     | `18390239321`  |
| "my list", "my to-do", "to-do", "remind me", "I need to" | Lemar's To-Do   | `18390239511`  |
| "shortlist", "shortlist board"                           | Shortlist       | unknown — resolve via `search` / `get_board_info` |
| Any other board by name                                  | Unknown         | resolve, then `get_board_info` |

---

## Pre-Mapped Boards

### Admin Board

**Purpose:** Day-to-day admin execution work — research, filing, scheduling, calls, document creation, supplies, financial admin, menu updates.

**Board ID:** `18324306759`

**Default Status:** `Planned`

**Groups:**

| Group name           | Group ID            | When to use                                                              |
|----------------------|---------------------|--------------------------------------------------------------------------|
| Current Projects     | `group_title`       | Active in-progress admin work                                            |
| Future Projects      | `group_mky9jzcv`    | Backlog / not-yet-started planned work                                   |
| Planned              | `group_mkxsdqmm`    | Scheduled but not yet active                                             |
| Supplies/Equipment   | `group_mkx9ak1c`    | Anything to order, replace, or restock (paper, ink, cleaning, hardware)  |
| Menus                | `group_mm127kr1`    | Menu updates, additions, removals (use Operations for audits)            |
| To Pay               | `group_mm136m3`     | Bills, payroll, vendor payments, reimbursements                          |
| Archive              | `group_mkx9e17j`    | Completed work — never write here from the skill                         |

**Default group:** `group_mkxsdqmm` (Planned) for most new tasks. Override based on content:
- Supplies/equipment → `group_mkx9ak1c`
- Financial → `group_mm136m3`
- Menu work → `group_mm127kr1`

**Columns:**

| Column label  | Column ID              | Type      | Accepted values / notes                                                  |
|---------------|------------------------|-----------|--------------------------------------------------------------------------|
| Status        | `status`               | status    | `Planned` (default), `Working on it`, `Stuck`, `Done`                    |
| Due Date      | `date4`                | date      | ISO `YYYY-MM-DD`                                                         |
| Dispensary    | `dropdown_mkx99cy8`    | dropdown  | `Cuzzie's Dispensary & Delivery`, `The Station`, `Office`, `Both`        |
| Priority      | `color_mkx91yfh`       | status    | `Low`, `Medium`, `High`, `Critical`                                      |
| Recurring?    | `color_mkywezgs`       | status    | Set when task repeats                                                    |
| Task Type     | `dropdown_mkzjy76e`    | dropdown  | `Research`, `Scheduling`, `Filing`, `Document Creation`, `Call`, `Supplies`, `Payroll`, `Account Management`, `Menu` |

**Subitem columns (Admin):**

| Subitem label | Column ID              | Type       |
|---------------|------------------------|------------|
| Status        | `status`               | status     |
| Date          | `date0`                | date       |
| Dispensary    | `dropdown_mky4140v`    | dropdown   |
| Priority      | `color_mky4f5ft`       | status     |
| Notes         | `long_text_mky4sy63`   | long text  |
| Link          | `text_mky4p1gr`        | text       |
| Login Info    | `text_mky4hh7y`        | text       |

---

### Operations Board

**Purpose:** Store-floor and operational work — inventory tasks, menu audits, menus, budtender tasks, deliveries, price changes, on-site operations across Cuzzie's and The Station.

**Board ID:** `18396190103`

**Default Status:** `Working on it` (board has **no "Planned" status**)

**Groups:**

| Group name              | Group ID            | When to use                                  |
|-------------------------|---------------------|----------------------------------------------|
| Weekly Tasks            | `group_mm0jtrdx`    | Recurring weekly work                        |
| Cataloging              | `group_mm1wb2tk`    | Product cataloging                           |
| Miscellaneous           | `group_mkzrh5sj`    | One-off operations work                      |
| Budtender Tasks         | `group_mkzrkwb5`    | Budtender-specific assignments               |
| Inventory Tasks         | `topics`            | Inventory counts, transfers, reconciliations |
| Menu Audits             | `group_title`       | Menu audits specifically                     |
| Delivery Tasks          | `group_mkzsk83v`    | Delivery ops                                 |
| Price Changes           | `group_mkzrsnx8`    | Price update work                            |
| Menus                   | `group_mm26wm5c`    | Menu additions, edits, removals              |
| Overdue                 | `group_mkzvgnbe`    | Past-due items — usually a triage bucket; don't post new tasks here unless instructed |
| Inventory Archive       | `group_mkzrzfpq`    | Completed — skill never writes               |
| Menu Audit Archive      | `group_mkzrew11`    | Completed — skill never writes               |
| Price Changes Archive   | `group_mm034zq8`    | Completed — skill never writes               |
| Miscellaneous Archive   | `group_mm0ef85m`    | Completed — skill never writes               |
| Weekly Task Archive     | `group_mm0mc633`    | Completed — skill never writes               |

**Default group:** `group_mkzrh5sj` (Miscellaneous) when nothing more specific fits. Routing rules:
- Inventory → `topics`
- Menu work → `group_mm26wm5c`
- Menu audits specifically → `group_title`
- Delivery → `group_mkzsk83v`
- Price changes → `group_mkzrsnx8`
- Budtender-facing → `group_mkzrkwb5`
- Recurring weekly → `group_mm0jtrdx`
- Cataloging → `group_mm1wb2tk`

**Columns:**

| Column label             | Column ID              | Type      | Accepted values / notes                                                  |
|--------------------------|------------------------|-----------|--------------------------------------------------------------------------|
| Person                   | `person`               | people    | Assignee                                                                 |
| Dispensary Name          | `dropdown_mkzrcy5z`    | dropdown  | `Cuzzie's Dispensary & Delivery`, `The Station`, `Both`                  |
| Status                   | `status`               | status    | **No "Planned"** — default `Working on it`. Others: `Stuck`, `Done`      |
| Priority                 | `color_mkzre1zw`       | status    | `Low`, `Medium`, `High`, `Critical`                                      |
| Files                    | `file_mkzrksn3`        | file      | Skip unless explicit upload                                              |
| Date                     | `date4`                | date      | ISO `YYYY-MM-DD`                                                         |
| Link                     | `text_mkzrw5vx`        | text      | URL — only set when one is provided                                      |
| Bot Action               | `color_mm1ww44f`       | status    | Automation flag — skip unless instructed                                 |
| Price Change Due Date    | `date_mkzr3841`        | date      | Only for Price Changes group                                             |

**Subitem columns (Operations):**

| Subitem label | Column ID  | Type     |
|---------------|------------|----------|
| Owner         | `person`   | people   |
| Status        | `status`   | status   |
| Date          | `date0`    | date     |

---

### Ken's Board

**Purpose:** Graphic design queue — deal graphics, social posts, kiosk graphics (Weedmaps/Leafly/Dutchie), postcards, flyers, signage, merch, branding.

**Board ID:** `18390239321`

**Default Status:** `Planned`

**Groups:**

| Group name        | Group ID           | When to use                                                  |
|-------------------|--------------------|--------------------------------------------------------------|
| Current Projects  | `group_title`      | **All new tasks land here.**                                 |
| Archive           | `group_mkx9e17j`   | Completed — skill never writes                               |

**Columns:**

| Column label   | Column ID                  | Type           | Accepted values / notes                                       |
|----------------|----------------------------|----------------|---------------------------------------------------------------|
| Status         | `status`                   | status         | `Planned` (default), `Working on it`, `Stuck`, `Done`         |
| Due Date       | `date4`                    | date           | ISO `YYYY-MM-DD`                                              |
| Dispensary     | `dropdown_mkx99cy8`        | dropdown       | `Cuzzie's Dispensary & Delivery`, `The Station`, `Both`       |
| Media Type     | `dropdown_mkz8bzna`        | dropdown       | `Deal Graphic`, `Social`, `Kiosk`, `Postcard`, `Flyer`, `Signage`, `Merch`, `Branding` (verify exact labels via `get_column_type_info`) |
| Priority       | `color_mkx91yfh`           | status         | `Low`, `Medium`, `High`, `Critical`                           |
| Assigned To    | `multiple_person_mkx9xzya` | multi-people   | Ken by default                                                |

---

### Lemar's To-Do

**Purpose:** Lemar's personal queue — strategic / ownership-level work he'll drive himself, things to remember, decisions to make.

**Board ID:** `18390239511`

**Default Status:** `Planned`

**Groups:**

| Group name        | Group ID           | When to use                                  |
|-------------------|--------------------|----------------------------------------------|
| Current Projects  | `group_title`      | Active strategic work Lemar's driving        |
| Planned           | `group_mkxsdqmm`   | **Default for new tasks** — scheduled / soon |
| Archive           | `group_mkx9e17j`   | Completed — skill never writes               |

**Default group:** `group_mkxsdqmm` (Planned) unless Lemar says he's actively working on it now.

**Columns:**

| Column label   | Column ID                  | Type           | Accepted values / notes                                       |
|----------------|----------------------------|----------------|---------------------------------------------------------------|
| Status         | `status`                   | status         | `Planned` (default), `Working on it`, `Stuck`, `Done`         |
| Due Date       | `date4`                    | date           | ISO `YYYY-MM-DD`                                              |
| Dispensary     | `dropdown_mkx99cy8`        | dropdown       | `Cuzzie's Dispensary & Delivery`, `The Station`, `Office`, `Both` |
| Priority       | `color_mkx91yfh`           | status         | `Low`, `Medium`, `High`, `Critical`                           |
| Assigned To    | `multiple_person_mkx9xzya` | multi-people   | Lemar by default                                              |

---

## Setting Column Values — JSON Format

Monday's `create_item` accepts `columnValues` as a JSON object keyed by column ID. The expected value shape depends on the column type:

```json
{
  "status":               { "label": "Working on it" },
  "color_mkx91yfh":       { "label": "High" },
  "date4":                { "date": "2026-05-25" },
  "dropdown_mkx99cy8":    { "labels": ["Cuzzie's Dispensary & Delivery"] },
  "multiple_person_mkx9xzya": { "personsAndTeams": [{ "id": 12345678, "kind": "person" }] },
  "person":               { "personsAndTeams": [{ "id": 12345678, "kind": "person" }] },
  "text_mkzrw5vx":        "https://example.com",
  "long_text_mky4sy63":   { "text": "longer body of text" }
}
```

Notes:

- **Status / dropdown columns:** prefer `label` (the human-readable value) rather than `index`. Monday will resolve it. For multi-select dropdowns (like Dispensary), use `labels` as an array.
- **Date:** ISO `YYYY-MM-DD`. Add `"time": "HH:MM:SS"` when needed.
- **People / multi-people:** the `id` is the Monday user ID. Keep the table below current.
- Only include columns that exist on the target board. Unknown columns will error.
- If a status/dropdown value gets rejected, call `get_column_type_info` on that column to see the exact labels Monday accepts.

**Known user IDs:**

| Name           | Monday user ID  |
|----------------|-----------------|
| Lemar          | `<TODO>`        |
| Admin          | `<TODO>`        |
| Ken            | `<TODO>`        |

> **TODO:** Fill in user IDs as you learn them. Until then, leave People/Assigned To unset and let board defaults apply, or set via `list_users_and_teams` lookup at runtime.

---

## Handling Unknown Boards (the `get_board_info` pattern)

When Lemar names a board that isn't in this file:

1. Resolve the board ID. If he gave one, use it. Otherwise call `search` / `list_workspaces` (Monday MCP) to find it. If you still can't resolve it, **ask Lemar** — don't guess.
2. Call `get_board_info` with the board ID. This returns groups, columns, and column types.
3. Map what you can — Status, Priority, Due Date, Dispensary, Task Type are the common ones. Skip anything you can't confidently map.
4. Create the item with the mapped columns; post the full task detail as a `create_update` regardless.
5. At the end of the run, tell Lemar: *"I posted to [board name] — want me to add its columns to `board-config.md` so future posts use the right defaults?"* If yes, append a new section to this file with the discovered structure.

---

## Maintenance Checklist

When you discover something new about a board (a column, a group, a status value, a user ID), update this file in the same session. The skill leans on this reference for every post — stale entries cause silent miscategorization.
