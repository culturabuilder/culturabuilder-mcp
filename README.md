# 🚀 CulturaBuilder MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Claude Desktop](https://img.shields.io/badge/Claude-Desktop-purple.svg)](https://claude.ai/desktop)

> **Framework that unifies multiple development tools into `/cb:` commands for Claude Code**

## 🎯 What is CulturaBuilder MCP?

CulturaBuilder MCP is a comprehensive framework that transforms Claude Code into a unified command center for development. Through the Model Context Protocol (MCP), we offer 16 specialized commands that integrate best practices from multiple frameworks into a single powerful interface.

### ✨ Key Features

- **⚡ Performance**: Fast response for all commands
- **🧩 Modular**: Extensible architecture with independent components
- **🔧 16 Commands**: Specialized tools for every need
- **🤖 9 AI Personas**: Virtual experts for each domain
- **💾 Token Optimization**: 70% reduction with `--uc` flag
- **🔄 Smart Delegation**: Parallel processing with sub-agents

## 📦 Quick Installation

### Prerequisites
- **Claude Desktop** or **Claude Code CLI**
- **Python 3.8+** (see OS-specific instructions below)

### 🎯 Automatic Installation (Recommended)

#### macOS/Linux:
```bash
curl -sSL https://raw.githubusercontent.com/culturabuilder/culturabuilder-mcp/main/install.sh | bash
```

#### Windows (PowerShell como Admin):
```powershell
irm https://raw.githubusercontent.com/culturabuilder/culturabuilder-mcp/main/install.ps1 | iex
```

### 🍎 macOS - Manual Installation
```bash
# If pip doesn't work, use python3 -m pip
brew install python3  # If Python not installed
python3 -m pip install culturabuilder
python3 -m culturabuilder install
```

### 🪟 Windows - Manual Installation
```powershell
# Install Python if needed
winget install Python.Python.3.12
# Restart PowerShell
python -m pip install culturabuilder
python -m culturabuilder install
```

### 🐧 Linux - Manual Installation
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip
pip3 install culturabuilder

# Fedora/RHEL
sudo dnf install python3 python3-pip
pip3 install culturabuilder

# Configure
python3 -m culturabuilder install
```

### ❌ Common Errors

**"command not found: pip"** → Use `python3 -m pip` instead of `pip`

**"sudo: apt: command not found" (on Mac)** → Use `brew` on macOS, not `apt`

📚 **[Complete Installation Guide](INSTALL.md)** with detailed troubleshooting

## 🎮 Available Commands (16)

### Development (4)
- `/cb:build` - Build components with automatic framework detection
- `/cb:implement` - Implement features with specialized AI
- `/cb:design` - Create architectures and system designs
- `/cb:test` - Execute and create tests

### Analysis (4)
- `/cb:analyze` - Deep code and architecture analysis
- `/cb:troubleshoot` - Debug and resolve issues
- `/cb:explain` - Technical explanations
- `/cb:estimate` - Time and complexity estimation

### Quality (3)
- `/cb:improve` - Automatic quality improvement
- `/cb:cleanup` - Technical debt reduction
- `/cb:document` - Generate documentation

### Management (3)
- `/cb:task` - Project management
- `/cb:git` - Smart Git management
- `/cb:spawn` - Multi-agent orchestration

### Meta (2)
- `/cb:index` - Command discovery
- `/cb:load` - Load project context

## 🧠 AI Persona System

CulturaBuilder MCP includes 9 specialized personas that activate automatically:

| Persona | Specialty | Activation |
|---------|-----------|------------|
| **Architect** | System architecture | Design and scalability |
| **Frontend** | UI/UX and accessibility | Components and interfaces |
| **Backend** | APIs, infrastructure, deployment | Services and automation |
| **Security** | Security and compliance | Vulnerabilities and protection |
| **Performance** | Optimization and metrics | Bottlenecks and speed |
| **QA** | Testing and quality | Validation and edge cases |
| **Analyzer** | Root cause analysis | Debugging and investigation |
| **Refactorer** | Clean code | Technical debt and simplification |
| **Scribe** | Documentation and education | Guides and knowledge transfer |

## 💾 Token Optimization

CulturaBuilder automatically optimizes token usage:

```
Context Usage > 75% OR Large Operations
                    ↓
           💾 TOKEN OPTIMIZATION ACTIVE 💾
                    ↓
    70% reduction using symbols, abbreviations, and compression
```

## 📚 Documentation

- **[Quick Start Guide](QUICK_START.md)** - Get started in 5 minutes
- **[Complete Guide](README_BEGINNER_FRIENDLY.md)** - Detailed tutorial
- **[Command Reference](Docs/COMMANDS_REFERENCE.md)** - All commands
- **[Architecture](Docs/ARCHITECTURE.md)** - Technical design
- **[FAQ](FAQ.md)** - Frequently asked questions

## 🤝 Contributing

We love contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

```bash
# Clone the repository
git clone https://github.com/culturabuilder/culturabuilder-mcp.git

# Create a branch
git checkout -b feature/your-feature

# Make your changes and commit
git commit -m "feat: feature description"

# Submit the PR
git push origin feature/your-feature
```

## 🏗️ Architecture

```
CulturaBuilder MCP
       │
       ├── Core Framework
       │   ├── Commands Engine (16 commands)
       │   ├── Persona System (9 personas)
       │   ├── Token Optimizer
       │   └── MCP Integration
       │
       ├── Installation System
       │   ├── Component Registry
       │   ├── Validators
       │   └── Managers
       │
       └── Claude Integration
           ├── Command Definitions
           ├── Hooks System
           └── Settings Management
```

## 📊 Performance

- **Initialization**: < 200ms
- **Simple command**: < 100ms
- **Full build**: < 60s
- **Deep analysis**: < 10s
- **Token efficiency**: 70% reduction with --uc

## 🔒 Security

- ✅ Installation only in user directory
- ✅ Validation of all inputs
- ✅ No automatic execution of external scripts
- ✅ Auditable logs of all operations
- ✅ Command argument sanitization

## 🌟 Why CulturaBuilder MCP?

1. **Unification**: One command for multiple frameworks
2. **Intelligence**: Specialized AI for each domain
3. **Efficiency**: Smart automation of repetitive tasks
4. **Quality**: Best practices applied automatically
5. **Performance**: 70% token reduction for optimal usage

## 📈 Roadmap

- [ ] More framework integrations
- [ ] Plugin system for custom commands
- [ ] Optional web interface
- [ ] Advanced metrics and analytics
- [ ] Enhanced token optimization

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/culturabuilder/culturabuilder-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/culturabuilder/culturabuilder-mcp/discussions)
- **Wiki**: [Complete Documentation](https://github.com/culturabuilder/culturabuilder-mcp/wiki)
- **Email**: contact@culturabuilder.dev

## 📄 License

MIT - Use freely in personal and commercial projects!

---

<div align="center">

**Developed with ❤️ by the CulturaBuilder Community**

[Website](https://culturabuilder.dev) • [GitHub](https://github.com/culturabuilder) • [Discord](https://discord.gg/culturabuilder)

</div>