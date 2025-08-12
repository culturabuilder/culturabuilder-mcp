```
 ██████╗██╗   ██╗██╗  ████████╗██╗   ██╗██████╗  █████╗ ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗ 
██╔════╝██║   ██║██║  ╚══██╔══╝██║   ██║██╔══██╗██╔══██╗██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║     ██║   ██║   ██║██████╔╝███████║██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝
██║     ██║   ██║██║     ██║   ██║   ██║██╔══██╗██╔══██║██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝███████╗██║   ╚██████╔╝██║  ██║██║  ██║██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚══════╝╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```
# Guia Completo

> **Para iniciantes**: Este guia começa do zero e vai até o avançado. Não se preocupe se você nunca usou terminal antes!

## 📌 Índice Rápido

- [O que é isso?](#o-que-é-culturabuilder)
- [Para que serve?](#para-que-serve)
- [Pré-requisitos](#pré-requisitos-o-que-você-precisa-ter-instalado)
- [Instalação Passo a Passo](#instalação-passo-a-passo)
- [Primeiros Comandos](#primeiros-comandos)
- [Solução de Problemas](#problemas-comuns-e-soluções)
- [Guia Avançado](#para-usuários-avançados)

---

## 🤔 O que é CulturaBuilder?

**Explicação Simples**: CulturaBuilder é um framework integrador que adiciona superpoderes ao Claude Code. Com ele, você pode usar comandos especiais que começam com `/cb:` para automatizar tarefas de programação, unificando as melhores práticas de diversos frameworks em uma única interface.

**Para Técnicos**: É um framework que integra múltiplas ferramentas e metodologias de desenvolvimento, oferecendo 17+ comandos especializados através do Claude Code, com arquitetura modular e extensível.

### Como funciona?

CulturaBuilder unifica diversos frameworks e ferramentas em comandos simples e consistentes. Todos os comandos começam com `/cb:` para fácil identificação e uso.

---

## 🎯 Para que serve?

Com CulturaBuilder, você pode pedir ao Claude para:

- **Construir projetos** → `/cb:build`
- **Analisar código** → `/cb:analyze`
- **Criar documentação** → `/cb:document`
- **Fazer deploy** → `/cb:deploy`
- **E muito mais!** → 25+ comandos disponíveis

### Exemplo Prático:
```
Você: /cb:build meu-app
Claude: [Constrói automaticamente a estrutura do seu app]
```

---

## 📋 Pré-requisitos (O que você precisa ter instalado)

### 1️⃣ Claude Desktop (OBRIGATÓRIO)

**O que é**: O aplicativo oficial do Claude para desktop.

**Como instalar**:
1. Acesse: https://claude.ai/desktop
2. Baixe a versão para seu sistema (Windows/Mac/Linux)
3. Instale seguindo as instruções na tela
4. Faça login com sua conta Anthropic

**Como verificar se está instalado**:
- Procure "Claude" nos seus aplicativos
- Deve aparecer um ícone do Claude Desktop

### 2️⃣ Python 3.8+ (OBRIGATÓRIO)

**O que é**: Linguagem de programação necessária para rodar o CulturaBuilder.

**Como instalar**:

#### Windows:
1. Acesse: https://python.org/downloads
2. Baixe Python 3.8 ou superior
3. **IMPORTANTE**: Marque "Add Python to PATH" durante instalação
4. Instale

#### macOS:
```bash
# Abra o Terminal (Cmd+Espaço, digite "Terminal")
# Cole e execute:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3
```

#### Linux:
```bash
# Abra o Terminal
sudo apt update
sudo apt install python3 python3-pip
```

**Como verificar se está instalado**:
```bash
# No terminal, digite:
python3 --version
# Deve aparecer algo como: Python 3.8.10
```

### 3️⃣ Git (OPCIONAL - só se for instalar do código fonte)

**O que é**: Sistema para baixar código do GitHub.

**Como instalar**: https://git-scm.com/downloads

---

## 📦 Instalação Passo a Passo

### 🟢 Método 1: Para Iniciantes (RECOMENDADO)

#### Passo 1: Abrir o Terminal

**Windows**:
- Pressione `Windows + R`
- Digite `cmd` e pressione Enter

**macOS**:
- Pressione `Cmd + Espaço`
- Digite "Terminal" e pressione Enter

**Linux**:
- Pressione `Ctrl + Alt + T`

#### Passo 2: Instalar o CulturaBuilder

Cole este comando no terminal e pressione Enter:

```bash
pip install culturabuilder
```

**Se der erro**, tente:
```bash
pip3 install culturabuilder
```

**Ainda com erro?** Tente:
```bash
python3 -m pip install culturabuilder
```

#### Passo 3: Configurar o Claude Desktop

Agora execute:

```bash
python3 -m culturabuilder install
```

O instalador vai:
1. Detectar onde está o Claude Desktop
2. Criar os arquivos de configuração
3. Instalar os comandos /cb:
4. Configurar tudo automaticamente

#### Passo 4: Verificar se Funcionou

1. Abra o Claude Desktop
2. Digite `/` na caixa de mensagem
3. Deve aparecer uma lista com comandos `/cb:`
4. Sucesso! 🎉

---

## 🚀 Primeiros Comandos

### Teste Básico

No Claude Desktop, digite:

```
/cb:help
```

Isso mostra todos os comandos disponíveis.

### Exemplos Práticos

```bash
# Ver comandos disponíveis
/cb:help

# Analisar qualidade do código
/cb:analyze

# Criar documentação
/cb:document --lang pt-BR

# Construir projeto
/cb:build meu-projeto

# Limpar código
/cb:cleanup
```

---

## ❌ Problemas Comuns e Soluções

### Problema 1: "comando não encontrado" ou "command not found"

**Solução**:
```bash
# Tente com python3 ao invés de python
python3 -m culturabuilder install
```

### Problema 2: "pip não encontrado"

**Solução Windows**:
1. Reinstale Python marcando "Add to PATH"
2. Reinicie o computador

**Solução Mac/Linux**:
```bash
# Instale pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### Problema 3: Comandos /cb: não aparecem no Claude

**Solução**:
1. Feche completamente o Claude Desktop
2. Execute novamente:
```bash
python3 -m culturabuilder install --repair
```
3. Abra o Claude Desktop novamente

### Problema 4: "Permission denied" ou "Acesso negado"

**Solução Mac/Linux**:
```bash
# Use sudo
sudo python3 -m culturabuilder install
```

**Solução Windows**:
- Execute o CMD como Administrador
- Clique direito no CMD → "Executar como administrador"

### Problema 5: Claude Desktop não está instalado

**Solução**:
1. Instale primeiro: https://claude.ai/desktop
2. Depois execute a instalação do CulturaBuilder

---

## 🎓 Para Usuários Avançados

### Instalação via Código Fonte

```bash
# Clone o repositório
git clone https://github.com/CulturaBuilder/CulturaBuilder-MCP.git
cd CulturaBuilder-MCP

# Instale dependências
pip install -r requirements.txt

# Execute instalador
python3 setup.py install
```

### Configuração Manual do MCP

Edite `~/.claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "culturabuilder": {
      "command": "node",
      "args": ["path/to/culturabuilder-mcp/dist/index.js"],
      "env": {
        "CULTURABUILDER_LANG": "pt-BR"
      }
    }
  }
}
```


### Desenvolvimento e Contribuição

```bash
# Fork o projeto
# Clone seu fork
git clone https://github.com/SEU-USUARIO/CulturaBuilder-MCP.git

# Crie branch
git checkout -b minha-feature

# Faça suas mudanças
# Commit
git commit -m "feat: minha nova feature"

# Push
git push origin minha-feature

# Abra Pull Request
```

---

## 📚 Documentação Completa

### Para Iniciantes
- [Guia Visual com Screenshots](docs/visual-guide.md)
- [Primeiros Passos](docs/getting-started.md)
- [FAQ - Perguntas Frequentes](docs/faq.md)

### Para Intermediários
- [Todos os Comandos](docs/commands.md)
- [Configurações Avançadas](docs/configuration.md)
- [Personalização](docs/customization.md)

### Para Avançados
- [Arquitetura do Sistema](docs/architecture.md)
- [Criando Novos Comandos](docs/extending.md)
- [API Reference](docs/api.md)

---

## 🆘 Precisa de Ajuda?

### Opções de Suporte:

1. **Issues no GitHub**: https://github.com/CulturaBuilder/CulturaBuilder-MCP/issues
2. **Discussões**: https://github.com/CulturaBuilder/CulturaBuilder-MCP/discussions
3. **Discord**: [Link para comunidade]
4. **Email**: suporte@culturabuilder.com

### Antes de pedir ajuda:

1. Verifique se o Claude Desktop está instalado
2. Confirme a versão do Python: `python3 --version`
3. Tente os passos de solução de problemas acima
4. Copie a mensagem de erro completa

---

## 🎉 Próximos Passos

Agora que instalou, experimente:

1. Digite `/cb:help` no Claude para ver todos os comandos
2. Teste `/cb:analyze` em algum código seu
3. Use `/cb:document` para criar documentação
4. Explore os outros 22+ comandos!

---

## 📝 Licença

MIT - Use livremente!

---

**Feito com ❤️ pela comunidade CulturaBuilder**