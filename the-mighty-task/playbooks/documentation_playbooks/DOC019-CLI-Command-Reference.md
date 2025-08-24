# CLI Development - Marco Universal

## Propósito del Documento
Este marco universal proporciona una estructura para diseñar, documentar e implementar interfaces de línea de comandos (CLI) efectivas y amigables para desarrolladores. El documento está diseñado para ser adaptable a cualquier tipo de herramienta CLI, lenguaje de programación y caso de uso.

## 🎯 Objetivos Clave

- Establecer principios de diseño para CLI intuitiva y poderosa
- Crear documentación clara y completa para herramientas CLI
- Implementar patrones de usabilidad y experiencia de desarrollador
- Asegurar mantenibilidad y extensibilidad de la CLI
- Facilitar testing y validación de comandos CLI

---

## 📐 Principios de Diseño de CLI

### Filosofía de Diseño
**Decisión:** [Approach de diseño adoptado]

**Principios considerados:**
- **UNIX Philosophy:** Small, focused, composable tools
- **Progressive Disclosure:** Basic to advanced functionality
- **Consistency:** Uniform patterns and conventions
- **Error Prevention:** Clear validation and helpful messages
- **Performance First:** Fast execution and minimal overhead

**Design patterns adoptados:**
- [Pattern 1: Command hierarchy design]
- [Pattern 2: Parameter naming conventions]
- [Pattern 3: Output formatting standards]
- [Pattern 4: Error handling approach]

### Convenciones de Naming
**Decisión:** [Naming strategy adoptada]

**Command naming:**
- **Verbs:** [Action-based commands like 'create', 'list', 'update']
- **Nouns:** [Resource-based commands like 'user', 'project', 'config']
- **Compound:** [Combination like 'user-create', 'project-list']

**Parameter naming:**
- **Short flags:** [-v, -h, -f] [Single character options]
- **Long flags:** [--verbose, --help, --force] [Descriptive options]
- **Consistency:** [Same flags mean same things across commands]

---

## 🏗️ Arquitectura de CLI

### Command Structure
**Decisión:** [CLI architecture pattern]

**Structure patterns:**
- **Flat structure:** [Single level commands]
- **Hierarchical:** [Nested subcommands]
- **Plugin-based:** [Extensible command architecture]
- **Hybrid:** [Combination of patterns]

#### Command Hierarchy Example
```
cli-tool
├── config
│   ├── get
│   ├── set
│   └── list
├── project
│   ├── create
│   ├── list
│   ├── deploy
│   └── delete
└── user
    ├── login
    ├── logout
    └── profile
```

### Framework y Tools
**Decisión:** [CLI framework elegido]

**Framework options:**
- **Node.js:** Commander.js, Yargs, Oclif
- **Python:** Click, Argparse, Typer
- **Go:** Cobra, CLI, Kingpin  
- **Rust:** Clap, StructOpt
- **Java:** JCommander, Spring Shell
- **Other:** [Framework específico del lenguaje]

---

## ⚙️ Command Design Patterns

### Command Categories
**Decisión:** [Categorización de comandos]

#### Core Commands
- **Initialization:** [setup, init, bootstrap]
- **Configuration:** [config, settings, preferences]
- **CRUD Operations:** [create, read, update, delete]
- **Deployment:** [deploy, build, publish]

#### Utility Commands
- **Information:** [info, version, help, status]
- **Debugging:** [debug, trace, logs, inspect]
- **Maintenance:** [cleanup, migrate, backup]

### Parameter Types
**Decisión:** [Types de parámetros soportados]

**Basic types:**
- **String:** [Text inputs, paths, URLs]
- **Number:** [Integers, floats, port numbers]
- **Boolean:** [Flags, switches, toggles]
- **Array:** [Multiple values, lists]
- **File/Path:** [File inputs, directory paths]

**Complex types:**
- **Enum/Choice:** [Predefined options]
- **JSON:** [Complex object inputs]
- **Key-Value:** [Configuration pairs]

---

## 📝 Command Documentation

### Help System Design
**Decisión:** [Help system implementation]

**Help levels:**
- **Command help:** [Individual command usage]
- **Category help:** [Group of related commands]
- **Global help:** [Overall CLI usage]
- **Contextual help:** [Situation-specific guidance]

### Documentation Structure
**Decisión:** [Documentation format]

#### Command Reference Template
```markdown
## [COMMAND_NAME]

**Description:** [What this command does]

**Usage:** 
```
[cli-tool] [command] [subcommand] [options] [arguments]
```

**Arguments:**
- `[argument]` - [Description of argument]

**Options:**
- `-h, --help` - Show help information
- `-v, --verbose` - Enable verbose output
- `--format [FORMAT]` - Output format (json|yaml|table)

**Examples:**
```bash
# Basic usage
[cli-tool] [command] [basic-example]

# Advanced usage
[cli-tool] [command] --option value [advanced-example]
```

**Related Commands:**
- [`[related-command]`](#related-command) - [Brief description]
```

---

## 🎨 User Experience Design

### Input Validation
**Decisión:** [Validation strategy]

**Validation types:**
- **Format validation:** [Email, URL, regex patterns]
- **Range validation:** [Number ranges, string length]
- **Dependency validation:** [Required combinations]
- **Environment validation:** [System requirements]

### Error Handling
**Decisión:** [Error handling approach]

**Error categories:**
- **User errors:** [Invalid input, missing arguments]
- **System errors:** [Permission denied, file not found]
- **Network errors:** [Connection failed, timeout]
- **Application errors:** [Logic errors, unexpected states]

#### Error Message Format
```
Error: [ERROR_TYPE] - [Brief description]

Cause: [What went wrong]
Solution: [How to fix it]

For more help: [cli-tool] help [command]
```

### Output Formatting
**Decisión:** [Output format options]

**Format types:**
- **Human-readable:** [Formatted tables, colored output]
- **Machine-readable:** [JSON, YAML, CSV]
- **Structured:** [XML, formatted logs]

---

## 🧪 Testing Strategy

### Testing Levels
**Decisión:** [CLI testing approach]

#### Unit Tests
- **Command parsing:** [Argument parsing logic]
- **Validation logic:** [Input validation functions]
- **Business logic:** [Core functionality]
- **Error handling:** [Error scenarios]

#### Integration Tests
- **Command execution:** [End-to-end command testing]
- **File operations:** [File system interactions]
- **Network operations:** [API calls, downloads]
- **System integration:** [Environment interactions]

#### User Experience Tests
- **Usability testing:** [Developer workflow testing]
- **Performance testing:** [Command execution time]
- **Compatibility testing:** [Different OS and environments]

### Test Automation
**Decisión:** [Test automation framework]

```bash
# Test command examples
test-framework run --command "cli-tool --help"
test-framework expect --output "Usage: cli-tool"

test-framework run --command "cli-tool invalid-command"
test-framework expect --exit-code 1
test-framework expect --stderr "Error: Unknown command"
```

---

## 📊 Performance y Optimization

### Performance Considerations
**Decisión:** [Performance optimization strategy]

**Optimization areas:**
- **Startup time:** [Fast CLI initialization]
- **Command execution:** [Efficient processing]
- **Memory usage:** [Minimal resource consumption]
- **Network efficiency:** [Optimized API calls]

### Caching Strategy
**Decisión:** [Caching implementation]

**Cache types:**
- **Command metadata:** [Command definitions, help text]
- **User data:** [Authentication tokens, preferences]
- **Remote data:** [API responses, file downloads]
- **Computed results:** [Expensive calculations]

---

## 🔧 Configuration Management

### Configuration Strategy
**Decisión:** [Configuration approach]

**Configuration sources (priority order):**
1. Command-line arguments
2. Environment variables  
3. Configuration files
4. Default values

### Configuration File Format
**Decisión:** [Config file format]

```yaml
# CLI configuration example
cli-tool:
  defaults:
    output-format: json
    verbose: false
  
  profiles:
    development:
      api-endpoint: https://dev-api.example.com
      timeout: 30s
    
    production:
      api-endpoint: https://api.example.com
      timeout: 10s
  
  aliases:
    deploy: project deploy
    ls: project list
```

---

## 🚀 Distribution y Installation

### Distribution Strategy
**Decisión:** [Distribution method]

**Distribution channels:**
- **Package managers:** [npm, pip, brew, apt, yum]
- **Binary releases:** [GitHub releases, direct download]
- **Container images:** [Docker images]
- **Installation scripts:** [curl install, custom installers]

### Update Mechanism
**Decisión:** [Update strategy]

**Update approaches:**
- **Manual updates:** [User-initiated updates]
- **Automatic updates:** [Background updates]
- **Notification-based:** [Update available notifications]
- **Version management:** [Multiple version support]

---

## 📋 Development Templates

### Command Template
```typescript
// Command implementation template
interface CommandConfig {
  name: string;
  description: string;
  arguments: ArgumentDefinition[];
  options: OptionDefinition[];
  handler: CommandHandler;
}

interface ArgumentDefinition {
  name: string;
  description: string;
  type: 'string' | 'number' | 'boolean' | 'array';
  required: boolean;
  validation?: ValidationRule[];
}

interface OptionDefinition {
  short?: string;
  long: string;
  description: string;
  type: 'string' | 'number' | 'boolean' | 'array';
  default?: any;
  choices?: string[];
}

type CommandHandler = (args: any, options: any) => Promise<void>;
```

### CLI Framework Setup Template
```javascript
// CLI setup example (Node.js with Commander)
#!/usr/bin/env node

const { Command } = require('commander');
const program = new Command();

program
  .name('[cli-tool-name]')
  .description('[CLI tool description]')
  .version('[version]');

// Add commands
program
  .command('[command-name]')
  .description('[Command description]')
  .argument('[argument]', '[Argument description]')
  .option('-v, --verbose', 'Enable verbose output')
  .action((argument, options) => {
    // Command implementation
    console.log(`Executing ${argument} with options:`, options);
  });

program.parse();
```

---

## 📋 Development Checklist

### Design Phase
- [ ] CLI architecture defined
- [ ] Command hierarchy planned
- [ ] Naming conventions established
- [ ] User workflows mapped
- [ ] Error scenarios identified

### Implementation Phase  
- [ ] Framework selected and configured
- [ ] Core commands implemented
- [ ] Input validation added
- [ ] Error handling implemented
- [ ] Help system created

### Testing Phase
- [ ] Unit tests written
- [ ] Integration tests implemented
- [ ] User workflow testing completed
- [ ] Performance benchmarks met
- [ ] Documentation validated

### Release Phase
- [ ] Distribution package created
- [ ] Installation instructions written
- [ ] User documentation complete
- [ ] Release notes prepared
- [ ] Update mechanism tested

---

## 📚 Documentation Templates

### README Template for CLI Tools
```markdown
# [CLI Tool Name]

[Brief description of what the CLI tool does]

## Installation

```bash
# Installation command
npm install -g [cli-tool]
# or
pip install [cli-tool]
# or
brew install [cli-tool]
```

## Quick Start

```bash
# Initialize
[cli-tool] init

# Basic usage
[cli-tool] [command] [arguments]

# Get help
[cli-tool] --help
```

## Commands

- [`init`](#init) - Initialize new project
- [`deploy`](#deploy) - Deploy application  
- [`config`](#config) - Manage configuration

## Configuration

[Configuration file location and format]

## Examples

[Common usage examples]
```

---

**Versión del Marco:** 3.0 Universal  
**Actualizado:** 2025-01-22  
**Aplicable a:** CLI tools, command-line applications, developer tools  
**Próxima revisión:** [Fecha planificada]
