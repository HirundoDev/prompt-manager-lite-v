# Playbook v2 — DOC033: ADR Template

Guía para completar y mantener los ADRs usando la plantilla oficial del proyecto.

Relacionado con: `docs/template-ADR.md`

---

## 1) Propósito del documento

Este playbook describe cómo usar correctamente la plantilla de ADR para registrar decisiones de arquitectura de forma consistente y auditables. Asegura estructura, nomenclatura y calidad, de forma que, si el formato se rompe, pueda reconstruirse fielmente.

---

## 2) Cuándo crear un ADR

- Cambios de arquitectura, patrones, librerías base, infraestructura o decisiones con impacto a largo plazo.
- Selección de tecnologías (frameworks, DB, mensajería, CI/CD, hosting, etc.).
- Cambios que afectan múltiples equipos o repositorios.

No se crean ADRs para detalles de implementación menores o cambios triviales.

---

## 3) Ubicación y convención de nombres

- Carpeta: `adrs/`
- Nombre de archivo: `ADR-XXXX-titulo-kebab-case.md` (XXXX = número secuencial con 4 dígitos, ej. `ADR-0007-adoptar-hexagonal.md`).
- Título interno del documento: `[Número ADR]. [Título de la Decisión]`.

Estados válidos: `Propuesto | Aceptado | Reemplazado | Obsoleto`.

---

## 4) Estructura obligatoria del ADR

Debe seguir exactamente la plantilla de `docs/template-ADR.md`:

1. Encabezado
   - Número y Título
   - Fecha (YYYY-MM-DD)
   - Estado (uno de los válidos)
2. Contexto
3. Alternativas consideradas (mínimo 2)
4. Decisión (clara y concisa)
   - Justificación (criterios: coste, simplicidad, rendimiento, mantenibilidad, etc.)
5. Consecuencias
   - Positivas, Negativas, Riesgos
6. Notas adicionales (opcional)

Mantener los niveles de encabezado `#`, `##` exactamente como en la plantilla.

---

## 5) Pasos para crear o actualizar un ADR

1. Duplicar la plantilla `docs/template-ADR.md` y moverla a `adrs/` con el nombre correcto.
2. Completar todos los campos con información real (no dejar `[placeholder]`).
3. Asegurar 2+ alternativas reales en “Alternativas consideradas”.
4. Escribir una “Decisión” inequívoca y su “Justificación”.
5. Documentar “Consecuencias” incluyendo riesgos y mitigaciones.
6. Si reemplaza un ADR anterior, indicar referencia cruzada (ej. “Reemplaza a ADR-0003”).
7. Actualizar el índice (`docs/DOC017-ADR-Index.md`) si existe automatización, ejecutarla; si es manual, añadir/actualizar fila.
8. Revisar ortografía, formato Markdown, enlaces y consistencia.

---

## 6) Checklist de validación

- [ ] Nombre del archivo y título cumplen la convención.
- [ ] Fecha en formato `YYYY-MM-DD`.
- [ ] Estado válido y actualizado.
- [ ] Mínimo 2 alternativas consideradas con Pros/Contras.
- [ ] Decisión y Justificación claras.
- [ ] Consecuencias incluyen positivas, negativas y riesgos.
- [ ] Referencias cruzadas (si aplica) a otros ADRs o docs.
- [ ] Enlaces relativos correctos.
- [ ] Markdown válido (encabezados, listas, código).

---

## 7) Ejemplo mínimo (extracto)

```markdown
# ADR-0012. Adoptar Arquitectura Hexagonal

**Fecha:** 2025-08-06

**Estado:** Aceptado

## Contexto
Necesitamos desacoplar dominio de frameworks para mejorar testabilidad y portabilidad.

## Alternativas Consideradas
1. MVC tradicional (Pros: simple; Contras: acoplamiento alto)
2. Hexagonal (Pros: aislamiento dominio; Contras: curva aprendizaje)

## Decisión
Adoptar Arquitectura Hexagonal.

**Justificación:** Facilita pruebas, reduce acoplamientos de infraestructura, mejora mantenibilidad.

## Consecuencias
- Positivas: Test unitarios más simples, puertos/adaptadores claros.
- Negativas: Esfuerzo inicial de adopción.
- Riesgos: Sobre-abstracción; mitigación: guías y ejemplos.
```

---

## 8) Buenas prácticas

- Escribir para lectores futuros; evitar jerga específica del momento.
- Cuantificar cuando sea posible (benchmarks, costes, SLAs).
- Enlazar discusiones relevantes (issues/PRs/Docs). 
- Mantener un tono neutral y técnico.

---

## 9) Errores comunes a evitar

- Dejar placeholders o secciones vacías.
- No documentar alternativas descartadas y por qué.
- Usar un estado incorrecto o no actualizarlo con el tiempo.
- Títulos vagos; deben ser accionables y descriptivos.

---

## 10) Mantenimiento

- Cuando un ADR queda obsoleto, crear uno nuevo que lo reemplace y actualizar estados.
- Verificar que el índice (`DOC017-ADR-Index.md`) referencia correctamente todos los ADRs.

---

## 11) Referencias

- Plantilla base: `docs/template-ADR.md`
- Índice de ADRs: `docs/DOC017-ADR-Index.md`
- Guía general de trabajo: `GUIA_COMPLETA_DE_USO.md`

