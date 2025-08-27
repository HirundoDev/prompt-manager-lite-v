"""
Templates CLI
=============

Templates universales para desarrollo de CLI y herramientas de línea de comandos.
"""

def create_cli_reference_template(theme, date_str, filename):
    """Marco de referencia para desarrollo de CLI"""
    return f'''# CLI Development - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Desarrollo de CLI  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para el desarrollo de herramientas CLI, adaptable a diferentes lenguajes y frameworks.

### Decisiones Clave a Capturar
- **Framework CLI** y lenguaje elegido
- **Arquitectura de comandos** y subcomandos
- **Gestión de argumentos** y opciones
- **User experience** y feedback
- **Distribución** y deployment

---

## 🏗️ Arquitectura CLI

### Framework y Lenguaje
**Decisión:** [Stack tecnológico elegido]

#### Por Lenguaje
- **Node.js:** [Commander.js, Yargs, Oclif, Inquirer]
- **Python:** [Click, argparse, Typer, Fire]
- **Go:** [Cobra, Urfave/CLI, Kingpin]
- **Rust:** [Clap, StructOpt, Argh]
- **Java:** [Picocli, JCommander, Spring Shell]
- **Other:** [Especificar framework]

**Justificación:** [Por qué esta elección]

### Estructura de Comandos
**Decisión:** [Arquitectura de comandos definida]

#### Single Command CLI
```bash
# Estructura simple
mycli [options] <arguments>
mycli --help
mycli --version
```

#### Multi-Command CLI
```bash
# Estructura con subcomandos
mycli <command> [subcommand] [options] <arguments>
mycli user create --email john@example.com
mycli project list --format table
mycli config set key value
```

#### Nested Commands
```bash
# Estructura anidada
mycli resource subresource action [options]
mycli database migration create --name add_users
mycli docker container start --name myapp
```

---

## ⚙️ Command Structure

### Command Patterns
**Decisión:** [Patrones de comando implementados]

#### CRUD Operations
```bash
mycli [resource] create [options]
mycli [resource] read|get|show [id] [options]  
mycli [resource] update [id] [options]
mycli [resource] delete|remove [id] [options]
mycli [resource] list [options]
```

#### Action-Based Commands
```bash
mycli deploy [environment] [options]
mycli test [suite] [options]
mycli build [target] [options]
mycli sync [source] [destination] [options]
```

### Global vs Local Options
**Decisión:** [Manejo de opciones globales y locales]

#### Global Options
```bash
# Available for all commands
--verbose, -v     # Verbose output
--quiet, -q       # Suppress output
--config, -c      # Config file path
--help, -h        # Show help
--version         # Show version
```

#### Command-Specific Options
```bash
# Specific to individual commands
mycli deploy --env production --force
mycli test --coverage --parallel
mycli build --target docker --push
```

---

## 📝 Argument Parsing

### Argument Types
**Decisión:** [Tipos de argumentos soportados]

#### Positional Arguments
```bash
# Required positional arguments
mycli create <name> <type>
mycli deploy <environment>
```

#### Optional Arguments
```bash
# With default values
mycli build [target=development]
mycli test [pattern=**/*.test.js]
```

#### Flags/Options
```bash
# Boolean flags
--force, --no-force
--verbose, --quiet
--dry-run

# Value options
--config path/to/config.json
--format table|json|yaml
--timeout 30s
```

### Validation Strategy
**Decisión:** [Validación de argumentos]
```javascript
// Ejemplo con Commander.js
program
  .command('create <name>')
  .option('-t, --type <type>', 'resource type', 'default')
  .option('-f, --force', 'force creation')
  .action((name, options) => {{
    // Validation logic
    if (!isValidName(name)) {{
      console.error('Error: Invalid name format');
      process.exit(1);
    }}
    
    if (!['user', 'project', 'config'].includes(options.type)) {{
      console.error('Error: Invalid type. Must be user, project, or config');
      process.exit(1);
    }}
    
    // Command logic here
  }});
```

---

## 🎨 User Experience

### Output Formatting
**Decisión:** [Estrategia de formato de salida]

#### Structured Output
```bash
# Table format
mycli list --format table
┌─────┬──────────────┬─────────────┬─────────────────────┐
│ ID  │ Name         │ Status      │ Created             │
├─────┼──────────────┼─────────────┼─────────────────────┤
│ 1   │ Project A    │ active      │ 2024-01-15 10:30:00 │
│ 2   │ Project B    │ inactive    │ 2024-01-14 15:45:00 │
└─────┴──────────────┴─────────────┴─────────────────────┘

# JSON format
mycli list --format json
{{
  "data": [
    {{ "id": 1, "name": "Project A", "status": "active" }},
    {{ "id": 2, "name": "Project B", "status": "inactive" }}
  ]
}}

# YAML format
mycli list --format yaml
data:
  - id: 1
    name: "Project A"
    status: "active"
  - id: 2
    name: "Project B" 
    status: "inactive"
```

#### Progress Indicators
```javascript
// Progress bars and spinners
const ora = require('ora');
const ProgressBar = require('progress');

// Spinner for indeterminate progress
const spinner = ora('Processing...').start();
// spinner.succeed('Completed!');

// Progress bar for determinate progress
const bar = new ProgressBar(':bar :percent :etas', {{ total: 100 }});
// bar.tick();
```

### Interactive Elements
**Decisión:** [Elementos interactivos implementados]

#### Prompts and Confirmations
```javascript
// Inquirer.js examples
const inquirer = require('inquirer');

// Simple confirmation
const {{ confirm }} = await inquirer.prompt([{{
  type: 'confirm',
  name: 'confirm',
  message: 'Are you sure you want to delete this project?',
  default: false
}}]);

// Selection menu
const {{ choice }} = await inquirer.prompt([{{
  type: 'list',
  name: 'choice',
  message: 'Select deployment environment:',
  choices: ['development', 'staging', 'production']
}}]);

// Text input with validation
const {{ name }} = await inquirer.prompt([{{
  type: 'input',
  name: 'name',
  message: 'Enter project name:',
  validate: (input) => input.length > 0 || 'Name is required'
}}]);
```

---

## 🔧 Configuration Management

### Config Strategy
**Decisión:** [Estrategia de configuración]

#### Config File Locations
```bash
# Priority order (highest to lowest)
1. --config flag specified file
2. ./[app-name].config.[json|yaml|toml]
3. ~/.config/[app-name]/config.[json|yaml|toml]  
4. /etc/[app-name]/config.[json|yaml|toml]
5. Environment variables
6. Default values
```

#### Config File Format
```json
// JSON configuration
{{
  "api": {{
    "base_url": "https://api.example.com",
    "timeout": 30000,
    "retries": 3
  }},
  "output": {{
    "format": "table",
    "colors": true,
    "verbose": false
  }},
  "profiles": {{
    "default": {{
      "environment": "development",
      "region": "us-east-1"
    }},
    "production": {{
      "environment": "production", 
      "region": "us-west-2"
    }}
  }}
}}
```

### Environment Variables
**Decisión:** [Variables de entorno soportadas]
```bash
# Standard environment variables
MYCLI_CONFIG_PATH=/path/to/config.json
MYCLI_API_KEY=secret_key_here
MYCLI_ENVIRONMENT=production
MYCLI_VERBOSE=true
MYCLI_NO_COLOR=false
```

---

## 📚 Help System

### Help Documentation
**Decisión:** [Sistema de ayuda implementado]

#### Auto-generated Help
```bash
# Global help
mycli --help
mycli -h

# Command-specific help
mycli deploy --help
mycli user create --help

# Subcommand help
mycli database migration --help
```

#### Help Content Structure
```
USAGE:
    mycli [OPTIONS] <SUBCOMMAND>

OPTIONS:
    -h, --help       Print help information
    -V, --version    Print version information
    -v, --verbose    Use verbose output
    -q, --quiet      Suppress output

SUBCOMMANDS:
    create    Create a new resource
    list      List all resources
    deploy    Deploy to environment
    help      Print this message or the help of the given subcommand(s)

Use "mycli <subcommand> --help" for more information on a specific command.
```

### Examples and Usage
**Decisión:** [Documentación de ejemplos]
```bash
# Built-in examples command
mycli examples
mycli help examples

# In help output
EXAMPLES:
    mycli create myproject --type web
    mycli deploy production --force
    mycli list --format json --filter status=active
```

---

## 🚦 Error Handling

### Error Strategy
**Decisión:** [Manejo de errores implementado]

#### Exit Codes
```bash
# Standard exit codes
0   # Success
1   # General error
2   # Misuse of shell builtins
64  # Command line usage error
65  # Data format error
66  # Cannot open input
67  # Addressee unknown
68  # Host name unknown
69  # Service unavailable
70  # Internal software error
```

#### Error Messages
```javascript
// User-friendly error messages
class CLIError extends Error {{
  constructor(message, code = 1, suggestions = []) {{
    super(message);
    this.code = code;
    this.suggestions = suggestions;
  }}
}}

// Usage example
throw new CLIError(
  'Project "myapp" not found',
  1,
  [
    'Check if the project name is correct',
    'Run "mycli list" to see available projects',
    'Use "mycli create myapp" to create a new project'
  ]
);
```

#### Graceful Degradation
```javascript
// Handle network failures gracefully
async function fetchData() {{
  try {{
    const data = await api.getData();
    return data;
  }} catch (error) {{
    if (error.code === 'ENOTFOUND') {{
      console.error('Network error: Please check your internet connection');
      return getCachedData(); // Fallback to cached data
    }}
    throw error;
  }}
}}
```

---

## 🧪 Testing Strategy

### CLI Testing
**Decisión:** [Estrategia de testing para CLI]

#### Unit Testing
```javascript
// Test individual functions
describe('Command parser', () => {{
  test('parses create command correctly', () => {{
    const args = ['create', 'myproject', '--type', 'web'];
    const parsed = parseArgs(args);
    
    expect(parsed.command).toBe('create');
    expect(parsed.name).toBe('myproject');
    expect(parsed.type).toBe('web');
  }});
}});
```

#### Integration Testing
```javascript
// Test complete command execution
const {{ execSync }} = require('child_process');

describe('CLI Integration', () => {{
  test('create command works end-to-end', () => {{
    const output = execSync('node cli.js create testproject --type web', {{
      encoding: 'utf8'
    }});
    
    expect(output).toContain('Project "testproject" created successfully');
  }});
}});
```

#### Output Testing
```javascript
// Test output formatting
describe('Output formatting', () => {{
  test('formats table output correctly', () => {{
    const data = [{{ id: 1, name: 'test', status: 'active' }}];
    const output = formatTable(data);
    
    expect(output).toMatch(/┌.*┐/); // Table borders
    expect(output).toContain('test');
    expect(output).toContain('active');
  }});
}});
```

---

## 📦 Distribution y Packaging

### Package Distribution
**Decisión:** [Método de distribución]

#### npm (Node.js)
```json
// package.json
{{
  "name": "@company/mycli",
  "version": "1.0.0",
  "bin": {{
    "mycli": "./bin/mycli.js"
  }},
  "files": [
    "bin/",
    "lib/",
    "README.md"
  ],
  "engines": {{
    "node": ">=14.0.0"
  }}
}}
```

#### pip (Python)
```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="mycli",
    version="1.0.0",
    packages=find_packages(),
    entry_points={{
        "console_scripts": [
            "mycli=mycli.main:main",
        ],
    }},
    python_requires=">=3.8",
)
```

#### Cargo (Rust)
```toml
# Cargo.toml
[package]
name = "mycli"
version = "1.0.0"
edition = "2021"

[[bin]]
name = "mycli"
path = "src/main.rs"

[dependencies]
clap = {{ version = "4.0", features = ["derive"] }}
```

### Cross-Platform Support
**Decisión:** [Soporte multiplataforma]
- **Windows:** [Executable, MSI installer, Chocolatey]
- **macOS:** [Binary, Homebrew, macOS installer]
- **Linux:** [Binary, deb/rpm packages, snap, AppImage]

### Auto-Update Mechanism
**Decisión:** [Actualización automática]
```javascript
// Check for updates
async function checkForUpdates() {{
  const currentVersion = require('./package.json').version;
  const latestVersion = await getLatestVersion();
  
  if (semver.gt(latestVersion, currentVersion)) {{
    console.log(`Update available: ${currentVersion} → ${latestVersion}`);
    console.log('Run "mycli update" to update');
  }}
}}
```

---

## 📊 Monitoring y Analytics

### Usage Analytics
**Decisión:** [Telemetría y analytics]
- **Anonymous usage stats:** [Command frequency, error rates]
- **Performance metrics:** [Command execution time]
- **Error reporting:** [Crash reports, error patterns]
- **Opt-out mechanism:** [User privacy controls]

### Logging
**Decisión:** [Sistema de logging]
```javascript
// Structured logging
const winston = require('winston');

const logger = winston.createLogger({{
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({{
      filename: '~/.mycli/logs/error.log',
      level: 'error'
    }}),
    new winston.transports.File({{
      filename: '~/.mycli/logs/combined.log'
    }})
  ]
}});

// Usage
logger.info('Command executed', {{
  command: 'create',
  args: ['myproject'],
  duration: 1250,
  success: true
}});
```

---

## 🔐 Security Considerations

### Input Validation
**Decisión:** [Validación de entrada]
- **Path traversal prevention:** [Sanitize file paths]
- **Command injection prevention:** [Escape shell commands]
- **Input size limits:** [Prevent DoS attacks]
- **Format validation:** [Validate structured inputs]

### Credential Management
**Decisión:** [Gestión de credenciales]
- **Secure storage:** [Keychain, credential managers]
- **Token expiration:** [Automatic refresh]
- **Encryption:** [At-rest credential encryption]

---

## 🔄 Próximos Pasos

### CLI Foundation
- [ ] [Setup CLI framework y estructura básica]
- [ ] [Implementar command parsing]
- [ ] [Crear help system]

### Core Functionality  
- [ ] [Implementar comandos principales]
- [ ] [Agregar configuration management]
- [ ] [Setup error handling]

### User Experience
- [ ] [Implementar progress indicators]
- [ ] [Agregar interactive prompts]
- [ ] [Optimizar output formatting]

### Distribution
- [ ] [Setup packaging y build]
- [ ] [Crear distribution pipeline]
- [ ] [Implementar auto-update]

### Monitoring
- [ ] [Setup logging system]
- [ ] [Implementar error tracking]
- [ ] [Agregar usage analytics]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''
