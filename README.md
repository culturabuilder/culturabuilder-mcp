# 🚀 CulturaBuilder MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Claude Desktop](https://img.shields.io/badge/Claude-Desktop-purple.svg)](https://claude.ai/desktop)

> **Framework integrador que unifica múltiplos frameworks de desenvolvimento em comandos `/cb:` para Claude Code**

## 🎯 O que é CulturaBuilder MCP?

CulturaBuilder MCP é um framework revolucionário que transforma o Claude Code em um centro de comando unificado para desenvolvimento. Através do Model Context Protocol (MCP), oferecemos 25+ comandos especializados que integram as melhores práticas de múltiplos frameworks em uma interface única e poderosa.

### ✨ Principais Características

- **🌍 Bilíngue**: Suporte completo para PT-BR e EN-US
- **⚡ Performance**: Resposta < 100ms para todos os comandos
- **🧩 Modular**: Arquitetura extensível com componentes independentes
- **🔧 25+ Comandos**: Ferramentas especializadas para cada necessidade
- **🤖 11 Personas IA**: Especialistas virtuais para cada domínio
- **🌊 Wave Orchestration**: Execução inteligente multi-estágio

## 📦 Instalação Rápida

### Pré-requisitos
- **Claude Desktop** ou **Claude Code CLI**
- **Python 3.8+** (veja instruções por OS abaixo)

### 🎯 Instalação Automática (Recomendado)

#### macOS/Linux:
```bash
curl -sSL https://raw.githubusercontent.com/culturabuilder/culturabuilder-mcp/main/install.sh | bash
```

#### Windows (PowerShell como Admin):
```powershell
irm https://raw.githubusercontent.com/culturabuilder/culturabuilder-mcp/main/install.ps1 | iex
```

### 🍎 macOS - Instalação Manual
```bash
# Se pip não funcionar, use python3 -m pip
brew install python3  # Se não tiver Python
python3 -m pip install culturabuilder
python3 -m culturabuilder install
```

### 🪟 Windows - Instalação Manual
```powershell
# Instalar Python se necessário
winget install Python.Python.3.12
# Reiniciar PowerShell
python -m pip install culturabuilder
python -m culturabuilder install
```

### 🐧 Linux - Instalação Manual
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip
pip3 install culturabuilder

# Fedora/RHEL
sudo dnf install python3 python3-pip
pip3 install culturabuilder

# Configurar
python3 -m culturabuilder install
```

### ❌ Erros Comuns

**"command not found: pip"** → Use `python3 -m pip` ao invés de `pip`

**"sudo: apt: command not found" (no Mac)** → Use `brew` no macOS, não `apt`

📚 **[Guia Completo de Instalação](INSTALL.md)** com troubleshooting detalhado

## 🎮 Comandos Disponíveis

### Desenvolvimento
- `/cb:build` - Constrói componentes com detecção automática de framework
- `/cb:implement` - Implementa features com IA especializada
- `/cb:design` - Cria arquiteturas e designs de sistema
- `/cb:scaffold` - Gera estruturas de projeto

### Análise e Qualidade
- `/cb:analyze` - Análise profunda de código e arquitetura
- `/cb:improve` - Melhoria automática de qualidade
- `/cb:test` - Execução e criação de testes
- `/cb:security` - Auditoria de segurança

### Documentação e Deploy
- `/cb:document` - Gera documentação bilíngue
- `/cb:git` - Gerenciamento Git inteligente
- `/cb:deploy` - Deploy com rollback automático
- `/cb:workflow` - Automação de workflows

## 🧠 Sistema de Personas IA

CulturaBuilder MCP inclui 11 personas especializadas que se ativam automaticamente:

| Persona | Especialidade | Ativação |
|---------|--------------|----------|
| **Architect** | Arquitetura de sistemas | Design e escalabilidade |
| **Frontend** | UI/UX e acessibilidade | Componentes e interfaces |
| **Backend** | APIs e confiabilidade | Serviços e infraestrutura |
| **Security** | Segurança e compliance | Vulnerabilidades e proteção |
| **Performance** | Otimização e métricas | Bottlenecks e velocidade |
| **QA** | Testes e qualidade | Validação e edge cases |
| **DevOps** | Automação e CI/CD | Deploy e monitoramento |
| **Analyzer** | Root cause analysis | Debugging e investigação |
| **Refactorer** | Clean code | Technical debt e simplificação |
| **Mentor** | Educação e guias | Aprendizado e documentação |
| **Scribe** | Escrita profissional | Documentação e localização |

## 🌊 Wave Orchestration

Para operações complexas, o CulturaBuilder ativa automaticamente o modo Wave:

```
Complexidade ≥ 0.7 + Arquivos > 20 + Tipos de operação > 2
                    ↓
           🌊 WAVE MODE ATIVADO 🌊
                    ↓
    Review → Planning → Implementation → Validation
```

## 📚 Documentação

- **[Guia de Início Rápido](QUICK_START.md)** - Comece em 5 minutos
- **[Guia Completo](README_BEGINNER_FRIENDLY.md)** - Tutorial detalhado
- **[Referência de Comandos](Docs/COMMANDS_REFERENCE.md)** - Todos os comandos
- **[Arquitetura](Docs/ARCHITECTURE.md)** - Design técnico
- **[FAQ](FAQ.md)** - Perguntas frequentes

## 🤝 Contribuindo

Adoramos contribuições! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para começar.

```bash
# Clone o repositório
git clone https://github.com/culturabuilder/culturabuilder-mcp.git

# Crie uma branch
git checkout -b feature/sua-feature

# Faça suas mudanças e commit
git commit -m "feat: descrição da feature"

# Envie o PR
git push origin feature/sua-feature
```

## 🏗️ Arquitetura

```
CulturaBuilder MCP
       │
       ├── Core Framework
       │   ├── Commands Engine
       │   ├── Persona System
       │   ├── Wave Orchestrator
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

- **Inicialização**: < 200ms
- **Comando simples**: < 100ms
- **Build completo**: < 60s
- **Análise profunda**: < 10s
- **Token efficiency**: 30-50% de redução

## 🔒 Segurança

- ✅ Instalação apenas no diretório do usuário
- ✅ Validação de todos os inputs
- ✅ Sem execução automática de scripts externos
- ✅ Logs auditáveis de todas as operações
- ✅ Sanitização de argumentos de comando

## 🌟 Por que CulturaBuilder MCP?

1. **Unificação**: Um comando para múltiplos frameworks
2. **Inteligência**: IA especializada para cada domínio
3. **Eficiência**: Automação inteligente de tarefas repetitivas
4. **Qualidade**: Melhores práticas aplicadas automaticamente
5. **Comunidade**: Suporte ativo e desenvolvimento contínuo

## 📈 Roadmap

- [ ] Suporte para mais idiomas
- [ ] Integração com mais frameworks
- [ ] Plugin system para comandos customizados
- [ ] Interface web opcional
- [ ] Métricas e analytics avançados

## 💬 Suporte

- **Issues**: [GitHub Issues](https://github.com/culturabuilder/culturabuilder-mcp/issues)
- **Discussões**: [GitHub Discussions](https://github.com/culturabuilder/culturabuilder-mcp/discussions)
- **Wiki**: [Documentação Completa](https://github.com/culturabuilder/culturabuilder-mcp/wiki)
- **Email**: contact@culturabuilder.dev

## 📄 Licença

MIT - Use livremente em projetos pessoais e comerciais!

---

<div align="center">

**Desenvolvido com ❤️ pela Comunidade CulturaBuilder**

[Website](https://culturabuilder.dev) • [GitHub](https://github.com/culturabuilder) • [Discord](https://discord.gg/culturabuilder)

</div>