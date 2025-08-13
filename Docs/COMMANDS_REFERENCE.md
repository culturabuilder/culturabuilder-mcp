# 📚 Referência Completa de Comandos - CulturaBuilder

> **Versão**: 1.0.0 | **Total de comandos**: 25 verificados | **Categorias**: 5

## 📋 Índice por Categoria

### 🔨 Desenvolvimento (8 comandos)
[build](#cbbuild) • [scaffold](#cbscaffold) • [debug](#cbdebug) • [refactor](#cbrefactor) • [improve](#cbimprove) • [cleanup](#cbcleanup) • [inspect](#cbinspect) • [workflow](#cbworkflow)

### 🔍 Análise e Qualidade (4 comandos)
[analyze](#cbanalyze) • [audit](#cbaudit) • [security](#cbsecurity) • [performance](#cbperformance)

### 🧪 Testes e Deploy (4 comandos)
[test](#cbtest) • [deploy](#cbdeploy) • [rollback](#cbrollback) • [release](#cbrelease)

### 📝 Documentação (4 comandos)
[document](#cbdocument) • [readme](#cbreadme) • [changelog](#cbchangelog) • [help](#cbhelp)

### 🛠️ Ferramentas (5 comandos)
[git](#cbgit) • [metrics](#cbmetrics) • [ai](#cbai) • [learn](#cblearn) • [config](#cbconfig)

---

## 🔨 Comandos de Desenvolvimento

### `/cb:build`

**Descrição**: 🔨 Constrói componentes do projeto com detecção automática de framework

**Sintaxe**:
```bash
/cb:build [target] [--optimize] [--clean] [--type]
```

**Argumentos**:
- `target` - Alvo da construção (frontend, backend, all)
- `--optimize` - Otimizar para produção
- `--clean` - Limpar antes de construir
- `--type` - Tipo de build (dev, prod, test)

**Exemplos**:
```bash
/cb:build frontend
/cb:build --all --optimize
/cb:build backend --clean --type prod
```

**Casos de Uso**:
- Construir aplicação para produção
- Compilar TypeScript para JavaScript
- Bundling e minificação de assets
- Gerar builds otimizados

---

### `/cb:scaffold`

**Descrição**: 🏗️ Cria estrutura de projetos com templates modernos

**Sintaxe**:
```bash
/cb:scaffold <type> <name> [--template] [--with-tests]
```

**Argumentos**:
- `type` - Tipo do scaffold (component, api, service, module)
- `name` - Nome do recurso a criar
- `--template` - Template específico a usar
- `--with-tests` - Incluir arquivos de teste

**Exemplos**:
```bash
/cb:scaffold component Button
/cb:scaffold api users --with-tests
/cb:scaffold service AuthService --template jwt
```

**Templates Disponíveis**:
- `react-component` - Componente React com hooks
- `vue-component` - Componente Vue 3
- `rest-api` - API REST com Express
- `graphql-api` - API GraphQL com Apollo
- `microservice` - Microserviço completo

---

### `/cb:debug`

**Descrição**: 🐛 Debug avançado com análise de stack trace

**Sintaxe**:
```bash
/cb:debug [error] [--trace] [--context] [--suggest-fix]
```

**Argumentos**:
- `error` - Mensagem de erro ou tipo
- `--trace` - Mostrar stack trace completo
- `--context` - Incluir contexto do código
- `--suggest-fix` - Sugerir correções

**Exemplos**:
```bash
/cb:debug "undefined is not a function"
/cb:debug --trace
/cb:debug TypeError --suggest-fix
```

**Funcionalidades**:
- Análise de stack trace
- Identificação de padrões de erro
- Sugestões de correção baseadas em IA
- Histórico de erros recorrentes

---

### `/cb:refactor`

**Descrição**: ♻️ Refatora código mantendo funcionalidade e melhorando qualidade

**Sintaxe**:
```bash
/cb:refactor [target] [--pattern] [--safe-mode] [--preview]
```

**Argumentos**:
- `target` - Arquivo ou diretório alvo
- `--pattern` - Padrão de refatoração (solid, dry, clean)
- `--safe-mode` - Modo seguro com validação extra
- `--preview` - Visualizar mudanças antes de aplicar

**Exemplos**:
```bash
/cb:refactor --pattern solid
/cb:refactor legacy --safe-mode
/cb:refactor src/utils --pattern dry --preview
```

**Padrões Suportados**:
- `solid` - Princípios SOLID
- `dry` - Don't Repeat Yourself
- `clean` - Clean Code principles
- `functional` - Programação funcional
- `oop` - Orientação a objetos

---

### `/cb:improve`

**Descrição**: ✨ Melhora código baseado em análise e melhores práticas

**Sintaxe**:
```bash
/cb:improve [target] [--quality] [--performance] [--security]
```

**Argumentos**:
- `target` - Arquivo ou módulo específico
- `--quality` - Focar em qualidade de código
- `--performance` - Otimizar performance
- `--security` - Melhorar segurança

**Exemplos**:
```bash
/cb:improve --quality
/cb:improve --performance --focus critical
/cb:improve auth.js --security
```

**Melhorias Aplicadas**:
- Simplificação de lógica complexa
- Otimização de algoritmos
- Correção de code smells
- Aplicação de design patterns
- Melhoria de legibilidade

---

### `/cb:cleanup`

**Descrição**: 🧹 Limpeza inteligente de código morto e formatação

**Sintaxe**:
```bash
/cb:cleanup [target] [--aggressive] [--dry-run] [--format]
```

**Argumentos**:
- `target` - Diretório ou arquivo alvo
- `--aggressive` - Limpeza agressiva
- `--dry-run` - Simular sem aplicar mudanças
- `--format` - Aplicar formatação

**Exemplos**:
```bash
/cb:cleanup --aggressive
/cb:cleanup src/ --dry-run
/cb:cleanup --format
```

**O que é limpo**:
- Código morto não utilizado
- Imports não utilizados
- Variáveis não utilizadas
- Console.logs esquecidos
- Comentários obsoletos
- Espaços em branco extras

---

### `/cb:inspect`

**Descrição**: 🔎 Inspeção profunda de código e dependências

**Sintaxe**:
```bash
/cb:inspect [target] [--dependencies] [--structure] [--complexity]
```

**Argumentos**:
- `target` - Arquivo ou módulo para inspecionar
- `--dependencies` - Analisar dependências
- `--structure` - Mostrar estrutura do código
- `--complexity` - Calcular complexidade ciclomática

**Exemplos**:
```bash
/cb:inspect --dependencies
/cb:inspect src/ --complexity
/cb:inspect app.js --structure
```

**Métricas Fornecidas**:
- Complexidade ciclomática
- Acoplamento entre módulos
- Coesão de componentes
- Tamanho de funções/classes
- Profundidade de herança

---

### `/cb:workflow`

**Descrição**: ⚡ Cria e gerencia workflows complexos de desenvolvimento

**Sintaxe**:
```bash
/cb:workflow <action> [name] [--steps] [--automate]
```

**Argumentos**:
- `action` - Ação (create, run, list, delete)
- `name` - Nome do workflow
- `--steps` - Definir passos do workflow
- `--automate` - Executar automaticamente

**Exemplos**:
```bash
/cb:workflow create ci-cd
/cb:workflow run daily-tasks
/cb:workflow list
```

**Workflows Pré-definidos**:
- `ci-cd` - Pipeline completo de CI/CD
- `daily-tasks` - Tarefas diárias de manutenção
- `release` - Processo de release
- `hotfix` - Workflow de hotfix
- `feature` - Desenvolvimento de features

---

## 🔍 Comandos de Análise e Qualidade

### `/cb:analyze`

**Descrição**: 🔍 Analisa código e arquitetura com foco em qualidade e segurança

**Sintaxe**:
```bash
/cb:analyze [scope] [--deep] [--focus] [--report]
```

**Argumentos**:
- `scope` - Escopo da análise (file, module, project)
- `--deep` - Análise profunda e detalhada
- `--focus` - Área de foco (security, performance, quality)
- `--report` - Gerar relatório detalhado

**Exemplos**:
```bash
/cb:analyze --deep
/cb:analyze --focus security
/cb:analyze module auth --report
```

**Análises Realizadas**:
- Qualidade de código (complexidade, duplicação)
- Vulnerabilidades de segurança
- Performance e gargalos
- Conformidade com padrões
- Dívida técnica

---

### `/cb:audit`

**Descrição**: 🔍 Auditoria completa do projeto com relatórios detalhados

**Sintaxe**:
```bash
/cb:audit [--scope] [--focus] [--report] [--fix]
```

**Argumentos**:
- `--scope` - Escopo da auditoria (all, security, deps)
- `--focus` - Foco específico da auditoria
- `--report` - Formato do relatório (html, json, markdown)
- `--fix` - Corrigir problemas automaticamente

**Exemplos**:
```bash
/cb:audit --scope all
/cb:audit --focus security --fix
/cb:audit --report html
```

**Verificações**:
- Dependências desatualizadas
- Vulnerabilidades conhecidas
- Licenças de dependências
- Configurações de segurança
- Conformidade com OWASP

---

### `/cb:security`

**Descrição**: 🔒 Auditoria de segurança e correção de vulnerabilidades

**Sintaxe**:
```bash
/cb:security [--scan] [--fix] [--report] [--compliance]
```

**Argumentos**:
- `--scan` - Executar scan completo
- `--fix` - Corrigir vulnerabilidades automaticamente
- `--report` - Gerar relatório de segurança
- `--compliance` - Verificar conformidade (OWASP, PCI)

**Exemplos**:
```bash
/cb:security --scan
/cb:security --fix --report
/cb:security --compliance owasp
```

**Verificações de Segurança**:
- SQL Injection
- XSS (Cross-Site Scripting)
- CSRF (Cross-Site Request Forgery)
- Exposição de dados sensíveis
- Configurações inseguras
- Dependências vulneráveis

---

### `/cb:performance`

**Descrição**: ⚡ Otimização de performance com métricas detalhadas

**Sintaxe**:
```bash
/cb:performance [target] [--profile] [--optimize] [--benchmark]
```

**Argumentos**:
- `target` - Alvo da análise
- `--profile` - Criar perfil de performance
- `--optimize` - Aplicar otimizações
- `--benchmark` - Executar benchmarks

**Exemplos**:
```bash
/cb:performance --profile
/cb:performance --optimize bundle-size
/cb:performance api --benchmark
```

**Métricas Analisadas**:
- Tempo de resposta
- Uso de memória
- Tamanho de bundle
- Tempo de carregamento
- Queries de banco de dados
- Renderização de componentes

---

## 🧪 Comandos de Testes e Deploy

### `/cb:test`

**Descrição**: 🧪 Executa testes com cobertura e relatórios detalhados

**Sintaxe**:
```bash
/cb:test [type] [--coverage] [--watch] [--parallel]
```

**Argumentos**:
- `type` - Tipo de teste (unit, integration, e2e, all)
- `--coverage` - Gerar relatório de cobertura
- `--watch` - Modo watch para desenvolvimento
- `--parallel` - Executar testes em paralelo

**Exemplos**:
```bash
/cb:test unit
/cb:test --all --coverage
/cb:test e2e --parallel
```

**Tipos de Teste**:
- `unit` - Testes unitários
- `integration` - Testes de integração
- `e2e` - Testes end-to-end
- `smoke` - Testes de smoke
- `regression` - Testes de regressão

---

### `/cb:deploy`

**Descrição**: 🚀 Implanta projeto em produção com rollback automático

**Sintaxe**:
```bash
/cb:deploy [--env] [--rollback-on-error] [--dry-run]
```

**Argumentos**:
- `--env` - Ambiente de deploy (dev, staging, prod)
- `--rollback-on-error` - Rollback automático em caso de erro
- `--dry-run` - Simular deploy sem executar

**Exemplos**:
```bash
/cb:deploy --env staging
/cb:deploy --env prod --rollback-on-error
/cb:deploy --dry-run
```

**Processo de Deploy**:
1. Validação pré-deploy
2. Build de produção
3. Execução de testes
4. Deploy para ambiente
5. Health checks
6. Rollback se necessário

---

### `/cb:rollback`

**Descrição**: ↩️ Rollback inteligente com segurança

**Sintaxe**:
```bash
/cb:rollback [target] [--to] [--safe] [--backup]
```

**Argumentos**:
- `target` - Alvo do rollback (deployment, database)
- `--to` - Versão específica ou "previous"
- `--safe` - Modo seguro com validações extras
- `--backup` - Criar backup antes do rollback

**Exemplos**:
```bash
/cb:rollback --to previous
/cb:rollback deployment --safe
/cb:rollback database --to v1.2.0 --backup
```

**Funcionalidades**:
- Rollback de deploy
- Rollback de migrations
- Rollback de configurações
- Backup automático
- Validação de integridade

---

### `/cb:release`

**Descrição**: 🚢 Prepara e cria releases com versionamento semântico

**Sintaxe**:
```bash
/cb:release [version] [--tag] [--notes] [--draft]
```

**Argumentos**:
- `version` - Versão do release (major, minor, patch, ou específica)
- `--tag` - Tag do Git para o release
- `--notes` - Notas de release
- `--draft` - Criar como rascunho

**Exemplos**:
```bash
/cb:release 1.2.0
/cb:release minor --notes "New features"
/cb:release --tag v2.0.0 --draft
```

**Processo de Release**:
1. Atualizar versão
2. Gerar changelog
3. Criar tag no Git
4. Build de produção
5. Publicar release
6. Notificar stakeholders

---

## 📝 Comandos de Documentação

### `/cb:document`

**Descrição**: 📝 Gera documentação bilíngue (PT-BR/EN-US) do projeto

**Sintaxe**:
```bash
/cb:document [type] [--lang] [--format] [--include-examples]
```

**Argumentos**:
- `type` - Tipo de documentação (api, user, technical)
- `--lang` - Idioma (pt-BR, en-US)
- `--format` - Formato (markdown, html, pdf)
- `--include-examples` - Incluir exemplos de código

**Exemplos**:
```bash
/cb:document --lang pt-BR
/cb:document api --format markdown
/cb:document user --include-examples
```

**Tipos de Documentação**:
- API Reference
- Guia do Usuário
- Documentação Técnica
- README
- Wiki

---

### `/cb:readme`

**Descrição**: 📄 Cria README profissional com badges e estrutura

**Sintaxe**:
```bash
/cb:readme [--template] [--lang] [--badges] [--toc]
```

**Argumentos**:
- `--template` - Template a usar (standard, minimal, detailed)
- `--lang` - Idioma do README
- `--badges` - Incluir badges (CI, coverage, version)
- `--toc` - Incluir índice

**Exemplos**:
```bash
/cb:readme --template standard
/cb:readme --lang pt-BR --badges
/cb:readme --template detailed --toc
```

**Seções Incluídas**:
- Descrição do projeto
- Instalação
- Uso básico
- Documentação
- Contribuindo
- Licença

---

### `/cb:changelog`

**Descrição**: 📋 Gera changelog automático baseado em commits

**Sintaxe**:
```bash
/cb:changelog [--format] [--from] [--to] [--include-contributors]
```

**Argumentos**:
- `--format` - Formato do changelog (markdown, json)
- `--from` - Versão inicial
- `--to` - Versão final
- `--include-contributors` - Incluir contribuidores

**Exemplos**:
```bash
/cb:changelog --format markdown
/cb:changelog --from v1.0.0 --to HEAD
/cb:changelog --include-contributors
```

**Categorias de Mudanças**:
- ✨ Features
- 🐛 Bug Fixes
- 📚 Documentation
- 🎨 Style
- ♻️ Refactor
- ⚡ Performance
- 🔒 Security

---

### `/cb:help`

**Descrição**: ❓ Ajuda e documentação dos comandos CulturaBuilder

**Sintaxe**:
```bash
/cb:help [command] [--lang] [--examples]
```

**Argumentos**:
- `command` - Comando específico para ajuda
- `--lang` - Idioma da ajuda
- `--examples` - Mostrar mais exemplos

**Exemplos**:
```bash
/cb:help
/cb:help build --examples
/cb:help --lang en-US
```

---

## 🛠️ Comandos de Ferramentas

### `/cb:git`

**Descrição**: 📦 Gerenciamento Git com mensagens bilíngues e changelog automático

**Sintaxe**:
```bash
/cb:git <action> [--message] [--auto-changelog] [--semantic]
```

**Argumentos**:
- `action` - Ação Git (commit, push, tag, release)
- `--message` - Mensagem de commit
- `--auto-changelog` - Gerar changelog automaticamente
- `--semantic` - Usar versionamento semântico

**Exemplos**:
```bash
/cb:git commit --message "feat: novo componente"
/cb:git release --semantic
/cb:git tag v1.0.0 --auto-changelog
```

**Funcionalidades**:
- Commits semânticos
- Geração de changelog
- Versionamento automático
- Git flow simplificado
- Hooks personalizados

---

### `/cb:metrics`

**Descrição**: 📊 Visualiza métricas de uso e performance do projeto

**Sintaxe**:
```bash
/cb:metrics [--summary] [--export] [--period]
```

**Argumentos**:
- `--summary` - Mostrar resumo das métricas
- `--export` - Exportar métricas (html, csv, json)
- `--period` - Período de análise (day, week, month)

**Exemplos**:
```bash
/cb:metrics --summary
/cb:metrics --export html
/cb:metrics --period week
```

**Métricas Disponíveis**:
- Linhas de código
- Cobertura de testes
- Complexidade
- Dívida técnica
- Performance
- Uso de recursos

---

### `/cb:ai`

**Descrição**: 🤖 Assistente IA para sugestões e otimizações de código

**Sintaxe**:
```bash
/cb:ai <query> [--context] [--suggest] [--explain]
```

**Argumentos**:
- `query` - Pergunta ou solicitação
- `--context` - Contexto adicional
- `--suggest` - Sugerir melhorias
- `--explain` - Explicar código

**Exemplos**:
```bash
/cb:ai "como otimizar este código?"
/cb:ai suggest --context current-file
/cb:ai explain authentication.js
```

**Capacidades**:
- Sugestões de otimização
- Explicação de código complexo
- Geração de testes
- Refatoração assistida
- Resolução de bugs

---

### `/cb:learn`

**Descrição**: 📚 Sistema de aprendizado interativo com tutoriais progressivos

**Sintaxe**:
```bash
/cb:learn [topic] [--level] [--interactive] [--lang]
```

**Argumentos**:
- `topic` - Tópico de aprendizado
- `--level` - Nível (beginner, intermediate, advanced)
- `--interactive` - Modo interativo
- `--lang` - Idioma do conteúdo

**Exemplos**:
```bash
/cb:learn basics
/cb:learn testing --level intermediate
/cb:learn patterns --interactive
```

**Tópicos Disponíveis**:
- Fundamentos de programação
- Padrões de design
- Testes
- Clean Code
- Arquitetura
- DevOps

---

### `/cb:config`

**Descrição**: ⚙️ Configuração do CulturaBuilder e personalização

**Sintaxe**:
```bash
/cb:config <action> [key] [value] [--global] [--reset]
```

**Argumentos**:
- `action` - Ação (get, set, list, reset)
- `key` - Chave de configuração
- `value` - Valor da configuração
- `--global` - Aplicar globalmente
- `--reset` - Resetar para padrões

**Exemplos**:
```bash
/cb:config set language pt-BR
/cb:config get theme
/cb:config list
/cb:config reset --global
```

**Configurações Disponíveis**:
- `language` - Idioma padrão (pt-BR, en-US)
- `theme` - Tema da interface (dark, light)
- `auto-save` - Salvamento automático
- `metrics` - Coleta de métricas
- `notifications` - Notificações

---

## 📊 Tabela de Referência Rápida

| Comando | Categoria | Uso Principal |
|---------|-----------|---------------|
| `/cb:build` | Desenvolvimento | Construir projeto |
| `/cb:scaffold` | Desenvolvimento | Criar estruturas |
| `/cb:debug` | Desenvolvimento | Debugar erros |
| `/cb:refactor` | Desenvolvimento | Refatorar código |
| `/cb:improve` | Desenvolvimento | Melhorar qualidade |
| `/cb:cleanup` | Desenvolvimento | Limpar código |
| `/cb:inspect` | Desenvolvimento | Inspecionar código |
| `/cb:workflow` | Desenvolvimento | Gerenciar workflows |
| `/cb:analyze` | Análise | Analisar qualidade |
| `/cb:audit` | Análise | Auditar projeto |
| `/cb:security` | Análise | Verificar segurança |
| `/cb:performance` | Análise | Otimizar performance |
| `/cb:test` | Testes | Executar testes |
| `/cb:deploy` | Deploy | Fazer deploy |
| `/cb:rollback` | Deploy | Reverter deploy |
| `/cb:release` | Deploy | Criar release |
| `/cb:document` | Documentação | Gerar docs |
| `/cb:readme` | Documentação | Criar README |
| `/cb:changelog` | Documentação | Gerar changelog |
| `/cb:help` | Documentação | Ver ajuda |
| `/cb:git` | Ferramentas | Gerenciar Git |
| `/cb:metrics` | Ferramentas | Ver métricas |
| `/cb:ai` | Ferramentas | Assistente IA |
| `/cb:learn` | Ferramentas | Aprender |
| `/cb:config` | Ferramentas | Configurar |

---

## 🔗 Links Úteis

- [Documentação Completa](DOCUMENTATION.md)
- [Guia de Instalação](INSTALLATION_GUIDE.md)
- [Arquitetura do Sistema](ARCHITECTURE.md)
- [Contribuindo](../CONTRIBUTING.md)
- [FAQ](../FAQ.md)

---

**Última atualização**: 08 de Agosto de 2024 | **Versão**: 1.0.0
---
CulturaBuilder
