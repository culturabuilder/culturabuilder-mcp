# 📚 Documentação Completa - CulturaBuilder

> **Versão**: 1.0.0 | **Última atualização**: Agosto 2024 | **Licença**: MIT

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Arquitetura](#arquitetura)
3. [Instalação](#instalação)
4. [Configuração](#configuração)
5. [Uso Básico](#uso-básico)
6. [Comandos Disponíveis](#comandos-disponíveis)
7. [Workflows Comuns](#workflows-comuns)
8. [Configuração Avançada](#configuração-avançada)
9. [Troubleshooting](#troubleshooting)
10. [FAQ Técnico](#faq-técnico)

---

## 🎯 Visão Geral

### O que é o CulturaBuilder?

CulturaBuilder é um conjunto de comandos especializados para desenvolvimento que se integra ao Claude Desktop e Claude Code através do Model Context Protocol (MCP). Com 25 comandos `/cb:` verificados, automatiza tarefas complexas de desenvolvimento, análise de código, documentação e deploy.

### Por que usar?

- **🚀 Produtividade**: Automatize tarefas repetitivas com comandos simples
- **🧠 Inteligência**: Comandos que entendem contexto e sugerem melhorias
- **🌐 Bilíngue**: Suporte completo para PT-BR e EN-US
- **🔧 Extensível**: Adicione seus próprios comandos facilmente
- **📊 Métricas**: Analytics local com total privacidade

### Casos de Uso

- **Desenvolvimento Rápido**: Scaffolding, refatoração, limpeza de código
- **Análise e Qualidade**: Auditoria, segurança, performance
- **Documentação**: READMEs, changelogs, documentação técnica
- **DevOps**: Deploy, rollback, versionamento
- **Aprendizado**: Tutoriais interativos, sugestões de melhoria

---

## 🏗️ Arquitetura

### Componentes Principais

```
┌──────────────────┐     ┌──────────────────┐
│  Claude Desktop  │────▶│    MCP Server    │
│   (Aplicativo)   │     │  (TypeScript)    │
└──────────────────┘     └──────────────────┘
         │                        │
         ▼                        ▼
┌──────────────────┐     ┌──────────────────┐
│   Claude Code    │────▶│  Commands (/cb:) │
│   (Terminal)     │     │   (Markdown)     │
└──────────────────┘     └──────────────────┘
```

### Estrutura de Diretórios

```
CulturaBuilder/
├── culturabuilder-mcp/       # Servidor MCP
│   ├── src/
│   │   └── index.ts         # Definição dos comandos
│   ├── dist/                # JavaScript compilado
│   └── package.json         # Dependências Node.js
├── docs/                    # Documentação
│   ├── DOCUMENTATION.md     # Este arquivo
│   ├── COMMANDS_REFERENCE.md
│   └── ARCHITECTURE.md
└── setup/                   # Scripts de instalação
```

### Tecnologias Utilizadas

- **TypeScript/Node.js**: Servidor MCP
- **Model Context Protocol**: Comunicação com Claude
- **Markdown**: Definição de comandos
- **Bash/Python**: Scripts de automação

---

## 💾 Instalação

### Pré-requisitos

| Software | Versão Mínima | Obrigatório | Link |
|----------|---------------|-------------|------|
| Claude Desktop | Última | ✅ Sim | [Download](https://claude.ai/desktop) |
| Python | 3.8+ | ✅ Sim | [Download](https://python.org) |
| Node.js | 18+ | ✅ Sim | [Download](https://nodejs.org) |
| Git | 2.0+ | ⚠️ Recomendado | [Download](https://git-scm.com) |

### Instalação Rápida (2 minutos)

```bash
# 1. Clone o repositório
git clone https://github.com/decomontenegro/CulturaBuilder-MCP.git
cd CulturaBuilder-MCP

# 2. Instale as dependências
cd culturabuilder-mcp
npm install
npm run build

# 3. Configure o Claude Desktop
cd ..
python3 setup/install.py

# 4. Teste
# No Claude Desktop ou Terminal, digite:
/cb:help
```

### Instalação Manual

#### 1. Configurar MCP Server

```bash
# Navegue até o diretório do MCP
cd culturabuilder-mcp

# Instale dependências
npm install

# Compile TypeScript
npm run build
```

#### 2. Configurar Claude Desktop

Edite `~/.claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "culturabuilder": {
      "command": "node",
      "args": ["/caminho/para/culturabuilder-mcp/dist/index.js"],
      "env": {
        "CULTURABUILDER_LANG": "pt-BR"
      }
    }
  }
}
```

#### 3. Verificar Instalação

```bash
# No terminal com Claude Code
claude

# Digite
/cb:help
```

---

## ⚙️ Configuração

### Configuração Básica

```bash
# Definir idioma padrão
/cb:config set language pt-BR

# Definir tema (futuro)
/cb:config set theme dark

# Ver configurações
/cb:config list
```

### Variáveis de Ambiente

```bash
# ~/.bashrc ou ~/.zshrc
export CULTURABUILDER_LANG="pt-BR"
export CULTURABUILDER_DEBUG="false"
export CULTURABUILDER_HOME="$HOME/.culturabuilder"
```

### Arquivos de Configuração

- `~/.claude/claude_desktop_config.json` - Configuração do MCP
- `~/.culturabuilder/config.json` - Configurações do CulturaBuilder
- `~/.claude/commands/cb/` - Definições dos comandos

---

## 🚀 Uso Básico

### Primeiros Comandos

```bash
# Ver ajuda
/cb:help

# Analisar código
/cb:analyze

# Construir projeto
/cb:build

# Criar documentação
/cb:document --lang pt-BR
```

### Sintaxe dos Comandos

```
/cb:<comando> [argumentos] [--flags]
```

**Exemplos**:
- `/cb:build frontend --optimize`
- `/cb:test unit --coverage`
- `/cb:deploy --env production --dry-run`

### Comandos Mais Usados

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `/cb:build` | Constrói projeto | `/cb:build --all` |
| `/cb:analyze` | Analisa código | `/cb:analyze --deep` |
| `/cb:test` | Executa testes | `/cb:test --coverage` |
| `/cb:cleanup` | Limpa código | `/cb:cleanup --aggressive` |
| `/cb:git` | Operações Git | `/cb:git commit` |

---

## 📖 Comandos Disponíveis

### Visão Geral - 25 Comandos Verificados

Total de **25 comandos** organizados em **5 categorias**:

#### 🔨 Desenvolvimento (8 comandos)
- `build`, `scaffold`, `debug`, `refactor`, `improve`, `cleanup`, `inspect`, `workflow`

#### 🔍 Análise e Qualidade (4 comandos)
- `analyze`, `audit`, `security`, `performance`

#### 🧪 Testes e Deploy (4 comandos)
- `test`, `deploy`, `rollback`, `release`

#### 📝 Documentação (4 comandos)
- `document`, `readme`, `changelog`, `help`

#### 🛠️ Ferramentas (5 comandos)
- `git`, `metrics`, `ai`, `learn`, `config`

Para referência completa de cada comando, veja [COMMANDS_REFERENCE.md](COMMANDS_REFERENCE.md).

---

## 🔄 Workflows Comuns

### Workflow de Desenvolvimento

```bash
# 1. Criar estrutura do projeto
/cb:scaffold api users

# 2. Desenvolver
# ... código ...

# 3. Analisar qualidade
/cb:analyze --deep

# 4. Limpar código
/cb:cleanup

# 5. Testar
/cb:test --coverage

# 6. Commit
/cb:git commit --message "feat: nova API de usuários"
```

### Workflow de Deploy

```bash
# 1. Auditoria pré-deploy
/cb:audit --scope all

# 2. Build de produção
/cb:build --optimize --env production

# 3. Testes finais
/cb:test --all

# 4. Deploy
/cb:deploy --env production

# 5. Se houver problema
/cb:rollback --safe
```

### Workflow de Documentação

```bash
# 1. Gerar README
/cb:readme --template standard

# 2. Documentação técnica
/cb:document --format markdown

# 3. Changelog
/cb:changelog --from v1.0.0

# 4. Commit documentação
/cb:git commit --message "docs: atualizar documentação"
```

---

## 🔧 Configuração Avançada

### Criando Comandos Personalizados

1. Crie arquivo em `~/.claude/commands/cb/meu-comando.md`:

```markdown
---
allowed-tools: ['Read', 'Write', 'Edit']
description: "Meu comando personalizado"
---

# /cb:meu-comando

## Execução
1. Ler arquivos
2. Processar
3. Gerar saída
```

2. Adicione ao MCP server se necessário

### Integração com CI/CD

```yaml
# .github/workflows/culturabuilder.yml
name: CulturaBuilder CI

on: [push, pull_request]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: CulturaBuilder Analysis
        run: |
          /cb:analyze --deep
          /cb:test --coverage
          /cb:audit --fix
```

### Hooks e Automação

```bash
# .git/hooks/pre-commit
#!/bin/bash
/cb:cleanup --dry-run
/cb:test unit
```

---

## 🐛 Troubleshooting

### Problemas Comuns

#### Comandos não aparecem

**Sintoma**: `/cb:` comandos não funcionam

**Soluções**:
1. Verifique se Claude Desktop está rodando
2. Reinicie o Claude Desktop
3. Verifique `~/.claude/claude_desktop_config.json`
4. Execute: `npm run build` no diretório do MCP

#### Erro "comando não encontrado"

**Sintoma**: `command not found: claude`

**Soluções**:
```bash
# macOS
brew install claude

# Linux
sudo apt install claude-cli

# Ou use o caminho completo
/usr/local/bin/claude
```

#### MCP Server não conecta

**Sintoma**: Erro de conexão com MCP

**Soluções**:
1. Verifique se Node.js está instalado: `node --version`
2. Recompile o MCP: `cd culturabuilder-mcp && npm run build`
3. Verifique logs: `~/.claude/logs/`

### Logs e Debug

```bash
# Ativar modo debug
export CULTURABUILDER_DEBUG=true

# Ver logs do Claude
tail -f ~/.claude/logs/claude.log

# Testar MCP diretamente
node culturabuilder-mcp/dist/index.js
```

---

## ❓ FAQ Técnico

### P: Posso usar sem Claude Desktop?

**R**: Os comandos `/cb:` funcionam tanto no Claude Desktop quanto no Claude Code (terminal). Você precisa de pelo menos um dos dois.

### P: Como adicionar suporte para outro idioma?

**R**: Edite os arquivos em `~/.claude/commands/cb/` e adicione traduções. O sistema já suporta PT-BR e EN-US.

### P: Qual a diferença entre MCP e comandos nativos?

**R**: 
- **MCP Server**: Registra comandos no Claude Desktop via protocolo
- **Comandos nativos**: Arquivos markdown em `~/.claude/commands/cb/`

Ambos trabalham juntos para fornecer a funcionalidade completa.

### P: Posso usar em produção?

**R**: Sim! O CulturaBuilder é estável para uso em produção. Recomendamos:
- Usar versionamento
- Fazer backups antes de operações críticas
- Testar comandos com `--dry-run` quando disponível

### P: Como contribuir?

**R**: Veja [CONTRIBUTING.md](../CONTRIBUTING.md) para detalhes. Aceitamos PRs para:
- Novos comandos
- Correções de bugs
- Melhorias na documentação
- Traduções

---

## 📈 Roadmap

### v1.1 (Em desenvolvimento)
- [ ] Interface web simplificada
- [ ] Mais templates de scaffold
- [ ] Integração com mais IDEs

### v2.0 (Futuro)
- [ ] Comandos via API REST
- [ ] Plugins customizáveis
- [ ] Dashboard de métricas

---

## 📄 Licença

MIT - Veja [LICENSE](../LICENSE) para detalhes.

---

## 🤝 Suporte

- **GitHub Issues**: [Reportar problemas](https://github.com/decomontenegro/CulturaBuilder-MCP/issues)
- **Discussões**: [GitHub Discussions](https://github.com/decomontenegro/CulturaBuilder-MCP/discussions)
- **Email**: suporte@culturabuilder.com

---

**Última atualização**: 08 de Agosto de 2024 | **Versão**: 1.0.0