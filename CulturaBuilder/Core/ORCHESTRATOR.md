# ORCHESTRATOR.md - CulturaBuilder Intelligent Routing System

Intelligent routing system for 16 commands and 11 personas in CulturaBuilder framework.

## 🧠 Detection Engine

Analyzes requests to understand intent, complexity, and requirements.

### Pre-Operation Validation Checks

**Resource Validation**:
- Token usage prediction based on operation complexity and scope
- Memory and processing requirements estimation
- File system permissions and available space verification
- MCP server availability and response time checks

**Compatibility Validation**:
- Flag combination conflict detection (e.g., `--no-mcp` with `--seq`)
- Persona + command compatibility verification
- Tool availability for requested operations
- Project structure requirements validation

**Risk Assessment**:
- Operation complexity scoring (0.0-1.0 scale)
- Failure probability based on historical patterns
- Resource exhaustion likelihood prediction
- Cascading failure potential analysis

**Validation Logic**: Resource availability, flag compatibility, risk assessment, outcome prediction, and safety recommendations. Operations with risk scores >0.8 trigger safe mode suggestions.

**Resource Management Thresholds**:
- **Green Zone** (0-60%): Full operations, predictive monitoring active
- **Yellow Zone** (60-75%): Resource optimization, caching, suggest --uc mode
- **Orange Zone** (75-85%): Warning alerts, defer non-critical operations  
- **Red Zone** (85-95%): Force efficiency modes, block resource-intensive operations
- **Critical Zone** (95%+): Emergency protocols, essential operations only

### Pattern Recognition Rules

#### Complexity Detection
```yaml
simple:
  indicators:
    - single file operations
    - basic CRUD tasks
    - straightforward queries
    - < 3 step workflows
  token_budget: 5K
  time_estimate: < 5 min

moderate:
  indicators:
    - multi-file operations
    - analysis tasks
    - refactoring requests
    - 3-10 step workflows
  token_budget: 15K
  time_estimate: 5-30 min

complex:
  indicators:
    - system-wide changes
    - architectural decisions
    - performance optimization
    - > 10 step workflows
  token_budget: 30K+
  time_estimate: > 30 min
```

#### Domain Identification
```yaml
frontend:
  keywords: [UI, component, React, Vue, CSS, responsive, accessibility, implement component, build UI]
  file_patterns: ["*.jsx", "*.tsx", "*.vue", "*.css", "*.scss"]
  typical_operations: [create, implement, style, optimize, test]

backend:
  keywords: [API, database, server, endpoint, authentication, performance, implement API, build service]
  file_patterns: ["*.js", "*.ts", "*.py", "*.go", "controllers/*", "models/*"]
  typical_operations: [implement, optimize, secure, scale]

infrastructure:
  keywords: [deploy, Docker, CI/CD, monitoring, scaling, configuration]
  file_patterns: ["Dockerfile", "*.yml", "*.yaml", ".github/*", "terraform/*"]
  typical_operations: [setup, configure, automate, monitor]

security:
  keywords: [vulnerability, authentication, encryption, audit, compliance]
  file_patterns: ["*auth*", "*security*", "*.pem", "*.key"]
  typical_operations: [scan, harden, audit, fix]

documentation:
  keywords: [document, README, wiki, guide, manual, instructions, commit, release, changelog]
  file_patterns: ["*.md", "*.rst", "*.txt", "docs/*", "README*", "CHANGELOG*"]
  typical_operations: [write, document, explain, translate, localize]

iterative:
  keywords: [improve, refine, enhance, correct, polish, fix, iterate, loop, repeatedly]
  file_patterns: ["*.*"]  # Can apply to any file type
  typical_operations: [improve, refine, enhance, correct, polish, fix, iterate]

```

#### Operation Type Classification
```yaml
analysis:
  verbs: [analyze, review, explain, understand, investigate, troubleshoot]
  outputs: [insights, recommendations, reports]
  typical_tools: [Grep, Read, Sequential]

creation:
  verbs: [create, build, implement, generate, design]
  outputs: [new files, features, components]
  typical_tools: [Write, Magic, Context7]

implementation:
  verbs: [implement, develop, code, construct, realize]
  outputs: [working features, functional code, integrated components]
  typical_tools: [Write, Edit, MultiEdit, Magic, Context7, Sequential]

modification:
  verbs: [update, refactor, improve, optimize, fix]
  outputs: [edited files, improvements]
  typical_tools: [Edit, MultiEdit, Sequential]

debugging:
  verbs: [debug, fix, troubleshoot, resolve, investigate]
  outputs: [fixes, root causes, solutions]
  typical_tools: [Grep, Sequential, Playwright]

iterative:
  verbs: [improve, refine, enhance, correct, polish, fix, iterate, loop]
  outputs: [progressive improvements, refined results, enhanced quality]
  typical_tools: [Sequential, Read, Edit, MultiEdit, TodoWrite]

```

### Intent Extraction Algorithm
```
1. Parse user request for keywords and patterns
2. Match against domain/operation matrices
3. Score complexity based on scope and steps
4. Estimate resource requirements
5. Select appropriate persona and MCP servers
6. Apply token optimization if needed
7. Generate routing recommendation
```

## 🚦 Routing Intelligence

Dynamic decision trees that map detected patterns to optimal tool combinations, persona activation, and orchestration strategies.

### Command Routing Engine
Intelligent routing for 16 commands with persona and MCP server selection.

**Command Categories**:
- **Development (4)**: build, implement, design, test
- **Analysis (4)**: analyze, troubleshoot, explain, estimate
- **Quality (3)**: improve, cleanup, document
- **Management (3)**: task, git, spawn
- **Meta (2)**: index, load

### Master Routing Table

| Pattern | Complexity | Domain | Auto-Activates | Confidence |
|---------|------------|---------|----------------|------------|
| "analyze architecture" | complex | infrastructure | architect persona, --ultrathink, Sequential | 95% |
| "create component" | simple | frontend | frontend persona, Magic, --uc | 90% |
| "implement feature" | moderate | any | domain-specific persona, Context7, Sequential | 88% |
| "implement API" | moderate | backend | backend persona, --seq, Context7 | 92% |
| "implement UI component" | simple | frontend | frontend persona, Magic, --c7 | 94% |
| "implement authentication" | complex | security | security persona, backend persona, --validate | 90% |
| "fix bug" | moderate | any | analyzer persona, --think, Sequential | 85% |
| "optimize performance" | complex | backend | performance persona, --think-hard, Playwright | 90% |
| "security audit" | complex | security | security persona, --ultrathink, Sequential | 95% |
| "write documentation" | moderate | documentation | scribe persona, Context7 | 95% |
| "improve iteratively" | moderate | iterative | refactorer persona, --seq, --loop | 90% |
| "analyze large codebase" | complex | any | --delegate --parallel-dirs, analyzer persona | 95% |
| "comprehensive audit" | complex | multi | --delegate --parallel-focus, security persona | 95% |
| "improve large system" | complex | any | --delegate auto, architect persona | 90% |
| "security audit" | complex | security | security persona, --ultrathink | 95% |
| "modernize legacy system" | complex | legacy | architect persona, --delegate | 92% |
| "comprehensive code review" | complex | quality | qa persona, --think-hard | 94% |

### Decision Trees

#### Tool Selection Logic

**Base Tool Selection**:
- **Search**: Grep (specific patterns) or Agent (open-ended)
- **Understanding**: Sequential (complexity >0.7) or Read (simple)  
- **Documentation**: Context7
- **UI**: Magic
- **Testing**: Playwright

**Delegation Evaluation**:
- **Delegation Score >0.6**: Add Task tool, auto-enable delegation flags based on scope
- **Token Optimization >75%**: Enable --uc flag for compression

**Auto-Flag Assignment**:
- Directory count >7 → `--delegate --parallel-dirs`
- Focus areas >2 → `--multi-agent --parallel-focus`  
- High complexity + critical quality → `--wave-mode --wave-validation`
- Multiple operation types → `--wave-mode --adaptive-waves`

#### Task Delegation Intelligence

**Sub-Agent Delegation Decision Matrix**:

**Delegation Scoring Factors**:
- **Complexity >0.6**: +0.3 score
- **Parallelizable Operations**: +0.4 (scaled by opportunities/5, max 1.0)
- **High Token Requirements >15K**: +0.2 score  
- **Multi-domain Operations >2**: +0.1 per domain


**Strategy Recommendations**:
- **Directories >7**: `--delegate folders`
- **Files >50**: `--delegate files`
- **Focus Areas >2**: `--delegate auto`
- **High Complexity**: `--concurrency 7`
- **Default**: Single-agent execution

**Auto-Delegation Triggers**:
```yaml
directory_threshold:
  condition: directory_count > 7
  action: auto_enable --delegate --parallel-dirs
  confidence: 95%

file_threshold:
  condition: file_count > 50 AND complexity > 0.6
  action: auto_enable --delegate --sub-agents [calculated]
  confidence: 90%

multi_domain:
  condition: domains.length > 3
  action: auto_enable --delegate --parallel-focus
  confidence: 85%

complex_analysis:
  condition: complexity > 0.8 AND scope = comprehensive
  action: auto_enable --delegate --focus-agents
  confidence: 90%

token_optimization:
  condition: estimated_tokens > 20000
  action: auto_enable --delegate --aggregate-results
  confidence: 80%
```


**Delegation Routing Table**:

| Operation | Complexity | Auto-Delegates | Performance Gain |
|-----------|------------|----------------|------------------|
| `/cb:load @monorepo/` | moderate | --delegate folders | 65% |
| `/cb:analyze --comprehensive` | high | --delegate auto | 70% |
| Comprehensive system improvement | high | --delegate --concurrency 7 | 75% |
| Enterprise security audit | high | --delegate auto --ultrathink | 80% |
| Large-scale refactoring | high | --delegate files | 70% |

**Sub-Agent Specialization Matrix**:
- **Quality**: qa persona, complexity/maintainability focus, Read/Grep/Sequential tools
- **Security**: security persona, vulnerabilities/compliance focus, Grep/Sequential/Context7 tools
- **Performance**: performance persona, bottlenecks/optimization focus, Read/Sequential/Playwright tools
- **Architecture**: architect persona, patterns/structure focus, Read/Sequential/Context7 tools
- **API**: backend persona, endpoints/contracts focus, Grep/Context7/Sequential tools


#### Persona Auto-Activation System

**Multi-Factor Activation Scoring**:
- **Keyword Matching**: Base score from domain-specific terms (30%)
- **Context Analysis**: Project phase, urgency, complexity assessment (40%)
- **User History**: Past preferences and successful outcomes (20%)
- **Performance Metrics**: Current system state and bottlenecks (10%)

**Intelligent Activation Rules**:

**Performance Issues** → `--persona-performance` + `--focus performance`
- **Trigger Conditions**: Response time >500ms, error rate >1%, high resource usage
- **Confidence Threshold**: 85% for automatic activation

**Security Concerns** → `--persona-security` + `--focus security`
- **Trigger Conditions**: Vulnerability detection, auth failures, compliance gaps
- **Confidence Threshold**: 90% for automatic activation

**UI/UX Tasks** → `--persona-frontend` + `--magic`
- **Trigger Conditions**: Component creation, responsive design, accessibility
- **Confidence Threshold**: 80% for automatic activation

**Complex Debugging** → `--persona-analyzer` + `--think` + `--seq`
- **Trigger Conditions**: Multi-component failures, root cause investigation
- **Confidence Threshold**: 75% for automatic activation

**Documentation Tasks** → `--persona-scribe`
- **Trigger Conditions**: README, wiki, guides, commit messages, API docs
- **Confidence Threshold**: 70% for automatic activation

#### Flag Auto-Activation Patterns

**Context-Based Auto-Activation**:
- Performance issues → --persona-performance + --focus performance + --think
- Security concerns → --persona-security + --focus security + --validate
- UI/UX tasks → --persona-frontend + --magic + --c7
- Complex debugging → --think + --seq + --persona-analyzer
- Large codebase → --uc when context >75% + --delegate auto
- Testing operations → --persona-qa + --play + --validate
- Infrastructure operations → --persona-backend + --safe-mode + --validate
- Refactoring → --persona-refactorer + --validate
- Iterative improvement → --loop for polish, refine, enhance keywords

**Token Optimization Auto-Activation**:
- Context usage >75% → --uc flag enabled
- Large operations >50 files → --uc flag suggested
- Emergency mode >95% context → Ultra-compression forced

**Sub-Agent Auto-Activation**:
- File analysis → --delegate files when >50 files detected
- Directory analysis → --delegate folders when >7 directories detected
- Mixed scope → --delegate auto for complex project structures
- High concurrency → --concurrency auto-adjusted based on system resources

**Loop Auto-Activation**:
- Quality improvement → --loop for polish, refine, enhance, improve keywords
- Iterative requests → --loop when "iteratively", "step by step", "incrementally" detected
- Refinement operations → --loop for cleanup, fix, correct operations on existing code

#### Flag Precedence Rules
1. Safety flags (--safe-mode) > optimization flags
2. Explicit flags > auto-activation
3. Thinking depth: --ultrathink > --think-hard > --think
4. --no-mcp overrides all individual MCP flags
5. Scope: system > project > module > file
6. Last specified persona takes precedence
7. Sub-Agent delegation: explicit --delegate > auto-detection
8. Loop mode: explicit --loop > auto-detection based on refinement keywords
9. --uc auto-activation overrides verbose flags

### Confidence Scoring
Based on pattern match strength (40%), historical success rate (30%), context completeness (20%), resource availability (10%).

## Quality Gates & Validation Framework

### 8-Step Validation Cycle
```yaml
quality_gates:
  step_1_syntax: "language parsers, Context7 validation"
  step_2_type: "Sequential analysis, type compatibility"
  step_3_lint: "Context7 rules, quality analysis"
  step_4_security: "Sequential analysis, vulnerability assessment"
  step_5_test: "Playwright E2E, coverage analysis (≥80% unit, ≥70% integration)"
  step_6_performance: "Sequential analysis, benchmarking"
  step_7_documentation: "Context7 patterns, completeness validation"
  step_8_integration: "Playwright testing, deployment validation"

validation_automation:
  continuous_integration: "CI/CD pipeline integration, early failure detection"
  intelligent_monitoring: "success rate monitoring, adaptive validation"
  evidence_generation: "comprehensive evidence, validation metrics"
```

### Task Completion Criteria
```yaml
completion_requirements:
  validation: "all 8 steps pass, evidence provided, metrics documented"
  ai_integration: "MCP coordination, persona integration, tool orchestration, ≥90% context retention"
  performance: "response time targets, resource limits, success thresholds, token efficiency"
  quality: "code quality standards, security compliance, performance assessment, integration testing"

evidence_requirements:
  quantitative: "performance/quality/security metrics, coverage percentages, response times"
  qualitative: "code quality improvements, security enhancements, UX improvements"
  documentation: "change rationale, test results, performance benchmarks, security scans"
```

## ⚡ Performance Optimization

Resource management, operation batching, and intelligent optimization for sub-100ms performance targets.

**Token Management**: Intelligent resource allocation based on unified Resource Management Thresholds (see Detection Engine section)

**Operation Batching**:
- **Tool Coordination**: Parallel operations when no dependencies
- **Context Sharing**: Reuse analysis results across related routing decisions
- **Cache Strategy**: Store successful routing patterns for session reuse
- **Task Delegation**: Intelligent sub-agent spawning for parallel processing
- **Resource Distribution**: Dynamic token allocation across sub-agents

**Resource Allocation**:
- **Detection Engine**: 1-2K tokens for pattern analysis
- **Decision Trees**: 500-1K tokens for routing logic
- **MCP Coordination**: Variable based on servers activated


## 🔗 Integration Intelligence

Smart MCP server selection and orchestration.

### MCP Server Selection Matrix
**Reference**: See MCP.md for detailed server capabilities, workflows, and integration patterns.

**Quick Selection Guide**:
- **Context7**: Library docs, framework patterns
- **Sequential**: Complex analysis, multi-step reasoning
- **Magic**: UI components, design systems
- **Playwright**: E2E testing, performance metrics

### Intelligent Server Coordination
**Reference**: See MCP.md for complete server orchestration patterns and fallback strategies.

**Core Coordination Logic**: Multi-server operations, fallback chains, resource optimization

### Persona Integration
**Reference**: See PERSONAS.md for detailed persona specifications and MCP server preferences.

## 🚨 Emergency Protocols

Handling resource constraints and failures gracefully.

### Resource Management
Threshold-based resource management follows the unified Resource Management Thresholds (see Detection Engine section above).

### Graceful Degradation
- **Level 1**: Reduce verbosity, skip optional enhancements, use cached results
- **Level 2**: Disable advanced features, simplify operations, batch aggressively
- **Level 3**: Essential operations only, maximum compression, queue non-critical

### Error Recovery Patterns
- **MCP Timeout**: Use fallback server
- **Token Limit**: Activate compression
- **Tool Failure**: Try alternative tool
- **Parse Error**: Request clarification




## 🔧 Configuration

### Orchestrator Settings
```yaml
orchestrator_config:
  # Performance
  enable_caching: true
  cache_ttl: 3600
  parallel_operations: true
  max_parallel: 3
  
  # Intelligence
  learning_enabled: true
  confidence_threshold: 0.7
  pattern_detection: aggressive
  
  # Resource Management
  token_reserve: 10%
  emergency_threshold: 90%
  compression_threshold: 75%
  
  # Token Optimization
  token_optimization:
    enable_auto_compression: true
    compression_threshold: 0.75
    emergency_threshold: 0.95
    progressive_levels: 5
```

### Custom Routing Rules
Users can add custom routing patterns via YAML configuration files.
