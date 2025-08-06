# 📚 Guía Completa de Referencia - Prompt Manager Lite v

**⚠️ IMPORTANTE: Esta guía debe ser leída al inicio de cada conversación para entender el flujo de trabajo correcto.**

---

## 🏁 **CONCEPTO FUNDAMENTAL - LEER PRIMERO**

### **🔑 La carpeta `prompt-manager-lite-v` ES TODO el sistema de documentación**

**📁 Esta carpeta contiene:**
- ✅ TODOS los documentos necesarios para cualquier proyecto
- ✅ TODOS los schemas JSON para el master blueprint
- ✅ TODAS las guías (playbooks) para completar cada archivo
- ✅ TODOS los scripts de verificación y combinación
- ✅ TODAS las plantillas para features, bugs, tareas, ideas

**🎯 Tu trabajo es:**
- ❌ NO crear documentos nuevos
- ✅ COMPLETAR los placeholders de los archivos que YA ESTÁN aquí
- ✅ USAR los playbooks para entender qué poner en cada archivo
- ✅ VERIFICAR constantemente el progreso con los scripts

**🔄 Flujo simple:**
1. Copias esta carpeta `prompt-manager-lite-v` a tu proyecto
2. Completas los archivos existentes con información real
3. Generas el master blueprint final
4. Tienes documentación completa y estructurada

---

## 🎯 **Principios Fundamentales**

### **🚫 REGLAS ESTRICTAS - NUNCA VIOLER:**

1. **NO CREAR ARCHIVOS NUEVOS** - Solo usar los existentes
2. **NO MODIFICAR ESTRUCTURA** - Respetar carpetas y organización
3. **SIEMPRE VERIFICAR** - Usar comandos de verificación antes y después
4. **SEGUIR PLAYBOOKS** - Cada archivo tiene su guía específica
5. **COMPLETAR PLACEHOLDERS** - Reemplazar todos los `[placeholder]` correctamente

---

## 🗂️ **Estructura del Sistema (NO MODIFICAR)**

```
prompt-manager-lite-v/
├── docs/                           # 📝 Documentos del proyecto (36 archivos)
├── schemas/                        # ⚙️ Schemas JSON modulares (27 archivos)
│   └── master_blueprint_parts/     # Partes del blueprint maestro
├── prompt_playbooks/               # 📚 Guías para completar cada archivo
├── features/                       # 🚀 Funcionalidades (usar templates existentes)
├── bugs/                           # 🐛 Bugs (usar templates existentes)
├── operations/                     # 🔧 Tareas (usar templates existentes)
├── proposals/                      # 💡 Ideas (usar templates existentes)
├── combine_schemas.py              # 🔗 Script para generar master blueprint
├── verify_integrity.py            # 🔍 Script de verificación
├── GUIA_COMPLETA_DE_USO.md         # 📖 ESTA GUÍA - Manual completo
├── ARCHIVO_REFERENCIA_COMPLETA.md  # 🗺️ Mapa detallado de todos los archivos
└── file_integrity.json            # 📊 Estado de archivos (generado)
```

**🗺️ REFERENCIA RÁPIDA:** Si no sabes qué hace un archivo específico, consulta `ARCHIVO_REFERENCIA_COMPLETA.md`

---

## ⚡ **Comandos Esenciales (MEMORIZAR)**

### **🔍 Verificación de Estado**
```bash
# SIEMPRE ejecutar antes de empezar
python3 verify_integrity.py

# Primera vez o después de cambios mayores
python3 verify_integrity.py store
```

### **🔗 Generar Master Blueprint**
```bash
# Solo cuando schemas estén completos
python3 combine_schemas.py
```

---

## 📋 **Flujo de Trabajo Obligatorio**

### **PASO 1: Verificar Estado Actual**
```bash
python3 verify_integrity.py
```
**Analizar output:**
- `📝 PLANTILLA` = Necesita completarse
- `🔄 EN PROGRESO` = Parcialmente completado
- `✅ COMPLETADO` = Terminado
- `🚫 FALTANTE` = Archivo perdido

### **PASO 2: Seleccionar Archivo a Completar**
**SOLO trabajar con archivos existentes:**
- `docs/DOC000-ProjectBrief.md`
- `docs/DOC001-ProjectREADME.md`
- `schemas/master_blueprint_parts/projectInfo.json`
- etc.

### **PASO 3: Consultar Documentación**
**Antes de modificar CUALQUIER archivo:**
```bash
# Para saber QUÉ HACE el archivo
cat ARCHIVO_REFERENCIA_COMPLETA.md

# Para saber CÓMO completarlo
ls prompt_playbooks/playbook-*
cat prompt_playbooks/playbook-[nombre-archivo].md
```

### **PASO 4: Completar Placeholders**
**Reemplazar TODOS los placeholders:**
- `[Nombre del Proyecto]` → Nombre real
- `[Descripción]` → Descripción real
- `[placeholder]` → Contenido real

### **PASO 5: Verificar Cambios**
```bash
python3 verify_integrity.py
```
**Confirmar que el archivo cambió de estado.**

### **PASO 6: Repetir Ciclo**
**Continuar con siguiente archivo prioritario.**

---

## 🎯 **Archivos por Tipo y Propósito**

### **📝 Documentos (`docs/`)**
**Cada archivo tiene propósito específico:**
- `DOC000-ProjectBrief.md` → Visión general del proyecto
- `DOC001-ProjectREADME.md` → README principal
- `DOC004-FrontendArchitecture.md` → Arquitectura frontend
- `DOC006-BackendArchitecture.md` → Arquitectura backend
- `DOC008-APISpecification.md` → Especificación de API
- **etc. (36 documentos totales)**

### **⚙️ Schemas (`schemas/master_blueprint_parts/`)**
**Cada schema modela una parte específica:**
- `projectInfo.json` → Información básica
- `architecture.json` → Arquitectura general
- `dataModel.json` → Modelo de datos
- `apiContract.json` → Contratos de API
- **etc. (27 schemas totales)**

### **🚀 Features (`features/`)**
**Para nuevas funcionalidades:**
- `template.md` → Plantilla base (NO MODIFICAR)
- `F000-Ejemplo-de-Feature/` → Ejemplo de referencia
- **Usar template.md para copiar cuando sea necesario**

### **🐛 Bugs (`bugs/`)**
**Para documentar errores:**
- `template.md` → Plantilla base (NO MODIFICAR)
- `B000-Ejemplo-de-Bug/` → Ejemplo de referencia

### **🔧 Operations (`operations/`)**
**Para tareas y operaciones:**
- `template.md` → Plantilla base (NO MODIFICAR)  
- `T000-Ejemplo-de-Tarea/` → Ejemplo de referencia

### **💡 Proposals (`proposals/`)**
**Para ideas y propuestas:**
- `template.md` → Plantilla base (NO MODIFICAR)
- `IDEA000-Ejemplo-de-Idea/` → Ejemplo de referencia

---

## 🚨 **Errores Comunes y Cómo Evitarlos**

### **❌ ERROR: Crear archivos nuevos**
```bash
# MAL - NO HACER
touch docs/MI_NUEVO_DOC.md
```
```bash
# BIEN - USAR EXISTENTES
# Completar docs/DOC000-ProjectBrief.md
```

### **❌ ERROR: Modificar estructura**
```bash
# MAL - NO HACER
mkdir mi_carpeta_nueva
```
```bash
# BIEN - RESPETAR ESTRUCTURA
# Trabajar dentro de carpetas existentes
```

### **❌ ERROR: No verificar antes de trabajar**
```bash
# MAL - NO HACER
# Empezar a editar sin verificar
```
```bash
# BIEN - SIEMPRE VERIFICAR
python3 verify_integrity.py
# Luego trabajar
```

### **❌ ERROR: Ignorar playbooks**
```bash
# MAL - NO HACER
# Completar archivo sin consultar guía
```
```bash
# BIEN - CONSULTAR PLAYBOOK
cat prompt_playbooks/playbook-projectInfo.md
# Luego completar siguiendo guía
```

### **❌ ERROR: Dejar placeholders**
```bash
# MAL - DEJAR ASÍ
"projectName": "[Nombre del Proyecto]"
```
```bash
# BIEN - COMPLETAR
"projectName": "Mi Sistema de Gestión"
```

---

## 📊 **Sistema de Monitoreo**

### **Estados de Archivos:**
- **📝 PLANTILLA** (`X placeholders`) = Sin empezar, necesita trabajo
- **🔄 EN PROGRESO** (`Y/X placeholders`) = Parcialmente completado
- **✅ COMPLETADO** (`0 placeholders`) = Terminado correctamente
- **✨ SIN CAMBIOS** = Archivo sin placeholders, ya estaba completo
- **🚫 FALTANTE** = Archivo perdido o eliminado accidentalmente

### **Meta de Completitud:**
**Objetivo: Lograr el mayor número de archivos ✅ COMPLETADOS**

---

## 🎯 **Objetivo Final**

**Al seguir esta guía correctamente:**

✅ **Todos los archivos mantendrán su formato original**  
✅ **Todos los placeholders serán reemplazados con información real**  
✅ **La estructura del sistema permanecerá intacta**  
✅ **Se generará un master blueprint JSON completo**  
✅ **Tendrás documentación profesional y estructurada**  

---

## 🔄 **Recordatorio para Cada Sesión**

**Al empezar CUALQUIER conversación sobre este proyecto:**

1. ✅ Leer esta guía completa
2. ✅ Ejecutar `python3 verify_integrity.py` 
3. ✅ Identificar archivos en estado `📝 PLANTILLA`
4. ✅ Consultar playbook correspondiente
5. ✅ Completar placeholders respetando formato
6. ✅ Verificar cambios con `python3 verify_integrity.py`
7. ✅ Repetir ciclo con siguiente archivo prioritario

**🚫 NUNCA crear archivos nuevos, SIEMPRE usar los existentes.**

---

**📋 Esta es la única forma correcta de trabajar con Prompt Manager Lite. Cualquier desviación compromete la integridad del sistema.**
