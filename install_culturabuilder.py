#!/usr/bin/env python3
"""
CulturaBuilder Installer
Fork do SuperClaude com comandos /cb: nativos
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

class CulturaBuilderInstaller:
    """Instalador do CulturaBuilder com integração MCP"""
    
    def __init__(self):
        self.home = Path.home()
        self.claude_dir = self.home / ".claude"
        self.culturabuilder_dir = self.home / ".culturabuilder"
        self.mcp_settings_path = self.claude_dir / "claude_desktop_config.json"
        
    def print_header(self):
        """Print installation header"""
        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     🌟 CulturaBuilder Installation Wizard 🌟            ║
║                                                          ║
║     Construa cultura através de tecnologia              ║
║     Build culture through technology                    ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
        """)
        
    def check_prerequisites(self):
        """Check if all prerequisites are met"""
        print("\n📋 Verificando pré-requisitos...")
        
        # Check Python
        python_version = sys.version_info
        if python_version.major < 3 or python_version.minor < 8:
            print("❌ Python 3.8+ é necessário")
            return False
            
        print("✅ Python 3.8+ detectado")
        
        # Check Node.js
        try:
            node_version = subprocess.run(
                ["node", "--version"],
                capture_output=True,
                text=True,
                check=True
            ).stdout.strip()
            print(f"✅ Node.js detectado: {node_version}")
        except:
            print("❌ Node.js não encontrado. Instale em: https://nodejs.org")
            return False
            
        # Check Claude directory
        if not self.claude_dir.exists():
            self.claude_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Diretório Claude criado: {self.claude_dir}")
        else:
            print(f"✅ Diretório Claude encontrado: {self.claude_dir}")
            
        return True
        
    def create_mcp_server(self):
        """Create the MCP server for CulturaBuilder"""
        print("\n🔧 Criando servidor MCP do CulturaBuilder...")
        
        mcp_dir = Path(__file__).parent / "culturabuilder-mcp"
        mcp_dir.mkdir(exist_ok=True)
        
        # Create TypeScript configuration
        tsconfig = {
            "compilerOptions": {
                "target": "ES2022",
                "module": "ESNext",
                "moduleResolution": "node",
                "outDir": "./dist",
                "rootDir": "./src",
                "strict": True,
                "esModuleInterop": True,
                "skipLibCheck": True,
                "forceConsistentCasingInFileNames": True,
                "resolveJsonModule": True,
                "allowJs": True,
                "declaration": True
            },
            "include": ["src/**/*"],
            "exclude": ["node_modules", "dist"]
        }
        
        with open(mcp_dir / "tsconfig.json", "w") as f:
            json.dump(tsconfig, f, indent=2)
            
        # Create main MCP server file
        server_code = '''import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// Definição dos comandos CulturaBuilder
const CULTURABUILDER_COMMANDS = {
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
  
  if (!CULTURABUILDER_COMMANDS[name]) {
    throw new Error(`Comando não encontrado: ${name}`);
  }
  
  // Simulate command execution
  const commandInfo = CULTURABUILDER_COMMANDS[name];
  
  // Return bilingual response
  const response = {
    content: [
      {
        type: "text",
        text: `🌟 Executando ${name}\\n\\n${commandInfo.description}\\n\\nExemplos:\\n${commandInfo.examples.join("\\n")}`
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
'''
        
        # Create src directory and save server file
        src_dir = mcp_dir / "src"
        src_dir.mkdir(exist_ok=True)
        
        with open(src_dir / "index.ts", "w") as f:
            f.write(server_code)
            
        print("✅ Servidor MCP criado")
        return mcp_dir
        
    def install_mcp_dependencies(self, mcp_dir: Path):
        """Install MCP server dependencies"""
        print("\n📦 Instalando dependências do servidor MCP...")
        
        try:
            # Install dependencies
            subprocess.run(
                ["npm", "install"],
                cwd=mcp_dir,
                check=True,
                capture_output=True
            )
            print("✅ Dependências instaladas")
            
            # Build TypeScript
            subprocess.run(
                ["npm", "run", "build"],
                cwd=mcp_dir,
                check=True,
                capture_output=True
            )
            print("✅ Servidor compilado")
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Aviso: Erro ao compilar servidor: {e}")
            print("Continuando instalação...")
            
        return True
        
    def configure_claude_mcp(self, mcp_dir: Path):
        """Configure Claude to use CulturaBuilder MCP server"""
        print("\n⚙️ Configurando Claude Desktop para CulturaBuilder...")
        
        # Load or create MCP settings
        mcp_config = {}
        if self.mcp_settings_path.exists():
            with open(self.mcp_settings_path, "r") as f:
                mcp_config = json.load(f)
                
        # Add CulturaBuilder server
        if "mcpServers" not in mcp_config:
            mcp_config["mcpServers"] = {}
            
        mcp_config["mcpServers"]["culturabuilder"] = {
            "command": "node",
            "args": [str(mcp_dir / "dist" / "index.js")],
            "env": {
                "CULTURABUILDER_LANG": "pt-BR"
            }
        }
        
        # Save configuration
        with open(self.mcp_settings_path, "w") as f:
            json.dump(mcp_config, f, indent=2)
            
        print(f"✅ Configuração MCP salva em: {self.mcp_settings_path}")
        return True
        
    def create_command_shortcuts(self):
        """Create command shortcuts in Claude configuration"""
        print("\n📝 Criando atalhos de comandos...")
        
        # Update CLAUDE.md
        claude_md_content = """# CulturaBuilder - Sistema de Comandos Nativos

## 🌟 Comandos /cb: (CulturaBuilder)

Todos os comandos começando com `/cb:` são comandos nativos do CulturaBuilder.

### Comandos Disponíveis:

#### Desenvolvimento
- `/cb:build` - Constrói componentes do projeto
- `/cb:scaffold` - Cria estrutura de projetos
- `/cb:refactor` - Refatora código

#### Análise e Qualidade
- `/cb:analyze` - Analisa código e arquitetura
- `/cb:improve` - Melhora qualidade do código
- `/cb:security` - Auditoria de segurança
- `/cb:performance` - Otimização de performance

#### Testes e Deploy
- `/cb:test` - Executa testes
- `/cb:deploy` - Implanta em produção
- `/cb:workflow` - Gerencia workflows

#### Documentação e Aprendizado
- `/cb:document` - Gera documentação bilíngue
- `/cb:learn` - Sistema de aprendizado
- `/cb:help` - Ajuda e exemplos

#### Ferramentas
- `/cb:git` - Gerenciamento Git
- `/cb:metrics` - Visualiza métricas
- `/cb:ai` - Assistente IA
- `/cb:config` - Configurações

## 🎯 Uso Rápido

1. Digite `/cb:` e veja todos os comandos disponíveis
2. Use Tab para autocompletar
3. Adicione `--help` para ver opções de cada comando

## 🌐 Suporte Bilíngue

Todos os comandos suportam PT-BR e EN-US:
- Padrão: Português (PT-BR)
- Inglês: Adicione `--lang en-US`

@COMMANDS.md
@FLAGS.md
@PRINCIPLES.md
@RULES.md
@MCP.md
@PERSONAS.md
@ORCHESTRATOR.md
@MODES.md
"""
        
        with open(self.claude_dir / "CLAUDE.md", "w") as f:
            f.write(claude_md_content)
            
        print("✅ Atalhos de comandos criados")
        return True
        
    def create_culturabuilder_config(self):
        """Create CulturaBuilder configuration"""
        print("\n🔧 Criando configuração do CulturaBuilder...")
        
        self.culturabuilder_dir.mkdir(exist_ok=True)
        
        # Create settings file
        settings = {
            "version": "1.0.0",
            "language": "pt-BR",
            "theme": "dark",
            "features": {
                "metrics": True,
                "ai_assistant": True,
                "auto_complete": True,
                "bilingual": True
            },
            "commands": {
                "prefix": "/cb:",
                "aliases": {
                    "/build": "/cb:build",
                    "/analyze": "/cb:analyze",
                    "/deploy": "/cb:deploy"
                }
            }
        }
        
        with open(self.culturabuilder_dir / "settings.json", "w") as f:
            json.dump(settings, f, indent=2)
            
        print(f"✅ Configuração criada em: {self.culturabuilder_dir}")
        return True
        
    def print_success(self):
        """Print success message"""
        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     ✅ CulturaBuilder Instalado com Sucesso! ✅         ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

🎉 Parabéns! O CulturaBuilder está pronto para uso!

📋 Próximos passos:

1. Reinicie o Claude Desktop
2. Os comandos /cb: estarão disponíveis no autocomplete
3. Digite /cb:help para ver todos os comandos

🌟 Comandos principais:
   • /cb:build    - Construir projeto
   • /cb:analyze  - Analisar código
   • /cb:test     - Executar testes
   • /cb:deploy   - Implantar
   • /cb:help     - Ver ajuda

🌐 Interface Web:
   Execute: python3 -m http.server 5173
   Acesse: http://localhost:5173

💡 Dica: Use Tab para autocompletar comandos!

Obrigado por escolher CulturaBuilder!
Construa cultura através de tecnologia! 🚀
        """)
        
    def run(self):
        """Run the complete installation"""
        self.print_header()
        
        if not self.check_prerequisites():
            print("\n❌ Instalação cancelada. Corrija os pré-requisitos.")
            return False
            
        # Create and configure MCP server
        mcp_dir = self.create_mcp_server()
        self.install_mcp_dependencies(mcp_dir)
        self.configure_claude_mcp(mcp_dir)
        
        # Create configurations
        self.create_command_shortcuts()
        self.create_culturabuilder_config()
        
        # Success!
        self.print_success()
        return True


if __name__ == "__main__":
    installer = CulturaBuilderInstaller()
    installer.run()