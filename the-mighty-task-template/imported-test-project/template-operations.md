# **OPERACIONES Y CONTROL DE SISTEMAS: [TÍTULO DE LA OPERACIÓN]**

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

**Responsable:** [NOMBRE]  
**Tipo:** [INSTALACIÓN/CONFIGURACIÓN/MIGRACIÓN/MANTENIMIENTO]  
**Prioridad:** [ALTA/MEDIA/BAJA]  

---

## 🎯 **OBJETIVO DE LA OPERACIÓN**

### **Descripción:**
[¿Qué se va a instalar, configurar o implementar?]

### **Justificación:**
[¿Por qué es necesaria esta operación?]

### **Resultado Esperado:**
[¿Qué debe funcionar al finalizar?]

---

## 📋 **INFORMACIÓN DEL SISTEMA**

### **Entorno:**
- **Sistema Operativo:** [Linux/Windows/macOS] [versión]
- **Arquitectura:** [x64/ARM/etc.]
- **Recursos disponibles:** [RAM/CPU/Disco]
- **Red:** [Configuración de red relevante]

### **Servicios/Aplicaciones Existentes:**
- **[Servicio 1]:** [versión] - [estado]
- **[Servicio 2]:** [versión] - [estado]
- **[Servicio 3]:** [versión] - [estado]

### **Dependencias:**
- **[Dependencia 1]:** [versión requerida]
- **[Dependencia 2]:** [versión requerida]
- **[Dependencia 3]:** [versión requerida]

---

## 🔍 **INVESTIGACIÓN Y COMPARACIÓN**

### **Opciones Evaluadas:**

#### **Opción 1: [NOMBRE_HERRAMIENTA_1]**
- **Pros:** 
  - ✅ [Ventaja 1]
  - ✅ [Ventaja 2]
- **Contras:**
  - ❌ [Desventaja 1]
  - ❌ [Desventaja 2]
- **Costo:** [Gratuito/Licencia/Suscripción]
- **Complejidad:** [Baja/Media/Alta]

#### **Opción 2: [NOMBRE_HERRAMIENTA_2]**
- **Pros:** 
  - ✅ [Ventaja 1]
  - ✅ [Ventaja 2]
- **Contras:**
  - ❌ [Desventaja 1]
  - ❌ [Desventaja 2]
- **Costo:** [Gratuito/Licencia/Suscripción]
- **Complejidad:** [Baja/Media/Alta]

#### **Opción 3: [NOMBRE_HERRAMIENTA_3]**
- **Pros:** 
  - ✅ [Ventaja 1]
  - ✅ [Ventaja 2]
- **Contras:**
  - ❌ [Desventaja 1]
  - ❌ [Desventaja 2]
- **Costo:** [Gratuito/Licencia/Suscripción]
- **Complejidad:** [Baja/Media/Alta]

### **Decisión Final:**
**Herramienta elegida:** [NOMBRE_HERRAMIENTA]  
**Razones:** [Por qué se eligió esta opción]

---

## 📦 **PLAN DE INSTALACIÓN/CONFIGURACIÓN**

### **FASE 1: Preparación**
**Tiempo estimado:** [X minutos]

- [ ] **Backup del sistema actual**
  - [ ] Configuraciones existentes
  - [ ] Datos críticos
  - [ ] Lista de servicios activos
- [ ] **Verificar requisitos del sistema**
  - [ ] Espacio en disco suficiente
  - [ ] RAM disponible
  - [ ] Puertos necesarios libres
- [ ] **Descargar recursos necesarios**
  - [ ] Instaladores/paquetes
  - [ ] Archivos de configuración
  - [ ] Documentación oficial

### **FASE 2: Instalación**
**Tiempo estimado:** [X minutos]

#### **Comandos de Instalación:**
```bash
# Paso 1: [Descripción]
[comando 1]

# Paso 2: [Descripción]
[comando 2]

# Paso 3: [Descripción]
[comando 3]
```

#### **Checklist de Instalación:**
- [ ] **Paso 1:** [Descripción detallada]
  - **Comando:** `[comando]`
  - **Resultado esperado:** [qué debe aparecer]
  - **Verificación:** `[comando verificación]`

- [ ] **Paso 2:** [Descripción detallada]
  - **Comando:** `[comando]`
  - **Resultado esperado:** [qué debe aparecer]
  - **Verificación:** `[comando verificación]`

- [ ] **Paso 3:** [Descripción detallada]
  - **Comando:** `[comando]`
  - **Resultado esperado:** [qué debe aparecer]
  - **Verificación:** `[comando verificación]`

### **FASE 3: Configuración**
**Tiempo estimado:** [X minutos]

#### **Archivos de Configuración:**

**Archivo 1: [ruta/archivo.conf]**
```ini
# Configuración para [propósito]
[configuración]
```

**Archivo 2: [ruta/archivo.yml]**
```yaml
# Configuración para [propósito]
configuracion:
  parametro1: valor1
  parametro2: valor2
```

#### **Configuraciones Paso a Paso:**
- [ ] **Configurar [aspecto 1]**
  - **Archivo:** `[ruta]`
  - **Cambios:** [descripción de cambios]
  - **Comando aplicar:** `[comando]`

- [ ] **Configurar [aspecto 2]**
  - **Archivo:** `[ruta]`
  - **Cambios:** [descripción de cambios]
  - **Comando aplicar:** `[comando]`

### **FASE 4: Inicio y Habilitación**
**Tiempo estimado:** [X minutos]

- [ ] **Iniciar servicios**
  ```bash
  sudo systemctl start [servicio]
  sudo systemctl enable [servicio]
  ```

- [ ] **Verificar estado**
  ```bash
  sudo systemctl status [servicio]
  ```

- [ ] **Configurar inicio automático**
  - [ ] Agregar a systemd/init
  - [ ] Configurar dependencias
  - [ ] Probar reinicio del sistema

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

- [ ] **Prueba 3:** [Descripción]
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

# Verificar conectividad
[comando conectividad]
```

### **Mantenimiento Programado:**
- **Diario:** [tareas diarias]
- **Semanal:** [tareas semanales]
- **Mensual:** [tareas mensuales]
- **Trimestral:** [tareas trimestrales]

### **Procedimientos de Backup:**
```bash
# Backup de configuración
[comando backup config]

# Backup de datos
[comando backup datos]

# Verificar backup
[comando verificar backup]
```

---

## 🚨 **TROUBLESHOOTING**

### **Problemas Comunes:**

#### **Error 1: [Descripción del error]**
- **Síntomas:** [cómo se manifiesta]
- **Causa probable:** [qué lo causa]
- **Solución:**
  ```bash
  [comandos de solución]
  ```
- **Prevención:** [cómo evitarlo]

#### **Error 2: [Descripción del error]**
- **Síntomas:** [cómo se manifiesta]
- **Causa probable:** [qué lo causa]
- **Solución:**
  ```bash
  [comandos de solución]
  ```
- **Prevención:** [cómo evitarlo]

#### **Error 3: [Descripción del error]**
- **Síntomas:** [cómo se manifiesta]
- **Causa probable:** [qué lo causa]
- **Solución:**
  ```bash
  [comandos de solución]
  ```
- **Prevención:** [cómo evitarlo]

### **Comandos de Diagnóstico:**
```bash
# Verificar logs de error
[comando logs error]

# Verificar conectividad
[comando test conectividad]

# Verificar configuración
[comando validar config]

# Verificar recursos del sistema
[comando recursos sistema]
```

---

## 📚 **DOCUMENTACIÓN Y RECURSOS**

### **Documentación Oficial:**
- [Nombre] - [URL] - [Descripción]
- [Nombre] - [URL] - [Descripción]

### **Tutoriales Útiles:**
- [Título] - [URL] - [Relevancia]
- [Título] - [URL] - [Relevancia]

### **Comunidad/Soporte:**
- **Foro oficial:** [URL]
- **Stack Overflow:** [tags relevantes]
- **Discord/Slack:** [enlaces de comunidad]
- **GitHub Issues:** [repositorio]

### **Herramientas Relacionadas:**
- **[Herramienta 1]:** [Descripción] - [URL]
- **[Herramienta 2]:** [Descripción] - [URL]

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

---

**ESTADO GENERAL DE LA OPERACIÓN: [PORCENTAJE]% COMPLETADO**

**PRÓXIMOS PASOS:**
1. [Siguiente acción prioritaria]
2. [Otra acción]
3. [Más acciones]
- [ ] **Backup realizado** de nueva configuración
- [ ] **Documentación actualizada**

### **Entrega:**
- [ ] **Usuario/equipo notificado** de completitud
- [ ] **Credenciales entregadas** (si aplica)
- [ ] **Documentación de usuario** proporcionada
- [ ] **Capacitación realizada** (si necesaria)
- [ ] **Soporte post-implementación** acordado

---

## 🎯 **PRÓXIMOS PASOS**

### **Seguimiento Inmediato (24-48h):**
- [ ] **Monitorear logs** por errores
- [ ] **Verificar performance** del sistema
- [ ] **Confirmar funcionamiento** con usuarios
- [ ] **Ajustar configuración** si es necesario

### **Seguimiento a Mediano Plazo (1-2 semanas):**
- [ ] **Optimizar configuración** basado en uso real
- [ ] **Actualizar documentación** con lecciones aprendidas
- [ ] **Planificar actualizaciones** futuras
- [ ] **Evaluar necesidad** de herramientas adicionales

### **Mantenimiento Futuro:**
- [ ] **Calendario de actualizaciones** definido
- [ ] **Procedimientos de backup** automatizados
- [ ] **Alertas de monitoreo** configuradas
- [ ] **Plan de escalamiento** documentado

---

**ESTADO FINAL:** [COMPLETADO/EN_PROGRESO/FALLIDO]  
**TIEMPO TOTAL:** [X horas]  
**ÚLTIMA ACTUALIZACIÓN:** [YYYY-MM-DD HH:mm]
