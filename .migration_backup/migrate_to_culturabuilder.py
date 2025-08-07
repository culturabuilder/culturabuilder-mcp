#!/usr/bin/env python3
"""
Migração completa de SuperClaude para CulturaBuilder
Complete migration from SuperClaude to CulturaBuilder
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple
import argparse

class CulturaBuilderMigration:
    """Gerenciador de migração para CulturaBuilder"""
    
    def __init__(self, root_path: Path, dry_run: bool = False):
        self.root_path = root_path
        self.dry_run = dry_run
        self.changes_log = []
        self.backup_dir = root_path / ".migration_backup"
        
        # Mapeamento de substituições
        self.replacements = {
            # Nomes principais
            "SuperClaude": "CulturaBuilder",
            "superclaude": "culturabuilder",
            "SUPERCLAUDE": "CULTURABUILDER",
            
            # Prefixos de comando
            "/sc:": "/cb:",
            "sc:": "cb:",
            
            # URLs e emails
            "superclaude.dev": "culturabuilder.org",
            "contact@superclaude.dev": "contact@culturabuilder.org",
            "security@superclaude.dev": "security@culturabuilder.org",
            "conduct@superclaude.dev": "conduct@culturabuilder.org",
            
            # GitHub
            "superclaude-org": "culturabuilder-org",
            "SuperClaude_Framework": "CulturaBuilder_Framework",
            "SuperClaude_Website": "CulturaBuilder_Website",
        }
        
        # Arquivos para renomear
        self.files_to_rename = {
            "superclaude-user-guide.md": "culturabuilder-user-guide.md",
            ".superclaude-metadata.json": ".culturabuilder-metadata.json",
            ".superclaude-metrics.json": ".culturabuilder-metrics.json",
        }
        
        # Diretórios para renomear
        self.dirs_to_rename = {
            "SuperClaude": "CulturaBuilder",
        }
    
    def backup_project(self):
        """Cria backup completo antes da migração"""
        if not self.dry_run:
            print(f"📦 Criando backup em {self.backup_dir}...")
            if self.backup_dir.exists():
                shutil.rmtree(self.backup_dir)
            shutil.copytree(self.root_path, self.backup_dir, 
                          ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc', '.migration_backup'))
            print("✅ Backup criado com sucesso!")
    
    def migrate_file_content(self, file_path: Path) -> bool:
        """Migra conteúdo de um arquivo"""
        try:
            # Ignora arquivos binários e específicos
            if file_path.suffix in ['.pyc', '.pyo', '.pyd', '.so', '.dll', '.dylib', '.exe', '.png', '.jpg', '.jpeg', '.gif', '.ico']:
                return False
            
            # Ignora diretórios específicos
            if any(part in file_path.parts for part in ['.git', '__pycache__', 'node_modules', '.migration_backup']):
                return False
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_content = content
            
            # Aplica todas as substituições
            for old, new in self.replacements.items():
                if old in content:
                    content = content.replace(old, new)
                    self.changes_log.append(f"  ✏️  {file_path}: '{old}' → '{new}'")
            
            # Se houve mudanças, salva o arquivo
            if content != original_content:
                if not self.dry_run:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                return True
            
            return False
            
        except Exception as e:
            print(f"⚠️  Erro ao processar {file_path}: {e}")
            return False
    
    def rename_files_and_dirs(self):
        """Renomeia arquivos e diretórios"""
        print("\n📝 Renomeando arquivos e diretórios...")
        
        # Renomeia diretórios primeiro (de baixo para cima)
        for old_name, new_name in self.dirs_to_rename.items():
            for dir_path in sorted(self.root_path.rglob(old_name), reverse=True):
                if dir_path.is_dir():
                    new_path = dir_path.parent / new_name
                    if not self.dry_run:
                        dir_path.rename(new_path)
                    self.changes_log.append(f"  📁 {dir_path} → {new_path}")
                    print(f"  📁 Renomeado: {old_name} → {new_name}")
        
        # Renomeia arquivos
        for old_name, new_name in self.files_to_rename.items():
            for file_path in self.root_path.rglob(old_name):
                if file_path.is_file():
                    new_path = file_path.parent / new_name
                    if not self.dry_run:
                        file_path.rename(new_path)
                    self.changes_log.append(f"  📄 {file_path} → {new_path}")
                    print(f"  📄 Renomeado: {old_name} → {new_name}")
    
    def update_package_files(self):
        """Atualiza arquivos de configuração do pacote"""
        print("\n⚙️  Atualizando configurações do pacote...")
        
        # pyproject.toml
        pyproject_path = self.root_path / "pyproject.toml"
        if pyproject_path.exists():
            with open(pyproject_path, 'r') as f:
                content = f.read()
            
            # Atualizações específicas para pyproject.toml
            content = re.sub(r'name = "superclaude"', 'name = "culturabuilder"', content)
            content = re.sub(r'SuperClaude', 'CulturaBuilder', content)
            content = re.sub(r'superclaude', 'culturabuilder', content)
            
            # Atualiza scripts
            content = content.replace('[project.scripts]', '[project.scripts]')
            content = content.replace('SuperClaude = "CulturaBuilder.__main__:main"', 
                                    'CulturaBuilder = "CulturaBuilder.__main__:main"')
            content = content.replace('superclaude = "CulturaBuilder.__main__:main"',
                                    'culturabuilder = "CulturaBuilder.__main__:main"')
            
            if not self.dry_run:
                with open(pyproject_path, 'w') as f:
                    f.write(content)
            
            print("  ✅ pyproject.toml atualizado")
    
    def create_bilingual_structure(self):
        """Cria estrutura bilíngue para documentação"""
        print("\n🌐 Criando estrutura bilíngue...")
        
        docs_path = self.root_path / "CulturaBuilder" / "Docs"
        if not docs_path.exists():
            docs_path = self.root_path / "Docs"
        
        # Cria diretórios para idiomas
        pt_br_path = docs_path / "pt-BR"
        en_us_path = docs_path / "en-US"
        
        if not self.dry_run:
            pt_br_path.mkdir(parents=True, exist_ok=True)
            en_us_path.mkdir(parents=True, exist_ok=True)
            
            # Copia documentação existente para en-US
            for doc_file in docs_path.glob("*.md"):
                if doc_file.is_file():
                    shutil.copy2(doc_file, en_us_path / doc_file.name)
            
            print(f"  ✅ Estrutura bilíngue criada em {docs_path}")
    
    def update_command_prefixes(self):
        """Atualiza prefixos de comando em todos os arquivos .md"""
        print("\n🔧 Atualizando prefixos de comando...")
        
        commands_path = self.root_path / "CulturaBuilder" / "Commands"
        if not commands_path.exists():
            commands_path = self.root_path / "SuperClaude" / "Commands"
        
        if commands_path.exists():
            for cmd_file in commands_path.glob("*.md"):
                self.migrate_file_content(cmd_file)
                print(f"  ✅ {cmd_file.name}: /sc: → /cb:")
    
    def create_migration_report(self):
        """Cria relatório de migração"""
        report_path = self.root_path / "MIGRATION_REPORT.md"
        
        report = f"""# Relatório de Migração CulturaBuilder
# CulturaBuilder Migration Report

## 📊 Resumo / Summary

- **Total de arquivos processados / Total files processed**: {len(self.changes_log)}
- **Modo / Mode**: {'Dry Run (simulação)' if self.dry_run else 'Execução real / Real execution'}
- **Backup criado em / Backup created at**: {self.backup_dir if not self.dry_run else 'N/A'}

## 📝 Mudanças Realizadas / Changes Made

### Substituições de Texto / Text Replacements
{chr(10).join(self.changes_log[:50])}
{'... e mais ' + str(len(self.changes_log) - 50) + ' mudanças' if len(self.changes_log) > 50 else ''}

## ✅ Próximos Passos / Next Steps

1. **Testar a instalação / Test installation**:
   ```bash
   pip install -e .
   culturabuilder --version
   ```

2. **Verificar comandos / Verify commands**:
   ```bash
   culturabuilder --help
   culturabuilder metrics --status
   ```

3. **Atualizar repositório Git / Update Git repository**:
   ```bash
   git remote set-url origin https://github.com/culturabuilder-org/CulturaBuilder_Framework.git
   ```

## 🔄 Reverter Mudanças / Revert Changes

Se necessário, restaure o backup / If needed, restore from backup:
```bash
rm -rf {self.root_path}
mv {self.backup_dir} {self.root_path}
```

---
*Migração concluída com sucesso! / Migration completed successfully!*
*Bem-vindo ao CulturaBuilder! / Welcome to CulturaBuilder!*
"""
        
        if not self.dry_run:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
        
        print(f"\n📄 Relatório salvo em: {report_path}")
    
    def run(self):
        """Executa a migração completa"""
        print("🚀 Iniciando migração SuperClaude → CulturaBuilder")
        print(f"📁 Diretório: {self.root_path}")
        print(f"🔍 Modo: {'Dry Run (simulação)' if self.dry_run else 'Execução real'}")
        
        if not self.dry_run:
            # Faz backup antes de começar
            self.backup_project()
        
        # 1. Renomeia arquivos e diretórios
        self.rename_files_and_dirs()
        
        # 2. Atualiza conteúdo dos arquivos
        print("\n📝 Migrando conteúdo dos arquivos...")
        file_count = 0
        for file_path in self.root_path.rglob("*"):
            if file_path.is_file():
                if self.migrate_file_content(file_path):
                    file_count += 1
        
        print(f"  ✅ {file_count} arquivos migrados")
        
        # 3. Atualiza arquivos de configuração
        self.update_package_files()
        
        # 4. Atualiza prefixos de comando
        self.update_command_prefixes()
        
        # 5. Cria estrutura bilíngue
        self.create_bilingual_structure()
        
        # 6. Cria relatório
        self.create_migration_report()
        
        print("\n✨ Migração concluída com sucesso!")
        print("🎉 Bem-vindo ao CulturaBuilder!")
        
        if self.dry_run:
            print("\n⚠️  Este foi um dry run. Para executar a migração real, rode sem --dry-run")


def main():
    parser = argparse.ArgumentParser(
        description="Migra SuperClaude para CulturaBuilder"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula a migração sem fazer mudanças reais"
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path.cwd(),
        help="Caminho do projeto (padrão: diretório atual)"
    )
    
    args = parser.parse_args()
    
    # Executa migração
    migrator = CulturaBuilderMigration(args.path, args.dry_run)
    migrator.run()


if __name__ == "__main__":
    main()