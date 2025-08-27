# **OPERACIONES Y SISTEMAS: [TÍTULO DE LA OPERACIÓN]**

Versión: [VERSION] (Modular Operations)  
Fecha: [FECHA]

### **REGLA MANDATORIA: EL CICLO DE VIDA DE ESTA OPERACIÓN**

Este documento es la **fuente única de verdad** para operaciones de sistemas, instalaciones y configuraciones. Su integridad es absoluta y su ciclo de vida sigue estas reglas:

1. **Actualización Continua:** A medida que cada "Tarea" o "Fase" se completa, su estado **DEBE** ser actualizado de PENDIENTE a COMPLETADO.  
2. **Prueba de Completitud:** Ninguna tarea se considerará COMPLETADO sin una referencia tangible (logs, capturas, comandos ejecutados).  
3. **Inmutabilidad de Tareas Completadas:** Una vez que una tarea está COMPLETADO y verificada, no se modifica.

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

**REGLA AI-4: VALIDACIÓN DE OPERACIONES**
- OBLIGATORIO verificar que existe prueba de funcionamiento
- OBLIGATORIO incluir comando ejecutado + respuesta esperada + respuesta obtenida
- Sin prueba tangible = NO SE PUEDE marcar COMPLETADO

## 📊 **ESTADO ACTUAL EN TIEMPO REAL**

**ESTADO GENERAL DE LA OPERACIÓN: [PORCENTAJE]% COMPLETADO**

**FASE ACTUAL EN PROGRESO:** [Número de fase activa]

**ACTUALMENTE TRABAJANDO EN:**
- **ID:** [OPS-NN.X.N] 
- **Tarea:** [Nombre específico de la tarea en progreso]
- **Iniciado:** [YYYY-MM-DD HH:mm:ss]
- **Estimado completar:** [YYYY-MM-DD HH:mm:ss]
- **Progreso:** [Descripción del avance actual]
- **Bloqueadores:** [Ninguno / Lista de bloqueadores]

**PRÓXIMO EN COLA:**
- [ID-SIGUIENTE] [Descripción de la siguiente tarea]

**ÚLTIMOS COMPLETADOS:**
- [ID-PREV] [Tarea completada] ✅ (YYYY-MM-DD HH:mm:ss)

---

## **HISTORIAL GRANULAR DE CAMBIOS**

### **REGISTRO CRONOLÓGICO DE TODOS LOS MOVIMIENTOS:**

**[YYYY-MM-DD HH:mm:ss] - CAMBIO DE ESTADO**
- **ID:** [OPS-NN.X.N]
- **Estado:** [ANTERIOR] → [NUEVO]
- **Agente:** [nombre-del-agente-ai]
- **Contexto:** [Razón específica del cambio]
- **Comandos ejecutados:** [lista de comandos]
- **Archivos involucrados:** [lista de archivos afectados]

---

## 🎯 **OBJETIVO DE LA OPERACIÓN**

### **Descripción:**
[¿Qué se va a instalar, configurar o implementar?]

### **Justificación:**
[¿Por qué es necesaria esta operación?]

### **Alcance:**
- **Incluye:** [Lista de lo que SÍ está incluido]
- **Excluye:** [Lista de lo que NO está incluido]

### **Criterios de Éxito:**
- [ ] [Criterio 1 medible]
- [ ] [Criterio 2 medible]
- [ ] [Criterio 3 medible]

---

## 📋 **CHECKLIST DE VERIFICACIÓN DE OPERACIÓN**

* **Checklist de Verificación de Operación:**  
  * [ ] **[OPS-01] [Análisis del Sistema]:** [Estado: NO_INICIADO] [Asignado: AGENTE] [Est: Xh]
    * [ ] **[OPS-01.A.1] [Inventario de Sistema]:** [Estado: NO_INICIADO]
      * **Descripción:** Documentar estado actual del sistema, servicios existentes y recursos disponibles
      * **Criterios de éxito:** Inventario completo con versiones y estados
      * **Archivos involucrados:** [Lista de archivos de configuración a revisar]
      * **Validación:** [Comandos para verificar estado del sistema]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Compatibilidades, mejores prácticas]
    * [ ] **[OPS-01.A.2] [Análisis de Dependencias]:** [Estado: NO_INICIADO]
      * **Descripción:** Identificar y documentar todas las dependencias requeridas
      * **Criterios de éxito:** Lista completa de dependencias con versiones
      * **Archivos involucrados:** [Archivos de configuración de dependencias]
      * **Validación:** [Comandos para verificar dependencias]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Versiones compatibles, conflictos conocidos]
  * [ ] **[OPS-02] [Investigación y Comparación]:** [Estado: NO_INICIADO] [Asignado: AGENTE] [Est: Yh]
    * [ ] **[OPS-02.B.1] [Evaluación de Opciones]:** [Estado: NO_INICIADO]
      * **Descripción:** Comparar diferentes herramientas/enfoques para la operación
      * **Criterios de éxito:** Matriz de comparación con decisión justificada
      * **Archivos involucrados:** [Documentos de investigación]
      * **Validación:** [Criterios de evaluación cumplidos]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Comparativas, benchmarks, reviews]
  * [ ] **[OPS-03] [Implementación]:** [Estado: NO_INICIADO] [Asignado: AGENTE] [Est: Zh]
    * [ ] **[OPS-03.C.1] [Instalación]:** [Estado: NO_INICIADO]
      * **Descripción:** Ejecutar instalación de software/servicios según plan
      * **Criterios de éxito:** Software instalado y funcionando básicamente
      * **Archivos involucrados:** [Scripts de instalación, archivos de configuración]
      * **Validación:** [Comandos para verificar instalación exitosa]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Guías de instalación, troubleshooting común]
    * [ ] **[OPS-03.C.2] [Configuración]:** [Estado: NO_INICIADO]
      * **Descripción:** Aplicar configuraciones específicas según requerimientos
      * **Criterios de éxito:** Configuración aplicada y validada
      * **Archivos involucrados:** [Archivos de configuración modificados]
      * **Validación:** [Pruebas de configuración]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Mejores prácticas de configuración]
  * [ ] **[OPS-04] [Pruebas y Validación]:** [Estado: NO_INICIADO] [Asignado: AGENTE] [Est: Wh]
    * [ ] **[OPS-04.D.1] [Pruebas Funcionales]:** [Estado: NO_INICIADO]
      * **Descripción:** Ejecutar pruebas para verificar funcionamiento correcto
      * **Criterios de éxito:** Todas las pruebas funcionales pasan
      * **Archivos involucrados:** [Scripts de prueba, logs de resultados]
      * **Validación:** [Resultados de pruebas documentados]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Mejores prácticas de testing]
    * [ ] **[OPS-04.D.2] [Pruebas de Integración]:** [Estado: NO_INICIADO]
      * **Descripción:** Verificar integración con sistemas existentes
      * **Criterios de éxito:** Integración funciona sin conflictos
      * **Archivos involucrados:** [Configuraciones de integración]
      * **Validación:** [Pruebas de conectividad y comunicación]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Patrones de integración]
  * [ ] **[OPS-05] [Monitoreo y Documentación]:** [Estado: NO_INICIADO] [Asignado: AGENTE] [Est: Vh]
    * [ ] **[OPS-05.E.1] [Configuración de Monitoreo]:** [Estado: NO_INICIADO]
      * **Descripción:** Implementar monitoreo y alertas para la nueva operación
      * **Criterios de éxito:** Monitoreo activo y alertas configuradas
      * **Archivos involucrados:** [Configuraciones de monitoreo]
      * **Validación:** [Alertas funcionando correctamente]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Herramientas de monitoreo]
    * [ ] **[OPS-05.E.2] [Documentación Final]:** [Estado: NO_INICIADO]
      * **Descripción:** Completar documentación de operación y procedimientos
      * **Criterios de éxito:** Documentación completa y actualizada
      * **Archivos involucrados:** [Documentos de operación y troubleshooting]
      * **Validación:** [Documentación revisada y aprobada]
      * **Estimación:** [Tiempo estimado: Xh]
      * **Investigación web requerida:** [Estándares de documentación]

---

## 🧪 **PRUEBAS Y VALIDACIÓN**

### **Pruebas Funcionales:**
- [ ] **Prueba 1:** [Descripción]
  - **Comando:** `[comando de prueba]`
  - **Resultado esperado:** [qué debe ocurrir]
  - **Estado:** [✅/❌/⏳]

- [ ] **Prueba 2:** [Descripción]
  - **Comando:** `[comando de prueba]`
  - **Resultado esperado:** [qué debe ocurrir]
  - **Estado:** [✅/❌/⏳]

### **Pruebas de Integración:**
- [ ] **Conectividad con [sistema/servicio]**
- [ ] **Funcionamiento con servicios existentes**
- [ ] **Performance bajo carga normal**
- [ ] **Logs generándose correctamente**

### **Pruebas de Seguridad:**
- [ ] **Puertos expuestos solo los necesarios**
- [ ] **Permisos de archivos correctos**
- [ ] **Usuarios/grupos configurados apropiadamente**
- [ ] **Certificados SSL/TLS válidos (si aplica)**

---

## 📊 **MONITOREO Y MANTENIMIENTO**

### **Métricas a Monitorear:**
- **CPU:** [umbral de alerta]
- **Memoria:** [umbral de alerta]
- **Disco:** [umbral de alerta]
- **Red:** [umbral de alerta]
- **Logs de error:** [patrón a buscar]

### **Comandos de Monitoreo:**
```bash
# Verificar estado general
[comando status]

# Ver logs en tiempo real
[comando logs]

# Verificar recursos
[comando recursos]
```

---

## 🔄 **PROCEDIMIENTOS DE ROLLBACK**

### **Plan de Rollback:**
En caso de que la operación falle o cause problemas:

1. **Detener servicios nuevos**
   ```bash
   sudo systemctl stop [servicio]
   ```

2. **Restaurar configuraciones**
   ```bash
   [comandos restaurar backup]
   ```

3. **Reiniciar servicios originales**
   ```bash
   sudo systemctl start [servicios_originales]
   ```

4. **Verificar funcionamiento**
   ```bash
   [comandos verificación]
   ```

### **Criterios para Rollback:**
- [ ] **Performance degradada** más del 20%
- [ ] **Servicios críticos** no funcionando
- [ ] **Errores constantes** en logs
- [ ] **Usuarios reportando** problemas

---

## 📝 **LOG DE EJECUCIÓN**

### **Registro de Actividades:**
| Fecha | Hora | Actividad | Estado | Observaciones |
|-------|------|-----------|--------|---------------|
| [YYYY-MM-DD] | [HH:mm] | [Descripción] | [✅/❌/⏳] | [Notas] |
| [YYYY-MM-DD] | [HH:mm] | [Descripción] | [✅/❌/⏳] | [Notas] |

### **Problemas Encontrados:**
- **[Problema 1]:** [Descripción] - [Solución aplicada]
- **[Problema 2]:** [Descripción] - [Solución aplicada]

### **Desviaciones del Plan:**
- **[Desviación 1]:** [Por qué ocurrió] - [Cómo se manejó]
- **[Desviación 2]:** [Por qué ocurrió] - [Cómo se manejó]

---

## ✅ **CHECKLIST FINAL**

### **Instalación Completada:**
- [ ] **Software instalado** correctamente
- [ ] **Configuración aplicada** según especificaciones
- [ ] **Servicios iniciados** y habilitados
- [ ] **Pruebas funcionales** pasadas
- [ ] **Integración verificada** con sistemas existentes
- [ ] **Monitoreo configurado** y funcionando

### **Documentación Completada:**
- [ ] **Procedimientos documentados** en este template
- [ ] **Configuraciones respaldadas** y documentadas
- [ ] **Troubleshooting guide** creado
- [ ] **Rollback procedures** validados
- [ ] **Handover documentation** preparada

### **Seguimiento Post-Implementación:**
- [ ] **Monitoreo 24h** sin incidentes
- [ ] **Performance baseline** establecido
- [ ] **Alertas configuradas** y probadas
- [ ] **Equipo capacitado** en nueva configuración
- [ ] **Documentación transferida** a equipo de soporte

### **Entrega:**
- [ ] **Usuario/equipo notificado** de completitud
- [ ] **Credenciales entregadas** (si aplica)
- [ ] **Documentación de usuario** proporcionada
- [ ] **Capacitación realizada** (si necesaria)
- [ ] **Soporte post-implementación** acordado

---

**ESTADO GENERAL DE LA OPERACIÓN: [PORCENTAJE]% COMPLETADO**

**PRÓXIMOS PASOS:**
1. [Siguiente acción prioritaria]
2. [Otra acción]
3. [Más acciones]
