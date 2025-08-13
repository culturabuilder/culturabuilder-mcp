#!/bin/bash

# Script de teste para validar o instalador do CulturaBuilder
# Testa apenas a detecção sem executar a instalação completa

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Teste do Instalador CulturaBuilder ===${NC}\n"

# Teste 1: Detecção de OS
echo -e "${YELLOW}Teste 1: Detecção de Sistema Operacional${NC}"
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "${GREEN}✓${NC} macOS detectado corretamente"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo -e "${GREEN}✓${NC} Linux detectado corretamente"
else
    echo -e "${GREEN}✓${NC} Sistema: $OSTYPE"
fi

# Teste 2: Verificação Python (sem grep -P)
echo -e "\n${YELLOW}Teste 2: Detecção de Versão Python${NC}"
if command -v python3 &> /dev/null; then
    # Usar awk ao invés de grep -P (compatível com macOS)
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓${NC} Python encontrado: $PYTHON_VERSION"
    
    # Extrair major e minor
    MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ -n "$MAJOR" ] && [ -n "$MINOR" ]; then
        echo -e "${GREEN}✓${NC} Versão parseada: Major=$MAJOR, Minor=$MINOR"
        
        if [ "$MAJOR" -ge 3 ] && [ "$MINOR" -ge 8 ]; then
            echo -e "${GREEN}✓${NC} Python 3.8+ confirmado"
        else
            echo -e "${RED}✗${NC} Python < 3.8"
        fi
    else
        echo -e "${RED}✗${NC} Falha ao parsear versão"
    fi
else
    echo -e "${RED}✗${NC} Python3 não encontrado"
fi

# Teste 3: Verificação pip
echo -e "\n${YELLOW}Teste 3: Verificação pip${NC}"
if python3 -m pip --version &> /dev/null; then
    PIP_VERSION=$(python3 -m pip --version | awk '{print $2}')
    echo -e "${GREEN}✓${NC} pip encontrado: $PIP_VERSION"
else
    echo -e "${YELLOW}⚠${NC} pip não encontrado (instalação necessária)"
fi

# Teste 4: Verificação Homebrew (macOS apenas)
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "\n${YELLOW}Teste 4: Verificação Homebrew (macOS)${NC}"
    if command -v brew &> /dev/null; then
        BREW_VERSION=$(brew --version | head -1 | awk '{print $2}')
        echo -e "${GREEN}✓${NC} Homebrew encontrado: $BREW_VERSION"
    else
        echo -e "${YELLOW}⚠${NC} Homebrew não encontrado"
    fi
fi

# Teste 5: Verificação Git
echo -e "\n${YELLOW}Teste 5: Verificação Git${NC}"
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version | awk '{print $3}')
    echo -e "${GREEN}✓${NC} Git encontrado: $GIT_VERSION"
else
    echo -e "${YELLOW}⚠${NC} Git não encontrado (necessário para instalação do fonte)"
fi

# Resumo
echo -e "\n${BLUE}=== Resumo dos Testes ===${NC}"
echo -e "${GREEN}Testes completados!${NC}"
echo ""
echo "Se todos os testes passaram, o instalador deve funcionar corretamente."
echo "Para instalar o CulturaBuilder, execute:"
echo -e "${YELLOW}  bash install.sh${NC}"
echo ""
echo "Ou baixe e execute diretamente:"
echo -e "${YELLOW}  curl -sSL https://raw.githubusercontent.com/culturabuilder/culturabuilder-mcp/main/install.sh | bash${NC}"

# CulturaBuilder