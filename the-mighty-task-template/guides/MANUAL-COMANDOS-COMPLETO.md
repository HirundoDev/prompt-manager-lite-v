# Manual Completo de Comandos - The Mighty Task

**Versión:** 4.0 - Sistema de Guías Operacionales  
**Fecha:** 2025-08-26  
**Propósito:** Referencia completa de todos los comandos y scripts disponibles incluyendo gestión de guías operacionales  

---

## 📋 **Índice**

1. [Scripts Principales](#-scripts-principales)
2. [Comandos por Flujo de Trabajo](#-comandos-por-flujo-de-trabajo)
3. [Comandos de Diagnóstico y Mantenimiento](#-comandos-de-diagnóstico-y-mantenimiento)
4. [Parámetros Comunes](#-parámetros-comunes)
5. [Códigos de Salida](#-códigos-de-salida)
6. [Ejemplos de Uso Común](#-ejemplos-de-uso-común)
7. [Resolución de Problemas](#-resolución-de-problemas)

---

## 🛠️ **Scripts Principales**

### **1. generate-daily.py**

**Propósito:** Generar la estructura básica de trabajo diario con directorios y archivos iniciales.

#### **Comandos Disponibles**

```bash
# Generar sesión con tema específico y fecha actual
python scripts/generate-daily.py --theme "BACKEND-API-SETUP"

# Generar sesión con fecha específica
python scripts/generate-daily.py --theme "BACKEND-API-SETUP" --date "2025-01-22"

# Generar sesión automática (tema default + fecha actual)
python scripts/generate-daily.py --auto

# Listar todos los temas disponibles
python scripts/generate-daily.py --list-themes

# Forzar sobrescritura de sesión existente
python scripts/generate-daily.py --theme "API-DESIGN" --date "2025-01-22" --force

# Generar en modo silencioso
python scripts/generate-daily.py --theme "FRONTEND-COMPONENTS" --quiet

# Mostrar ayuda detallada
python scripts/generate-daily.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|---------|
| `--theme` | Tema de la sesión | ❌ | `BACKEND-API-SETUP` |
| `--date` | Fecha en formato YYYY-MM-DD | ❌ | `2025-01-22` |
| `--auto` | Modo automático con valores por defecto | ❌ | - |
| `--force` | Sobrescribir sesión existente | ❌ | - |
| `--quiet` | Modo silencioso | ❌ | - |
| `--list-themes` | Mostrar temas disponibles | ❌ | - |

#### **Lo que Genera**

- 📁 Directorio principal: `daily-work/YYYY-MM-DD_THEME/`
- 📄 Archivo principal: `pending-tasks-YYYY-MM-DD_THEME.md`
- 📁 Subdirectorios: `support-docs/`, `assets/screenshots/`, `assets/logs/`
- 📄 READMEs descriptivos para cada directorio
- 📊 Actualización del sistema de tracking `.tracking.json`

---

### **2. playbook-processor.py**

**Propósito:** Generar templates dinámicos basados en playbooks universales para una sesión específica.

#### **Comandos Disponibles**

```bash
# Procesar playbooks para sesión específica
python scripts/playbook-processor.py --date="2025-01-22" --theme="BACKEND-API-SETUP"

# Listar todos los playbooks disponibles
python scripts/playbook-processor.py --list-playbooks

# Escanear y mostrar información detallada de playbooks
python scripts/playbook-processor.py --scan-all

# Procesar solo playbooks específicos
python scripts/playbook-processor.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --playbooks="DOC006,DOC007"

# Generar templates en modo verbose
python scripts/playbook-processor.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --verbose

# Forzar regeneración de templates existentes
python scripts/playbook-processor.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --force

# Mostrar ayuda detallada
python scripts/playbook-processor.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|---------|
| `--date` | Fecha de la sesión | ✅ | `2025-01-22` |
| `--theme` | Tema de la sesión | ✅ | `BACKEND-API-SETUP` |
| `--playbooks` | Lista específica de playbooks | ❌ | `DOC006,DOC007` |
| `--force` | Forzar regeneración | ❌ | - |
| `--verbose` | Modo detallado | ❌ | - |
| `--list-playbooks` | Listar playbooks | ❌ | - |
| `--scan-all` | Escanear información detallada | ❌ | - |

#### **Lo que Genera**

- 📄 Templates en `support-docs/` basados en playbooks universales
- 📋 Estructuras con placeholders `[TECNOLOGÍA_ESPECÍFICA]`
- 🔗 Referencias a playbooks originales
- ⚙️ Decisiones técnicas estructuradas
- 📊 Actualización del tracking con templates generados

---

### **3. consistency-checker.py**

**Propósito:** Verificar la integridad y consistencia del sistema completo.

#### **Comandos Disponibles**

```bash
# Escaneo completo del sistema
python scripts/consistency-checker.py --scan-all

# Verificar sesión específica
python scripts/consistency-checker.py --check-session --date="2025-01-22" --theme="BACKEND-API-SETUP"

# Verificar solo el sistema de tracking
python scripts/consistency-checker.py --check-tracking

# Detectar archivos duplicados
python scripts/consistency-checker.py --check-duplicates

# Verificar estructura de directorios
python scripts/consistency-checker.py --check-structure

# Validar playbooks
python scripts/consistency-checker.py --check-playbooks

# Generar reporte detallado de consistencia
python scripts/consistency-checker.py --generate-report

# Modo reparación automática
python scripts/consistency-checker.py --auto-fix

# Verificación en modo verbose
python scripts/consistency-checker.py --scan-all --verbose

# Mostrar ayuda detallada
python scripts/consistency-checker.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|---------|
| `--scan-all` | Escaneo completo | ❌ | - |
| `--check-session` | Verificar sesión específica | ❌ | - |
| `--date` | Fecha de sesión a verificar | ❌ | `2025-01-22` |
| `--theme` | Tema de sesión a verificar | ❌ | `BACKEND-API-SETUP` |
| `--check-tracking` | Solo verificar tracking | ❌ | - |
| `--check-duplicates` | Solo detectar duplicados | ❌ | - |
| `--check-structure` | Solo verificar estructura | ❌ | - |
| `--check-playbooks` | Solo validar playbooks | ❌ | - |
| `--generate-report` | Generar reporte detallado | ❌ | - |
| `--auto-fix` | Reparación automática | ❌ | - |
| `--verbose` | Modo detallado | ❌ | - |

#### **Lo que Verifica**

- 📁 Estructura de directorios esperada
- 📄 Existencia de archivos críticos
- 📊 Integridad del archivo `.tracking.json`
- 🔗 Referencias válidas entre archivos
- 📚 Consistencia de playbooks
- 🔍 Detección de contenido duplicado
- ⚖️ Validación de formatos

---

### **4. report-generator.py**

**Propósito:** Generar reportes de progreso y métricas para sesiones específicas.

#### **Comandos Disponibles**

```bash
# Generar reporte básico para sesión
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP"

# Generar reporte en formato HTML
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --format html

# Generar reporte en formato Markdown
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --format markdown

# Incluir métricas detalladas
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --detailed

# Generar reporte con análisis de progreso
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --progress-analysis

# Especificar archivo de salida personalizado
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --output="custom-report.md"

# Generar reporte para múltiples sesiones
python scripts/report-generator.py --theme="BACKEND-API-SETUP" --all-sessions

# Mostrar ayuda detallada
python scripts/report-generator.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|---------|
| `--date` | Fecha de la sesión | ✅ | `2025-01-22` |
| `--theme` | Tema de la sesión | ✅ | `BACKEND-API-SETUP` |
| `--format` | Formato del reporte | ❌ | `html` o `markdown` |
| `--output` | Archivo de salida personalizado | ❌ | `custom-report.md` |
| `--detailed` | Incluir métricas detalladas | ❌ | - |
| `--progress-analysis` | Análisis de progreso | ❌ | - |
| `--all-sessions` | Procesar todas las sesiones del tema | ❌ | - |

#### **Lo que Genera**

- 📊 Métricas de progreso de tareas
- 📈 Estadísticas de completitud
- 📄 Análisis de templates utilizados
- 🎯 Identificación de áreas de mejora
- 📂 Reportes en `reports/` con timestamp

---

### **5. mission-resumer.py**

**Propósito:** Crear resúmenes ejecutivos consolidados por tema o proyecto.

#### **Comandos Disponibles**

```bash
# Generar resumen por tema específico (genera automáticamente en mission-resumes/)
python scripts/mission-resumer.py --theme="BACKEND"

# Fusionar sesiones de tema FRONTEND
python scripts/mission-resumer.py --theme="FRONTEND"

# Fusionar sesiones con tema API
python scripts/mission-resumer.py --theme="API"

# Con base path personalizado
python scripts/mission-resumer.py --theme="BACKEND" --base-path="/ruta/custom/proyecto"

# Mostrar ayuda detallada
python scripts/mission-resumer.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|---------|
| `--theme` | Tema a fusionar | ✅ | `BACKEND` |
| `--base-path` | Ruta base del proyecto | ❌ | `/ruta/proyecto` |

#### **Lo que Genera**

- 📚 **Playbooks fusionados** en `mission-resumes/DOCxxx-*.md`
- 📁 **Assets consolidados** en `mission-resumes/assets/`
- 📈 **Charts consolidados** en `mission-resumes/charts/`
- 📋 **Log de consolidación** en `consolidation-log.json`
- 📄 **Resumen de consolidación** en `consolidation-resume.md`
- 🔄 **Fusión inteligente** sin pérdida de contenido

### **6. test-system.py**

**Propósito:** Suite completa de testing para validar el sistema.

#### **Comandos Disponibles**

```bash
# Ejecutar suite completo de tests
python scripts/test-system.py --full-test

# Tests rápidos de funcionalidad
python scripts/test-system.py --quick-test

# Tests básicos de smoke testing
python scripts/test-system.py --smoke-test

# Tests con limpieza automática
python scripts/test-system.py --full-test --cleanup

# Tests sin limpieza de datos
python scripts/test-system.py --full-test --no-cleanup

# Solo generar reporte sin ejecutar tests
python scripts/test-system.py --report-only

# Mostrar ayuda detallada
python scripts/test-system.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|---------|
| `--full-test` | Suite completo de tests | ❌ | - |
| `--quick-test` | Tests rápidos funcionales | ❌ | - |
| `--smoke-test` | Tests básicos de smoke | ❌ | - |
| `--cleanup` | Limpiar datos después | ❌ | - |
| `--no-cleanup` | No limpiar datos | ❌ | - |
| `--report-only` | Solo generar reporte | ❌ | - |

#### **Lo que Valida**

- 📁 Estructura de directorios correcta
- 📝 Scripts existentes y ejecutables
- 📚 Documentación completa
- 🌐 Generación de sesiones
- 📄 Procesamiento de playbooks
- 📋 Sistema de tracking
- ✅ Consistencia general

---

### **7. web-guide-manager.py**

**Propósito:** Gestión de web-guides para reutilizar investigaciones web entre sesiones.

#### **Comandos Disponibles**

```bash
# Crear nuevo web-guide
python scripts/web-guide-manager.py --create "API-Authentication-Research" --session "2025-08-25_BACKEND-API-SETUP"

# Buscar web-guides existentes
python scripts/web-guide-manager.py --search "authentication"

# Listar todos los web-guides
python scripts/web-guide-manager.py --list

# Copiar web-guide a nueva sesión
python scripts/web-guide-manager.py --copy "API-Auth-Guide" --target-session "2025-08-26_API-DESIGN"

# Consolidar web-guides similares
python scripts/web-guide-manager.py --consolidate "auth,security"

# Validar actualidad de web-guides
python scripts/web-guide-manager.py --validate

# Generar índice de web-guides
python scripts/web-guide-manager.py --generate-index

# Mostrar ayuda detallada
python scripts/web-guide-manager.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|----------|
| `--create` | Crear nuevo web-guide | ❌ | `"API-Auth-Research"` |
| `--session` | Sesión asociada | ❌ | `"2025-08-25_BACKEND-API-SETUP"` |
| `--search` | Buscar por términos | ❌ | `"authentication"` |
| `--list` | Listar todos los web-guides | ❌ | - |
| `--copy` | Copiar web-guide existente | ❌ | `"API-Auth-Guide"` |
| `--target-session` | Sesión destino para copia | ❌ | `"2025-08-26_API-DESIGN"` |
| `--consolidate` | Consolidar por temas | ❌ | `"auth,security"` |
| `--validate` | Validar actualidad | ❌ | - |
| `--generate-index` | Generar índice | ❌ | - |

#### **Lo que Genera**

- 📄 Web-guides en `daily-work/[SESSION]/web-guides/`
- 🔍 Templates de investigación estructurados
- 📊 Tracking de web-guides en `.tracking.json`
- 📚 Índices de investigaciones por tema
- 🔗 Referencias cruzadas entre sesiones

---

### **8. operation-guide-manager.py (🆕 NUEVO v4.0)**

**Propósito:** Gestión independiente de guías operacionales para instalaciones, investigación, planificación y análisis.

#### **Comandos Disponibles**

```bash
# Crear nueva guía operacional
python3 scripts/operation-guide-manager.py --create "docker-installation" \
  --title "Instalación Docker Ubuntu" \
  --description "Guía completa para Docker en Ubuntu 22.04" \
  --tags "docker,instalacion,ubuntu"

# Buscar guías por tags
python3 scripts/operation-guide-manager.py --search --tags "docker"
python3 scripts/operation-guide-manager.py --search --tags "installation,setup"

# Buscar guías por nombre
python3 scripts/operation-guide-manager.py --search --name "docker"
python3 scripts/operation-guide-manager.py --search --name "postgres"

# Búsqueda libre en contenido
python3 scripts/operation-guide-manager.py --search --content "ubuntu installation"

# Listar todas las guías operacionales
python3 scripts/operation-guide-manager.py --list

# Mostrar ayuda detallada
python3 scripts/operation-guide-manager.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|----------|
| `--create` | Crear nueva guía operacional | ❌ | `"docker-installation"` |
| `--title` | Título descriptivo de la guía | ❌ | `"Instalación Docker Ubuntu"` |
| `--description` | Descripción detallada | ❌ | `"Guía completa para Docker"` |
| `--tags` | Tags separados por comas | ❌ | `"docker,ubuntu,installation"` |
| `--search` | Activar modo búsqueda | ❌ | - |
| `--name` | Buscar por nombre de guía | ❌ | `"docker"` |
| `--content` | Búsqueda libre en contenido | ❌ | `"ubuntu installation"` |
| `--list` | Listar todas las guías | ❌ | - |

#### **Lo que Genera**

- 📄 Guías operacionales en `operational-guides/[NOMBRE].md`
- 📊 Tracking independiente en `.operational-guides-tracking.json`
- 🔍 Templates estructurados para operaciones
- 📚 Metadatos completos (título, descripción, tags, fechas)
- 🔗 Sistema de búsqueda y filtrado avanzado

#### **Casos de Uso**

```bash
# Ejemplo 1: Instalación de Docker
python3 scripts/operation-guide-manager.py --create "docker-installation" \
  --title "Instalación Docker Ubuntu 22.04" \
  --description "Proceso completo de instalación y configuración de Docker" \
  --tags "docker,ubuntu,installation,containers"

# Ejemplo 2: Comparación de bases de datos
python3 scripts/operation-guide-manager.py --create "postgres-vs-mysql" \
  --title "PostgreSQL vs MySQL Comparison" \
  --description "Análisis comparativo entre PostgreSQL y MySQL" \
  --tags "database,comparison,postgresql,mysql"

# Ejemplo 3: Metodología de planificación
python3 scripts/operation-guide-manager.py --create "idea-planning-method" \
  --title "Metodología de Planificación de Ideas" \
  --description "Framework para estructurar y desarrollar nuevas ideas" \
  --tags "planning,methodology,ideas,framework"
```

---

### **9. maintenance.py**

**Propósito:** Mantenimiento automático del sistema (limpieza, backups, optimización).

#### **Comandos Disponibles**

```bash
# Mantenimiento diario
python scripts/maintenance.py --daily

# Mantenimiento semanal
python scripts/maintenance.py --weekly

# Mantenimiento mensual
python scripts/maintenance.py --monthly

# Solo crear backup completo
python scripts/maintenance.py --backup

# Mostrar ayuda detallada
python scripts/maintenance.py --help
```

#### **Parámetros**

| Parámetro | Descripción | Requerido | Ejemplo |
|-----------|-------------|-----------|---------|
| `--daily` | Mantenimiento diario | ❌ | - |
| `--weekly` | Mantenimiento semanal | ❌ | - |
| `--monthly` | Mantenimiento mensual | ❌ | - |
| `--backup` | Crear backup completo | ❌ | - |

#### **Lo que Hace**

**Mantenimiento Diario:**
- 🧽 Limpieza de archivos temporales
- 📁 Verificación de estructura
- 📋 Actualización de tracking

**Mantenimiento Semanal:**
- 📦 Archivado de sesiones antiguas
- 📈 Optimización de reportes
- 🔍 Detección de duplicados

**Mantenimiento Mensual:**
- 🚮 Backup completo del sistema
- 📦 Compresión de archivos antiguos
- 📊 Análisis de uso y métricas

---

## 🔄 **Comandos por Flujo de Trabajo**

### **Flujo Completo: Nueva Sesión de Desarrollo**

```bash
# 1. Crear estructura inicial
python3 scripts/generate_daily/cli.py --theme "BACKEND-API-SETUP" --date "2025-01-22"

# 2. Generar templates basados en playbooks
python3 scripts/playbook-processor.py --date="2025-01-22" --theme="BACKEND-API-SETUP"

# 3. Verificar que todo está consistente
python3 scripts/consistency_checker/cli.py --check-session --date="2025-01-22" --theme="BACKEND-API-SETUP"

# 4. Al final del día, generar reporte
python3 scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP"
```

### **🆕 Flujo Completo: Nueva Sesión Operacional (v4.0)**

```bash
# 1. Crear guía operacional (opcional, si no existe)
python3 scripts/operation-guide-manager.py --create "docker-setup" \
  --title "Docker Installation Guide" \
  --tags "docker,installation,ubuntu"

# 2. Crear sesión operacional
python3 scripts/generate_daily/cli.py --theme "SYSTEM-INSTALLATION" --template operations-modular

# 3. Trabajar en la sesión (referenciando guías operacionales)
# [Desarrollo del trabajo operacional]

# 4. Generar reporte
python3 scripts/report-generator.py --date="$(date +%Y-%m-%d)" --theme="SYSTEM-INSTALLATION"

# 5. Consolidar (incluye referencias a guías operacionales)
python3 scripts/mission_resumer/cli.py --theme="SYSTEM-INSTALLATION"
```

### **Flujo de Mantenimiento Diario**

```bash
# Verificación matutina
python3 scripts/consistency_checker/cli.py --scan-all

# Check rápido de sesión activa
python3 scripts/consistency_checker/cli.py --check-session --date="2025-01-22" --theme="BACKEND-API-SETUP"

# Estado del sistema
python3 scripts/status_checker/cli.py

# Al finalizar el día
python3 scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --detailed

# 🆕 Gestión de guías operacionales
python3 scripts/operation-guide-manager.py --list  # Ver guías disponibles
```

### **Flujo de Análisis Semanal**

```bash
# Verificación completa del sistema
python3 scripts/consistency_checker/cli.py --scan-all --generate-report

# Fusionar y consolidar sesiones del tema BACKEND
python3 scripts/mission_resumer/cli.py --theme="BACKEND"

# 🆕 Consolidar sesiones operacionales
python3 scripts/mission_resumer/cli.py --theme="SYSTEM-INSTALLATION"
python3 scripts/mission_resumer/cli.py --theme="TECHNOLOGY-RESEARCH"

# Generar reportes consolidados por tema
python3 scripts/report-generator.py --theme="BACKEND-API-SETUP" --all-sessions

# 🆕 Revisar guías operacionales utilizadas
python3 scripts/operation-guide-manager.py --search --tags "recent"
```

---

## 🔧 **Comandos de Diagnóstico y Mantenimiento**

### **Diagnóstico General**

```bash
# Estado completo del sistema
python scripts/consistency-checker.py --scan-all --verbose

# Información de playbooks disponibles
python scripts/playbook-processor.py --list-playbooks

# Temas configurados
python scripts/generate-daily.py --list-themes

# Verificar tracking general
python scripts/consistency-checker.py --check-tracking
```

### **Limpieza y Reparación**

```bash
# Reparación automática de problemas menores
python scripts/consistency-checker.py --auto-fix

# Detectar y reportar duplicados
python scripts/consistency-checker.py --check-duplicates

# Verificar solo estructura de directorios
python scripts/consistency-checker.py --check-structure
```

### **Comandos de Información**

```bash
# Ver ayuda de cualquier script
python scripts/[SCRIPT_NAME].py --help

# Listar sesiones existentes
ls -la daily-work/

# Ver contenido del tracking
cat daily-work/.tracking.json | python -m json.tool

# Estadísticas rápidas del sistema
find daily-work/ -name "*.md" | wc -l
```

---

## ⚙️ **Parámetros Comunes**

### **Parámetros Globales**

| Parámetro | Descripción | Scripts que lo Usan |
|-----------|-------------|---------------------|
| `--help` | Mostrar ayuda detallada | Todos |
| `--verbose` | Salida detallada | `consistency-checker.py`, `playbook-processor.py` |
| `--force` | Forzar sobrescritura | `generate-daily.py`, `playbook-processor.py` |
| `--quiet` | Modo silencioso | `generate-daily.py` |
| `--date` | Fecha específica (YYYY-MM-DD) | `generate-daily.py`, `playbook-processor.py`, `report-generator.py` |
| `--theme` | Tema específico | Todos los scripts principales |

### **Formatos de Fecha**

```bash
# Formato requerido
--date="2025-01-22"

# Ejemplos válidos
--date="2025-12-31"
--date="2025-01-01"

# Formatos inválidos (evitar)
--date="22-01-2025"  # ❌
--date="2025/01/22"  # ❌
--date="Jan 22, 2025"  # ❌
```

### **Temas Disponibles**

#### **Temas de Desarrollo (Template development)**
```bash
BACKEND-API-SETUP
BACKEND-ARCHITECTURE
FRONTEND-COMPONENTS
FRONTEND-ARCHITECTURE
DATABASE-SCHEMA
DEPLOYMENT-CONFIG
TESTING-STRATEGY
DESIGN-SYSTEM
API-DESIGN
CLI-DEVELOPMENT
DATA-MODELING
DEVOPS-SETUP
```

#### **🆕 Temas Operacionales (Template operations-modular v4.0)**
```bash
SYSTEM-INSTALLATION
TECHNOLOGY-RESEARCH
IDEA-PLANNING
PROCESS-DESIGN
COMPARISON-ANALYSIS
SERVICE-SETUP
INVESTIGATION-PLANNING
```

---

## 🚨 **Códigos de Salida**

| Código | Significado | Descripción |
|--------|-------------|-------------|
| `0` | Éxito | Operación completada sin errores |
| `1` | Error general | Error no específico |
| `2` | Error de parámetros | Parámetros inválidos o faltantes |
| `3` | Error de archivo | Archivo no encontrado o no accesible |
| `4` | Error de directorio | Directorio no encontrado o no accesible |
| `5` | Error de tracking | Problema con el sistema de tracking |
| `6` | Error de consistencia | Problemas de integridad detectados |
| `7` | Error de playbook | Playbook no válido o no encontrado |

### **Manejo de Errores Común**

```bash
# Verificar éxito de comando
python scripts/generate-daily.py --theme "BACKEND-API-SETUP" && echo "✅ Sesión creada exitosamente"

# Manejar errores
python scripts/generate-daily.py --theme "INVALID-THEME" || echo "❌ Error al crear sesión"

# Capturar código de salida
python scripts/consistency-checker.py --scan-all
echo "Código de salida: $?"
```

---

## 💡 **Ejemplos de Uso Común**

### **Scenario 1: Nuevo Proyecto Backend**

```bash
# Flujo completo típico con web-guides
python3 scripts/generate_daily/cli.py --date="$(date +%Y-%m-%d)" --theme="BACKEND-API-SETUP"
python3 scripts/playbook-processor.py --date="$(date +%Y-%m-%d)" --theme="BACKEND-API-SETUP"
# [Crear web-guide si necesitas investigar]
python3 scripts/web-guide-manager.py --create "API-Research" --session "$(date +%Y-%m-%d)_BACKEND-API-SETUP"
# [Trabajar en la sesión]
python3 scripts/report-generator.py --date="$(date +%Y-%m-%d)" --theme="BACKEND-API-SETUP"
python3 scripts/mission_resumer/cli.py --theme="BACKEND-API"

# Día 3: Modelado de datos
python3 scripts/generate_daily/cli.py --theme "DATABASE-SCHEMA" --date "2025-01-24"
python3 scripts/playbook-processor.py --date="2025-01-24" --theme="DATABASE-SCHEMA"

# Resumen y consolidación semanal
python3 scripts/mission_resumer/cli.py --theme="BACKEND"
```

### **🆕 Scenario 1b: Instalación de Sistema (v4.0)**

```bash
# Crear guía operacional para Docker
python3 scripts/operation-guide-manager.py --create "docker-ubuntu-install" \
  --title "Instalación Docker Ubuntu 22.04" \
  --description "Proceso completo de instalación y configuración" \
  --tags "docker,ubuntu,installation,containers"

# Crear sesión operacional
python3 scripts/generate_daily/cli.py --theme "SYSTEM-INSTALLATION" --template operations-modular

# [Trabajar en la instalación referenciando la guía]

# Generar reporte
python3 scripts/report-generator.py --date="$(date +%Y-%m-%d)" --theme="SYSTEM-INSTALLATION"

# Consolidar con referencias a guías operacionales
python3 scripts/mission_resumer/cli.py --theme="SYSTEM-INSTALLATION"
```

### **Scenario 2: Proyecto Frontend**

```bash
# Setup de design system
python3 scripts/generate_daily/cli.py --theme "DESIGN-SYSTEM" --date "2025-01-22"
python3 scripts/playbook-processor.py --date="2025-01-22" --theme="DESIGN-SYSTEM"

# Desarrollo de componentes
python3 scripts/generate_daily/cli.py --theme "FRONTEND-COMPONENTS" --date "2025-01-23"
python3 scripts/playbook-processor.py --date="2025-01-23" --theme="FRONTEND-COMPONENTS"

# Arquitectura frontend
python3 scripts/generate_daily/cli.py --theme "FRONTEND-ARCHITECTURE" --date "2025-01-24"
python3 scripts/playbook-processor.py --date="2025-01-24" --theme="FRONTEND-ARCHITECTURE"
```

### **🆕 Scenario 2b: Investigación Tecnológica (v4.0)**

```bash
# Crear guía para comparación de frameworks
python3 scripts/operation-guide-manager.py --create "react-vs-vue-analysis" \
  --title "React vs Vue.js Comparison" \
  --description "Análisis comparativo detallado entre React y Vue.js" \
  --tags "frontend,comparison,react,vue,frameworks"

# Crear sesión de investigación
python3 scripts/generate_daily/cli.py --theme "TECHNOLOGY-RESEARCH" --template operations-modular

# [Realizar investigación usando la guía operacional]

# Consolidar resultados
python3 scripts/mission_resumer/cli.py --theme="TECHNOLOGY-RESEARCH"
```

### **Scenario 3: Proyecto DevOps**

```bash
# Configuración de deployment
python scripts/generate-daily.py --theme "DEPLOYMENT-CONFIG" --date "2025-01-22"
python scripts/playbook-processor.py --date="2025-01-22" --theme="DEPLOYMENT-CONFIG"

# Setup de DevOps tools
python scripts/generate-daily.py --theme "DEVOPS-SETUP" --date "2025-01-23"
python scripts/playbook-processor.py --date="2025-01-23" --theme="DEVOPS-SETUP"

# Estrategia de testing
python scripts/generate-daily.py --theme "TESTING-STRATEGY" --date "2025-01-24"
python scripts/playbook-processor.py --date="2025-01-24" --theme="TESTING-STRATEGY"
```

### **Scenario 4: Mantenimiento y Auditoría**

```bash
# Verificación completa mensual
python scripts/consistency-checker.py --scan-all --generate-report

# Limpieza automática
python scripts/consistency-checker.py --auto-fix

# Reportes consolidados por tema
python scripts/report-generator.py --theme="BACKEND-API-SETUP" --all-sessions
python scripts/report-generator.py --theme="FRONTEND-COMPONENTS" --all-sessions

# Resumen ejecutivo por temas
python scripts/mission-resumer.py --theme="BACKEND"
python scripts/mission-resumer.py --theme="FRONTEND"
```

---

## 🐛 **Resolución de Problemas**

### **Error: "No estás en el directorio raíz"**

```bash
# Verificar ubicación actual
pwd

# Buscar el archivo indicador
find . -name "PLAN-COMPLETO.md" -type f

# Navegar al directorio correcto
cd [ruta-donde-esta-PLAN-COMPLETO.md]
```

### **Error: "Sesión no encontrada"**

```bash
# Listar sesiones existentes
ls -la daily-work/

# Verificar formato de fecha/tema
python scripts/generate-daily.py --list-themes

# Regenerar sesión si es necesario
python scripts/generate-daily.py --theme "TEMA-CORRECTO" --date "2025-01-22" --force
```

### **Error: "Playbook no encontrado"**

```bash
# Verificar playbooks disponibles
python scripts/playbook-processor.py --list-playbooks

# Verificar estructura de playbooks
ls -la playbooks/documentation_playbooks/

# Escanear playbooks
python scripts/playbook-processor.py --scan-all
```

### **Error: "Tracking corrupted"**

```bash
# Respaldo del tracking actual
cp daily-work/.tracking.json daily-work/.tracking.json.backup

# Verificar integridad
python scripts/consistency-checker.py --check-tracking

# Reparación automática
python scripts/consistency-checker.py --auto-fix
```

### **Error: "Permission denied"**

```bash
# Verificar permisos de scripts
ls -la scripts/

# Dar permisos de ejecución
chmod +x scripts/*.py

# Verificar permisos de Python
which python
python --version
```

### **Comandos de Diagnóstico Avanzado**

```bash
# Debug completo del sistema
python scripts/consistency-checker.py --scan-all --verbose > system-debug.log 2>&1

# Verificar dependencias
python -c "import json, os, datetime; print('Dependencies OK')"

# Test de escritura en directorio
touch daily-work/test-write && rm daily-work/test-write && echo "Write permissions OK"

# Verificar estructura completa
find . -type f \( -name "*.py" -o -name "*.md" \) | sort
```

---

## 📚 **Referencias Rápidas**

### **Setup diario básico**

```bash
# Setup diario básico - DESARROLLO
python3 scripts/generate_daily/cli.py --theme "TEMA" --date "FECHA"
python3 scripts/playbook-processor.py --date="FECHA" --theme="TEMA"

# 🆕 Setup diario básico - OPERACIONAL (v4.0)
python3 scripts/generate_daily/cli.py --theme "SYSTEM-INSTALLATION" --template operations-modular

# Verificación diaria
python3 scripts/consistency_checker/cli.py --scan-all

# Estado del sistema
python3 scripts/status_checker/cli.py

# Reporte de fin de día
python3 scripts/report-generator.py --date="FECHA" --theme="TEMA"

# 🆕 Gestión de guías operacionales
python3 scripts/operation-guide-manager.py --list
python3 scripts/operation-guide-manager.py --search --tags "installation"
```

### **Estructura de Directorios Esperada**

```
the-mighty-task/
├── PLAN-COMPLETO.md              # Archivo indicador
├── scripts/                     # Scripts ejecutables
├── playbooks/                   # Playbooks universales
├── daily-work/                  # Sesiones de trabajo
│   └── .tracking.json           # Sistema de tracking
├── reports/                     # Reportes generados
└── mission-resumes/             # Resúmenes ejecutivos
```

### **Variables de Entorno Útiles**

```bash
# Establecer directorio por defecto
export TMT_ROOT="/ruta/al/proyecto"

# Modo debug global
export TMT_DEBUG=1

# Formato de fecha por defecto
export TMT_DATE_FORMAT="%Y-%m-%d"
```

---

Este manual proporciona una referencia completa de todos los comandos disponibles en The Mighty Task v3.0. Para información más detallada sobre el flujo de trabajo completo, consulta `FLUJO-COMPLETO-SISTEMA.md` en el directorio `guides/`.
