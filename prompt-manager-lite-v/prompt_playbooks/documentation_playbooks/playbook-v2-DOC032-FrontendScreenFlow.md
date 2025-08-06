# Playbook v2 — DOC032: Frontend Screen Flow

Guía para documentar el flujo de pantallas del frontend.

Relacionado con: `docs/DOC032-Frontend-Screen-Flow.md`

---

## 1) Propósito

Representar visual y textualmente las pantallas, estados y transiciones del FE para diseñar, desarrollar y probar con alineación.

---

## 2) Estructura obligatoria del documento

1. Diagrama de flujo (Mermaid `flowchart` o `stateDiagram`)
2. Lista de pantallas con descripción breve
3. Reglas de navegación (condiciones, guards)
4. Estados de carga y error por pantalla (si aplica)

---

## 3) Fuente de datos

- `schemas/master_blueprint_parts/uxFlows.json` (o sección ux en el combinado).
- Wireframes/mockups si existen.

---

## 4) Pasos para completar/actualizar

1. Identificar pantallas claves y rutas.
2. Crear diagrama Mermaid con nodos (pantallas) y aristas (transiciones con condiciones).
3. Documentar cada pantalla: propósito, acciones principales, estados de carga/error.
4. Alinear con rutas reales de FE y estados globales (auth, permisos).

---

## 5) Checklist de validación

- [ ] Diagrama renderiza sin errores.
- [ ] Todas las pantallas del flujo están listadas.
- [ ] Transiciones y condiciones claras.
- [ ] Estados de error/carga documentados cuando apliquen.

---

## 6) Buenas prácticas

- Mantener nombres de pantallas igual que en el router.
- Incluir estados vacíos (empty state) y edge cases.

---

## 7) Errores comunes a evitar

- Flujos que no contemplan auth/permisos.
- Diagramas desactualizados.

---

## 8) Referencias

- Documento: `docs/DOC032-Frontend-Screen-Flow.md`
- Blueprint UX: `schemas/master_blueprint_parts/uxFlows.json`
- Guía general: `GUIA_COMPLETA_DE_USO.md`

