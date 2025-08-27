# DOC035 - Error Tracking Universal Framework

**Versión:** 1.0  
**Fecha:** 2025-08-25  
**Categoría:** Playbook Universal  
**Aplicabilidad:** Independiente de tecnología  

---

## 🎯 **PROPÓSITO**

Marco universal para detectar, documentar, rastrear y resolver errores de manera sistemática en cualquier proyecto de desarrollo, independientemente de la tecnología utilizada.

---

## 📋 **METODOLOGÍA CORE**

### **FASE 1: DETECCIÓN PROACTIVA**

#### **1.1 Configuración de Monitoreo**
```markdown
**HERRAMIENTAS POR TECNOLOGÍA:**
- **JavaScript/Node.js:** Sentry, LogRocket, Bugsnag
- **Python:** Sentry, Rollbar, Airbrake
- **Java:** Sentry, Bugsnag, Raygun
- **Go:** Sentry, Honeybadger
- **PHP:** Sentry, Bugsnag, Rollbar
- **C#/.NET:** Sentry, Raygun, Elmah
- **Frontend:** Sentry, LogRocket, FullStory
```

#### **1.2 Puntos de Captura Obligatorios**
- **Excepciones no manejadas** (`uncaughtException`, `unhandledRejection`)
- **Errores de API** (4xx, 5xx responses)
- **Timeouts y fallos de conexión**
- **Errores de validación de datos**
- **Fallos de autenticación/autorización**
- **Errores de base de datos**
- **Errores de servicios externos**

### **FASE 2: CLASIFICACIÓN SISTEMÁTICA**

#### **2.1 Categorías de Error**
```markdown
**OPERACIONALES (Esperados):**
- Errores de validación de entrada
- Fallos de conectividad temporales
- Límites de recursos alcanzados
- Timeouts de servicios externos

**PROGRAMÁTICOS (Bugs):**
- Referencias null/undefined
- Errores de lógica de negocio
- Problemas de concurrencia
- Memory leaks
- Errores de configuración
```

#### **2.2 Niveles de Severidad**
```markdown
**CRÍTICO:** Aplicación no funcional, pérdida de datos
**ALTO:** Funcionalidad principal afectada
**MEDIO:** Funcionalidad secundaria afectada
**BAJO:** Problemas menores, UX degradada
**INFO:** Eventos informativos para análisis
```

### **FASE 3: DOCUMENTACIÓN ESTRUCTURADA**

#### **3.1 Template de Error Report**
```markdown
## ERROR-[ID] - [TÍTULO_DESCRIPTIVO]

**Fecha:** [YYYY-MM-DD HH:mm:ss]
**Severidad:** [CRÍTICO/ALTO/MEDIO/BAJO/INFO]
**Categoría:** [OPERACIONAL/PROGRAMÁTICO]
**Tecnología:** [Lenguaje/Framework]
**Entorno:** [DEV/STAGING/PROD]

### **Descripción del Error:**
[Descripción clara y concisa del problema]

### **Stack Trace:**
```
[Stack trace completo]
```

### **Contexto de Reproducción:**
- **URL/Endpoint:** [Si aplica]
- **Datos de entrada:** [Payload, parámetros]
- **Usuario afectado:** [ID o tipo de usuario]
- **Navegador/OS:** [Si es frontend]
- **Timestamp:** [Momento exacto]

### **Impacto:**
- **Usuarios afectados:** [Número o porcentaje]
- **Funcionalidad impactada:** [Qué no funciona]
- **Duración:** [Tiempo del problema]

### **Investigación:**
- **Causa raíz:** [Análisis técnico]
- **Factores contribuyentes:** [Condiciones que causaron el error]
- **Logs relevantes:** [Enlaces o extractos]

### **Solución Aplicada:**
- **Acciones tomadas:** [Pasos específicos]
- **Código modificado:** [Archivos/funciones]
- **Validación:** [Cómo se verificó la solución]

### **Prevención:**
- **Mejoras implementadas:** [Validaciones, tests, monitoreo]
- **Lecciones aprendidas:** [Qué evitar en el futuro]
```

### **FASE 4: PROCESO DE RESOLUCIÓN**

#### **4.1 Flujo de Respuesta**
```markdown
**INMEDIATO (0-15 min):**
1. Confirmar el error y su severidad
2. Evaluar impacto en usuarios
3. Implementar workaround temporal si es crítico
4. Notificar a stakeholders relevantes

**INVESTIGACIÓN (15 min - 2h):**
1. Reproducir el error en entorno controlado
2. Analizar logs y stack traces
3. Identificar causa raíz
4. Documentar hallazgos

**RESOLUCIÓN (2h - 24h):**
1. Desarrollar solución definitiva
2. Implementar tests para prevenir regresión
3. Desplegar fix en staging
4. Validar solución completa
5. Desplegar a producción

**POST-MORTEM (24-48h):**
1. Documentar incidente completo
2. Identificar mejoras de proceso
3. Actualizar monitoreo/alertas
4. Compartir lecciones aprendidas
```

#### **4.2 Criterios de Priorización**
```markdown
**CRÍTICO - Resolver inmediatamente:**
- Aplicación completamente caída
- Pérdida de datos
- Vulnerabilidades de seguridad
- Errores que afectan >50% usuarios

**ALTO - Resolver en 24h:**
- Funcionalidad principal degradada
- Errores que afectan 10-50% usuarios
- Performance severamente impactada

**MEDIO - Resolver en 1 semana:**
- Funcionalidades secundarias afectadas
- Errores que afectan <10% usuarios
- UX degradada pero funcional

**BAJO - Resolver en sprint actual:**
- Problemas menores de UI/UX
- Optimizaciones de performance
- Errores edge case raros
```

---

## 🔧 **HERRAMIENTAS Y CONFIGURACIÓN**

### **Configuración Básica por Tecnología**

#### **Node.js/JavaScript**
```javascript
// Configuración Sentry
const Sentry = require('@sentry/node');

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 1.0,
  beforeSend(event, hint) {
    // Filtrar información sensible
    if (event.exception) {
      const error = hint.originalException;
      event.tags = {
        ...event.tags,
        errorType: error.isOperational ? 'operational' : 'programmer',
        severity: error.severity || 'medium'
      };
    }
    return event;
  }
});

// Manejo de errores no capturados
process.on('uncaughtException', (error) => {
  Sentry.captureException(error);
  if (!error.isOperational) {
    process.exit(1);
  }
});

process.on('unhandledRejection', (reason) => {
  Sentry.captureException(reason);
});
```

#### **Python**
```python
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    environment=os.environ.get('ENVIRONMENT'),
    traces_sample_rate=1.0,
    before_send=filter_sensitive_data
)

def filter_sensitive_data(event, hint):
    # Filtrar datos sensibles
    if 'exception' in event:
        event['tags'] = {
            **event.get('tags', {}),
            'error_type': getattr(hint.get('exc_info', [None, None, None])[1], 'error_type', 'unknown'),
            'severity': getattr(hint.get('exc_info', [None, None, None])[1], 'severity', 'medium')
        }
    return event
```

### **Logging Estructurado**
```json
{
  "timestamp": "2025-08-25T17:59:59Z",
  "level": "ERROR",
  "message": "Database connection failed",
  "error_id": "ERR-DB-001",
  "context": {
    "user_id": "user123",
    "request_id": "req-456",
    "endpoint": "/api/users",
    "database": "postgres-main"
  },
  "stack_trace": "...",
  "tags": ["database", "connection", "critical"]
}
```

---

## 📊 **MÉTRICAS Y MONITOREO**

### **KPIs Esenciales**
- **Error Rate:** Errores por minuto/hora
- **MTTR (Mean Time To Resolution):** Tiempo promedio de resolución
- **MTTD (Mean Time To Detection):** Tiempo promedio de detección
- **Error Distribution:** Distribución por categoría/severidad
- **Affected Users:** Usuarios impactados por errores
- **Recurring Errors:** Errores que se repiten

### **Alertas Configuradas**
```yaml
# Ejemplo configuración alertas
alerts:
  critical_errors:
    condition: "error_rate > 10 per minute"
    notification: ["slack", "email", "sms"]
    escalation: "immediate"
  
  high_error_rate:
    condition: "error_rate > 5 per minute for 5 minutes"
    notification: ["slack", "email"]
    escalation: "15_minutes"
  
  new_error_type:
    condition: "new unique error detected"
    notification: ["slack"]
    escalation: "30_minutes"
```

---

## 🔄 **INTEGRACIÓN CON DESARROLLO**

### **En template-pendingtask.md**
```markdown
## 🚨 **TRACKING DE ERRORES**

### **Errores Encontrados:**
- [ ] **[ERR-001]** [Descripción breve] - [Severidad] - [Estado]
- [ ] **[ERR-002]** [Descripción breve] - [Severidad] - [Estado]

### **Soluciones Aplicadas:**
- [x] **[ERR-001]** Implementado try-catch en función X
- [x] **[ERR-002]** Agregada validación de entrada

### **Mejoras de Monitoreo:**
- [ ] Configurar alertas para endpoint crítico
- [ ] Agregar logging estructurado en módulo Y
- [ ] Implementar health checks
```

### **Code Review Checklist**
```markdown
**ERROR HANDLING REVIEW:**
- [ ] ¿Todos los errores tienen códigos únicos?
- [ ] ¿Se implementó logging apropiado?
- [ ] ¿Hay manejo de errores en funciones async?
- [ ] ¿Se validan inputs antes de procesamiento?
- [ ] ¿Errores operacionales están marcados correctamente?
- [ ] ¿Se agregaron tests para casos de error?
```

---

## 📚 **MEJORES PRÁCTICAS**

### **DO's**
- ✅ Usar códigos de error únicos y consistentes
- ✅ Implementar logging estructurado con contexto
- ✅ Distinguir entre errores operacionales y programáticos
- ✅ Configurar alertas basadas en severidad
- ✅ Documentar todos los errores críticos
- ✅ Implementar circuit breakers para servicios externos
- ✅ Usar herramientas de monitoreo centralizadas

### **DON'Ts**
- ❌ Ignorar errores o usar try-catch vacíos
- ❌ Exponer stack traces a usuarios finales
- ❌ Usar console.log para errores en producción
- ❌ Mezclar errores de negocio con errores técnicos
- ❌ Reintentar operaciones sin límites
- ❌ Hardcodear mensajes de error
- ❌ Fallar silenciosamente

---

## 🎯 **CASOS DE USO COMUNES**

### **API REST Errors**
```javascript
// Estructura estándar para errores de API
const ApiError = {
  error_code: "API-AUTH-001",
  message: "Invalid authentication token",
  details: "Token expired or malformed",
  timestamp: "2025-08-25T17:59:59Z",
  request_id: "req-123456",
  documentation_url: "https://docs.api.com/errors/auth"
};
```

### **Database Errors**
```python
# Manejo de errores de base de datos
try:
    result = db.execute(query)
except DatabaseConnectionError as e:
    logger.error("DB-CONN-001: Database connection failed", 
                extra={"query": query, "error": str(e)})
    raise OperationalError("Database temporarily unavailable")
except DatabaseTimeoutError as e:
    logger.error("DB-TIMEOUT-001: Query timeout", 
                extra={"query": query, "timeout": e.timeout})
    raise OperationalError("Operation timed out")
```

---

## 🔗 **RECURSOS ADICIONALES**

- **Sentry Documentation:** https://docs.sentry.io/
- **Error Handling Best Practices:** Node.js, Python, Java guides
- **Monitoring Tools Comparison:** Sentry vs Rollbar vs Bugsnag
- **Incident Response Templates:** Post-mortem templates
- **Error Code Standards:** Industry standards por tecnología

---

**PRÓXIMO PASO:** Integrar este framework con DOC036-ErrorCodes.md para códigos únicos de error.
