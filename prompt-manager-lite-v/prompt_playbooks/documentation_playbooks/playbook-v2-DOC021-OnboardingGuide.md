# Playbook v2: DOC021 - Guía de Incorporación

**Objetivo:** Ensamblar una guía de incorporación completa y actualizada, asegurando que los nuevos miembros tengan acceso a la información de contacto correcta.

**Agente Asignado:** Onboarding Buddy Agent

**Principio Fundamental:** Una buena incorporación es un acelerador de productividad. Tu rol es asegurar que la guía sea un documento vivo y preciso.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el objeto `projectManagement.keyContacts` del `master_blueprint.json`.

---

## Fase 2: Generación del Documento

La plantilla `DOC021-OnboardingGuide.md` es mayormente estática. Tu única tarea de poblado dinámico es la sección de **Contactos Clave**.

1.  **Leer Plantilla:** Carga el contenido de `DOC021-OnboardingGuide.md`.
2.  **Poblar Contactos:**
    -   Reemplaza el placeholder `[projectManagement.keyContacts.projectLead]` con el valor correspondiente del objeto extraído.
    -   Reemplaza el placeholder `[projectManagement.keyContacts.techLead]`.
    -   Reemplaza el placeholder `[projectManagement.keyContacts.productOwner]`.

---

## Fase 3: Ensamblaje Final

1.  **Validar:** Asegúrate de que el documento final contenga los nombres de los contactos correctamente insertados.
2.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC021-OnboardingGuide.md`.