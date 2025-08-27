# Sistema de Guías Operacionales v4.0 - The Mighty Task

**Fecha:** 2025-08-26  
**Versión:** 4.0  
**Estado:** Sistema Independiente Implementado y Funcional  

---

## 🎯 **OBJETIVO DEL SISTEMA**

El **Sistema de Guías Operacionales v4.0** es un módulo independiente dentro de The Mighty Task diseñado para gestionar conocimiento operacional reutilizable como instalaciones, investigaciones, planificación de ideas y análisis comparativos.

### **🔑 Características Principales**

- **🔄 Gestión Independiente:** Tracking separado del sistema de desarrollo
- **🏷️ Sistema de Tags:** Búsqueda y filtrado avanzado por etiquetas
- **📝 Metadatos Completos:** Título, descripción, tags, fechas de creación/modificación
- **🔍 Búsqueda Múltiple:** Por nombre, tags, contenido libre
- **📊 Integración con Mission-Resumer:** Referencias automáticas en consolidaciones
- **🎨 Templates Modulares:** Uso del template operations-modular

---

## 📁 **ARQUITECTURA DEL SISTEMA**

### **Estructura de Archivos**

```
the-mighty-task/
├── 📂 operational-guides/                    # Directorio independiente
│   ├── .operational-guides-tracking.json    # Tracking separado
│   ├── docker-installation.md               # Guía Docker Ubuntu
│   ├── postgres-comparison.md               # Comparación PostgreSQL
│   ├── idea-planning-methodology.md         # Metodología de ideas
│   ├── service-setup-checklist.md           # Checklist servicios
│   └── technology-research-framework.md     # Framework investigación
│
├── 📂 scripts/
│   └── operation-guide-manager.py           # Gestor principal
│
└── 📂 daily-work/
    └── [FECHA]_[TEMA-OPERACIONAL]/          # Sesiones operacionales
        └── pending-tasks-[FECHA]_[TEMA].md  # Template operations-modular
```

### **Separación de Responsabilidades**

| Componente | Propósito | Tracking |
|------------|-----------|----------|
| **Web-Guides** | Investigaciones web por sesión | `.tracking.json` |
| **Operational-Guides** | Conocimiento operacional reutilizable | `.operational-guides-tracking.json` |
| **Development Sessions** | Desarrollo de código y arquitectura | `.tracking.json` |

---

## 🛠️ **OPERATION-GUIDE-MANAGER.PY**

### **Comandos Principales**

#### **1. Crear Nueva Guía**

```bash
python3 scripts/operation-guide-manager.py --create "docker-installation" \
  --title "Instalación Docker Ubuntu 22.04" \
  --description "Proceso completo de instalación y configuración de Docker" \
  --tags "docker,ubuntu,installation,containers"
```

#### **2. Búsqueda por Tags**

```bash
# Buscar por tag específico
python3 scripts/operation-guide-manager.py --search --tags "docker"

# Buscar por múltiples tags
python3 scripts/operation-guide-manager.py --search --tags "installation,ubuntu"
```

#### **3. Búsqueda por Nombre**

```bash
python3 scripts/operation-guide-manager.py --search --name "docker"
python3 scripts/operation-guide-manager.py --search --name "postgres"
```

#### **4. Búsqueda Libre en Contenido**

```bash
python3 scripts/operation-guide-manager.py --search --content "ubuntu installation"
```

#### **5. Listar Todas las Guías**

```bash
python3 scripts/operation-guide-manager.py --list
```

### **Estructura del Tracking JSON**

```json
{
  "guides": {
    "docker-installation": {
      "title": "Instalación Docker Ubuntu 22.04",
      "description": "Proceso completo de instalación y configuración",
      "tags": ["docker", "ubuntu", "installation", "containers"],
      "created_date": "2025-08-26",
      "modified_date": "2025-08-26",
      "file_path": "operational-guides/docker-installation.md"
    }
  },
  "metadata": {
    "total_guides": 1,
    "last_updated": "2025-08-26T12:00:00",
    "version": "4.0"
  }
}
```

---

## 🎨 **TEMAS OPERACIONALES**

### **Temas Disponibles (Template operations-modular)**

| Tema | Descripción | Playbooks |
|------|-------------|-----------|
| `SYSTEM-INSTALLATION` | Instalaciones de sistemas y herramientas | DOC035, DOC036 |
| `TECHNOLOGY-RESEARCH` | Investigación y análisis tecnológico | DOC035, DOC036 |
| `IDEA-PLANNING` | Planificación y estructuración de ideas | DOC035, DOC036 |
| `PROCESS-DESIGN` | Diseño de procesos y metodologías | DOC035, DOC036 |
| `COMPARISON-ANALYSIS` | Análisis comparativo de tecnologías | DOC035, DOC036 |
| `SERVICE-SETUP` | Configuración de servicios | DOC035, DOC036 |
| `INVESTIGATION-PLANNING` | Planificación de investigaciones | DOC035, DOC036 |

### **Uso con Generate-Daily**

```bash
# Crear sesión operacional
python3 scripts/generate_daily/cli.py --theme "SYSTEM-INSTALLATION" --template operations-modular

# Crear sesión de investigación
python3 scripts/generate_daily/cli.py --theme "TECHNOLOGY-RESEARCH" --template operations-modular

# Crear sesión de planificación
python3 scripts/generate_daily/cli.py --theme "IDEA-PLANNING" --template operations-modular
```

---

## 🔄 **FLUJO DE TRABAJO COMPLETO**

### **Paso 1: Crear Guía Operacional**

```bash
# Ejemplo: Instalación de PostgreSQL
python3 scripts/operation-guide-manager.py --create "postgresql-installation" \
  --title "Instalación PostgreSQL Ubuntu" \
  --description "Guía completa para instalar y configurar PostgreSQL" \
  --tags "postgresql,database,installation,ubuntu"
```

### **Paso 2: Crear Sesión Operacional**

```bash
# Crear sesión usando tema operacional
python3 scripts/generate_daily/cli.py --theme "SYSTEM-INSTALLATION" --template operations-modular
```

### **Paso 3: Trabajar en la Sesión**

- Abrir archivo principal: `pending-tasks-[FECHA]_SYSTEM-INSTALLATION.md`
- Referenciar guía operacional creada: `postgresql-installation.md`
- Completar tareas siguiendo la metodología del template operations-modular
- Documentar comandos, validaciones y resultados

### **Paso 4: Generar Reporte**

```bash
python3 scripts/report-generator.py --date="$(date +%Y-%m-%d)" --theme="SYSTEM-INSTALLATION"
```

### **Paso 5: Consolidar con Mission-Resumer**

```bash
python3 scripts/mission_resumer/cli.py --theme="SYSTEM-INSTALLATION"
```

**Resultado:** El mission-resumer incluirá automáticamente una sección con las guías operacionales referenciadas.

---

## 📊 **INTEGRACIÓN CON MISSION-RESUMER**

### **Sección de Guías Operacionales**

El mission-resumer v4.0 incluye automáticamente una sección dedicada:

```markdown
## 📚 GUÍAS OPERACIONALES REFERENCIADAS

### postgresql-installation
- **Título:** Instalación PostgreSQL Ubuntu
- **Descripción:** Guía completa para instalar y configurar PostgreSQL
- **Tags:** postgresql, database, installation, ubuntu
- **Archivo:** operational-guides/postgresql-installation.md
- **Usado en:** 2025-08-26_SYSTEM-INSTALLATION

### docker-installation
- **Título:** Instalación Docker Ubuntu 22.04
- **Descripción:** Proceso completo de instalación y configuración
- **Tags:** docker, ubuntu, installation, containers
- **Archivo:** operational-guides/docker-installation.md
- **Usado en:** 2025-08-25_SYSTEM-INSTALLATION
```

---

## 🎯 **CASOS DE USO TÍPICOS**

### **1. Instalación de Herramientas**

```bash
# Crear guía para Node.js
python3 scripts/operation-guide-manager.py --create "nodejs-installation" \
  --title "Instalación Node.js con NVM" \
  --description "Instalación de Node.js usando Node Version Manager" \
  --tags "nodejs,nvm,installation,javascript"

# Crear sesión de instalación
python3 scripts/generate_daily/cli.py --theme "SYSTEM-INSTALLATION" --template operations-modular
```

### **2. Investigación Tecnológica**

```bash
# Crear guía de comparación
python3 scripts/operation-guide-manager.py --create "react-vs-vue" \
  --title "React vs Vue.js Comparison 2025" \
  --description "Análisis comparativo actualizado entre React y Vue.js" \
  --tags "frontend,comparison,react,vue,frameworks"

# Crear sesión de investigación
python3 scripts/generate_daily/cli.py --theme "TECHNOLOGY-RESEARCH" --template operations-modular
```

### **3. Planificación de Ideas**

```bash
# Crear metodología de planificación
python3 scripts/operation-guide-manager.py --create "startup-idea-framework" \
  --title "Framework de Validación de Ideas de Startup" \
  --description "Metodología para validar y estructurar ideas de negocio" \
  --tags "startup,ideas,planning,methodology,business"

# Crear sesión de planificación
python3 scripts/generate_daily/cli.py --theme "IDEA-PLANNING" --template operations-modular
```

### **4. Configuración de Servicios**

```bash
# Crear guía de configuración
python3 scripts/operation-guide-manager.py --create "nginx-ssl-setup" \
  --title "Configuración Nginx con SSL" \
  --description "Setup completo de Nginx con certificados SSL/TLS" \
  --tags "nginx,ssl,https,webserver,security"

# Crear sesión de configuración
python3 scripts/generate_daily/cli.py --theme "SERVICE-SETUP" --template operations-modular
```

---

## 🔍 **BÚSQUEDA Y FILTRADO**

### **Búsqueda por Tags**

```bash
# Encontrar todas las guías de instalación
python3 scripts/operation-guide-manager.py --search --tags "installation"

# Encontrar guías de Docker
python3 scripts/operation-guide-manager.py --search --tags "docker"

# Búsqueda con múltiples tags
python3 scripts/operation-guide-manager.py --search --tags "database,postgresql"
```

### **Búsqueda por Nombre**

```bash
# Buscar guías que contengan "docker" en el nombre
python3 scripts/operation-guide-manager.py --search --name "docker"

# Buscar guías de instalación
python3 scripts/operation-guide-manager.py --search --name "installation"
```

### **Búsqueda Libre**

```bash
# Buscar en contenido completo
python3 scripts/operation-guide-manager.py --search --content "ubuntu 22.04"

# Buscar metodologías
python3 scripts/operation-guide-manager.py --search --content "methodology framework"
```

---

## ⚙️ **CONFIGURACIÓN Y PERSONALIZACIÓN**

### **Validación de Duplicados**

El sistema previene automáticamente la creación de guías duplicadas:

```bash
# Si ya existe "docker-installation", mostrará error
python3 scripts/operation-guide-manager.py --create "docker-installation" \
  --title "Nueva instalación Docker"
# ❌ Error: Ya existe una guía con el nombre 'docker-installation'
```

### **Estructura del Template**

Las guías operacionales usan una estructura estándar:

```markdown
# [TÍTULO DE LA GUÍA]

**Fecha de Creación:** [FECHA]
**Tags:** [TAG1, TAG2, TAG3]
**Descripción:** [DESCRIPCIÓN]

## 🎯 Objetivo

[Descripción del objetivo de la guía]

## 📋 Prerrequisitos

- [Prerequisito 1]
- [Prerequisito 2]

## 🔧 Proceso Paso a Paso

### Paso 1: [Nombre del paso]
[Descripción detallada]

### Paso 2: [Nombre del paso]
[Descripción detallada]

## ✅ Validación

- [ ] [Criterio de validación 1]
- [ ] [Criterio de validación 2]

## 🔍 Troubleshooting

### Problema: [Descripción del problema]
**Solución:** [Solución detallada]

## 📚 Referencias

- [Enlace 1]
- [Enlace 2]
```

---

## 🚀 **MEJORES PRÁCTICAS**

### **1. Naming Convention**

```bash
# ✅ Nombres descriptivos y claros
docker-installation
postgresql-setup
react-vs-vue-comparison
startup-idea-framework

# ❌ Nombres genéricos o ambiguos
guide1
setup
comparison
```

### **2. Tags Efectivos**

```bash
# ✅ Tags específicos y útiles
--tags "docker,ubuntu,installation,containers"
--tags "database,postgresql,setup,configuration"
--tags "frontend,comparison,react,vue,frameworks"

# ❌ Tags genéricos o redundantes
--tags "guide,help,tutorial"
--tags "good,useful,important"
```

### **3. Descripciones Claras**

```bash
# ✅ Descripciones específicas
--description "Proceso completo de instalación de Docker en Ubuntu 22.04 con configuración de permisos"

# ❌ Descripciones vagas
--description "Guía de Docker"
--description "Como instalar cosas"
```

### **4. Mantenimiento Regular**

```bash
# Revisar guías periódicamente
python3 scripts/operation-guide-manager.py --list

# Buscar guías por fecha de creación reciente
python3 scripts/operation-guide-manager.py --search --content "2025-08"
```

---

## 🔧 **TROUBLESHOOTING**

### **Error: "Guía ya existe"**

```bash
# Verificar guías existentes
python3 scripts/operation-guide-manager.py --list

# Buscar por nombre similar
python3 scripts/operation-guide-manager.py --search --name "docker"
```

### **Error: "Tracking file corrupted"**

```bash
# Verificar integridad del tracking
cat operational-guides/.operational-guides-tracking.json | python3 -m json.tool

# Backup y regeneración si es necesario
cp operational-guides/.operational-guides-tracking.json operational-guides/.backup-tracking.json
```

### **Búsqueda sin resultados**

```bash
# Verificar tags exactos
python3 scripts/operation-guide-manager.py --list

# Usar búsqueda libre como alternativa
python3 scripts/operation-guide-manager.py --search --content "término"
```

---

## 📈 **MÉTRICAS Y ESTADÍSTICAS**

### **Información del Sistema**

El tracking JSON incluye métricas automáticas:

```json
{
  "metadata": {
    "total_guides": 5,
    "last_updated": "2025-08-26T12:00:00",
    "version": "4.0",
    "most_used_tags": ["installation", "docker", "ubuntu"],
    "creation_stats": {
      "2025-08-26": 3,
      "2025-08-25": 2
    }
  }
}
```

### **Comandos de Análisis**

```bash
# Ver estadísticas rápidas
python3 scripts/operation-guide-manager.py --list | wc -l

# Analizar tags más usados
grep -o '"tags":.*' operational-guides/.operational-guides-tracking.json
```

---

## 🎉 **CONCLUSIÓN**

El **Sistema de Guías Operacionales v4.0** proporciona una solución completa para gestionar conocimiento operacional reutilizable dentro de The Mighty Task. Con su arquitectura independiente, sistema de búsqueda avanzado e integración automática con mission-resumer, facilita la creación, organización y reutilización de guías operacionales para instalaciones, investigaciones, planificación y análisis.

**Características destacadas:**
- ✅ Gestión independiente con tracking separado
- ✅ Búsqueda y filtrado avanzado por tags, nombre y contenido
- ✅ Integración automática con consolidaciones
- ✅ Templates modulares especializados
- ✅ Validación de duplicados
- ✅ Metadatos completos y estructurados

**El sistema está 100% operacional y listo para uso en producción.** 🚀
