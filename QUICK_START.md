# 🚀 Guia Rápido - CulturaBuilder em 5 Minutos

> **Objetivo**: Ter o CulturaBuilder funcionando em menos de 5 minutos!

## ✅ Checklist Rápido

Você precisa ter:
- [ ] Claude Desktop instalado ([baixar aqui](https://claude.ai/desktop))
- [ ] Python 3.8+ instalado ([baixar aqui](https://python.org/downloads))
- [ ] Terminal aberto

## 📦 Instalação Expressa (3 comandos)

### 1️⃣ Instalar CulturaBuilder
```bash
pip install culturabuilder
```

### 2️⃣ Configurar Claude Desktop
```bash
python3 -m culturabuilder install
```

### 3️⃣ Testar
Abra o Claude Desktop e digite:
```
/cb:help
```

**Pronto! Se apareceram os comandos, está funcionando!** 🎉

---

## 🎯 Seus Primeiros Comandos

### Comando mais úteis para começar:

| Comando | O que faz | Exemplo |
|---------|-----------|---------|
| `/cb:help` | Lista todos os comandos | `/cb:help` |
| `/cb:analyze` | Analisa código | `/cb:analyze meu_arquivo.py` |
| `/cb:document` | Cria documentação | `/cb:document --lang pt-BR` |
| `/cb:cleanup` | Limpa e organiza código | `/cb:cleanup` |
| `/cb:build` | Constrói projeto | `/cb:build meu-app` |

### Exemplo Prático

```bash
# No Claude Desktop, peça:
"Use /cb:analyze para verificar a qualidade do meu código"

# Ou:
"Execute /cb:document para criar um README"

# Ou ainda:
"Rode /cb:cleanup para limpar este arquivo"
```

---

## 🆘 Troubleshooting Rápido

### Se algo der errado:

| Problema | Solução Rápida |
|----------|----------------|
| "comando não encontrado" | Use `python3` ao invés de `python` |
| "pip não encontrado" | Windows: Reinstale Python com "Add to PATH"<br>Mac/Linux: `sudo apt install python3-pip` |
| Comandos /cb: não aparecem | Reinicie o Claude Desktop |
| "Permission denied" | Mac/Linux: Use `sudo`<br>Windows: Execute como Admin |

### Comando de Emergência

Se nada funcionar, execute isto:
```bash
# Remove tudo e reinstala
python3 -m culturabuilder uninstall --complete
pip uninstall culturabuilder -y
pip install culturabuilder
python3 -m culturabuilder install --repair
```

---

## 📚 Próximos Passos

### Nível Iniciante
1. Experimente `/cb:help` para ver todos os comandos
2. Use `/cb:analyze` em algum código seu
3. Teste `/cb:document` para criar documentação

### Nível Intermediário
1. Configure a interface web (opcional)
2. Personalize os comandos
3. Explore os 25+ comandos disponíveis

### Nível Avançado
1. Crie seus próprios comandos
2. Contribua com o projeto
3. Integre com seu workflow

---

## 💡 Dicas de Ouro

### Dica 1: Use Tab para Autocompletar
No terminal, após digitar `culturabuilder`, pressione Tab para ver opções.

### Dica 2: Modo Verboso para Debug
Se algo não funcionar, use:
```bash
python3 -m culturabuilder install --verbose
```

### Dica 3: Backup da Configuração
Após instalar, faça backup:
```bash
cp ~/.claude/claude_desktop_config.json ~/.claude/backup_config.json
```

### Dica 4: Comandos Favoritos
Os mais usados pela comunidade:
- `/cb:analyze` - Análise de código
- `/cb:cleanup` - Limpeza
- `/cb:document` - Documentação
- `/cb:test` - Testes

### Dica 5: Atalhos Úteis
- `/cb:h` = `/cb:help`
- `/cb:a` = `/cb:analyze`
- `/cb:d` = `/cb:document`

---

## 🔗 Links Importantes

- **GitHub**: https://github.com/CulturaBuilder/CulturaBuilder-MCP
- **Documentação**: https://culturabuilder.com/docs
- **Suporte**: https://github.com/CulturaBuilder/CulturaBuilder-MCP/issues
- **Discord**: [Comunidade CulturaBuilder]

---

## 🎉 Parabéns!

Você agora tem o CulturaBuilder instalado e funcionando!

**Próximo passo**: Digite `/cb:help` no Claude Desktop e explore os comandos!

---

<div align="center">
  
**Instalação típica: 2-3 minutos** ⏱️

**Dificuldade: Fácil** ⭐⭐☆☆☆

**Suporte: Disponível** 💬

</div>