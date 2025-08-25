"""
Template Base y Genérico
========================

Template genérico que se usa como fallback para casos no específicos.
"""

def create_generic_template(theme, date_str, filename):
    """Template genérico para casos no específicos"""
    return f'''# Marco de Referencia - {filename.split('.')[0]}

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** {filename.split('.')[0]}  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal**, adaptable a diferentes tecnologías y contextos.

### Decisiones Clave a Documentar
- [Identificar decisiones principales para esta área]
- [Listar opciones técnicas relevantes]
- [Capturar justificaciones y trade-offs]
- [Documentar patrones y estándares]

---

## 🔧 Decisiones Técnicas

### Decisión Principal 1
**Decisión:** [Describir la decisión tomada]
**Opciones consideradas:** [Listar alternativas]
**Justificación:** [Razón de la elección]

### Decisión Principal 2
**Decisión:** [Describir la decisión tomada]
**Opciones consideradas:** [Listar alternativas]
**Justificación:** [Razón de la elección]

### Decisión Principal 3
**Decisión:** [Describir la decisión tomada]
**Opciones consideradas:** [Listar alternativas]
**Justificación:** [Razón de la elección]

---

## 🏗️ Implementación

### Configuración Base
```bash
# Comandos de setup y configuración
[COMPLETAR con comandos específicos]
```

### Estructura del Proyecto
```
[DEFINIR estructura de carpetas y organización]
```

### Herramientas y Dependencies
- **Principal:** [Herramienta o framework principal]
- **Supporting:** [Herramientas de soporte]
- **Development:** [Herramientas de desarrollo]

---

## 📋 Checklist de Implementación

### Setup Inicial
- [ ] [Tarea de setup 1]
- [ ] [Tarea de setup 2]
- [ ] [Tarea de setup 3]

### Desarrollo
- [ ] [Tarea de desarrollo 1]
- [ ] [Tarea de desarrollo 2]
- [ ] [Tarea de desarrollo 3]

### Testing y Validación
- [ ] [Tarea de testing 1]
- [ ] [Tarea de testing 2]
- [ ] [Tarea de testing 3]

---

## 🔄 Próximos Pasos

1. [Paso inmediato 1]
2. [Paso inmediato 2]
3. [Paso inmediato 3]

### Consideraciones Futuras
- [Consideración 1]
- [Consideración 2]
- [Consideración 3]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''
