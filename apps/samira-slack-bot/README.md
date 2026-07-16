# samira-slack-bot

A small program that lets Samira (the Atlas Executor) act in Slack through her own bot
account instead of Lemar's personal account. It needs somewhere to run 24/7 — this repo
folder is the code; below is how to get it running for free on Vercel.

This lives at `apps/samira-slack-bot/` inside the `lboonejr/atlas` repo (a subfolder,
not its own repo — see the note at the bottom).

This was **not run/tested locally** (no Node.js available in the environment that wrote
it), so there may be a hiccup on first deploy. If a step below shows an error, copy
exactly what it says and send it to Claude rather than trying to interpret it yourself —
this gets fixed directly in the code, no local setup needed on your end.

## Deploy for free on Vercel

1. Go to [vercel.com](https://vercel.com) and sign up using your GitHub login (this
   avoids creating a separate password).
2. Click **Add New** → **Project**.
3. Pick the `lboonejr/atlas` repository from the list.
4. Before clicking deploy, there's a **Root Directory** setting — click "Edit" next to
   it and type: `apps/samira-slack-bot`
   (This tells Vercel the code lives in a subfolder, not at the top of the repo.)
5. Leave the Build/Output settings on their defaults — nothing to change there.
6. Open **Environment Variables** and add one:
   - Name: `SLACK_BOT_TOKEN`
   - Value: the **Bot User OAuth Token** from your Slack app (starts with `xoxb-`),
     found on the app's **OAuth & Permissions** page.
   This stays inside Vercel's settings only — never paste it into chat.
7. Click **Deploy**. This takes under a minute.
8. When it's done, Vercel shows you a web address, something like
   `https://samira-slack-bot.vercel.app`. That's the app's home.
9. To check it's alive, visit `https://samira-slack-bot.vercel.app/health` in a browser
   — it should say "Samira Slack MCP bot server is running."

Nothing here costs money — Vercel's free plan comfortably covers a low-traffic bot like
this, and unlike some free hosts it doesn't "fall asleep" between uses in a way that
would make Samira's hourly check-ins fail.

## Register it as a custom connector in claude.ai

1. claude.ai → **Settings → Connectors → Add custom connector**.
2. Name it something like "Slack (Samira bot)".
3. URL: your Vercel address with `/mcp` on the end, e.g.
   `https://samira-slack-bot.vercel.app/mcp`
4. No extra login needed here — the server already holds the Slack bot token itself.
5. Save, and confirm claude.ai can connect to it (it should list several `slack_*`
   actions).

## Slack app requirements (should already be done)

- Bot Token Scopes: `chat:write`, `reactions:write`, `reactions:read`, `channels:read`,
  `channels:history`, `groups:read`, `groups:history`, `im:history`, `users:read`.
  (Add `canvases:write` / `canvases:read` too if you want the canvas-editing actions to
  work — add these if those specific actions error out.)
- The bot must be invited into every channel it needs to read or post in — in Slack,
  type `/invite @Samira` inside each of: `#decisions`, `#reports`, `#atlas`, `#admin`,
  `#car-search`, `#investor-pipeline`, and any active project channels.

## Once this is live

Tell Claude it's connected. Claude will then point Samira's hourly routine at this new
bot connector instead of your personal Slack account — this only affects Samira; the
Daily Brief and Inbox Janitor routines are untouched.

## Other hosting options

If you'd rather use a traditional always-on host instead of Vercel (Render, Railway,
Fly.io), this folder also has a `server.js` you can run instead — same logic, just
listens on a port the way those hosts expect (`npm start`, with `PORT` and
`SLACK_BOT_TOKEN` set in the host's environment settings). Most of those charge a small
monthly fee for a plan that doesn't sleep between uses, which is the tradeoff against
Vercel's free tier.

## Why this is a subfolder, not its own repo

The GitHub access this was built with can read and write the `atlas` repo but can't
create new repositories, so the code lives at `apps/samira-slack-bot/` inside `atlas`
rather than standing alone.
