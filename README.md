# CulturaBuilder MCP 🚀

> Adicione superpoderes ao Claude Desktop com comandos especializados para desenvolvimento!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Claude Desktop](https://img.shields.io/badge/Claude-Desktop-purple.svg)](https://claude.ai/desktop)

## O que é isso? 🤔

CulturaBuilder adiciona comandos especiais (que começam com `/cb:`) ao Claude Desktop, permitindo automatizar tarefas de desenvolvimento como construir projetos, analisar código, criar documentação e muito mais!

**Exemplo**: Digite `/cb:analyze` no Claude e ele analisa seu código automaticamente.

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

## Documentação 📖

- **[Guia Rápido](QUICK_START.md)** - Comece em 5 minutos
- **[FAQ](FAQ.md)** - Perguntas frequentes
- **[Guia Completo](docs/README.md)** - Documentação detalhada
- **[Contribuindo](CONTRIBUTING.md)** - Como ajudar o projeto

## Suporte 💬

- **Issues**: [GitHub Issues](https://github.com/CulturaBuilder/CulturaBuilder-MCP/issues)
- **Discussões**: [GitHub Discussions](https://github.com/CulturaBuilder/CulturaBuilder-MCP/discussions)
- **Email**: suporte@culturabuilder.com

## Licença 📄

MIT - Use livremente!

---

**Feito com ❤️ pela comunidade CulturaBuilder**