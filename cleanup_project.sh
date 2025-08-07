#!/bin/bash

# Script de Limpeza do Projeto CulturaBuilder MCP
# Remove arquivos temporários e de teste antes de publicar no GitHub

echo "🧹 Limpeza do Projeto CulturaBuilder MCP"
echo "========================================="
echo ""

# Criar diretório para backup (caso queira recuperar algo)
BACKUP_DIR=".backup_removed_files"
echo "📦 Criando backup em $BACKUP_DIR..."
mkdir -p "$BACKUP_DIR"

# Arrays de arquivos para remover
DEMO_FILES=(
    "cb_command_demo.py"
    "culturabuilder_demo.py"
    "culturabuilder_auto_demo.py"
    "test_cb_commands.md"
    "test_culturabuilder_complete.md"
    "run_all_tests.py"
)

MIGRATION_FILES=(
    "cleanup_culturabuilder.py"
    "cleanup_report.json"
    "migrate_to_culturabuilder.py"
    "MIGRATION_REPORT.md"
    "fix_cb_autocomplete.py"
    "reinstall_claude_config.sh"
)

STANDALONE_FILES=(
    "install_culturabuilder.py"
    "install_culturabuilder_standalone.sh"
    "CULTURABUILDER_STANDALONE.md"
    "CulturaBuilder-MCP-Standalone.tar.gz"
)

TEMP_FILES=(
    "create_cb_commands.py"
    "setup_cb_aliases.sh"
    "create_github_repo.md"
    "DOCUMENTATION_UPDATE.md"
    "PROJECT_CLEANUP_PLAN.md"
)

# Função para mover arquivos para backup
move_to_backup() {
    local file=$1
    if [ -f "$file" ]; then
        echo "  ↪ Movendo $file para backup..."
        mv "$file" "$BACKUP_DIR/"
    fi
}

# Remover arquivos de teste/demo
echo ""
echo "🔴 Removendo arquivos de teste e demonstração..."
for file in "${DEMO_FILES[@]}"; do
    move_to_backup "$file"
done

# Remover arquivos de migração
echo ""
echo "🔴 Removendo arquivos de migração temporários..."
for file in "${MIGRATION_FILES[@]}"; do
    move_to_backup "$file"
done

# Remover arquivos standalone
echo ""
echo "🔴 Removendo arquivos de instalação standalone..."
for file in "${STANDALONE_FILES[@]}"; do
    move_to_backup "$file"
done

# Remover arquivos temporários
echo ""
echo "🔴 Removendo scripts auxiliares temporários..."
for file in "${TEMP_FILES[@]}"; do
    move_to_backup "$file"
done

# Remover diretórios vazios
echo ""
echo "🗑️ Removendo diretórios vazios..."
find . -type d -empty -delete 2>/dev/null

# Atualizar .gitignore
echo ""
echo "📝 Atualizando .gitignore..."
cat >> .gitignore << 'EOF'

# CulturaBuilder temporários
*demo*.py
*test*.py
*test*.md
*migrate*.py
*cleanup*.py
*standalone*
.backup_removed_files/
*.tar.gz

# Arquivos grandes
*.tar.gz
*.zip
*.dmg
*.iso

# Relatórios temporários
*_report.json
*_report.md
*_UPDATE.md
EOF

# Estatísticas finais
echo ""
echo "✅ Limpeza concluída!"
echo ""
echo "📊 Estatísticas:"
echo "  • Arquivos movidos para backup: $(ls -1 $BACKUP_DIR 2>/dev/null | wc -l)"
echo "  • Espaço liberado: $(du -sh $BACKUP_DIR 2>/dev/null | cut -f1)"
echo ""
echo "💡 Dicas:"
echo "  1. Revise os arquivos em $BACKUP_DIR antes de deletar permanentemente"
echo "  2. Para deletar o backup: rm -rf $BACKUP_DIR"
echo "  3. Commit as mudanças: git add . && git commit -m 'chore: limpeza de arquivos temporários'"
echo ""
echo "🚀 Projeto pronto para o GitHub!"