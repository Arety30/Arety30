const MODEL = process.env.GEMINI_MODEL || "gemini-2.5-flash";
const MAX_MESSAGE_CHARS = 4000;
const MAX_HISTORY_ITEMS = 12;

export default async function handler(req, res) {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("Access-Control-Allow-Origin", process.env.ALLOWED_ORIGIN || "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return res.status(405).json({ error: "Use POST." });

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) return res.status(503).json({ error: "Server is missing GEMINI_API_KEY." });

  const body = req.body && typeof req.body === "object" ? req.body : {};
  const message = typeof body.message === "string" ? body.message.trim() : "";
  if (!message) return res.status(400).json({ error: "A message is required." });
  if (message.length > MAX_MESSAGE_CHARS) {
    return res.status(413).json({ error: `Message must be ${MAX_MESSAGE_CHARS} characters or fewer.` });
  }

  const history = Array.isArray(body.history) ? body.history.slice(-MAX_HISTORY_ITEMS) : [];
  const contents = [];
  for (const item of history) {
    if (!item || !["user", "model"].includes(item.role) || typeof item.text !== "string") continue;
    const text = item.text.trim().slice(0, MAX_MESSAGE_CHARS);
    if (text) contents.push({ role: item.role, parts: [{ text }] });
  }
  contents.push({ role: "user", parts: [{ text: message }] });

  try {
    const upstream = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(MODEL)}:generateContent?key=${encodeURIComponent(apiKey)}`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          contents,
          generationConfig: { maxOutputTokens: 1200, temperature: 0.7 }
        }),
        signal: AbortSignal.timeout(30000)
      }
    );
    const data = await upstream.json().catch(() => ({}));
    if (!upstream.ok) {
      // Do not return upstream request URLs or credentials to the browser.
      return res.status(502).json({ error: "The model provider returned an error.", status: upstream.status });
    }
    const reply = data?.candidates?.[0]?.content?.parts
      ?.map(part => typeof part.text === "string" ? part.text : "")
      .join("")
      .trim();
    if (!reply) return res.status(502).json({ error: "The model returned no text. Try again." });
    return res.status(200).json({ reply, model: MODEL });
  } catch {
    return res.status(504).json({ error: "The model request timed out or could not connect." });
  }
}
