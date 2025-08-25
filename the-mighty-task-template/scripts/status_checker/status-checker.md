# Status Checker - Documentación del Script

## 📋 Propósito

El script `status-checker.py` proporciona una vista general del estado del sistema The Mighty Task, analizando la calidad del contenido, métricas de productividad y generando recomendaciones inteligentes para optimizar el flujo de trabajo.

## 🎯 Funcionalidades Principales

### ✅ Dashboard de Salud
- **Score general del sistema**: Métrica combinada de salud
- **Productividad**: Ratio de sesiones con contenido significativo
- **Consistencia**: Estado de playbooks y configuración
- **Completitud**: Porcentaje promedio de trabajo completado

### 🔍 Análisis Inteligente
- **Calidad de sesiones**: Distingue templates de trabajo real
- **Distribución por tema**: Análisis de actividad por área
- **Actividad reciente**: Últimas sesiones y su estado
- **Detección de patrones**: Identificación de tendencias

### 💡 Recomendaciones Automáticas
- **Acciones críticas**: Problemas que requieren atención inmediata
- **Mejoras sugeridas**: Optimizaciones del flujo de trabajo
- **Comandos específicos**: Sugerencias de scripts a ejecutar
- **Mantenimiento**: Tareas de limpieza y organización

## 🔧 Arquitectura Modular

### Estructura de Archivos
```
scripts/status_checker/
├── __init__.py          # Inicialización del módulo
├── status.py           # Lógica principal de análisis
├── display.py          # Módulo de visualización y reportes
├── cli.py              # Interface de línea de comandos
└── status-checker.md   # Esta documentación
```

### Dependencias Compartidas
- `shared/template_detector.py` - Análisis de calidad de contenido
- `shared/playbook_registry.py` - Estado de playbooks y temas
- `shared/colored_output.py` - Output consistente y colorido

## 🚀 Uso del Script

### Comandos Básicos
```bash
# Estado general del sistema (default)
python scripts/status-checker.py

# Estado rápido en una línea
python scripts/status-checker.py --quick

# Análisis detallado de sesiones
python scripts/status-checker.py --detailed-sessions

# Solo métricas de calidad
python scripts/status-checker.py --quality-only
```

### Opciones de Salida
```bash
# Exportar reporte completo
python scripts/status-checker.py --export-report "status-report.md"

# Salida en formato JSON
python scripts/status-checker.py --json

# Modo silencioso
python scripts/status-checker.py --quiet

# Combinación: JSON silencioso
python scripts/status-checker.py --json --quiet
```

### Filtros Específicos
```bash
# Filtrar por tema
python scripts/status-checker.py --theme "BACKEND-API-SETUP"

# Solo sesiones de alta calidad
python scripts/status-checker.py --min-quality 70
```

## 📊 Métricas Calculadas

### Score de Salud General (0-100%)
Combinación ponderada de:
- **Productividad (60%)**: Ratio de sesiones con contenido vs templates
- **Consistencia (20%)**: Estado de playbooks y configuración
- **Completitud (20%)**: Calidad promedio del contenido

### Score de Productividad
- **Sesiones significativas**: Porcentaje con trabajo real vs solo templates
- **Alta calidad**: Porcentaje de sesiones >70% completitud
- **Actividad reciente**: Tendencia de trabajo en últimas sesiones

### Score de Consistencia
- **Salud de playbooks**: Estado del PlaybookRegistry
- **Temas configurados**: Porcentaje de temas sin problemas
- **Duplicados**: Impacto de templates duplicados

### Score de Completitud
- **Promedio de sesiones**: Completitud media de todas las sesiones
- **Tendencia de calidad**: Mejora o deterioro en el tiempo
- **Distribución**: Balance entre sesiones completas e incompletas

## 🎯 Tipos de Recomendaciones

### Acciones Críticas (Alta Prioridad)
- **Sin sesiones**: Sistema vacío, necesita inicialización
- **Configuración rota**: Problemas críticos de estructura
- **Datos corruptos**: Issues que impiden funcionamiento

### Mejoras Sugeridas (Prioridad Media)
- **Completar sesiones**: Alto ratio de templates sin completar
- **Consolidar trabajo**: Múltiples sesiones listas para mission-resume
- **Mejorar calidad**: Completitud promedio baja

### Mantenimiento (Baja Prioridad)
- **Limpiar duplicados**: Templates repetidos detectados
- **Actualizar playbooks**: Archivos faltantes o inconsistentes
- **Organizar assets**: Optimización de estructura

## 🔍 Análisis de Componentes

### 1. Sesiones de Trabajo
- **Total vs Significativas**: Ratio de trabajo real
- **Distribución por tema**: Actividad por área de trabajo
- **Calidad promedio**: Score de completitud general
- **Actividad reciente**: Últimas 5 sesiones por fecha

### 2. Playbooks y Temas
- **Temas disponibles**: Configuración completa
- **Playbooks faltantes**: Archivos referenciados no existentes
- **Templates duplicados**: Contenido repetido
- **Salud del registry**: Integridad de la configuración

### 3. Mission Resumes
- **Total consolidaciones**: Resúmenes creados
- **Distribución por tamaño**: Pequeños, medianos, grandes
- **Actividad de consolidación**: Frecuencia de uso
- **Sesiones promedio**: Eficiencia de consolidación

## 📈 Interpretación de Resultados

### Estados de Salud
- **Excelente (80-100%)**: Sistema funcionando óptimamente
- **Bueno (60-79%)**: Funcionamiento normal con mejoras menores
- **Necesita atención (40-59%)**: Problemas que afectan productividad
- **Requiere mejoras (<40%)**: Issues significativos que resolver

### Códigos de Salida
- `0`: Sistema saludable, sin acciones críticas
- `1`: Sistema necesita atención, pero funcional
- `2`: Acciones críticas pendientes, requiere intervención

### Indicadores Visuales
- ✅ **Verde**: Estado óptimo o completado
- ⚠️ **Amarillo**: Advertencias o mejoras sugeridas
- ❌ **Rojo**: Problemas críticos o faltantes
- 💡 **Azul**: Información o sugerencias

## 🔧 Configuración y Personalización

### Umbrales Configurables
- **Alta calidad**: >70% completitud por defecto
- **Sesión significativa**: >10% contenido no-template
- **Salud crítica**: <40% score general
- **Actividad reciente**: Últimas 5 sesiones

### Filtros Disponibles
- `--theme`: Analizar solo un tema específico
- `--min-quality`: Filtro de calidad mínima
- `--quiet`: Reducir output de consola
- `--json`: Formato estructurado para integración

## 📊 Integración con Otros Scripts

### Flujo de Monitoreo
1. **status-checker.py** → Evaluar estado actual
2. **generate-daily.py** → Crear sesiones si es necesario
3. **consistency-checker.py** → Verificar integridad si hay problemas
4. **mission-resumer.py** → Consolidar si hay suficiente contenido

### Uso en Automatización
```bash
# Script de monitoreo diario
#!/bin/bash
STATUS=$(python scripts/status-checker.py --quick --json)
HEALTH=$(echo $STATUS | jq -r '.quality_metrics.overall_health_score')

if (( $(echo "$HEALTH < 60" | bc -l) )); then
    echo "Sistema necesita atención"
    python scripts/consistency-checker.py --scan-all
fi
```

## 🔄 Casos de Uso Comunes

### Inicio de Día
```bash
# Verificar estado antes de trabajar
python scripts/status-checker.py --quick
```

### Revisión Semanal
```bash
# Análisis completo con reporte
python scripts/status-checker.py --export-report "weekly-status.md"
```

### Debugging de Problemas
```bash
# Análisis detallado de sesiones
python scripts/status-checker.py --detailed-sessions
```

### Integración CI/CD
```bash
# Verificación automática en pipeline
python scripts/status-checker.py --json --quiet > status.json
```

## 📝 Notas de Desarrollo

### Principios de Diseño
- **Claridad**: Información fácil de entender y accionable
- **Eficiencia**: Análisis rápido sin impacto en rendimiento
- **Extensibilidad**: Fácil agregar nuevas métricas
- **Integración**: Compatible con otros scripts del sistema

### Testing Recomendado
- Probar con proyectos en diferentes estados de salud
- Validar precisión de métricas calculadas
- Verificar recomendaciones generadas
- Confirmar exportación de reportes