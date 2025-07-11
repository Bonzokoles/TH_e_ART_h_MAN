# 🧙 TH_e_ART_h_MAN - AI Copilot Workspace

## AI-Powered Stable Diffusion Copilot

**Offline AI assistant using Ollama Wizard Uncensored for artwork analysis and prompt generation**

---

## 🚀 Quick Start for VSCode + Copilot

### 1. Open Workspace
```bash
# Open the workspace file in VSCode:
code ai-copilot-workspace.code-workspace
```

### 2. Setup Environment  
```bash
# Use VSCode Task (Ctrl+Shift+P → "Tasks: Run Task"):
"Setup Python Environment"

# Or manually:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install Ollama & Models
```bash
# Download Ollama from: https://ollama.ai
# Then install models:
ollama pull wizard-uncensored:13b
ollama pull wizard-uncensored:7b
```

### 4. Start Development with Copilot
```bash
# Ask GitHub Copilot or Windsurf Copilot:
"Help me implement the OllamaBridge class in tools/ollama_bridge.py 
based on the requirements in COPILOT_IMPLEMENTATION_GUIDE.md"
```

---

## 📁 Workspace Structure

```
TH_e_ART_h_MAN/
├── 📄 ai-copilot-workspace.code-workspace  # VSCode workspace config
├── 📄 COPILOT_IMPLEMENTATION_GUIDE.md     # Step-by-step guide for Copilot
├── 📄 requirements.txt                     # Python dependencies
├── 📁 training_data/                       # Training datasets
│   ├── 📁 art_descriptions/                # Artwork analysis data
│   └── 📁 sd_prompts/                      # Stable Diffusion prompts
├── 📁 ollama_models/                       # Local AI models
├── 📁 tools/                              # Data collection & processing
├── 📁 adapted_extensions/                  # Modified SD WebUI extensions
├── 📁 copilot_workspace/                   # Copilot interface & templates
└── 📁 outputs/                            # Generated models & results
```

---

## 🎯 Implementation Phases

### Phase 1: Environment Setup ✅
- [x] VSCode workspace configuration
- [x] Python environment setup
- [x] Ollama model installation
- [x] Dependencies installation

### Phase 2: Data Collection 🔄
- [ ] WikiArt scraper (`tools/art_scraper.py`)
- [ ] SD prompts collector (`tools/prompt_collector.py`)
- [ ] Data processing pipeline (`tools/data_processor.py`)

### Phase 3: Ollama Integration 🔄
- [ ] Ollama bridge (`tools/ollama_bridge.py`)
- [ ] Prompt templates (`copilot_workspace/prompt_templates.py`)
- [ ] Model fine-tuning (`tools/fine_tuning.py`)

### Phase 4: Extension Adaptation 🔄
- [ ] Ollama utilities (`adapted_extensions/ollama_utilities/`)
- [ ] Enhanced promptgen (`adapted_extensions/enhanced_promptgen/`)

### Phase 5: Copilot Interface 🔄
- [ ] Chat interface (`copilot_workspace/chat_interface.py`)
- [ ] Workspace manager (`copilot_workspace/workspace_manager.py`)

### Phase 6: Testing & Validation 🔄
- [ ] Component tests (`tests/`)
- [ ] Integration tests
- [ ] Quality assessment

---

## 🤖 Copilot Usage Examples

### Ask Copilot to Implement Core Components:

```
"Create a WikiArtScraper class that scrapes artwork descriptions 
from WikiArt.org with rate limiting and error handling"
```

```
"Implement an OllamaBridge class that connects to local Ollama 
instance and supports streaming responses for real-time chat"
```

```
"Build a Gradio interface for conversational prompt generation 
that integrates with the OllamaBridge"
```

### Ask Copilot for Data Processing:

```
"Create a data processor that converts scraped artwork descriptions 
into training data for fine-tuning Ollama models"
```

```
"Implement a prompt quality analyzer that scores Stable Diffusion 
prompts based on technical parameters and user ratings"
```

---

## 🔧 VSCode Tasks & Debugging

### Available Tasks (Ctrl+Shift+P → "Tasks: Run Task"):
- **Setup Python Environment** - Install dependencies
- **Start Ollama Service** - Launch Ollama server
- **Run Data Collection** - Execute data scrapers
- **Test Ollama Connection** - Verify model connectivity

### Debug Configurations:
- **Python: Data Collector** - Debug data collection scripts
- **Python: Ollama Bridge** - Debug Ollama integration

---

## 📚 Key References for Copilot

### Existing Extensions to Adapt:
- [ChatGPT Utilities](https://github.com/hallatore/stable-diffusion-webui-chatgpt-utilities)
- [PromptGen](https://github.com/AUTOMATIC1111/stable-diffusion-webui-promptgen)
- [Chat-Diffusion](https://github.com/prompt-engineering/chat-diffusion)

### Data Sources:
- **WikiArt** - Artwork descriptions and metadata
- **Lexica.art** - High-quality SD prompts with results
- **Civitai** - Community prompts and models
- **Met Museum API** - Professional artwork data

### AI Model Info:
- **Wizard Uncensored** - Primary conversation model
- **Custom Fine-tuned** - Art analysis specialist
- **PromptGen Models** - SD prompt generation

---

## 🎨 Example Workflows

### 1. Artwork Analysis → Prompt Generation
```
User uploads artwork image
→ Ollama analyzes visual elements
→ Generates technical SD prompt
→ Provides style guidance and parameters
```

### 2. Conversational Prompt Building
```
User: "I want a fantasy landscape"
→ Copilot asks clarifying questions
→ Builds prompt with wildcards
→ Suggests technical improvements
→ Exports to SD WebUI
```

### 3. Style Transfer Guidance
```
User: "Make it like Van Gogh"
→ Copilot provides style breakdown
→ Technical prompt modifications
→ Parameter recommendations
→ Quality enhancement tips
```

---

## 🚀 Ready to Start!

1. **Open VSCode** with the workspace file
2. **Enable GitHub Copilot** or Windsurf Copilot
3. **Follow COPILOT_IMPLEMENTATION_GUIDE.md** step by step
4. **Ask Copilot** to implement each component
5. **Test frequently** using provided configurations
6. **Document progress** and update checklists

**Let Copilot guide the implementation! 🧙‍♂️✨**
