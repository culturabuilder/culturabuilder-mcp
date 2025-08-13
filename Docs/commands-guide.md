# CulturaBuilder Commands Guide 🛠️

## 💡 Don't Overthink It - CulturaBuilder Tries to Help

**The truth about these 17 commands**: You don't need to memorize them. Just start with `/cb:analyze` or `/cb:implement` and see what happens! 

**Here's how it usually works:**
- Type `/` in Claude Code → See available commands
- Use basic ones like `/cb:analyze`, `/cb:build`, `/cb:improve` 
- **CulturaBuilder tries to pick helpful tools and experts** for each situation
- More commands become useful as you get comfortable

**Auto-activation is pretty neat** 🪄 - CulturaBuilder attempts to detect what you're trying to do and activate relevant specialists (security expert, performance optimizer, etc.) without you managing it. Usually works well! 😊

---

## Quick "Just Try These" List 🚀

**Start here** (no reading required):
```bash
/cb:index                    # See what's available
/cb:analyze src/            # Tries to analyze your code smartly 
/cb:workflow feature-100-prd.md  # Creates step-by-step implementation workflow from PRD
/cb:implement user-auth     # Creates features and components (replaces v2 /build)
/cb:build                   # Attempts intelligent project building
/cb:improve messy-file.js   # Tries to clean up code 
/cb:troubleshoot "error"    # Attempts to help with problems
```

**That's honestly enough to get started.** Everything else below is here when you get curious about what other tools are available. 🛠️

---

A practical guide to all 16 CulturaBuilder slash commands. We'll be honest about what works well and what's still rough around the edges.

## Quick Reference 📋

*(You really don't need to memorize this - just pick what sounds useful)*

| Command | Purpose | Auto-Activates | Best For |
|---------|---------|-----------------|----------|
| `/cb:analyze` | Smart code analysis | Security/performance experts | Finding issues, understanding codebases |
| `/cb:build` | Intelligent building | Frontend/backend specialists | Compilation, bundling, deployment prep |
| `/cb:implement` | Feature implementation | Domain-specific experts | Creating features, components, APIs, services |
| `/cb:improve` | Automatic code cleanup | Quality experts | Refactoring, optimization, quality fixes |
| `/cb:troubleshoot` | Problem investigation | Debug specialists | Debugging, issue investigation |
| `/cb:test` | Smart testing | QA experts | Running tests, coverage analysis |
| `/cb:document` | Auto documentation | Writing specialists | README files, code comments, guides |
| `/cb:git` | Enhanced git workflows | DevOps specialists | Smart commits, branch management |
| `/cb:design` | System design help | Architecture experts | Architecture planning, API design |
| `/cb:explain` | Learning assistant | Teaching specialists | Learning concepts, understanding code |
| `/cb:cleanup` | Debt reduction | Refactoring experts | Removing dead code, organizing files |
| `/cb:load` | Context understanding | Analysis experts | Project analysis, codebase understanding |
| `/cb:estimate` | Smart estimation | Planning experts | Time/effort planning, complexity analysis |
| `/cb:spawn` | Complex workflows | Orchestration system | Multi-step operations, workflow automation |
| `/cb:task` | Project management | Planning system | Long-term feature planning, task tracking |
| `/cb:workflow` | Implementation planning | Workflow system | Creating step-by-step workflows from PRDs |
| `/cb:index` | Command navigation | Help system | Finding the right command for your task |

**Pro tip**: Just try the ones that sound useful. CulturaBuilder usually tries to activate helpful experts and tools for each situation! 🎯

## Development Commands 🔨

### `/workflow` - Implementation Workflow Generator 🗺️
**What it does**: Analyzes PRDs and feature requirements to create comprehensive step-by-step implementation workflows.

**The helpful part**: Takes your PRD and breaks it down into a structured implementation plan with expert guidance, dependency mapping, and task orchestration! 🎯

**When to use it**:
- Starting a new feature from a PRD or specification
- Need a clear implementation roadmap
- Want expert guidance on implementation strategy
- Planning complex features with multiple dependencies

**The magic**: Auto-activates appropriate expert personas (architect, security, frontend, backend) and MCP servers (Context7 for patterns, Sequential for complex analysis) based on your feature requirements.

**Examples**:
```bash
/cb:workflow docs/feature-100-prd.md --strategy systematic --c7 --sequential
/cb:workflow "user authentication system" --persona security --output detailed
/cb:workflow payment-api --strategy mvp --risks --dependencies
```

**What you get**:
- **Roadmap Format**: Phase-based implementation plan with timelines
- **Tasks Format**: Organized epics, stories, and actionable tasks  
- **Detailed Format**: Step-by-step instructions with time estimates
- **Risk Assessment**: Potential issues and mitigation strategies
- **Dependency Mapping**: Internal and external dependencies
- **Expert Guidance**: Domain-specific best practices and patterns

### `/implement` - Feature Implementation
**What it does**: Implements features, components, and functionality with intelligent expert activation.

**The helpful part**: CulturaBuilder auto-activates the right experts (frontend, backend, security) and tools based on what you're implementing! 🎯

**When to use it**:
- Creating new features or components (replaces v2's `/build` functionality)
- Implementing APIs, services, or modules
- Building UI components with modern frameworks
- Developing business logic and integrations

**Basic syntax**:
```bash
/cb:implement user authentication system      # Implement complete feature
/cb:implement --type component LoginForm      # Create specific component  
/cb:implement --type api user-management      # Build API endpoints
/cb:implement --framework react dashboard     # Framework-specific implementation
```

**Useful flags**:
- `--type component|api|service|feature|module` - Implementation type
- `--framework react|vue|express|django|etc` - Target framework
- `--safe` - Conservative implementation approach
- `--iterative` - Step-by-step development with validation
- `--with-tests` - Include test implementation
- `--documentation` - Generate docs alongside code

**Real examples**:
```bash
/cb:implement user authentication --type feature --with-tests
/cb:implement dashboard component --type component --framework react
/cb:implement REST API for orders --type api --safe
/cb:implement payment processing --type service --iterative
/cb:implement search functionality --framework vue --documentation
```

**Auto-activation patterns**:
- **Frontend**: UI components, React/Vue/Angular → frontend persona + Magic MCP
- **Backend**: APIs, services, databases → backend persona + Context7
- **Security**: Auth, payments, sensitive data → security persona + validation
- **Complex features**: Multi-step implementations → Sequential MCP + architect persona

**Gotchas**:
- Specify `--type` for better results (component vs service vs feature)
- Use `--framework` when working with specific tech stacks
- Try `--safe` for production code or `--iterative` for complex features
- Remember: this replaces v2's `/build` for actual code implementation

---

### `/build` - Project Building
**What it does**: Builds, compiles, and packages projects with smart error handling.

**The easy way**: Just type `/cb:build` and CulturaBuilder tries to figure out your build system! 🎯

**When to use it**:
- You need to compile/bundle your project (just try `/cb:build`)
- Build process is failing and you want help debugging  
- Setting up build optimization (it tries to detect what you need)
- Preparing for deployment

**Basic syntax**:
```bash
/cb:build                          # Build current project
/cb:build --type prod              # Production build
/cb:build --clean                  # Clean build (remove old artifacts)
/cb:build --optimize               # Enable optimizations
/cb:build src/                     # Build specific directory
```

**Useful flags**:
- `--type dev|prod|test` - Build type
- `--clean` - Clean before building  
- `--optimize` - Enable build optimizations
- `--verbose` - Show detailed build output

**Real examples**:
```bash
/cb:build --type prod --optimize   # Production build with optimizations
/cb:build --clean --verbose        # Clean build with detailed output
/cb:build src/components           # Build just the components folder
```

**Gotchas**:
- Works best with common build tools (npm, webpack, etc.)
- May struggle with very custom build setups
- Check your build tool is in PATH

---

### `/design` - System & Component Design
**What it does**: Creates system architecture, API designs, and component specifications.

**When to use it**:
- Planning new features or systems
- Need API or database design
- Creating component architecture
- Documenting system relationships

**Basic syntax**:
```bash
/cb:design user-auth-system        # Design a user authentication system
/cb:design --type api auth         # Design just the API part
/cb:design --format spec payment   # Create formal specification
```

**Useful flags**:
- `--type architecture|api|component|database` - Design focus
- `--format diagram|spec|code` - Output format
- `--iterative` - Refine design through iterations

**Real examples**:
```bash
/cb:design --type api user-management    # Design user management API
/cb:design --format spec chat-system     # Create chat system specification
/cb:design --type database ecommerce     # Design database schema
```

**Gotchas**:
- More conceptual than code-generating
- Output quality depends on how clearly you describe requirements
- Great for planning phase, less for implementation details

## Analysis Commands 🔍

### `/analyze` - Code Analysis  
**What it does**: Comprehensive analysis of code quality, security, performance, and architecture.

**The helpful part**: CulturaBuilder tries to detect what kind of analysis you need and usually picks relevant experts! 🔍

**When to use it**:
- Understanding unfamiliar codebases (just point it at any folder)
- Finding security vulnerabilities (security expert usually jumps in)
- Performance bottleneck hunting (performance expert usually helps)
- Code quality assessment (quality specialist often takes over)

**Basic syntax**:
```bash
/cb:analyze src/                   # Analyze entire src directory
/cb:analyze --focus security       # Focus on security issues
/cb:analyze --depth deep app.js    # Deep analysis of specific file
```

**Useful flags**:
- `--focus quality|security|performance|architecture` - Analysis focus
- `--depth quick|deep` - Analysis thoroughness
- `--format text|json|report` - Output format

**Real examples**:
```bash
/cb:analyze --focus security --depth deep     # Deep security analysis
/cb:analyze --focus performance src/api/      # Performance analysis of API
/cb:analyze --format report .                 # Generate analysis report
```

**Gotchas**:
- Can take a while on large codebases
- Security analysis is pretty good, performance analysis varies
- Works best with common languages (JS, Python, etc.)

---

### `/troubleshoot` - Problem Investigation
**What it does**: Systematic debugging and problem investigation.

**When to use it**:
- Something's broken and you're not sure why
- Need systematic debugging approach
- Error messages are confusing
- Performance issues investigation

**Basic syntax**:
```bash
/cb:troubleshoot "login not working"     # Investigate login issue
/cb:troubleshoot --logs error.log        # Analyze error logs
/cb:troubleshoot performance             # Performance troubleshooting
```

**Useful flags**:
- `--logs <file>` - Include log file analysis
- `--systematic` - Use structured debugging approach
- `--focus network|database|frontend` - Focus area

**Real examples**:
```bash
/cb:troubleshoot "API returning 500" --logs server.log
/cb:troubleshoot --focus database "slow queries"
/cb:troubleshoot "build failing" --systematic
```

**Gotchas**:
- Works better with specific error descriptions
- Include relevant error messages and logs when possible
- May suggest obvious things first (that's usually good!)

---

### `/explain` - Educational Explanations
**What it does**: Explains code, concepts, and technologies in an educational way.

**When to use it**:
- Learning new technologies or patterns
- Understanding complex code
- Need clear explanations for team members
- Documenting tricky concepts

**Basic syntax**:
```bash
/cb:explain async/await               # Explain async/await concept
/cb:explain --code src/utils.js       # Explain specific code file
/cb:explain --beginner React hooks    # Beginner-friendly explanation
```

**Useful flags**:
- `--beginner` - Simpler explanations
- `--advanced` - Technical depth
- `--code <file>` - Explain specific code
- `--examples` - Include practical examples

**Real examples**:
```bash
/cb:explain --beginner "what is REST API"
/cb:explain --code src/auth.js --advanced
/cb:explain --examples "React context patterns"
```

**Gotchas**:
- Great for well-known concepts, may struggle with very niche topics
- Better with specific questions than vague "explain this codebase"
- Include context about your experience level

## Quality Commands ✨

### `/improve` - Code Enhancement
**What it does**: Systematic improvements to code quality, performance, and maintainability.

**When to use it**:
- Refactoring messy code
- Performance optimization
- Applying best practices
- Modernizing old code

**Basic syntax**:
```bash
/cb:improve src/legacy/            # Improve legacy code
/cb:improve --type performance     # Focus on performance
/cb:improve --safe src/utils.js    # Safe, low-risk improvements only
```

**Useful flags**:
- `--type quality|performance|maintainability|style` - Improvement focus
- `--safe` - Only apply low-risk changes
- `--preview` - Show what would be changed without doing it

**Real examples**:
```bash
/cb:improve --type performance --safe src/api/
/cb:improve --preview src/components/LegacyComponent.js
/cb:improve --type style . --safe
```

**Gotchas**:
- Always use `--preview` first to see what it wants to change
- `--safe` is your friend - prevents risky refactoring
- Works best on smaller files/modules rather than entire codebases

---

### `/cleanup` - Technical Debt Reduction
**What it does**: Removes dead code, unused imports, and organizes file structure.

**When to use it**:
- Codebase feels cluttered
- Lots of unused imports/variables
- File organization is messy
- Before major refactoring

**Basic syntax**:
```bash
/cb:cleanup src/                   # Clean up src directory
/cb:cleanup --dead-code            # Focus on dead code removal
/cb:cleanup --imports package.js   # Clean up imports in specific file
```

**Useful flags**:
- `--dead-code` - Remove unused code
- `--imports` - Clean up import statements
- `--files` - Reorganize file structure
- `--safe` - Conservative cleanup only

**Real examples**:
```bash
/cb:cleanup --dead-code --safe src/utils/
/cb:cleanup --imports src/components/
/cb:cleanup --files . --safe
```

**Gotchas**:
- Can be aggressive - always review changes carefully
- May not catch all dead code (especially dynamic imports)
- Better to run on smaller sections than entire projects

---

### `/test` - Testing & Quality Assurance
**What it does**: Runs tests, generates coverage reports, and maintains test quality.

**When to use it**:
- Running test suites
- Checking test coverage
- Generating test reports
- Setting up continuous testing

**Basic syntax**:
```bash
/cb:test                           # Run all tests
/cb:test --type unit               # Run only unit tests
/cb:test --coverage                # Generate coverage report
/cb:test --watch src/              # Watch mode for development
```

**Useful flags**:
- `--type unit|integration|e2e|all` - Test type
- `--coverage` - Generate coverage reports
- `--watch` - Run tests in watch mode
- `--fix` - Try to fix failing tests automatically

**Real examples**:
```bash
/cb:test --type unit --coverage
/cb:test --watch src/components/
/cb:test --type e2e --fix
```

**Gotchas**:
- Needs your test framework to be properly configured
- Coverage reports depend on your existing test setup
- `--fix` is experimental - review what it changes

## Documentation Commands 📝

### `/document` - Focused Documentation
**What it does**: Creates documentation for specific components, functions, or features.

**When to use it**:
- Need README files
- Writing API documentation
- Adding code comments
- Creating user guides

**Basic syntax**:
```bash
/cb:document src/api/auth.js       # Document authentication module
/cb:document --type api            # API documentation
/cb:document --style brief README  # Brief README file
```

**Useful flags**:
- `--type inline|external|api|guide` - Documentation type
- `--style brief|detailed` - Level of detail
- `--template` - Use specific documentation template

**Real examples**:
```bash
/cb:document --type api src/controllers/
/cb:document --style detailed --type guide user-onboarding
/cb:document --type inline src/utils/helpers.js
```

**Gotchas**:
- Better with specific files/functions than entire projects
- Quality depends on how well-structured your code is
- May need some editing to match your project's documentation style

## Project Management Commands 📊

### `/estimate` - Project Estimation
**What it does**: Estimates time, effort, and complexity for development tasks.

**When to use it**:
- Planning new features
- Sprint planning
- Understanding project complexity
- Resource allocation

**Basic syntax**:
```bash
/cb:estimate "add user authentication"    # Estimate auth feature
/cb:estimate --detailed shopping-cart     # Detailed breakdown
/cb:estimate --complexity user-dashboard  # Complexity analysis
```

**Useful flags**:
- `--detailed` - Detailed breakdown of tasks
- `--complexity` - Focus on technical complexity
- `--team-size <n>` - Consider team size in estimates

**Real examples**:
```bash
/cb:estimate --detailed "implement payment system"
/cb:estimate --complexity --team-size 3 "migrate to microservices"
/cb:estimate "add real-time chat" --detailed
```

**Gotchas**:
- Estimates are rough - use as starting points, not gospel
- Works better with clear, specific feature descriptions
- Consider your team's experience with the tech stack

---

### `/task` - Long-term Project Management
**What it does**: Manages complex, multi-session development tasks and features.

**When to use it**:
- Planning features that take days/weeks
- Breaking down large projects
- Tracking progress across sessions
- Coordinating team work

**Basic syntax**:
```bash
/cb:task create "implement user dashboard"  # Create new task
/cb:task status                            # Check task status
/cb:task breakdown "payment integration"    # Break down into subtasks
```

**Useful flags**:
- `create` - Create new long-term task
- `status` - Check current task status
- `breakdown` - Break large task into smaller ones
- `--priority high|medium|low` - Set task priority

**Real examples**:
```bash
/cb:task create "migrate from REST to GraphQL" --priority high
/cb:task breakdown "e-commerce checkout flow"
/cb:task status
```

**Gotchas**:
- Still experimental - doesn't always persist across sessions reliably 😅
- Better for planning than actual project management
- Works best when you're specific about requirements

---

### `/spawn` - Complex Operation Orchestration
**What it does**: Coordinates complex, multi-step operations and workflows.

**When to use it**:
- Operations involving multiple tools/systems
- Coordinating parallel workflows
- Complex deployment processes
- Multi-stage data processing

**Basic syntax**:
```bash
/cb:spawn deploy-pipeline          # Orchestrate deployment
/cb:spawn --parallel migrate-data  # Parallel data migration
/cb:spawn setup-dev-environment    # Complex environment setup
```

**Useful flags**:
- `--parallel` - Run operations in parallel when possible
- `--sequential` - Force sequential execution
- `--monitor` - Monitor operation progress

**Real examples**:
```bash
/cb:spawn --parallel "test and deploy to staging"
/cb:spawn setup-ci-cd --monitor
/cb:spawn --sequential database-migration
```

**Gotchas**:
- Most complex command - expect some rough edges
- Better for well-defined workflows than ad-hoc operations
- May need multiple iterations to get right

## Version Control Commands 🔄

### `/git` - Enhanced Git Operations
**What it does**: Git operations with intelligent commit messages and workflow optimization.

**When to use it**:
- Making commits with better messages
- Branch management
- Complex git workflows
- Git troubleshooting

**Basic syntax**:
```bash
/cb:git commit                     # Smart commit with auto-generated message
/cb:git --smart-commit add .       # Add and commit with smart message
/cb:git branch feature/new-auth    # Create and switch to new branch
```

**Useful flags**:
- `--smart-commit` - Generate intelligent commit messages
- `--branch-strategy` - Apply branch naming conventions
- `--interactive` - Interactive mode for complex operations

**Real examples**:
```bash
/cb:git --smart-commit "fixed login bug"
/cb:git branch feature/user-dashboard --branch-strategy
/cb:git merge develop --interactive
```

**Gotchas**:
- Smart commit messages are pretty good but review them
- Assumes you're following common git workflows
- Won't fix bad git habits - just makes them easier

## Utility Commands 🔧

### `/index` - Command Navigation
**What it does**: Helps you find the right command for your task.

**When to use it**:
- Not sure which command to use
- Exploring available commands
- Learning about command capabilities

**Basic syntax**:
```bash
/cb:index                          # List all commands
/cb:index testing                  # Find commands related to testing
/cb:index --category analysis      # Commands in analysis category
```

**Useful flags**:
- `--category <cat>` - Filter by command category
- `--search <term>` - Search command descriptions

**Real examples**:
```bash
/cb:index --search "performance"
/cb:index --category quality
/cb:index git
```

**Gotchas**:
- Simple but useful for discovery
- Better than trying to remember all 16 commands

---

### `/load` - Project Context Loading
**What it does**: Loads and analyzes project context for better understanding.

**When to use it**:
- Starting work on unfamiliar project
- Need to understand project structure
- Before making major changes
- Onboarding team members

**Basic syntax**:
```bash
/cb:load                           # Load current project context
/cb:load src/                      # Load specific directory context
/cb:load --deep                    # Deep analysis of project structure
```

**Useful flags**:
- `--deep` - Comprehensive project analysis
- `--focus <area>` - Focus on specific project area
- `--summary` - Generate project summary

**Real examples**:
```bash
/cb:load --deep --summary
/cb:load src/components/ --focus architecture
/cb:load . --focus dependencies
```

**Gotchas**:
- Can take time on large projects
- More useful at project start than during development
- Helps with onboarding but not a replacement for good docs

## Command Tips & Patterns 💡

### Effective Flag Combinations
```bash
# Safe improvement workflow
/cb:improve --preview src/component.js    # See what would change
/cb:improve --safe src/component.js       # Apply safe changes only

# Comprehensive analysis
/cb:analyze --focus security --depth deep
/cb:test --coverage
/cb:document --type api

# Smart git workflow
/cb:git add .
/cb:git --smart-commit --branch-strategy

# Project understanding workflow
/cb:load --deep --summary
/cb:analyze --focus architecture
/cb:document --type guide
```

### Common Workflows

**New Project Onboarding**:
```bash
/cb:load --deep --summary
/cb:analyze --focus architecture
/cb:test --coverage
/cb:document README
```

**Bug Investigation**:
```bash
/cb:troubleshoot "specific error message" --logs
/cb:analyze --focus security
/cb:test --type unit affected-component
```

**Code Quality Improvement**:
```bash
/cb:analyze --focus quality
/cb:improve --preview src/
/cb:cleanup --safe
/cb:test --coverage
```

**Pre-deployment Checklist**:
```bash
/cb:test --type all --coverage
/cb:analyze --focus security
/cb:build --type prod --optimize
/cb:git --smart-commit
```

### Troubleshooting Command Issues

**Command not working as expected?**
- Try adding `--help` to see all options
- Use `--preview` or `--safe` flags when available
- Start with smaller scope (single file vs. entire project)

**Analysis taking too long?**
- Use `--focus` to narrow scope
- Try `--depth quick` instead of deep analysis
- Analyze smaller directories first

**Build/test commands failing?**
- Make sure your tools are in PATH
- Check that config files are in expected locations
- Try running the underlying commands directly first

**Not sure which command to use?**
- Use `/index` to browse available commands
- Look at the Quick Reference table above
- Try the most specific command first, then broader ones

---

## Final Notes 📝

**The real truth about these commands** 💯:
- **Just try them** - You don't need to study this guide first
- **Start with the basics** - `/analyze`, `/build`, `/improve` cover most needs
- **Let auto-activation work** - CulturaBuilder usually picks helpful experts
- **Experiment freely** - Use `--preview` if you want to see what would happen first

**Still rough around the edges:**
- Complex orchestration (spawn, task) can be a bit flaky
- Some analysis depends heavily on your project setup  
- Error handling could be better in some commands

**Getting better all the time:**
- We actively improve commands based on user feedback
- Newer commands (analyze, improve) tend to work better
- Auto-activation keeps getting smarter

**Don't stress about memorizing this** 🧘‍♂️
- CulturaBuilder is designed to be discoverable through use
- Type `/` to see available commands
- Commands suggest what they can do when you use `--help`
- The intelligent routing handles most of the complexity

**Need help?** Check the GitHub issues or create a new one if you're stuck! 🚀

---

*Happy coding! Just remember - you can skip most of this guide and learn by doing. 🎯*

---
CulturaBuilder
