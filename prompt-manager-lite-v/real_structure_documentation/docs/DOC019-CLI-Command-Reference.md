# CLI Command Reference
> **Purpose:** Comprehensive command-line interface documentation following 2025 best practices for CLI design, user experience, and developer productivity. This reference provides complete documentation for all available commands, arguments, flags, and usage patterns.

**Document Type:** CLI Documentation & Reference  
**Version:** 2.0 - Enhanced with 2025 Best Practices  
**Last Updated:** 2025-01-15  
**Template Status:** Production Ready

---

## Document Control
| Field | Value |
|-------|-------|
| **Project Name** | [PROJECT_NAME] |
| **CLI Tool Name** | [CLI_TOOL_NAME] |
| **Current Version** | [CLI_VERSION] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] |
| **Maintainer** | [MAINTAINER_NAME] |

---

## 📋 Table of Contents
- [🎯 CLI Overview](#-cli-overview)
- [🚀 Getting Started](#-getting-started)
- [📖 Command Reference](#-command-reference)
- [🔧 Global Options](#-global-options)
- [💡 Usage Examples](#-usage-examples)
- [🛠️ Advanced Usage](#️-advanced-usage)
- [❓ Troubleshooting](#-troubleshooting)
- [📚 Additional Resources](#-additional-resources)

---

## 🎯 CLI Overview

### What is [CLI_TOOL_NAME]?

[CLI_TOOL_NAME] is a powerful command-line interface designed to streamline [PRIMARY_PURPOSE]. Built with modern CLI design principles, it provides an intuitive, efficient, and robust experience for developers and system administrators.

### Key Features
- **Human-First Design:** Intuitive commands with clear, helpful output
- **Composable Operations:** Commands work together seamlessly via pipes and scripts
- **Comprehensive Help:** Built-in documentation and examples for every command
- **Error Recovery:** Helpful error messages with suggested solutions
- **Cross-Platform:** Works consistently across Linux, macOS, and Windows
- **Automation-Friendly:** Perfect for scripts and CI/CD pipelines

### Design Philosophy
Our CLI follows the [Command Line Interface Guidelines](https://clig.dev/) and embraces these principles:
- **Consistency:** Predictable patterns across all commands
- **Discoverability:** Easy to learn and explore functionality
- **Robustness:** Handles errors gracefully and provides clear feedback
- **Composability:** Works well with other tools and in automation
- **Accessibility:** Inclusive design for users of all experience levels

---

## 🚀 Getting Started

### Installation

#### Package Managers
```bash
# macOS (Homebrew)
brew install [CLI_TOOL_NAME]

# Linux (apt)
sudo apt install [CLI_TOOL_NAME]

# Linux (yum)
sudo yum install [CLI_TOOL_NAME]

# Node.js (npm)
npm install -g [CLI_TOOL_NAME]

# Python (pip)
pip install [CLI_TOOL_NAME]
```

#### Direct Download
```bash
# Download latest release
curl -L https://github.com/[ORG]/[CLI_TOOL_NAME]/releases/latest/download/[CLI_TOOL_NAME]-linux-amd64 -o [CLI_TOOL_NAME]
chmod +x [CLI_TOOL_NAME]
sudo mv [CLI_TOOL_NAME] /usr/local/bin/
```

### Quick Start

```bash
# Check installation
[CLI_TOOL_NAME] --version

# Get help
[CLI_TOOL_NAME] --help

# Run your first command
[CLI_TOOL_NAME] [BASIC_COMMAND]

# Explore available commands
[CLI_TOOL_NAME] help
```

### Configuration

#### Global Configuration
```bash
# Set global configuration
[CLI_TOOL_NAME] config set [KEY] [VALUE]

# View current configuration
[CLI_TOOL_NAME] config list

# Reset to defaults
[CLI_TOOL_NAME] config reset
```

#### Environment Variables
```bash
# Common environment variables
export [CLI_TOOL_NAME]_CONFIG_PATH="~/.config/[CLI_TOOL_NAME]"
export [CLI_TOOL_NAME]_LOG_LEVEL="info"
export [CLI_TOOL_NAME]_OUTPUT_FORMAT="table"
export NO_COLOR=1  # Disable colored output
```

---

## 📖 Command Reference

### Core Commands

#### `init` - Initialize New Project
Initialize a new project with default configuration and structure.

**Usage:**
```bash
[CLI_TOOL_NAME] init [PROJECT_NAME] [OPTIONS]
```

**Arguments:**
- `PROJECT_NAME` (string, optional) - Name of the project to initialize. Defaults to current directory name.

**Options:**
- `-t, --template <template>` - Project template to use (default: "basic")
- `-f, --force` - Overwrite existing files without confirmation
- `-i, --interactive` - Use interactive mode for configuration
- `--dry-run` - Show what would be created without making changes

**Examples:**
```bash
# Initialize project in current directory
[CLI_TOOL_NAME] init

# Initialize with specific name and template
[CLI_TOOL_NAME] init my-project --template advanced

# Interactive initialization
[CLI_TOOL_NAME] init --interactive

# Preview initialization without changes
[CLI_TOOL_NAME] init --dry-run
```

**Exit Codes:**
- `0` - Success
- `1` - General error
- `2` - Directory already exists (without --force)

---

#### `build` - Build Project
Compile and build the project according to configuration.

**Usage:**
```bash
[CLI_TOOL_NAME] build [TARGET] [OPTIONS]
```

**Arguments:**
- `TARGET` (string, optional) - Specific build target. Defaults to "all"

**Options:**
- `-e, --env <environment>` - Build environment (development, staging, production)
- `-w, --watch` - Watch for changes and rebuild automatically
- `-c, --clean` - Clean build artifacts before building
- `-v, --verbose` - Enable verbose output
- `-j, --jobs <number>` - Number of parallel jobs (default: CPU count)
- `--no-cache` - Disable build cache

**Examples:**
```bash
# Basic build
[CLI_TOOL_NAME] build

# Production build with clean
[CLI_TOOL_NAME] build --env production --clean

# Watch mode for development
[CLI_TOOL_NAME] build --watch --verbose

# Build specific target
[CLI_TOOL_NAME] build frontend --env staging
```

**Exit Codes:**
- `0` - Build successful
- `1` - Build failed
- `2` - Configuration error

---

#### `deploy` - Deploy Application
Deploy the built application to specified environment.

**Usage:**
```bash
[CLI_TOOL_NAME] deploy [ENVIRONMENT] [OPTIONS]
```

**Arguments:**
- `ENVIRONMENT` (string, required) - Target deployment environment

**Options:**
- `-c, --config <file>` - Deployment configuration file
- `-f, --force` - Force deployment without confirmation
- `-r, --rollback` - Rollback to previous version
- `--dry-run` - Simulate deployment without making changes
- `--wait` - Wait for deployment to complete
- `--timeout <seconds>` - Deployment timeout (default: 300)

**Examples:**
```bash
# Deploy to staging
[CLI_TOOL_NAME] deploy staging

# Production deployment with confirmation
[CLI_TOOL_NAME] deploy production --wait

# Rollback deployment
[CLI_TOOL_NAME] deploy production --rollback

# Dry run deployment
[CLI_TOOL_NAME] deploy staging --dry-run
```

**Exit Codes:**
- `0` - Deployment successful
- `1` - Deployment failed
- `3` - Rollback required

---

### Management Commands

#### `status` - Show Project Status
Display current project status, health, and metrics.

**Usage:**
```bash
[CLI_TOOL_NAME] status [COMPONENT] [OPTIONS]
```

**Arguments:**
- `COMPONENT` (string, optional) - Specific component to check

**Options:**
- `-f, --format <format>` - Output format (table, json, yaml)
- `-w, --watch` - Continuously monitor status
- `--refresh <seconds>` - Refresh interval for watch mode (default: 5)
- `-q, --quiet` - Show only essential information

**Examples:**
```bash
# Show overall status
[CLI_TOOL_NAME] status

# Monitor specific component
[CLI_TOOL_NAME] status database --watch

# JSON output for scripting
[CLI_TOOL_NAME] status --format json

# Quiet status check
[CLI_TOOL_NAME] status --quiet
```

---

#### `logs` - View Application Logs
Display and follow application logs with filtering options.

**Usage:**
```bash
[CLI_TOOL_NAME] logs [SERVICE] [OPTIONS]
```

**Arguments:**
- `SERVICE` (string, optional) - Specific service to show logs for

**Options:**
- `-f, --follow` - Follow log output in real-time
- `-n, --lines <number>` - Number of lines to show (default: 100)
- `--since <time>` - Show logs since timestamp (e.g., "2h", "2025-01-15")
- `--level <level>` - Filter by log level (debug, info, warn, error)
- `--grep <pattern>` - Filter logs by pattern
- `--no-color` - Disable colored output

**Examples:**
```bash
# Show recent logs
[CLI_TOOL_NAME] logs

# Follow logs for specific service
[CLI_TOOL_NAME] logs api --follow

# Show error logs from last 2 hours
[CLI_TOOL_NAME] logs --level error --since 2h

# Filter logs by pattern
[CLI_TOOL_NAME] logs --grep "authentication"
```

---

### Utility Commands

#### `config` - Manage Configuration
View and modify CLI configuration settings.

**Usage:**
```bash
[CLI_TOOL_NAME] config <SUBCOMMAND> [OPTIONS]
```

**Subcommands:**
- `list` - Show all configuration values
- `get <key>` - Get specific configuration value
- `set <key> <value>` - Set configuration value
- `unset <key>` - Remove configuration value
- `reset` - Reset to default configuration
- `edit` - Open configuration in editor

**Options:**
- `-g, --global` - Operate on global configuration
- `-l, --local` - Operate on local project configuration
- `--json` - Output in JSON format

**Examples:**
```bash
# List all configuration
[CLI_TOOL_NAME] config list

# Set configuration value
[CLI_TOOL_NAME] config set output.format table

# Get specific value
[CLI_TOOL_NAME] config get api.endpoint

# Edit configuration interactively
[CLI_TOOL_NAME] config edit
```

---

#### `version` - Show Version Information
Display version information and build details.

**Usage:**
```bash
[CLI_TOOL_NAME] version [OPTIONS]
```

**Options:**
- `--short` - Show only version number
- `--json` - Output in JSON format
- `--check` - Check for updates

**Examples:**
```bash
# Show full version information
[CLI_TOOL_NAME] version

# Show only version number
[CLI_TOOL_NAME] version --short

# Check for updates
[CLI_TOOL_NAME] version --check
```

---

## 🔧 Global Options

These options are available for all commands:

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help information |
| `-v, --verbose` | Enable verbose output |
| `-q, --quiet` | Suppress non-essential output |
| `--no-color` | Disable colored output |
| `--config <file>` | Use specific configuration file |
| `--log-level <level>` | Set logging level (debug, info, warn, error) |
| `--output <format>` | Output format (table, json, yaml, plain) |
| `--dry-run` | Show what would happen without making changes |
| `--version` | Show version information |

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `[CLI_TOOL_NAME]_CONFIG_PATH` | Configuration file path | `~/.config/[CLI_TOOL_NAME]` |
| `[CLI_TOOL_NAME]_LOG_LEVEL` | Default log level | `info` |
| `[CLI_TOOL_NAME]_OUTPUT_FORMAT` | Default output format | `table` |
| `[CLI_TOOL_NAME]_API_ENDPOINT` | API endpoint URL | `https://api.example.com` |
| `NO_COLOR` | Disable colored output | (unset) |
| `DEBUG` | Enable debug mode | (unset) |

---

## 💡 Usage Examples

### Common Workflows

#### Project Setup and Development
```bash
# Initialize new project
[CLI_TOOL_NAME] init my-app --template react

# Configure for development
[CLI_TOOL_NAME] config set env development

# Start development build with watch
[CLI_TOOL_NAME] build --watch --verbose

# Check project status
[CLI_TOOL_NAME] status --watch
```

#### Deployment Pipeline
```bash
# Build for production
[CLI_TOOL_NAME] build --env production --clean

# Run pre-deployment checks
[CLI_TOOL_NAME] status --format json | jq '.health'

# Deploy to staging
[CLI_TOOL_NAME] deploy staging --wait

# Deploy to production with confirmation
[CLI_TOOL_NAME] deploy production --force
```

#### Monitoring and Debugging
```bash
# Monitor application logs
[CLI_TOOL_NAME] logs --follow --level warn

# Check specific service status
[CLI_TOOL_NAME] status api --format json

# Debug configuration issues
[CLI_TOOL_NAME] config list --verbose
```

### Scripting and Automation

#### Bash Script Example
```bash
#!/bin/bash
set -e

# Build and deploy script
echo "Building application..."
[CLI_TOOL_NAME] build --env production

echo "Running health checks..."
if [CLI_TOOL_NAME] status --quiet; then
    echo "Deploying to production..."
    [CLI_TOOL_NAME] deploy production --wait
    echo "Deployment successful!"
else
    echo "Health checks failed, aborting deployment"
    exit 1
fi
```

#### CI/CD Integration
```yaml
# GitHub Actions example
- name: Build Application
  run: [CLI_TOOL_NAME] build --env production --no-color

- name: Deploy to Staging
  run: [CLI_TOOL_NAME] deploy staging --wait --no-color
  if: github.ref == 'refs/heads/main'
```

### Power User Tips

#### Aliases and Functions
```bash
# Useful aliases
alias [CLI_SHORT]='[CLI_TOOL_NAME]'
alias [CLI_SHORT]-dev='[CLI_TOOL_NAME] build --watch --verbose'
alias [CLI_SHORT]-prod='[CLI_TOOL_NAME] build --env production --clean'

# Bash function for quick deployment
deploy-quick() {
    [CLI_TOOL_NAME] build --env production && \
    [CLI_TOOL_NAME] deploy "$1" --wait
}
```

#### Output Processing
```bash
# Extract specific information with jq
[CLI_TOOL_NAME] status --format json | jq '.services[] | select(.status == "unhealthy")'

# Monitor deployment progress
[CLI_TOOL_NAME] deploy staging --format json | jq -r '.progress'

# Get configuration as environment variables
eval $([CLI_TOOL_NAME] config list --format env)
```

---

## 🛠️ Advanced Usage

### Configuration Management

#### Hierarchical Configuration
Configuration is loaded in this order (later values override earlier ones):
1. System-wide configuration (`/etc/[CLI_TOOL_NAME]/config.yaml`)
2. User configuration (`~/.config/[CLI_TOOL_NAME]/config.yaml`)
3. Project configuration (`./.[CLI_TOOL_NAME].yaml`)
4. Environment variables
5. Command-line flags

#### Configuration File Format
```yaml
# ~/.config/[CLI_TOOL_NAME]/config.yaml
api:
  endpoint: "https://api.example.com"
  timeout: 30s
  retries: 3

output:
  format: "table"
  color: true
  verbose: false

build:
  parallel_jobs: 4
  cache_enabled: true
  default_env: "development"

deploy:
  confirm_production: true
  rollback_on_failure: true
  health_check_timeout: 300s
```

### Plugin System

#### Installing Plugins
```bash
# Install plugin from registry
[CLI_TOOL_NAME] plugin install [PLUGIN_NAME]

# Install from URL
[CLI_TOOL_NAME] plugin install https://github.com/user/plugin

# List installed plugins
[CLI_TOOL_NAME] plugin list

# Update plugins
[CLI_TOOL_NAME] plugin update
```

#### Creating Custom Plugins
```bash
# Generate plugin template
[CLI_TOOL_NAME] plugin create my-plugin

# Plugin structure
my-plugin/
├── plugin.yaml      # Plugin metadata
├── commands/         # Command definitions
└── scripts/          # Implementation scripts
```

### Integration with Other Tools

#### Shell Completion
```bash
# Bash completion
echo 'source <([CLI_TOOL_NAME] completion bash)' >> ~/.bashrc

# Zsh completion
echo 'source <([CLI_TOOL_NAME] completion zsh)' >> ~/.zshrc

# Fish completion
[CLI_TOOL_NAME] completion fish > ~/.config/fish/completions/[CLI_TOOL_NAME].fish
```

#### Editor Integration
```bash
# Generate VS Code snippets
[CLI_TOOL_NAME] generate vscode-snippets > .vscode/[CLI_TOOL_NAME].code-snippets

# Generate Vim syntax
[CLI_TOOL_NAME] generate vim-syntax > ~/.vim/syntax/[CLI_TOOL_NAME].vim
```

---

## ❓ Troubleshooting

### Common Issues

#### Command Not Found
```bash
# Check if CLI is installed
which [CLI_TOOL_NAME]

# Check PATH
echo $PATH

# Reinstall if necessary
curl -L [INSTALL_URL] | bash
```

#### Permission Errors
```bash
# Check file permissions
ls -la ~/.config/[CLI_TOOL_NAME]/

# Fix permissions
chmod 600 ~/.config/[CLI_TOOL_NAME]/config.yaml

# Run with sudo if needed (not recommended)
sudo [CLI_TOOL_NAME] [COMMAND]
```

#### Configuration Issues
```bash
# Validate configuration
[CLI_TOOL_NAME] config validate

# Reset to defaults
[CLI_TOOL_NAME] config reset

# Check configuration precedence
[CLI_TOOL_NAME] config list --verbose
```

#### Network Connectivity
```bash
# Test API connectivity
[CLI_TOOL_NAME] status --verbose

# Check proxy settings
echo $HTTP_PROXY $HTTPS_PROXY

# Use different endpoint
[CLI_TOOL_NAME] config set api.endpoint https://backup-api.example.com
```

### Debug Mode

Enable debug mode for detailed troubleshooting:
```bash
# Environment variable
export DEBUG=1
[CLI_TOOL_NAME] [COMMAND]

# Command flag
[CLI_TOOL_NAME] [COMMAND] --log-level debug

# Configuration
[CLI_TOOL_NAME] config set log.level debug
```

### Getting Help

#### Built-in Help
```bash
# General help
[CLI_TOOL_NAME] --help

# Command-specific help
[CLI_TOOL_NAME] [COMMAND] --help

# List all commands
[CLI_TOOL_NAME] help

# Search help
[CLI_TOOL_NAME] help search [TERM]
```

#### Support Channels
- **Documentation:** [https://docs.example.com/[CLI_TOOL_NAME]](https://docs.example.com/[CLI_TOOL_NAME])
- **GitHub Issues:** [https://github.com/[ORG]/[CLI_TOOL_NAME]/issues](https://github.com/[ORG]/[CLI_TOOL_NAME]/issues)
- **Community Forum:** [https://community.example.com/[CLI_TOOL_NAME]](https://community.example.com/[CLI_TOOL_NAME])
- **Discord:** [https://discord.gg/[CLI_TOOL_NAME]](https://discord.gg/[CLI_TOOL_NAME])

---

## 📚 Additional Resources

### Documentation
- **[Getting Started Guide](./guides/getting-started.md)** - Comprehensive tutorial for new users
- **[API Reference](./api/reference.md)** - Complete API documentation
- **[Configuration Reference](./config/reference.md)** - All configuration options
- **[Plugin Development](./plugins/development.md)** - Guide for creating plugins

### Examples and Tutorials
- **[Example Projects](./examples/)** - Sample projects and configurations
- **[Video Tutorials](https://youtube.com/[CLI_TOOL_NAME])** - Step-by-step video guides
- **[Best Practices](./guides/best-practices.md)** - Recommended patterns and practices
- **[Migration Guide](./guides/migration.md)** - Upgrading from previous versions

### Community Resources
- **[Awesome [CLI_TOOL_NAME]](https://github.com/awesome-[CLI_TOOL_NAME])** - Curated list of resources
- **[Community Plugins](https://plugins.example.com)** - Plugin registry and marketplace
- **[Blog](https://blog.example.com/[CLI_TOOL_NAME])** - Latest news and updates
- **[Changelog](./CHANGELOG.md)** - Version history and release notes

### Development
- **[Contributing Guide](./CONTRIBUTING.md)** - How to contribute to the project
- **[Development Setup](./docs/development.md)** - Setting up development environment
- **[Architecture Overview](./docs/architecture.md)** - System design and architecture
- **[Release Process](./docs/releases.md)** - How releases are managed

---

## 📞 Support & Feedback

### Reporting Issues
When reporting issues, please include:
- CLI version (`[CLI_TOOL_NAME] version`)
- Operating system and version
- Complete command that failed
- Full error message and stack trace
- Configuration file (with sensitive data removed)

### Feature Requests
We welcome feature requests! Please:
- Check existing issues first
- Describe the use case clearly
- Explain why the feature would be valuable
- Provide examples of how it would work

### Contributing
We love contributions! See our [Contributing Guide](./CONTRIBUTING.md) for:
- Code style guidelines
- Development setup instructions
- Pull request process
- Community guidelines

---

*This CLI reference is automatically updated with each release. For the most current information, run `[CLI_TOOL_NAME] --help` or visit our [online documentation](https://docs.example.com/[CLI_TOOL_NAME]).*

---

**Last Updated:** [TIMESTAMP]  
**CLI Version:** [CLI_VERSION]  
**Documentation Version:** [DOC_VERSION]
