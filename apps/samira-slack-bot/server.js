import express from "express";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { buildServer } from "./lib/buildServer.js";
import { requireAuth } from "./lib/auth.js";

if (!process.env.SLACK_BOT_TOKEN) {
  throw new Error("Missing SLACK_BOT_TOKEN environment variable — set it in the host's environment settings.");
}

const app = express();
app.use(express.json());

app.post("/mcp", async (req, res) => {
  if (!requireAuth(req, res)) {
    return;
  }
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

// Health check stays open — no auth token needed to see the server is alive.
app.get(["/", "/health"], (_req, res) => {
  res.send("Samira Slack MCP bot server is running.");
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Samira Slack MCP server listening on port ${port}`);
});
