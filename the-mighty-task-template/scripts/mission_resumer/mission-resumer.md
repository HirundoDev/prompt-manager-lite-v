# Mission Resumer - Documentación del Script

## 📋 Propósito

El script `mission-resumer.py` consolida múltiples sesiones de trabajo en resúmenes ejecutivos inteligentes, excluyendo automáticamente contenido de template y preservando solo trabajo significativo.

## 🎯 Funcionalidades Principales

### ✅ Consolidación Inteligente
- **Detección de contenido real**: Distingue entre templates vacíos y trabajo completado
- **Filtrado automático**: Excluye placeholders y contenido de template
- **Fusión sin duplicación**: Evita repetir información entre sesiones
- **Preservación de contexto**: Mantiene estructura y metadatos importantes

### 🔍 Análisis de Sesiones
- **Escaneo automático**: Detecta todas las sesiones disponibles
- **Análisis de calidad**: Evalúa completitud y significancia del contenido
- **Métricas de progreso**: Calcula porcentajes de completitud
- **Validación previa**: Verifica que las sesiones sean apropiadas para consolidar

### 📊 Gestión de Assets
- **Copia inteligente**: Transfiere solo assets relevantes
- **Organización automática**: Estructura assets por sesión origen
- **Preservación de metadatos**: Mantiene timestamps y permisos

## 🔧 Arquitectura Modular

### Estructura de Archivos
```
scripts/mission_resumer/
├── __init__.py              # Inicialización del módulo
├── resumer.py              # Lógica principal de consolidación
├── cli.py                  # Interface de línea de comandos
└── mission-resumer.md      # Esta documentación
```

### Dependencias Compartidas
- `shared/template_detector.py` - Detección avanzada de templates
- `shared/playbook_registry.py` - Registro de playbooks y temas
- `shared/colored_output.py` - Output consistente y colorido

## 🚀 Uso del Script

### Comandos Básicos
```bash
# Consolidar todas las sesiones
python scripts/mission-resumer.py --output "SPRINT-01-SUMMARY"

# Consolidar por tema específico
python scripts/mission-resumer.py --theme "BACKEND-API-SETUP" --output "API-DEVELOPMENT"

# Consolidar sesiones específicas
python scripts/mission-resumer.py --sessions "2025-01-20_BACKEND-API-SETUP,2025-01-21_FRONTEND-COMPONENTS" --output "WEEK-01"

# Listar sesiones disponibles
python scripts/mission-resumer.py --list-sessions
```

### Opciones Avanzadas
```bash
# Filtrar por completitud mínima
python scripts/mission-resumer.py --output "QUALITY-SUMMARY" --min-completion 50

# Excluir sesiones solo con templates
python scripts/mission-resumer.py --output "CONTENT-ONLY" --exclude-templates

# Solo validar sin consolidar
python scripts/mission-resumer.py --validate-only --theme "TESTING-STRATEGY"

# Forzar sobrescritura
python scripts/mission-resumer.py --output "EXISTING-SUMMARY" --force

# Modo silencioso
python scripts/mission-resumer.py --output "FINAL-REPORT" --quiet
```

## 🔍 Proceso de Consolidación

### 1. Escaneo de Sesiones
- **Detección automática**: Busca directorios en `daily-work/`
- **Parseo de nombres**: Extrae fecha y tema de nombres de sesión
- **Análisis de contenido**: Evalúa cada archivo por separado
- **Cálculo de métricas**: Determina completitud y calidad

### 2. Validación Previa
- **Contenido significativo**: Verifica que al menos una sesión tenga trabajo real
- **Consistencia de temas**: Advierte sobre múltiples temas
- **Detección de duplicados**: Identifica sesiones duplicadas por fecha
- **Calidad promedio**: Evalúa si vale la pena consolidar

### 3. Filtrado Inteligente
- **Exclusión de templates**: Remueve líneas y secciones de template
- **Preservación de contenido**: Mantiene solo trabajo significativo
- **Limpieza de formato**: Elimina espacios excesivos y formato inconsistente
- **Estructuración**: Organiza contenido por sesión y tipo

### 4. Generación de Salida
- **Resumen ejecutivo**: Estadísticas y métricas consolidadas
- **Índice de sesiones**: Lista detallada de sesiones incluidas
- **Contenido consolidado**: Trabajo significativo organizado
- **Metadatos**: Información de trazabilidad y proceso

## 📊 Análisis de Contenido

### Métricas Calculadas
- **Completitud**: Porcentaje de contenido vs templates
- **Calidad**: Score basado en significancia del contenido
- **Cobertura**: Archivos procesados vs archivos totales
- **Assets**: Cantidad de evidencias y archivos de apoyo

### Tipos de Contenido Detectados
- **Template puro**: Solo placeholders y estructura base
- **Contenido parcial**: Mezcla de templates y trabajo real
- **Contenido completo**: Trabajo significativo sin templates
- **Assets**: Archivos de evidencia, capturas, logs

### Criterios de Exclusión
- Líneas que contienen solo `[TODO]` o placeholders
- Secciones con estructura de template sin contenido
- Archivos que no superan umbral mínimo de completitud
- Duplicados exactos entre sesiones

## 🗂️ Estructura de Salida

### Directorio Consolidado
```
mission-resumes/OUTPUT-NAME/
├── OUTPUT-NAME-CONSOLIDATED.md    # Documento principal
├── consolidation-log.json         # Log detallado del proceso
└── assets/                        # Assets copiados por sesión
    ├── SESSION-1/
    ├── SESSION-2/
    └── ...
```

### Contenido del Documento Principal
1. **Header**: Metadatos y timestamp
2. **Resumen Ejecutivo**: Estadísticas consolidadas
3. **Índice de Sesiones**: Lista con métricas por sesión
4. **Contenido Consolidado**: Trabajo significativo por sesión
5. **Assets y Evidencias**: Referencias a archivos copiados
6. **Metadatos**: Información de trazabilidad

## 🔧 Configuración y Personalización

### Filtros Disponibles
- `--min-completion`: Porcentaje mínimo de completitud (default: 10%)
- `--exclude-templates`: Excluir sesiones solo con templates
- `--theme`: Filtrar por tema específico
- `--sessions`: Especificar sesiones exactas

### Opciones de Comportamiento
- `--force`: Sobrescribir resúmenes existentes
- `--quiet`: Reducir output de consola
- `--validate-only`: Solo validar sin consolidar

## 📈 Mejoras v2.0

### Nuevas Características
- ✅ **Detección inteligente**: TemplateDetector para filtrado preciso
- ✅ **Análisis de calidad**: Métricas detalladas de completitud
- ✅ **Consolidación selectiva**: Filtros avanzados por tema y calidad
- ✅ **Logging completo**: Trazabilidad detallada del proceso
- ✅ **Gestión de assets**: Copia inteligente de evidencias

### Compatibilidad
- ✅ **Backward compatible**: Funciona con sesiones existentes
- ✅ **Migración automática**: Adapta formatos antiguos
- ✅ **Preservación**: No pierde información de sesiones anteriores

## 🐛 Manejo de Errores

### Errores Comunes
- **No hay sesiones**: Verifica que existan directorios en `daily-work/`
- **Solo templates**: Usa `--exclude-templates` o completa sesiones
- **Resumen existe**: Usa `--force` para sobrescribir
- **Tema inválido**: Verifica nombres de tema disponibles

### Códigos de Salida
- `0`: Consolidación exitosa
- `1`: Error de validación o parámetros
- `2`: Error de sistema o permisos

## 🔄 Integración con Otros Scripts

### Flujo Recomendado
1. **generate-daily.py** → Crear sesiones base
2. **playbook-processor.py** → Generar templates específicos
3. **[Trabajo manual]** → Completar contenido en sesiones
4. **mission-resumer.py** → Consolidar trabajo completado
5. **consistency-checker.py** → Validar integridad final

### Archivos Utilizados
- `daily-work/*/pending-tasks-*.md` → Contenido principal
- `daily-work/*/support-docs/*.md` → Documentos de apoyo
- `daily-work/*/assets/**` → Evidencias y archivos
- `daily-work/.tracking.json` → Metadatos de sesiones

## 📝 Notas de Desarrollo

### Principios de Diseño
- **Inteligencia**: Detección automática de contenido significativo
- **Preservación**: No perder trabajo importante
- **Organización**: Estructura clara y navegable
- **Trazabilidad**: Log completo del proceso de consolidación

### Testing Recomendado
- Probar con sesiones de diferentes temas
- Validar filtrado de templates vs contenido real
- Verificar copia correcta de assets
- Confirmar compatibilidad con formatos existentes