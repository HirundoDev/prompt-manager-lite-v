# DOC036 - Unique Error Codes Framework

**Versión:** 1.0  
**Fecha:** 2025-08-25  
**Categoría:** Playbook Universal  
**Aplicabilidad:** Independiente de tecnología  

---

## 🎯 **PROPÓSITO**

Marco universal para implementar códigos únicos de error en programación, asegurando que cada función, componente y módulo tenga identificadores únicos para facilitar debugging, soporte técnico y mantenimiento del código.

---

## 📋 **METODOLOGÍA CORE**

### **PRINCIPIOS FUNDAMENTALES**

#### **1. Unicidad Global**
- **Cada error debe tener un código único** en todo el proyecto
- **No reutilizar códigos** aunque el error parezca similar
- **Mantener registro centralizado** de códigos asignados
- **Evitar colisiones** entre módulos y equipos

#### **2. Consistencia de Formato**
- **Longitud fija:** Todos los códigos deben tener la misma longitud
- **Prefijos claros:** Identificar módulo/componente de origen
- **Sin ceros iniciales:** Evitar confusión con sistemas octales
- **Formato legible:** Fácil de comunicar y buscar

#### **3. Trazabilidad**
- **Código → Ubicación:** Búsqueda directa en código fuente
- **Código → Documentación:** Enlace directo a solución
- **Código → Contexto:** Información del módulo/función

---

## 🏗 **ARQUITECTURA DE CÓDIGOS**

### **Estructura Recomendada**
```
[PREFIX]-[MODULE]-[SEQUENCE]
```

#### **Ejemplos por Tecnología:**
```markdown
**JavaScript/Node.js:**
- ERR-AUTH-1001: Error de autenticación en login
- ERR-DB-1002: Conexión a base de datos fallida
- ERR-API-1003: Validación de parámetros API

**Python:**
- PY-USER-2001: Usuario no encontrado
- PY-FILE-2002: Archivo no accesible
- PY-CALC-2003: División por cero

**Java:**
- JV-SVC-3001: Servicio no disponible
- JV-CFG-3002: Configuración inválida
- JV-NET-3003: Timeout de red

**C#/.NET:**
- CS-DAL-4001: Error de acceso a datos
- CS-BIZ-4002: Regla de negocio violada
- CS-UI-4003: Validación de interfaz

**Go:**
- GO-HTTP-5001: Error en handler HTTP
- GO-JSON-5002: Parsing JSON fallido
- GO-CONN-5003: Pool de conexiones agotado
```

### **Rangos por Módulo**
```markdown
**AUTENTICACIÓN:** 1000-1999
- 1001-1099: Login/Logout
- 1100-1199: Tokens/JWT
- 1200-1299: Permisos/Roles
- 1300-1399: OAuth/SSO

**BASE DE DATOS:** 2000-2999
- 2001-2099: Conexiones
- 2100-2199: Queries/Transacciones
- 2200-2299: Migraciones
- 2300-2399: Backup/Restore

**API/WEB:** 3000-3999
- 3001-3099: Routing
- 3100-3199: Validación
- 3200-3299: Serialización
- 3300-3399: Rate Limiting

**BUSINESS LOGIC:** 4000-4999
- 4001-4099: Validaciones de negocio
- 4100-4199: Cálculos
- 4200-4299: Workflows
- 4300-4399: Reglas de dominio

**INFRAESTRUCTURA:** 5000-5999
- 5001-5099: Logging
- 5100-5199: Configuración
- 5200-5299: Monitoreo
- 5300-5399: Deployment
```

---

## 🔧 **IMPLEMENTACIÓN POR TECNOLOGÍA**

### **JavaScript/Node.js**
```javascript
// error-codes.js - Registro centralizado
const ERROR_CODES = {
  // Autenticación
  AUTH_INVALID_CREDENTIALS: 'ERR-AUTH-1001',
  AUTH_TOKEN_EXPIRED: 'ERR-AUTH-1002',
  AUTH_INSUFFICIENT_PERMISSIONS: 'ERR-AUTH-1003',
  
  // Base de datos
  DB_CONNECTION_FAILED: 'ERR-DB-2001',
  DB_QUERY_TIMEOUT: 'ERR-DB-2002',
  DB_CONSTRAINT_VIOLATION: 'ERR-DB-2003',
  
  // API
  API_INVALID_PAYLOAD: 'ERR-API-3001',
  API_RATE_LIMIT_EXCEEDED: 'ERR-API-3002',
  API_ENDPOINT_NOT_FOUND: 'ERR-API-3003'
};

// Clase de error personalizada
class AppError extends Error {
  constructor(code, message, details = {}) {
    super(message);
    this.code = code;
    this.details = details;
    this.timestamp = new Date().toISOString();
    this.name = 'AppError';
  }
}

// Uso en funciones
async function authenticateUser(credentials) {
  try {
    const user = await User.findByCredentials(credentials);
    if (!user) {
      throw new AppError(
        ERROR_CODES.AUTH_INVALID_CREDENTIALS,
        'Invalid username or password',
        { username: credentials.username }
      );
    }
    return user;
  } catch (error) {
    if (error instanceof AppError) throw error;
    
    throw new AppError(
      ERROR_CODES.DB_CONNECTION_FAILED,
      'Database connection error during authentication',
      { originalError: error.message }
    );
  }
}

// Middleware de manejo de errores
app.use((error, req, res, next) => {
  if (error instanceof AppError) {
    res.status(400).json({
      error_code: error.code,
      message: error.message,
      timestamp: error.timestamp,
      request_id: req.id,
      details: error.details
    });
  } else {
    // Error no manejado
    const unknownErrorCode = 'ERR-SYS-9999';
    logger.error(`${unknownErrorCode}: Unhandled error`, error);
    res.status(500).json({
      error_code: unknownErrorCode,
      message: 'Internal server error'
    });
  }
});
```

### **Python**
```python
# error_codes.py - Registro centralizado
class ErrorCodes:
    # Autenticación
    AUTH_INVALID_CREDENTIALS = "PY-AUTH-1001"
    AUTH_TOKEN_EXPIRED = "PY-AUTH-1002"
    AUTH_INSUFFICIENT_PERMISSIONS = "PY-AUTH-1003"
    
    # Base de datos
    DB_CONNECTION_FAILED = "PY-DB-2001"
    DB_QUERY_TIMEOUT = "PY-DB-2002"
    DB_CONSTRAINT_VIOLATION = "PY-DB-2003"
    
    # API
    API_INVALID_PAYLOAD = "PY-API-3001"
    API_RATE_LIMIT_EXCEEDED = "PY-API-3002"
    API_ENDPOINT_NOT_FOUND = "PY-API-3003"

# Excepción personalizada
class AppError(Exception):
    def __init__(self, code, message, details=None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}
        self.timestamp = datetime.utcnow().isoformat()

# Decorador para manejo automático de errores
def handle_errors(default_error_code):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AppError:
                raise  # Re-raise AppError as is
            except Exception as e:
                raise AppError(
                    default_error_code,
                    f"Unexpected error in {func.__name__}",
                    {"original_error": str(e)}
                )
        return wrapper
    return decorator

# Uso en funciones
@handle_errors(ErrorCodes.DB_CONNECTION_FAILED)
def authenticate_user(credentials):
    try:
        user = User.find_by_credentials(credentials)
        if not user:
            raise AppError(
                ErrorCodes.AUTH_INVALID_CREDENTIALS,
                "Invalid username or password",
                {"username": credentials.get("username")}
            )
        return user
    except DatabaseError as e:
        raise AppError(
            ErrorCodes.DB_CONNECTION_FAILED,
            "Database error during authentication",
            {"db_error": str(e)}
        )

# Middleware Flask
@app.errorhandler(AppError)
def handle_app_error(error):
    return jsonify({
        "error_code": error.code,
        "message": error.message,
        "timestamp": error.timestamp,
        "details": error.details
    }), 400
```

### **Java**
```java
// ErrorCodes.java - Registro centralizado
public final class ErrorCodes {
    // Autenticación
    public static final String AUTH_INVALID_CREDENTIALS = "JV-AUTH-1001";
    public static final String AUTH_TOKEN_EXPIRED = "JV-AUTH-1002";
    public static final String AUTH_INSUFFICIENT_PERMISSIONS = "JV-AUTH-1003";
    
    // Base de datos
    public static final String DB_CONNECTION_FAILED = "JV-DB-2001";
    public static final String DB_QUERY_TIMEOUT = "JV-DB-2002";
    public static final String DB_CONSTRAINT_VIOLATION = "JV-DB-2003";
    
    // API
    public static final String API_INVALID_PAYLOAD = "JV-API-3001";
    public static final String API_RATE_LIMIT_EXCEEDED = "JV-API-3002";
    public static final String API_ENDPOINT_NOT_FOUND = "JV-API-3003";
    
    private ErrorCodes() {} // Prevent instantiation
}

// Excepción personalizada
public class AppException extends Exception {
    private final String errorCode;
    private final Map<String, Object> details;
    private final Instant timestamp;
    
    public AppException(String errorCode, String message) {
        this(errorCode, message, Collections.emptyMap());
    }
    
    public AppException(String errorCode, String message, Map<String, Object> details) {
        super(message);
        this.errorCode = errorCode;
        this.details = new HashMap<>(details);
        this.timestamp = Instant.now();
    }
    
    // Getters
    public String getErrorCode() { return errorCode; }
    public Map<String, Object> getDetails() { return new HashMap<>(details); }
    public Instant getTimestamp() { return timestamp; }
}

// Uso en servicios
@Service
public class AuthenticationService {
    
    public User authenticateUser(Credentials credentials) throws AppException {
        try {
            User user = userRepository.findByCredentials(credentials);
            if (user == null) {
                Map<String, Object> details = Map.of("username", credentials.getUsername());
                throw new AppException(
                    ErrorCodes.AUTH_INVALID_CREDENTIALS,
                    "Invalid username or password",
                    details
                );
            }
            return user;
        } catch (DataAccessException e) {
            Map<String, Object> details = Map.of("dbError", e.getMessage());
            throw new AppException(
                ErrorCodes.DB_CONNECTION_FAILED,
                "Database error during authentication",
                details
            );
        }
    }
}

// Controller advice para manejo global
@ControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(AppException.class)
    public ResponseEntity<ErrorResponse> handleAppException(AppException e) {
        ErrorResponse response = ErrorResponse.builder()
            .errorCode(e.getErrorCode())
            .message(e.getMessage())
            .timestamp(e.getTimestamp())
            .details(e.getDetails())
            .build();
            
        return ResponseEntity.badRequest().body(response);
    }
}
```

### **Go**
```go
// error_codes.go - Registro centralizado
package errors

const (
    // Autenticación
    AuthInvalidCredentials     = "GO-AUTH-1001"
    AuthTokenExpired          = "GO-AUTH-1002"
    AuthInsufficientPerms     = "GO-AUTH-1003"
    
    // Base de datos
    DBConnectionFailed        = "GO-DB-2001"
    DBQueryTimeout           = "GO-DB-2002"
    DBConstraintViolation    = "GO-DB-2003"
    
    // API
    APIInvalidPayload        = "GO-API-3001"
    APIRateLimitExceeded     = "GO-API-3002"
    APIEndpointNotFound      = "GO-API-3003"
)

// AppError estructura personalizada
type AppError struct {
    Code      string                 `json:"error_code"`
    Message   string                 `json:"message"`
    Details   map[string]interface{} `json:"details,omitempty"`
    Timestamp time.Time              `json:"timestamp"`
}

func (e *AppError) Error() string {
    return fmt.Sprintf("%s: %s", e.Code, e.Message)
}

// Constructor de errores
func NewAppError(code, message string, details map[string]interface{}) *AppError {
    return &AppError{
        Code:      code,
        Message:   message,
        Details:   details,
        Timestamp: time.Now(),
    }
}

// Uso en funciones
func AuthenticateUser(credentials Credentials) (*User, error) {
    user, err := userRepo.FindByCredentials(credentials)
    if err != nil {
        return nil, NewAppError(
            DBConnectionFailed,
            "Database error during authentication",
            map[string]interface{}{"db_error": err.Error()},
        )
    }
    
    if user == nil {
        return nil, NewAppError(
            AuthInvalidCredentials,
            "Invalid username or password",
            map[string]interface{}{"username": credentials.Username},
        )
    }
    
    return user, nil
}

// Middleware HTTP
func ErrorMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        defer func() {
            if err := recover(); err != nil {
                var appErr *AppError
                if e, ok := err.(*AppError); ok {
                    appErr = e
                } else {
                    appErr = NewAppError(
                        "GO-SYS-9999",
                        "Internal server error",
                        map[string]interface{}{"panic": fmt.Sprintf("%v", err)},
                    )
                }
                
                w.Header().Set("Content-Type", "application/json")
                w.WriteHeader(http.StatusBadRequest)
                json.NewEncoder(w).Encode(appErr)
            }
        }()
        
        next.ServeHTTP(w, r)
    })
}
```

---

## 📊 **GESTIÓN DE CÓDIGOS**

### **Registro Centralizado**
```markdown
**SPREADSHEET/WIKI STRUCTURE:**
| Código | Módulo | Función/Clase | Descripción | Solución | Responsable | Fecha |
|--------|--------|---------------|-------------|----------|-------------|-------|
| ERR-AUTH-1001 | Auth | login() | Credenciales inválidas | Verificar usuario/pass | @dev1 | 2025-08-25 |
| ERR-DB-2001 | Database | connect() | Conexión fallida | Revisar config DB | @dev2 | 2025-08-25 |
| ERR-API-3001 | API | validate() | Payload inválido | Validar schema JSON | @dev3 | 2025-08-25 |
```

### **Herramientas de Gestión**
```bash
# Script para verificar códigos únicos
#!/bin/bash
echo "Verificando códigos únicos en el proyecto..."

# Buscar todos los códigos de error
grep -r "ERR-[A-Z]+-[0-9]+" src/ | \
  sed 's/.*\(ERR-[A-Z]\+-[0-9]\+\).*/\1/' | \
  sort | uniq -d

if [ $? -eq 0 ]; then
    echo "✅ Todos los códigos son únicos"
else
    echo "❌ Códigos duplicados encontrados"
    exit 1
fi
```

### **Validación en CI/CD**
```yaml
# .github/workflows/error-codes.yml
name: Validate Error Codes
on: [push, pull_request]

jobs:
  validate-codes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check unique error codes
        run: |
          # Extraer todos los códigos
          codes=$(grep -r "ERR-[A-Z]+-[0-9]+" src/ | \
                  sed 's/.*\(ERR-[A-Z]\+-[0-9]\+\).*/\1/' | sort)
          
          # Verificar unicidad
          duplicates=$(echo "$codes" | uniq -d)
          
          if [ -n "$duplicates" ]; then
            echo "❌ Códigos duplicados:"
            echo "$duplicates"
            exit 1
          fi
          
          echo "✅ Todos los códigos son únicos"
```

---

## 🔗 **INTEGRACIÓN CON DOC035**

### **Flujo Combinado**
```markdown
1. **Detectar Error** (DOC035) → Capturar con herramientas de monitoreo
2. **Identificar Código** (DOC036) → Buscar código único en logs
3. **Localizar Origen** (DOC036) → Buscar en código fuente
4. **Documentar Solución** (DOC035) → Actualizar knowledge base
5. **Prevenir Recurrencia** (DOC035) → Mejorar validaciones
```

### **Template Integrado para template-pendingtask.md**
```markdown
## 🚨 **TRACKING DE ERRORES Y CÓDIGOS**

### **Nuevos Códigos Asignados:**
- [ ] **[ERR-MOD-XXXX]** [Función/Método] - [Descripción breve]
- [ ] **[ERR-MOD-XXXY]** [Función/Método] - [Descripción breve]

### **Errores Encontrados:**
- [ ] **[ERR-AUTH-1001]** Login fallido - ALTO - Investigando
- [ ] **[ERR-DB-2001]** Conexión timeout - MEDIO - Solucionado

### **Validaciones Implementadas:**
- [x] Verificar unicidad de códigos nuevos
- [x] Actualizar registro centralizado
- [x] Agregar tests para casos de error
- [x] Documentar soluciones en wiki

### **Code Review Checklist:**
- [ ] ¿Cada throw/raise tiene código único?
- [ ] ¿Códigos siguen formato establecido?
- [ ] ¿Se actualizó registro centralizado?
- [ ] ¿Hay tests para nuevos códigos?
```

---

## 📚 **MEJORES PRÁCTICAS**

### **DO's**
- ✅ **Asignar código único** a cada punto de error
- ✅ **Usar formato consistente** en todo el proyecto
- ✅ **Mantener registro centralizado** actualizado
- ✅ **Incluir contexto útil** en detalles del error
- ✅ **Documentar soluciones** para cada código
- ✅ **Automatizar validación** de unicidad
- ✅ **Usar prefijos descriptivos** por módulo

### **DON'Ts**
- ❌ **Reutilizar códigos** aunque parezcan similares
- ❌ **Usar códigos genéricos** como "ERROR-001"
- ❌ **Hardcodear códigos** sin registro central
- ❌ **Cambiar códigos existentes** en producción
- ❌ **Usar formatos inconsistentes** entre módulos
- ❌ **Omitir contexto** en mensajes de error
- ❌ **Ignorar validación** en CI/CD

---

## 🎯 **CASOS DE USO ESPECÍFICOS**

### **Microservicios**
```markdown
**PREFIJOS POR SERVICIO:**
- USER-SVC-1XXX: Servicio de usuarios
- ORDER-SVC-2XXX: Servicio de órdenes
- PAY-SVC-3XXX: Servicio de pagos
- NOTIF-SVC-4XXX: Servicio de notificaciones

**COMUNICACIÓN ENTRE SERVICIOS:**
- Propagar códigos de error originales
- Agregar contexto del servicio actual
- Mantener trazabilidad completa
```

### **APIs REST**
```json
{
  "error_code": "API-VAL-3001",
  "message": "Invalid request payload",
  "timestamp": "2025-08-25T18:08:29Z",
  "request_id": "req-123456",
  "details": {
    "field": "email",
    "reason": "Invalid email format",
    "provided_value": "invalid-email"
  },
  "documentation_url": "https://docs.api.com/errors/API-VAL-3001"
}
```

### **Frontend/UI**
```javascript
// Mapeo de códigos a mensajes user-friendly
const ERROR_MESSAGES = {
  'ERR-AUTH-1001': 'Usuario o contraseña incorrectos',
  'ERR-AUTH-1002': 'Tu sesión ha expirado, por favor inicia sesión nuevamente',
  'ERR-API-3001': 'Los datos enviados no son válidos',
  'ERR-NET-5001': 'Problema de conexión, intenta nuevamente'
};

function handleError(errorCode, technicalMessage) {
  const userMessage = ERROR_MESSAGES[errorCode] || 'Ha ocurrido un error inesperado';
  
  // Mostrar mensaje amigable al usuario
  showUserNotification(userMessage);
  
  // Log técnico para debugging
  console.error(`${errorCode}: ${technicalMessage}`);
  
  // Reportar a sistema de monitoreo
  errorTracker.report(errorCode, technicalMessage);
}
```

---

## 🔗 **RECURSOS ADICIONALES**

- **Error Code Registry Template:** Spreadsheet para gestión centralizada
- **CI/CD Validation Scripts:** Scripts para validar unicidad automáticamente
- **IDE Snippets:** Templates para generar errores con códigos únicos
- **Documentation Templates:** Formatos para documentar soluciones
- **Monitoring Integration:** Configuración para herramientas de monitoreo

---

**INTEGRACIÓN:** Este playbook se complementa perfectamente con DOC035-ErrorTracking.md para crear un sistema completo de gestión de errores.
