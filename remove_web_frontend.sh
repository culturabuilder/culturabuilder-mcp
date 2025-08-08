#!/bin/bash

# Script para remover o frontend web do CulturaBuilder
# Transição para extensão VSCode

echo "================================================"
echo "   🔄 Remoção do Frontend Web CulturaBuilder   "
echo "================================================"
echo ""

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para confirmar
confirm() {
    read -p "$1 (s/n): " -n 1 -r
    echo
    [[ $REPLY =~ ^[Ss]$ ]]
}

# Informar sobre a mudança
echo -e "${BLUE}ℹ️  IMPORTANTE: Mudança de Arquitetura${NC}"
echo ""
echo "O frontend web foi descontinuado em favor de ferramentas"
echo "mais integradas ao fluxo de trabalho do desenvolvedor:"
echo ""
echo "  ✅ Extensão VSCode (nova)"
echo "  ✅ CLI melhorado"
echo "  ✅ Integração direta com Claude Desktop"
echo ""
echo -e "${YELLOW}Este script irá:${NC}"
echo "  1. Fazer backup dos arquivos web (caso queira no futuro)"
echo "  2. Remover diretórios culturabuilder-web/"
echo "  3. Atualizar documentação"
echo "  4. Limpar dependências desnecessárias"
echo ""

if ! confirm "Deseja continuar?"; then
    echo -e "${RED}Operação cancelada${NC}"
    exit 0
fi

# Criar diretório de backup
BACKUP_DIR="backup_web_frontend_$(date +%Y%m%d_%H%M%S)"
echo ""
echo -e "${YELLOW}📦 Criando backup em $BACKUP_DIR...${NC}"
mkdir -p "$BACKUP_DIR"

# Fazer backup se os diretórios existem
if [ -d "culturabuilder-web" ]; then
    echo "  - Fazendo backup de culturabuilder-web/"
    mv culturabuilder-web "$BACKUP_DIR/" 2>/dev/null
    echo -e "${GREEN}  ✓ Backup criado${NC}"
else
    echo -e "${YELLOW}  ⚠ culturabuilder-web/ não encontrado${NC}"
fi

# Remover arquivos relacionados ao web
echo ""
echo -e "${YELLOW}🗑️  Removendo arquivos web...${NC}"

# Lista de arquivos para remover
FILES_TO_REMOVE=(
    "start_culturabuilder.sh"
    "start_web.sh"
    "culturabuilder-web"
    "web_interface.md"
)

for file in "${FILES_TO_REMOVE[@]}"; do
    if [ -e "$file" ]; then
        echo "  - Removendo $file"
        rm -rf "$file" 2>/dev/null
    fi
done

echo -e "${GREEN}  ✓ Arquivos removidos${NC}"

# Atualizar .gitignore
echo ""
echo -e "${YELLOW}📝 Atualizando .gitignore...${NC}"
if [ -f ".gitignore" ]; then
    # Remover entradas antigas do web
    grep -v "culturabuilder-web" .gitignore > .gitignore.tmp
    mv .gitignore.tmp .gitignore
    
    # Adicionar backup ao gitignore
    echo "backup_web_frontend_*/" >> .gitignore
    echo -e "${GREEN}  ✓ .gitignore atualizado${NC}"
fi

# Criar arquivo de migração
echo ""
echo -e "${YELLOW}📄 Criando guia de migração...${NC}"
cat > MIGRATION_GUIDE.md << 'EOF'
# 📋 Guia de Migração - Frontend Web → Extensão VSCode

## O que Mudou?

### ❌ Removido
- Interface web Vue.js (localhost:5173)
- Backend FastAPI
- Dashboard web

### ✅ Novo
- **Extensão VSCode**: Execute comandos direto do editor
- **CLI melhorado**: Comandos mais rápidos e eficientes
- **Integração nativa**: Funciona direto com Claude Desktop

## Como Migrar?

### 1. Instalar Extensão VSCode
```bash
code --install-extension culturabuilder
```

### 2. Usar Comandos no VSCode
- Ctrl+Shift+C: Executar comando
- Menu contexto: Clique direito → CulturaBuilder
- Command Palette: Ctrl+Shift+P → "CB:"

### 3. CLI Continua Funcionando
```bash
cb help        # Ver comandos
cb build       # Construir projeto
cb analyze     # Analisar código
```

## Por que a Mudança?

1. **Integração**: VSCode é onde você já trabalha
2. **Simplicidade**: Menos complexidade, mais utilidade
3. **Performance**: Sem overhead de servidor web
4. **Manutenção**: Código mais simples e focado

## Precisa do Frontend Web?

O código foi preservado em:
`backup_web_frontend_*/`

Para restaurar:
```bash
mv backup_web_frontend_*/culturabuilder-web .
```

## Dúvidas?

- GitHub Issues: https://github.com/CulturaBuilder/CulturaBuilder-MCP/issues
- Discord: [Link da comunidade]
EOF

echo -e "${GREEN}  ✓ Guia de migração criado${NC}"

# Verificar e instalar extensão VSCode se disponível
echo ""
if command -v code &> /dev/null; then
    echo -e "${BLUE}🔍 VSCode detectado${NC}"
    if confirm "Deseja instalar a extensão CulturaBuilder para VSCode agora?"; then
        echo "Instalando extensão..."
        cd culturabuilder-vscode
        npm install
        npm run compile
        echo -e "${GREEN}  ✓ Extensão compilada${NC}"
        echo ""
        echo -e "${YELLOW}Para instalar no VSCode:${NC}"
        echo "  1. Abra o VSCode"
        echo "  2. Vá para Extensions (Ctrl+Shift+X)"
        echo "  3. Clique em '...' → Install from VSIX"
        echo "  4. Selecione culturabuilder-vscode/culturabuilder-1.0.0.vsix"
    fi
else
    echo -e "${YELLOW}⚠ VSCode não detectado${NC}"
    echo "Instale o VSCode para usar a nova extensão:"
    echo "https://code.visualstudio.com/"
fi

# Resumo final
echo ""
echo "================================================"
echo -e "${GREEN}✅ Migração Concluída!${NC}"
echo "================================================"
echo ""
echo "📁 Backup salvo em: $BACKUP_DIR/"
echo "📄 Leia MIGRATION_GUIDE.md para mais detalhes"
echo ""
echo -e "${BLUE}Próximos passos:${NC}"
echo "  1. Instale a extensão VSCode"
echo "  2. Configure Claude Desktop"
echo "  3. Use /cb: comandos direto do VSCode!"
echo ""
echo -e "${GREEN}Obrigado por usar CulturaBuilder! 🚀${NC}"