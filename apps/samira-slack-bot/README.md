# samira-slack-bot

A minimal remote MCP server that lets Samira (the Atlas Executor) act in Slack through
her own bot identity instead of Lemar's personal account. It wraps the Slack Web API
using a bot token (`xoxb-...`) and exposes the same read/write actions Samira's runbook
already uses: send message, add reaction, read channel/thread, list channel members,
read user profile, list channels, read/edit a canvas.

This lives at `apps/samira-slack-bot/` inside the `lboonejr/atlas` repo (not a separate
repo — the GitHub token this session had access to could read/write `atlas` but could
not create new repositories, so it's a subfolder of the existing one instead).

This was **not run/tested locally** (no Node.js available in the environment that wrote
it) — it follows the standard Model Context Protocol TypeScript SDK pattern for a
stateless Streamable HTTP server. Expect to do one debug round after first deploy if
something doesn't boot cleanly; send Claude the Render deploy/runtime logs and it'll fix
it directly in this repo.

## Deploy to Render (recommended — simplest path)

1. Go to [render.com](https://render.com) and sign up / log in (GitHub login is easiest).
2. Click **New +** → **Web Service**.
3. Connect the `lboonejr/atlas` GitHub repo.
4. Set **Root Directory** to `apps/samira-slack-bot` (important — this folder, not the
   repo root).
5. Runtime: **Node**. Build command: `npm install`. Start command: `npm start`.
6. Under **Environment Variables**, add `SLACK_BOT_TOKEN` and paste in the **Bot User
   OAuth Token** (starts `xoxb-`) from your Slack app's **OAuth & Permissions** page.
   This value stays inside Render's environment settings — it is never committed to the
   repo and never passes through chat.
7. Choose the **Starter** plan (~$7/mo) rather than Free — the free tier spins the
   service down after 15 minutes of inactivity, which risks a timed-out or failed call
   on Samira's hourly runs. Starter stays warm.
8. Click **Deploy**. Wait for the build to go green.
9. Once live, copy the service's public URL (something like
   `https://samira-slack-bot.onrender.com`). The MCP endpoint is that URL + `/mcp`,
   e.g. `https://samira-slack-bot.onrender.com/mcp`.
10. Sanity check it's alive: visiting the base URL in a browser should show
    "Samira Slack MCP bot server is running."

## Register it as a custom connector in claude.ai

1. claude.ai → **Settings → Connectors → Add custom connector**.
2. Name it something like "Slack (Samira bot)".
3. URL: the `/mcp` endpoint from step 7 above.
4. No additional auth needed at the claude.ai layer — the server holds the Slack bot
   token itself, server-side.
5. Save, and confirm claude.ai can connect (it should list the `slack_*` tools above).

## Slack app requirements (should already be done)

- Bot Token Scopes: `chat:write`, `reactions:write`, `reactions:read`, `channels:read`,
  `channels:history`, `groups:read`, `groups:history`, `im:history`, `users:read`.
  (`canvases:write`/`canvases:read` if you want canvas editing to work — add these if
  the canvas tools error out.)
- The bot must be invited (`/invite @Samira`) into every channel it needs to read or
  post in: `#decisions`, `#reports`, `#atlas`, `#admin`, `#car-search`,
  `#investor-pipeline`, and any active project channels.

## Once this is live

Tell Claude the new connector's name (or its `connector_uuid`, visible in claude.ai's
connector settings). Claude will swap Samira's trigger (`trig_01VGzAWGSadjRbJbKURxCYvG`)
to use this connector instead of the personal Slack one, via the RemoteTrigger API —
scoped only to Samira; Dawn and Basil are untouched.
