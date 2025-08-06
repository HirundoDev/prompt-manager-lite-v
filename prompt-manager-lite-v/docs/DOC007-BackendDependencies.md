# Plantilla Maestra: Panel de Control de Dependencias del Backend

> **Propósito:** Servir como un panel de control vivo para la salud de las dependencias del backend, monitorizando la seguridad, licencias y posibles conflictos.
> **Playbook de Referencia:** `playbook-v2-DOC007-BackendDependencies.md`

<!-- 
  INSTRUCCIONES PARA LA IA (Backend Health Agent):
  - Tu misión es ejecutar una serie de auditorías (ej. `pip-audit`, `npm audit`, `snyk`) y poblar esta plantilla.
  - Este documento debe ser la única fuente de verdad sobre la salud de la cadena de suministro de software del backend.
-->

# Panel de Control de Dependencias del Backend

| Gestor de Paquetes | Archivo Manifiesto | Estado General | Última Auditoría |
| --- | --- | --- | --- |
| `[pip/npm/maven]` | `[requirements.txt/package.json/pom.xml]` | `[✅ Saludable / ⚠️ Requiere Revisión]` | `[Fecha y Hora]` |

---

## 1. Dependencias de Producción

Estas son las dependencias necesarias para que la aplicación se ejecute en producción.

| Paquete | Versión | Licencia | Propósito | Estado de Seguridad |
| --- | --- | --- | --- | --- |
| [Iterar sobre las dependencias del manifiesto y los resultados de las auditorías] | | | | |

## 2. Dependencias de Desarrollo y Pruebas

Estas dependencias solo son necesarias para el desarrollo local, pruebas y construcción.

| Paquete | Versión | Licencia | Propósito | Estado de Seguridad |
| --- | --- | --- | --- | --- |
| [Iterar sobre las dependencias de desarrollo del manifiesto y los resultados de las auditorías] | | | | |

## 3. Resumen de la Auditoría de Seguridad

[Resumen de los resultados de la herramienta de auditoría. Listar vulnerabilidades críticas, altas, moderadas y bajas.]

## 4. Resumen de Licencias

[Resumen de las licencias encontradas. Advertir sobre licencias restrictivas, incompatibles o no aprobadas por la política de la empresa.]