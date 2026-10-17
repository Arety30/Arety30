# Arety Project Index 🚀

This index separates code that is already in GitHub from projects remembered from development conversations. A project mentioned in history is not automatically a complete or publishable codebase.

## Code currently in GitHub

| Project | Repository | Visibility | Current state |
|---|---|---:|---|
| Arety RCB documentation | [Arety-rcb](https://github.com/Arety30/Arety-rcb) | Public | Architecture/documentation site |
| GPU development box | [gpu-box](https://github.com/Arety30/gpu-box) | Public | Docker/bootstrap environment; relies on runtime secrets and a separate private data repo |
| RVTCB | [rvtcb](https://github.com/Arety30/rvtcb) | Private | Existing Python/C++ source; audit before publishing |
| Kaggle MCP | [kaggle-mcp](https://github.com/Arety30/kaggle-mcp) | Private | Existing MCP service; audit config and tokens before publishing |
| Gaming VM | [gaming-vm](https://github.com/Arety30/gaming-vm) | Private | Existing VM project; audit disk assets and config before publishing |
| Knowledge Graph | [Knowledge-Graph-1](https://github.com/Arety30/Knowledge-Graph-1) | Private | Empty repository at last inspection |
| AI app | [arety-ai-app](https://github.com/Arety30/arety-ai-app) | Private | Empty repository at last inspection |
| Profile | [Arety30](https://github.com/Arety30/Arety30) | Public | Profile README and portfolio index |

## New code in this repository

- **[PDF Text Extractor](projects/pdf-text-extractor/)** — standalone HTML app for extracting/searching/downloading selectable PDF text. Fresh rebuild, not recovered byte-for-byte source.
- **[TurboWarp Gemini Chatbot](projects/turbowarp-gemini-chatbot/)** — chat UI plus server-side Gemini API proxy; the key stays in a server environment variable. Fresh rebuild.
- **[Book Detector](projects/book-detector/)** — Flask prototype combining YOLO book-object detection with EasyOCR. Fresh rebuild.

## Project ideas and prototypes from development history

These are organized for follow-up. Entries marked *history only* need their original files recovered or a clearly labelled rebuild before they can be described as source-published.

### AI, cognition and ML
- Arety RCB — architecture and documentation
- RVTCB — Python/C++ cognitive-node experiment
- RPTCB — physical-node concept; implementation status needs confirmation
- Arety Chat / Arety AI chatbot — multiple prototypes and model integrations
- Flask Gemini chatbot — history only; old model/API version needs updating
- TurboWarp Gemini chatbot — prototype code now in this repository; backend must keep API keys in environment variables
- Book Detector — Flask, YOLO/Ultralytics, OpenCV, EasyOCR; prototype code now in this repository
- AI code generator — Python/C++/JSON generation experiments
- Knowledge distillation pipeline — remembered workflow; source/status needs audit
- Knowledge Graph — repo exists but was empty at last inspection
- AI model experiments — Ollama, Qwen, Llama, Gemini and other model integrations; not one single repo

### Web apps, search and cloud
- Abrar Cloud / FamilyCloud — Flask file storage, accounts, trash and planned Drive integration
- Arety API Gateway — custom OpenAI-compatible gateway; never commit API keys or customer request logs
- Abrar Browser — Android browser prototype
- Programmable Search Engine and private search engine
- PDF Info Extractor — rebuilt implementation in this repository
- Arety RCB documentation site
- Arety Chat test instance
- Thunkable AI learning/chat app
- Discord search integration
- Custom browser search integration
- Vite + React + TypeScript app experiments

### Hardware, embedded and offline computing
- Raspberry Pi 5 AI/offline server
- Pi M.2 HAT and offline Wikipedia/search storage
- ESP32 NodeMCU-32S communication and Wi-Fi experiments
- HC-12 serial/radio experiments
- Pi–ESP32 integration and private-network research
- Raspberry Pi Camera v2 experiments
- Android/LineageOS-on-Pi research
- Samsung Tizen TV/firmware compatibility research
- Offline Kiwix, HTTrack and DocFetcher setup

### Networking, systems and infrastructure
- WireGuard mesh VPN
- Linux offline-client gateway / OTA proxy concept
- Python/C++ JSON decision engine and code generator
- USB/FTDI/serial debugging utilities
- Tailscale remote access experiments
- Apache, Gunicorn, Uvicorn and FastAPI hosting
- Google Cloud, Colab VM and OpenStack VM experiments
- GPU box and workspace synchronization
- Kaggle MCP service
- Abrar OS / Dyverz OS research and Linux desktop experiments
- Self-hosted email and domain infrastructure

### Games and other prototypes
- Roblox parkour/obby
- Minecraft server
- Gaming VM
- Local document indexing and offline tools
- Android app and browser experiments

## Publishing rules

1. Keep API keys, tokens, passwords, private customer data, and personal files out of public repositories.
2. Keep deployment secrets in environment variables or GitHub Actions secrets.
3. Do not switch a private repository to public until its source, commit history, config files, logs, and assets have been reviewed.
4. Label experiments honestly; do not claim a project is finished if only an idea or partial prototype is available.
5. Each project should eventually live in its own repository with a concise README, setup instructions, license, and tests where appropriate.

## Next publishing targets

1. Audit RVTCB and decide which source can safely be public.
2. Recover original source for Abrar Cloud, the Gemini chatbots, Book Detector, and the JSON code generator.
3. Audit Kaggle MCP and Gaming VM before changing their visibility.
4. Create dedicated repositories for the larger projects, rather than mixing unrelated apps into one codebase.
