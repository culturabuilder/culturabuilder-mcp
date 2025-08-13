#!/bin/bash

# CulturaBuilder MCP - Script de Instalação Automático
# Detecta o sistema operacional e instala automaticamente

set -e  # Para em caso de erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════╗"
echo "║          CulturaBuilder MCP - Instalador             ║"
echo "║        Framework para Claude Code - v3.0.0           ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Detectar OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            OS="debian"
        elif [ -f /etc/redhat-release ]; then
            OS="redhat"
        else
            OS="linux"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
        OS="windows"
    else
        OS="unknown"
    fi
    echo -e "${GREEN}✓${NC} Sistema detectado: ${YELLOW}$OS${NC}"
}

# Verificar Python
check_python() {
    echo -e "\n${BLUE}Verificando Python...${NC}"
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | grep -Po '(?<=Python )\d+\.\d+')
        echo -e "${GREEN}✓${NC} Python encontrado: $PYTHON_VERSION"
        
        # Verificar se é 3.8+
        MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
        MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
        
        if [ "$MAJOR" -ge 3 ] && [ "$MINOR" -ge 8 ]; then
            echo -e "${GREEN}✓${NC} Python versão compatível"
            return 0
        else
            echo -e "${RED}✗${NC} Python muito antigo. Versão 3.8+ necessária"
            return 1
        fi
    else
        echo -e "${RED}✗${NC} Python não encontrado"
        return 1
    fi
}

# Instalar Python no macOS
install_python_macos() {
    echo -e "\n${BLUE}Instalando Python no macOS...${NC}"
    
    # Verificar Homebrew
    if ! command -v brew &> /dev/null; then
        echo -e "${YELLOW}Homebrew não encontrado. Instalando...${NC}"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    brew install python3
    echo -e "${GREEN}✓${NC} Python instalado via Homebrew"
}

# Instalar Python no Linux Debian/Ubuntu
install_python_debian() {
    echo -e "\n${BLUE}Instalando Python no Linux (Debian/Ubuntu)...${NC}"
    sudo apt update
    sudo apt install -y python3 python3-pip
    echo -e "${GREEN}✓${NC} Python instalado"
}

# Instalar Python no Linux RedHat/Fedora
install_python_redhat() {
    echo -e "\n${BLUE}Instalando Python no Linux (RedHat/Fedora)...${NC}"
    sudo dnf install -y python3 python3-pip
    echo -e "${GREEN}✓${NC} Python instalado"
}

# Instalar CulturaBuilder
install_culturabuilder() {
    echo -e "\n${BLUE}Instalando CulturaBuilder MCP...${NC}"
    
    # Tentar diferentes métodos
    if python3 -m pip install culturabuilder 2>/dev/null; then
        echo -e "${GREEN}✓${NC} CulturaBuilder instalado com sucesso"
    elif python3 -m pip install --user culturabuilder 2>/dev/null; then
        echo -e "${GREEN}✓${NC} CulturaBuilder instalado com --user flag"
    else
        echo -e "${YELLOW}Instalando do código fonte...${NC}"
        git clone https://github.com/culturabuilder/culturabuilder-mcp.git /tmp/culturabuilder-mcp
        cd /tmp/culturabuilder-mcp
        python3 -m pip install .
        cd -
        rm -rf /tmp/culturabuilder-mcp
        echo -e "${GREEN}✓${NC} CulturaBuilder instalado do código fonte"
    fi
}

# Configurar CulturaBuilder
configure_culturabuilder() {
    echo -e "\n${BLUE}Configurando CulturaBuilder no Claude...${NC}"
    
    python3 -m culturabuilder install --quick
    
    echo -e "${GREEN}✓${NC} Configuração completa"
}

# Verificar instalação
verify_installation() {
    echo -e "\n${BLUE}Verificando instalação...${NC}"
    
    if [ -d "$HOME/.claude" ]; then
        echo -e "${GREEN}✓${NC} Diretório ~/.claude encontrado"
        
        if [ -f "$HOME/.claude/CLAUDE.md" ]; then
            echo -e "${GREEN}✓${NC} Arquivos de configuração instalados"
        fi
    else
        echo -e "${RED}✗${NC} Instalação pode ter falhado"
        return 1
    fi
    
    echo -e "\n${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✓ CulturaBuilder MCP instalado com sucesso!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${YELLOW}Próximos passos:${NC}"
    echo "1. Abra o Claude Desktop ou Claude Code"
    echo "2. Digite: /cb:help"
    echo "3. Explore os comandos disponíveis!"
    echo ""
    echo -e "${BLUE}Documentação:${NC} https://github.com/culturabuilder/culturabuilder-mcp"
    echo -e "${BLUE}Suporte:${NC} https://github.com/culturabuilder/culturabuilder-mcp/issues"
}

# Main
main() {
    detect_os
    
    # Verificar ou instalar Python
    if ! check_python; then
        case $OS in
            macos)
                install_python_macos
                ;;
            debian)
                install_python_debian
                ;;
            redhat)
                install_python_redhat
                ;;
            *)
                echo -e "${RED}Sistema não suportado para instalação automática${NC}"
                echo "Por favor, instale Python 3.8+ manualmente"
                exit 1
                ;;
        esac
    fi
    
    # Instalar CulturaBuilder
    install_culturabuilder
    
    # Configurar
    configure_culturabuilder
    
    # Verificar
    verify_installation
}

# Executar
main