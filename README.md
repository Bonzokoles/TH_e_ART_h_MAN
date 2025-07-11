# 🧙 TH_e_ART_h_MAN

## AI-Powered Stable Diffusion Copilot - Work in Progress

⚠️ **This is not a complete application** - This repository contains the core components and working code for an AI-powered Stable Diffusion assistant. The application is currently in active development.

### What's Working:
- Ollama Bridge for local AI model integration  
- Wildcard Generator for prompt enhancement
- Gradio-based chat interface (with known issues)
- Basic web interface components

### Current Status:
- **Functional**: Core AI integration and prompt generation
- **In Development**: UI stability, full feature integration
- **Planned**: Enhanced wildcard system, image analysis, stable deployment

### Quick Start:
```bash
# Setup environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Install Ollama models
ollama pull wizard-uncensored:7b
ollama pull gemma3:1b

# Run main interface (may have runtime issues)
python copilot_workspace/chat_interface.py
```

### Repository Structure:
- `tools/` - Core AI integration (OllamaBridge, WildcardGenerator)
- `copilot_workspace/` - UI components (Gradio + Web interface)  
- `config/` - Model configurations and settings

**This is a development repository. Expect frequent changes and potential instability.**
