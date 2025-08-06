# Playbook v2: DOC013 - Actualización del Changelog

**Objetivo:** Mantener un registro histórico preciso de los cambios del proyecto, actualizando el archivo `CHANGELOG.md` de forma segura y sin pérdida de datos.

**Agente Asignado:** Release Manager Agent

**Principio Fundamental:** EL HISTORIAL ES SAGRADO. Tu función principal es añadir nuevas entradas a la sección `[Unreleased]`, no regenerar el archivo. La sobreescritura está estrictamente prohibida.

---

## Modo de Operación: Actualización (Default)

Esta es tu tarea estándar en cada ejecución.

### Fase 1: Extracción y Lectura

1.  **Leer Changelog Existente:** Lee el contenido completo del archivo `prompt_docs/DOC013-ChangeLog.md` en memoria.
2.  **Extraer Nuevos Cambios:** Extrae la lista de cambios recientes del `master_blueprint.json`. La ubicación exacta de estos cambios puede variar (ej. `projectUpdates.recentChanges`).

### Fase 2: Inserción Quirúrgica

1.  **Identificar Punto de Inserción:** Localiza la sección `## [Unreleased]` y las subsecciones (`### Added`, `### Changed`, etc.) en el contenido del changelog en memoria.
2.  **Insertar Cambios:** Para cada nuevo cambio extraído del blueprint, añádelo como un nuevo ítem de lista (`- `) bajo la categoría correspondiente (ej. un `fix` va bajo `### Fixed`).
3.  **No Duplicar:** Antes de añadir una entrada, verifica que no exista ya una idéntica en la sección `[Unreleased]` para evitar duplicados.

### Fase 3: Escritura Segura

1.  **Sobrescribir con Contenido Actualizado:** Escribe el contenido modificado (el original + las nuevas líneas) de vuelta al archivo `DOC013-ChangeLog.md`, reemplazando el contenido antiguo.

---

## Modo de Operación: Publicación de Versión (Avanzado)

Este es un procedimiento especial que solo se ejecuta cuando se crea una nueva versión.

1.  **Leer Changelog:** Lee el contenido completo del archivo.
2.  **Copiar Cambios:** Copia todo el contenido de las categorías bajo la sección `## [Unreleased]`.
3.  **Crear Nueva Versión:** Inserta un nuevo encabezado de versión `## [Número de Versión] - YYYY-MM-DD` debajo de la sección `[Unreleased]`.
4.  **Pegar Cambios:** Pega los cambios copiados bajo el nuevo encabezado de versión.
5.  **Limpiar `[Unreleased]`:** Elimina todas las entradas de la sección `[Unreleased]`, dejándola lista para el próximo ciclo de desarrollo.