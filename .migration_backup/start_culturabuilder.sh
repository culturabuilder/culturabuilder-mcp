#!/bin/bash

# CulturaBuilder Starter Script
# Script para iniciar o CulturaBuilder Web

echo "🚀 Iniciando CulturaBuilder..."
echo "================================"

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 não encontrado!${NC}"
    echo "Por favor, instale Python 3.8+ primeiro"
    exit 1
fi

echo -e "${GREEN}✅ Python3 encontrado:${NC} $(python3 --version)"

# Diretório base
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$BASE_DIR"

# 1. Executar migração (se ainda não foi feita)
if [ ! -f ".culturabuilder_migrated" ]; then
    echo ""
    echo -e "${YELLOW}📦 Executando migração para CulturaBuilder...${NC}"
    python3 migrate_to_culturabuilder.py
    
    if [ $? -eq 0 ]; then
        touch .culturabuilder_migrated
        echo -e "${GREEN}✅ Migração concluída!${NC}"
    else
        echo -e "${RED}❌ Erro na migração${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✅ Migração já realizada${NC}"
fi

# 2. Instalar dependências do backend
echo ""
echo -e "${YELLOW}📦 Instalando dependências do backend...${NC}"

# Criar ambiente virtual se não existir
if [ ! -d "culturabuilder-web/backend/venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv culturabuilder-web/backend/venv
fi

# Ativar ambiente virtual
source culturabuilder-web/backend/venv/bin/activate

# Instalar pip se necessário
python3 -m ensurepip --upgrade 2>/dev/null

# Instalar dependências
pip3 install --upgrade pip
pip3 install -r culturabuilder-web/backend/requirements.txt

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Dependências do backend instaladas!${NC}"
else
    echo -e "${RED}❌ Erro ao instalar dependências do backend${NC}"
    exit 1
fi

# 3. Instalar dependências do frontend
echo ""
echo -e "${YELLOW}📦 Verificando Node.js...${NC}"

if command -v node &> /dev/null; then
    echo -e "${GREEN}✅ Node.js encontrado:${NC} $(node --version)"
    
    echo "Instalando dependências do frontend..."
    cd culturabuilder-web
    
    if command -v npm &> /dev/null; then
        npm install
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✅ Dependências do frontend instaladas!${NC}"
        else
            echo -e "${YELLOW}⚠️  Erro ao instalar dependências do frontend${NC}"
            echo "Você pode instalar manualmente mais tarde com: npm install"
        fi
    else
        echo -e "${YELLOW}⚠️  npm não encontrado${NC}"
        echo "Instale Node.js para ter a interface web completa"
    fi
    
    cd ..
else
    echo -e "${YELLOW}⚠️  Node.js não encontrado${NC}"
    echo "A interface web não estará disponível"
    echo "Instale Node.js de: https://nodejs.org/"
fi

# 4. Iniciar o backend
echo ""
echo -e "${GREEN}🎉 Iniciando CulturaBuilder Backend...${NC}"
echo "================================"
echo "📍 Backend API: http://localhost:8000"
echo "📍 Documentação: http://localhost:8000/docs"
echo ""
echo "Para iniciar o frontend em outro terminal:"
echo "  cd culturabuilder-web && npm run dev"
echo ""
echo -e "${YELLOW}Pressione Ctrl+C para parar${NC}"
echo "================================"

# Iniciar backend
cd culturabuilder-web/backend
python3 main.py