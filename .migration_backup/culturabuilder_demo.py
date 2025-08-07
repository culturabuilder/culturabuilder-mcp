#!/usr/bin/env python3
"""
CulturaBuilder Demo - Interface CLI Interativa
Demonstração do CulturaBuilder sem dependências externas
"""

import os
import sys
import time
import json
from pathlib import Path
from typing import Dict, List, Any

# Cores para terminal
class Colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class CulturaBuilderDemo:
    """Demo interativo do CulturaBuilder"""
    
    def __init__(self):
        self.language = "pt-BR"
        self.commands_history = []
        self.clear_screen()
        
        # Banco de comandos
        self.commands = {
            "/cb:build": {
                "pt-BR": {
                    "name": "construir",
                    "desc": "Constrói componentes do projeto",
                    "example": "/cb:build --component frontend"
                },
                "en-US": {
                    "name": "build",
                    "desc": "Builds project components",
                    "example": "/cb:build --component frontend"
                }
            },
            "/cb:analyze": {
                "pt-BR": {
                    "name": "analisar",
                    "desc": "Analisa código e arquitetura",
                    "example": "/cb:analyze --deep"
                },
                "en-US": {
                    "name": "analyze", 
                    "desc": "Analyzes code and architecture",
                    "example": "/cb:analyze --deep"
                }
            },
            "/cb:deploy": {
                "pt-BR": {
                    "name": "implantar",
                    "desc": "Implanta projeto em produção",
                    "example": "/cb:deploy --env staging"
                },
                "en-US": {
                    "name": "deploy",
                    "desc": "Deploys project to production",
                    "example": "/cb:deploy --env staging"
                }
            },
            "/cb:metrics": {
                "pt-BR": {
                    "name": "métricas",
                    "desc": "Visualiza métricas de uso",
                    "example": "/cb:metrics --summary"
                },
                "en-US": {
                    "name": "metrics",
                    "desc": "View usage metrics",
                    "example": "/cb:metrics --summary"
                }
            },
            "/cb:help": {
                "pt-BR": {
                    "name": "ajuda",
                    "desc": "Mostra ajuda e comandos",
                    "example": "/cb:help"
                },
                "en-US": {
                    "name": "help",
                    "desc": "Shows help and commands",
                    "example": "/cb:help"
                }
            }
        }
        
        self.translations = {
            "pt-BR": {
                "welcome": "Bem-vindo ao CulturaBuilder!",
                "tagline": "Construa cultura através de tecnologia",
                "choose_language": "Escolha seu idioma:",
                "available_commands": "Comandos disponíveis:",
                "type_command": "Digite um comando (ou 'sair' para terminar):",
                "executing": "Executando",
                "success": "Comando executado com sucesso!",
                "error": "Erro ao executar comando",
                "invalid_command": "Comando inválido. Digite /cb:help para ver comandos disponíveis.",
                "goodbye": "Obrigado por usar CulturaBuilder!",
                "command_history": "Histórico de comandos:",
                "example": "Exemplo",
                "description": "Descrição",
                "building": "Construindo componentes...",
                "analyzing": "Analisando projeto...",
                "deploying": "Implantando aplicação...",
                "showing_metrics": "Carregando métricas...",
                "tip": "Dica",
                "tips": [
                    "Use Tab para autocompletar comandos",
                    "Use setas ↑↓ para navegar no histórico",
                    "Digite '?' após um comando para ver ajuda detalhada"
                ]
            },
            "en-US": {
                "welcome": "Welcome to CulturaBuilder!",
                "tagline": "Build culture through technology",
                "choose_language": "Choose your language:",
                "available_commands": "Available commands:",
                "type_command": "Type a command (or 'exit' to quit):",
                "executing": "Executing",
                "success": "Command executed successfully!",
                "error": "Error executing command",
                "invalid_command": "Invalid command. Type /cb:help to see available commands.",
                "goodbye": "Thank you for using CulturaBuilder!",
                "command_history": "Command history:",
                "example": "Example",
                "description": "Description",
                "building": "Building components...",
                "analyzing": "Analyzing project...",
                "deploying": "Deploying application...",
                "showing_metrics": "Loading metrics...",
                "tip": "Tip",
                "tips": [
                    "Use Tab to autocomplete commands",
                    "Use arrows ↑↓ to navigate history",
                    "Type '?' after a command for detailed help"
                ]
            }
        }
    
    def clear_screen(self):
        """Limpa a tela"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self):
        """Imprime o cabeçalho"""
        self.clear_screen()
        print(f"{Colors.PURPLE}{Colors.BOLD}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                                                          ║")
        print("║            🌟  C U L T U R A B U I L D E R  🌟          ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
        print(f"{Colors.CYAN}{self.t('tagline')}{Colors.RESET}")
        print()
    
    def t(self, key: str) -> str:
        """Traduz uma chave"""
        return self.translations[self.language].get(key, key)
    
    def choose_language(self):
        """Permite escolher o idioma"""
        print(f"\n{Colors.YELLOW}{self.t('choose_language')}{Colors.RESET}")
        print("1. Português (Brasil)")
        print("2. English (US)")
        
        choice = input(f"\n{Colors.GREEN}> {Colors.RESET}")
        if choice == "2":
            self.language = "en-US"
        else:
            self.language = "pt-BR"
    
    def show_welcome(self):
        """Mostra mensagem de boas-vindas"""
        print(f"\n{Colors.GREEN}{Colors.BOLD}{self.t('welcome')}{Colors.RESET}")
        print("=" * 60)
    
    def show_commands(self):
        """Mostra comandos disponíveis"""
        print(f"\n{Colors.YELLOW}{self.t('available_commands')}{Colors.RESET}\n")
        
        for cmd, info in self.commands.items():
            cmd_info = info[self.language]
            print(f"  {Colors.CYAN}{cmd:<20}{Colors.RESET} - {cmd_info['desc']}")
            print(f"  {Colors.BLUE}  {self.t('example')}: {cmd_info['example']}{Colors.RESET}")
            print()
    
    def execute_command(self, command: str):
        """Executa um comando"""
        self.commands_history.append(command)
        
        # Parse do comando
        parts = command.strip().split()
        if not parts:
            return
        
        cmd = parts[0].lower()
        
        # Comandos especiais
        if cmd in ['sair', 'exit', 'quit']:
            return False
        
        if cmd in ['help', 'ajuda', '/cb:help']:
            self.show_commands()
            return True
        
        if cmd == 'history':
            self.show_history()
            return True
        
        if cmd == 'clear':
            self.print_header()
            return True
        
        if cmd == 'lang':
            self.choose_language()
            self.print_header()
            return True
        
        # Comandos CulturaBuilder
        if cmd.startswith('/cb:'):
            self.simulate_command_execution(cmd)
        else:
            print(f"{Colors.RED}{self.t('invalid_command')}{Colors.RESET}")
        
        return True
    
    def simulate_command_execution(self, command: str):
        """Simula a execução de um comando"""
        print(f"\n{Colors.YELLOW}{self.t('executing')} {command}...{Colors.RESET}")
        
        # Animação de progresso
        self.show_progress_bar()
        
        # Simula saída baseada no comando
        if '/cb:build' in command:
            print(f"\n{Colors.GREEN}{self.t('building')}{Colors.RESET}")
            print("  ✅ Frontend components")
            print("  ✅ Backend services")
            print("  ✅ Database migrations")
            print(f"\n{Colors.GREEN}{Colors.BOLD}{self.t('success')}{Colors.RESET}")
            
        elif '/cb:analyze' in command:
            print(f"\n{Colors.GREEN}{self.t('analyzing')}{Colors.RESET}")
            print("\n📊 Análise de Qualidade:")
            print("  • Cobertura de código: 85%")
            print("  • Complexidade: Baixa")
            print("  • Vulnerabilidades: 0")
            print("  • Performance: Ótima")
            print(f"\n{Colors.GREEN}{Colors.BOLD}{self.t('success')}{Colors.RESET}")
            
        elif '/cb:deploy' in command:
            print(f"\n{Colors.GREEN}{self.t('deploying')}{Colors.RESET}")
            print("  🚀 Building Docker image...")
            print("  📦 Pushing to registry...")
            print("  ⚡ Deploying to Kubernetes...")
            print("  ✅ Health checks passed")
            print(f"\n{Colors.GREEN}{Colors.BOLD}{self.t('success')}{Colors.RESET}")
            
        elif '/cb:metrics' in command:
            print(f"\n{Colors.GREEN}{self.t('showing_metrics')}{Colors.RESET}")
            print("\n📈 Métricas de Uso:")
            print("  • Comandos executados: 127")
            print("  • Taxa de sucesso: 98.4%")
            print("  • Tempo economizado: 4.5 horas")
            print("  • Projetos criados: 8")
            self.show_mini_chart()
            
        else:
            print(f"{Colors.GREEN}{Colors.BOLD}{self.t('success')}{Colors.RESET}")
    
    def show_progress_bar(self):
        """Mostra uma barra de progresso animada"""
        width = 40
        for i in range(width + 1):
            progress = i / width
            bar = '█' * i + '░' * (width - i)
            percentage = progress * 100
            print(f'\r  [{bar}] {percentage:.0f}%', end='', flush=True)
            time.sleep(0.02)
        print()
    
    def show_mini_chart(self):
        """Mostra um mini gráfico ASCII"""
        print("\n  Uso semanal:")
        print("  25 |     ██")
        print("  20 |   ████")
        print("  15 | ██████")
        print("  10 | ████████")
        print("   5 | ██████████")
        print("   0 └────────────")
        print("     Seg Ter Qua Qui Sex")
    
    def show_history(self):
        """Mostra histórico de comandos"""
        print(f"\n{Colors.YELLOW}{self.t('command_history')}{Colors.RESET}")
        for i, cmd in enumerate(self.commands_history[-10:], 1):
            print(f"  {i}. {cmd}")
    
    def show_random_tip(self):
        """Mostra uma dica aleatória"""
        import random
        tips = self.translations[self.language]["tips"]
        tip = random.choice(tips)
        print(f"\n{Colors.BLUE}💡 {self.t('tip')}: {tip}{Colors.RESET}")
    
    def run(self):
        """Loop principal"""
        self.print_header()
        self.choose_language()
        self.print_header()
        self.show_welcome()
        self.show_commands()
        
        while True:
            try:
                # Mostra dica aleatória ocasionalmente
                if len(self.commands_history) % 5 == 4:
                    self.show_random_tip()
                
                # Prompt
                print()
                command = input(f"{Colors.GREEN}cb> {Colors.RESET}")
                
                # Executa comando
                if not self.execute_command(command):
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n{Colors.YELLOW}{self.t('goodbye')}{Colors.RESET}")
                break
            except Exception as e:
                print(f"{Colors.RED}{self.t('error')}: {e}{Colors.RESET}")
        
        print(f"\n{Colors.PURPLE}✨ {self.t('goodbye')} ✨{Colors.RESET}\n")


def main():
    """Função principal"""
    demo = CulturaBuilderDemo()
    demo.run()


if __name__ == "__main__":
    main()