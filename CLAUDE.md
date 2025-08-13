# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CulturaBuilder Framework Overview

CulturaBuilder is a comprehensive framework that extends Claude Code with specialized commands through the `/cb:` prefix. It integrates multiple development frameworks and tools into a unified command system for Claude Desktop and Claude Code CLI.

## Architecture

The framework follows a modular Python architecture with these core components:

- **Main Entry**: `CulturaBuilder/__main__.py` - Unified CLI entry point handling install/update/uninstall operations
- **Setup System**: `setup/` - Installation and configuration management
- **Command Definitions**: `CulturaBuilder/Commands/*.md` - Individual command specifications  
- **Core Framework**: `CulturaBuilder/Core/*.md` - Framework rules, principles, personas, and orchestration logic
- **Configuration**: `config/` - Requirements, features, and framework configuration

## Development Commands

### Build and Run
```bash
# Install the framework (Python 3.8+ required)
pip install culturabuilder
python3 -m culturabuilder install

# Run tests (if available in the future)
python3 -m pytest tests/

# Install in development mode
pip install -e .

# Build distribution
python3 -m build
```

### Installation Operations
```bash
# Quick installation with pre-selected components
python3 -m culturabuilder install --quick

# Minimal installation (core only)  
python3 -m culturabuilder install --minimal

# Developer profile installation
python3 -m culturabuilder install --profile developer

# Install specific components
python3 -m culturabuilder install --components core mcp commands

# Run system diagnostics
python3 -m culturabuilder install --diagnose

# Update existing installation
python3 -m culturabuilder update

# Uninstall framework
python3 -m culturabuilder uninstall
```

## Project Structure

```
CulturaBuilder/
├── CulturaBuilder/          # Main framework module
│   ├── __main__.py         # Entry point for python -m culturabuilder
│   ├── Core/               # Framework core files (COMMANDS.md, FLAGS.md, etc.)
│   ├── Commands/           # Command definitions (build.md, analyze.md, etc.)
│   └── Hooks/              # Hook system (placeholder for future)
├── setup/                  # Installation system
│   ├── base/              # Base installer classes
│   ├── components/        # Component installers (core.py, mcp.py, commands.py)
│   ├── core/              # Core setup utilities (registry.py, validator.py)
│   ├── managers/          # Configuration and metrics managers
│   ├── operations/        # Install/update/uninstall operations
│   └── utils/             # UI, logging, security utilities
├── config/                # Configuration files
│   ├── features.json      # Feature flags and capabilities
│   └── requirements.json  # System requirements
├── profiles/              # Installation profiles
│   ├── quick.json        # Quick installation profile
│   ├── minimal.json      # Minimal installation profile  
│   └── developer.json    # Developer profile
└── Docs/                 # Documentation in PT-BR and EN-US
```

## Key Components and Their Roles

### Installation System (`setup/`)

The installation system manages framework deployment to `~/.claude/`:

- **ComponentRegistry** (`setup/core/registry.py`): Discovers and manages installable components
- **Installer** (`setup/base/installer.py`): Handles file operations and backups
- **Validator** (`setup/core/validator.py`): Validates system requirements
- **ConfigManager** (`setup/managers/config_manager.py`): Manages configuration and profiles
- **MetricsManager** (`setup/managers/metrics_manager.py`): Tracks usage metrics

### Framework Core (`CulturaBuilder/Core/`)

The core framework files that guide Claude Code behavior:

- **COMMANDS.md**: All `/cb:` command definitions and usage
- **FLAGS.md**: Command flags for personas, MCP servers, and optimization
- **PERSONAS.md**: 11 specialized AI personas (architect, frontend, backend, etc.)
- **ORCHESTRATOR.md**: Intelligent routing and decision-making system
- **MCP.md**: Model Context Protocol server integrations
- **RULES.md**: Operational rules and guidelines
- **PRINCIPLES.md**: Development principles and philosophy
- **MODES.md**: Operational modes (task management, introspection, token efficiency)

### Command System (`CulturaBuilder/Commands/`)

Individual command specifications for:
- **Development**: build, implement, design, scaffold
- **Analysis**: analyze, troubleshoot, explain
- **Quality**: improve, test, cleanup
- **Documentation**: document, git
- **Management**: task, workflow, spawn

## Important Patterns

### Command Execution Flow
1. User types `/cb:command` in Claude Code
2. Framework detects command pattern and arguments
3. ORCHESTRATOR.md routes to appropriate persona and tools
4. Command handler executes with specified flags
5. Quality gates validate output
6. Result returned to user

### Installation Security
The installer validates that installation paths are within the user's home directory (see `setup/operations/install.py:422-429`). This prevents installation to system directories.

### Bilingual Support
All commands and documentation support both Portuguese (PT-BR) and English (EN-US). Default is PT-BR, use `--lang en-US` flag for English.

### Wave Orchestration
Complex operations automatically trigger "wave mode" for multi-stage execution when:
- Complexity ≥ 0.7
- Files > 20  
- Operation types > 2

## Testing Approach

Currently, the project uses manual testing. Future test implementation should:
1. Add pytest-based unit tests in `tests/`
2. Test component installation/uninstallation
3. Validate command parsing and execution
4. Test profile loading and validation
5. Verify metrics collection

## Configuration Files

- **pyproject.toml**: Modern Python project configuration (uses Hatch)
- **setup.py**: Legacy setup for compatibility
- **VERSION**: Single source of truth for version number
- **config/features.json**: Feature flags and capabilities
- **config/requirements.json**: System requirements per component

## Common Tasks

### Adding a New Command
1. Create command definition in `CulturaBuilder/Commands/[command].md`
2. Update `CulturaBuilder/Core/COMMANDS.md` with command reference
3. Add command handler in appropriate component
4. Update documentation

### Modifying Installation Logic
1. Edit relevant operation in `setup/operations/`
2. Update component in `setup/components/`
3. Test with `--dry-run` flag first
4. Run full installation test

### Updating Documentation
1. Documentation is bilingual - update both PT-BR and EN-US versions
2. Main docs in `Docs/` with English versions in `Docs/en-US/`
3. Keep README.md as primary user-facing documentation

## Error Handling

The framework uses comprehensive error handling:
- Component validation before installation
- Graceful fallback for missing dependencies
- Detailed logging to `~/.claude/logs/`
- User-friendly error messages with recovery suggestions

## Performance Considerations

- Installation typically completes in < 30 seconds
- Command response target: < 100ms
- Minimal dependencies (only setuptools required)
- Lazy loading of components when possible

## Security Notes

- Installation restricted to user home directory
- No automatic execution of external scripts
- Input validation on all command arguments
- Secure handling of configuration files