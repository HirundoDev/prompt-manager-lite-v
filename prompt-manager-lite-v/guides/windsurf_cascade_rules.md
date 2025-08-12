# Reglas locales para Windsurf/Cascade

Estas reglas se aplican por defecto en este repositorio cuando se usa el asistente en Windsurf/Cascade.

1) Fuente única de verdad (documentación)
- Siempre leer y seguir `guides/the_mighty_guide.md` antes de actuar.
- Respetar plantillas y playbooks al pie de la letra.

2) Verificación simple (sin banderas)
- Comando único: `python3 tools/verify_docs_and_schemas.py`.
- Tras ejecutarlo, abrir `verification_report.md` y usarlo como checklist visual.
- Presentar al usuario un resumen por DOC con ✔/✖ y enlace al reporte. Evitar listas grandes en consola.

3) Reglas de edición
- No crear DOCs fuera de `manifests/documentation_manifest.json`.
- No introducir schemas JSON fuera de `schemas/` ni sin referencia en `schemaRefs`/manifest.
- No modificar estructuras de plantillas/playbooks.
- Actualizar `docs_checklist-verificaction.md` cuando cambie un artefacto.
- Mantener índices: `DOC031` (bugs), `DOC030` (features), `DOC028` (operations).

4) Estilo de ayuda del asistente
- Priorizar orientación concreta (qué línea/archivo corregir) y ejemplos mínimos.
- Evitar proponer múltiples comandos o flags de entorno.
- Nunca realizar cambios automáticos en archivos sin que el usuario lo pida.

5) Orden de corrección recomendado
- Checklist → Playbook/estructura → Contenido real (sin placeholders, H1 con ID) → Índices → schemaRefs/manifest → referencias a scripts.

Estas reglas complementan y no reemplazan `guides/the_mighty_guide.md`.
