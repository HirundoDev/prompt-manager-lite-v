# Playbook v2: DOC022 - Proceso de Lanzamiento

**Objetivo:** Generar una checklist operativa y precisa para el proceso de lanzamiento, poblada con los comandos y estrategias específicas del proyecto.

**Agente Asignado:** Release Manager Agent

**Principio Fundamental:** Un proceso de lanzamiento documentado reduce el riesgo y aumenta la previsibilidad. Tu rol es asegurar que la documentación sea un espejo fiel de la práctica operativa.

---

## Fase 1: Extracción de Datos del Blueprint

Tu misión de extracción de datos es doble:

1.  **Extraer Gestión de Lanzamiento:** Lee y obtén el objeto completo `releaseManagement` del `master_blueprint.json`.
2.  **Extraer Comandos de Prueba:** Lee y obtén el objeto `qualityAssurance.testExecution` del `master_blueprint.json`.

---

## Fase 2: Generación del Documento

Utilizarás la plantilla `DOC022-ReleaseProcess.md` como base. Tu tarea es poblar los siguientes campos dinámicos:

-   **Estrategia de Versionado:** Reemplaza `[releaseManagement.versioningStrategy]` con el valor correspondiente.
-   **Comando de Pruebas:** Reemplaza `[qualityAssurance.testExecution.fullSuiteCommand]` con el comando para ejecutar la suite de pruebas completa.
-   **Comando de Publicación:** Reemplaza `[releaseManagement.publishCommand]` con el comando para publicar los paquetes.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Construye el documento completo combinando la plantilla con los datos poblados.
2.  **Validar:** Asegúrate de que todos los placeholders dinámicos han sido reemplazados con los datos correctos del blueprint.
3.  **Escribir Archivo:** Escribe el contenido final y actualizado en `DOC022-ReleaseProcess.md`.