# Como corrigir comandos /sc: para /cb:

## Problema
Os comandos aparecem como `/sc:` ao invés de `/cb:` no editor.

## Solução Rápida (escolha uma opção)

### Opção 1 - Correção automática (RECOMENDADO)
Execute este comando único no terminal:
```bash
curl -sSL https://raw.githubusercontent.com/culturabuilder/culturabuilder-mcp/main/fix_commands.sh | bash
```

### Opção 2 - Correção manual
Se preferir fazer manualmente, execute:
```bash
if [ -d "$HOME/.claude/commands/sc" ]; then 
    mkdir -p "$HOME/.claude/commands/cb" && \
    mv "$HOME/.claude/commands/sc"/*.md "$HOME/.claude/commands/cb/" 2>/dev/null && \
    rmdir "$HOME/.claude/commands/sc" && \
    echo "✅ Comandos corrigidos para /cb:"
else 
    echo "❌ Diretório /sc não encontrado"
fi
```

### Opção 3 - Reinstalação completa
Para reinstalar tudo do zero:
```bash
# Remover instalação antiga
python3 -m culturabuilder uninstall 2>/dev/null || rm -rf ~/.claude/commands/sc

# Instalar versão corrigida
curl -sSL https://raw.githubusercontent.com/culturabuilder/culturabuilder-mcp/main/install.sh | bash
```

## Após a correção
1. **Reinicie o editor** para ver as mudanças
2. Os comandos agora funcionam como:
   - `/cb:analyze`
   - `/cb:build`
   - `/cb:implement`
   - `/cb:help`
   - etc.

## Verificar se funcionou
```bash
ls ~/.claude/commands/cb/*.md | wc -l
```
Deve mostrar o número de comandos instalados (geralmente 16 ou mais).

---
CulturaBuilder Framework