# 🚀 Prompt Inicial para Prompt Manager Lite v

**⚠️ LEER ESTO ANTES DE CUALQUIER ACCIÓN**

## 🎯 **Context & Mission**

Estás trabajando con **Prompt Manager Lite**, un sistema de documentación estructurada que genera un **master blueprint JSON** como fuente única de verdad para proyectos de software.

### **📁 IMPORTANTE: La carpeta `prompt-manager-lite-v` ES el sistema completo**

- Esta carpeta `prompt-manager-lite-v` contiene TODA la documentación necesaria
- Se copia completa a cualquier proyecto 
- Los archivos que están aquí SON los documentos del proyecto
- NO necesitas crear documentos nuevos - solo completar los existentes

**🎯 Objetivo:** Completar placeholders de los archivos que YA ESTÁN en esta carpeta  
**🚫 PROHIBIDO:** Crear archivos nuevos - TODO ya existe aquí

---

## ⚡ **PROTOCOLO OBLIGATORIO DE INICIO**

### **PASO 1: Verificar Estado Actual (SIEMPRE PRIMERO)**
```bash
python3 verify_integrity.py
```

**📊 Analizar output para identificar:**
- `📝 PLANTILLA` (X placeholders) = Necesita completarse
- `🔄 EN PROGRESO` (Y/X placeholders) = Parcialmente listo
- `✅ COMPLETADO` (0 placeholders) = Terminado
- `🚫 FALTANTE` = Archivo perdido

### **PASO 2: Leer Documentación Esencial**
```bash
cat GUIA_COMPLETA_DE_USO.md
cat ARCHIVO_REFERENCIA_COMPLETA.md
```
**☝️ OBLIGATORIO:** Entender reglas, flujo de trabajo y propósito de cada archivo

### **PASO 3: Identificar Prioridades**
Basado en el output del PASO 1, enfocar en:
1. **🔴 CRÍTICOS:** `DOC000-ProjectBrief.md`, `projectInfo.json`
2. **🟡 IMPORTANTES:** `architecture.json`, `apiContract.json`, `dataModel.json`
3. **🟢 SECUNDARIOS:** Otros documentos según necesidad

---

## 📋 **FLUJO DE TRABAJO ESTRICTO**

### **Para CADA archivo que modifiques:**

1. **📚 Consultar Playbook**
   ```bash
   ls prompt_playbooks/playbook-* | grep [nombre-archivo]
   cat prompt_playbooks/playbook-[nombre-archivo].md
   ```

2. **✏️ Completar Placeholders**
   - Reemplazar TODOS los `[placeholder]`
   - Usar información real del proyecto
   - Mantener formato original del archivo

3. **🔍 Verificar Cambios**
   ```bash
   python3 verify_integrity.py
   ```
   - Confirmar que archivo cambió de estado
   - Verificar reducción de placeholders

4. **🔄 Repetir Ciclo**
   - Continuar con siguiente archivo prioritario

---

## 🗂️ **ESTRUCTURA DEL SISTEMA (NO TOCAR)**

```
prompt-manager-lite-v/
├── docs/                           # 📝 36 documentos (usar existentes)
├── schemas/master_blueprint_parts/ # ⚙️ 27 schemas (completar placeholders)
├── prompt_playbooks/               # 📚 Guías (consultar antes de editar)
├── features/                       # 🚀 Templates de funcionalidades
├── bugs/                           # 🐛 Templates de errores
├── operations/                     # 🔧 Templates de tareas
├── proposals/                      # 💡 Templates de ideas
├── combine_schemas.py              # 🔗 Script combinar (NO MODIFICAR)
├── verify_integrity.py            # 🔍 Script verificación (NO MODIFICAR)
├── GUIA_COMPLETA_DE_USO.md         # 📖 Manual completo (LEER)
└── ARCHIVO_REFERENCIA_COMPLETA.md  # 🗺️ Mapa de todos los archivos (CONSULTAR)
```

---

## 🚨 **REGLAS CRÍTICAS - NUNCA ROMPER**

### ❌ **PROHIBIDO ABSOLUTO:**
- Crear archivos nuevos (`touch`, `echo >`, etc.)
- Modificar estructura de carpetas (`mkdir`, `mv`, etc.)
- Cambiar nombres de archivos existentes
- Modificar scripts Python sin justificación
- Dejar placeholders `[así]` sin completar
- Trabajar sin verificar estado primero

### ✅ **OBLIGATORIO SIEMPRE:**
- Usar `python3 verify_integrity.py` antes y después
- Consultar playbooks antes de editar
- Completar TODOS los placeholders en cada archivo
- Respetar formato original de cada archivo
- Trabajar solo con archivos existentes

---

## 🎯 **OBJETIVOS DE SESIÓN**

### **Para Sesión Nueva (Proyecto Nuevo):**
1. Ejecutar verificación inicial
2. Completar `DOC000-ProjectBrief.md` (21 placeholders)
3. Completar `projectInfo.json` (información básica)
4. Completar `architecture.json` (arquitectura general)
5. Verificar progreso con `verify_integrity.py`

### **Para Continuar Sesión (Retomar Trabajo):**
1. Ejecutar `python3 verify_integrity.py`
2. Identificar archivos `📝 PLANTILLA` o `🔄 EN PROGRESO`
3. Continuar con siguiente archivo prioritario
4. Mantener ritmo de verificación constante

### **Para Finalizar Sesión:**
1. Ejecutar `python3 verify_integrity.py`
2. Si críticos completos: `python3 combine_schemas.py`
3. Verificar generación de `master_blueprint_combined.json`
4. Dejar estado limpio para próxima sesión

---

## 💬 **EJEMPLO DE PROMPT PARA INICIAR TRABAJO**

```
"Hola, necesito trabajar en mi proyecto usando Prompt Manager Lite.

Proyecto: [Nombre de tu proyecto]
Objetivo: [Documentar completamente / Continuar documentación / Generar blueprint]

Por favor:
1. Verifica el estado actual con verify_integrity.py
2. Identifica qué archivos necesitan completarse
3. Ayúdame a completar [archivo específico] siguiendo su playbook
4. Verifica los cambios después de cada modificación

Recuerda: Solo usar archivos existentes, completar todos los placeholders, y verificar constantemente."
```

---

## 📊 **COMANDOS DE REFERENCIA RÁPIDA**

```bash
# Estado actual del proyecto
python3 verify_integrity.py

# Crear nuevo snapshot (primera vez o después de cambios manuales)
python3 verify_integrity.py store

# Combinar schemas (cuando estén completos)
python3 combine_schemas.py

# Ver playbooks disponibles
ls prompt_playbooks/playbook-*

# Leer playbook específico
cat prompt_playbooks/playbook-[nombre].md

# Ver estructura de archivos
tree -L 2
```

---

## 🎉 **RESULTADO FINAL EXPECTED**

Al seguir este protocolo correctamente:
- ✅ Documentación estructurada y profesional
- ✅ Master blueprint JSON completo (`master_blueprint_combined.json`)
- ✅ Sistema íntegro y portable
- ✅ Fuente única de verdad para el proyecto
- ✅ Base sólida para agentes IA y desarrolladores

---

**🔄 Este prompt debe ser tu punto de partida en CADA sesión de trabajo con Prompt Manager Lite.**
