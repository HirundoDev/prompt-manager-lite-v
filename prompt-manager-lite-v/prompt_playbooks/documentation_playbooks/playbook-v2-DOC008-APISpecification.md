# Playbook v2 — DOC008: API Specification

Guía para completar y mantener la especificación de la API con estilo OpenAPI-lite.

Relacionado con: `docs/DOC008-APISpecification.md`

---

## 1) Propósito

Definir el contrato de la API como única fuente de verdad para FE/BE. Este playbook asegura estructura, consistencia y verificabilidad, y permite reconstruir el formato si se rompe.

---

## 2) Estructura obligatoria del documento

Debe seguir exactamente estas secciones (como en `DOC008-APISpecification.md`):

1. Título y metadatos
   - URL Base
   - Versión
2. Autenticación
   - Estrategia (p.ej. JWT Bearer)
   - Flujo de obtención/uso de token
3. Manejo de Errores (formato de respuesta)
4. Límite de Tasa (Rate Limiting)
5. Endpoints (uno por sección)
   - Método + Ruta
   - Descripción
   - Parámetros de ruta (tabla)
   - requestBody (JSON de ejemplo o schema)
   - Respuesta 200 (JSON de ejemplo o schema)

Mantener encabezados, tablas y bloques de código `json`.

---

## 3) Fuente de datos

- Principal: `schemas/master_blueprint_parts/apiContract.json` (o `master_blueprint_combined.json` si ya existe).
- Complementos: decisiones en ADRs y notas en `DOC008*` previas.

---

## 4) Pasos para completar/actualizar

1. Obtener `URL Base`, `Versión`, info de `authentication`, `rateLimiting` desde `apiContract`.
2. Iterar `apiContract.endpoints` y crear una subsección por endpoint:
   - Título: `### [MÉTODO] [ruta]`
   - Descripción: desde `endpoint.description`.
   - Parámetros: tabla con `name`, `type`, `description` (si aplica).
   - requestBody: ejemplo desde `endpoint.requestSchema` (como JSON de muestra).
   - Response 200: ejemplo desde `endpoint.responseSchema`.
3. Añadir notas de headers de auth si el endpoint está protegido.
4. Verificar consistencia de tipos, nombres y ejemplos con el modelo de datos.

---

## 5) Checklist de validación

- [ ] URL Base y Versión completadas.
- [ ] Autenticación descrita con flujo y header `Authorization` si aplica.
- [ ] Manejo de errores con ejemplo JSON presente.
- [ ] Política de Rate Limiting documentada.
- [ ] Todos los endpoints del `apiContract` tienen sección, parámetros, request y response.
- [ ] Ejemplos JSON válidos y formateados.
- [ ] Sin placeholders `[ ... ]` pendientes.

---

## 6) Ejemplo de sección de endpoint (plantilla)

```markdown
### GET /users/{id}

> Obtiene detalle de usuario por ID

**Parámetros de Ruta:**

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | string | Identificador del usuario |

**Cuerpo de la Petición (requestBody):**

```json
{}
```

**Respuesta Exitosa (200 OK):**

```json
{
  "id": "u_123",
  "email": "jane@example.com"
}
```
```

---

## 7) Buenas prácticas

- Mantener naming consistente con el modelo de datos.
- Incluir ejemplos mínimos viables pero reales.
- Documentar códigos alternativos (201/204/4xx/5xx) si el contrato lo exige.
- Establecer paginación, filtros y sorting cuando aplique.

---

## 8) Errores comunes a evitar

- Dejar placeholders o ejemplos vacíos.
- Omitir headers de autenticación.
- Desalinear nombres/tipos respecto al `dataModel`.
- No actualizar el doc al cambiar el contrato.

---

## 9) Referencias

- Documento: `docs/DOC008-APISpecification.md`
- Modelo de datos: `docs/DOC009-DataModel.md`
- Contrato: `schemas/master_blueprint_parts/apiContract.json`
- Guía general: `GUIA_COMPLETA_DE_USO.md`

