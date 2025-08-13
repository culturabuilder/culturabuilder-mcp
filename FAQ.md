# 🤔 FAQ - Perguntas Frequentes sobre CulturaBuilder

## Perguntas Básicas

### O que é CulturaBuilder?
É um framework integrador que unifica múltiplos frameworks de desenvolvimento, oferecendo comandos especiais começando com `/cb:` no Claude Code para automatizar tarefas de desenvolvimento.

### É gratuito?
Sim, o CulturaBuilder é 100% gratuito e open source (código aberto).

### Preciso saber programar para usar?
Não necessariamente! Muitos comandos são simples e autoexplicativos. Por exemplo, `/cb:document` cria documentação automaticamente.

### Funciona com Claude.ai (navegador)?
Não, apenas com o Claude Desktop (aplicativo instalado no computador).

### Funciona no Windows/Mac/Linux?
Sim, funciona em todos os três sistemas operacionais.

---

## Instalação

### Por que preciso do Python?
O CulturaBuilder é escrito em Python, então precisa dele para funcionar. É como precisar do Adobe Reader para abrir PDFs.

### Qual versão do Python preciso?
Python 3.8 ou superior. Para verificar: `python3 --version`

### Preciso pagar pelo Claude Desktop?
O Claude Desktop em si pode ter planos pagos, mas o CulturaBuilder funciona com qualquer versão.

### Como sei se a instalação funcionou?
Abra o Claude Desktop e digite `/`. Se aparecerem comandos `/cb:`, funcionou!

### Posso instalar sem usar o terminal?
Infelizmente não. O terminal é necessário, mas fornecemos comandos prontos para copiar e colar.

---

## Uso

### Como uso os comandos /cb:?
No Claude Desktop, digite `/cb:` seguido do comando. Exemplo: `/cb:help`

### Quantos comandos existem?
Mais de 25 comandos especializados para diferentes tarefas.

### Os comandos funcionam em português?
Sim! Suporte completo para português (PT-BR) e inglês (EN-US).

### Posso criar meus próprios comandos?
Sim, usuários avançados podem estender o sistema criando novos comandos.

### Os comandos são seguros?
Sim, todos os comandos são executados localmente no seu computador.

---

## Problemas Comuns

### "comando não encontrado"
**Solução**: Use `python3` ao invés de `python`

### "pip não está instalado"
**Solução**: 
- Windows: Reinstale Python marcando "Add to PATH"
- Mac/Linux: `sudo apt install python3-pip`

### Comandos /cb: não aparecem
**Soluções**:
1. Reinicie o Claude Desktop
2. Execute: `python3 -m culturabuilder install --repair`

### "Permission denied"
**Solução**: 
- Mac/Linux: Use `sudo` antes do comando
- Windows: Execute CMD como Administrador

### Claude Desktop não abre após instalação
**Solução**: 
1. Desinstale: `python3 -m culturabuilder uninstall`
2. Reinstale o Claude Desktop
3. Reinstale o CulturaBuilder

---

## Funcionalidades

### Posso usar offline?
Parcialmente. Os comandos funcionam offline, mas o Claude Desktop precisa de internet.

### Funciona com outros modelos de IA?
Não, é específico para o Claude Desktop da Anthropic.

### Posso compartilhar configurações com minha equipe?
Sim, as configurações podem ser exportadas e compartilhadas.

### Tem interface gráfica?
Sim, há uma interface web opcional em `http://localhost:3000`

### Como atualizo para nova versão?
```bash
pip install --upgrade culturabuilder
python3 -m culturabuilder update
```

---

## Segurança e Privacidade

### Meus dados são enviados para algum servidor?
Não, tudo funciona localmente no seu computador.

### É seguro usar em projetos comerciais?
Sim, a licença MIT permite uso comercial.

### O código é auditável?
Sim, todo código é open source no GitHub.

### Preciso dar permissões especiais?
Apenas as permissões normais para instalar software.

### Pode acessar meus arquivos?
Apenas os arquivos que você explicitamente pedir para processar.

---

## Desenvolvimento

### Como contribuo com o projeto?
Veja o arquivo CONTRIBUTING.md no GitHub para instruções detalhadas.

### Onde reporto bugs?
No GitHub Issues: https://github.com/CulturaBuilder/CulturaBuilder-MCP/issues

### Tem documentação para desenvolvedores?
Sim, na pasta `docs/` do repositório.

### Posso fazer fork do projeto?
Sim, é open source com licença MIT.

### Como adiciono um novo comando?
Veja `docs/extending.md` para guia completo.

---

## Comparações

### Qual a diferença do CulturaBuilder para outros MCPs?
CulturaBuilder é focado em desenvolvimento com suporte bilíngue e comandos especializados.

### É melhor que usar o Claude puro?
É diferente - adiciona comandos especializados que o Claude puro não tem.

### Funciona com ChatGPT/Gemini/outros?
Não, é específico para Claude Desktop.

### CulturaBuilder é único?
Sim, é um framework original desenvolvido especificamente para integrar múltiplos frameworks em comandos unificados.

---

## Diversos

### Como desinstalo completamente?
```bash
python3 -m culturabuilder uninstall --complete
```

### Ocupa muito espaço?
Cerca de 50MB instalado.

### Deixa o Claude mais lento?
Impacto mínimo no desempenho.

### Preciso de conhecimento técnico?
Básico para instalação, depois é bem intuitivo.

### Tem vídeos tutoriais?
Em breve! Por enquanto, use a documentação escrita.

---

## Ainda com dúvidas?

### Onde consigo mais ajuda?

1. **GitHub Discussions**: Perguntas gerais
2. **GitHub Issues**: Bugs e problemas
3. **Discord**: Chat em tempo real
4. **Email**: suporte@culturabuilder.com

### O que incluir ao pedir ajuda?

1. Sistema operacional (Windows/Mac/Linux)
2. Versão do Python (`python3 --version`)
3. Mensagem de erro completa
4. O que você tentou fazer
5. Passos para reproduzir o problema

---

**Não encontrou sua pergunta?** Abra uma issue no GitHub!