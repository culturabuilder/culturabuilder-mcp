# 🚀 Instruções de Deploy - CulturaBuilder MCP

## Passo 1: Criar Organização no GitHub (se ainda não existe)

1. Acesse: https://github.com/organizations/new
2. Nome da organização: `culturabuilder`
3. Email de contato: `contact@culturabuilder.dev`
4. Tipo: Open Source (gratuito)

## Passo 2: Criar Novo Repositório

1. Acesse: https://github.com/culturabuilder
2. Clique em "New repository"
3. Configure:
   - **Nome**: `culturabuilder-mcp`
   - **Descrição**: "Framework integrador que unifica múltiplos frameworks de desenvolvimento em comandos /cb: para Claude Code"
   - **Público**: ✅
   - **NÃO inicializar** com README, .gitignore ou licença

## Passo 3: Configurar Repositório Local

Execute estes comandos no terminal:

```bash
# Remover remote atual
git remote remove origin

# Adicionar novo remote
git remote add origin https://github.com/culturabuilder/culturabuilder-mcp.git

# Verificar remotes
git remote -v

# Push inicial
git push -u origin main
```

## Passo 4: Configurar Repositório no GitHub

### Topics/Tags
Adicione estas tags ao repositório:
- `claude-code`
- `mcp`
- `framework`
- `ai-development`
- `bilingual`
- `automation`
- `developer-tools`
- `python`

### About Section
Configure:
- **Website**: https://culturabuilder.dev
- **Topics**: Tags acima
- **Include in the home page**: ✅

### Settings Recomendadas

1. **General**:
   - Default branch: `main`
   - Features: ✅ Issues, ✅ Discussions, ✅ Wiki
   - Pull Requests: ✅ Allow merge commits

2. **Security**:
   - Security policy: Criar SECURITY.md
   - Dependency alerts: ✅ Enable
   - Dependabot: ✅ Enable

3. **Pages** (opcional):
   - Source: Deploy from branch
   - Branch: `main` / `docs`

## Passo 5: Criar Release Inicial

1. Acesse: https://github.com/culturabuilder/culturabuilder-mcp/releases/new
2. Configure:
   - **Tag**: `v1.0.0`
   - **Title**: `CulturaBuilder MCP v1.0.0 - Framework Integrador`
   - **Description**:
   ```markdown
   # 🎉 CulturaBuilder MCP v1.0.0
   
   Primeira release oficial do CulturaBuilder MCP!
   
   ## ✨ Features
   - 25+ comandos `/cb:` especializados
   - 11 Personas IA para diferentes domínios
   - Wave Orchestration para operações complexas
   - Suporte bilíngue (PT-BR/EN-US)
   - Arquitetura modular e extensível
   
   ## 📦 Instalação
   ```bash
   pip install culturabuilder
   python3 -m culturabuilder install
   ```
   
   ## 📚 Documentação
   - [README](README.md)
   - [Guia de Início Rápido](QUICK_START.md)
   - [FAQ](FAQ.md)
   ```
   - **Anexar arquivos**: Opcional (pode criar .tar.gz do projeto)

## Passo 6: Publicar no PyPI (Opcional)

Se quiser disponibilizar via `pip install culturabuilder`:

```bash
# Instalar ferramentas
pip install build twine

# Build do pacote
python3 -m build

# Upload para PyPI
python3 -m twine upload dist/*
```

## Passo 7: Divulgação

### Redes Sociais
- Twitter/X: Anunciar com hashtags #ClaudeCode #AI #Development
- LinkedIn: Post sobre o lançamento
- Reddit: r/ClaudeAI, r/Python, r/programming

### Comunidades
- Discord de IA e Desenvolvimento
- Grupos de WhatsApp/Telegram de desenvolvedores
- Forums de programação

## Verificação Final

- [ ] Código sem referências a outros projetos
- [ ] URLs apontando para culturabuilder/culturabuilder-mcp
- [ ] README.md focado exclusivamente no CulturaBuilder MCP
- [ ] Metadados atualizados (pyproject.toml, setup.py)
- [ ] Documentação completa e bilíngue
- [ ] Licença MIT presente
- [ ] CONTRIBUTING.md atualizado
- [ ] Sem informações sensíveis no código

## 🎯 Pronto para Deploy!

O projeto está completamente preparado para ser publicado como CulturaBuilder MCP - um framework independente e inovador para Claude Code.
---
CulturaBuilder
