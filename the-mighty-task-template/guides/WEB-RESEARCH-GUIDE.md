# GUÍA DE INVESTIGACIÓN WEB - The Mighty Task v3.3

**Fecha:** 2025-08-26  
**Versión:** 3.3 (Modular Operations)  
**Propósito:** Guía completa para investigación web sistemática usando The Mighty Task con templates modulares

---

## 🎯 **FILOSOFÍA DE INVESTIGACIÓN**

La investigación web en The Mighty Task es **obligatoria, sistemática y reutilizable**. Cada tarea debe validar información actualizada antes de la implementación.

### **Principios Fundamentales:**
1. **Información actualizada** - Verificar versiones y mejores prácticas actuales
2. **Fuentes confiables** - Documentación oficial, repositorios activos, expertos reconocidos
3. **Reutilización inteligente** - Crear web-guides para futuras referencias
4. **Validación práctica** - Probar información antes de documentar

---

## 🔍 **METODOLOGÍA DE INVESTIGACIÓN**

### **PASO 1: IDENTIFICAR NECESIDAD DE INVESTIGACIÓN**

**Antes de cada tarea, preguntarse:**
- ¿Qué tecnología/framework/librería voy a usar?
- ¿Cuál es la versión más reciente estable?
- ¿Qué mejores prácticas han cambiado recientemente?
- ¿Existen alternativas mejores disponibles?

**Ejemplo:**
```markdown
Tarea: Configurar servidor Express básico
Investigación requerida:
- Versión actual de Express.js
- Middleware recomendados 2025
- Mejores prácticas de seguridad
- Patrones de configuración actuales
```

### **PASO 2: CREAR WEB-GUIDE INICIAL**

```bash
# Crear nuevo web-guide
python scripts/web-guide-manager.py --create "express-setup" --session "2025-08-25_BACKEND-API-SETUP"
```

**Template inicial:**
```markdown
# Express.js Setup Guide - 2025

**Fecha de investigación:** 2025-08-25  
**Investigador:** [Nombre del agente AI]  
**Propósito:** Configuración de servidor Express para proyecto BACKEND-API-SETUP  
**Estado:** 🔍 EN_INVESTIGACIÓN

## Preguntas de Investigación
- [ ] ¿Cuál es la versión estable actual de Express?
- [ ] ¿Qué middleware son recomendados en 2025?
- [ ] ¿Cuáles son las mejores prácticas de seguridad?
- [ ] ¿Hay breaking changes recientes?

## Fuentes a Consultar
- [ ] Documentación oficial Express.js
- [ ] GitHub releases
- [ ] Stack Overflow (últimos 6 meses)
- [ ] Artículos de desarrolladores reconocidos

## Hallazgos
[Se llenará durante la investigación]

## Validación Práctica
[Se llenará con pruebas realizadas]
```

### **PASO 3: INVESTIGAR FUENTES CONFIABLES**

#### **Fuentes Primarias (Obligatorias):**
1. **Documentación oficial** - Siempre la primera fuente
2. **GitHub del proyecto** - Releases, issues, roadmap
3. **NPM/PyPI/etc** - Información de paquetes y dependencias

#### **Fuentes Secundarias (Recomendadas):**
1. **Stack Overflow** - Solo preguntas/respuestas de últimos 6 meses
2. **Dev.to, Medium** - Artículos de desarrolladores reconocidos
3. **YouTube** - Tutoriales de canales técnicos establecidos
4. **Reddit** - Discusiones en subreddits técnicos relevantes

#### **Fuentes a Evitar:**
- ❌ Tutoriales sin fecha
- ❌ Blogs personales sin credenciales
- ❌ Información de más de 1 año (para tecnologías rápidas)
- ❌ Foros no moderados

### **PASO 4: DOCUMENTAR HALLAZGOS**

```markdown
## Hallazgos de Investigación

### Express.js - Versión Actual
- **Versión estable:** 4.19.2 (2025-01-15)
- **Fuente:** https://github.com/expressjs/express/releases
- **Cambios importantes:** Mejoras de seguridad, deprecación de body-parser interno

### Middleware Recomendados 2025
#### Seguridad
- **helmet** v7.1.0 - Headers de seguridad
- **cors** v2.8.5 - CORS policy
- **express-rate-limit** v7.1.5 - Rate limiting

#### Logging
- **morgan** v1.10.0 - HTTP request logger
- **winston** v3.11.0 - Logging estructurado (preferido sobre Pino)

#### Utilidades
- **compression** v1.7.4 - Compresión gzip
- **express-validator** v7.0.1 - Validación de input

### Mejores Prácticas 2025
1. **Configuración por variables de entorno**
2. **Manejo de errores centralizado**
3. **Logging estructurado con contexto**
4. **Headers de seguridad obligatorios**
5. **Validación de input en todas las rutas**

### Breaking Changes Recientes
- Express 4.19: body-parser ya no incluido por defecto
- Helmet 7.x: Configuración de CSP más estricta
- Winston 3.11: Cambios en formato de transports
```

### **PASO 5: VALIDACIÓN PRÁCTICA**

```markdown
## Validación Práctica

### Prueba 1: Instalación y Configuración Básica
```bash
npm init -y
npm install express@^4.19.2 helmet@^7.1.0 cors@^2.8.5 morgan@^1.10.0
```
**Resultado:** ✅ Instalación exitosa, sin conflictos de dependencias

### Prueba 2: Servidor Básico
```javascript
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const morgan = require('morgan');

const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(morgan('combined'));
app.use(express.json());

// Ruta de prueba
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
**Resultado:** ✅ Servidor funciona correctamente

### Prueba 3: Validación de Seguridad
```bash
curl -I localhost:3000/health
```
**Headers verificados:**
- ✅ X-Content-Type-Options: nosniff
- ✅ X-Frame-Options: DENY
- ✅ X-XSS-Protection: 0
- ✅ Strict-Transport-Security: max-age=15552000
```

### **PASO 6: FINALIZAR WEB-GUIDE**

```markdown
# Express.js Setup Guide - 2025 ✅

**Fecha de investigación:** 2025-08-25  
**Investigador:** claude-3.5-sonnet  
**Estado:** ✅ VALIDADO_Y_PROBADO  
**Última actualización:** 2025-08-25

## Configuración Recomendada 2025

### Instalación
```bash
npm install express@^4.19.2 helmet@^7.1.0 cors@^2.8.5 morgan@^1.10.0 winston@^3.11.0
```

### Configuración Básica Validada
[Código completo probado]

### Middleware Obligatorios
[Lista detallada con versiones]

### Mejores Prácticas Verificadas
[Prácticas probadas en entorno real]

## Troubleshooting Común
### Error: Cannot find module 'body-parser'
**Causa:** Express 4.19+ no incluye body-parser
**Solución:** Usar `express.json()` y `express.urlencoded()`

### Headers CORS no funcionan
**Causa:** Orden incorrecto de middleware
**Solución:** cors() debe ir antes que las rutas

## Referencias Consultadas
- [Express.js Official Docs](https://expressjs.com/) - Consultado 2025-08-25
- [Express GitHub Releases](https://github.com/expressjs/express/releases) - v4.19.2
- [Helmet.js Documentation](https://helmetjs.github.io/) - v7.1.0
- [Node.js Security Best Practices](https://nodejs.org/en/docs/guides/security/) - 2025

## Validación Completa
- [x] Código probado en entorno local
- [x] Dependencias verificadas sin conflictos
- [x] Headers de seguridad confirmados
- [x] Performance básica validada (<100ms respuesta)
```

---

## 🛠️ **COMANDOS DE WEB-GUIDE MANAGER**

### **Crear y Gestionar Web-Guides**
```bash
# Crear nuevo web-guide
python scripts/web-guide-manager.py --create "express-setup" --session "2025-08-25_BACKEND-API-SETUP"

# Buscar web-guides existentes
python scripts/web-guide-manager.py --search "express"

# Listar todos los web-guides
python scripts/web-guide-manager.py --list-guides

# Actualizar web-guide existente
python scripts/web-guide-manager.py --update "express-setup" --add-section "troubleshooting"
```

### **Reutilización y Consolidación**
```bash
# Copiar web-guide a nueva sesión
python scripts/web-guide-manager.py --copy-guide "express-setup" --to-session "2025-08-26_BACKEND-API-SETUP-2"

# Consolidar web-guides por tema
python scripts/web-guide-manager.py --consolidate "backend"

# Generar índice de web-guides
python scripts/web-guide-manager.py --generate-index
```

### **Validación y Mantenimiento**
```bash
# Validar actualización de web-guides
python scripts/web-guide-manager.py --validate-age --days 30

# Verificar enlaces rotos
python scripts/web-guide-manager.py --check-links

# Generar reporte de investigación
python scripts/web-guide-manager.py --research-report --session "2025-08-25_BACKEND-API-SETUP"
```

---

## 📊 **MÉTRICAS DE INVESTIGACIÓN**

### **Calidad de Web-Guide:**
- ✅ **Fuentes primarias:** ≥3 fuentes oficiales consultadas
- ✅ **Actualidad:** Información de últimos 6 meses
- ✅ **Validación práctica:** Código probado funcionando
- ✅ **Completitud:** Instalación + configuración + troubleshooting
- ✅ **Trazabilidad:** Enlaces a todas las fuentes

### **Eficiencia de Investigación:**
- **Tiempo de investigación:** 15-30 minutos por web-guide
- **Reutilización:** ≥50% de web-guides reutilizados en futuras sesiones
- **Actualización:** Web-guides actualizados cada 3 meses
- **Cobertura:** 100% de tareas con investigación previa

---

## 🔄 **REUTILIZACIÓN DE WEB-GUIDES**

### **Antes de Crear Nuevo Web-Guide:**
```bash
# Buscar guides existentes
python scripts/web-guide-manager.py --search "express nodejs backend"

# Verificar actualidad
python scripts/web-guide-manager.py --check-age "express-setup-guide.md"
```

### **Actualizar Web-Guide Existente:**
```markdown
## Actualización 2025-08-26
**Cambios:**
- Express actualizado a 4.19.3
- Helmet configuración CSP mejorada
- Nuevo middleware: express-slow-down

**Validación:**
- [x] Código actualizado probado
- [x] Nuevas dependencias verificadas
- [x] Performance mantenida
```

### **Consolidar Web-Guides Similares:**
```bash
# Consolidar guides relacionados
python scripts/web-guide-manager.py --merge-guides "express-setup,express-security,express-middleware" --output "express-complete-guide"
```

---

## ✅ **CHECKLIST DE INVESTIGACIÓN**

### **Antes de Implementar Tarea:**
- [ ] Identificar tecnologías/frameworks a usar
- [ ] Buscar web-guides existentes
- [ ] Crear/actualizar web-guide si necesario
- [ ] Validar información con fuentes primarias
- [ ] Probar código en entorno local
- [ ] Documentar troubleshooting común

### **Durante la Investigación:**
- [ ] Consultar ≥3 fuentes confiables
- [ ] Verificar versiones actuales
- [ ] Identificar breaking changes
- [ ] Probar configuración básica
- [ ] Documentar problemas encontrados

### **Después de la Investigación:**
- [ ] Web-guide completo y validado
- [ ] Código probado funcionando
- [ ] Referencias documentadas
- [ ] Troubleshooting incluido
- [ ] Guide agregado al índice

---

## 🚨 **ERRORES COMUNES**

### **❌ Investigación Superficial:**
```markdown
# Express Setup
npm install express
app.listen(3000)
```

### **✅ Investigación Completa:**
```markdown
# Express.js Setup Guide - 2025 ✅

**Versión validada:** Express 4.19.2  
**Fuentes:** [3+ fuentes oficiales]  
**Código probado:** ✅ Funciona en local  
**Troubleshooting:** [Problemas comunes documentados]  
**Actualización:** [Fecha de última verificación]
```

### **❌ Sin Validación:**
```markdown
"Según un tutorial de 2022, usar body-parser..."
```

### **✅ Con Validación:**
```markdown
"Express 4.19+ incluye body-parser. Validado en documentación oficial (2025-08-25) y probado localmente."
```

---

**Estado:** ✅ Guía completa para investigación web sistemática  
**Uso:** Consultar antes de implementar cualquier tarea que requiera investigación
