# AI Agent Builder 🤖⚡

Build AI agents with drag-and-drop. No coding required. Create powerful autonomous agents in minutes.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](Dockerfile)

## Why AI Agents?

AI agents are the next big thing! Projects like `oh-my-claudecode` (17k stars) and `hermes-agent` (17k stars) are trending. This tool makes building them accessible to everyone.

## ✨ Features

- 🎯 **Visual Builder** - Drag and drop nodes to create workflows
- 🧠 **LLM Integration** - Connect to GPT-4, Claude, Gemini, Local models
- 💾 **Memory** - Persistent conversation history
- 📚 **Knowledge Base** - Upload PDFs, docs for RAG
- 🔌 **Tools** - Built-in tools + custom plugins
- 🔄 **Multi-agent** - Orchestrate multiple agents together
- 🌐 **Web UI** - Gradio interface for easy agent building
- 🐳 **Docker Ready** - Deploy anywhere

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Run CLI
python agent_builder.py

# Or use Web UI
python gradio_app.py
# Open http://localhost:7863
```

## 🐳 Docker

```bash
docker build -t ai-agent-builder .
docker run -p 7863:7863 -e OPENAI_API_KEY=your-key ai-agent-builder
```

## 📝 License

MIT License

## ⭐ Support

Star the repo if this helps!