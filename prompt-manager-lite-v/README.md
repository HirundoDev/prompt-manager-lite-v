# Prompt Manager Lite v

## 🎯 Introducción

Prompt Manager Lite es una versión simplificada y portátil del Prompt Manager diseñada para documentar rápidamente proyectos usando un esquema modular flexible. **Plug & Play**: copia la carpeta y comienza a documentar.

## 📁 Estructura de Carpetas

- **docs/**: Plantillas de documentos para la configuración inicial y definición del proyecto
- **schemas/**: Conjunto de schemas JSON modulares para modelar componentes clave del proyecto
- **prompt_playbooks/**: Guías y manuales que ayudan en el proceso de planificación y documentación
- **features/**: Templates y ejemplos para documentar funcionalidades
- **bugs/**: Templates y ejemplos para documentar bugs
- **operations/**: Templates y ejemplos para documentar tareas
- **proposals/**: Templates y ejemplos para documentar ideas

## 🚀 Flujo de Trabajo

### 1. **Establecer Línea Base**
```bash
# Crear snapshot inicial de todos los archivos
python3 verify_integrity.py store
```

### 2. **Completar Documentación**
- Rellena los documentos en `docs/` usando las guías en `prompt_playbooks/`
- Completa los schemas en `schemas/master_blueprint_parts/`
- Usa los templates en `features/`, `bugs/`, `operations/`, `proposals/`

### 3. **Verificar Progreso**
```bash
# Ver qué archivos han sido modificados vs plantillas sin completar
python3 verify_integrity.py
```

### 4. **Generar Master Blueprint**
```bash
# Combinar todos los schemas en un archivo JSON maestro
python3 combine_schemas.py
```

### 5. **Usar como Fuente de Verdad**
- El archivo `master_blueprint_combined.json` contiene toda la documentación estructurada
- Úsalo como contexto para agentes IA o como referencia del proyecto

## 🔍 Scripts Disponibles

### **verify_integrity.py**
Verifica qué archivos han sido modificados:
- **Store**: `python3 verify_integrity.py store` - Guarda estado inicial
- **Check**: `python3 verify_integrity.py` - Verifica cambios
- **Detección inteligente**: Cuenta placeholders como `[Nombre del Proyecto]` para determinar completitud

### **combine_schemas.py**
Combina schemas modulares:
- Fusiona todos los archivos en `schemas/master_blueprint_parts/`
- Genera `master_blueprint_combined.json`
- Valida que los schemas requeridos estén presentes

## 📊 Estados de Archivos

- ✅ **COMPLETADO**: Sin placeholders, documentación lista
- 🔄 **EN PROGRESO**: Algunos placeholders completados
- 📝 **PLANTILLA**: Sin modificar, necesita completarse
- ⚠️ **MODIFICADO**: Cambios detectados
- 🚫 **FALTANTE**: Archivo eliminado o movido

## 🎯 Ventajas del Sistema

- **Plug & Play**: Copia y comienza a usar inmediatamente
- **Trazabilidad**: Sabe exactamente qué está completo y qué falta
- **Modular**: Cada schema y documento es independiente
- **Portable**: No depende del CLI complejo del Prompt Manager
- **Inteligente**: Detecta automáticamente el progreso de documentación
