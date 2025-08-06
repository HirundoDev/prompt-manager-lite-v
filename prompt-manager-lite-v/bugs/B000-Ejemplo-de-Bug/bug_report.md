# Informe de Bug: [Título del Bug]

---

## 1. Metadatos

- **ID de Bug:** `B[ID]`
- **Título:** `[Título Corto y Descriptivo del Bug]`
- **Issue Relacionado:** `#[Número del Issue]`
- **Severidad:** `Crítica | Alta | Media | Baja`
- **Estado:** `Reportado | En Análisis | Solución Propuesta | En Progreso | Listo para Verificación | Cerrado`
- **Branch de Corrección:** `bugfix/[ID]-[short-name]`

## 2. Descripción del Problema

- **Comportamiento Observado:**
  - [¿Qué ocurrió exactamente? Incluir logs o capturas si es posible.]
- **Comportamiento Esperado:**
  - [¿Qué debería haber ocurrido?]

## 3. Pasos para Reproducir (100% Fiable)

1.  [Primer paso]
2.  [Segundo paso]
3.  [Tercer paso]

## 4. Análisis de Causa Raíz (RCA)

*Esta es la sección más importante. ¿Por qué ocurrió el bug en primer lugar?*

- **Análisis:** [Explicación técnica detallada de la causa fundamental del problema. No solo el síntoma, sino la causa.]
- **Lección Aprendida / Medida Preventiva:** [¿Qué podemos cambiar en nuestros procesos o pruebas para evitar que este tipo de bug vuelva a ocurrir?]

## 5. Manifiesto de la Solución

*Un registro de todos los cambios necesarios para solucionar el bug.*

| Ruta del Archivo                    | Estado     | Descripción del Cambio              |
| :---------------------------------- | :--------- | :---------------------------------- |
| `src/utils/calculation.js`          | Modificado | Añadida validación para evitar división por cero. |

## 6. Criterios de Verificación

- [ ] Los pasos de reproducción ya no provocan el bug.
- [ ] La funcionalidad X, que depende de este código, sigue funcionando como se esperaba.
- [ ] Se ha añadido una nueva prueba unitaria (`test_case_name`) que cubre este escenario.

## 7. Log de Implementación de la Solución

*Un diario de las acciones tomadas para corregir el bug.*

- **2025-07-20:** Se aplicó la validación en `src/utils/calculation.js` y se ejecutaron las pruebas locales.

## 8. Siguiente Acción Propuesta

- **[Descripción clara de la próxima tarea a realizar.]**