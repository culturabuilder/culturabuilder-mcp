# COMMANDS.md - CulturaBuilder Command System

CulturaBuilder command system for Claude Code - 16 unified commands with intelligent routing.

## Command System Architecture

### Core Command Structure
```yaml
---
command: "/cb:{command-name}"
category: "Primary classification"
purpose: "Operational objective"
wave-enabled: true|false
performance-profile: "optimization|standard|complex"
---
```

### Command Processing Pipeline
1. **Input Parsing**: `$ARGUMENTS` with `@<path>`, `!<command>`, `--<flags>`
2. **Context Resolution**: Auto-persona activation and MCP server selection
3. **Wave Eligibility**: Complexity assessment and wave mode determination
4. **Execution Strategy**: Tool orchestration and resource allocation
5. **Quality Gates**: Validation checkpoints and error handling

### Integration Layers
- **Claude Code**: Native slash command compatibility
- **Persona System**: Auto-activation based on command context
- **MCP Servers**: Context7, Sequential, Magic, Playwright integration
- **Wave System**: Multi-stage orchestration for complex operations

## Command Categories

**Development** (4): build, implement, design, test
**Analysis** (4): analyze, troubleshoot, explain, estimate
**Quality** (3): improve, cleanup, document
**Management** (3): task, git, spawn
**Meta** (2): index, load

### Development Commands

**`/cb:build [target] [flags]`**
- **Purpose**: Compile and bundle projects with framework detection
- **Auto-Persona**: Frontend, Backend, Architect
- **MCP**: Magic (UI), Context7 (patterns), Sequential (complex)
- **Tools**: Read, Grep, Glob, Bash, TodoWrite, Edit

**`/cb:implement [feature] [flags]`**
- **Purpose**: Feature implementation with intelligent guidance
- **Auto-Persona**: Frontend, Backend, Architect, Security
- **MCP**: Magic (UI), Context7 (patterns), Sequential (logic)
- **Tools**: Read, Write, Edit, MultiEdit, Bash, TodoWrite


**`/cb:design [system] [flags]`**
- **Purpose**: System design and architecture planning
- **Auto-Persona**: Architect, Frontend, Backend
- **MCP**: Sequential (planning), Context7 (patterns), Magic (UI)
- **Tools**: Write, Read, TodoWrite

**`/cb:test [type] [flags]`**
- **Purpose**: Testing workflows and validation
- **Auto-Persona**: QA, Backend, Frontend
- **MCP**: Playwright (E2E), Sequential (planning)
- **Tools**: Bash, Read, Write, TodoWrite

### Analysis Commands

**`/cb:analyze [target] [flags]`**
- **Purpose**: Multi-dimensional code and system analysis
- **Auto-Persona**: Analyzer, Architect, Security
- **MCP**: Sequential (primary), Context7 (patterns)
- **Tools**: Read, Grep, Glob, Bash, TodoWrite

**`/cb:troubleshoot [issue] [flags]`**
- **Purpose**: Debug and resolve problems
- **Auto-Persona**: Analyzer, QA
- **MCP**: Sequential, Playwright
- **Tools**: Read, Grep, Bash, TodoWrite

**`/cb:explain [topic] [flags]`**
- **Purpose**: Technical explanations and documentation
- **Auto-Persona**: Scribe, Analyzer
- **MCP**: Context7, Sequential
- **Tools**: Read, Write, TodoWrite

**`/cb:estimate [task] [flags]`**
- **Purpose**: Time and complexity estimation
- **Auto-Persona**: Architect, Analyzer
- **MCP**: Sequential, Context7
- **Tools**: Read, Grep, TodoWrite


### Quality Commands

**`/cb:improve [target] [flags]`**
- **Purpose**: Code enhancement and optimization
- **Auto-Persona**: Refactorer, Performance, Architect
- **MCP**: Sequential, Context7, Magic (UI)
- **Tools**: Read, Edit, MultiEdit, Bash

**`/cb:cleanup [target] [flags]`**
- **Purpose**: Technical debt reduction
- **Auto-Persona**: Refactorer
- **MCP**: Sequential
- **Tools**: Read, Edit, MultiEdit, Bash

**`/cb:document [target] [flags]`**
- **Purpose**: Documentation generation
- **Auto-Persona**: Scribe
- **MCP**: Context7, Sequential
- **Tools**: Read, Write, TodoWrite

### Management Commands

**`/cb:task [operation] [flags]`**
- **Purpose**: Project and task management
- **Auto-Persona**: Architect, Analyzer
- **MCP**: Sequential
- **Tools**: TodoWrite, Read, Write

**`/cb:git [operation] [flags]`**
- **Purpose**: Version control operations
- **Auto-Persona**: Backend, Scribe
- **MCP**: Sequential
- **Tools**: Bash, Read, Write

**`/cb:spawn [mode] [flags]`**
- **Purpose**: Multi-agent task orchestration
- **Auto-Persona**: Architect, Analyzer
- **MCP**: All servers
- **Tools**: Task, TodoWrite

### Meta Commands

**`/cb:index [query] [flags]`**
- **Purpose**: Command discovery and help
- **Auto-Persona**: Scribe, Analyzer
- **MCP**: Sequential
- **Tools**: Read, TodoWrite

**`/cb:load [path] [flags]`**
- **Purpose**: Project context loading
- **Auto-Persona**: Analyzer, Architect
- **MCP**: All servers
- **Tools**: Read, Grep, TodoWrite

## Command Summary

### Total Commands: 16

**Development (4)**: build, implement, design, test
**Analysis (4)**: analyze, troubleshoot, explain, estimate
**Quality (3)**: improve, cleanup, document
**Management (3)**: task, git, spawn
**Meta (2)**: index, load

### MCP Server Integration
- **Context7**: Documentation and patterns
- **Sequential**: Complex analysis and reasoning
- **Magic**: UI component generation
- **Playwright**: Testing and browser automation

### Persona System (9)
- **Technical**: architect, frontend, backend
- **Quality**: analyzer, qa, refactorer
- **Specialized**: security, performance, scribe

