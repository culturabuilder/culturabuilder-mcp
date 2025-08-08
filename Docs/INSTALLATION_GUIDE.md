# 📦 Guia de Instalação Completo - CulturaBuilder

> **Tempo estimado**: 5-10 minutos | **Dificuldade**: Fácil

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação Rápida](#instalação-rápida)
3. [Windows](#instalação-no-windows)
4. [macOS](#instalação-no-macos)
5. [Linux](#instalação-no-linux)
6. [Docker](#instalação-com-docker)
7. [Instalação Manual](#instalação-manual)
8. [Verificação](#verificação-da-instalação)
9. [Atualização](#atualização)
10. [Desinstalação](#desinstalação)
11. [Troubleshooting](#troubleshooting)

---

## ✅ Pré-requisitos

### Software Necessário

| Software | Versão Mínima | Obrigatório | Verificar |
|----------|---------------|-------------|-----------|
| Claude Desktop | Última | ✅ Sim | `claude --version` |
| Python | 3.8+ | ✅ Sim | `python3 --version` |
| Node.js | 18+ | ✅ Sim | `node --version` |
| npm | 8+ | ✅ Sim | `npm --version` |
| Git | 2.0+ | ⚠️ Opcional | `git --version` |

### Requisitos de Sistema

| Sistema | Versão Mínima | Arquitetura |
|---------|---------------|-------------|
| Windows | Windows 10 | x64 |
| macOS | macOS 11 (Big Sur) | Intel/Apple Silicon |
| Linux | Ubuntu 20.04+ | x64 |

### Espaço em Disco

- **Mínimo**: 500 MB
- **Recomendado**: 1 GB

---

## 🚀 Instalação Rápida

### Método Automático (Recomendado)

```bash
# 1. Instalar via pip
pip install culturabuilder

# 2. Configurar automaticamente
python3 -m culturabuilder install

# 3. Verificar instalação
/cb:help
```

### Método Manual (Avançado)

```bash
# 1. Clonar repositório
git clone https://github.com/decomontenegro/CulturaBuilder-MCP.git
cd CulturaBuilder-MCP

# 2. Instalar dependências
cd culturabuilder-mcp
npm install
npm run build

# 3. Configurar MCP
cd ..
python3 setup/install.py
```

---

## 🪟 Instalação no Windows

### Passo 1: Instalar Pré-requisitos

#### Python
1. Baixe Python em https://python.org/downloads
2. Execute o instalador
3. **IMPORTANTE**: Marque "Add Python to PATH"
4. Clique em "Install Now"

#### Node.js
1. Baixe Node.js em https://nodejs.org
2. Execute o instalador
3. Siga as instruções padrão
4. Reinicie o computador

#### Claude Desktop
1. Baixe em https://claude.ai/desktop
2. Execute o instalador
3. Faça login com sua conta

### Passo 2: Instalar CulturaBuilder

#### PowerShell (Recomendado)

```powershell
# Abrir PowerShell como Administrador
# Pressione Windows + X, selecione "Windows PowerShell (Admin)"

# Instalar CulturaBuilder
pip install culturabuilder

# Se der erro, tente:
python -m pip install culturabuilder

# Configurar
python -m culturabuilder install
```

#### Command Prompt

```cmd
# Abrir CMD como Administrador
# Pesquise "cmd", clique direito, "Executar como administrador"

# Instalar
pip install culturabuilder

# Configurar
python -m culturabuilder install
```

### Passo 3: Configuração Manual (se necessário)

```powershell
# Localizar arquivo de configuração
$configPath = "$env:USERPROFILE\.claude\claude_desktop_config.json"

# Criar diretório se não existir
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude"

# Editar configuração
notepad $configPath
```

Adicione ao arquivo:

```json
{
  "mcpServers": {
    "culturabuilder": {
      "command": "node",
      "args": ["C:\\Users\\SEU_USUARIO\\CulturaBuilder-MCP\\culturabuilder-mcp\\dist\\index.js"],
      "env": {
        "CULTURABUILDER_LANG": "pt-BR"
      }
    }
  }
}
```

### Passo 4: Variáveis de Ambiente (Opcional)

```powershell
# Adicionar ao PATH permanentemente
[Environment]::SetEnvironmentVariable(
  "Path",
  $env:Path + ";C:\CulturaBuilder\bin",
  [EnvironmentVariableTarget]::User
)

# Definir variáveis do CulturaBuilder
[Environment]::SetEnvironmentVariable(
  "CULTURABUILDER_HOME",
  "C:\CulturaBuilder",
  [EnvironmentVariableTarget]::User
)
```

---

## 🍎 Instalação no macOS

### Passo 1: Instalar Homebrew (se não tiver)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Passo 2: Instalar Pré-requisitos

```bash
# Python
brew install python@3.11

# Node.js
brew install node

# Claude Desktop
# Baixe de https://claude.ai/desktop e arraste para Applications
```

### Passo 3: Instalar CulturaBuilder

#### Método 1: Via pip

```bash
# Instalar
pip3 install culturabuilder

# Configurar
python3 -m culturabuilder install
```

#### Método 2: Do código fonte

```bash
# Clonar repositório
git clone https://github.com/decomontenegro/CulturaBuilder-MCP.git
cd CulturaBuilder-MCP

# Instalar dependências Node
cd culturabuilder-mcp
npm install
npm run build

# Configurar
cd ..
python3 setup/install.py
```

### Passo 4: Configuração Manual (se necessário)

```bash
# Criar diretório de configuração
mkdir -p ~/.claude

# Editar configuração
nano ~/.claude/claude_desktop_config.json
```

Adicione:

```json
{
  "mcpServers": {
    "culturabuilder": {
      "command": "node",
      "args": ["/Users/SEU_USUARIO/CulturaBuilder-MCP/culturabuilder-mcp/dist/index.js"],
      "env": {
        "CULTURABUILDER_LANG": "pt-BR"
      }
    }
  }
}
```

### Passo 5: Configurar Shell

```bash
# Para zsh (padrão no macOS)
echo 'export CULTURABUILDER_HOME="$HOME/.culturabuilder"' >> ~/.zshrc
echo 'export PATH="$PATH:$CULTURABUILDER_HOME/bin"' >> ~/.zshrc
source ~/.zshrc

# Para bash
echo 'export CULTURABUILDER_HOME="$HOME/.culturabuilder"' >> ~/.bash_profile
echo 'export PATH="$PATH:$CULTURABUILDER_HOME/bin"' >> ~/.bash_profile
source ~/.bash_profile
```

---

## 🐧 Instalação no Linux

### Ubuntu/Debian

#### Passo 1: Instalar Pré-requisitos

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Python e pip
sudo apt install python3 python3-pip -y

# Node.js via NodeSource
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install nodejs -y

# Git (opcional)
sudo apt install git -y

# Claude Desktop
# Baixe o .deb de https://claude.ai/desktop
sudo dpkg -i claude-desktop-*.deb
sudo apt install -f  # Corrige dependências se necessário
```

#### Passo 2: Instalar CulturaBuilder

```bash
# Via pip
pip3 install culturabuilder

# Adicionar ao PATH se necessário
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
source ~/.bashrc

# Configurar
python3 -m culturabuilder install
```

### Fedora/RHEL

```bash
# Pré-requisitos
sudo dnf install python3 python3-pip nodejs npm git -y

# CulturaBuilder
pip3 install culturabuilder
python3 -m culturabuilder install
```

### Arch Linux

```bash
# Pré-requisitos
sudo pacman -S python python-pip nodejs npm git

# CulturaBuilder
pip install culturabuilder
python -m culturabuilder install
```

### Configuração Manual Linux

```bash
# Criar configuração
mkdir -p ~/.claude
cat > ~/.claude/claude_desktop_config.json << EOF
{
  "mcpServers": {
    "culturabuilder": {
      "command": "node",
      "args": ["$HOME/CulturaBuilder-MCP/culturabuilder-mcp/dist/index.js"],
      "env": {
        "CULTURABUILDER_LANG": "pt-BR"
      }
    }
  }
}
EOF
```

---

## 🐳 Instalação com Docker

### Pré-requisitos

- Docker instalado
- Docker Compose (opcional)

### Dockerfile

```dockerfile
FROM node:18-alpine

WORKDIR /app

# Copiar arquivos
COPY culturabuilder-mcp/package*.json ./
COPY culturabuilder-mcp/tsconfig.json ./

# Instalar dependências
RUN npm ci --only=production

# Copiar código
COPY culturabuilder-mcp/src ./src

# Build
RUN npm run build

# Expor porta MCP
EXPOSE 5173

# Comando de início
CMD ["node", "dist/index.js"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  culturabuilder:
    build: .
    container_name: culturabuilder-mcp
    restart: unless-stopped
    environment:
      - CULTURABUILDER_LANG=pt-BR
      - NODE_ENV=production
    ports:
      - "5173:5173"
    volumes:
      - ./config:/app/config
      - ./logs:/app/logs
```

### Executar com Docker

```bash
# Build
docker build -t culturabuilder .

# Run
docker run -d \
  --name culturabuilder \
  -p 5173:5173 \
  -e CULTURABUILDER_LANG=pt-BR \
  culturabuilder

# Verificar logs
docker logs culturabuilder
```

---

## 🔧 Instalação Manual

### Passo 1: Baixar Código Fonte

```bash
# Via Git
git clone https://github.com/decomontenegro/CulturaBuilder-MCP.git

# Ou baixar ZIP
wget https://github.com/decomontenegro/CulturaBuilder-MCP/archive/main.zip
unzip main.zip
```

### Passo 2: Instalar Dependências

```bash
cd CulturaBuilder-MCP/culturabuilder-mcp

# Instalar dependências Node
npm install

# Build TypeScript
npm run build
```

### Passo 3: Configurar MCP Manualmente

```bash
# Localizar diretório de configuração do Claude
# Windows: %USERPROFILE%\.claude\
# macOS/Linux: ~/.claude/

# Criar arquivo de configuração
cat > ~/.claude/claude_desktop_config.json << 'EOF'
{
  "mcpServers": {
    "culturabuilder": {
      "command": "node",
      "args": ["/caminho/completo/para/culturabuilder-mcp/dist/index.js"],
      "env": {
        "CULTURABUILDER_LANG": "pt-BR",
        "CULTURABUILDER_DEBUG": "false"
      }
    }
  }
}
EOF
```

### Passo 4: Instalar Comandos

```bash
# Criar diretório de comandos
mkdir -p ~/.claude/commands/cb

# Copiar comandos (se disponíveis)
cp -r commands/* ~/.claude/commands/cb/
```

---

## ✅ Verificação da Instalação

### Teste Básico

```bash
# No Claude Desktop ou Claude Code
/cb:help

# Deve listar todos os comandos disponíveis
```

### Teste Completo

```bash
# 1. Verificar MCP Server
node culturabuilder-mcp/dist/index.js --version

# 2. Verificar configuração
cat ~/.claude/claude_desktop_config.json | grep culturabuilder

# 3. Testar comando simples
/cb:config list

# 4. Testar comando complexo
/cb:analyze --deep
```

### Script de Verificação

```bash
#!/bin/bash
# verify_installation.sh

echo "🔍 Verificando instalação do CulturaBuilder..."

# Verificar Node.js
if command -v node &> /dev/null; then
    echo "✅ Node.js: $(node --version)"
else
    echo "❌ Node.js não encontrado"
fi

# Verificar Python
if command -v python3 &> /dev/null; then
    echo "✅ Python: $(python3 --version)"
else
    echo "❌ Python não encontrado"
fi

# Verificar configuração MCP
if [ -f ~/.claude/claude_desktop_config.json ]; then
    echo "✅ Configuração MCP encontrada"
else
    echo "❌ Configuração MCP não encontrada"
fi

# Verificar CulturaBuilder
if [ -d culturabuilder-mcp/dist ]; then
    echo "✅ Build do CulturaBuilder encontrado"
else
    echo "❌ Build do CulturaBuilder não encontrado"
fi

echo "📋 Verificação completa!"
```

---

## 🔄 Atualização

### Via pip

```bash
# Atualizar para última versão
pip install --upgrade culturabuilder

# Reconfigurar se necessário
python3 -m culturabuilder update
```

### Via Git

```bash
cd CulturaBuilder-MCP

# Baixar atualizações
git pull origin main

# Reinstalar dependências
cd culturabuilder-mcp
npm install
npm run build

# Reconfigurar
cd ..
python3 setup/update.py
```

### Atualização Automática

```bash
# Configurar atualização automática
/cb:config set auto-update true

# Verificar atualizações
/cb:config check-updates
```

---

## 🗑️ Desinstalação

### Desinstalação Completa

```bash
# 1. Remover pacote pip
pip uninstall culturabuilder

# 2. Remover configuração MCP
rm ~/.claude/claude_desktop_config.json

# 3. Remover comandos
rm -rf ~/.claude/commands/cb

# 4. Remover diretório (se instalado manualmente)
rm -rf ~/CulturaBuilder-MCP

# 5. Limpar variáveis de ambiente
# Remover linhas do ~/.bashrc ou ~/.zshrc
```

### Script de Desinstalação

```bash
#!/bin/bash
# uninstall.sh

echo "🗑️ Desinstalando CulturaBuilder..."

# Remover pip package
pip uninstall -y culturabuilder 2>/dev/null

# Backup da configuração
cp ~/.claude/claude_desktop_config.json ~/.claude/claude_desktop_config.backup

# Remover configuração
sed -i '/"culturabuilder":/,/}/d' ~/.claude/claude_desktop_config.json

# Remover comandos
rm -rf ~/.claude/commands/cb

# Remover diretórios
rm -rf ~/CulturaBuilder-MCP
rm -rf ~/.culturabuilder

echo "✅ CulturaBuilder desinstalado!"
echo "📋 Backup da configuração salvo em ~/.claude/claude_desktop_config.backup"
```

---

## 🐛 Troubleshooting

### Problemas Comuns

#### "comando não encontrado"

```bash
# Verificar PATH
echo $PATH

# Adicionar ao PATH
export PATH="$PATH:$HOME/.local/bin"

# Tornar permanente
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
```

#### "Permission denied"

```bash
# Linux/macOS
sudo chmod +x setup/install.py
sudo python3 setup/install.py

# Windows (PowerShell Admin)
Set-ExecutionPolicy RemoteSigned
```

#### MCP não conecta

```bash
# Verificar processo
ps aux | grep culturabuilder

# Reiniciar Claude Desktop
pkill -f claude
```

#### Comandos não aparecem

1. Feche completamente o Claude Desktop
2. Verifique a configuração:
```bash
cat ~/.claude/claude_desktop_config.json
```
3. Recompile o MCP:
```bash
cd culturabuilder-mcp
npm run build
```
4. Reinicie o Claude Desktop

### Logs de Debug

```bash
# Ativar modo debug
export CULTURABUILDER_DEBUG=true

# Ver logs
tail -f ~/.claude/logs/mcp.log

# Windows
Get-Content "$env:USERPROFILE\.claude\logs\mcp.log" -Wait
```

### Resetar Configuração

```bash
# Backup
cp ~/.claude/claude_desktop_config.json ~/.claude/config.backup

# Resetar
rm ~/.claude/claude_desktop_config.json
python3 -m culturabuilder install --reset
```

---

## 📞 Suporte

### Canais de Suporte

- **GitHub Issues**: https://github.com/decomontenegro/CulturaBuilder-MCP/issues
- **Discord**: [Link da comunidade]
- **Email**: suporte@culturabuilder.com

### Informações para Suporte

Ao pedir ajuda, inclua:

1. Sistema operacional e versão
2. Versão do Python: `python3 --version`
3. Versão do Node.js: `node --version`
4. Logs de erro completos
5. Conteúdo de `~/.claude/claude_desktop_config.json`

---

**Última atualização**: 08 de Agosto de 2024 | **Versão**: 1.0.0