# 📋 Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2024-08-08

### 🎉 Release Inicial - CulturaBuilder

#### ✨ Added (Adicionado)
- **25 comandos `/cb:`** totalmente funcionais e verificados
  - 8 comandos de desenvolvimento (build, scaffold, debug, refactor, improve, cleanup, inspect, workflow)
  - 4 comandos de análise (analyze, audit, security, performance)
  - 4 comandos de teste/deploy (test, deploy, rollback, release)
  - 4 comandos de documentação (document, readme, changelog, help)
  - 5 comandos de ferramentas (git, metrics, ai, learn, config)
- **MCP Server** em TypeScript com integração completa ao Claude Desktop
- **Suporte bilíngue** PT-BR e EN-US nativo
- **Sistema de comandos** via arquivos Markdown em `~/.claude/commands/cb/`
- **Documentação completa** em português
  - docs/DOCUMENTATION.md - Documentação geral
  - docs/COMMANDS_REFERENCE.md - Referência de comandos
  - docs/ARCHITECTURE.md - Arquitetura técnica
  - docs/INSTALLATION_GUIDE.md - Guia de instalação
- **Scripts de instalação** automatizados para todas as plataformas
- **Arte ASCII** do CULTURABUILDER no README

#### 🔄 Changed (Alterado)
- **Renomeação completa**: SuperClaude Framework → CulturaBuilder
- **Namespace de comandos**: `/sc:` → `/cb:`
- **Foco simplificado**: Removido complexidade desnecessária
- **Arquitetura**: De 3 sistemas para 1 sistema focado (MCP + Claude Code)

#### 🗑️ Removed (Removido)
- **Frontend Web** - Interface web removida por complexidade desnecessária
- **Extensão VSCode** - Removida após análise de viabilidade
- Referências ao SuperClaude na documentação
- Arquivos de migração obsoletos
- ~110MB de código desnecessário

#### 🔒 Security (Segurança)
- Validação de input em todos os comandos
- Sanitização de argumentos
- Permissões configuráveis por comando
- Auditoria de execução de comandos

#### 🐛 Fixed (Corrigido)
- Sincronização entre comandos MCP e comandos nativos
- Inconsistência de porta na documentação (5173)
- Comandos faltantes no servidor MCP
- Documentação incorreta sobre funcionalidades

#### 📚 Documentation (Documentação)
- README.md completamente reescrito e simplificado
- README_BEGINNER_FRIENDLY.md para iniciantes
- PROJECT_STATUS.md documentando a simplificação
- Toda documentação em PT-BR com exemplos práticos

---

## [0.9.0] - 2024-08-07 (Pre-release)

### 🔄 Transição SuperClaude → CulturaBuilder

#### Added
- Primeiros 17 comandos `/cb:` funcionais
- Estrutura base do MCP server
- Configuração inicial do Claude Desktop

#### Changed
- Início da migração de SuperClaude para CulturaBuilder
- Mudança de namespace de comandos

#### Known Issues
- 8 comandos ainda não implementados no MCP
- Documentação incompleta
- VSCode extension em desenvolvimento

---

## [0.5.0] - 2024-08-05 (Alpha - SuperClaude)

### 🏗️ Versão Original SuperClaude

#### Added
- Framework inicial SuperClaude
- Comandos `/sc:` básicos
- Interface web experimental
- Extensão VSCode planejada

#### Experimental
- Frontend React para visualização
- Sistema de plugins
- Integração com múltiplas IDEs

---

## Roadmap Futuro

### [1.1.0] - Planejado
- [ ] Interface web opcional simplificada
- [ ] Mais templates de scaffold
- [ ] Comandos adicionais para cloud providers
- [ ] Melhorias na performance do MCP server

### [1.2.0] - Planejado
- [ ] Plugin system para comandos customizados
- [ ] Integração com GitHub Actions
- [ ] Dashboard de métricas local
- [ ] Suporte para mais idiomas

### [2.0.0] - Futuro
- [ ] API REST para comandos
- [ ] Cloud sync de configurações
- [ ] Marketplace de comandos
- [ ] AI-powered command suggestions

---

## Notas de Migração

### De SuperClaude (0.x) para CulturaBuilder (1.0)

#### Mudanças Breaking
1. **Namespace de comandos**: Todos os comandos `/sc:` agora são `/cb:`
2. **Configuração**: Arquivo de config movido para `~/.claude/`
3. **Dependências**: Node.js 18+ agora é obrigatório

#### Como Migrar
```bash
# 1. Desinstalar SuperClaude
pip uninstall superclaude

# 2. Instalar CulturaBuilder
pip install culturabuilder

# 3. Reconfigurar
python3 -m culturabuilder install

# 4. Atualizar comandos nos scripts
# Substituir /sc: por /cb: em todos os lugares
```

---

## Contribuidores

### Desenvolvedores Principais
- André Montenegro (@decomontenegro) - Criador e mantenedor

### Contribuições
- Comunidade CulturaBuilder - Feedback e testes
- Usuários beta - Reportes de bugs e sugestões

### Agradecimentos Especiais
- Anthropic pela criação do Claude e MCP
- Comunidade open source pelos exemplos e inspiração

---

## Links

- [GitHub](https://github.com/decomontenegro/CulturaBuilder-MCP)
- [Issues](https://github.com/decomontenegro/CulturaBuilder-MCP/issues)
- [Discussions](https://github.com/decomontenegro/CulturaBuilder-MCP/discussions)

---

**Convenções de Versionamento**:
- **MAJOR**: Mudanças incompatíveis na API
- **MINOR**: Funcionalidades adicionadas de forma compatível
- **PATCH**: Correções de bugs compatíveis

**Tipos de Mudança**:
- ✨ **Added**: Nova funcionalidade
- 🔄 **Changed**: Mudanças em funcionalidades existentes
- ⚠️ **Deprecated**: Funcionalidades que serão removidas
- 🗑️ **Removed**: Funcionalidades removidas
- 🐛 **Fixed**: Correções de bugs
- 🔒 **Security**: Correções de vulnerabilidades

---

[1.0.0]: https://github.com/decomontenegro/CulturaBuilder-MCP/releases/tag/v1.0.0
[0.9.0]: https://github.com/decomontenegro/CulturaBuilder-MCP/releases/tag/v0.9.0
[0.5.0]: https://github.com/decomontenegro/CulturaBuilder-MCP/releases/tag/v0.5.0