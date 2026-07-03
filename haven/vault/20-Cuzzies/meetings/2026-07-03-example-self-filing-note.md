---
created: 2026-07-03T09:15-04:00
updated: 2026-07-03T13:39:52-04:00
domain: cuzzies
type: meeting
status: active
tags: [example, onboarding]
source: manual
---

# Example: a note that files itself

This note is a live demonstration of the filing rules. It has complete, valid
frontmatter, so the next time `vault-keeper` sweeps the Inbox it will:

1. Read `domain: cuzzies` → destination is `20-Cuzzies/`.
2. Read `type: meeting` → subfolder is `meetings/`.
3. Move this file to `20-Cuzzies/meetings/` and touch `updated`.

If you delete the `domain` line and drop it back in `00-Inbox`, vault-keeper will
instead **leave it here** and flag it, because it can no longer be filed
deterministically. That gap is the enforcement mechanism — delete this example
note once you have seen it move, it is only here to prove the loop works.
