# GUÍA DE WORKFLOW DIARIO - The Mighty Task v3.3

**Fecha:** 2025-08-26  
**Versión:** 3.3 (Modular Operations)  
**Propósito:** Guía completa para uso correcto del sistema The Mighty Task con templates modulares

---

## 🎯 **FILOSOFÍA CENTRAL**

The Mighty Task funciona bajo el principio de **"Checklist como Fuente de Verdad"**. Todo el sistema gira alrededor de mantener checklists actualizados y precisos que reflejen el estado real del trabajo.

### **Reglas Fundamentales:**
1. **El checklist nunca miente** - Es la única fuente de verdad del progreso
2. **Actualización inmediata** - Cambios de estado se registran al momento
3. **Especificidad obligatoria** - Cada tarea debe ser específica y medible
4. **Investigación web primero** - Validar información antes de implementar

---

## 📋 **COMANDOS PRINCIPALES**

### 🎯 **TIPOS DE TEMPLATES DISPONIBLES**

### **1. Template Development (Default)**
```bash
python3 scripts/generate-daily.py --theme "BACKEND-API-SETUP"
# Usa: template-pendingtask.md
# Enfoque: Desarrollo de código, programación, features
```

### **2. Template Operations**
```bash
python3 scripts/generate-daily.py --theme "DEVOPS-SETUP" --template operations
# Usa: template-pendingtask-operations.md
# Enfoque: Operaciones generales, sistemas, configuraciones
```

### **3. Template Operations Modular**
```bash
python3 scripts/generate-daily.py --theme "DEVOPS-SETUP" --template operations-modular
# Usa: template-pendingtask-operations-modular.md
# Enfoque: Instalaciones específicas, investigaciones, comparaciones, guías
```

### **4. Template Research**
```bash
python3 scripts/generate-daily.py --theme "API-DESIGN" --template research
# Usa: template-web-research.md
# Enfoque: Investigación web, estudios, análisis
```

### **Generar Nueva Sesión Diaria**
```bash
# Sesión de desarrollo (default)
python3 scripts/generate-daily.py --theme "BACKEND-API-SETUP"

# Sesión de operaciones/instalaciones
python3 scripts/generate-daily.py --theme "DATABASE-SETUP" --template operations

# Sesión de investigación web
python3 scripts/generate-daily.py --theme "TECH-RESEARCH" --template research

# Con fecha específica
python3 scripts/generate-daily.py --theme "FRONTEND-COMPONENTS" --date "2025-01-22"

# Modo automático (usa fecha actual y tema default)
python3 scripts/generate-daily.py --auto
```

### **Tipos de Templates Disponibles (v3.3)**

#### **Template Development (Default)**
- Enfocado en desarrollo de software
- Incluye secciones de playbooks específicos
- Tracking de errores y códigos únicos integrado
- Ideal para: APIs, frontend, backend, databases

#### **Template Operations**
- Diseñado para instalaciones y configuraciones de sistemas
- Enfoque en procedimientos paso a paso con validación obligatoria
- Rollback procedures y monitoreo incluidos
- Tracking granular con timestamps y agentes AI
- Reglas estrictas de completitud con pruebas tangibles
- Ideal para: deployments, configuraciones de sistema, instalaciones

#### **Template Research** 
- Optimizado para investigaciones web
- Estructura para documentar hallazgos
- Integración con web-guide-manager
- Ideal para: análisis de tecnologías, comparativas

**Resultado esperado:**
- Directorio `daily-work/2025-08-26_DATABASE-SETUP/` creado
- Archivo `pending-tasks-2025-08-26_DATABASE-SETUP.md` con template según tipo seleccionado

### **1. INICIO DE SESIÓN DIARIA**

```bash
# Generar nueva sesión diaria
python scripts/generate-daily.py --theme BACKEND-API-SETUP --date 2025-08-25

# Verificar estado del sistema
python scripts/status-checker.py --dashboard
```

**Resultado esperado:**
- Directorio `daily-work/2025-08-25_BACKEND-API-SETUP/` creado
- Archivo `pending-tasks-2025-08-25_BACKEND-API-SETUP.md` con template actualizado
- Dashboard de estado del sistema

### **2. CONFIGURACIÓN DE TAREAS**

**Formato obligatorio para cada tarea:**
```markdown
* [ ] **[BACKEND-01.A.1] Configurar servidor Express básico:** [Estado: NO_INICIADO]
  * **Descripción:** Crear servidor Express.js con middleware básico (cors, helmet, morgan), configurar puerto desde variables de entorno, y establecer rutas base (/health, /api/v1). Incluir manejo de errores global y logging estructurado.
  * **Criterios de éxito:** Servidor responde en puerto configurado, rutas base funcionan, logs se generan correctamente
  * **Archivos involucrados:** `src/server.js`, `src/middleware/`, `.env.example`, `package.json`
  * **Validación:** `curl localhost:3000/health` retorna 200, logs aparecen en consola
  * **Estimación:** 2h
  * **Investigación web requerida:** Versión actual Express.js, middleware recomendados 2025, mejores prácticas seguridad
```

### **3. INVESTIGACIÓN WEB OBLIGATORIA**

**Antes de iniciar cualquier tarea:**

1. **Crear web-guide específico:**
```bash
python scripts/web-guide-manager.py --create "express-setup" --session "2025-08-25_BACKEND-API-SETUP"
```

2. **Investigar fuentes confiables:**
   - Documentación oficial
   - GitHub releases recientes
   - Stack Overflow (últimos 6 meses)
   - Artículos de desarrolladores reconocidos

3. **Documentar hallazgos en web-guide:**
```markdown
# Express.js Setup Guide - 2025

**Fecha de investigación:** 2025-08-25  
**Versión investigada:** Express 4.19.x  
**Fuentes consultadas:**
- https://expressjs.com/en/starter/installing.html
- https://github.com/expressjs/express/releases

## Configuración Recomendada 2025
[Información validada y actualizada]
```

### **4. EJECUCIÓN DE TAREAS**

**Reglas durante la implementación:**

1. **Actualizar estado inmediatamente:**
```markdown
* [x] **[BACKEND-01.A.1] Configurar servidor Express básico:** [Estado: COMPLETADO]
```

2. **Registrar en historial:**
```markdown
**[2025-08-25 14:30:22] - TAREA COMPLETADA**
- **ID:** BACKEND-01.A.1
- **Estado:** EN_PROGRESO → COMPLETADO
- **Agente:** claude-3.5-sonnet
- **Tiempo real invertido:** 1.5h (vs 2h estimado)
- **Prueba de completitud:** curl localhost:3000/health retorna {"status":"ok"}
- **Artefactos generados:** src/server.js, package.json actualizado
```

3. **Validar con pruebas tangibles:**
```bash
# Ejecutar validación
curl localhost:3000/health
# Resultado esperado: {"status":"ok","timestamp":"2025-08-25T14:30:22Z"}
```

### **5. GENERACIÓN DE REPORTES**

```bash
# Generar reporte de sesión
python scripts/report-generator.py --session "2025-08-25_BACKEND-API-SETUP" --format html

# Verificar consistencia
python scripts/consistency-checker.py --scan-all
```

### **6. CONSOLIDACIÓN (AL FINAL DEL DÍA)**

```bash
# Consolidar en mission-resume
python scripts/mission-resumer.py --theme "BACKEND-API-SETUP" --consolidate-sessions

# Verificar resultado
python scripts/status-checker.py --mission-summary
```

---

## 🤖 **REGLAS ESPECÍFICAS PARA AGENTES AI**

### **IDENTIFICACIÓN OBLIGATORIA**
```markdown
[Agente: claude-3.5-sonnet] - Iniciando tarea BACKEND-01.A.1
```

### **FORMATO DE TIMESTAMP**
```markdown
[2025-08-25 14:30:22] - NUNCA usar "hace 2 horas" o formatos relativos
```

### **ACTUALIZACIÓN COMPLETA**
Al cambiar cualquier estado, DEBE actualizar:
1. Checkbox correspondiente [ ] → [x]
2. Sección "ESTADO ACTUAL EN TIEMPO REAL"
3. "HISTORIAL GRANULAR DE CAMBIOS"
4. Porcentaje general de completitud

### **INMUTABILIDAD DE COMPLETADOS**
- Items COMPLETADOS son INMUTABLES
- Solo se permite agregar al historial
- NUNCA modificar contenido completado

### **VALIDACIÓN TANGIBLE OBLIGATORIA**
- Sin prueba tangible = NO se puede marcar COMPLETADO
- Incluir: comando ejecutado + respuesta esperada + respuesta obtenida

---

## 📊 **MÉTRICAS DE CALIDAD**

### **Indicadores de Sesión Exitosa:**
- ✅ 100% de tareas tienen descripción detallada
- ✅ Todas las tareas completadas tienen prueba tangible
- ✅ Web-guides creados para investigaciones
- ✅ Historial granular actualizado
- ✅ Reportes generados sin errores

### **Comandos de Verificación:**
```bash
# Verificar calidad de especificación
python scripts/consistency-checker.py --validate-task-specs

# Verificar completitud de tracking
python scripts/consistency-checker.py --check-tracking

# Verificar web-guides
python scripts/web-guide-manager.py --validate-guides
```

---

## 🚨 **ERRORES COMUNES A EVITAR**

### **❌ MAL:**
```markdown
* [x] Configurar Express [Estado: COMPLETADO]
```

### **✅ BIEN:**
```markdown
* [x] **[BACKEND-01.A.1] Configurar servidor Express básico:** [Estado: COMPLETADO]
  * **Descripción:** Crear servidor Express.js con middleware básico...
  * **Prueba de completitud:** curl localhost:3000/health retorna 200
```

### **❌ MAL:**
```markdown
[Ayer] - Completé la tarea
```

### **✅ BIEN:**
```markdown
[2025-08-25 14:30:22] - TAREA COMPLETADA
```

---

## 🔄 **FLUJO DE CONTINUIDAD MULTI-DÍA**

### **Detectar Tareas Continuadas:**
```bash
# Buscar tareas en progreso
python scripts/status-checker.py --active-tasks

# Continuar tarea en nueva sesión
python scripts/generate-daily.py --continue-task "BACKEND-01.A.1" --theme BACKEND-API-SETUP-2
```

### **Reutilizar Web-Guides:**
```bash
# Buscar guides existentes
python scripts/web-guide-manager.py --search "express"

# Copiar guide a nueva sesión
python scripts/web-guide-manager.py --copy-guide "express-setup" --to-session "2025-08-26_BACKEND-API-SETUP-2"
```

---

## ✅ **CHECKLIST DE FINALIZACIÓN DIARIA**

- [ ] Todas las tareas tienen estado actualizado
- [ ] Historial granular completo
- [ ] Web-guides creados para investigaciones
- [ ] Pruebas tangibles documentadas
- [ ] Reporte de sesión generado
- [ ] Consistency check ejecutado sin errores
- [ ] Mission-resume consolidado (si aplica)

---

**Estado:** ✅ Guía completa y lista para uso  
**Uso:** Consultar antes de cada sesión diaria para mantener calidad y consistencia
