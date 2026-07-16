import express from "express";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { z } from "zod";
import { WebClient } from "@slack/web-api";

const token = process.env.SLACK_BOT_TOKEN;
if (!token) {
  console.error("Missing SLACK_BOT_TOKEN env var — set it in your host's environment settings.");
}
const slack = new WebClient(token);

function jsonResult(value) {
  return { content: [{ type: "text", text: JSON.stringify(value) }] };
}

function buildServer() {
  const server = new McpServer({ name: "samira-slack-bot", version: "1.0.0" });

  server.tool(
    "slack_send_message",
    "Send a message to a Slack channel, optionally as a thread reply. Uses the bot's own identity, not a human user.",
    {
      channel_id: z.string().describe("Channel ID to post to"),
      message: z.string().describe("Message text (Slack markdown/mrkdwn)"),
      thread_ts: z.string().optional().describe("Parent message ts to reply in a thread"),
      reply_broadcast: z.boolean().optional().describe("Also show the threaded reply in the channel"),
    },
    async ({ channel_id, message, thread_ts, reply_broadcast }) => {
      const res = await slack.chat.postMessage({
        channel: channel_id,
        text: message,
        thread_ts,
        reply_broadcast,
      });
      return jsonResult({ ok: res.ok, ts: res.ts, channel: res.channel });
    }
  );

  server.tool(
    "slack_add_reaction",
    "Add an emoji reaction to a message, as the bot.",
    {
      channel_id: z.string(),
      timestamp: z.string().describe("ts of the message to react to"),
      emoji: z.string().describe("Emoji name without colons, e.g. white_check_mark"),
    },
    async ({ channel_id, timestamp, emoji }) => {
      const res = await slack.reactions.add({ channel: channel_id, timestamp, name: emoji });
      return jsonResult({ ok: res.ok });
    }
  );

  server.tool(
    "slack_get_reactions",
    "Get the reactions currently on a message, with who set each one.",
    { channel_id: z.string(), timestamp: z.string() },
    async ({ channel_id, timestamp }) => {
      const res = await slack.reactions.get({ channel: channel_id, timestamp, full: true });
      return jsonResult(res.message?.reactions || []);
    }
  );

  server.tool(
    "slack_read_channel",
    "Read recent messages from a channel, newest first.",
    {
      channel_id: z.string(),
      limit: z.number().optional(),
      oldest: z.string().optional(),
      latest: z.string().optional(),
    },
    async ({ channel_id, limit, oldest, latest }) => {
      const res = await slack.conversations.history({
        channel: channel_id,
        limit: limit || 100,
        oldest,
        latest,
      });
      return jsonResult(res.messages || []);
    }
  );

  server.tool(
    "slack_read_thread",
    "Read a thread: parent message plus all replies.",
    { channel_id: z.string(), message_ts: z.string(), limit: z.number().optional() },
    async ({ channel_id, message_ts, limit }) => {
      const res = await slack.conversations.replies({
        channel: channel_id,
        ts: message_ts,
        limit: limit || 100,
      });
      return jsonResult(res.messages || []);
    }
  );

  server.tool(
    "slack_list_channel_members",
    "List member user IDs of a channel.",
    { channel_id: z.string() },
    async ({ channel_id }) => {
      const res = await slack.conversations.members({ channel: channel_id });
      return jsonResult(res.members || []);
    }
  );

  server.tool(
    "slack_read_user_profile",
    "Get a Slack user's profile info.",
    { user_id: z.string() },
    async ({ user_id }) => {
      const res = await slack.users.info({ user: user_id });
      return jsonResult(res.user || {});
    }
  );

  server.tool(
    "slack_search_channels",
    "List channels the bot is a member of, optionally filtered by a name substring. Bot tokens cannot full-text search across the workspace the way a user token can — this only lists/filters known channels.",
    { query: z.string().optional() },
    async ({ query }) => {
      const res = await slack.conversations.list({ types: "public_channel,private_channel", limit: 200 });
      let channels = res.channels || [];
      if (query) {
        const q = query.toLowerCase();
        channels = channels.filter((c) => (c.name || "").toLowerCase().includes(q));
      }
      return jsonResult(channels.map((c) => ({ id: c.id, name: c.name })));
    }
  );

  server.tool(
    "slack_read_canvas",
    "Read a Slack canvas's raw file info (use the returned url_private with an authorized request to fetch full markdown).",
    { canvas_id: z.string() },
    async ({ canvas_id }) => {
      const res = await slack.files.info({ file: canvas_id });
      return jsonResult(res.file || {});
    }
  );

  server.tool(
    "slack_update_canvas",
    "Edit a Slack canvas in place: replace or insert markdown content.",
    {
      canvas_id: z.string(),
      markdown: z.string(),
      operation: z.enum(["replace", "insert_after", "insert_before"]).default("replace"),
      section_id: z.string().optional(),
    },
    async ({ canvas_id, markdown, operation, section_id }) => {
      const change = { operation, document_content: { type: "markdown", markdown } };
      if (section_id) change.section_id = section_id;
      const res = await slack.canvases.edit({ canvas_id, changes: [change] });
      return jsonResult({ ok: res.ok });
    }
  );

  return server;
}

const app = express();
app.use(express.json());

app.post("/mcp", async (req, res) => {
  try {
    const server = buildServer();
    const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
    res.on("close", () => {
      transport.close();
      server.close();
    });
    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
  } catch (err) {
    console.error("MCP request error", err);
    if (!res.headersSent) {
      res.status(500).json({
        jsonrpc: "2.0",
        error: { code: -32603, message: "Internal server error" },
        id: null,
      });
    }
  }
});

app.get("/", (_req, res) => {
  res.send("Samira Slack MCP bot server is running.");
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Samira Slack MCP server listening on port ${port}`);
});
