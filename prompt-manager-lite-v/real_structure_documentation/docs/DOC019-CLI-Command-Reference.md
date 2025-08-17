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

[CLI_TOOL_NAME] is a powerful command-line interface designed to streamline [PRIMARY_PURPOSE]. Built with modern CLI design principles, it provides an intuitive, efficient, and robust experience for [TARGET_USERS].

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
# [PACKAGE_MANAGER_1] ([PLATFORM_1])
[INSTALL_COMMAND_1]

# [PACKAGE_MANAGER_2] ([PLATFORM_2])
[INSTALL_COMMAND_2]

# [PACKAGE_MANAGER_3] ([PLATFORM_3])
[INSTALL_COMMAND_3]

# [PACKAGE_MANAGER_4] ([PLATFORM_4])
[INSTALL_COMMAND_4]

# [PACKAGE_MANAGER_5] ([PLATFORM_5])
[INSTALL_COMMAND_5]
```

#### Direct Download
```bash
# Download latest release
curl -L [DOWNLOAD_URL] -o [CLI_TOOL_NAME]
chmod +x [CLI_TOOL_NAME]
sudo mv [CLI_TOOL_NAME] [INSTALL_PATH]
```

### Quick Start

```bash
# Check installation
[CLI_TOOL_NAME] --version

# Get help
[CLI_TOOL_NAME] --help

# Run your first command
[CLI_TOOL_NAME] [BASIC_COMMAND_EXAMPLE]

# Explore available commands
[CLI_TOOL_NAME] help
```

### Configuration

#### Global Configuration
```bash
# Set global configuration
[CLI_TOOL_NAME] config set [CONFIG_KEY] [CONFIG_VALUE]

# View current configuration
[CLI_TOOL_NAME] config list

# Reset to defaults
[CLI_TOOL_NAME] config reset
```

#### Environment Variables
```bash
# Common environment variables
export [CLI_TOOL_NAME]_CONFIG_PATH="[CONFIG_PATH]"
export [CLI_TOOL_NAME]_LOG_LEVEL="[LOG_LEVEL]"
export [CLI_TOOL_NAME]_OUTPUT_FORMAT="[OUTPUT_FORMAT]"
export NO_COLOR=1  # Disable colored output
```

---

## 📖 Command Reference

### Core Commands

#### `init` - Initialize New Project
Initialize a new project with default configuration and structure.

**Usage:**
```bash
[CLI_TOOL_NAME] init [PROJECT_NAME_PLACEHOLDER] [OPTIONS]
```

**Arguments:**
- `[PROJECT_NAME_ARG]` (string, optional) - [PROJECT_NAME_DESCRIPTION]

**Options:**
- `[OPTION_1_FLAG], --[OPTION_1_LONG] <[OPTION_1_VALUE]>` - [OPTION_1_DESCRIPTION]
- `[OPTION_2_FLAG], --[OPTION_2_LONG]` - [OPTION_2_DESCRIPTION]
- `[OPTION_3_FLAG], --[OPTION_3_LONG]` - [OPTION_3_DESCRIPTION]
- `--[OPTION_4_LONG]` - [OPTION_4_DESCRIPTION]

**Examples:**
```bash
# [EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] init

# [EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] init [EXAMPLE_PROJECT_NAME] --[EXAMPLE_OPTION] [EXAMPLE_VALUE]

# [EXAMPLE_3_DESCRIPTION]
[CLI_TOOL_NAME] init --[EXAMPLE_INTERACTIVE_FLAG]

# [EXAMPLE_4_DESCRIPTION]
[CLI_TOOL_NAME] init --[EXAMPLE_DRY_RUN_FLAG]
```

**Exit Codes:**
- `[EXIT_CODE_1]` - [EXIT_CODE_1_DESCRIPTION]
- `[EXIT_CODE_2]` - [EXIT_CODE_2_DESCRIPTION]
- `[EXIT_CODE_3]` - [EXIT_CODE_3_DESCRIPTION]

---

#### `build` - Build Project
Compile and build the project according to configuration.

**Usage:**
```bash
[CLI_TOOL_NAME] build [TARGET_PLACEHOLDER] [OPTIONS]
```

**Arguments:**
- `[TARGET_ARG]` (string, optional) - [TARGET_DESCRIPTION]

**Options:**
- `[BUILD_OPTION_1_FLAG], --[BUILD_OPTION_1_LONG] <[BUILD_OPTION_1_VALUE]>` - [BUILD_OPTION_1_DESCRIPTION]
- `[BUILD_OPTION_2_FLAG], --[BUILD_OPTION_2_LONG]` - [BUILD_OPTION_2_DESCRIPTION]
- `[BUILD_OPTION_3_FLAG], --[BUILD_OPTION_3_LONG]` - [BUILD_OPTION_3_DESCRIPTION]
- `[BUILD_OPTION_4_FLAG], --[BUILD_OPTION_4_LONG]` - [BUILD_OPTION_4_DESCRIPTION]
- `[BUILD_OPTION_5_FLAG], --[BUILD_OPTION_5_LONG] <[BUILD_OPTION_5_VALUE]>` - [BUILD_OPTION_5_DESCRIPTION]
- `--[BUILD_OPTION_6_LONG]` - [BUILD_OPTION_6_DESCRIPTION]

**Examples:**
```bash
# [BUILD_EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] build

# [BUILD_EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] build --[BUILD_EXAMPLE_2_OPTION_1] [BUILD_EXAMPLE_2_VALUE] --[BUILD_EXAMPLE_2_OPTION_2]

# [BUILD_EXAMPLE_3_DESCRIPTION]
[CLI_TOOL_NAME] build --[BUILD_EXAMPLE_3_OPTION_1] --[BUILD_EXAMPLE_3_OPTION_2]

# [BUILD_EXAMPLE_4_DESCRIPTION]
[CLI_TOOL_NAME] build [BUILD_EXAMPLE_4_TARGET] --[BUILD_EXAMPLE_4_OPTION] [BUILD_EXAMPLE_4_VALUE]
```

**Exit Codes:**
- `[BUILD_EXIT_CODE_1]` - [BUILD_EXIT_CODE_1_DESCRIPTION]
- `[BUILD_EXIT_CODE_2]` - [BUILD_EXIT_CODE_2_DESCRIPTION]
- `[BUILD_EXIT_CODE_3]` - [BUILD_EXIT_CODE_3_DESCRIPTION]

---

#### `deploy` - Deploy Application
Deploy the built application to specified environment.

**Usage:**
```bash
[CLI_TOOL_NAME] deploy [ENVIRONMENT_PLACEHOLDER] [OPTIONS]
```

**Arguments:**
- `[ENVIRONMENT_ARG]` (string, required) - [ENVIRONMENT_DESCRIPTION]

**Options:**
- `[DEPLOY_OPTION_1_FLAG], --[DEPLOY_OPTION_1_LONG] <[DEPLOY_OPTION_1_VALUE]>` - [DEPLOY_OPTION_1_DESCRIPTION]
- `[DEPLOY_OPTION_2_FLAG], --[DEPLOY_OPTION_2_LONG]` - [DEPLOY_OPTION_2_DESCRIPTION]
- `[DEPLOY_OPTION_3_FLAG], --[DEPLOY_OPTION_3_LONG]` - [DEPLOY_OPTION_3_DESCRIPTION]
- `--[DEPLOY_OPTION_4_LONG]` - [DEPLOY_OPTION_4_DESCRIPTION]
- `--[DEPLOY_OPTION_5_LONG]` - [DEPLOY_OPTION_5_DESCRIPTION]
- `--[DEPLOY_OPTION_6_LONG] <[DEPLOY_OPTION_6_VALUE]>` - [DEPLOY_OPTION_6_DESCRIPTION]

**Examples:**
```bash
# [DEPLOY_EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] deploy [DEPLOY_EXAMPLE_1_ENV]

# [DEPLOY_EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] deploy [DEPLOY_EXAMPLE_2_ENV] --[DEPLOY_EXAMPLE_2_OPTION]

# [DEPLOY_EXAMPLE_3_DESCRIPTION]
[CLI_TOOL_NAME] deploy [DEPLOY_EXAMPLE_3_ENV] --[DEPLOY_EXAMPLE_3_OPTION]

# [DEPLOY_EXAMPLE_4_DESCRIPTION]
[CLI_TOOL_NAME] deploy [DEPLOY_EXAMPLE_4_ENV] --[DEPLOY_EXAMPLE_4_OPTION]
```

**Exit Codes:**
- `[DEPLOY_EXIT_CODE_1]` - [DEPLOY_EXIT_CODE_1_DESCRIPTION]
- `[DEPLOY_EXIT_CODE_2]` - [DEPLOY_EXIT_CODE_2_DESCRIPTION]
- `[DEPLOY_EXIT_CODE_3]` - [DEPLOY_EXIT_CODE_3_DESCRIPTION]

---

### Management Commands

#### `status` - Show Project Status
Display current project status, health, and metrics.

**Usage:**
```bash
[CLI_TOOL_NAME] status [COMPONENT_PLACEHOLDER] [OPTIONS]
```

**Arguments:**
- `[COMPONENT_ARG]` (string, optional) - [COMPONENT_DESCRIPTION]

**Options:**
- `[STATUS_OPTION_1_FLAG], --[STATUS_OPTION_1_LONG] <[STATUS_OPTION_1_VALUE]>` - [STATUS_OPTION_1_DESCRIPTION]
- `[STATUS_OPTION_2_FLAG], --[STATUS_OPTION_2_LONG]` - [STATUS_OPTION_2_DESCRIPTION]
- `--[STATUS_OPTION_3_LONG] <[STATUS_OPTION_3_VALUE]>` - [STATUS_OPTION_3_DESCRIPTION]
- `[STATUS_OPTION_4_FLAG], --[STATUS_OPTION_4_LONG]` - [STATUS_OPTION_4_DESCRIPTION]

**Examples:**
```bash
# [STATUS_EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] status

# [STATUS_EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] status [STATUS_EXAMPLE_2_COMPONENT] --[STATUS_EXAMPLE_2_OPTION]

# [STATUS_EXAMPLE_3_DESCRIPTION]
[CLI_TOOL_NAME] status --[STATUS_EXAMPLE_3_OPTION] [STATUS_EXAMPLE_3_VALUE]

# [STATUS_EXAMPLE_4_DESCRIPTION]
[CLI_TOOL_NAME] status --[STATUS_EXAMPLE_4_OPTION]
```

---

#### `logs` - View Application Logs
Display and follow application logs with filtering options.

**Usage:**
```bash
[CLI_TOOL_NAME] logs [SERVICE_PLACEHOLDER] [OPTIONS]
```

**Arguments:**
- `[SERVICE_ARG]` (string, optional) - [SERVICE_DESCRIPTION]

**Options:**
- `[LOGS_OPTION_1_FLAG], --[LOGS_OPTION_1_LONG]` - [LOGS_OPTION_1_DESCRIPTION]
- `[LOGS_OPTION_2_FLAG], --[LOGS_OPTION_2_LONG] <[LOGS_OPTION_2_VALUE]>` - [LOGS_OPTION_2_DESCRIPTION]
- `--[LOGS_OPTION_3_LONG] <[LOGS_OPTION_3_VALUE]>` - [LOGS_OPTION_3_DESCRIPTION]
- `--[LOGS_OPTION_4_LONG] <[LOGS_OPTION_4_VALUE]>` - [LOGS_OPTION_4_DESCRIPTION]
- `--[LOGS_OPTION_5_LONG] <[LOGS_OPTION_5_VALUE]>` - [LOGS_OPTION_5_DESCRIPTION]
- `--[LOGS_OPTION_6_LONG]` - [LOGS_OPTION_6_DESCRIPTION]

**Examples:**
```bash
# [LOGS_EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] logs

# [LOGS_EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] logs [LOGS_EXAMPLE_2_SERVICE] --[LOGS_EXAMPLE_2_OPTION]

# [LOGS_EXAMPLE_3_DESCRIPTION]
[CLI_TOOL_NAME] logs --[LOGS_EXAMPLE_3_OPTION_1] [LOGS_EXAMPLE_3_VALUE_1] --[LOGS_EXAMPLE_3_OPTION_2] [LOGS_EXAMPLE_3_VALUE_2]

# [LOGS_EXAMPLE_4_DESCRIPTION]
[CLI_TOOL_NAME] logs --[LOGS_EXAMPLE_4_OPTION] "[LOGS_EXAMPLE_4_PATTERN]"
```

---

### Utility Commands

#### `config` - Manage Configuration
View and modify CLI configuration settings.

**Usage:**
```bash
[CLI_TOOL_NAME] config <[SUBCOMMAND_PLACEHOLDER]> [OPTIONS]
```

**Subcommands:**
- `[SUBCOMMAND_1]` - [SUBCOMMAND_1_DESCRIPTION]
- `[SUBCOMMAND_2] <[SUBCOMMAND_2_ARG]>` - [SUBCOMMAND_2_DESCRIPTION]
- `[SUBCOMMAND_3] <[SUBCOMMAND_3_ARG_1]> <[SUBCOMMAND_3_ARG_2]>` - [SUBCOMMAND_3_DESCRIPTION]
- `[SUBCOMMAND_4] <[SUBCOMMAND_4_ARG]>` - [SUBCOMMAND_4_DESCRIPTION]
- `[SUBCOMMAND_5]` - [SUBCOMMAND_5_DESCRIPTION]
- `[SUBCOMMAND_6]` - [SUBCOMMAND_6_DESCRIPTION]

**Options:**
- `[CONFIG_OPTION_1_FLAG], --[CONFIG_OPTION_1_LONG]` - [CONFIG_OPTION_1_DESCRIPTION]
- `[CONFIG_OPTION_2_FLAG], --[CONFIG_OPTION_2_LONG]` - [CONFIG_OPTION_2_DESCRIPTION]
- `--[CONFIG_OPTION_3_LONG]` - [CONFIG_OPTION_3_DESCRIPTION]

**Examples:**
```bash
# [CONFIG_EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] config [CONFIG_EXAMPLE_1_SUBCOMMAND]

# [CONFIG_EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] config [CONFIG_EXAMPLE_2_SUBCOMMAND] [CONFIG_EXAMPLE_2_KEY] [CONFIG_EXAMPLE_2_VALUE]

# [CONFIG_EXAMPLE_3_DESCRIPTION]
[CLI_TOOL_NAME] config [CONFIG_EXAMPLE_3_SUBCOMMAND] [CONFIG_EXAMPLE_3_KEY]

# [CONFIG_EXAMPLE_4_DESCRIPTION]
[CLI_TOOL_NAME] config [CONFIG_EXAMPLE_4_SUBCOMMAND]
```

---

#### `version` - Show Version Information
Display version information and build details.

**Usage:**
```bash
[CLI_TOOL_NAME] version [OPTIONS]
```

**Options:**
- `--[VERSION_OPTION_1_LONG]` - [VERSION_OPTION_1_DESCRIPTION]
- `--[VERSION_OPTION_2_LONG]` - [VERSION_OPTION_2_DESCRIPTION]
- `--[VERSION_OPTION_3_LONG]` - [VERSION_OPTION_3_DESCRIPTION]

**Examples:**
```bash
# [VERSION_EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] version

# [VERSION_EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] version --[VERSION_EXAMPLE_2_OPTION]

# [VERSION_EXAMPLE_3_DESCRIPTION]
[CLI_TOOL_NAME] version --[VERSION_EXAMPLE_3_OPTION]
```

---

## 🔧 Global Options

These options are available for all commands:

| Option | Description |
|--------|-------------|
| `[GLOBAL_OPTION_1_FLAG], --[GLOBAL_OPTION_1_LONG]` | [GLOBAL_OPTION_1_DESCRIPTION] |
| `[GLOBAL_OPTION_2_FLAG], --[GLOBAL_OPTION_2_LONG]` | [GLOBAL_OPTION_2_DESCRIPTION] |
| `[GLOBAL_OPTION_3_FLAG], --[GLOBAL_OPTION_3_LONG]` | [GLOBAL_OPTION_3_DESCRIPTION] |
| `--[GLOBAL_OPTION_4_LONG]` | [GLOBAL_OPTION_4_DESCRIPTION] |
| `--[GLOBAL_OPTION_5_LONG] <[GLOBAL_OPTION_5_VALUE]>` | [GLOBAL_OPTION_5_DESCRIPTION] |
| `--[GLOBAL_OPTION_6_LONG] <[GLOBAL_OPTION_6_VALUE]>` | [GLOBAL_OPTION_6_DESCRIPTION] |
| `--[GLOBAL_OPTION_7_LONG] <[GLOBAL_OPTION_7_VALUE]>` | [GLOBAL_OPTION_7_DESCRIPTION] |
| `--[GLOBAL_OPTION_8_LONG]` | [GLOBAL_OPTION_8_DESCRIPTION] |
| `--[GLOBAL_OPTION_9_LONG]` | [GLOBAL_OPTION_9_DESCRIPTION] |

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `[ENV_VAR_1]` | [ENV_VAR_1_DESCRIPTION] | `[ENV_VAR_1_DEFAULT]` |
| `[ENV_VAR_2]` | [ENV_VAR_2_DESCRIPTION] | `[ENV_VAR_2_DEFAULT]` |
| `[ENV_VAR_3]` | [ENV_VAR_3_DESCRIPTION] | `[ENV_VAR_3_DEFAULT]` |
| `[ENV_VAR_4]` | [ENV_VAR_4_DESCRIPTION] | `[ENV_VAR_4_DEFAULT]` |
| `[ENV_VAR_5]` | [ENV_VAR_5_DESCRIPTION] | `[ENV_VAR_5_DEFAULT]` |
| `[ENV_VAR_6]` | [ENV_VAR_6_DESCRIPTION] | `[ENV_VAR_6_DEFAULT]` |

---

## 💡 Usage Examples

### Common Workflows

#### Project Setup and Development
```bash
# [WORKFLOW_1_STEP_1_DESCRIPTION]
[CLI_TOOL_NAME] init [WORKFLOW_1_PROJECT_NAME] --[WORKFLOW_1_OPTION] [WORKFLOW_1_VALUE]

# [WORKFLOW_1_STEP_2_DESCRIPTION]
[CLI_TOOL_NAME] config set [WORKFLOW_1_CONFIG_KEY] [WORKFLOW_1_CONFIG_VALUE]

# [WORKFLOW_1_STEP_3_DESCRIPTION]
[CLI_TOOL_NAME] build --[WORKFLOW_1_BUILD_OPTION_1] --[WORKFLOW_1_BUILD_OPTION_2]

# [WORKFLOW_1_STEP_4_DESCRIPTION]
[CLI_TOOL_NAME] status --[WORKFLOW_1_STATUS_OPTION]
```

#### Deployment Pipeline
```bash
# [WORKFLOW_2_STEP_1_DESCRIPTION]
[CLI_TOOL_NAME] build --[WORKFLOW_2_BUILD_OPTION_1] [WORKFLOW_2_BUILD_VALUE] --[WORKFLOW_2_BUILD_OPTION_2]

# [WORKFLOW_2_STEP_2_DESCRIPTION]
[CLI_TOOL_NAME] status --[WORKFLOW_2_STATUS_OPTION] [WORKFLOW_2_STATUS_VALUE] | [WORKFLOW_2_PIPE_COMMAND]

# [WORKFLOW_2_STEP_3_DESCRIPTION]
[CLI_TOOL_NAME] deploy [WORKFLOW_2_ENV_1] --[WORKFLOW_2_DEPLOY_OPTION_1]

# [WORKFLOW_2_STEP_4_DESCRIPTION]
[CLI_TOOL_NAME] deploy [WORKFLOW_2_ENV_2] --[WORKFLOW_2_DEPLOY_OPTION_2]
```

#### Monitoring and Debugging
```bash
# [WORKFLOW_3_STEP_1_DESCRIPTION]
[CLI_TOOL_NAME] logs --[WORKFLOW_3_LOGS_OPTION_1] --[WORKFLOW_3_LOGS_OPTION_2] [WORKFLOW_3_LOGS_VALUE]

# [WORKFLOW_3_STEP_2_DESCRIPTION]
[CLI_TOOL_NAME] status [WORKFLOW_3_SERVICE] --[WORKFLOW_3_STATUS_OPTION] [WORKFLOW_3_STATUS_VALUE]

# [WORKFLOW_3_STEP_3_DESCRIPTION]
[CLI_TOOL_NAME] config [WORKFLOW_3_CONFIG_SUBCOMMAND] --[WORKFLOW_3_CONFIG_OPTION]
```

### Scripting and Automation

#### Bash Script Example
```bash
#!/bin/bash
set -e

# [SCRIPT_DESCRIPTION]
echo "[SCRIPT_STEP_1_MESSAGE]"
[CLI_TOOL_NAME] build --[SCRIPT_BUILD_OPTION] [SCRIPT_BUILD_VALUE]

echo "[SCRIPT_STEP_2_MESSAGE]"
if [CLI_TOOL_NAME] status --[SCRIPT_STATUS_OPTION]; then
    echo "[SCRIPT_SUCCESS_MESSAGE]"
    [CLI_TOOL_NAME] deploy [SCRIPT_DEPLOY_ENV] --[SCRIPT_DEPLOY_OPTION]
    echo "[SCRIPT_COMPLETION_MESSAGE]"
else
    echo "[SCRIPT_FAILURE_MESSAGE]"
    exit 1
fi
```

#### CI/CD Integration
```yaml
# [CI_CD_PLATFORM] example
- name: [CI_CD_STEP_1_NAME]
  run: [CLI_TOOL_NAME] build --[CI_CD_BUILD_OPTION_1] [CI_CD_BUILD_VALUE] --[CI_CD_BUILD_OPTION_2]

- name: [CI_CD_STEP_2_NAME]
  run: [CLI_TOOL_NAME] deploy [CI_CD_DEPLOY_ENV] --[CI_CD_DEPLOY_OPTION_1] --[CI_CD_DEPLOY_OPTION_2]
  if: [CI_CD_CONDITION]
```

### Power User Tips

#### Aliases and Functions
```bash
# [ALIASES_SECTION_TITLE]
alias [ALIAS_1]='[CLI_TOOL_NAME]'
alias [ALIAS_2]='[CLI_TOOL_NAME] [ALIAS_2_COMMAND] --[ALIAS_2_OPTION_1] --[ALIAS_2_OPTION_2]'
alias [ALIAS_3]='[CLI_TOOL_NAME] [ALIAS_3_COMMAND] --[ALIAS_3_OPTION_1] [ALIAS_3_VALUE] --[ALIAS_3_OPTION_2]'

# [FUNCTION_DESCRIPTION]
[FUNCTION_NAME]() {
    [CLI_TOOL_NAME] [FUNCTION_COMMAND_1] --[FUNCTION_OPTION_1] [FUNCTION_VALUE] && \
    [CLI_TOOL_NAME] [FUNCTION_COMMAND_2] "$1" --[FUNCTION_OPTION_2]
}
```

#### Output Processing
```bash
# [OUTPUT_EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] status --[OUTPUT_OPTION_1] [OUTPUT_VALUE_1] | [OUTPUT_PROCESSOR_1] '[OUTPUT_FILTER_1]'

# [OUTPUT_EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] deploy [OUTPUT_ENV] --[OUTPUT_OPTION_2] [OUTPUT_VALUE_2] | [OUTPUT_PROCESSOR_2] '[OUTPUT_FILTER_2]'

# [OUTPUT_EXAMPLE_3_DESCRIPTION]
eval $([CLI_TOOL_NAME] config [OUTPUT_SUBCOMMAND] --[OUTPUT_OPTION_3] [OUTPUT_VALUE_3])
```

---

## 🛠️ Advanced Usage

### Configuration Management

#### Hierarchical Configuration
Configuration is loaded in this order (later values override earlier ones):
1. [CONFIG_LEVEL_1] (`[CONFIG_PATH_1]`)
2. [CONFIG_LEVEL_2] (`[CONFIG_PATH_2]`)
3. [CONFIG_LEVEL_3] (`[CONFIG_PATH_3]`)
4. [CONFIG_LEVEL_4]
5. [CONFIG_LEVEL_5]

#### Configuration File Format
```yaml
# [CONFIG_FILE_PATH]
[CONFIG_SECTION_1]:
  [CONFIG_KEY_1]: "[CONFIG_VALUE_1]"
  [CONFIG_KEY_2]: [CONFIG_VALUE_2]
  [CONFIG_KEY_3]: [CONFIG_VALUE_3]

[CONFIG_SECTION_2]:
  [CONFIG_KEY_4]: "[CONFIG_VALUE_4]"
  [CONFIG_KEY_5]: [CONFIG_VALUE_5]
  [CONFIG_KEY_6]: [CONFIG_VALUE_6]

[CONFIG_SECTION_3]:
  [CONFIG_KEY_7]: [CONFIG_VALUE_7]
  [CONFIG_KEY_8]: [CONFIG_VALUE_8]
  [CONFIG_KEY_9]: "[CONFIG_VALUE_9]"

[CONFIG_SECTION_4]:
  [CONFIG_KEY_10]: [CONFIG_VALUE_10]
  [CONFIG_KEY_11]: [CONFIG_VALUE_11]
  [CONFIG_KEY_12]: [CONFIG_VALUE_12]
```

### Plugin System

#### Installing Plugins
```bash
# [PLUGIN_EXAMPLE_1_DESCRIPTION]
[CLI_TOOL_NAME] plugin install [PLUGIN_NAME_PLACEHOLDER]

# [PLUGIN_EXAMPLE_2_DESCRIPTION]
[CLI_TOOL_NAME] plugin install [PLUGIN_URL_PLACEHOLDER]

# [PLUGIN_EXAMPLE_3_DESCRIPTION]
[CLI_TOOL_NAME] plugin list

# [PLUGIN_EXAMPLE_4_DESCRIPTION]
[CLI_TOOL_NAME] plugin update
```

#### Creating Custom Plugins
```bash
# [PLUGIN_CREATE_DESCRIPTION]
[CLI_TOOL_NAME] plugin create [PLUGIN_CREATE_NAME]

# [PLUGIN_STRUCTURE_TITLE]
[PLUGIN_DIRECTORY_NAME]/
├── [PLUGIN_FILE_1]      # [PLUGIN_FILE_1_DESCRIPTION]
├── [PLUGIN_DIR_1]/         # [PLUGIN_DIR_1_DESCRIPTION]
└── [PLUGIN_DIR_2]/          # [PLUGIN_DIR_2_DESCRIPTION]
```

### Integration with Other Tools

#### Shell Completion
```bash
# [COMPLETION_1_DESCRIPTION]
echo 'source <([CLI_TOOL_NAME] completion [SHELL_1])' >> [COMPLETION_1_FILE]

# [COMPLETION_2_DESCRIPTION]
echo 'source <([CLI_TOOL_NAME] completion [SHELL_2])' >> [COMPLETION_2_FILE]

# [COMPLETION_3_DESCRIPTION]
[CLI_TOOL_NAME] completion [SHELL_3] > [COMPLETION_3_PATH]
```

#### Editor Integration
```bash
# [EDITOR_INTEGRATION_1_DESCRIPTION]
[CLI_TOOL_NAME] generate [EDITOR_1_TYPE] > [EDITOR_1_OUTPUT_PATH]

# [EDITOR_INTEGRATION_2_DESCRIPTION]
[CLI_TOOL_NAME] generate [EDITOR_2_TYPE] > [EDITOR_2_OUTPUT_PATH]
```

---

## ❓ Troubleshooting

### Common Issues

#### Command Not Found
```bash
# [TROUBLESHOOT_1_DESCRIPTION]
which [CLI_TOOL_NAME]

# [TROUBLESHOOT_2_DESCRIPTION]
echo $PATH

# [TROUBLESHOOT_3_DESCRIPTION]
curl -L [REINSTALL_URL] | bash
```

#### Permission Errors
```bash
# [PERMISSION_CHECK_DESCRIPTION]
ls -la [PERMISSION_CHECK_PATH]

# [PERMISSION_FIX_DESCRIPTION]
chmod [PERMISSION_MODE] [PERMISSION_FILE_PATH]

# [SUDO_USAGE_DESCRIPTION]
sudo [CLI_TOOL_NAME] [COMMAND_PLACEHOLDER]
```

#### Configuration Issues
```bash
# [CONFIG_VALIDATE_DESCRIPTION]
[CLI_TOOL_NAME] config validate

# [CONFIG_RESET_DESCRIPTION]
[CLI_TOOL_NAME] config reset

# [CONFIG_PRECEDENCE_DESCRIPTION]
[CLI_TOOL_NAME] config list --[CONFIG_VERBOSE_OPTION]
```

#### Network Connectivity
```bash
# [NETWORK_TEST_DESCRIPTION]
[CLI_TOOL_NAME] status --[NETWORK_VERBOSE_OPTION]

# [PROXY_CHECK_DESCRIPTION]
echo $[PROXY_VAR_1] $[PROXY_VAR_2]

# [ENDPOINT_CHANGE_DESCRIPTION]
[CLI_TOOL_NAME] config set [ENDPOINT_CONFIG_KEY] [BACKUP_ENDPOINT_URL]
```

### Debug Mode

Enable debug mode for detailed troubleshooting:
```bash
# [DEBUG_ENV_DESCRIPTION]
export [DEBUG_VAR]=[DEBUG_VALUE]
[CLI_TOOL_NAME] [COMMAND_PLACEHOLDER]

# [DEBUG_FLAG_DESCRIPTION]
[CLI_TOOL_NAME] [COMMAND_PLACEHOLDER] --[DEBUG_OPTION] [DEBUG_LEVEL]

# [DEBUG_CONFIG_DESCRIPTION]
[CLI_TOOL_NAME] config set [DEBUG_CONFIG_KEY] [DEBUG_CONFIG_VALUE]
```

### Getting Help

#### Built-in Help
```bash
# [HELP_GENERAL_DESCRIPTION]
[CLI_TOOL_NAME] --help

# [HELP_COMMAND_DESCRIPTION]
[CLI_TOOL_NAME] [COMMAND_PLACEHOLDER] --help

# [HELP_LIST_DESCRIPTION]
[CLI_TOOL_NAME] help

# [HELP_SEARCH_DESCRIPTION]
[CLI_TOOL_NAME] help search [SEARCH_TERM]
```

#### Support Channels
- **[SUPPORT_CHANNEL_1]:** [[SUPPORT_URL_1]]([SUPPORT_URL_1])
- **[SUPPORT_CHANNEL_2]:** [[SUPPORT_URL_2]]([SUPPORT_URL_2])
- **[SUPPORT_CHANNEL_3]:** [[SUPPORT_URL_3]]([SUPPORT_URL_3])
- **[SUPPORT_CHANNEL_4]:** [[SUPPORT_URL_4]]([SUPPORT_URL_4])

---

## 📚 Additional Resources

### Documentation
- **[[GUIDE_1_TITLE]]([GUIDE_1_PATH])** - [GUIDE_1_DESCRIPTION]
- **[[GUIDE_2_TITLE]]([GUIDE_2_PATH])** - [GUIDE_2_DESCRIPTION]
- **[[GUIDE_3_TITLE]]([GUIDE_3_PATH])** - [GUIDE_3_DESCRIPTION]
- **[[GUIDE_4_TITLE]]([GUIDE_4_PATH])** - [GUIDE_4_DESCRIPTION]

### Examples and Tutorials
- **[[RESOURCE_1_TITLE]]([RESOURCE_1_PATH])** - [RESOURCE_1_DESCRIPTION]
- **[[RESOURCE_2_TITLE]]([RESOURCE_2_URL])** - [RESOURCE_2_DESCRIPTION]
- **[[RESOURCE_3_TITLE]]([RESOURCE_3_PATH])** - [RESOURCE_3_DESCRIPTION]
- **[[RESOURCE_4_TITLE]]([RESOURCE_4_PATH])** - [RESOURCE_4_DESCRIPTION]

### Community Resources
- **[[COMMUNITY_RESOURCE_1_TITLE]]([COMMUNITY_RESOURCE_1_URL])** - [COMMUNITY_RESOURCE_1_DESCRIPTION]
- **[[COMMUNITY_RESOURCE_2_TITLE]]([COMMUNITY_RESOURCE_2_URL])** - [COMMUNITY_RESOURCE_2_DESCRIPTION]
- **[[COMMUNITY_RESOURCE_3_TITLE]]([COMMUNITY_RESOURCE_3_URL])** - [COMMUNITY_RESOURCE_3_DESCRIPTION]
- **[[COMMUNITY_RESOURCE_4_TITLE]]([COMMUNITY_RESOURCE_4_PATH])** - [COMMUNITY_RESOURCE_4_DESCRIPTION]

### Development
- **[[DEV_RESOURCE_1_TITLE]]([DEV_RESOURCE_1_PATH])** - [DEV_RESOURCE_1_DESCRIPTION]
- **[[DEV_RESOURCE_2_TITLE]]([DEV_RESOURCE_2_PATH])** - [DEV_RESOURCE_2_DESCRIPTION]
- **[[DEV_RESOURCE_3_TITLE]]([DEV_RESOURCE_3_PATH])** - [DEV_RESOURCE_3_DESCRIPTION]
- **[[DEV_RESOURCE_4_TITLE]]([DEV_RESOURCE_4_PATH])** - [DEV_RESOURCE_4_DESCRIPTION]

---

## 📞 Support & Feedback

### Reporting Issues
When reporting issues, please include:
- [ISSUE_REQUIREMENT_1] (`[CLI_TOOL_NAME] version`)
- [ISSUE_REQUIREMENT_2]
- [ISSUE_REQUIREMENT_3]
- [ISSUE_REQUIREMENT_4]
- [ISSUE_REQUIREMENT_5]

### Feature Requests
We welcome feature requests! Please:
- [FEATURE_REQUEST_STEP_1]
- [FEATURE_REQUEST_STEP_2]
- [FEATURE_REQUEST_STEP_3]
- [FEATURE_REQUEST_STEP_4]

### Contributing
We love contributions! See our [[CONTRIBUTING_GUIDE_TITLE]]([CONTRIBUTING_GUIDE_PATH]) for:
- [CONTRIBUTING_ITEM_1]
- [CONTRIBUTING_ITEM_2]
- [CONTRIBUTING_ITEM_3]
- [CONTRIBUTING_ITEM_4]

---

*[FOOTER_NOTE_1] For the most current information, run `[CLI_TOOL_NAME] --help` or visit our [[ONLINE_DOCS_TITLE]]([ONLINE_DOCS_URL]).*

---

**[FOOTER_FIELD_1]:** [FOOTER_VALUE_1]  
**[FOOTER_FIELD_2]:** [FOOTER_VALUE_2]  
**[FOOTER_FIELD_3]:** [FOOTER_VALUE_3]
