# Board Configuration Reference

This file maps Monday.com boards Lemar references in conversation to their concrete IDs, group structure, column inventory, and accepted values. Keep it in sync — when a new board is encountered (see "Unknown Boards" at bottom), add it here so future runs don't have to re-discover.

---

## Board Name Resolution Table

Match Lemar's phrasing (case-insensitive, fuzzy) against this table to pick a target board.

| Lemar says…                                             | Resolves to     | Board ID          |
|---------------------------------------------------------|-----------------|-------------------|
| "admin", "admin board", "for admin", "tell my admin"    | Admin Board     | `<TODO_ADMIN_ID>` |
| "operations", "ops", "ops board", "add to ops"          | Operations      | `<TODO_OPS_ID>`   |
| "Ken", "Ken's", "Ken's board", "design board"           | Ken's Board     | `<TODO_KENS_ID>`  |
| "my list", "my to-do", "to-do", "remind me", "I need to"| Lemar's To-Do   | `<TODO_TODO_ID>`  |
| "shortlist", "shortlist board"                          | Shortlist       | `<TODO_SHORTLIST_ID>` — verify via `get_board_info` |
| Any other board by name                                 | Unknown         | Look up the ID via `list_workspaces` / search, then `get_board_info` |

> **TODO:** Fill in the board IDs above. Until then, the skill should call `list_workspaces` + search Monday at runtime to resolve the IDs, then update this table.

---

## Pre-Mapped Boards

### Admin Board

**Purpose:** Day-to-day admin execution work — research, filing, scheduling, calls, document creation, supplies, financial admin, menu updates.

**Board ID:** `<TODO_ADMIN_ID>`

**Groups:**

| Group name             | Group ID              | When to use                                                              |
|------------------------|-----------------------|--------------------------------------------------------------------------|
| Supplies/Equipment     | `<TODO_GROUP_ID>`     | Anything to order, replace, or restock (paper, ink, cleaning, hardware)  |
| To Pay                 | `<TODO_GROUP_ID>`     | Bills, payroll, vendor payments, reimbursements                          |
| Menus                  | `<TODO_GROUP_ID>`     | Menu updates, additions, removals (use Operations for audits)            |
| `<TODO group name>`    | `<TODO_GROUP_ID>`     | `<TODO description>`                                                     |

> **TODO:** Enumerate all Admin board groups and their IDs.

**Columns:**

| Column label    | Column ID           | Type     | Accepted values / notes                                            |
|-----------------|---------------------|----------|--------------------------------------------------------------------|
| Status          | `<TODO_COL_ID>`     | status   | `Planned`, `Working on it`, `Stuck`, `Done`, …                     |
| Priority        | `<TODO_COL_ID>`     | status   | `Low`, `Medium`, `High`, `Critical`                                |
| Due Date        | `<TODO_COL_ID>`     | date     | ISO format `YYYY-MM-DD`                                            |
| Dispensary      | `<TODO_COL_ID>`     | status / dropdown | `Cuzzie's`, `The Station`, `Office`, `Both`             |
| Task Type       | `<TODO_COL_ID>`     | status / dropdown | `Research`, `Scheduling`, `Filing`, `Document Creation`, `Call`, `Supplies`, `Payroll`, `Account Management`, `Menu`, … |
| Assignee        | `<TODO_COL_ID>`     | people   | Default: admin                                                     |
| Recurring       | `<TODO_COL_ID>`     | checkbox / status | Set if task repeats                                       |

> **TODO:** Pull the full column inventory (and the exact label/index pairs the API accepts) for the Admin board.

---

### Operations Board

**Purpose:** Store-floor and operational work — inventory tasks, menu audits, menus, on-site operations across Cuzzie's and The Station.

**Board ID:** `<TODO_OPS_ID>`

**Groups:**

| Group name        | Group ID         | When to use                                  |
|-------------------|------------------|----------------------------------------------|
| Menus             | `group_mm26wm5c` | Menu work (additions, edits, removals)       |
| Menu Audits       | `group_title`    | Menu audits specifically                     |
| Inventory Tasks   | `topics`         | Inventory counts, transfers, reconciliations |
| `<TODO>`          | `<TODO>`         | `<TODO>`                                     |

> **TODO:** Confirm the remaining Operations groups and their IDs. `group_title` and `topics` are common default group IDs in Monday — double-check they map to the intended groups for this board.

**Columns:**

| Column label    | Column ID           | Type     | Accepted values / notes                                            |
|-----------------|---------------------|----------|--------------------------------------------------------------------|
| Status          | `<TODO_COL_ID>`     | status   | **No "Planned" status.** Default: `Working on it`. Others: `Stuck`, `Done`. |
| Priority        | `<TODO_COL_ID>`     | status   | `Low`, `Medium`, `High`, `Critical`                                |
| Due Date        | `<TODO_COL_ID>`     | date     | ISO format `YYYY-MM-DD`                                            |
| Dispensary      | `<TODO_COL_ID>`     | status / dropdown | `Cuzzie's`, `The Station`, `Both`                         |
| Task Type       | `<TODO_COL_ID>`     | status / dropdown | `Inventory`, `Menu`, `Menu Audit`, …                      |
| Assignee        | `<TODO_COL_ID>`     | people   |                                                                    |

> **TODO:** Full column inventory.

---

### Ken's Board

**Purpose:** Graphic design queue — deal graphics, social posts, kiosk graphics (Weedmaps/Leafly/Dutchie), postcards, flyers, signage, merch, branding.

**Board ID:** `<TODO_KENS_ID>`

**Groups:**

| Group name        | Group ID        | When to use                                                  |
|-------------------|-----------------|--------------------------------------------------------------|
| Current Projects  | `group_title`   | **All new tasks land here.**                                 |
| Archive           | `<TODO>`        | Lemar / Ken move completed work here; the skill never writes |

**Columns:**

| Column label    | Column ID           | Type     | Accepted values / notes                                            |
|-----------------|---------------------|----------|--------------------------------------------------------------------|
| Status          | `<TODO_COL_ID>`     | status   |                                                                    |
| Priority        | `<TODO_COL_ID>`     | status   |                                                                    |
| Due Date        | `<TODO_COL_ID>`     | date     |                                                                    |
| Dispensary      | `<TODO_COL_ID>`     | status   | When the design is location-specific                               |
| Design Type     | `<TODO_COL_ID>`     | status / dropdown | `Deal Graphic`, `Social`, `Kiosk`, `Postcard`, `Flyer`, `Signage`, `Merch`, `Branding` |
| Dimensions      | `<TODO_COL_ID>`     | text     | Free-text; common values: `1080x1080`, `1080x1920`, etc.           |

> **TODO:** Full column inventory.

---

### Lemar's To-Do

**Purpose:** Lemar's personal queue — strategic / ownership-level work he'll drive himself, things to remember, decisions to make.

**Board ID:** `<TODO_TODO_ID>`

**Groups:**

| Group name        | Group ID        | When to use                          |
|-------------------|-----------------|--------------------------------------|
| `<TODO>`          | `<TODO>`        | `<TODO>`                             |

**Columns:**

| Column label    | Column ID           | Type     | Accepted values / notes              |
|-----------------|---------------------|----------|--------------------------------------|
| Status          | `<TODO_COL_ID>`     | status   |                                      |
| Priority        | `<TODO_COL_ID>`     | status   |                                      |
| Due Date        | `<TODO_COL_ID>`     | date     |                                      |

> **TODO:** Full group + column inventory.

---

## Setting Column Values — JSON Format

Monday's `create_item` accepts `columnValues` as a JSON object keyed by column ID. The expected value shape depends on the column type:

```json
{
  "status_column_id":   { "label": "Working on it" },
  "priority_column_id": { "label": "High" },
  "date_column_id":     { "date": "2026-05-25" },
  "dropdown_column_id": { "labels": ["Cuzzie's"] },
  "people_column_id":   { "personsAndTeams": [{ "id": 12345678, "kind": "person" }] },
  "text_column_id":     "free-form text",
  "checkbox_column_id": { "checked": "true" },
  "long_text_column_id":{ "text": "longer body of text" }
}
```

Notes:

- For `status` / dropdown columns: prefer `label` (the human-readable value) rather than `index`. Monday will resolve it.
- For `date`: ISO `YYYY-MM-DD`. Add `"time": "HH:MM:SS"` when needed.
- For `people`: the `id` is the Monday user ID — keep a small mapping of common assignees here as you learn them.
- Only include columns that exist on the target board. Unknown columns will error.
- When in doubt, call `get_column_type_info` for the board + column ID to verify the expected value shape.

**Known user IDs:**

| Name           | Monday user ID  |
|----------------|-----------------|
| Lemar          | `<TODO>`        |
| Admin          | `<TODO>`        |
| Ken            | `<TODO>`        |

> **TODO:** Fill in user IDs as you learn them.

---

## Handling Unknown Boards (the `get_board_info` pattern)

When Lemar names a board that isn't in this file:

1. Resolve the board ID. If he gave one, use it. Otherwise call `list_workspaces` or `search` (Monday MCP) to find it. If you still can't resolve it, **ask Lemar** — don't guess.
2. Call `get_board_info` with the board ID. This returns groups, columns, and column types.
3. Map what you can — Status, Priority, Due Date, Dispensary, Task Type are the common ones. Skip anything you can't confidently map.
4. Create the item with the mapped columns; post the full task detail as a `create_update` regardless.
5. At the end of the run, tell Lemar: *"I posted to [board name] — want me to add its columns to `board-config.md` so future posts use the right defaults?"* If yes, append a new section to this file with the discovered structure.

---

## Maintenance Checklist

When you discover something new about a board (a column, a group, a status value, a user ID), update this file in the same session. The skill leans on this reference for every post — stale entries cause silent miscategorization.
