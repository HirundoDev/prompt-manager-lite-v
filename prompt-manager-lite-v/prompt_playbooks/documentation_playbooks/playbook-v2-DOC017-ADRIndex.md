# Playbook v2 — DOC017: ADR Index

Guía para generar y mantener el índice de ADRs.

Relacionado con: `docs/DOC017-ADR-Index.md`

---

## 1) Propósito

Mantener una tabla única y actualizada de todos los ADRs del proyecto, con número, título, fecha y estado.

---

## 2) Estructura obligatoria del documento

1. Título y propósito
2. Tabla con columnas: ADR | Título de la Decisión | Fecha | Estado
3. Filas generadas para cada archivo en `adrs/`

---

## 3) Fuente de datos

- Sistema de archivos: carpeta `adrs/` (fuente de verdad).
- Extraer de cada ADR: número, título, fecha, estado (primeros bloques del archivo).

---

## 4) Pasos para generar/actualizar

1. Escanear `adrs/` y ordenar por número.
2. Extraer metadatos del encabezado de cada ADR.
3. Reconstruir la tabla en `DOC017-ADR-Index.md`.
4. Verificar enlaces relativos a cada ADR.

---

## 5) Checklist de validación

- [ ] Todos los ADRs presentes en la tabla.
- [ ] Enlaces correctos a cada archivo.
- [ ] Estados y fechas consistentes.
- [ ] Orden por número creciente.

---

## 6) Buenas prácticas

- Automatizar actualización (script o tarea) cuando se añada/modifique un ADR.
- Mantener títulos concisos y descriptivos.

---

## 7) Errores comunes a evitar

- ADRs faltantes en la tabla.
- Enlaces rotos.
- Fechas con formato incorrecto.

---

## 8) Referencias

- Documento: `docs/DOC017-ADR-Index.md`
- Plantilla ADR: `docs/template-ADR.md`
- Guía general: `GUIA_COMPLETA_DE_USO.md`

