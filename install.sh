#!/bin/bash

# CulturaBuilder - Instalador Universal
# Instalação completa em um único comando

set -e

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Banner
echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════╗"
echo "║              CulturaBuilder Framework                ║"
echo "║                   Instalador v3.0.0                  ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Detectar OS
OS="unknown"
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
fi
echo -e "${GREEN}✓${NC} Sistema: ${YELLOW}$OS${NC}"

# Verificar e instalar Python se necessário
install_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${YELLOW}Instalando Python...${NC}"
        
        if [[ "$OS" == "macos" ]]; then
            # macOS - instalar Homebrew se necessário
            if ! command -v brew &> /dev/null; then
                echo -e "${YELLOW}Instalando Homebrew...${NC}"
                NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 2>/dev/null
                
                # Adicionar ao PATH
                [[ -f /opt/homebrew/bin/brew ]] && eval "$(/opt/homebrew/bin/brew shellenv)"
                [[ -f /usr/local/bin/brew ]] && eval "$(/usr/local/bin/brew shellenv)"
            fi
            brew install python3
        elif [[ "$OS" == "linux" ]]; then
            # Linux - detectar distribuição
            if [ -f /etc/debian_version ]; then
                sudo apt update && sudo apt install -y python3 python3-pip
            elif [ -f /etc/redhat-release ]; then
                sudo dnf install -y python3 python3-pip
            else
                echo -e "${RED}Instale Python 3.8+ manualmente${NC}"
                exit 1
            fi
        fi
    fi
    
    # Verificar versão
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓${NC} Python: $PYTHON_VERSION"
}

# Instalar pip se necessário
install_pip() {
    if ! python3 -m pip --version &> /dev/null; then
        echo -e "${YELLOW}Instalando pip...${NC}"
        curl -s https://bootstrap.pypa.io/get-pip.py | python3
    fi
}

# Instalar CulturaBuilder
install_culturabuilder() {
    echo -e "\n${BLUE}Instalando CulturaBuilder...${NC}"
    
    # Tentar instalar do PyPI
    if python3 -m pip install culturabuilder 2>/dev/null; then
        echo -e "${GREEN}✓${NC} Instalado via pip"
    else
        # Instalar do GitHub
        echo -e "${YELLOW}Instalando do código fonte...${NC}"
        TEMP_DIR=$(mktemp -d)
        git clone https://github.com/culturabuilder/culturabuilder-mcp.git "$TEMP_DIR" 2>/dev/null
        cd "$TEMP_DIR"
        python3 -m pip install . 2>/dev/null
        cd - > /dev/null
        rm -rf "$TEMP_DIR"
        echo -e "${GREEN}✓${NC} Instalado do GitHub"
    fi
    
    # Configurar
    echo -e "${BLUE}Configurando...${NC}"
    
    # Adicionar ao PATH se necessário
    export PATH="$HOME/.local/bin:$PATH"
    
    # Executar configuração
    python3 -m culturabuilder install --quick 2>/dev/null || {
        python3 -m culturabuilder install --minimal 2>/dev/null
    }
    
    echo -e "${GREEN}✓${NC} Configuração completa"
}

# Verificar instalação
verify() {
    if [ -d "$HOME/.claude" ]; then
        echo -e "\n${GREEN}════════════════════════════════════════════${NC}"
        echo -e "${GREEN}✓ CulturaBuilder instalado com sucesso!${NC}"
        echo -e "${GREEN}════════════════════════════════════════════${NC}"
        echo ""
        echo -e "${YELLOW}Para começar:${NC}"
        echo "Digite: /cb:help"
        echo ""
        echo -e "${BLUE}Documentação:${NC} https://github.com/culturabuilder/culturabuilder-mcp"
        return 0
    else
        echo -e "${RED}Erro na instalação${NC}"
        return 1
    fi
}

# Executar instalação
main() {
    install_python
    install_pip
    install_culturabuilder
    verify
}

# Rodar
main

# CulturaBuilder