# Consistency Checker - Documentación del Script

## 📋 Propósito

El script `consistency-checker.py` verifica la integridad completa del sistema The Mighty Task, detectando inconsistencias, templates no completados, duplicados y problemas de estructura con validaciones inteligentes.

## 🎯 Funcionalidades Principales

### ✅ Verificación Modular
- **Estructura del proyecto**: Directorios y archivos críticos
- **Consistencia de playbooks**: Validación usando PlaybookRegistry
- **Sesiones diarias**: Análisis de contenido y completitud
- **Detección de templates**: Precisión del TemplateDetector
- **Sistema de tracking**: Consistencia de metadatos
- **Duplicados**: Detección avanzada entre archivos y sesiones

### 🔍 Análisis Inteligente
- **Calidad de contenido**: Distingue templates de trabajo real
- **Métricas de completitud**: Porcentajes de progreso por sesión
- **Salud del sistema**: Evaluación general del estado
- **Detección de anomalías**: Patrones inconsistentes o problemáticos

### 📊 Reportes Detallados
- **Resumen ejecutivo**: Estadísticas clave del sistema
- **Categorización de issues**: Críticos, mayores, advertencias
- **Exportación**: Reportes en Markdown y JSON
- **Recomendaciones**: Sugerencias de mejora automáticas

## 🔧 Arquitectura Modular

### Estructura de Archivos
```
scripts/consistency_checker/
├── __init__.py              # Inicialización del módulo
├── checker.py              # Clase principal ConsistencyChecker
├── checker_methods.py      # Métodos de verificación específicos
├── checker_utils.py        # Utilidades y verificaciones adicionales
├── report_generator.py     # Generador de reportes
├── cli.py                  # Interface de línea de comandos
└── consistency-checker.md  # Esta documentación
```

### Dependencias Compartidas
- `shared/template_detector.py` - Detección inteligente de templates
- `shared/playbook_registry.py` - Registro centralizado de playbooks
- `shared/colored_output.py` - Output consistente y colorido

## 🚀 Uso del Script

### Comandos Básicos
```bash
# Verificación completa del sistema
python scripts/consistency-checker.py --scan-all

# Verificar solo estructura
python scripts/consistency-checker.py --check-structure

# Verificar solo sesiones
python scripts/consistency-checker.py --check-sessions

# Verificar solo playbooks
python scripts/consistency-checker.py --check-playbooks
```

### Verificaciones Específicas
```bash
# Verificar detección de templates
python scripts/consistency-checker.py --check-templates

# Verificar sistema de tracking
python scripts/consistency-checker.py --check-tracking

# Verificar duplicados
python scripts/consistency-checker.py --check-duplicates
```

### Opciones de Salida
```bash
# Generar reporte detallado
python scripts/consistency-checker.py --scan-all --report-file "report.md"

# Solo issues críticos
python scripts/consistency-checker.py --scan-all --critical-only

# Salida JSON
python scripts/consistency-checker.py --scan-all --json-output

# Modo silencioso
python scripts/consistency-checker.py --scan-all --quiet
```

## 🔍 Tipos de Verificaciones

### 1. Estructura del Proyecto
- **Directorios requeridos**: `daily-work/`, `playbooks/`, `mission-resumes/`, `scripts/`
- **Archivos críticos**: `PLAN-COMPLETO.md`, `template-pendingtask.md`
- **Estructura modular**: Verificación de módulos de scripts
- **Permisos y accesibilidad**: Validación de lectura/escritura

### 2. Consistencia de Playbooks
- **Integridad del registro**: Validación de PlaybookRegistry
- **Mapeos de temas**: Consistencia entre temas y playbooks
- **Archivos faltantes**: Playbooks referenciados pero no existentes
- **Templates duplicados**: Detección de contenido repetido

### 3. Sesiones Diarias
- **Estructura de sesión**: Archivos principales y subdirectorios
- **Calidad de contenido**: Análisis de completitud vs templates
- **Consistencia de nombres**: Formato de directorios y archivos
- **Assets y evidencias**: Verificación de archivos de apoyo

### 4. Detección de Templates
- **Precisión del detector**: Casos de prueba automáticos
- **Falsos positivos/negativos**: Identificación de errores
- **Patrones de template**: Validación de expresiones regulares
- **Calibración**: Ajuste de umbrales de detección

### 5. Sistema de Tracking
- **Archivo `.tracking.json`**: Estructura y validez
- **Consistencia de datos**: Sesiones trackeadas vs existentes
- **Metadatos completos**: Información requerida presente
- **Sincronización**: Coherencia entre tracking y realidad

### 6. Duplicados
- **Entre playbooks**: Templates idénticos o muy similares
- **Entre sesiones**: Contenido repetido en diferentes fechas
- **Algoritmo de similitud**: Comparación inteligente de contenido
- **Umbrales configurables**: Sensibilidad de detección

## 📈 Métricas y Estadísticas

### Métricas Calculadas
- **Sesiones totales**: Cantidad de directorios de sesión
- **Sesiones con contenido**: Sesiones con trabajo significativo
- **Solo templates**: Sesiones que contienen únicamente templates
- **Calidad promedio**: Score promedio de completitud
- **Completitud del sistema**: Métrica general de salud

### Indicadores de Salud
- **Good**: Sistema funcionando correctamente
- **Fair**: Algunos issues menores, funcionamiento aceptable
- **Poor**: Múltiples problemas, requiere atención
- **Critical**: Issues críticos, funcionamiento comprometido

### Códigos de Salida
- `0`: Verificación exitosa, sin issues críticos ni mayores
- `1`: Issues mayores detectados, requiere revisión
- `2`: Issues críticos detectados, requiere acción inmediata

## 🔧 Configuración y Personalización

### Umbrales Configurables
- **Similitud de duplicados**: 80% por defecto
- **Calidad mínima**: 10% completitud para considerar significativo
- **Ratio de templates**: 50% máximo de sesiones solo con templates
- **Precisión de detección**: 90% mínimo en casos de prueba

### Filtros Disponibles
- `--critical-only`: Solo mostrar issues críticos
- `--quiet`: Reducir output de consola
- `--json-output`: Formato estructurado para integración

## 📊 Integración con Otros Scripts

### Flujo Recomendado
1. **generate-daily.py** → Crear sesiones
2. **playbook-processor.py** → Generar templates
3. **[Trabajo manual]** → Completar contenido
4. **consistency-checker.py** → Verificar integridad
5. **mission-resumer.py** → Consolidar si todo está bien

### Archivos Analizados
- `daily-work/*/pending-tasks-*.md` → Contenido principal
- `daily-work/*/support-docs/*.md` → Documentos de apoyo
- `daily-work/.tracking.json` → Metadatos de tracking
- `playbooks/**/*.md` → Playbooks base
- `mission-resumes/*/` → Consolidaciones existentes

## 🐛 Manejo de Errores

### Errores Críticos
- **Directorio raíz incorrecto**: Falta `PLAN-COMPLETO.md`
- **Estructura corrupta**: Directorios principales faltantes
- **Tracking corrupto**: JSON inválido o estructura incorrecta
- **Permisos insuficientes**: No se puede leer/escribir archivos

### Errores Mayores
- **Archivos faltantes**: Playbooks referenciados no existen
- **Sesiones incompletas**: Archivos principales faltantes
- **Inconsistencias de registro**: Mapeos incorrectos
- **Metadatos inconsistentes**: Tracking desactualizado

### Advertencias
- **Alto ratio de templates**: Muchas sesiones sin completar
- **Duplicados detectados**: Contenido repetido
- **Baja calidad promedio**: Sesiones poco desarrolladas
- **Detección imprecisa**: Errores en clasificación de templates

## 📝 Notas de Desarrollo

### Principios de Diseño
- **Modularidad**: Separación clara de responsabilidades
- **Extensibilidad**: Fácil agregar nuevas verificaciones
- **Robustez**: Manejo graceful de errores
- **Usabilidad**: Output claro y accionable

### Testing Recomendado
- Probar con proyectos en diferentes estados
- Validar detección de todos los tipos de issues
- Verificar precisión de métricas calculadas
- Confirmar funcionalidad de reportes exportados