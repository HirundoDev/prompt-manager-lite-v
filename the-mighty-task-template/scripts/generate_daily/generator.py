"""
Daily Session Generator - Core Module
=====================================

Genera sesiones diarias con validaciones anti-duplicación y detección de templates.
"""

import os
import sys
import json
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Importar módulos compartidos
sys.path.append(str(Path(__file__).parent.parent))
from shared.template_detector import TemplateDetector
from shared.playbook_registry import PlaybookRegistry
from shared.colored_output import ColoredOutput

class DailySessionGenerator:
    """Generador de sesiones diarias con validaciones avanzadas."""
    
    def __init__(self, base_path: Optional[Path] = None):
        self.base_path = Path(base_path or Path(__file__).parent.parent.parent)
        self.daily_work_dir = self.base_path / 'daily-work'
        self.template_files = {
            'development': self.base_path / 'template-pendingtask.md',
            'operations': self.base_path / 'template-operations.md',
            'research': self.base_path / 'template-web-research.md'
        }
        self.tracking_file = self.daily_work_dir / '.tracking.json'
        
        # Inicializar módulos compartidos
        self.registry = PlaybookRegistry(self.base_path)
        self.detector = TemplateDetector()
        
        # Verificar estructura del proyecto (buscar archivos indicadores)
        if not any([
            (self.base_path / 'README.md').exists(),
            (self.base_path / 'template-pendingtask.md').exists(),
            (self.base_path / 'scripts').exists()
        ]):
            ColoredOutput.error("No estás en el directorio raíz de The Mighty Task")
            ColoredOutput.info("Ejecuta este script desde el directorio que contiene scripts/ y README.md")
            sys.exit(1)
    
    def validate_session_parameters(self, date_str: str, theme: str) -> Tuple[bool, List[str]]:
        """
        Valida parámetros de sesión antes de crear.
        
        Returns:
            Tuple (es_válido, lista_errores)
        """
        errors = []
        
        # Validar formato de fecha
        try:
            session_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            if session_date > date.today():
                errors.append(f"Fecha futura no permitida: {date_str}")
        except ValueError:
            errors.append(f"Formato de fecha inválido: {date_str}. Usar YYYY-MM-DD")
        
        # Validar tema
        available_themes = list(self.registry.THEME_PLAYBOOK_MAPPING.keys())
        if theme not in available_themes:
            errors.append(f"Tema '{theme}' no válido. Disponibles: {', '.join(available_themes)}")
        else:
            # Validar que el tema tenga playbooks válidos
            validation = self.registry.validate_theme_consistency(theme)
            if not validation['valid']:
                errors.extend(validation['issues'])
        
        return len(errors) == 0, errors
    
    def check_existing_session(self, date_str: str, theme: str) -> Dict[str, any]:
        """
        Verifica si ya existe una sesión similar.
        
        Returns:
            Dict con información de sesión existente
        """
        session_name = f"{date_str}_{theme}"
        session_dir = self.daily_work_dir / session_name
        
        result = {
            'exists': session_dir.exists(),
            'session_name': session_name,
            'session_dir': session_dir,
            'conflicts': [],
            'similar_sessions': []
        }
        
        if session_dir.exists():
            # Verificar contenido existente
            main_file = session_dir / f"pending-tasks-{session_name}.md"
            if main_file.exists():
                try:
                    content = main_file.read_text(encoding='utf-8')
                    analysis = self.detector.analyze_content_quality(content)
                    
                    result['content_analysis'] = analysis
                    result['has_meaningful_content'] = analysis['type'] != 'template'
                    
                    if result['has_meaningful_content']:
                        result['conflicts'].append("Sesión contiene trabajo significativo")
                    
                except Exception as e:
                    result['conflicts'].append(f"Error leyendo archivo principal: {e}")
        
        # Buscar sesiones similares (mismo tema, fechas cercanas)
        if self.daily_work_dir.exists():
            for existing_dir in self.daily_work_dir.iterdir():
                if existing_dir.is_dir() and existing_dir.name != session_name:
                    if theme in existing_dir.name:
                        result['similar_sessions'].append(existing_dir.name)
        
        return result
    
    def detect_template_duplicates(self, theme: str) -> List[Dict]:
        """
        Detecta posibles duplicaciones de templates para un tema.
        
        Returns:
            Lista de posibles duplicaciones detectadas
        """
        duplicates = []
        
        # Verificar duplicados en playbooks base
        registry_duplicates = self.registry.detect_duplicate_templates()
        
        # Verificar duplicados en sesiones existentes del mismo tema
        if self.daily_work_dir.exists():
            theme_sessions = []
            for session_dir in self.daily_work_dir.iterdir():
                if session_dir.is_dir() and theme in session_dir.name:
                    theme_sessions.append(session_dir)
            
            # Comparar templates entre sesiones
            for session_dir in theme_sessions:
                support_docs_dir = session_dir / 'support-docs'
                if support_docs_dir.exists():
                    for doc_file in support_docs_dir.glob('DOC*.md'):
                        if doc_file.exists():
                            try:
                                content = doc_file.read_text(encoding='utf-8')
                                if self.detector.is_template_content(content):
                                    duplicates.append({
                                        'type': 'template_in_session',
                                        'file': str(doc_file),
                                        'session': session_dir.name,
                                        'suggestion': 'Completar o eliminar template vacío'
                                    })
                            except Exception:
                                pass
        
        return duplicates
    
    def load_template_content(self, template_type: str = 'development') -> str:
        """
        Cargar contenido del template según el tipo
        
        Args:
            template_type: Tipo de template (development, operations, operations-modular, research)
            
        Returns:
            Contenido del template como string
        """
        try:
            if template_type == 'operations':
                template_path = self.base_path / 'template-pendingtask-operations.md'
            elif template_type == 'operations-modular':
                template_path = self.base_path / 'template-pendingtask-operations-modular.md'
            elif template_type == 'research':
                template_path = self.base_path / 'template-web-research.md'
            else:  # development (default)
                template_path = self.base_path / 'template-pendingtask.md'
            
            if not template_path.exists():
                ColoredOutput.error(f"Template no encontrado: {template_path}")
                ColoredOutput.info(f"Asegúrate de que existe el archivo: {template_path}")
                sys.exit(1)
                
            return template_path.read_text(encoding='utf-8')
        except Exception as e:
            ColoredOutput.error(f"Error leyendo template: {e}")
            sys.exit(1)
    
    def _get_default_template(self) -> str:
        """Template por defecto si no existe archivo."""
        return """# Tareas Pendientes - {date} - {theme}

**Fecha:** {date}  
**Tema:** {theme}  
**Estado:** En progreso  
**Generado:** {timestamp}

---

## ✅ Tareas Principales

### 🎯 Objetivos del Día
- [ ] [TODO] Definir objetivos específicos para {theme}
- [ ] [TODO] Revisar playbooks relevantes
- [ ] [TODO] Configurar entorno de trabajo

### 📋 Tareas Específicas
- [ ] [TODO] Tarea específica 1
- [ ] [TODO] Tarea específica 2
- [ ] [TODO] Tarea específica 3

---

## 📚 Playbooks de Referencia

{playbooks_section}

---

## 📊 Progreso del Día

### ⏱️ Tiempo Invertido
- **Inicio:** {timestamp}
- **Tiempo total:** [TODO] Actualizar al final del día

### 📈 Completitud
- **Tareas completadas:** 0/{total_tasks}
- **Porcentaje:** 0%

---

## 📝 Notas y Observaciones

### 💡 Aprendizajes
- [TODO] Documentar aprendizajes del día

### 🚧 Bloqueadores
- [TODO] Documentar cualquier bloqueador encontrado

### 🎯 Próximos Pasos
- [TODO] Definir próximos pasos para mañana

---

## 📈 Métricas del Día

| Métrica | Valor |
|---------|-------|
| Tareas completadas | 0 |
| Tiempo invertido | 0h |
| Playbooks consultados | 0 |
| Templates completados | 0 |

---

**Generado por:** The Mighty Task - Daily Session Generator  
**Última actualización:** {timestamp}
"""

    def customize_template_content(self, template_content: str, date_str: str, theme: str, template_type: str = 'development') -> str:
        """
        Personaliza el contenido del template con datos específicos
        
        Args:
            template_content: Contenido base del template
            date_str: Fecha en formato YYYY-MM-DD
            theme: Tema de la sesión
            template_type: Tipo de template para personalización condicional
            
        Returns:
            Contenido personalizado del template
        """
        # Reemplazos básicos comunes a todos los templates
        customized = template_content.replace('[FECHA]', date_str)
        customized = customized.replace('[TEMA]', theme)
        customized = customized.replace('[YYYY-MM-DD]', date_str)
        
        # Personalización específica por tipo de template
        if template_type == 'development':
            # Para templates de desarrollo, incluir secciones de playbooks
            customized = customized.replace('[PLAYBOOK_SECTIONS]', self._get_playbook_sections())
        elif template_type == 'operations':
            # Para templates de operaciones, usar placeholders más simples
            customized = customized.replace('[TÍTULO DE LA OPERACIÓN]', f"OPERACIÓN: {theme}")
            customized = customized.replace('[VERSION]', "1.0")
            customized = customized.replace('[PORCENTAJE]', "0")
            customized = customized.replace('[Número de fase activa]', "1 - Análisis del Sistema")
            customized = customized.replace('[OPS-NN.X.N]', "OPS-01.A.1")
            customized = customized.replace('[Nombre específico de la tarea en progreso]', "Inventario de Sistema")
            customized = customized.replace('[ID-SIGUIENTE]', "OPS-01.A.2")
            customized = customized.replace('[Descripción de la siguiente tarea]', "Análisis de Dependencias")
        elif template_type == 'research':
            # Para templates de investigación
            customized = customized.replace('[TÍTULO DE LA INVESTIGACIÓN]', f"INVESTIGACIÓN: {theme}")
            customized = customized.replace('[OBJETIVO_INVESTIGACION]', f"Investigar y documentar: {theme}")
        
        return customized
    
    def _get_playbook_sections(self) -> str:
        """
        Genera secciones de playbooks para incluir en templates de desarrollo.
        
        Returns:
            String con secciones de playbooks formateadas
        """
        return """
## 📚 Playbooks de Referencia

### Playbooks Asociados
- Consultar playbooks originales en `playbooks/documentation_playbooks/`
- Completar templates correspondientes en `support-docs/`

### Estructura de Trabajo
1. Revisar playbooks originales para contexto
2. Completar templates específicos 
3. Documentar decisiones técnicas
4. Actualizar estados de progreso
"""
    
    def create_session_structure(self, date_str: str, theme: str, force: bool = False, template_type: str = 'development') -> Dict[str, any]:
        """
        Crea la estructura completa de la sesión.
        
        Returns:
            Dict con resultado de la creación
        """
        session_name = f"{date_str}_{theme}"
        session_dir = self.daily_work_dir / session_name
        
        result = {
            'success': False,
            'session_name': session_name,
            'session_dir': str(session_dir),
            'files_created': [],
            'directories_created': [],
            'warnings': [],
            'errors': []
        }
        
        try:
            # Verificar sesión existente
            existing_check = self.check_existing_session(date_str, theme)
            
            if existing_check['exists'] and not force:
                if existing_check.get('has_meaningful_content', False):
                    result['errors'].append("Sesión existe con contenido significativo. Usar --force para sobrescribir")
                    return result
                else:
                    result['warnings'].append("Sesión existe pero solo con templates. Sobrescribiendo...")
            
            # Crear directorio principal
            session_dir.mkdir(parents=True, exist_ok=True)
            result['directories_created'].append(str(session_dir))
            
            # Crear subdirectorios
            subdirs = [
                'support-docs',
                'assets',
                'assets/screenshots', 
                'assets/logs',
                'charts'
            ]
            
            for subdir in subdirs:
                subdir_path = session_dir / subdir
                subdir_path.mkdir(parents=True, exist_ok=True)
                result['directories_created'].append(str(subdir_path))
            
            # Crear archivo principal de tareas
            main_file = session_dir / f"pending-tasks-{session_name}.md"
            template_content = self.load_template_content(template_type)
            customized_content = self.customize_template_content(template_content, date_str, theme, template_type)
            
            main_file.write_text(customized_content, encoding='utf-8')
            result['files_created'].append(str(main_file))
            
            # Crear READMEs en subdirectorios
            readme_contents = {
                'support-docs': f"""# Support Documents - {theme}

Este directorio contiene templates y documentos de apoyo generados para la sesión.

## Archivos Esperados
- Templates de playbooks específicos para {theme}
- Documentos de referencia adicionales
- Notas técnicas específicas

## Uso
1. Los templates se generan con `playbook-processor.py`
2. Completar templates durante el desarrollo
3. Mantener como referencia para futuras sesiones
""",
                'assets': f"""# Assets - {session_name}

Directorio para evidencias y archivos de apoyo de la sesión.

## Estructura
- `screenshots/` - Capturas de pantalla
- `logs/` - Archivos de log y debugging
- Otros archivos de evidencia

## Buenas Prácticas
- Usar nombres descriptivos
- Organizar por tipo de archivo
- Documentar propósito en commits
"""
            }
            
            for subdir, content in readme_contents.items():
                readme_file = session_dir / subdir / 'README.md'
                readme_file.write_text(content, encoding='utf-8')
                result['files_created'].append(str(readme_file))
            
            # Actualizar tracking
            self.update_tracking(date_str, theme, result)
            
            result['success'] = True
            
        except Exception as e:
            result['errors'].append(f"Error creando sesión: {e}")
        
        return result
    
    def update_tracking(self, date_str: str, theme: str, creation_result: Dict):
        """Actualiza el archivo de tracking con la nueva sesión."""
        try:
            # Cargar tracking existente
            tracking_data = self.load_tracking_data()
            
            # Crear entrada para la nueva sesión
            session_entry = {
                'date': date_str,
                'theme': theme,
                'session_name': f"{date_str}_{theme}",
                'created_at': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'status': 'created',
                'files_created': creation_result['files_created'],
                'directories_created': creation_result['directories_created'],
                'playbooks_mapped': self.registry.THEME_PLAYBOOK_MAPPING.get(theme, []),
                'templates_generated': [],  # Se actualiza con playbook-processor
                'generator_version': '2.0_modular'
            }
            
            # Actualizar o agregar sesión
            updated = False
            for i, existing_session in enumerate(tracking_data['processed_dates']):
                if (existing_session.get('date') == date_str and 
                    existing_session.get('theme') == theme):
                    tracking_data['processed_dates'][i] = session_entry
                    updated = True
                    break
            
            if not updated:
                tracking_data['processed_dates'].append(session_entry)
            
            # Actualizar estadísticas
            if 'session_statistics' not in tracking_data:
                tracking_data['session_statistics'] = {}
            
            tracking_data['session_statistics']['total_sessions'] = len(tracking_data['processed_dates'])
            tracking_data['session_statistics']['last_session_created'] = datetime.now().isoformat()
            
            # Guardar tracking actualizado
            self.save_tracking_data(tracking_data)
            
        except Exception as e:
            ColoredOutput.warning(f"Error actualizando tracking: {e}")
    
    def load_tracking_data(self) -> Dict:
        """Carga datos de tracking existentes."""
        if self.tracking_file.exists():
            try:
                with open(self.tracking_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                ColoredOutput.warning("Archivo de tracking corrupto, creando nuevo")
        
        return {
            "processed_dates": [],
            "playbook_usage": {},
            "consistency_checks": {},
            "session_statistics": {}
        }
    
    def save_tracking_data(self, data: Dict) -> bool:
        """Guarda datos de tracking."""
        try:
            self.tracking_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.tracking_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            ColoredOutput.error(f"Error guardando tracking: {e}")
            return False
    
    def show_creation_summary(self, result: Dict, date_str: str, theme: str):
        """Muestra resumen de la creación de sesión."""
        ColoredOutput.header(f"Sesión Creada: {date_str}_{theme}")
        
        if result['success']:
            ColoredOutput.success("✅ Sesión creada exitosamente")
            
            print(f"📁 **Directorio:** `{result['session_dir']}`")
            print(f"📄 **Archivos creados:** {len(result['files_created'])}")
            print(f"📂 **Directorios creados:** {len(result['directories_created'])}")
            
            if result['warnings']:
                ColoredOutput.section("Advertencias")
                for warning in result['warnings']:
                    ColoredOutput.warning(warning)
            
            ColoredOutput.section("Próximos Pasos")
            print("1. Generar templates de apoyo:")
            print(f"   python scripts/playbook-processor.py --date='{date_str}' --theme='{theme}'")
            print("\n2. Verificar consistencia:")
            print("   python scripts/consistency-checker.py --scan-all")
            print("\n3. Al final del día, generar reporte:")
            print(f"   python scripts/report-generator.py --date='{date_str}' --theme='{theme}'")
            
        else:
            ColoredOutput.error("❌ Error creando sesión")
            for error in result['errors']:
                ColoredOutput.error(f"  • {error}")
    
    def list_available_themes(self):
        """Lista todos los temas disponibles con información."""
        ColoredOutput.header("Temas Disponibles")
        
        themes = self.registry.get_available_themes()
        
        print("🎯 **Temas configurados:**\n")
        
        for theme_info in themes:
            status_icon = "✅" if theme_info['valid'] else "❌"
            print(f"{status_icon} **{theme_info['name']}**")
            print(f"   📝 {theme_info['description']}")
            print(f"   📚 Playbooks: {', '.join(theme_info['playbooks'])}")
            print(f"   📊 Estado: {theme_info['existing_playbooks']}/{theme_info['playbook_count']} playbooks disponibles")
            
            if not theme_info['valid']:
                print(f"   ⚠️  {theme_info['missing_playbooks']} playbooks faltantes")
            
            print()
        
        print(f"**Total temas disponibles:** {len(themes)}")
        
        # Mostrar duplicados si existen
        duplicates = self.registry.detect_duplicate_templates()
        if duplicates:
            ColoredOutput.warning(f"⚠️ {len(duplicates)} grupos de templates duplicados detectados")
            ColoredOutput.info("Ejecutar consistency-checker para más detalles")