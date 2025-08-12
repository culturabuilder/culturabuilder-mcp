```
 ██████╗██╗   ██╗██╗  ████████╗██╗   ██╗██████╗  █████╗ ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗ 
██╔════╝██║   ██║██║  ╚══██╔══╝██║   ██║██╔══██╗██╔══██╗██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║     ██║   ██║   ██║██████╔╝███████║██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝
██║     ██║   ██║██║     ██║   ██║   ██║██╔══██╗██╔══██║██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝███████╗██║   ╚██████╔╝██║  ██║██║  ██║██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚══════╝╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```

> Framework integrador que unifica múltiplos frameworks de desenvolvimento em comandos `/cb:` para Claude Code!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Claude Desktop](https://img.shields.io/badge/Claude-Desktop-purple.svg)](https://claude.ai/desktop)

## O que é isso? 🤔

CulturaBuilder é um framework integrador que unifica as melhores práticas de múltiplos frameworks de desenvolvimento em uma interface única e poderosa. Através de comandos `/cb:` no Claude Code, você tem acesso a ferramentas especializadas para automatizar tarefas de desenvolvimento, análise de código, documentação e muito mais!

**Comandos Unificados**: Todos os comandos começam com `/cb:` para fácil identificação
**Integração Completa**: Combina o melhor de diversos frameworks em uma solução coesa
**Exemplo**: Digite `/cb:analyze` no Claude e ele analisa seu código automaticamente usando as melhores ferramentas disponíveis.

## Início Rápido ⚡

### Pré-requisitos

Você precisa ter instalado:
1. **Claude Desktop** - [Baixar aqui](https://claude.ai/desktop)
2. **Python 3.8+** - [Baixar aqui](https://python.org/downloads)

### Instalação (2 minutos)

1. Abra o terminal e execute:
```bash
pip install culturabuilder
```

2. Configure o Claude Desktop:
```bash
python3 -m culturabuilder install
```

3. Teste no Claude Desktop:
```
/cb:help
```

**Pronto!** Se os comandos apareceram, está funcionando! 🎉

## Comandos Disponíveis 📚

O CulturaBuilder oferece 25+ comandos organizados em categorias:

| Categoria | Comandos | Exemplo |
|-----------|----------|---------|
| **Desenvolvimento** | build, scaffold, debug | `/cb:build meu-app` |
| **Análise** | analyze, audit, inspect | `/cb:analyze` |
| **Qualidade** | cleanup, improve, test | `/cb:cleanup` |
| **Documentação** | document, readme | `/cb:document --lang pt-BR` |
| **Deploy** | deploy, rollback | `/cb:deploy --env prod` |

Digite `/cb:help` no Claude para ver todos!

## Problemas Comuns ❓

| Problema | Solução |
|----------|---------|
| "comando não encontrado" | Use `python3` ao invés de `python` |
| Comandos /cb: não aparecem | Reinicie o Claude Desktop |
| "Permission denied" | Mac/Linux: use `sudo`<br>Windows: execute como Admin |

**Mais problemas?** Veja o [FAQ completo](FAQ.md) ou o [Guia de Troubleshooting](TROUBLESHOOTING.md)

## Como Funciona? 🛠️

### Sistema de Comandos `/cb:`
O CulturaBuilder implementa um sistema unificado de comandos que integra múltiplas ferramentas e frameworks através de uma interface consistente. Cada comando `/cb:` é otimizado para tarefas específicas de desenvolvimento.

### Arquitetura Integrada
- **Comandos Nativos**: 17+ comandos especializados que funcionam diretamente no Claude Code
- **Framework Unificado**: Integra as melhores práticas de diversos frameworks em uma solução coesa
- **Interface Consistente**: Todos os comandos seguem o padrão `/cb:` para facilitar o uso e memorização

### Categorias de Comandos
- **Desenvolvimento**: build, implement, design, scaffold
- **Análise**: analyze, troubleshoot, explain, inspect  
- **Qualidade**: improve, test, cleanup, refactor
- **Documentação**: document, readme, changelog
- **Gestão**: git, task, workflow, deploy

## Documentação 📖

- **[Guia Rápido](QUICK_START.md)** - Comece em 5 minutos
- **[FAQ](FAQ.md)** - Perguntas frequentes
- **[Guia Completo](README_BEGINNER_FRIENDLY.md)** - Tutorial do zero ao avançado
- **[Contribuindo](CONTRIBUTING.md)** - Como ajudar o projeto

## Suporte 💬

- **Issues**: [GitHub Issues](https://github.com/CulturaBuilder/CulturaBuilder-MCP/issues)
- **Discussões**: [GitHub Discussions](https://github.com/CulturaBuilder/CulturaBuilder-MCP/discussions)
- **Email**: suporte@culturabuilder.com

## Licença 📄

MIT - Use livremente!

---

**Feito com ❤️ pela comunidade CulturaBuilder**