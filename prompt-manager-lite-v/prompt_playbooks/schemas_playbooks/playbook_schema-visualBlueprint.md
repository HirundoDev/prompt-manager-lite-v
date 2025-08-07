# Schema Playbook — visualBlueprint

Propósito: consolidar blueprint visual (páginas, layouts, componentes clave) para alinear diseño e implementación.

Ubicación: `schemas/master_blueprint_parts/visualBlueprint.json`

---

1) Estructura
- LEGACY `screens[]`: { screenName, description, image_url, link_to_prototype }
- `figmaRef?`: enlace/ID del archivo principal de Figma
- `prototypeLinks[]?`: URIs a prototipos navegables
- `pages[]`: { id, title, route, layout, components[], componentRefs[]? }
- `layouts[]`: { name, regions[] }
- `navigation`: { menuItems[] }
- `states[]`: { pageId, stateId, description, wireframeRef }
- `assets[]`: { type: image|icon|illustration|video|component, uri, description }
- `breakpoints[]`: { name, width }
- `themes[]`: { name, tokensRef }
- `annotations[]`: { target: screenName|pageId|componentId, note, severity: info|warning|critical }

---

2) Procedimiento
1. Inventariar páginas y rutas.
2. Definir layouts y navegación.
3. Mapear estados/Wireframes.
4. Registrar assets y puntos de quiebre responsivos.
5. Anotar decisiones/consideraciones relevantes.
6. Enlazar componentes de `componentLibrary` vía `pages[].componentRefs[]`.
7. Documentar `figmaRef` y `prototypeLinks` si existen.

---

3) Ejemplo
```json
{
  "figmaRef": "https://www.figma.com/file/ABC123/Proyecto",
  "prototypeLinks": ["https://www.figma.com/proto/ABC123/flow"],
  "pages": [{"id": "home", "title": "Home", "route": "/", "layout": "main", "components": ["Header", "Hero"], "componentRefs": ["cmp-header", "cmp-hero"]}],
  "layouts": [{"name": "main", "regions": ["header", "content", "footer"]}],
  "navigation": {"menuItems": ["Home", "Profile"]},
  "states": [{"pageId": "home", "stateId": "empty", "description": "No data yet", "wireframeRef": "Login-Empty"}],
  "assets": [{"type": "image", "uri": "/assets/hero.png", "description": "Hero Illustration"}],
  "breakpoints": [{"name": "md", "width": 768}],
  "themes": [{"name": "light", "tokensRef": "design-tokens.json#light"}],
  "annotations": [{"target": "home", "note": "CTA debe ser primario", "severity": "info"}]
}
```

---

4) Checklist
- [ ] Páginas y layouts definidos.
- [ ] Navegación alineada.
- [ ] Estados/Wireframes enlazados.
- [ ] Assets y breakpoints catalogados.
- [ ] Anotaciones capturadas.
- [ ] `figmaRef` y `prototypeLinks` documentados.
- [ ] `componentRefs` enlazan a `componentLibrary`.
