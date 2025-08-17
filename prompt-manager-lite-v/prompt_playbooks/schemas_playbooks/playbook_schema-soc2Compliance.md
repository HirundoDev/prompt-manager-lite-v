# Playbook: Universal SOC 2 Compliance Schema Template

## Propósito
Este playbook guía el uso del schema `soc2Compliance.json` como template universal para documentar frameworks de compliance y seguridad. El schema utiliza placeholders `[VARIABLE]` que deben ser reemplazados con información específica del proyecto, permitiendo adaptabilidad a SOC 2, ISO 27001, PCI DSS, HIPAA, o cualquier otro framework de compliance.

## Filosofía Template-First
- **Schema como Receptor**: El schema está diseñado para RECIBIR información, no para definirla
- **Placeholders Universales**: Usar `[VARIABLE]` para todos los valores específicos del proyecto
- **Adaptabilidad Total**: Funciona para cualquier framework de compliance o estándar de seguridad
- **Mejores Prácticas Generales**: Incorpora patrones universales de compliance sin prescribir frameworks específicos

## Contexto del Schema

### Objetivo
El schema `soc2Compliance.json` proporciona una estructura completa para documentar y gestionar todos los aspectos de un programa de cumplimiento SOC 2, desde la definición del alcance hasta la implementación de controles y la gestión de auditorías.

### Relación con Otros Schemas
- **architecture.json**: Para controles técnicos y arquitectura de seguridad
- **forensicAudit.json**: Para procesos de auditoría y gestión de evidencia
- **operationalStrategy.json**: Para procedimientos operativos
- **testingStrategy.json**: Para pruebas de controles

### Documentos Generados
- **DOC033-SOC2Compliance.md**: Documento principal de cumplimiento SOC 2
- Políticas y procedimientos específicos de SOC 2
- Planes de auditoría y cronogramas
- Reportes de cumplimiento y métricas

## Estructura del Schema

### Campos Obligatorios

#### 1. Información Básica
```json
{
  "title": "Nombre del programa SOC 2",
  "description": "Descripción detallada de objetivos y alcance",
  "reportType": "Type I | Type II"
}
```

#### 2. Alcance (scope)
Define qué sistemas, datos y procesos están incluidos en la auditoría SOC 2:

**systemsInScope**: Lista de sistemas críticos
- Aplicaciones principales
- Infraestructura de soporte
- Bases de datos
- Servicios en la nube
- Redes y seguridad

**dataTypes**: Tipos de datos procesados
- Datos de clientes
- Información financiera
- Datos personales (PII)
- Información confidencial
- Datos de transacciones

**boundaries**: Límites claros del alcance
- Inclusiones específicas
- Exclusiones con justificación
- Alcance geográfico

#### 3. Criterios de Servicios de Confianza (trustServicesCriteria)
Los cinco criterios TSC con su aplicabilidad:

**Security (Obligatorio)**
- Siempre incluido en auditorías SOC 2
- Controles de acceso físico y lógico
- Gestión de identidad y autenticación
- Seguridad de red y monitoreo

**Availability (Opcional)**
- Incluir si hay compromisos de disponibilidad
- SLAs específicos de tiempo de actividad
- Sistemas críticos 24/7

**Processing Integrity (Opcional)**
- Incluir para procesamiento de transacciones críticas
- Sistemas financieros
- Procesamiento de datos sensibles

**Confidentiality (Opcional)**
- Incluir si se manejan datos bajo NDAs
- Información propietaria
- Datos confidenciales de clientes

**Privacy (Opcional)**
- Incluir si se procesan datos personales
- Cumplimiento con GDPR, CCPA
- Gestión del ciclo de vida de PII

#### 4. Gobernanza (governance)
Estructura organizacional para el programa SOC 2:

**executiveSponsor**: Patrocinador ejecutivo
- Típicamente CISO, CTO o CEO
- Responsabilidades de alto nivel
- Autoridad para tomar decisiones

**programLead**: Líder del programa
- Gestión día a día del programa
- Coordinación con auditores
- Gestión de evidencia

**committee**: Comité de cumplimiento
- Representantes de áreas clave
- Reuniones regulares
- Toma de decisiones colaborativa

#### 5. Controles (controls)
Lista detallada de controles implementados:

**Mapeo a TSC**: Cada control debe mapear a puntos de enfoque específicos
**Tipos de Control**:
- Preventivo: Previene incidentes
- Detectivo: Detecta problemas
- Correctivo: Corrige problemas
- Compensatorio: Mitiga riesgos residuales

**Naturaleza del Control**:
- Manual: Ejecutado por personas
- Automatizado: Ejecutado por sistemas
- IT-dependent manual: Manual pero depende de IT

#### 6. Proceso de Auditoría (auditProcess)
Información sobre el auditor y cronograma:

**Selección del Auditor**:
- Firma CPA certificada
- Experiencia en SOC 2
- Experiencia en la industria
- Referencias de clientes similares

**Cronograma**:
- Fecha de inicio
- Fases de la auditoría
- Entregables esperados
- Fecha de finalización

### Campos Opcionales Importantes

#### 7. Evaluación de Riesgos (riskAssessment)
- Metodología utilizada (NIST, ISO 27005)
- Registro de riesgos identificados
- Controles mitigantes
- Riesgo residual

#### 8. Gestión de Evidencia (evidenceManagement)
- Repositorio de evidencia
- Procesos de recolección
- Controles de acceso
- Retención y eliminación

#### 9. Monitoreo Continuo (monitoring)
- Métricas clave (KPIs)
- Dashboards de cumplimiento
- Alertas automáticas
- Reportes regulares

#### 10. Gestión de Deficiencias (deficiencyManagement)
- Proceso de identificación
- Clasificación de deficiencias
- Planes de remediación
- Seguimiento y validación

## Guías de Completado por Industria

### SaaS/Tecnología
**TSC Típicos**: Security + Availability + Confidentiality
**Controles Clave**:
- Autenticación multifactor
- Cifrado de datos
- Monitoreo de seguridad 24/7
- Gestión de parches
- Respaldo y recuperación

**Métricas Importantes**:
- Tiempo de actividad del sistema (>99.9%)
- Tiempo de respuesta a incidentes (<4 horas)
- Cobertura de parches (>95%)

### Servicios Financieros
**TSC Típicos**: Security + Processing Integrity + Confidentiality
**Controles Adicionales**:
- Segregación de funciones
- Reconciliación de transacciones
- Controles de fraude
- Auditoría de transacciones

**Métricas Específicas**:
- Precisión de procesamiento (99.99%)
- Tiempo de reconciliación
- Detección de fraude

### Healthcare/Salud
**TSC Típicos**: Security + Privacy + Confidentiality
**Controles Específicos**:
- Gestión de consentimiento
- Auditoría de acceso a datos
- Retención y eliminación de datos
- Controles de privacidad

**Consideraciones Especiales**:
- Cumplimiento con HIPAA
- Gestión de PHI (Protected Health Information)
- Derechos de los pacientes

## Proceso de Completado

### Fase 1: Planificación Inicial
1. **Definir Objetivos**
   - ¿Por qué necesita SOC 2?
   - ¿Qué quiere demostrar?
   - ¿Cuáles son los drivers de negocio?

2. **Determinar Alcance**
   - Sistemas críticos para el negocio
   - Datos sensibles procesados
   - Ubicaciones geográficas
   - Proveedores críticos

3. **Seleccionar TSC**
   - Basado en el modelo de negocio
   - Requisitos contractuales
   - Expectativas de clientes
   - Regulaciones aplicables

### Fase 2: Evaluación Actual
1. **Inventario de Controles**
   - Controles existentes
   - Gaps identificados
   - Efectividad actual
   - Evidencia disponible

2. **Evaluación de Riesgos**
   - Amenazas identificadas
   - Vulnerabilidades conocidas
   - Impacto potencial
   - Probabilidad de ocurrencia

3. **Análisis de Brechas**
   - Controles faltantes
   - Controles inefectivos
   - Evidencia insuficiente
   - Procesos inadecuados

### Fase 3: Diseño del Programa
1. **Estructura de Gobernanza**
   - Roles y responsabilidades
   - Comités y reportes
   - Escalación y toma de decisiones
   - Comunicación y coordinación

2. **Diseño de Controles**
   - Controles por TSC
   - Mapeo a puntos de enfoque
   - Procedimientos detallados
   - Evidencia requerida

3. **Procesos de Soporte**
   - Gestión de evidencia
   - Monitoreo continuo
   - Gestión de deficiencias
   - Capacitación y concientización

### Fase 4: Implementación
1. **Implementar Controles**
   - Seguir diseño aprobado
   - Documentar procedimientos
   - Capacitar al personal
   - Probar efectividad

2. **Establecer Monitoreo**
   - Configurar métricas
   - Implementar dashboards
   - Establecer alertas
   - Definir reportes

3. **Preparar Evidencia**
   - Recolectar evidencia histórica
   - Establecer procesos continuos
   - Organizar repositorio
   - Validar completitud

## Validación del Schema

### Campos Obligatorios
- [ ] `title` - Nombre descriptivo del programa
- [ ] `description` - Objetivos claros y alcance
- [ ] `scope` - Sistemas, datos y límites definidos
- [ ] `reportType` - Type I o Type II especificado
- [ ] `trustServicesCriteria` - Al menos Security incluido
- [ ] `governance` - Roles y responsabilidades asignados
- [ ] `controls` - Controles mapeados a TSC
- [ ] `auditProcess` - Auditor y cronograma definidos

### Consistencia Interna
- [ ] Controles mapean a TSC seleccionados
- [ ] Evidencia corresponde a controles
- [ ] Métricas alineadas con objetivos
- [ ] Cronograma realista y factible

### Completitud por TSC
**Security (Obligatorio)**:
- [ ] Controles de acceso definidos
- [ ] Gestión de identidad implementada
- [ ] Monitoreo de seguridad establecido
- [ ] Respuesta a incidentes documentada

**Availability (Si aplica)**:
- [ ] SLAs definidos
- [ ] Monitoreo de disponibilidad
- [ ] Planes de continuidad
- [ ] Procedimientos de recuperación

**Processing Integrity (Si aplica)**:
- [ ] Controles de validación
- [ ] Reconciliación de datos
- [ ] Gestión de errores
- [ ] Auditoría de transacciones

**Confidentiality (Si aplica)**:
- [ ] Clasificación de datos
- [ ] Controles de acceso
- [ ] Cifrado implementado
- [ ] Gestión de claves

**Privacy (Si aplica)**:
- [ ] Gestión de consentimiento
- [ ] Derechos de sujetos de datos
- [ ] Retención y eliminación
- [ ] Transferencias internacionales

## Errores Comunes a Evitar

### Errores de Alcance
- **Alcance muy amplio**: Incluir sistemas no críticos
- **Alcance muy estrecho**: Excluir sistemas importantes
- **Límites poco claros**: Ambigüedad en inclusiones/exclusiones

### Errores de Mapeo
- **Mapeo incorrecto**: Controles no alineados con TSC
- **Puntos de enfoque omitidos**: No cubrir todos los requerimientos
- **Controles duplicados**: Redundancia sin valor agregado

### Errores de Implementación
- **Controles teóricos**: Controles que no se ejecutan realmente
- **Evidencia insuficiente**: No generar evidencia adecuada
- **Responsabilidades poco claras**: Roles mal definidos

### Errores de Cronograma
- **Tiempos irreales**: Subestimar esfuerzo requerido
- **Dependencias no consideradas**: No planificar interdependencias
- **Recursos insuficientes**: No asignar recursos adecuados

## Mantenimiento del Schema

### Actualizaciones Regulares
- **Trimestral**: Métricas y estado de controles
- **Semestral**: Revisión de riesgos y controles
- **Anual**: Revisión completa del programa
- **Ad-hoc**: Cambios significativos en el entorno

### Triggers para Actualización
- Cambios en sistemas críticos
- Nuevas regulaciones o estándares
- Resultados de auditorías
- Incidentes de seguridad significativos
- Cambios organizacionales

### Versionado
- Mantener historial de cambios
- Documentar razones para cambios
- Comunicar cambios a stakeholders
- Validar impacto en auditoría

## Integración con Otros Schemas

### Schemas Relacionados
- **architecture.json**: Controles técnicos implementados
- **forensicAudit.json**: Procesos de auditoría y evidencia
- **operationalStrategy.json**: Procedimientos operativos
- **testingStrategy.json**: Pruebas de controles

### Sincronización
- Asegurar consistencia entre schemas
- Evitar duplicación de información
- Mantener referencias actualizadas
- Validar cambios en cascada

## Herramientas y Recursos

### Herramientas Recomendadas
- **Plataformas GRC**: Gestión integrada de cumplimiento
- **Herramientas de Monitoreo**: Métricas en tiempo real
- **Sistemas de Gestión Documental**: Control de versiones
- **Plataformas de Evidencia**: Recolección automatizada

### Referencias Externas
- **AICPA Trust Services Criteria**: Estándar oficial
- **SOC 2 Implementation Guide**: Guías de implementación
- **Industry Best Practices**: Mejores prácticas por sector
- **Regulatory Guidance**: Orientación regulatoria

### Capacitación Recomendada
- **Certificación SOC 2**: Para líderes del programa
- **Auditoría Interna**: Para propietarios de controles
- **Gestión de Riesgos**: Para evaluadores de riesgo
- **Marcos de Seguridad**: NIST, ISO 27001 para contexto

---

**Nota**: Este schema debe actualizarse cuando se publiquen nuevas versiones de los Trust Services Criteria o cambien significativamente los requisitos de SOC 2.