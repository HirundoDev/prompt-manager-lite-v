# PLAN: Mission-Resumer Completo v5.0
**Fecha:** 2025-08-26  
**Objetivo:** Implementar mission-resumer como punto único de consolidación con pre-carga automática

## 🎯 **OBJETIVO PRINCIPAL**

Modificar `mission-resumer.py` para que automáticamente:
1. **Pre-cargue** toda la estructura necesaria en `mission-resumes/`
2. **Consolide** todo el contenido de daily-works
3. **Mantenga** mission-resumes/ como carpeta única con todo disponible

## 📁 **ESTRUCTURA FINAL DESEADA**

```
mission-resumes/
├── assets/                           # Consolidado de todos los assets
│   ├── logs/                        # Logs consolidados
│   └── screenshots/                 # Screenshots consolidados
├── charts/                          # Consolidado de todos los charts/diagramas
├── web-guides/                      # Consolidado de todas las web-guides
├── support-docs/                    # DOCs específicos consolidados
├── DOC003-DesignSystem.md          # Template vacío listo para llenar
├── DOC004-FrontendArchitecture.md  # Template vacío listo para llenar
├── DOC005-FrontendDependencies.md  # Template vacío listo para llenar
├── DOC006-BackendArchitecture.md   # Template vacío listo para llenar
├── DOC007-BackendDependencies.md   # Template vacío listo para llenar
├── DOC008-APISpecification.md      # Template vacío listo para llenar
├── DOC009-DataModel.md             # Template vacío listo para llenar
├── DOC010-Deployment.md            # Template vacío listo para llenar
├── DOC011-TestingStrategy.md       # Template vacío listo para llenar
├── DOC019-CLI-Command-Reference.md # Template vacío listo para llenar
├── DOC035-ErrorTracking.md         # Template vacío listo para llenar
├── DOC036-ErrorCodes.md            # Template vacío listo para llenar
├── [tema]-CONSOLIDATED.md          # Consolidaciones por tema
└── consolidation-log-*.json        # Logs de consolidación
```

## 🔧 **FUNCIONALIDADES A IMPLEMENTAR**

### **1. Pre-carga Automática de Templates**
```python
def _initialize_mission_resumes_structure(self):
    """Pre-carga automáticamente toda la estructura necesaria."""
    
    # 1. Crear carpetas base
    folders = ['assets', 'assets/logs', 'assets/screenshots', 'charts', 'web-guides', 'support-docs']
    for folder in folders:
        (self.mission_resumes_dir / folder).mkdir(parents=True, exist_ok=True)
    
    # 2. Copiar templates DOC vacíos desde playbooks/documentation_playbooks/
    doc_templates_dir = self.base_path / 'playbooks' / 'documentation_playbooks'
    for doc_file in doc_templates_dir.glob('DOC*.md'):
        dest_file = self.mission_resumes_dir / doc_file.name
        if not dest_file.exists():  # Solo si no existe
            shutil.copy2(doc_file, dest_file)
```

### **2. Consolidación Completa de Assets**
```python
def _consolidate_all_assets(self, sessions):
    """Consolida assets, charts, web-guides de todas las sesiones."""
    
    for session in sessions:
        session_dir = session['directory']
        
        # Consolidar assets
        self._consolidate_folder(session_dir / 'assets', 'assets', session['name'])
        
        # Consolidar charts
        self._consolidate_folder(session_dir / 'charts', 'charts', session['name'])
        
        # Consolidar web-guides
        self._consolidate_folder(session_dir / 'web-guides', 'web-guides', session['name'])
        
        # Consolidar support-docs
        self._consolidate_folder(session_dir / 'support-docs', 'support-docs', session['name'])
```

### **3. Consolidación Inteligente por Carpetas**
```python
def _consolidate_folder(self, source_dir, target_folder, session_name):
    """Consolida una carpeta específica manteniendo organización."""
    
    if not source_dir.exists():
        return
    
    target_dir = self.mission_resumes_dir / target_folder / session_name
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Copiar todos los archivos manteniendo estructura
    for file_path in source_dir.rglob('*'):
        if file_path.is_file():
            relative_path = file_path.relative_to(source_dir)
            dest_path = target_dir / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, dest_path)
```

## 🚀 **PROCESO DE IMPLEMENTACIÓN**

### **Fase 1: Modificar MissionResumer.__init__()**
- Agregar llamada a `_initialize_mission_resumes_structure()` en el constructor
- Asegurar que siempre se ejecute al instanciar la clase

### **Fase 2: Extender create_consolidated_playbook()**
- Agregar llamada a `_consolidate_all_assets()` antes de generar contenido
- Mantener funcionalidad existente de consolidación

### **Fase 3: Actualizar Status-Checker**
- Modificar para validar que todos los DOCs estén en mission-resumes/
- Verificar que estructura de carpetas esté completa

### **Fase 4: Testing Completo**
- Probar con diferentes temas
- Verificar que no sobrescriba contenido existente
- Validar consolidación de todos los tipos de assets

## 📋 **VALIDACIONES NECESARIAS**

### **Checker debe verificar:**
1. ✅ Todos los DOC templates están en mission-resumes/
2. ✅ Estructura de carpetas completa (assets, charts, web-guides, support-docs)
3. ✅ Daily-works tienen respaldo consolidado en mission-resumes/
4. ✅ No hay pérdida de información en el proceso

### **Comandos de validación:**
```bash
# Verificar estructura completa
python3 scripts/status_checker/cli.py --detailed-mission-resumes

# Consolidar tema específico
python3 scripts/mission_resumer/cli.py --theme "BACKEND-API-SETUP" --output "backend-final"

# Validar que todo esté respaldado
python3 scripts/consistency_checker/cli.py --validate-mission-resumes
```

## 🎯 **RESULTADO ESPERADO**

**Al ejecutar mission-resumer:**
1. **Automáticamente** crea estructura completa en mission-resumes/
2. **Pre-carga** todos los DOC templates vacíos
3. **Consolida** todo el contenido de daily-works
4. **Mantiene** mission-resumes/ como punto único de verdad
5. **Preserva** contenido existente (no sobrescribe)

## 📊 **MÉTRICAS DE ÉXITO**

- ✅ 12 DOC templates pre-cargados automáticamente
- ✅ 4 carpetas base creadas (assets, charts, web-guides, support-docs)
- ✅ 100% de assets consolidados desde daily-works
- ✅ 0 pérdida de información en el proceso
- ✅ Status-checker valida completitud de mission-resumes/

---

**Este plan asegura que mission-resumes/ sea el punto único donde todo se consolida automáticamente, manteniendo la estructura limpia y organizada.**
