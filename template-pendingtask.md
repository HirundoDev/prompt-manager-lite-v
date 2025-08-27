# **MANDATO DE RECONSTRUCCIÓN: [TÍTULO DE LA MISIÓN]**

Versión: [VERSION] (con Checklists)  
Fecha: [FECHA]

### **REGLA MANDATORIA: EL CICLO DE VIDA DE ESTE MANDATO**

Este documento es la **fuente única de verdad** para la reconstrucción del ecosistema "Prompt-Manager". Su integridad es absoluta y su ciclo de vida sigue estas reglas:

1. **Actualización Continua:** A medida que cada "Acción" o "Misión" se completa, su estado **DEBE** ser actualizado de PENDIENTE a COMPLETADO.  
2. **Prueba de Completitud (Proof of Completion):** Ninguna tarea se considerará COMPLETADO sin una referencia tangible (hash de commit, enlace a PR, log de pruebas).  
3. **Inmutabilidad de Misiones Completadas:** Una vez que una misión está COMPLETADO y verificada, no se modifica. Si se requiere trabajo adicional, se creará una nueva misión.

### **REGLAS ESPECÍFICAS PARA AGENTES AI:**

**REGLA AI-1: IDENTIFICACIÓN OBLIGATORIA**
- Todo agente AI DEBE identificarse al hacer cambios: [Agente: nombre-modelo]
- Ejemplo: [Agente: claude-4-sonnet] o [Agente: gpt-4]

**REGLA AI-2: FORMATO DE TIMESTAMP OBLIGATORIO**
- Usar formato: [YYYY-MM-DD HH:mm:ss]
- Ejemplo: [2024-01-15 14:30:22]
- NUNCA usar formatos relativos ("hace 2 horas", "ayer")

**REGLA AI-3: ACTUALIZACIÓN COMPLETA OBLIGATORIA**
- Al cambiar estado de cualquier item, DEBE actualizar:
  1. El checkbox correspondiente [ ] → [x] 
  2. La sección "ESTADO ACTUAL EN TIEMPO REAL"
  3. El "HISTORIAL GRANULAR DE CAMBIOS"
  4. El porcentaje general de completitud

**REGLA AI-4: INMUTABILIDAD DE COMPLETADOS**
- Items marcados como COMPLETADO son INMUTABLES
- Solo se permite agregar al historial, nunca modificar contenido completado

**REGLA AI-5: VALIDACIÓN CON PRUEBAS TANGIBLES**
- OBLIGATORIO verificar que existe prueba de completitud tangible
- OBLIGATORIO incluir comando ejecutado + respuesta esperada + respuesta obtenida
- Sin prueba tangible = NO SE PUEDE marcar COMPLETADO

**REGLA AI-6: SECUENCIALIDAD OBLIGATORIA**
- MISIÓN 1 debe estar 100% COMPLETADA antes de iniciar MISIÓN 2
- Una misión = UN módulo funcional completo
- NO se permite trabajar en múltiples misiones simultáneamente

**REGLA AI-7: NUNCA RESUMIR, SIEMPRE EXPANDIR**
- PROHIBIDO eliminar items del checklist
- PROHIBIDO "resumir" o "simplificar" tareas
- OBLIGATORIO agregar nuevos items cuando se descubren
- Formato: [ID-NUEVO] [Descripción específica] [Estado: NO_INICIADO]

**REGLA AI-8: REGISTRO INMEDIATO**
- Al completar CUALQUIER item: actualizar archivo INMEDIATAMENTE
- Al descubrir nueva tarea: agregar al checklist INMEDIATAMENTE  
- Al encontrar bloqueador: registrar en historial INMEDIATAMENTE

## **ESTADO ACTUAL EN TIEMPO REAL**

**ESTADO GENERAL DE LA MISIÓN: [PORCENTAJE]% COMPLETADO**

**MISIÓN ACTUAL EN PROGRESO:** [Número de misión activa]

**ACTUALMENTE TRABAJANDO EN:**
- **ID:** [CATEGORIA-NN.X.N] 
- **Tarea:** [Nombre específico de la tarea en progreso]
- **Iniciado:** [YYYY-MM-DD HH:mm:ss]
- **Estimado completar:** [YYYY-MM-DD HH:mm:ss]
- **Progreso:** [Descripción del avance actual]
- **Bloqueadores:** [Ninguno / Lista de bloqueadores]

**PRÓXIMO EN COLA:**
- [ID-SIGUIENTE] [Descripción de la siguiente tarea]
- [ID-OTRO] [Otra tarea en cola]

**ÚLTIMOS COMPLETADOS:**
- [ID-PREV] [Tarea completada] ✅ (YYYY-MM-DD HH:mm:ss)
- [ID-PREV2] [Otra tarea completada] ✅ (YYYY-MM-DD HH:mm:ss)

---

## **HISTORIAL GRANULAR DE CAMBIOS**

### **REGISTRO CRONOLÓGICO DE TODOS LOS MOVIMIENTOS:**

**[YYYY-MM-DD HH:mm:ss] - CAMBIO DE ESTADO**
- **ID:** [CATEGORIA-NN.X.N]
- **Estado:** [ANTERIOR] → [NUEVO]
- **Agente:** [nombre-del-agente-ai]
- **Contexto:** [Razón específica del cambio]
- **Estimación:** [tiempo estimado si aplica]
- **Archivos involucrados:** [lista de archivos afectados]
- **Notas:** [observaciones importantes]

**[YYYY-MM-DD HH:mm:ss] - TAREA COMPLETADA**
- **ID:** [CATEGORIA-NN.X.N]
- **Estado:** EN_PROGRESO → COMPLETADO
- **Agente:** [nombre-del-agente-ai]
- **Tiempo real invertido:** [Xh] (vs [Yh] estimado)
- **Prueba de completitud:** [evidencia tangible]
- **Artefactos generados:** [archivos/commits creados]

**[YYYY-MM-DD HH:mm:ss] - NUEVA TAREA DESCUBIERTA**
- **ID:** [CATEGORIA-NN.X.N] (NUEVO)
- **Descripción:** [qué tarea se agregó]
- **Agente:** [nombre-del-agente-ai]
- **Razón:** [por qué se descubrió esta tarea]
- **Prioridad:** [ALTA/MEDIA/BAJA]
- **Estimación:** [tiempo estimado]

---

## **FILOSOFÍA CENTRAL DE RECONSTRUCCIÓN: [FILOSOFÍA ESPECÍFICA]**

[Descripción de la filosofía central que rige esta misión específica]

## **MISIONES DE RECONSTRUCCIÓN (PLAN DE ACCIÓN HIPER-EXPLÍCITO)**

### **MISIÓN [NÚMERO]: [NOMBRE DE LA MISIÓN]**

### **CONTEXTO DE LA MISIÓN [NÚMERO]**

**QUÉ SE DEBE HACER:**
- **Objetivo específico:** [Descripción detallada del objetivo]
- **Problema que resuelve:** [Problema específico que aborda esta misión]
- **Resultado funcional esperado:** [Qué debe funcionar al completarse]

**CÓMO VALIDAR QUE ESTÁ COMPLETO:**
- **Pasos de verificación:** [Pasos específicos para verificar completitud]
- **Comandos de validación:** [Comandos para probar funcionalidad]
- **Criterios de éxito:** [Criterios medibles de éxito]

**INFORMACIÓN CRÍTICA:**
- **Detalles técnicos:** [Aspectos técnicos importantes]
- **Configuraciones:** [Configuraciones específicas requeridas]
- **Consideraciones especiales:** [Aspectos importantes a considerar]

---

* **Estado:** [PENDIENTE/EN PROGRESO/COMPLETADO]
* **Diagnóstico / Falla Crítica (Estado Actual):** [Descripción detallada del problema actual que debe ser resuelto]
* **Objetivo Estratégico (Estado Esperado):** [Descripción clara del estado final deseado]
* **Plan de Acción Paso a Paso:**  
  1. **[Nombre del Paso Principal]:**  
     * [Descripción detallada de la acción]
     * [Subacciones específicas si aplica]
  2. **[Otro Paso Principal]:**  
     * [Más detalles]
* **Prueba de Completitud:** [Criterios específicos y verificables que confirman que la misión está completa]

### **VALIDACIÓN CON PRUEBAS TANGIBLES - MISIÓN [NÚMERO]**

**PRUEBA 1: [NOMBRE_PRUEBA]**
- **Comando:** `[comando-exacto-ejecutado]`
- **Respuesta esperada:** `[output-esperado]`
- **Respuesta obtenida:** `[output-real]`
- **Estado:** [✅ PASÓ / ❌ FALLÓ]
- **Fecha:** [YYYY-MM-DD HH:mm:ss]

**PRUEBA 2: [OTRA_PRUEBA]**
- **Comando:** `[comando-exacto-ejecutado]`
- **Respuesta esperada:** `[output-esperado]`
- **Respuesta obtenida:** `[output-real]`
- **Estado:** [✅ PASÓ / ❌ FALLÓ]
- **Fecha:** [YYYY-MM-DD HH:mm:ss]

**PRUEBA 3: [VALIDACIÓN_FUNCIONAL]**
- **Comando:** `[comando-exacto-ejecutado]`
- **Respuesta esperada:** `[output-esperado]`
- **Respuesta obtenida:** `[output-real]`
- **Estado:** [✅ PASÓ / ❌ FALLÓ]
- **Fecha:** [YYYY-MM-DD HH:mm:ss]

**COMENTARIOS Y GUÍAS DE LA MISIÓN [NÚMERO]:**
- **Cómo funciona:** [Explicación de uso del módulo completado]
- **Dónde validar:** [Ubicación de pruebas/resultados]
- **Dependencias confirmadas:** [Qué requiere para funcionar]
- **Notas para futuro:** [Consideraciones importantes para próximas misiones]
* **Checklist de Verificación de Misión:**  
  * [ ] **[CAT-01] [Categoría Principal]:** [Estado: NO_INICIADO] [Asignado: AGENTE] [Est: Xh]
    * [ ] **[CAT-01.A.1] [Título Específico]:** [Estado: NO_INICIADO]
      * **Descripción:** [Descripción detallada de 2-3 líneas explicando QUÉ se hace exactamente]
      * **Criterios de éxito:** [Criterios específicos y medibles]
      * **Archivos involucrados:** [Lista de archivos que se crearán/modificarán]
      * **Validación:** [Cómo verificar que está completo]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Temas a investigar antes de implementar]
      * **Códigos de error únicos:** [Lista de códigos que implementará: PREFIX-MODULE-001, etc.]
    * [ ] **[CAT-01.A.2] [Otro Título Específico]:** [Estado: NO_INICIADO]
      * **Descripción:** [Descripción detallada de 2-3 líneas explicando QUÉ se hace exactamente]
      * **Criterios de éxito:** [Criterios específicos y medibles]
      * **Archivos involucrados:** [Lista de archivos que se crearán/modificarán]
      * **Validación:** [Cómo verificar que está completo]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Temas a investigar antes de implementar]
      * **Códigos de error únicos:** [Lista de códigos que implementará: PREFIX-MODULE-001, etc.]
  * [ ] **[CAT-02] [Otra Categoría]:** [Estado: NO_INICIADO] [Asignado: AGENTE] [Est: Yh]
    * [ ] **[CAT-02.B.1] [Título Específico]:** [Estado: NO_INICIADO]
      * **Descripción:** [Descripción detallada de 2-3 líneas explicando QUÉ se hace exactamente]
      * **Criterios de éxito:** [Criterios específicos y medibles]
      * **Archivos involucrados:** [Lista de archivos que se crearán/modificarán]
      * **Validación:** [Cómo verificar que está completo]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Temas a investigar antes de implementar]
      * **Códigos de error únicos:** [Lista de códigos que implementará: PREFIX-MODULE-001, etc.]

### **FASE [NÚMERO]: [NOMBRE DE LA FASE]**

* **Descripción:** [Qué abarca esta fase]
* **Objetivo:** [Meta específica de la fase]

  **FASE [LETRA]: [NOMBRE DE SUBFASE] ([DESCRIPCIÓN BREVE])**

  *   [ ] **Acción [NÚMERO]:** [Descripción de la acción]
      *   [ ] [Subacción detallada]
      *   [ ] [Otra subacción]
  *   [ ] **Acción [NÚMERO]:** [Otra acción]
      *   [ ] [Detalles específicos]

**PRUEBA DE COMPLETITUD - FASE [IDENTIFICADOR]:**
- **Fecha:** [FECHA DE COMPLETITUD]
- **Descripción:** [Resumen de lo que se completó]
- **Artefactos Generados/Modificados:**
  - `[ruta/archivo]` → [Descripción del cambio]
  - `[otra/ruta]` → [Otro cambio]
- **Comandos Validados:** [Lista de comandos probados]
- **Funcionalidad Confirmada:** [Resumen de funcionalidad verificada]

### **TRACKING DE ERRORES Y CÓDIGOS ÚNICOS**

**REGISTRO DE ERRORES IMPLEMENTADOS:**
- **[ERROR-CODE-001]** - [Descripción del error] - [Archivo: ruta/archivo.ext] - [Función: nombreFuncion()]
- **[ERROR-CODE-002]** - [Descripción del error] - [Archivo: ruta/archivo.ext] - [Función: otraFuncion()]

**CONFIGURACIÓN DE ERROR TRACKING:**
- **Herramienta:** [Sentry/Rollbar/Custom/etc.]
- **DSN/Config:** [Configuración específica]
- **Nivel de logging:** [DEBUG/INFO/WARN/ERROR]
- **Integración con:** [DOC035-ErrorTracking.md]

**VALIDACIÓN DE CÓDIGOS ÚNICOS:**
- **Prefijo del proyecto:** [PREFIX]
- **Módulos identificados:** [AUTH, API, DB, etc.]
- **Último código asignado:** [PREFIX-MODULE-XXX]
- **Script de validación:** [Comando para verificar unicidad]

**MÉTRICAS DE ERRORES:**
- **Errores detectados:** [0]
- **Errores resueltos:** [0]
- **Tiempo promedio resolución:** [N/A]
- **Cobertura de error tracking:** [0%]

### **CRITERIOS DE FINALIZACIÓN TOTAL**

* **Condiciones de Éxito:**
  1. [Criterio específico y medible]
  2. [Otro criterio]
  3. [Más criterios]
  4. **Todos los códigos de error implementados y únicos**
  5. **Error tracking configurado y funcionando**

* **Pruebas de Aceptación:**
  1. [Test específico que debe pasar]
  2. [Otro test]
  3. **Validación de códigos únicos ejecutada exitosamente**
  4. **Error tracking capturando errores correctamente**

* **Documentación Requerida:**
  1. [Documento que debe existir]
  2. [Otro documento]
  3. **Registro completo de códigos de error en DOC036**
  4. **Configuración de error tracking documentada**

### **MÉTRICAS DE ÉXITO**

* **Cuantitativas:**
  - [Métrica numérica específica]
  - [Otra métrica]

* **Cualitativas:**
  - [Criterio de calidad]
  - [Otro criterio]

### **NOTAS Y CONSIDERACIONES ADICIONALES**

* **Dependencias:** [Qué debe completarse antes]
* **Riesgos:** [Posibles problemas y mitigaciones]
* **Recursos Necesarios:** [Herramientas, tiempo, etc.]

---

**ESTADO GENERAL DE LA MISIÓN: [PORCENTAJE]% COMPLETADO**

**PRÓXIMOS PASOS:**
1. [Siguiente acción prioritaria]
2. [Otra acción]
3. [Más acciones]
