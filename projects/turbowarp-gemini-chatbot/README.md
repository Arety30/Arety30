# TurboWarp Gemini Chatbot ✨

A small chat UI with a serverless API proxy so the Gemini API key stays on the server instead of in browser JavaScript.

## Deploy

1. Import this repository into Vercel.
2. Set the project root directory to `projects/turbowarp-gemini-chatbot`.
3. Add `GEMINI_API_KEY` in Vercel → Project Settings → Environment Variables. Never paste the key into this repository.
4. Optionally set `GEMINI_MODEL` (defaults to `gemini-2.5-flash`) and `ALLOWED_ORIGIN`.
5. Deploy, then open `chatbot.html` through the deployed site. The API route is `/api/chat`.

## Use with TurboWarp

The same `POST /api/chat` endpoint accepts JSON:

```json
{ "message": "Hello!", "history": [] }
```

It returns `{ "reply": "...", "model": "..." }`. A TurboWarp extension can call this endpoint using its HTTP/fetch capability. Do not put a Gemini key in a Scratch/TurboWarp project.

## Important deployment notes

- This is a prototype, not a production-hardened public API.
- The endpoint has input-size and history limits but no built-in durable rate limiting or user authentication. Add platform-level rate limits and access controls before sharing it widely; an open endpoint can be abused and incur API charges.
- CORS is configurable with `ALLOWED_ORIGIN`; use the exact origin you need instead of `*` where practical.
- Only send conversation text you are comfortable sending to the configured model provider.

## Status

Fresh rebuild of the remembered TurboWarp/Gemini chatbot idea; it is not claimed to be the original files recovered byte-for-byte.
