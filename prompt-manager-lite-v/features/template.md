# Especificación de Feature: [Título de la Feature]

---

## 1. Metadatos

- **ID de Feature:** `F[ID]`
- **Título:** `[Título Descriptivo]`
- **Issue Relacionado:** `#[Número del Issue]`
- **Estado:** `Propuesto | En Progreso | Listo para Integración | Completado | En Espera`
- **Branch:** `feature/[ID]-[short-name]`

## 2. Resumen Ejecutivo

*   **¿Qué estamos construyendo?**
    *   [Descripción clara y concisa de la funcionalidad desde la perspectiva del usuario.]
*   **¿Por qué es importante?**
    *   [El problema que resuelve o el valor que aporta al negocio/usuario.]

## 3. Análisis de Impacto Arquitectónico

*Esta sección es una checklist viva. Marca los documentos que serán modificados por esta feature.*

- [ ] `DOC008-APISpecification.md`
- [ ] `DOC009-DataModel.md`
- [ ] `DOC006-BackendArchitecture.md`
- [ ] `DOC004-FrontendArchitecture.md`
- [ ] `DOC028-OperationsRunbook.md`
- [ ] `DOC019-CLI-Command-Reference.md`
- [ ] Otros: `[Especificar]`

## 4. Especificaciones Técnicas (En Desarrollo)

*Esta sección se rellena durante el desarrollo.*

### 4.1. Nuevos Endpoints de API

| Verbo  | Ruta                  | Descripción de la Operación |
| :----- | :-------------------- | :-------------------------- |
| `POST` | `/api/v1/ejemplo`     | Crea un nuevo recurso.      |

### 4.2. Cambios en el Esquema de la Base de Datos

- **Nueva Tabla:** `nombre_tabla`
- **Modificación de Tabla:** `tabla_existente` (añadir columna `nueva_columna`)

### 4.3. Nuevas Dependencias o Librerías

- `[nombre-de-la-libreria]@[version]`

### 4.4. Nuevas Variables de Entorno

- `NUEVA_API_KEY`

### 4.5. Nuevos Comandos de CLI

| Comando        | Argumentos y Opciones       | Descripción de la Operación |
| :------------- | :-------------------------- | :-------------------------- |
| `mi-app sync`  | `--force`, `--verbose`      | Sincroniza los datos locales. |

### 4.6. Archivos Afectados

*Un registro de todos los archivos creados o modificados por esta feature.*

| Ruta del Archivo                    | Estado     | Descripción del Cambio              |
| :---------------------------------- | :--------- | :---------------------------------- |
| `src/controllers/user_controller.js` | Modificado | Añadida la función `getUserById`.   |
| `src/services/user_service.js`      | Creado     | Lógica de negocio para usuarios.    |

## 5. Criterios de Aceptación

*¿Cómo sabremos que hemos terminado y que funciona?*

- [ ] El usuario puede [acción del usuario].
- [ ] El endpoint `GET /api/v1/ejemplo` devuelve [respuesta esperada].
- [ ] Las pruebas de integración cubren el nuevo flujo.

## 6. Registro de Progreso y Decisiones

*Un log de decisiones importantes tomadas durante el desarrollo.*

- **2025-07-20:** Se decidió usar `libreria-x` en lugar de `libreria-y` por motivos de rendimiento.

---

## 7. Siguiente Acción Propuesta

*Esta sección es actualizada por el agente al final de una sesión de trabajo para facilitar la continuación.*

- **[Descripción clara de la próxima tarea a realizar.]**