import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// Definição dos comandos CulturaBuilder
const CULTURABUILDER_COMMANDS: Record<string, {
  description: string;
  args: string[];
  examples: string[];
}> = {
  "/cb:build": {
    description: "🔨 Constrói componentes do projeto com detecção automática de framework",
    args: ["target", "--optimize", "--clean", "--type"],
    examples: ["/cb:build frontend", "/cb:build --all --optimize"]
  },
  "/cb:analyze": {
    description: "🔍 Analisa código e arquitetura com foco em qualidade e segurança",
    args: ["scope", "--deep", "--focus", "--report"],
    examples: ["/cb:analyze --deep", "/cb:analyze --focus security"]
  },
  "/cb:deploy": {
    description: "🚀 Implanta projeto em produção com rollback automático",
    args: ["--env", "--rollback-on-error", "--dry-run"],
    examples: ["/cb:deploy --env staging", "/cb:deploy --env prod --rollback-on-error"]
  },
  "/cb:improve": {
    description: "✨ Melhora código baseado em análise e melhores práticas",
    args: ["target", "--quality", "--performance", "--security"],
    examples: ["/cb:improve --quality", "/cb:improve --performance --focus critical"]
  },
  "/cb:metrics": {
    description: "📊 Visualiza métricas de uso e performance do projeto",
    args: ["--summary", "--export", "--period"],
    examples: ["/cb:metrics --summary", "/cb:metrics --export html"]
  },
  "/cb:test": {
    description: "🧪 Executa testes com cobertura e relatórios detalhados",
    args: ["type", "--coverage", "--watch", "--parallel"],
    examples: ["/cb:test unit", "/cb:test --all --coverage"]
  },
  "/cb:document": {
    description: "📝 Gera documentação bilíngue (PT-BR/EN-US) do projeto",
    args: ["type", "--lang", "--format", "--include-examples"],
    examples: ["/cb:document --lang pt-BR", "/cb:document api --format markdown"]
  },
  "/cb:workflow": {
    description: "⚡ Cria e gerencia workflows complexos de desenvolvimento",
    args: ["action", "name", "--steps", "--automate"],
    examples: ["/cb:workflow create ci-cd", "/cb:workflow run daily-tasks"]
  },
  "/cb:ai": {
    description: "🤖 Assistente IA para sugestões e otimizações de código",
    args: ["query", "--context", "--suggest", "--explain"],
    examples: ["/cb:ai 'como otimizar este código?'", "/cb:ai suggest --context current-file"]
  },
  "/cb:learn": {
    description: "📚 Sistema de aprendizado interativo com tutoriais progressivos",
    args: ["topic", "--level", "--interactive", "--lang"],
    examples: ["/cb:learn basics", "/cb:learn advanced --topic testing"]
  },
  "/cb:git": {
    description: "📦 Gerenciamento Git com mensagens bilíngues e changelog automático",
    args: ["action", "--message", "--auto-changelog", "--semantic"],
    examples: ["/cb:git commit --message 'feat: novo componente'", "/cb:git release --semantic"]
  },
  "/cb:scaffold": {
    description: "🏗️ Cria estrutura de projetos com templates modernos",
    args: ["type", "name", "--template", "--with-tests"],
    examples: ["/cb:scaffold component Button", "/cb:scaffold api users --with-tests"]
  },
  "/cb:refactor": {
    description: "♻️ Refatora código mantendo funcionalidade e melhorando qualidade",
    args: ["target", "--pattern", "--safe-mode", "--preview"],
    examples: ["/cb:refactor --pattern solid", "/cb:refactor legacy --safe-mode"]
  },
  "/cb:security": {
    description: "🔒 Auditoria de segurança e correção de vulnerabilidades",
    args: ["--scan", "--fix", "--report", "--compliance"],
    examples: ["/cb:security --scan", "/cb:security --fix --report"]
  },
  "/cb:performance": {
    description: "⚡ Otimização de performance com métricas detalhadas",
    args: ["target", "--profile", "--optimize", "--benchmark"],
    examples: ["/cb:performance --profile", "/cb:performance --optimize bundle-size"]
  },
  "/cb:config": {
    description: "⚙️ Configuração do CulturaBuilder e personalização",
    args: ["action", "key", "value", "--global", "--reset"],
    examples: ["/cb:config set language pt-BR", "/cb:config set theme dark"]
  },
  "/cb:help": {
    description: "❓ Ajuda e documentação dos comandos CulturaBuilder",
    args: ["command", "--lang", "--examples"],
    examples: ["/cb:help", "/cb:help build --examples"]
  }
};

// Create server instance
const server = new Server(
  {
    name: "culturabuilder",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Handler for listing tools (commands)
server.setRequestHandler(ListToolsRequestSchema, async () => {
  const tools = Object.entries(CULTURABUILDER_COMMANDS).map(([command, info]) => ({
    name: command,
    description: info.description,
    inputSchema: {
      type: "object",
      properties: {
        args: {
          type: "array",
          items: { type: "string" },
          description: `Arguments: ${info.args.join(", ")}`
        }
      }
    }
  }));
  
  return { tools };
});

// Handler for executing tools (commands)
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  
  if (!(name in CULTURABUILDER_COMMANDS)) {
    throw new Error(`Comando não encontrado: ${name}`);
  }
  
  // Simulate command execution
  const commandInfo = CULTURABUILDER_COMMANDS[name as keyof typeof CULTURABUILDER_COMMANDS];
  
  // Return bilingual response
  const response = {
    content: [
      {
        type: "text",
        text: `🌟 Executando ${name}\n\n${commandInfo.description}\n\nExemplos:\n${commandInfo.examples.join("\n")}`
      }
    ]
  };
  
  return response;
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("🌟 CulturaBuilder MCP Server iniciado com sucesso!");
}

main().catch((error) => {
  console.error("Erro ao iniciar servidor:", error);
  process.exit(1);
});
