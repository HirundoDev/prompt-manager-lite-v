# Plantilla Maestra: Panel de Control de Dependencias del Frontend

> **Propósito:** Servir como un panel de control vivo para la salud de las dependencias del frontend, monitorizando la seguridad, licencias y el impacto en el rendimiento.
> **Playbook de Referencia:** `playbook-v2-DOC005-FrontendDependencies.md`

<!-- 
  INSTRUCCIONES PARA LA IA (Frontend Health Agent):
  - Tu misión es ejecutar una serie de auditorías y poblar esta plantilla para generar un informe de estado.
  - Este documento debe ser la única fuente de verdad sobre la salud de la cadena de suministro de software del frontend.
-->

# Panel de Control de Dependencias del Frontend

| Gestor de Paquetes | Archivo Manifiesto | Estado General | Última Auditoría |
| --- | --- | --- | --- |
| `[npm/yarn]` | `[package.json]` | `[✅ Saludable / ⚠️ Requiere Revisión]` | `[Fecha y Hora]` |

---

## 1. Dependencias de Producción (`dependencies`)

Estas son las dependencias que se incluyen en el bundle final para el cliente.

| Paquete | Versión | Licencia | Propósito | Impacto en Bundle (gzipped) | Estado de Seguridad |
| --- | --- | --- | --- | --- | --- |
| [Iterar sobre `dependencies` del `package.json` y los resultados de las auditorías] | | | | | |

## 2. Dependencias de Desarrollo (`devDependencies`)

Estas dependencias solo son necesarias para el desarrollo local y no afectan el bundle de producción.

| Paquete | Versión | Licencia | Propósito | Estado de Seguridad |
| --- | --- | --- | --- | --- |
| [Iterar sobre `devDependencies` del `package.json` y los resultados de las auditorías] | | | | |

## 3. Resumen de la Auditoría de Seguridad

[Resumen de los resultados de `npm audit`. Listar vulnerabilidades críticas, altas, moderadas y bajas.]

## 4. Resumen de Licencias

[Resumen de las licencias encontradas. Advertir sobre licencias restrictivas o incompatibles.]