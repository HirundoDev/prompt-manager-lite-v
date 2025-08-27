#!/usr/bin/env python3
"""
Web Guide Manager - The Mighty Task v3.1
========================================

Gestiona web-guides para reutilización de investigaciones web entre sesiones.
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

class WebGuideManager:
    def __init__(self, base_path: str = None):
        """Inicializar el gestor de web-guides."""
        if base_path:
            self.base_path = Path(base_path)
        else:
            # Detectar automáticamente el directorio base
            current_dir = Path.cwd()
            if (current_dir / "daily-work").exists():
                self.base_path = current_dir
            elif (current_dir.parent / "daily-work").exists():
                self.base_path = current_dir.parent
            else:
                self.base_path = current_dir
        
        self.daily_work_dir = self.base_path / "daily-work"
        self.mission_resumes_dir = self.base_path / "mission-resumes"
        self.tracking_file = self.base_path / ".tracking.json"
        
        # Crear directorios si no existen
        self.daily_work_dir.mkdir(exist_ok=True)
        self.mission_resumes_dir.mkdir(exist_ok=True)
        
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
            "web_guides": {
                "guides_created": [],
                "consolidated_guides": {},
                "last_updated": datetime.now().isoformat()
            }
        }
    
    def _save_tracking(self):
        """Guardar datos de tracking."""
        self.tracking_data["web_guides"]["last_updated"] = datetime.now().isoformat()
        
        with open(self.tracking_file, 'w', encoding='utf-8') as f:
            json.dump(self.tracking_data, f, indent=2, ensure_ascii=False)
    
    def create_guide(self, guide_name: str, session: str, template: str = "basic", use_research_template: bool = False) -> bool:
        """Crear nuevo web-guide."""
        try:
            # Validar sesión
            session_dir = self.daily_work_dir / session
            if not session_dir.exists():
                ColoredOutput.error(f"Sesión no encontrada: {session}")
                return False
            
            # Crear directorio web-guides si no existe
            web_guides_dir = session_dir / "web-guides"
            web_guides_dir.mkdir(exist_ok=True)
            
            # Crear archivo del guide
            guide_file = web_guides_dir / f"{guide_name}-guide.md"
            
            if guide_file.exists():
                ColoredOutput.warning(f"Web-guide ya existe: {guide_file}")
                return False
            
            # Generar contenido del template
            if use_research_template:
                content = self._load_research_template(guide_name)
            else:
                content = self._generate_template(guide_name, template)
            
            with open(guide_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Actualizar tracking
            guide_info = {
                "guide_name": f"{guide_name}-guide.md",
                "created_date": datetime.now().isoformat(),
                "session": session,
                "template_used": template,
                "last_updated": datetime.now().isoformat(),
                "tags": self._extract_tags(guide_name)
            }
            
            self.tracking_data["web_guides"]["guides_created"].append(guide_info)
            self._save_tracking()
            
            ColoredOutput.success(f"Web-guide creado: {guide_file}")
            return True
            
        except Exception as e:
            ColoredOutput.error(f"Error creando web-guide: {e}")
            return False
    
    def _generate_template(self, guide_name: str, template: str) -> str:
        """Generar template para web-guide."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        if template == "basic":
            return f"""# {guide_name.title().replace('-', ' ')} Guide - 2025

**Fecha de investigación:** {current_date}  
**Investigador:** [Nombre del agente AI]  
**Propósito:** [Descripción del propósito de la investigación]  
**Estado:** 🔍 EN_INVESTIGACIÓN

## Preguntas de Investigación
- [ ] [Pregunta específica 1]
- [ ] [Pregunta específica 2]
- [ ] [Pregunta específica 3]

## Fuentes a Consultar
- [ ] Documentación oficial
- [ ] GitHub releases
- [ ] Stack Overflow (últimos 6 meses)
- [ ] Artículos de desarrolladores reconocidos

## Hallazgos
[Se llenará durante la investigación]

### Versión Actual
- **Versión estable:** [Versión]
- **Fuente:** [URL]
- **Cambios importantes:** [Lista de cambios]

### Mejores Prácticas 2025
1. [Práctica 1]
2. [Práctica 2]
3. [Práctica 3]

### Configuración Recomendada
```bash
# Comandos de instalación
[comandos]
```

```javascript
// Código de ejemplo
[código]
```

## Validación Práctica
### Prueba 1: [Nombre de la prueba]
```bash
[comando]
```
**Resultado:** [✅ EXITOSO / ❌ FALLÓ]

## Troubleshooting Común
### Problema 1: [Descripción]
**Causa:** [Causa del problema]
**Solución:** [Solución detallada]

## Referencias Consultadas
- [Fuente 1](URL) - Consultado {current_date}
- [Fuente 2](URL) - Consultado {current_date}

## Validación Completa
- [ ] Código probado en entorno local
- [ ] Dependencias verificadas sin conflictos
- [ ] Documentación actualizada
- [ ] Performance validada
"""
        
        return self._generate_template(guide_name, "basic")
    
    def _extract_tags(self, guide_name: str) -> List[str]:
        """Extraer tags del nombre del guide."""
        tags = [guide_name.lower()]
        
        tech_tags = {
            'express': ['nodejs', 'backend', 'server'],
            'react': ['frontend', 'javascript', 'ui'],
            'vue': ['frontend', 'javascript', 'ui'],
            'node': ['nodejs', 'backend', 'javascript'],
            'python': ['backend', 'scripting'],
            'docker': ['containerization', 'devops'],
            'database': ['data', 'storage'],
            'mongodb': ['database', 'nosql'],
            'git': ['version-control', 'development']
        }
        
        for tech, tech_tags_list in tech_tags.items():
            if tech in guide_name.lower():
                tags.extend(tech_tags_list)
        
        return list(set(tags))
    
    def _load_research_template(self, guide_name: str) -> str:
        """Cargar y personalizar template-web-research.md."""
        template_path = self.base_path / "template-web-research.md"
        
        if not template_path.exists():
            ColoredOutput.warning(f"Template de investigación no encontrado: {template_path}")
            return self._generate_template(guide_name, "basic")
        
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Personalizar el contenido
            current_date = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M:%S")
            
            # Reemplazar placeholders si existen
            content = content.replace("[FECHA]", current_date)
            content = content.replace("[HORA]", current_time)
            content = content.replace("[TEMA_INVESTIGACION]", guide_name.replace('-', ' ').title())
            content = content.replace("[INVESTIGADOR]", "AI Agent")
            
            # Agregar header personalizado
            header = f"""# Investigación Web: {guide_name.replace('-', ' ').title()}

**Generado desde:** template-web-research.md  
**Fecha:** {current_date} {current_time}  
**Investigador:** AI Agent  
**Tema:** {guide_name.replace('-', ' ').title()}

---

"""
            
            return header + content
            
        except Exception as e:
            ColoredOutput.error(f"Error cargando template de investigación: {e}")
            return self._generate_template(guide_name, "basic")
    
    def search_guides(self, query: str) -> List[Dict]:
        """Buscar web-guides por query."""
        results = []
        
        for guide_info in self.tracking_data["web_guides"]["guides_created"]:
            if self._matches_query(guide_info, query):
                guide_path = self._find_guide_file(guide_info)
                if guide_path:
                    guide_info["file_path"] = str(guide_path)
                    results.append(guide_info)
        
        return results
    
    def _matches_query(self, guide_info: Dict, query: str) -> bool:
        """Verificar si un guide coincide con la query."""
        query_lower = query.lower()
        
        if query_lower in guide_info["guide_name"].lower():
            return True
        
        if "tags" in guide_info:
            for tag in guide_info["tags"]:
                if query_lower in tag.lower():
                    return True
        
        if query_lower in guide_info["session"].lower():
            return True
        
        return False
    
    def _find_guide_file(self, guide_info: Dict) -> Optional[Path]:
        """Encontrar archivo físico del guide."""
        session = guide_info["session"]
        guide_name = guide_info["guide_name"]
        
        session_path = self.daily_work_dir / session / "web-guides" / guide_name
        if session_path.exists():
            return session_path
        
        for mission_dir in self.mission_resumes_dir.glob("*/"):
            if mission_dir.is_dir():
                guide_path = mission_dir / "web-guides" / guide_name
                if guide_path.exists():
                    return guide_path
        
        return None
    
    def list_guides(self, format_output: str = "table") -> List[Dict]:
        """Listar todos los web-guides."""
        guides = []
        
        for guide_info in self.tracking_data["web_guides"]["guides_created"]:
            guide_path = self._find_guide_file(guide_info)
            guide_info["exists"] = guide_path is not None
            guide_info["file_path"] = str(guide_path) if guide_path else "NOT_FOUND"
            guides.append(guide_info)
        
        if format_output == "table":
            self._print_guides_table(guides)
        
        return guides
    
    def _print_guides_table(self, guides: List[Dict]):
        """Imprimir tabla de guides."""
        if not guides:
            ColoredOutput.warning("No hay web-guides creados")
            return
        
        ColoredOutput.info("Web-Guides Disponibles:")
        print()
        
        print(f"{'Guide':<30} {'Sesión':<25} {'Fecha':<12} {'Estado':<10}")
        print("-" * 80)
        
        for guide in guides:
            name = guide["guide_name"][:28]
            session = guide["session"][:23]
            date = guide["created_date"][:10]
            status = "✅ OK" if guide["exists"] else "❌ MISSING"
            
            print(f"{name:<30} {session:<25} {date:<12} {status:<10}")

def main():
    """Función principal del CLI."""
    parser = argparse.ArgumentParser(
        description='Web Guide Manager - The Mighty Task v3.1',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Crear nuevo web-guide básico
  python scripts/web-guide-manager.py --create "express-setup" --session "2025-08-25_BACKEND-API-SETUP"
  
  # Crear web-guide usando template de investigación
  python scripts/web-guide-manager.py --create "react-hooks-research" --session "2025-08-25_FRONTEND-COMPONENTS" --use-research-template
  
  # Buscar web-guides
  python scripts/web-guide-manager.py --search "express"
  
  # Listar todos los guides
  python scripts/web-guide-manager.py --list-guides
        """
    )
    
    parser.add_argument('--create', metavar='GUIDE_NAME', help='Crear nuevo web-guide')
    parser.add_argument('--session', metavar='SESSION', help='Sesión para el web-guide')
    parser.add_argument('--template', choices=['basic', 'technology', 'research'], default='basic', help='Template a usar')
    parser.add_argument('--use-research-template', action='store_true', help='Usar template-web-research.md como base')
    
    parser.add_argument('--search', metavar='QUERY', help='Buscar web-guides')
    parser.add_argument('--list-guides', action='store_true', help='Listar todos los web-guides')
    
    parser.add_argument('--base-path', metavar='PATH', help='Directorio base del proyecto')
    parser.add_argument('--quiet', action='store_true', help='Salida mínima')
    
    args = parser.parse_args()
    
    manager = WebGuideManager(args.base_path)
    
    try:
        if args.create:
            if not args.session:
                ColoredOutput.error("--session es requerido para --create")
                return 1
            
            success = manager.create_guide(args.create, args.session, args.template, args.use_research_template)
            return 0 if success else 1
        
        elif args.search:
            results = manager.search_guides(args.search)
            if results:
                ColoredOutput.success(f"Encontrados {len(results)} web-guides:")
                for result in results:
                    print(f"  - {result['guide_name']} (sesión: {result['session']})")
            else:
                ColoredOutput.warning(f"No se encontraron web-guides para: {args.search}")
            return 0
        
        elif args.list_guides:
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