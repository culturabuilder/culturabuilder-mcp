# 📦 Guia Completo de Instalação - CulturaBuilder MCP

## 🚨 Problemas Comuns Resolvidos

### ❌ Erro: "command not found: pip"
**Solução**: Use `python3 -m pip` ao invés de `pip`

### ❌ Erro: "sudo: apt: command not found" no Mac
**Solução**: Use `brew` no macOS, não `apt`

---

## 🍎 macOS (seu sistema)

### Método 1: Instalação Rápida (Recomendado)
```bash
# 1. Instalar Python se necessário
brew install python3

# 2. Instalar CulturaBuilder usando python3
python3 -m pip install culturabuilder

# 3. Configurar no Claude
python3 -m culturabuilder install
```

### Método 2: Se brew não estiver instalado
```bash
# 1. Instalar Homebrew primeiro
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Depois seguir Método 1
```

### Método 3: Sem Homebrew
```bash
# 1. Verificar se Python já está instalado
python3 --version

# 2. Se Python 3.8+ estiver instalado
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip
python3 -m pip install culturabuilder

# 3. Configurar
python3 -m culturabuilder install
```

---

## 🪟 Windows

### Método 1: PowerShell (Recomendado)
```powershell
# 1. Instalar Python
winget install Python.Python.3.12

# 2. Reiniciar PowerShell

# 3. Instalar CulturaBuilder
python -m pip install culturabuilder

# 4. Configurar
python -m culturabuilder install
```

### Método 2: Download Manual
```batch
# 1. Baixar Python de https://python.org/downloads/
#    ✅ Marcar "Add Python to PATH"

# 2. Abrir novo Prompt de Comando

# 3. Instalar
python -m pip install culturabuilder

# 4. Configurar
python -m culturabuilder install
```

---

## 🐧 Linux (Ubuntu/Debian)

### Instalação Completa
```bash
# 1. Atualizar sistema
sudo apt update

# 2. Instalar Python e pip
sudo apt install python3 python3-pip

# 3. Instalar CulturaBuilder
pip3 install culturabuilder

# 4. Configurar
python3 -m culturabuilder install
```

---

## 🐧 Linux (Fedora/RHEL)

```bash
# 1. Instalar Python
sudo dnf install python3 python3-pip

# 2. Instalar CulturaBuilder
pip3 install culturabuilder

# 3. Configurar
python3 -m culturabuilder install
```

---

## 🔥 Instalação Alternativa com UV (Mais Rápido)

### Para todos os sistemas:
```bash
# 1. Instalar UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Criar ambiente virtual
uv venv

# 3. Ativar ambiente
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 4. Instalar CulturaBuilder
uv pip install culturabuilder

# 5. Configurar
python -m culturabuilder install
```

---

## 📥 Instalação do Código Fonte

### Para desenvolvedores:
```bash
# 1. Clonar repositório
git clone https://github.com/culturabuilder/culturabuilder-mcp.git
cd culturabuilder-mcp

# 2. Instalar em modo desenvolvimento
python3 -m pip install -e .

# 3. Configurar
python3 -m culturabuilder install
```

---

## 🆘 Troubleshooting

### Python não encontrado
```bash
# macOS/Linux
which python3

# Windows
where python
```

### pip não encontrado
```bash
# Use sempre python3 -m pip ao invés de pip
python3 -m pip --version

# Se não funcionar, instale pip
python3 -m ensurepip --default-pip
```

### Permissão negada
```bash
# macOS/Linux - use --user flag
python3 -m pip install --user culturabuilder

# Ou com sudo (não recomendado)
sudo python3 -m pip install culturabuilder
```

### Claude não reconhece comandos /cb:
```bash
# 1. Verificar instalação
ls ~/.claude/

# 2. Deve mostrar:
# CLAUDE.md  COMMANDS.md  FLAGS.md  etc...

# 3. Se não, reinstalar
python3 -m culturabuilder install --force
```

### Erro de SSL/Certificate
```bash
# Temporário (não recomendado para produção)
python3 -m pip install --trusted-host pypi.org culturabuilder
```

---

## ✅ Verificar Instalação

### Teste 1: Python
```bash
python3 --version
# Deve mostrar: Python 3.8 ou superior
```

### Teste 2: CulturaBuilder
```bash
python3 -m culturabuilder --version
# Deve mostrar: CulturaBuilder v3.0.0
```

### Teste 3: Claude
```bash
# Abrir Claude Desktop ou Claude Code
# Digitar:
/cb:help
# Deve mostrar lista de comandos
```

---

## 🚀 Próximos Passos

1. ✅ Python instalado
2. ✅ CulturaBuilder instalado
3. ✅ Configurado no Claude
4. 🎯 Pronto para usar!

### Primeiro comando:
```
/cb:help
```

---

## 📞 Suporte

### Erro não listado?

1. **GitHub Issues**: https://github.com/culturabuilder/culturabuilder-mcp/issues
2. **Discord**: https://discord.gg/culturabuilder
3. **Email**: support@culturabuilder.dev

### Informações para relatar erro:
```bash
# 1. Sistema operacional
uname -a  # Linux/Mac
ver       # Windows

# 2. Versão do Python
python3 --version

# 3. Erro completo
# Copie e cole a mensagem de erro
```
---
CulturaBuilder
