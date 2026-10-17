# Syed Abrar Ali · Arety

Student developer from Qatar building **Arety** — a self-hosted platform of services and tools under [arety.cloud](https://tests.arety.cloud), plus my own Linux distribution. Everything here is designed, written and operated by me, running on free compute tiers and hardware I own.

## Portfolio map

- **[Full project inventory](PROJECTS.md)** — organized by AI, web apps, hardware, networking, infrastructure, and games, with source/publication status.
- **[PDF Text Extractor](projects/pdf-text-extractor/)** — a small, browser-only PDF text extraction tool.
- **[TurboWarp Gemini Chatbot](projects/turbowarp-gemini-chatbot/)** — Gemini chat demo with a server-side API proxy.
- **[Book Detector](projects/book-detector/)** — Flask + YOLO + OCR computer-vision prototype.
- **[Arety RCB docs](https://github.com/Arety30/Arety-rcb)** · **[GPU Box](https://github.com/Arety30/gpu-box)**

The inventory distinguishes code already in GitHub from remembered prototypes that still need source recovery or a security review.

## Arety

| Project | What it is |
|---|---|
| **RVTCB — Real Virtual Technical Cognition Brain** (Arety 0.1 / RCB) | A full-mesh cognitive brain: every node is its own processor written in C++ (tokenizer, grammar, knowledge store, reasoning) with a Python cognition layer on top. The reasoning is entirely my own code — no vendor model does the thinking. Spec: [Arety-rcb](https://github.com/Arety30/Arety-rcb). Source is closed. |
| **Knowledge distillation pipeline** | Pulls knowledge out of large teacher models as *data*, organised into a node → sub-node → topic taxonomy and cross-checked across teachers, then loaded into the brain's nodes. |
| **Arety Chat** — [tests.arety.cloud](https://tests.arety.cloud) | Public chat interface over the RVTCB brain (RCB 1.0 and 1.2), hosted on free notebook compute. Earlier versions fused several hosted models behind one model name (`arety/omni`) with voice and camera input. |
| **Arety Voice API** | Speech recognition → language model → speech synthesis behind my own API keys. |
| **Phone line** | A real phone number answered by my own call server (speech recognition, a 12B language model I fine-tuned, speech synthesis), with SMS handling, softphone auto-provisioning and a CardDAV contacts directory. |
| **Arety Messenger** | WhatsApp-style web chat app + Android APK wrapper for a WhatsApp business sender. |
| **ai-finetuning.arety.cloud** | Fine-tuning request form and downloads site, hosted on a Raspberry Pi 5 and published through a Cloudflare Worker + Tailscale Funnel. |
| **mcp.arety.cloud** | My own MCP gateway: one domain exposing MCP servers I wrote (mail, Kaggle, GitHub, Hugging Face, Cloudflare, spending manager, shared profile, LinkedIn publishing). |

## Operating system

**Abrar OS / Dyverz OS** — an Arch-based distribution with its own ISO builder (also runs on Colab), a "looks" engine that restyles the desktop as Windows, macOS, Ubuntu, Fedora or Mint, a WinKernel layer with a `C:` partition and `.exe` installer, and a first-boot setup wizard.

## Apps & tooling

- **Abrar AI Hub** — offline desktop app and CLI (agent, study tools, notes, knowledge graph, meetings, plugins); the CLI is also served as a browser terminal.
- **laptop-agent** — Discord bot orchestrating seven local Ollama agents that run shell commands and edit files; Dockerized, with Apache gateway and n8n email automation, failing over between my laptop and a cloud VM.
- **MiniBank** — local card-issuing gateway (FastAPI + SQLite) with wallets, own-issued cards and NFC UIDs.
- **Self-hosted email** — Postfix + Dovecot servers, a TLS SMTP submission relay on the Pi, and dnsmasq as my own resolver with a private DNS zone.
- **[gpu-box](https://github.com/Arety30/gpu-box)** — Docker Compose + bootstrap for throwaway NVIDIA GPU boxes (CUDA 12.8, Tailscale SSH inside the container, 2-minute data sync).
- **colab-gaming-vm** — a QEMU virtual machine that boots inside Colab from repo-hosted disk images.
- **ESP32 Wi-Fi sniffer** — NodeMCU-32S frame capture with my own Python 802.11 header decoder.
- **Raspberry Pi 5 home server** — llama.cpp inference server (Ollama-compatible API) hosting my personal model, plus audio, Bluetooth and VNC tooling.

## More projects

- **AbrarCloud / Arety Cloud** — modular FastAPI personal-cloud backend: image parser, audio generator and parser, database editor, user-file storage.
- **Project Sovereign** — fully offline agentic system for 1–3B-parameter models: chain-of-thought loops, self-reflection, structured planning; FastAPI backend + frontend, 20-phase blueprint.
- **Arety Office** — offline browser office suite (Quill, x-spreadsheet) reading and writing real files via pandoc, LibreOffice and openpyxl.
- **Gemma 4 Studio** — offline web UI for a 4B multimodal model with native vision + audio through a llama.cpp server, plus Piper speech synthesis.
- **Defender Bot & security assessments** — dependency-free authorization-boundary defense engine (HTTP event correlation, proportionate responses, incident records) and multi-round security findings reports.
- **Discord bot family** — AbrarAssistant, ai_assistant, shell_executor, SystemControlBot, a reusable scaffold, and Discord Browser VM: a per-server Chromium browser running as an embedded Discord Activity.
- **chatgpt-compvm** — disposable Ubuntu desktop in Docker (Firefox, terminal, noVNC) remote-controlled through an MCP server over Tailscale.
- **apt-store** — desktop app-store client in Next.js + Electron. **Meeting and Study Room Hub** — Electron desktop app.
- **Full-Screen Chat** — Firefox extension with its own FastAPI backend.
- **abrar-twin** — my personal fine-tuned model (dataset + Colab notebook), served from the Raspberry Pi 5 through my llama.cpp server; custom Ollama Modelfiles.
- **projectonebeta** — early speech-to-text, audio generation and Asterisk ARI telephony prototypes, the roots of the Arety voice stack. **Arety Phone Space** — Gradio Space packaging the phone call server.
- **Images & packaging** — custom Ubuntu 26.04 arm64 ISO remastered with Cubic; Debian packaging (.deb).
- **Pi networking** — pi-mesh WireGuard/tailnet gateway and pi-desktop one-click remote desktop.
- **Smaller tools** — Video Stream Portal, routing-table service, chemistry quiz web app + CLI quiz runner, DuckDNS updater, RAM-gated mail relay, Cloudflare Worker gateway, a 3D-printed pod case design, and earlier HC-12 radio / Raspberry Pi serial-communication experiments.

## Stack

C++ · Python (FastAPI, Flask, CustomTkinter, MCP SDK, Gradio, Streamlit) · TypeScript (Next.js, Electron) · Firefox extensions · Linux (systemd, Apache, Postfix/Dovecot, dnsmasq, archiso, Wine) · Docker · Tailscale · Cloudflare Tunnels & Workers · Android · ESP32 · Asterisk/SIP · WireGuard · fine-tuning and distillation on free GPU tiers

## Milestones

- **2026-09-05** — registered arety.cloud and started publishing services under my own domain
- **2026-09-12** — first Arety Chat live at tests.arety.cloud
- **2026-10-08** — RVTCB native mode: the whole brain runs on my own C++ node processors
- **2026-10-09** — mcp.arety.cloud gateway launched
- **2026-10-11** — Arety Chat moved to free notebook hosting, independent of my laptop
