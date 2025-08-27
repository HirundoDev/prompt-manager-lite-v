#!/usr/bin/env python3
"""
Operation Guide Manager - The Mighty Task v4.0
===============================================

Gestiona guías operacionales independientes para planificación de ideas,
instalaciones, investigaciones y comparaciones antes de implementar.
"""

import argparse
import json
import os
import sys
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import hashlib
import re

# Agregar path para imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared.colored_output import ColoredOutput

class OperationGuideManager:
    def __init__(self, base_path: str = None):
        """Inicializar el gestor de guías operacionales."""
        if base_path:
            self.base_path = Path(base_path)
        else:
            # Detectar automáticamente el directorio base
            current_dir = Path.cwd()
            if (current_dir / "operational-guides").exists():
                self.base_path = current_dir
            elif (current_dir.parent / "operational-guides").exists():
                self.base_path = current_dir.parent
            else:
                self.base_path = current_dir
        
        self.operational_guides_dir = self.base_path / "operational-guides"
        self.tracking_file = self.operational_guides_dir / ".operational-guides-tracking.json"
        
        # Crear directorio si no existe
        self.operational_guides_dir.mkdir(exist_ok=True)
        
        # Cargar tracking
        self.tracking_data = self._load_tracking()
    
    def _load_tracking(self) -> Dict:
        """Cargar datos de tracking."""
        if self.tracking_file.exists():
            try:
                with open(self.tracking_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        return {
            "guides": [],
            "metadata": {
                "created_date": datetime.now().strftime("%Y-%m-%d"),
                "version": "1.0",
                "total_guides": 0,
                "last_updated": datetime.now().isoformat()
            },
            "settings": {
                "auto_backup": True,
                "validation_enabled": True,
                "duplicate_check": True
            }
        }
    
    def _save_tracking(self):
        """Guardar datos de tracking."""
        self.tracking_data["metadata"]["last_updated"] = datetime.now().isoformat()
        self.tracking_data["metadata"]["total_guides"] = len(self.tracking_data["guides"])
        
        with open(self.tracking_file, 'w', encoding='utf-8') as f:
            json.dump(self.tracking_data, f, indent=2, ensure_ascii=False)
    
    def create_guide(self, guide_name: str, title: str = None, description: str = None, tags: str = None) -> bool:
        """Crear nueva guía operacional."""
        try:
            # Validar duplicados
            if self._guide_exists(guide_name):
                ColoredOutput.error(f"Guía ya existe: {guide_name}")
                return False
            
            # Crear archivo de la guía
            guide_file = self.operational_guides_dir / f"{guide_name}.md"
            
            # Generar contenido del template
            content = self._generate_guide_template(guide_name, title, description, tags)
            
            with open(guide_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Actualizar tracking
            guide_info = {
                "name": guide_name,
                "filename": f"{guide_name}.md",
                "title": title or guide_name.replace('-', ' ').title(),
                "description": description or f"Guía operacional para {guide_name.replace('-', ' ')}",
                "tags": self._parse_tags(tags) if tags else self._extract_tags(guide_name),
                "created_date": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "usage_count": 0,
                "status": "active"
            }
            
            self.tracking_data["guides"].append(guide_info)
            self._save_tracking()
            
            ColoredOutput.success(f"Guía operacional creada: {guide_file}")
            ColoredOutput.info(f"Título: {guide_info['title']}")
            ColoredOutput.info(f"Tags: {', '.join(guide_info['tags'])}")
            return True
            
        except Exception as e:
            ColoredOutput.error(f"Error creando guía operacional: {e}")
            return False
    
    def _guide_exists(self, guide_name: str) -> bool:
        """Verificar si una guía ya existe."""
        # Verificar en tracking
        for guide in self.tracking_data["guides"]:
            if guide["name"] == guide_name:
                return True
        
        # Verificar archivo físico
        guide_file = self.operational_guides_dir / f"{guide_name}.md"
        return guide_file.exists()
    
    def _generate_guide_template(self, guide_name: str, title: str = None, description: str = None, tags: str = None) -> str:
        """Generar template para guía operacional."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        
        final_title = title or guide_name.replace('-', ' ').title()
        final_description = description or f"Guía operacional para {guide_name.replace('-', ' ')}"
        final_tags = self._parse_tags(tags) if tags else self._extract_tags(guide_name)
        
        return f"""# {final_title}

**Tipo:** Guía Operacional  
**Fecha de creación:** {current_date} {current_time}  
**Descripción:** {final_description}  
**Tags:** {', '.join(final_tags)}  
**Estado:** 🔄 PLANIFICACIÓN

---

## 📋 **PROPÓSITO DE LA GUÍA**

### **Objetivo Principal**
[Describir el objetivo principal de esta guía operacional]

### **Alcance**
- [ ] [Definir qué incluye esta guía]
- [ ] [Definir qué NO incluye esta guía]
- [ ] [Establecer límites y prerrequisitos]

---

## 🎯 **PLANIFICACIÓN INICIAL**

### **Investigación Previa Necesaria**
- [ ] [Investigación 1: Descripción]
- [ ] [Investigación 2: Descripción]
- [ ] [Investigación 3: Descripción]

### **Comparaciones a Realizar**
- [ ] [Comparación 1: Herramienta A vs B]
- [ ] [Comparación 2: Enfoque X vs Y]
- [ ] [Comparación 3: Metodología P vs Q]

### **Recursos Necesarios**
- **Tiempo estimado:** [X horas/días]
- **Herramientas:** [Lista de herramientas]
- **Conocimientos previos:** [Lista de prerrequisitos]

---

## 🔍 **FASE DE INVESTIGACIÓN**

### **Fuentes Consultadas**
- [ ] Documentación oficial
- [ ] Tutoriales actualizados (2024-2025)
- [ ] Casos de uso reales
- [ ] Comparativas técnicas

### **Hallazgos Clave**
[Se completará durante la investigación]

#### **Ventajas Identificadas**
1. [Ventaja 1]
2. [Ventaja 2]
3. [Ventaja 3]

#### **Desventajas o Limitaciones**
1. [Limitación 1]
2. [Limitación 2]
3. [Limitación 3]

---

## ⚖️ **ANÁLISIS COMPARATIVO**

### **Opción 1: [Nombre]**
- **Pros:** [Lista de ventajas]
- **Contras:** [Lista de desventajas]
- **Casos de uso ideales:** [Cuándo usar]

### **Opción 2: [Nombre]**
- **Pros:** [Lista de ventajas]
- **Contras:** [Lista de desventajas]
- **Casos de uso ideales:** [Cuándo usar]

### **Recomendación Final**
**Opción elegida:** [Opción seleccionada]  
**Justificación:** [Razones de la elección]

---

## 📝 **PLAN DE IMPLEMENTACIÓN**

### **Fases del Proyecto**
1. **Fase 1: Preparación**
   - [ ] [Tarea 1]
   - [ ] [Tarea 2]
   - [ ] [Tarea 3]

2. **Fase 2: Instalación/Configuración**
   - [ ] [Tarea 1]
   - [ ] [Tarea 2]
   - [ ] [Tarea 3]

3. **Fase 3: Validación**
   - [ ] [Tarea 1]
   - [ ] [Tarea 2]
   - [ ] [Tarea 3]

### **Comandos Clave**
```bash
# Comandos de instalación
[comandos principales]
```

```bash
# Comandos de configuración
[comandos de setup]
```

```bash
# Comandos de validación
[comandos de prueba]
```

---

## ✅ **CHECKLIST DE VALIDACIÓN**

### **Prerrequisitos**
- [ ] Sistema operativo compatible
- [ ] Dependencias instaladas
- [ ] Permisos necesarios configurados

### **Instalación Exitosa**
- [ ] Instalación completada sin errores
- [ ] Servicios iniciados correctamente
- [ ] Configuración aplicada

### **Pruebas Funcionales**
- [ ] Prueba básica 1: [Descripción]
- [ ] Prueba básica 2: [Descripción]
- [ ] Prueba de integración: [Descripción]

---

## 🚨 **TROUBLESHOOTING**

### **Problemas Comunes**

#### **Error 1: [Descripción del error]**
- **Síntomas:** [Cómo se manifiesta]
- **Causa:** [Causa probable]
- **Solución:** [Pasos para resolver]

#### **Error 2: [Descripción del error]**
- **Síntomas:** [Cómo se manifiesta]
- **Causa:** [Causa probable]
- **Solución:** [Pasos para resolver]

---

## 📚 **REFERENCIAS Y RECURSOS**

### **Documentación Oficial**
- [Enlace 1](URL) - Consultado {current_date}
- [Enlace 2](URL) - Consultado {current_date}

### **Tutoriales y Guías**
- [Tutorial 1](URL) - Consultado {current_date}
- [Tutorial 2](URL) - Consultado {current_date}

### **Herramientas Complementarias**
- [Herramienta 1](URL) - [Descripción]
- [Herramienta 2](URL) - [Descripción]

---

## 📊 **MÉTRICAS Y SEGUIMIENTO**

### **Indicadores de Éxito**
- [ ] [Métrica 1: Descripción]
- [ ] [Métrica 2: Descripción]
- [ ] [Métrica 3: Descripción]

### **Tiempo Invertido**
- **Investigación:** [X horas]
- **Implementación:** [X horas]
- **Validación:** [X horas]
- **Total:** [X horas]

---

## 🔄 **ACTUALIZACIONES**

### **Historial de Cambios**
- **{current_date}:** Guía creada
- **[Fecha]:** [Descripción del cambio]

### **Próximas Revisiones**
- **Fecha programada:** [Fecha]
- **Motivo:** [Razón de la revisión]

---

**Estado actual:** 🔄 PLANIFICACIÓN  
**Última actualización:** {current_date} {current_time}  
**Próximo paso:** Completar investigación previa
"""
    
    def _parse_tags(self, tags_str: str) -> List[str]:
        """Parsear string de tags."""
        if not tags_str:
            return []
        
        tags = [tag.strip().lower() for tag in tags_str.split(',')]
        return [tag for tag in tags if tag]
    
    def _extract_tags(self, guide_name: str) -> List[str]:
        """Extraer tags automáticamente del nombre de la guía."""
        tags = [guide_name.lower()]
        
        # Tags automáticos basados en palabras clave
        auto_tags = {
            'docker': ['containerization', 'devops', 'deployment'],
            'kubernetes': ['orchestration', 'devops', 'containers'],
            'postgres': ['database', 'sql', 'storage'],
            'mongodb': ['database', 'nosql', 'storage'],
            'redis': ['cache', 'database', 'performance'],
            'nginx': ['web-server', 'proxy', 'deployment'],
            'apache': ['web-server', 'deployment'],
            'installation': ['setup', 'configuration'],
            'comparison': ['analysis', 'research'],
            'planning': ['strategy', 'methodology'],
            'research': ['investigation', 'analysis'],
            'setup': ['installation', 'configuration'],
            'config': ['configuration', 'setup'],
            'deploy': ['deployment', 'devops'],
            'security': ['security', 'authentication'],
            'backup': ['backup', 'recovery', 'storage'],
            'monitoring': ['monitoring', 'observability'],
            'performance': ['optimization', 'performance'],
            'testing': ['testing', 'quality-assurance']
        }
        
        for keyword, keyword_tags in auto_tags.items():
            if keyword in guide_name.lower():
                tags.extend(keyword_tags)
        
        return list(set(tags))
    
    def search_guides(self, query: str = None, tags: str = None, name: str = None) -> List[Dict]:
        """Buscar guías operacionales."""
        results = []
        
        for guide_info in self.tracking_data["guides"]:
            if self._matches_search(guide_info, query, tags, name):
                guide_path = self.operational_guides_dir / guide_info["filename"]
                guide_info["exists"] = guide_path.exists()
                guide_info["file_path"] = str(guide_path)
                results.append(guide_info)
        
        return results
    
    def _matches_search(self, guide_info: Dict, query: str = None, tags: str = None, name: str = None) -> bool:
        """Verificar si una guía coincide con los criterios de búsqueda."""
        if query:
            query_lower = query.lower()
            if (query_lower not in guide_info["name"].lower() and 
                query_lower not in guide_info["title"].lower() and
                query_lower not in guide_info["description"].lower()):
                return False
        
        if tags:
            search_tags = [tag.strip().lower() for tag in tags.split(',')]
            guide_tags = [tag.lower() for tag in guide_info["tags"]]
            if not any(tag in guide_tags for tag in search_tags):
                return False
        
        if name:
            if name.lower() not in guide_info["name"].lower():
                return False
        
        return True
    
    def list_guides(self, format_output: str = "table") -> List[Dict]:
        """Listar todas las guías operacionales."""
        guides = []
        
        for guide_info in self.tracking_data["guides"]:
            guide_path = self.operational_guides_dir / guide_info["filename"]
            guide_info["exists"] = guide_path.exists()
            guide_info["file_path"] = str(guide_path)
            guides.append(guide_info)
        
        if format_output == "table":
            self._print_guides_table(guides)
        
        return guides
    
    def _print_guides_table(self, guides: List[Dict]):
        """Imprimir tabla de guías."""
        if not guides:
            ColoredOutput.warning("No hay guías operacionales creadas")
            return
        
        ColoredOutput.info("Guías Operacionales Disponibles:")
        print()
        
        print(f"{'Nombre':<25} {'Título':<30} {'Tags':<20} {'Estado':<10}")
        print("-" * 90)
        
        for guide in guides:
            name = guide["name"][:23]
            title = guide["title"][:28]
            tags = ", ".join(guide["tags"][:2])[:18]  # Mostrar solo primeros 2 tags
            status = "✅ OK" if guide["exists"] else "❌ MISSING"
            
            print(f"{name:<25} {title:<30} {tags:<20} {status:<10}")
        
        print()
        ColoredOutput.info(f"Total: {len(guides)} guías operacionales")

def main():
    """Función principal del CLI."""
    parser = argparse.ArgumentParser(
        description='Operation Guide Manager - The Mighty Task v4.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Crear nueva guía operacional
  python scripts/operation-guide-manager.py --create "docker-installation" \\
    --title "Instalación Docker Ubuntu" \\
    --description "Guía completa para Docker en Ubuntu 22.04" \\
    --tags "docker,instalacion,ubuntu"
  
  # Buscar guías por tags
  python scripts/operation-guide-manager.py --search --tags "docker,installation"
  
  # Buscar por nombre
  python scripts/operation-guide-manager.py --search --name "installation"
  
  # Listar todas las guías
  python scripts/operation-guide-manager.py --list
        """
    )
    
    parser.add_argument('--create', metavar='GUIDE_NAME', help='Crear nueva guía operacional')
    parser.add_argument('--title', metavar='TITLE', help='Título de la guía')
    parser.add_argument('--description', metavar='DESC', help='Descripción de la guía')
    parser.add_argument('--tags', metavar='TAGS', help='Tags separados por comas')
    
    parser.add_argument('--search', action='store_true', help='Buscar guías operacionales')
    parser.add_argument('--query', metavar='QUERY', help='Búsqueda por texto libre')
    parser.add_argument('--name', metavar='NAME', help='Buscar por nombre')
    
    parser.add_argument('--list', action='store_true', help='Listar todas las guías')
    
    parser.add_argument('--base-path', metavar='PATH', help='Directorio base del proyecto')
    parser.add_argument('--quiet', action='store_true', help='Salida mínima')
    
    args = parser.parse_args()
    
    manager = OperationGuideManager(args.base_path)
    
    try:
        if args.create:
            success = manager.create_guide(args.create, args.title, args.description, args.tags)
            return 0 if success else 1
        
        elif args.search:
            results = manager.search_guides(args.query, args.tags, args.name)
            if results:
                ColoredOutput.success(f"Encontradas {len(results)} guías operacionales:")
                for result in results:
                    print(f"  - {result['name']} - {result['title']}")
                    print(f"    Tags: {', '.join(result['tags'])}")
                    print(f"    Archivo: {result['file_path']}")
                    print()
            else:
                ColoredOutput.warning("No se encontraron guías operacionales con esos criterios")
            return 0
        
        elif args.list:
            manager.list_guides()
            return 0
        
        else:
            parser.print_help()
            return 1
            
    except KeyboardInterrupt:
        ColoredOutput.warning("Operación cancelada por el usuario")
        return 1
    except Exception as e:
        ColoredOutput.error(f"Error inesperado: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
