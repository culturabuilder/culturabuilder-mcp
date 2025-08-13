#!/bin/bash

# Script para corrigir comandos instalados com namespace errado
# Muda de /sc: para /cb:

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Corrigindo namespace dos comandos CulturaBuilder...${NC}"

# Verificar se existe o diretório .claude
if [ ! -d "$HOME/.claude" ]; then
    echo -e "${RED}Diretório ~/.claude não encontrado${NC}"
    exit 1
fi

# Verificar se existe commands/sc
if [ -d "$HOME/.claude/commands/sc" ]; then
    echo -e "${YELLOW}Encontrado diretório com namespace antigo /sc${NC}"
    
    # Criar diretório cb se não existir
    mkdir -p "$HOME/.claude/commands/cb"
    
    # Mover arquivos
    if ls "$HOME/.claude/commands/sc"/*.md 1> /dev/null 2>&1; then
        echo -e "${BLUE}Movendo comandos para namespace /cb...${NC}"
        mv "$HOME/.claude/commands/sc"/*.md "$HOME/.claude/commands/cb/" 2>/dev/null || true
        
        # Remover diretório sc vazio
        rmdir "$HOME/.claude/commands/sc" 2>/dev/null || true
        
        echo -e "${GREEN}✓ Comandos movidos para /cb:${NC}"
    fi
fi

# Verificar se existe commands/cb agora
if [ -d "$HOME/.claude/commands/cb" ]; then
    # Contar arquivos
    COUNT=$(ls -1 "$HOME/.claude/commands/cb"/*.md 2>/dev/null | wc -l)
    if [ "$COUNT" -gt 0 ]; then
        echo -e "${GREEN}✓ $COUNT comandos disponíveis em /cb:${NC}"
        echo ""
        echo -e "${GREEN}Comandos corrigidos com sucesso!${NC}"
        echo -e "${YELLOW}Reinicie seu editor para ver as mudanças.${NC}"
        echo ""
        echo "Comandos agora disponíveis como:"
        echo "  /cb:analyze"
        echo "  /cb:build"
        echo "  /cb:implement"
        echo "  /cb:help"
        echo "  ..."
    fi
else
    echo -e "${RED}Nenhum comando encontrado para corrigir${NC}"
    echo -e "${YELLOW}Execute a instalação primeiro:${NC}"
    echo "python3 -m culturabuilder install --quick"
fi

# CulturaBuilder