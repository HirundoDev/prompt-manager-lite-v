# Generate Daily - Documentación del Script

## 📋 Propósito

El script `generate-daily.py` es responsable de crear la estructura básica de sesiones de trabajo diarias con validaciones anti-duplicación y detección inteligente de templates.

## 🎯 Funcionalidades Principales

### ✅ Validaciones Avanzadas
- **Anti-duplicación**: Detecta sesiones existentes y previene sobrescritura accidental
- **Detección de templates**: Distingue entre contenido real y templates vacíos
- **Validación de parámetros**: Verifica fechas, temas y consistencia de playbooks

### 🏗️ Creación de Estructura
- **Directorio principal**: `daily-work/YYYY-MM-DD_THEME/`
- **Subdirectorios**: `support-docs/`, `assets/`, `charts/`
- **Archivo principal**: `pending-tasks-YYYY-MM-DD_THEME.md`
- **READMEs**: Documentación automática en subdirectorios

### 📊 Sistema de Tracking
- **Registro centralizado**: Actualiza `.tracking.json` automáticamente
- **Metadatos completos**: Fecha, tema, archivos creados, playbooks asociados
- **Estadísticas**: Contadores y métricas del sistema

## 🔧 Arquitectura Modular

### Estructura de Archivos
```
scripts/generate_daily/
├── __init__.py          # Inicialización del módulo
├── generator.py         # Lógica principal del generador
├── cli.py              # Interface de línea de comandos
└── generate-daily.md   # Esta documentación
```

### Dependencias Compartidas
- `shared/template_detector.py` - Detección de templates vs contenido real
- `shared/playbook_registry.py` - Registro centralizado de playbooks
- `shared/colored_output.py` - Output colorido consistente

## 🚀 Uso del Script

### Comandos Básicos
```bash
# Crear sesión para hoy
python scripts/generate-daily.py --theme "BACKEND-API-SETUP"

# Crear sesión con fecha específica
python scripts/generate-daily.py --theme "FRONTEND-COMPONENTS" --date "2025-01-22"

# Modo automático
python scripts/generate-daily.py --auto

# Listar temas disponibles
python scripts/generate-daily.py --list-themes
```

### Opciones Avanzadas
```bash
# Forzar sobrescritura
python scripts/generate-daily.py --theme "API-DESIGN" --force

# Verificar solo duplicados
python scripts/generate-daily.py --theme "BACKEND-API-SETUP" --check-duplicates

# Modo silencioso
python scripts/generate-daily.py --theme "DATABASE-SCHEMA" --quiet

# Omitir validaciones (no recomendado)
python scripts/generate-daily.py --theme "TESTING-STRATEGY" --skip-validation
```

## 🔍 Validaciones Implementadas

### 1. Validación de Parámetros
- **Formato de fecha**: Debe ser YYYY-MM-DD
- **Fechas futuras**: No permitidas
- **Temas válidos**: Debe existir en mapeo de playbooks
- **Consistencia de playbooks**: Verifica que existan archivos asociados

### 2. Detección de Duplicación
- **Sesiones existentes**: Verifica si ya existe la sesión
- **Contenido significativo**: Distingue templates vacíos de trabajo real
- **Templates duplicados**: Detecta templates idénticos entre sesiones
- **Playbooks duplicados**: Identifica duplicación en playbooks base

### 3. Análisis de Contenido
- **Calidad de contenido**: Evalúa completitud y significancia
- **Placeholders**: Detecta elementos de template no completados
- **Métricas de completitud**: Calcula porcentajes de trabajo realizado

## 📈 Mejoras v2.0

### Nuevas Características
- ✅ **Detección inteligente**: Distingue templates de contenido real
- ✅ **Registro centralizado**: PlaybookRegistry para consistencia
- ✅ **Validaciones robustas**: Previene duplicación y errores
- ✅ **Arquitectura modular**: Separación clara de responsabilidades
- ✅ **Tracking mejorado**: Metadatos completos y estadísticas

### Compatibilidad
- ✅ **Backward compatible**: Funciona con sesiones existentes
- ✅ **Migración automática**: Actualiza tracking a nuevo formato
- ✅ **Preservación de datos**: No pierde información existente

## 🔧 Configuración

### Temas Disponibles
El script utiliza el mapeo definido en `PlaybookRegistry`:
- `BACKEND-API-SETUP` → DOC006, DOC007, DOC008
- `FRONTEND-COMPONENTS` → DOC003, DOC004, DOC005
- `DATABASE-SCHEMA` → DOC009
- Y más...

### Personalización de Templates
El template base se lee desde `template-pendingtask.md` y se personaliza con:
- Fecha y tema específicos
- Lista de playbooks relevantes
- Contadores de tareas automáticos
- Secciones específicas del tema

## 🐛 Manejo de Errores

### Errores Comunes
- **Directorio incorrecto**: Verifica presencia de `PLAN-COMPLETO.md`
- **Tema inválido**: Muestra lista de temas disponibles
- **Fecha inválida**: Valida formato YYYY-MM-DD
- **Sesión existente**: Requiere `--force` para sobrescribir contenido real

### Códigos de Salida
- `0`: Éxito
- `1`: Error de parámetros o validación
- `2`: Error de sistema o permisos

## 🔄 Integración con Otros Scripts

### Flujo Recomendado
1. **generate-daily.py** → Crear estructura básica
2. **playbook-processor.py** → Generar templates específicos
3. **consistency-checker.py** → Verificar integridad
4. **report-generator.py** → Generar reportes finales

### Archivos Generados
- `pending-tasks-*.md` → Usado por report-generator
- `.tracking.json` → Usado por todos los scripts
- `support-docs/` → Usado por playbook-processor
- `assets/` → Usado por mission-resumer

## 📝 Notas de Desarrollo

### Principios de Diseño
- **Modularidad**: Separación clara de responsabilidades
- **Reutilización**: Módulos compartidos entre scripts
- **Robustez**: Validaciones exhaustivas y manejo de errores
- **Usabilidad**: Interface clara y mensajes informativos

### Testing
- Validar con diferentes temas y fechas
- Probar escenarios de duplicación
- Verificar integración con otros scripts
- Confirmar preservación de datos existentes