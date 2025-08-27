# **OPERACIONES MODULARES: [TIPO_OPERACIÓN] - [TÍTULO_ESPECÍFICO]**

Versión: 1.0 (Modular Operations Specific)  
Fecha: [FECHA]

### **CLASIFICACIÓN DE OPERACIÓN**

**TIPO PRINCIPAL:** [Seleccionar UNO]
- [ ] **INSTALACIÓN** - Servicios, aplicaciones, herramientas
- [ ] **INVESTIGACIÓN** - Análisis, comparaciones, estudios
- [ ] **CONFIGURACIÓN** - Sistemas, entornos, parámetros
- [ ] **DOCUMENTACIÓN** - Guías, manuales, procedimientos
- [ ] **ANÁLISIS** - Comparación de archivos, tecnologías, opciones
- [ ] **IMPLEMENTACIÓN** - Despliegues, migraciones, actualizaciones

**SUBTIPO ESPECÍFICO:** [Detallar]
- Ejemplo: "Instalación de Docker + Kubernetes en Ubuntu 22.04"
- Ejemplo: "Investigación de alternativas a Redis para cache"
- Ejemplo: "Comparación de PostgreSQL vs MongoDB para proyecto X"

### **REGLA MANDATORIA: CICLO DE VIDA OPERACIONAL**

Este documento es la **fuente única de verdad** para esta operación específica. Su integridad es absoluta:

1. **Granularidad Obligatoria:** Cada paso debe ser verificable independientemente
2. **Prueba Tangible:** Comandos ejecutados + outputs + capturas de pantalla
3. **Inmutabilidad:** Pasos completados NO se modifican
4. **Trazabilidad:** Cada cambio debe estar documentado con timestamp

### **REGLAS ESPECÍFICAS PARA AGENTES AI:**

**REGLA AI-OPS-1: IDENTIFICACIÓN Y CONTEXTO**
- Identificarse: [Agente: nombre-modelo]
- Especificar tipo de operación en cada cambio
- Timestamp obligatorio: [YYYY-MM-DD HH:mm:ss]

**REGLA AI-OPS-2: VALIDACIÓN OPERACIONAL**
- OBLIGATORIO: Comando ejecutado + resultado esperado + resultado obtenido
- OBLIGATORIO: Captura de pantalla o log para pasos críticos
- OBLIGATORIO: Verificación de funcionamiento post-instalación

**REGLA AI-OPS-3: CONTROL DE ABANDONO**
- Marcar claramente estado: ACTIVO / PAUSADO / BLOQUEADO / COMPLETADO
- Si se pausa: documentar razón y próximos pasos
- Si se bloquea: documentar bloqueador y alternativas
- NUNCA dejar operaciones sin estado claro

## 📊 **ESTADO OPERACIONAL EN TIEMPO REAL**

**ESTADO GENERAL:** [0-100]% COMPLETADO

**OPERACIÓN ACTUAL:**
- **Fase:** [Número y nombre de fase actual]
- **Paso específico:** [Descripción detallada]
- **Iniciado:** [YYYY-MM-DD HH:mm:ss]
- **Tiempo estimado:** [X minutos/horas]
- **Progreso:** [Descripción específica del avance]

**ESTADO DE CONTROL:**
- **Estado:** [ACTIVO / PAUSADO / BLOQUEADO / COMPLETADO]
- **Última actividad:** [YYYY-MM-DD HH:mm:ss]
- **Próxima revisión:** [YYYY-MM-DD HH:mm:ss]
- **Responsable:** [Persona/Agente asignado]

**BLOQUEADORES ACTUALES:**
- [ ] [Descripción del bloqueador 1]
- [ ] [Descripción del bloqueador 2]

---

## 🎯 **DEFINICIÓN DE LA OPERACIÓN**

### **Objetivo Principal:**
[¿Qué se va a lograr exactamente?]

### **Justificación:**
[¿Por qué es necesaria esta operación?]

### **Criterios de Éxito:**
- [ ] [Criterio específico y medible 1]
- [ ] [Criterio específico y medible 2]
- [ ] [Criterio específico y medible 3]

### **Criterios de Fallo:**
- [ ] [Condición que indicaría fallo 1]
- [ ] [Condición que indicaría fallo 2]

---

## 📋 **FASES OPERACIONALES**

### **FASE 1: PREPARACIÓN Y ANÁLISIS**

**OPS-01.A - Análisis del Entorno**
- [ ] **OPS-01.A.1** Inventario del sistema actual
  - **Comando:** `[comando específico]`
  - **Resultado esperado:** [descripción]
  - **Estado:** [NO_INICIADO/EN_PROGRESO/COMPLETADO]
  - **Evidencia:** [archivo/captura]

- [ ] **OPS-01.A.2** Verificación de prerrequisitos
  - **Comando:** `[comando específico]`
  - **Resultado esperado:** [descripción]
  - **Estado:** [NO_INICIADO/EN_PROGRESO/COMPLETADO]
  - **Evidencia:** [archivo/captura]

- [ ] **OPS-01.A.3** Identificación de dependencias
  - **Comando:** `[comando específico]`
  - **Resultado esperado:** [descripción]
  - **Estado:** [NO_INICIADO/EN_PROGRESO/COMPLETADO]
  - **Evidencia:** [archivo/captura]

**OPS-01.B - Planificación Detallada**
- [ ] **OPS-01.B.1** Definir secuencia de pasos
- [ ] **OPS-01.B.2** Identificar puntos de rollback
- [ ] **OPS-01.B.3** Preparar scripts de verificación

### **FASE 2: IMPLEMENTACIÓN**

**OPS-02.A - Instalación/Configuración Principal**
- [ ] **OPS-02.A.1** [Paso específico 1]
  - **Comando:** `[comando específico]`
  - **Resultado esperado:** [descripción]
  - **Estado:** [NO_INICIADO/EN_PROGRESO/COMPLETADO]
  - **Evidencia:** [archivo/captura]

- [ ] **OPS-02.A.2** [Paso específico 2]
  - **Comando:** `[comando específico]`
  - **Resultado esperado:** [descripción]
  - **Estado:** [NO_INICIADO/EN_PROGRESO/COMPLETADO]
  - **Evidencia:** [archivo/captura]

**OPS-02.B - Configuración Específica**
- [ ] **OPS-02.B.1** [Configuración específica 1]
- [ ] **OPS-02.B.2** [Configuración específica 2]

### **FASE 3: VERIFICACIÓN Y VALIDACIÓN**

**OPS-03.A - Pruebas Funcionales**
- [ ] **OPS-03.A.1** Verificación de instalación
  - **Comando:** `[comando de verificación]`
  - **Resultado esperado:** [descripción]
  - **Estado:** [NO_INICIADO/EN_PROGRESO/COMPLETADO]
  - **Evidencia:** [archivo/captura]

- [ ] **OPS-03.A.2** Pruebas de funcionamiento
  - **Comando:** `[comando de prueba]`
  - **Resultado esperado:** [descripción]
  - **Estado:** [NO_INICIADO/EN_PROGRESO/COMPLETADO]
  - **Evidencia:** [archivo/captura]

**OPS-03.B - Validación de Rendimiento**
- [ ] **OPS-03.B.1** Métricas de performance
- [ ] **OPS-03.B.2** Pruebas de carga (si aplica)

### **FASE 4: DOCUMENTACIÓN Y CIERRE**

**OPS-04.A - Documentación**
- [ ] **OPS-04.A.1** Crear guía de uso
- [ ] **OPS-04.A.2** Documentar configuración final
- [ ] **OPS-04.A.3** Crear procedimientos de mantenimiento

**OPS-04.B - Transferencia de Conocimiento**
- [ ] **OPS-04.B.1** Preparar documentación para equipo
- [ ] **OPS-04.B.2** Crear checklist de monitoreo

---

## 🔍 **SECCIÓN ESPECÍFICA: INVESTIGACIÓN Y ANÁLISIS**

### **Investigación Realizada:**
- **Fuentes consultadas:**
  - [ ] [Fuente 1: URL/documento]
  - [ ] [Fuente 2: URL/documento]
  - [ ] [Fuente 3: URL/documento]

- **Alternativas evaluadas:**
  - [ ] **Opción A:** [Descripción] - Pros: [lista] - Contras: [lista]
  - [ ] **Opción B:** [Descripción] - Pros: [lista] - Contras: [lista]
  - [ ] **Opción C:** [Descripción] - Pros: [lista] - Contras: [lista]

- **Decisión tomada:** [Opción seleccionada y justificación]

### **Comparaciones Realizadas:**
- **Archivos/Tecnologías comparadas:**
  - [ ] [Item 1 vs Item 2]: Resultado: [descripción]
  - [ ] [Item 3 vs Item 4]: Resultado: [descripción]

---

## 📚 **SECCIÓN ESPECÍFICA: CREACIÓN DE GUÍAS**

### **Guías a Crear:**
- [ ] **Guía 1:** [Nombre] - Audiencia: [target] - Estado: [pendiente/en_progreso/completada]
- [ ] **Guía 2:** [Nombre] - Audiencia: [target] - Estado: [pendiente/en_progreso/completada]

### **Estructura de Guías:**
- [ ] Introducción y contexto
- [ ] Prerrequisitos
- [ ] Pasos detallados
- [ ] Troubleshooting
- [ ] Referencias adicionales

---

## 🚨 **PROCEDIMIENTOS DE ROLLBACK**

### **Puntos de Rollback Definidos:**
- **Punto 1:** Después de OPS-01 (Análisis)
  - **Comando rollback:** `[comando]`
  - **Condiciones:** [cuándo aplicar]

- **Punto 2:** Después de OPS-02.A (Instalación)
  - **Comando rollback:** `[comando]`
  - **Condiciones:** [cuándo aplicar]

### **Procedimiento de Emergencia:**
1. **Parar operación:** `[comando]`
2. **Verificar estado:** `[comando]`
3. **Ejecutar rollback:** `[comando]`
4. **Validar rollback:** `[comando]`

---

## 📊 **MÉTRICAS Y MONITOREO**

### **Métricas de la Operación:**
- **Tiempo total estimado:** [X horas]
- **Tiempo real utilizado:** [X horas]
- **Eficiencia:** [porcentaje]
- **Errores encontrados:** [número]
- **Rollbacks ejecutados:** [número]

### **Monitoreo Post-Operación:**
- [ ] **Monitoreo día 1:** [qué verificar]
- [ ] **Monitoreo semana 1:** [qué verificar]
- [ ] **Monitoreo mes 1:** [qué verificar]

---

## 📝 **HISTORIAL GRANULAR DE CAMBIOS**

### **REGISTRO CRONOLÓGICO COMPLETO:**

**[YYYY-MM-DD HH:mm:ss] - INICIO DE OPERACIÓN**
- **Agente:** [nombre-agente]
- **Acción:** Creación del documento operacional
- **Contexto:** [razón de inicio]
- **Estado inicial:** 0% completado

**[YYYY-MM-DD HH:mm:ss] - CAMBIO DE ESTADO**
- **ID:** [OPS-XX.X.X]
- **Estado:** [ANTERIOR] → [NUEVO]
- **Agente:** [nombre-agente]
- **Comando ejecutado:** `[comando]`
- **Resultado:** [descripción del resultado]
- **Archivos afectados:** [lista de archivos]
- **Evidencia:** [referencia a captura/log]

---

## 🎯 **CONTROL DE NO ABANDONO**

### **Sistema de Seguimiento:**
- **Última actividad:** [YYYY-MM-DD HH:mm:ss]
- **Próxima revisión obligatoria:** [YYYY-MM-DD HH:mm:ss]
- **Frecuencia de revisión:** [diaria/semanal]
- **Responsable de seguimiento:** [persona/agente]

### **Alertas de Abandono:**
- [ ] **Alerta 24h:** Si no hay actividad en 24 horas
- [ ] **Alerta 72h:** Si no hay actividad en 72 horas
- [ ] **Alerta crítica:** Si no hay actividad en 1 semana

### **Procedimiento de Reactivación:**
1. **Revisar estado actual**
2. **Evaluar viabilidad de continuación**
3. **Actualizar contexto y dependencias**
4. **Redefinir próximos pasos**
5. **Asignar nuevo responsable si es necesario**

---

## 📋 **CHECKLIST FINAL DE COMPLETITUD**

### **Antes de Marcar como COMPLETADO:**
- [ ] Todos los pasos tienen evidencia tangible
- [ ] Todas las pruebas de funcionamiento pasaron
- [ ] Documentación creada y validada
- [ ] Procedimientos de rollback probados
- [ ] Métricas recopiladas y analizadas
- [ ] Transferencia de conocimiento realizada
- [ ] Monitoreo post-operación configurado

### **Entregables Finales:**
- [ ] **Documentación técnica:** [ubicación]
- [ ] **Guías de usuario:** [ubicación]
- [ ] **Scripts de automatización:** [ubicación]
- [ ] **Procedimientos de mantenimiento:** [ubicación]
- [ ] **Métricas y reportes:** [ubicación]

---

## 🏁 **CIERRE DE OPERACIÓN**

**FECHA DE CIERRE:** [YYYY-MM-DD HH:mm:ss]
**AGENTE RESPONSABLE:** [nombre]
**ESTADO FINAL:** [COMPLETADO/CANCELADO/PAUSADO]
**COMPLETITUD:** [porcentaje]%

**RESUMEN EJECUTIVO:**
[Descripción concisa de lo logrado, problemas encontrados, y recomendaciones]

**LECCIONES APRENDIDAS:**
- [Lección 1]
- [Lección 2]
- [Lección 3]

**PRÓXIMOS PASOS RECOMENDADOS:**
- [Recomendación 1]
- [Recomendación 2]
- [Recomendación 3]

---

**FIRMA DIGITAL:** [Agente/Persona] - [YYYY-MM-DD HH:mm:ss]
