# ANÁLISIS ARQUITECTURA DUAL DASHBOARD - The Mighty Task

**Fecha:** 2025-08-26  
**Objetivo:** Diseñar arquitectura dual para gestión local y servidor de proyectos mighty-task

## 🔍 **ANÁLISIS DE SITUACIÓN ACTUAL**

### **Estructura Actual de Mighty-Task:**
```
the-mighty-task-template/
├── scripts/                    # Backend Python ya implementado
│   ├── generate_daily/         # Generación de sesiones
│   ├── mission_resumer/        # Consolidación v5.0
│   ├── status_checker/         # Monitoreo del sistema
│   ├── consistency_checker/    # Verificación de integridad
│   └── shared/                 # Utilidades compartidas
├── daily-work/                 # Sesiones de trabajo (vacío actualmente)
├── mission-resumes/            # Consolidaciones (vacío actualmente)
├── playbooks/                  # Templates universales
├── reports/                    # Reportes generados
└── operational-guides/         # Guías operacionales
```

### **Capacidades Actuales del Backend Python:**
✅ **Sistema modular completo** con arquitectura v5.0  
✅ **PlaybookRegistry** - Gestión centralizada de templates  
✅ **Mission-Resumer v5.0** - Consolidación automática  
✅ **Status-Checker** - Monitoreo completo del sistema  
✅ **Consistency-Checker** - Validación de integridad  
✅ **Shared utilities** - ColoredOutput, TemplateDetector  

### **Lo que FALTA para Multi-Proyecto:**
❌ **Identificadores únicos** por proyecto  
❌ **Sistema de exportación/importación**  
❌ **APIs REST** para comunicación remota  
❌ **Gestión de múltiples workspaces**  
❌ **Compresión de proyectos completos**  

---

## 🏗️ **ARQUITECTURA DUAL PROPUESTA**

### **1. DASHBOARD LOCAL**
**Propósito:** Gestión directa de proyectos en la misma máquina

**Características:**
- Acceso directo al filesystem
- Ejecución directa de scripts Python
- Sin necesidad de APIs
- Gestión de múltiples proyectos locales
- Importación/exportación entre proyectos

**Tecnologías:**
- Svelte 5 frontend
- Tauri o Electron para acceso filesystem
- Comunicación directa con scripts Python

### **2. DASHBOARD SERVIDOR**
**Propósito:** Gestión centralizada de múltiples proyectos remotos

**Características:**
- APIs REST para comunicación
- Gestión de múltiples usuarios/proyectos
- Sistema de autenticación
- Backup y sincronización automática
- Dashboard de administración

**Tecnologías:**
- Svelte 5 frontend
- FastAPI backend (Python)
- Base de datos para metadatos
- Sistema de archivos distribuido

---

## 🔑 **SISTEMA DE IDENTIFICADORES ÚNICOS**

### **Project ID Structure:**
```
[ORGANIZATION]-[PROJECT]-[TIMESTAMP]
Ejemplo: HIRUNDO-BACKEND-API-20250826174500
```

### **Metadatos de Proyecto:**
```json
{
  "project_id": "HIRUNDO-BACKEND-API-20250826174500",
  "name": "Backend API Development",
  "organization": "HIRUNDO",
  "created_at": "2025-08-26T17:45:00Z",
  "last_modified": "2025-08-26T17:45:00Z",
  "version": "1.0.0",
  "description": "API development for main application",
  "tags": ["backend", "api", "python"],
  "owner": "developer@hirundo.dev",
  "collaborators": [],
  "settings": {
    "default_template": "development",
    "auto_backup": true,
    "compression_level": 6
  }
}
```

---

## 📦 **SISTEMA DE COMPRESIÓN Y EXPORTACIÓN**

### **Formato de Exportación (.mtp - Mighty Task Package):**
```
project-export.mtp (ZIP comprimido)
├── project-metadata.json      # Metadatos del proyecto
├── daily-work/                # Todas las sesiones
├── mission-resumes/           # Consolidaciones
├── playbooks/                 # Templates personalizados
├── reports/                   # Reportes generados
├── operational-guides/        # Guías operacionales
├── scripts/config/            # Configuraciones específicas
└── export-manifest.json       # Inventario completo
```

### **Export Manifest:**
```json
{
  "export_date": "2025-08-26T17:45:00Z",
  "export_version": "1.0.0",
  "project_id": "HIRUNDO-BACKEND-API-20250826174500",
  "files_count": 156,
  "total_size_bytes": 2457600,
  "checksum": "sha256:abc123...",
  "contents": {
    "daily_sessions": 12,
    "mission_resumes": 3,
    "reports": 8,
    "playbooks": 12,
    "operational_guides": 5
  },
  "dependencies": [],
  "compatibility": {
    "min_mighty_task_version": "5.0.0",
    "python_version": "3.8+"
  }
}
```

---

## 🔧 **MODIFICACIONES NECESARIAS EN SCRIPTS**

### **1. Nuevo Módulo: Project Manager**
```python
# scripts/shared/project_manager.py
class ProjectManager:
    def generate_project_id(self, org: str, name: str) -> str
    def create_project_metadata(self, **kwargs) -> Dict
    def export_project(self, output_path: str) -> bool
    def import_project(self, package_path: str) -> bool
    def list_projects(self) -> List[Dict]
    def switch_project(self, project_id: str) -> bool
```

### **2. Nuevo Módulo: Export/Import System**
```python
# scripts/shared/export_import.py
class ProjectExporter:
    def compress_project(self, project_path: str) -> str
    def generate_manifest(self, project_path: str) -> Dict
    def validate_export(self, package_path: str) -> bool

class ProjectImporter:
    def extract_package(self, package_path: str) -> str
    def validate_compatibility(self, manifest: Dict) -> bool
    def merge_project(self, source_path: str, target_path: str) -> bool
```

### **3. APIs REST para Dashboard Servidor**
```python
# scripts/api/
├── main.py                    # FastAPI app
├── routers/
│   ├── projects.py           # CRUD proyectos
│   ├── sessions.py           # Gestión sesiones
│   ├── mission_resumer.py    # Consolidación
│   ├── status.py             # Estado del sistema
│   └── export_import.py      # Exportación/importación
└── models/
    ├── project.py            # Modelos de datos
    ├── session.py
    └── response.py
```

### **4. Modificaciones en Scripts Existentes**

**A. PlaybookRegistry - Agregar soporte multi-proyecto:**
```python
def __init__(self, project_id: str = None, base_path: Path = None):
    self.project_id = project_id
    # ... resto del código
```

**B. MissionResumer - Agregar metadatos de proyecto:**
```python
def consolidate_sessions(self, project_id: str, theme: str):
    # Incluir project_id en logs y outputs
    # ... resto del código
```

**C. StatusChecker - Incluir información de proyecto:**
```python
def get_system_status(self, project_id: str = None):
    # Mostrar información específica del proyecto
    # ... resto del código
```

---

## 🌐 **ARQUITECTURA DE COMUNICACIÓN**

### **Dashboard Local ↔ Scripts Python:**
```
Dashboard Local (Svelte)
    ↓ Direct filesystem access
Scripts Python (subprocess calls)
    ↓ Direct file operations
Local Project Files
```

### **Dashboard Servidor ↔ Proyectos Remotos:**
```
Dashboard Servidor (Svelte)
    ↓ HTTP/WebSocket
FastAPI Backend
    ↓ File operations + Database
Remote Project Files + Metadata DB
```

---

## 📋 **PLAN DE IMPLEMENTACIÓN**

### **Fase 1: Modificaciones Base (Semana 1)**
1. ✅ Crear ProjectManager module
2. ✅ Implementar sistema de identificadores únicos
3. ✅ Modificar scripts existentes para soporte multi-proyecto
4. ✅ Crear sistema de export/import básico

### **Fase 2: Dashboard Local (Semana 2)**
1. ✅ Adaptar dashboard Svelte para multi-proyecto
2. ✅ Implementar selector de proyectos
3. ✅ Crear funcionalidad de import/export
4. ✅ Testing con múltiples proyectos locales

### **Fase 3: APIs Backend (Semana 3)**
1. ✅ Crear FastAPI backend
2. ✅ Implementar endpoints para todas las funcionalidades
3. ✅ Sistema de autenticación básico
4. ✅ Testing de APIs

### **Fase 4: Dashboard Servidor (Semana 4)**
1. ✅ Adaptar frontend para comunicación API
2. ✅ Implementar gestión de múltiples usuarios
3. ✅ Sistema de backup automático
4. ✅ Deployment y testing completo

---

## 🎯 **BENEFICIOS DE ESTA ARQUITECTURA**

### **Para Desarrolladores Individuales:**
- **Dashboard Local** para proyectos personales
- Acceso rápido sin configuración de servidor
- Importación/exportación fácil entre proyectos

### **Para Equipos/Organizaciones:**
- **Dashboard Servidor** para colaboración
- Gestión centralizada de múltiples proyectos
- Backup automático y sincronización
- Control de acceso y permisos

### **Flexibilidad:**
- Mismo código base para ambos dashboards
- Migración fácil de local a servidor
- Compatibilidad total con sistema actual

---

**Estado:** ✅ Análisis completo - Listo para implementación  
**Próximo paso:** Implementar ProjectManager y sistema de identificadores únicos
