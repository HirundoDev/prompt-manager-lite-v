# Playbook v2 — DOC010: Deployment

Guía paso a paso para elaborar y mantener el manual de despliegue multi-entorno.

Relacionado con: `docs/DOC010-Deployment.md`

---

## 1) Propósito

Estandarizar cómo describir infraestructura, prerrequisitos, variables de entorno, pasos de despliegue, rollback y pipeline CI/CD.

---

## 2) Estructura obligatoria del documento

1. Visión General de Infraestructura
2. Prerrequisitos (CLIs, accesos)
3. Configuración de entorno (variables FE/BE en tablas)
4. Proceso de despliegue (Backend, Frontend) con bloques de comando
5. Procedimiento de Rollback
6. Pipeline CI/CD (herramienta, triggers, etapas)

Mantener encabezados y tablas como en `DOC010-Deployment.md`.

---

## 3) Fuente de datos

- `schemas/master_blueprint_parts/operationalManual.json` (o sección `operationalManual` en el combinado).
- ADRs relevantes de infraestructura.

---

## 4) Pasos para completar/actualizar

1. Rellenar proveedores (frontend/backend/db) y entornos soportados.
2. Enumerar CLIs y accesos requeridos.
3. Construir tablas de variables de entorno (FE y BE) iterando desde el blueprint.
4. Escribir pasos de despliegue: build, push, migrate, deploy (BE) y build, deploy (FE) con comandos exactos.
5. Documentar rollback por componente y evidencias.
6. Resumir pipeline CI/CD: herramienta, triggers, etapas.

---

## 5) Checklist de validación

- [ ] Variables de entorno completas y con ejemplo.
- [ ] Pasos de despliegue reproducibles sin ambigüedad.
- [ ] Rollback descrito y testeado.
- [ ] CI/CD resumido con triggers claros.
- [ ] Sin placeholders pendientes.

---

## 6) Buenas prácticas

- Comandos listos para copiar/pegar.
- Incluir requisitos mínimos de versiones (Node, Docker, CLIs).
- Indicar tiempos aproximados y riesgos (deploy windows).

---

## 7) Errores comunes a evitar

- Variables incompletas o sin alcance de entorno.
- Omitir pasos de migración de base de datos.
- Falta de procedimiento de rollback.

---

## 8) Referencias

- Documento: `docs/DOC010-Deployment.md`
- Blueprint: `schemas/master_blueprint_parts/operationalManual.json`
- Guía general: `GUIA_COMPLETA_DE_USO.md`

