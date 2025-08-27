"""
Operations Templates
===================

Templates universales para error tracking, códigos de error y operaciones de sistemas.
"""

def create_error_tracking_template(theme, date_str, filename):
    """Marco de referencia para error tracking universal"""
    return f'''# Error Tracking - Marco de Referencia

**Fecha:** {date_str}  
**Tema:** {theme}  
**Playbook:** {filename}

---

## 🎯 **OBJETIVO DEL ERROR TRACKING**

### **Descripción:**
Implementar un sistema robusto de tracking de errores que sea:
- **Universal:** Funciona con cualquier tecnología
- **Escalable:** Crece con el proyecto
- **Actionable:** Permite tomar decisiones basadas en datos

### **Criterios de Éxito:**
- [ ] Errores categorizados y priorizados
- [ ] Métricas de error establecidas
- [ ] Alertas configuradas para errores críticos
- [ ] Dashboard de monitoreo operativo

---

## 📋 **CHECKLIST DE IMPLEMENTACIÓN**

### **Fase 1: Configuración Base**
- [ ] **Definir categorías de errores**
  - Críticos (afectan funcionalidad principal)
  - Importantes (afectan UX pero no bloquean)
  - Menores (mejoras de calidad)
  
- [ ] **Establecer niveles de severidad**
  - FATAL: Sistema no funciona
  - ERROR: Funcionalidad específica falla
  - WARNING: Comportamiento inesperado
  - INFO: Información de contexto

### **Fase 2: Instrumentación**
- [ ] **Configurar logging estructurado**
  - Formato consistente (JSON recomendado)
  - Campos obligatorios: timestamp, level, message, context
  - Correlación IDs para tracing

- [ ] **Implementar captura de errores**
  - Try-catch blocks estratégicos
  - Error boundaries (frontend)
  - Global error handlers

### **Fase 3: Agregación y Análisis**
- [ ] **Configurar herramienta de agregación**
  - Opciones: ELK Stack, Splunk, DataDog, Sentry
  - Centralización de logs
  - Búsqueda y filtrado eficiente

- [ ] **Establecer métricas clave**
  - Error rate por endpoint/función
  - MTTR (Mean Time To Resolution)
  - Error frequency trends
  - User impact metrics

### **Fase 4: Alertas y Respuesta**
- [ ] **Configurar alertas inteligentes**
  - Umbrales dinámicos
  - Escalation policies
  - Integración con herramientas de comunicación

- [ ] **Definir procedimientos de respuesta**
  - Runbooks para errores comunes
  - Escalation matrix
  - Post-mortem templates

---

## 🔧 **IMPLEMENTACIÓN TÉCNICA**

### **Logging Estructurado (Ejemplo)**
```json
{{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "ERROR",
  "service": "user-auth",
  "correlation_id": "req-123-456",
  "error_code": "AUTH_001",
  "message": "Invalid credentials provided",
  "context": {{
    "user_id": "user_789",
    "endpoint": "/api/login",
    "ip_address": "192.168.1.100"
  }}
}}
```

### **Error Categorization Schema**
```yaml
error_categories:
  authentication:
    codes: ["AUTH_001", "AUTH_002", "AUTH_003"]
    severity: "HIGH"
    
  database:
    codes: ["DB_001", "DB_002", "DB_003"]
    severity: "CRITICAL"
    
  validation:
    codes: ["VAL_001", "VAL_002"]
    severity: "MEDIUM"
```

---

## 📊 **MÉTRICAS Y MONITOREO**

### **KPIs Principales**
- **Error Rate:** < 1% para endpoints críticos
- **MTTR:** < 15 minutos para errores críticos
- **Error Diversity:** Número de tipos únicos de errores
- **Resolution Rate:** % de errores resueltos en SLA

### **Dashboard Requerido**
- Vista en tiempo real de errores activos
- Trends históricos por categoría
- Top errores por frecuencia e impacto
- Health status por servicio/componente

---

## 🚨 **ALERTAS Y ESCALACIÓN**

### **Configuración de Alertas**
```yaml
alerts:
  critical_error_spike:
    condition: "error_rate > 5% in 5min"
    channels: ["slack", "pagerduty"]
    
  database_errors:
    condition: "db_errors > 10 in 1min"
    channels: ["email", "slack"]
    
  authentication_failures:
    condition: "auth_failures > 50 in 5min"
    channels: ["security-team"]
```

---

## 📚 **RECURSOS Y REFERENCIAS**

### **Herramientas Recomendadas**
- **Open Source:** ELK Stack, Grafana, Prometheus
- **SaaS:** Sentry, DataDog, New Relic, Rollbar
- **Cloud Native:** CloudWatch, Azure Monitor, GCP Logging

### **Best Practices**
- Evitar logging de información sensible
- Usar sampling para high-volume logs
- Implementar log rotation y retention policies
- Correlacionar errores con métricas de negocio

---

*Consultar playbook original: `playbooks/{filename}`*
'''

def create_error_codes_template(theme, date_str, filename):
    """Marco de referencia para códigos únicos de error"""
    return f'''# Error Codes - Marco de Referencia

**Fecha:** {date_str}  
**Tema:** {theme}  
**Playbook:** {filename}

---

## 🎯 **OBJETIVO DE CÓDIGOS ÚNICOS**

### **Descripción:**
Establecer un sistema de códigos únicos de error que permita:
- **Identificación rápida** de problemas específicos
- **Trazabilidad completa** desde logs hasta documentación
- **Automatización** de respuestas y resoluciones
- **Métricas precisas** por tipo de error

### **Criterios de Éxito:**
- [ ] Nomenclatura consistente implementada
- [ ] Códigos únicos para cada tipo de error
- [ ] Documentación automática de códigos
- [ ] Validación en CI/CD de unicidad

---

## 📋 **CHECKLIST DE IMPLEMENTACIÓN**

### **Fase 1: Diseño del Sistema**
- [ ] **Definir convención de nomenclatura**
  - Formato: [DOMAIN]_[CATEGORY]_[NUMBER]
  - Ejemplo: AUTH_LOGIN_001, DB_CONNECTION_002
  
- [ ] **Establecer dominios principales**
  - AUTH: Autenticación y autorización
  - DB: Base de datos y persistencia
  - API: Endpoints y comunicación
  - VAL: Validación de datos
  - SYS: Errores de sistema

### **Fase 2: Implementación Técnica**
- [ ] **Crear registro central de códigos**
  - Archivo/base de datos con todos los códigos
  - Descripción detallada de cada error
  - Procedimientos de resolución

- [ ] **Implementar validación de unicidad**
  - Script de verificación en CI/CD
  - Prevenir códigos duplicados
  - Alertas por códigos no documentados

### **Fase 3: Integración con Logging**
- [ ] **Modificar sistema de logging**
  - Incluir error_code en todos los logs
  - Correlacionar con mensajes descriptivos
  - Mantener backward compatibility

- [ ] **Actualizar error handlers**
  - Mapear excepciones a códigos
  - Incluir contexto relevante
  - Facilitar debugging

---

## 🔧 **IMPLEMENTACIÓN TÉCNICA**

### **Convención de Nomenclatura**
```
Formato: [DOMAIN]_[CATEGORY]_[NUMBER]

Dominios:
- AUTH: Autenticación/Autorización
- DB: Base de datos
- API: APIs y comunicación
- VAL: Validación
- SYS: Sistema
- BIZ: Lógica de negocio

Categorías por dominio:
AUTH: LOGIN, LOGOUT, PERMISSION, TOKEN
DB: CONNECTION, QUERY, TRANSACTION, MIGRATION
API: REQUEST, RESPONSE, TIMEOUT, RATE_LIMIT
VAL: INPUT, SCHEMA, BUSINESS_RULE
SYS: MEMORY, DISK, NETWORK, CONFIG
```

### **Registro de Códigos (JSON)**
```json
{{
  "error_codes": {{
    "AUTH_LOGIN_001": {{
      "description": "Invalid username or password",
      "severity": "MEDIUM",
      "category": "authentication",
      "resolution": "Verify credentials and account status",
      "related_docs": ["auth-troubleshooting.md"],
      "examples": ["User entered wrong password", "Account locked"]
    }},
    "DB_CONNECTION_001": {{
      "description": "Database connection timeout",
      "severity": "HIGH",
      "category": "infrastructure",
      "resolution": "Check database connectivity and pool settings",
      "related_docs": ["db-troubleshooting.md"],
      "examples": ["Connection pool exhausted", "Network issues"]
    }}
  }}
}}
```

### **Implementación en Código**
```python
# Python example
class ErrorCodes:
    AUTH_LOGIN_001 = "AUTH_LOGIN_001"
    AUTH_LOGIN_002 = "AUTH_LOGIN_002"
    DB_CONNECTION_001 = "DB_CONNECTION_001"
    
    @classmethod
    def get_description(cls, code):
        return ERROR_REGISTRY.get(code, {{}}).get('description', 'Unknown error')

# Usage
logger.error("Authentication failed", extra={{
    "error_code": ErrorCodes.AUTH_LOGIN_001,
    "user_id": user.id,
    "correlation_id": request.correlation_id
}})
```

---

## 🔍 **VALIDACIÓN Y CONTROL DE CALIDAD**

### **Script de Validación CI/CD**
```bash
#!/bin/bash
# validate-error-codes.sh

echo "Validating error code uniqueness..."

# Extract all error codes from codebase
grep -r "ERROR_CODE\|error_code" src/ | grep -o '[A-Z_]*_[0-9]*' | sort | uniq -c | sort -nr

# Check for duplicates
duplicates=$(grep -r "ERROR_CODE\|error_code" src/ | grep -o '[A-Z_]*_[0-9]*' | sort | uniq -d)

if [ ! -z "$duplicates" ]; then
    echo "❌ Duplicate error codes found:"
    echo "$duplicates"
    exit 1
fi

echo "✅ All error codes are unique"
```

### **Documentación Automática**
```python
# generate-error-docs.py
import json
import re

def generate_error_documentation():
    """Generate markdown documentation from error registry"""
    
    with open('error_registry.json', 'r') as f:
        registry = json.load(f)
    
    markdown = "# Error Codes Reference\\n\\n"
    
    for code, details in registry['error_codes'].items():
        markdown += f"## {code}\\n"
        markdown += f"**Description:** {details['description']}\\n"
        markdown += f"**Severity:** {details['severity']}\\n"
        markdown += f"**Resolution:** {details['resolution']}\\n\\n"
    
    with open('docs/error-codes.md', 'w') as f:
        f.write(markdown)
```

---

## 📊 **MÉTRICAS Y MONITOREO**

### **KPIs de Códigos de Error**
- **Coverage:** % de errores con códigos únicos
- **Documentation Rate:** % de códigos documentados
- **Resolution Time:** Tiempo promedio por tipo de error
- **Recurrence Rate:** Frecuencia de errores específicos

### **Dashboard de Error Codes**
```sql
-- Top error codes by frequency
SELECT 
    error_code,
    COUNT(*) as occurrences,
    AVG(resolution_time) as avg_resolution_time
FROM error_logs 
WHERE timestamp >= NOW() - INTERVAL 24 HOUR
GROUP BY error_code
ORDER BY occurrences DESC
LIMIT 10;
```

---

## 🚀 **PRÓXIMOS PASOS**

### **Implementación Gradual**
1. **Semana 1:** Definir convención y crear registro inicial
2. **Semana 2:** Implementar validación en CI/CD
3. **Semana 3:** Migrar errores existentes a nuevos códigos
4. **Semana 4:** Configurar monitoreo y alertas

### **Mejora Continua**
- Review mensual de códigos más frecuentes
- Actualización de documentación automática
- Análisis de tendencias y patrones
- Optimización de resoluciones

---

*Consultar playbook original: `playbooks/{filename}`*
'''
