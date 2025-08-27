# The Mighty Task Template - Sistema de Gestión de Tareas Diarias

**Versión:** 3.1 - Con Web-Guides y Especificación Avanzada  
**Estado:** 100% Funcional con Mejoras Implementadas  
**Fecha:** 2025-08-25

---

## 🎯 **DESCRIPCIÓN GENERAL**

The Mighty Task es un sistema completo de gestión de tareas diarias basado en **playbooks universales** y **checklists como fuente de verdad**. Diseñado para maximizar la productividad mediante estructura, automatización y tracking granular.

### **Características Principales:**
- ✅ **Generación automática** de sesiones diarias temáticas
- ✅ **Templates dinámicos** basados en playbooks universales
- ✅ **Sistema de tracking** JSON completo con métricas
- ✅ **Verificación de consistencia** automática
- ✅ **Reportes HTML/MD** para seguimiento detallado
- ✅ **Consolidación inteligente** de múltiples sesiones
- ✅ **Arquitectura modular** v2.0 completamente funcional
- 🆕 **Especificación detallada** de tareas con 6 campos obligatorios
- 🆕 **Sistema web-guides** para reutilización de investigaciones
- 🆕 **Guías de workflow** para uso correcto del sistema

- 🎯 **Playbooks universales** adaptables a cualquier framework o tecnología
- 📋 **Decisiones técnicas** estructuradas con placeholders claros
- 🔧 **Flexibilidad total** para React, Vue, Angular, Node.js, Python, etc.
- 📝 **Templates contextualizados** con marcos de referencia específicos
- ⚖️ **Comparación de opciones** integrada en cada decisión arquitectónica
- 🚀 **Escalabilidad** desde proyectos pequeños hasta enterprise

---

## 🚀 **Inicio Rápido**

### **1. Configuración Inicial**

```bash
# Clonar o acceder al directorio
cd the-mighty-task

# Verificar estructura (debe contener PLAN-COMPLETO.md)
ls -la

# Dar permisos de ejecución a scripts
chmod +x scripts/*.py
```

### **2. Crear tu Primera Sesión**

```bash
# Generar sesión para hoy con tema específico
python scripts/generate-daily.py --theme "BACKEND-API-SETUP"

# Generar templates de apoyo basados en playbooks
python scripts/playbook-processor.py --date="2025-01-22" --theme="BACKEND-API-SETUP"

# Verificar que todo está consistente
python scripts/consistency-checker.py --scan-all
```

### **3. Trabajar con la Sesión**

1. Abre el archivo principal: `daily-work/2025-01-22_BACKEND-API-SETUP/pending-tasks-2025-01-22_BACKEND-API-SETUP.md`
2. Completa los templates generados en `support-docs/`
3. Guarda evidencias en `assets/screenshots/` y `assets/logs/`
4. Al final del día, genera reporte: `python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP"`

---

## 📁 **Estructura del Sistema**

```
the-mighty-task/
├── 📄 PLAN-COMPLETO.md              # Plan completo del sistema
├── 📄 README.md                     # Este archivo
├── 📄 QUICK_START.md               # Guía de inicio rápido
├── 📄 template-pendingtask.md      # Template base para personalización
│
├── 📂 playbooks/                   # Playbooks como GUÍAS (INTACTOS)
│   └── documentation_playbooks/
│       ├── DOC003-DesignSystem.md
│       ├── DOC004-FrontendArchitecture.md
│       ├── DOC005-FrontendDependencies.md
│       ├── DOC006-BackendArchitecture.md
│       ├── DOC007-BackendDependencies.md
│       ├── DOC008-APISpecification.md
│       ├── DOC009-DataModel.md
│       ├── DOC010-Deployment.md
│       ├── DOC011-TestingStrategy.md
│       └── DOC019-CLI-Command-Reference.md
│
├── 📂 daily-work/                  # Trabajo diario por fecha+tema
│   ├── 📁 YYYY-MM-DD_THEME/
│   │   ├── pending-tasks-YYYY-MM-DD_THEME.md  # Archivo principal
│   │   ├── 📂 support-docs/                    # Templates generados
│   │   └── 📂 assets/                         # Evidencias y logs
│   └── 📄 .tracking.json                     # Sistema de tracking
│
├── 📂 reports/                     # Reportes generados
├── 📂 mission-resumes/            # Resúmenes ejecutivos
└├── 📂 scripts/                    # Scripts de automatización
    ├── generate-daily.py          # Generar estructura diaria
    ├── playbook-processor.py      # Procesar playbooks → templates
    ├── consistency-checker.py     # Verificar consistencia
    ├── report-generator.py        # Generar reportes
    ├── mission-resumer.py         # Crear resúmenes
    └── web-guide-manager.py       # 🆕 Gestionar web-guides
```

---

## 🛠️ **Scripts Principales**

### **1. generate-daily.py**
**Propósito:** Crear la estructura básica de trabajo diario.

```bash
# Crear sesión específica
python scripts/generate-daily.py --theme "BACKEND-API-SETUP" --date "2025-01-22"

# Crear con fecha actual
python scripts/generate-daily.py --theme "FRONTEND-COMPONENTS"

# Modo automático (fecha actual + tema default)
python scripts/generate-daily.py --auto

# Listar temas disponibles
python scripts/generate-daily.py --list-themes

# Sobrescribir sesión existente
python scripts/generate-daily.py --theme "API-DESIGN" --date "2025-01-22" --force
```

### **2. playbook-processor.py**
**Propósito:** Generar templates específicos basados en playbooks.

```bash
# Procesar playbooks para una sesión
python scripts/playbook-processor.py --date="2025-01-22" --theme="BACKEND-API-SETUP"

# Listar playbooks disponibles
python scripts/playbook-processor.py --list-playbooks

# Ver información detallada de playbooks
python scripts/playbook-processor.py --scan-all
```

### **3. consistency-checker.py**
**Propósito:** Verificar integridad y consistencia del sistema.

```bash
# Escanear todo el sistema
python scripts/consistency-checker.py --scan-all

# Verificar sesión específica
python scripts/consistency-checker.py --check-session --date="2025-01-22" --theme="BACKEND-API-SETUP"

# Solo verificar tracking
python scripts/consistency-checker.py --check-tracking

# Solo verificar duplicados
python scripts/consistency-checker.py --check-duplicates

# Generar reporte detallado
python scripts/consistency-checker.py --generate-report
```

### **4. report-generator.py** 
**Propósito:** Generar reportes de progreso y métricas.

```bash
# Generar reporte de sesión
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP"

# Reporte en formato específico
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP" --format html
```

### **5. mission-resumer.py**
**Propósito:** Crear resúmenes ejecutivos por tema.

```bash
# Resumen por tema
python scripts/mission-resumer.py --theme="BACKEND" --output="combined-backend-missions.md"
```

---

## 🎨 **Temas Disponibles**

| Tema | Descripción | Playbooks |
|------|-------------|-----------|  
| **BACKEND-API-SETUP** | Configuración y desarrollo de APIs backend | DOC006, DOC007, DOC008 |
| **BACKEND-ARCHITECTURE** | Arquitectura y estructura backend | DOC006, DOC007 |
| **FRONTEND-COMPONENTS** | Desarrollo de componentes frontend | DOC003, DOC004 |
| **FRONTEND-ARCHITECTURE** | Arquitectura y estructura frontend | DOC004 |
| **DATABASE-SCHEMA** | Diseño y modelado de base de datos | DOC009 |
| **DEPLOYMENT-CONFIG** | Configuración de deployment y DevOps | DOC010 |
| **TESTING-STRATEGY** | Estrategias y implementación de testing | DOC011 |
| **DESIGN-SYSTEM** | Sistema de diseño y componentes UI | DOC003 |
| **API-DESIGN** | Diseño y especificación de APIs | DOC008 |
| **CLI-DEVELOPMENT** | Desarrollo de herramientas CLI | DOC019 |
| **DATA-MODELING** | Modelado y estructuras de datos | DOC009 |
| **DEVOPS-SETUP** | Configuración de herramientas DevOps | DOC010 |

---

## 🔄 **Flujo de Trabajo Completo**

### **Paso 1: Generar Sesión**
```bash
python scripts/generate-daily.py --theme "BACKEND-API-SETUP" --date "2025-01-22"
```
- ✅ Crea estructura de directorios
- ✅ Genera archivo principal de tareas
- ✅ Crea READMEs para subdirectorios
- ✅ Actualiza sistema de tracking

### **Paso 2: Generar Templates**
```bash
python scripts/playbook-processor.py --date="2025-01-22" --theme="BACKEND-API-SETUP"
```
- ✅ Parsea playbooks relevantes
- ✅ Genera templates vacíos con TODOs
- ✅ Mantiene referencias a playbooks originales
- ✅ Actualiza tracking con templates generados

### **Paso 3: Trabajar en la Sesión**
- 📝 Abre archivo principal de tareas
- 📚 Consulta playbooks originales como guía
- ✍️ Completa templates en `support-docs/`
- 📸 Guarda evidencias en `assets/`
- ⏱️ Actualiza progreso en tiempo real

### **Paso 4: Verificar Consistencia**
```bash
python scripts/consistency-checker.py --scan-all
```
- 🔍 Verifica estructura de archivos
- 🔗 Valida referencias a playbooks
- 📊 Detecta contenido duplicado
- 🗂️ Confirma integridad del tracking

### **Paso 5: Generar Reportes**
```bash
python scripts/report-generator.py --date="2025-01-22" --theme="BACKEND-API-SETUP"
```
- 📈 Analiza métricas de progreso
- 📊 Genera reportes HTML/MD detallados
- 🎯 Incluye métricas de calidad y productividad

### **🆕 Paso 6: Gestionar Web-Guides**
```bash
# Crear web-guide para investigación
python scripts/web-guide-manager.py --create "express-setup" --session "2025-01-22_BACKEND-API-SETUP"

# Buscar guides existentes
python scripts/web-guide-manager.py --search "express"

# Listar todos los guides
python scripts/web-guide-manager.py --list-guides
```
- 🔍 Crea guides para investigaciones web
- 📚 Reutiliza investigaciones entre sesiones
- 🗂️ Organiza conocimiento por temas
- 📄 Genera reporte HTML y MD
- 📊 Incluye estadísticas detalladas
- 🎯 Identifica áreas de mejora

---

## 📊 **Sistema de Tracking**

El sistema mantiene un archivo `.tracking.json` con:

```json
{
  "processed_dates": [
    {
      "date": "2025-01-22",
      "theme": "BACKEND-API-SETUP",
      "playbooks_used": ["DOC006", "DOC007", "DOC008"],
      "files_created": [...],
      "templates_generated": [...],
      "status": "completed",
      "created_at": "2025-01-22T09:00:00Z",
      "last_updated": "2025-01-22T18:30:00Z"
    }
  ],
  "playbook_usage": {
    "DOC006": 4,
    "DOC007": 3,
    "DOC008": 4
  },
  "consistency_checks": {
    "last_check": "2025-01-22T12:00:00Z",
    "issues_found": 0,
    "total_files_checked": 15
  }
}
```

---

## 🔧 **Personalización**

### **Personalizar Template Base**
Edita `template-pendingtask.md` para cambiar:
- Estructura de secciones
- Campos personalizados
- Formato de progreso
- Métricas específicas

### **Agregar Nuevos Temas**
1. Agrega el tema en `AVAILABLE_THEMES` en `generate-daily.py`
2. Define mapeo en `THEME_PLAYBOOK_MAPPING`
3. Agrega el mismo mapeo en `playbook-processor.py`

### **Crear Nuevos Playbooks**
1. Crea archivo `DOC0XX-NombreDelPlaybook.md` en `playbooks/documentation_playbooks/`
2. Agrega mapeo en `PLAYBOOK_FILE_MAPPING` en `playbook-processor.py`
3. Asocia con temas relevantes

### **🆕 Personalizar Web-Guides**
1. Modifica templates en `web-guide-manager.py`
2. Agrega nuevos tags en `_extract_tags()`
3. Personaliza estructura de consolidación

---

## 🐛 **Troubleshooting**

### **Problemas Comunes**

#### **Error: "No estás en el directorio raíz"**
**Solución:** Ejecuta los scripts desde el directorio que contiene `PLAN-COMPLETO.md`

#### **Error: "Sesión no encontrada"**
**Solución:** 
```bash
# Verificar sesiones existentes
ls -la daily-work/

# Regenerar sesión si es necesaria
python scripts/generate-daily.py --theme="TEMA" --date="FECHA" --force
```

#### **Error: "Playbook no encontrado"**
**Solución:**
```bash
# Verificar playbooks disponibles
python scripts/playbook-processor.py --list-playbooks

# Verificar estructura
ls -la playbooks/documentation_playbooks/
```

#### **Problemas de Consistencia**
**Solución:**
```bash
# Ejecutar verificación completa
python scripts/consistency-checker.py --scan-all

# Generar reporte detallado de problemas
python scripts/consistency-checker.py --generate-report
```

### **Comandos de Diagnóstico**

```bash
# Verificar permisos
ls -la scripts/

# Verificar Python
python3 --version

# Verificar estructura completa
find . -type f -name "*.py" -o -name "*.md" | head -20

# Test de script básico
python scripts/generate-daily.py --list-themes
```

---

## 📋 **Buenas Prácticas**

### **Para Usuarios**
- ✅ Siempre usar fechas en formato `YYYY-MM-DD`
- ✅ Temas en mayúsculas con guiones: `BACKEND-API-SETUP`
- ✅ Ejecutar `consistency-checker.py` periódicamente
- ✅ Completar templates antes de generar reportes
- ✅ Usar `assets/` para todas las evidencias

### **Para Desarrollo**
- ✅ Mantener playbooks originales intactos
- ✅ Usar tracking para todas las operaciones
- ✅ Validar inputs en todos los scripts
- ✅ Mantener compatibilidad con formato MD
- ✅ Logging detallado en operaciones críticas

---

## 🔄 **Actualizaciones y Mantenimiento**

### **Mantenimiento Regular**
```bash
# Semanal: verificar consistencia
python scripts/consistency-checker.py --scan-all

# Mensual: limpiar archivos temporales
find daily-work/ -name "*.tmp" -delete

# Trimestral: generar resúmenes por tema
python scripts/mission-resumer.py --theme="BACKEND" --output="quarterly-backend.md"
```

### **Backup Recomendado**
- 📂 `daily-work/` - Datos principales
- 📂 `playbooks/` - Guías de referencia
- 📄 `.tracking.json` - Historial del sistema
- 📂 `reports/` - Reportes generados

---

## 🤝 **Contribuciones**

Para contribuir al proyecto:

1. **Reportar bugs:** Usar `consistency-checker.py` para generar reportes detallados
2. **Proponer mejoras:** Seguir estructura de playbooks existente
3. **Nuevos temas:** Definir mapeo claro a playbooks
4. **Testing:** Validar con casos de uso reales

---

## 📞 **Soporte**

- 📖 **Documentación completa:** `PLAN-COMPLETO.md`
- 🚀 **Inicio rápido:** `QUICK_START.md`
- 🔍 **Diagnóstico:** `python scripts/consistency-checker.py --scan-all`
- 📊 **Estado del sistema:** `daily-work/.tracking.json`

---

## 📄 **Licencia**

Este proyecto es parte del sistema The Mighty Task - Sistema Dinámico de Gestión de Tareas.

---

**¡Comienza tu primera sesión de trabajo hoy mismo!** 🚀
