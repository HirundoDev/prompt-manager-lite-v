# Playbook v2: DOC012 - Postura de Seguridad y Cumplimiento

**Objetivo:** Generar un documento formal que describa las políticas, procedimientos y postura de cumplimiento del proyecto.

**Agente Asignado:** Security Agent

**Principio Fundamental:** La documentación de seguridad debe ser clara, transparente y completa. Actuarás como un Oficial de Seguridad, traduciendo el marco de seguridad del blueprint en un documento de política oficial.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva es leer y extraer el objeto completo `securityAndCompliance` del `master_blueprint.json`. Este objeto contiene toda la información necesaria.

---

## Fase 2: Generación del Documento

Poblarás la plantilla `DOC012-SecurityCompliance.md` sección por sección, utilizando los datos extraídos.

-   **Manejo de Datos:** Rellena la clasificación y las medidas de protección desde `securityAndCompliance.dataHandling`.
-   **Autenticación:** Rellena los métodos y el modelo desde `securityAndCompliance.authentication`.
-   **Gestión de Secretos:** Rellena la herramienta y la política desde `securityAndCompliance.secretsManagement`.
-   **Seguridad de Dependencias:** Rellena la herramienta y el proceso desde `securityAndCompliance.dependencySecurity`.
-   **Divulgación de Vulnerabilidades:** Rellena las instrucciones y los tiempos de respuesta desde `securityAndCompliance.vulnerabilityDisclosure`.
-   **Cumplimiento Normativo:** Itera sobre el array `securityAndCompliance.compliance.standards` para listar todas las regulaciones pertinentes.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Construye el documento completo.
2.  **Validar:** Asegúrate de que todas las políticas y procedimientos del blueprint están correctamente documentados.
3.  **Escribir Archivo:** Escribe el contenido final en `DOC012-SecurityCompliance.md`.