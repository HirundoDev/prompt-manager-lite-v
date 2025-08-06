# Guía de Usuario: `update-content`

## DESCRIPCIÓN

El comando `update-content` se utiliza para modificar el contenido de un artefacto. Esto es útil para actualizar la documentación, cambiar el código de un script, o cualquier otra modificación del contenido del archivo asociado al artefacto. Además, el comando crea automáticamente un backup del contenido original antes de la modificación.

## ARGUMENTOS

- **`artefact_id`** (requerido): El ID único del artefacto cuyo contenido se desea actualizar.

## FLAGS (OPCIONALES)

- **`--content CONTENT`**: Proporciona el nuevo contenido directamente en la línea de comandos. Es útil para cambios pequeños o para scripts.
- **`--from-file FROM_FILE`**: Especifica la ruta a un archivo que contiene el nuevo contenido. Es la opción recomendada para cambios grandes o para mantener la formato del contenido.

## EJEMPLOS DE USO

### Ejemplo 1: Actualizar el contenido de un artefacto directamente

```bash
prompt-engine-cli update-content DOC001 --content "Este es el nuevo contenido del documento."
```

Este comando reemplaza el contenido del artefacto `DOC001` con el texto proporcionado.

### Ejemplo 2: Actualizar el contenido desde un archivo

```bash
prompt-engine-cli update-content FTR001 --from-file ./feature_specs/new_login.md
```

Este comando lee el contenido del archivo `new_login.md` y lo utiliza para reemplazar el contenido del artefacto `FTR001`.

### Ejemplo 3: Actualizar un script de utilidad

```bash
prompt-engine-cli update-content UTIL001 --from-file ./scripts/new_version.py
```

Este comando actualiza el script de utilidad `UTIL001` con el contenido de `new_version.py`.

