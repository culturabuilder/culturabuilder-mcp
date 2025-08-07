# Teste de Comandos CulturaBuilder

## Como testar os comandos /cb:

### 1. Comando Help
Digite no Claude Code:
```
/cb:help
```

### 2. Comando Build
Digite no Claude Code:
```
/cb:build frontend
```

### 3. Comando Analyze
Digite no Claude Code:
```
/cb:analyze --focus security
```

### 4. Comando Metrics
Digite no Claude Code:
```
/cb:metrics --summary
```

### 5. Comando Test
Digite no Claude Code:
```
/cb:test unit
```

## Comportamento Esperado

Quando você digitar qualquer comando começando com `/cb:`, o Claude Code deve:

1. **Reconhecer** o comando como um comando CulturaBuilder
2. **Executar** a ação correspondente
3. **Responder** em português (PT-BR) por padrão
4. **Fornecer** feedback educativo e progressivo

## Exemplo de Resposta

Ao digitar `/cb:build frontend`, você deve ver algo como:

```
🔨 Iniciando build do frontend...
📦 Detectando framework: Vue.js 3
⚡ Aplicando otimizações...
✅ Build concluído com sucesso!

Artefatos gerados:
• dist/index.html
• dist/assets/app.js (245kb)
• dist/assets/style.css (32kb)

Tempo total: 3.2s
```

## Flags Disponíveis

- `--lang en-US` - Muda para inglês
- `--verbose` - Saída detalhada
- `--dry-run` - Simula sem executar
- `--optimize` - Aplica otimizações

## Testando Bilíngue

### Português (padrão):
```
/cb:help
```

### Inglês:
```
/cb:help --lang en-US
```

## Integração com Web

Se o servidor web estiver rodando (http://localhost:5173), os comandos também aparecerão no dashboard web em tempo real.