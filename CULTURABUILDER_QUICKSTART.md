# 🚀 CulturaBuilder - Guia de Início Rápido

## ✨ O que é CulturaBuilder?

CulturaBuilder é a evolução do CulturaBuilder Framework - uma plataforma revolucionária que combina o poder de CLI com uma interface web moderna, bilíngue (PT-BR/EN-US) e intuitiva para construir cultura através de tecnologia.

## 📦 Instalação Rápida (macOS)

### Opção 1: Demo Interativo (Sem Dependências)

```bash
# Execute o demo interativo
python3 culturabuilder_demo.py
```

### Opção 2: Instalação Completa com Script

```bash
# Torne o script executável e rode
chmod +x start_culturabuilder.sh
./start_culturabuilder.sh
```

### Opção 3: Instalação Manual Passo a Passo

#### 1. Migrar para CulturaBuilder
```bash
# Fazer backup e migrar
python3 migrate_to_culturabuilder.py --dry-run  # Teste primeiro
python3 migrate_to_culturabuilder.py             # Migração real
```

#### 2. Instalar Backend (Python)
```bash
# Criar ambiente virtual
python3 -m venv culturabuilder-web/backend/venv

# Ativar ambiente virtual
source culturabuilder-web/backend/venv/bin/activate

# Instalar pip e atualizar
python3 -m ensurepip --upgrade
pip3 install --upgrade pip

# Instalar dependências
cd culturabuilder-web/backend
pip3 install fastapi uvicorn websockets pydantic
```

#### 3. Instalar Frontend (Node.js) - Opcional
```bash
# Se você tem Node.js instalado
cd culturabuilder-web
npm install
```

Se não tem Node.js, baixe de: https://nodejs.org/

#### 4. Executar o Sistema

**Terminal 1 - Backend:**
```bash
cd culturabuilder-web/backend
source venv/bin/activate
python3 main.py
```

**Terminal 2 - Frontend (se tiver Node.js):**
```bash
cd culturabuilder-web
npm run dev
```

## 🎮 Como Usar

### Interface CLI (Sempre Disponível)

```bash
# Demo interativo
python3 culturabuilder_demo.py

# Comandos disponíveis no demo:
/cb:build     # Construir componentes
/cb:analyze   # Analisar projeto
/cb:deploy    # Implantar aplicação
/cb:metrics   # Ver métricas
/cb:help      # Ajuda

# Comandos especiais:
lang          # Mudar idioma (PT/EN)
clear         # Limpar tela
history       # Ver histórico
exit          # Sair
```

### Interface Web (Requer Node.js)

1. Abra http://localhost:5173 no navegador
2. Use os atalhos:
   - `Cmd/Ctrl + K` - Command Palette
   - `Cmd/Ctrl + /` - AI Assistant
   - `Cmd/Ctrl + B` - Toggle Sidebar

## 🌟 Características Principais

### 🌐 Bilíngue Nativo
- Interface completa em Português e Inglês
- Troca dinâmica de idioma
- Documentação localizada

### 🎨 Design Moderno
- Interface clean com espaçamento generoso
- Tema claro/escuro
- Animações suaves
- Dashboard interativo

### 🤖 IA Integrada
- Assistente que entende linguagem natural
- Sugestões inteligentes
- Aprendizado adaptativo

### 📊 Métricas Visuais
- Dashboards em tempo real
- Gráficos interativos
- Insights automáticos

### 🎓 Tutoriais Interativos
- Aprenda fazendo
- Níveis progressivos
- Gamificação

## 🔧 Solução de Problemas

### Python não encontrado
```bash
# macOS geralmente tem python3
which python3
# Se não tiver, instale com Homebrew:
brew install python3
```

### pip não encontrado
```bash
# Use pip3 ou instale com:
python3 -m ensurepip --upgrade
```

### Erro de permissão
```bash
# Adicione permissão de execução
chmod +x arquivo.py
```

### Node.js não instalado
O frontend web é opcional. O sistema funciona perfeitamente via CLI.
Para instalar Node.js: https://nodejs.org/

## 📚 Estrutura do Projeto

```
CulturaBuilder/
├── 📱 culturabuilder-web/       # Aplicação Web
│   ├── src/                     # Frontend Vue.js
│   ├── backend/                 # Backend FastAPI
│   └── package.json            # Configuração Node.js
│
├── 🖥️ CulturaBuilder/          # Core CLI
│   ├── Commands/               # Comandos /cb:
│   ├── Core/                  # Framework core
│   └── Docs/                  # Documentação
│       ├── pt-BR/            # Docs em Português
│       └── en-US/            # Docs em Inglês
│
├── 🔧 setup/                   # Sistema de instalação
│   └── managers/              # Gerenciadores
│
├── 📝 culturabuilder_demo.py  # Demo interativo
├── 🔄 migrate_to_culturabuilder.py # Script de migração
└── 🚀 start_culturabuilder.sh # Script de inicialização
```

## 🎯 Próximos Passos

1. **Execute o Demo**: `python3 culturabuilder_demo.py`
2. **Explore os Comandos**: Digite `/cb:help` no demo
3. **Mude o Idioma**: Digite `lang` para alternar PT/EN
4. **Veja as Métricas**: Digite `/cb:metrics`

## 💡 Dicas

- Use `Tab` para autocompletar comandos (na versão completa)
- Use setas `↑↓` para navegar no histórico
- Digite `?` após um comando para ajuda detalhada
- O sistema funciona 100% offline
- Todos os dados são locais e privados

## 🤝 Comunidade

CulturaBuilder foi criado para democratizar tecnologia e construir pontes culturais através de uma experiência acessível e inclusiva.

## 📞 Suporte

- GitHub: https://github.com/culturabuilder-org/CulturaBuilder_Framework
- Email: contact@culturabuilder.org

---

**Bem-vindo ao CulturaBuilder! 🌟**
*Construa cultura através de tecnologia*