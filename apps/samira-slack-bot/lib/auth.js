import { timingSafeEqual } from "node:crypto";

// Bearer-token gate for the MCP endpoint. Returns true when the request is
// authorized; otherwise writes the error response and returns false.
// Fails closed: if MCP_AUTH_TOKEN isn't configured, nothing gets through.
export function requireAuth(req, res) {
  const expected = process.env.MCP_AUTH_TOKEN;
  if (!expected) {
    res.status(503).json({
      error: "MCP_AUTH_TOKEN not configured. Set it in the host's environment settings — the endpoint refuses all requests until it is.",
    });
    return false;
  }
  const header = req.headers["authorization"] || "";
  // The token can arrive as a Bearer header or, for clients whose connector
  // config has no auth-header field (e.g. claude.ai custom connectors), as a
  // `key` query parameter on the endpoint URL.
  const queryKey = new URL(req.url || "/", "http://localhost").searchParams.get("key") || "";
  const provided = header.startsWith("Bearer ") ? header.slice("Bearer ".length) : queryKey;
  const expectedBuf = Buffer.from(expected);
  const providedBuf = Buffer.from(provided);
  if (providedBuf.length !== expectedBuf.length || !timingSafeEqual(providedBuf, expectedBuf)) {
    res.status(401).json({ error: "Unauthorized. Send 'Authorization: Bearer <MCP_AUTH_TOKEN>' or append '?key=<MCP_AUTH_TOKEN>' to the endpoint URL." });
    return false;
  }
  return true;
}
