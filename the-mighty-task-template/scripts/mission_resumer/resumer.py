"""
Mission Resumer - Core Module
=============================

Consolida múltiples sesiones de trabajo en resúmenes ejecutivos con validaciones mejoradas.
"""

import os
import sys
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set

# Importar módulos compartidos
sys.path.append(str(Path(__file__).parent.parent))
from shared.template_detector import TemplateDetector
from shared.playbook_registry import PlaybookRegistry
from shared.colored_output import ColoredOutput

class MissionResumer:
    """Consolidador inteligente de sesiones con detección de templates."""
    
    def __init__(self, base_path: Optional[Path] = None):
        self.base_path = Path(base_path or Path(__file__).parent.parent.parent)
        self.daily_work_dir = self.base_path / 'daily-work'
        self.mission_resumes_dir = self.base_path / 'mission-resumes'
        
        # Crear directorio mission-resumes si no existe
        self.mission_resumes_dir.mkdir(exist_ok=True)
        
        # Inicializar estructura completa automáticamente
        self._initialize_mission_resumes_structure()
        
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
    
    def scan_available_sessions(self, theme_filter: Optional[str] = None) -> List[Dict]:
        """
        Escanea sesiones disponibles para consolidación.
        
        Returns:
            Lista de sesiones con metadatos y análisis de contenido
        """
        sessions = []
        
        if not self.daily_work_dir.exists():
            all_sessions = self.scan_sessions(theme_filter=theme_filter)
            sessions = [s for s in all_sessions if s['has_meaningful_content']]
        else:
            for session_dir in self.daily_work_dir.glob('*'):
                if session_dir.is_dir():
                    # Extraer tema del nombre del directorio
                    parts = session_dir.name.split('_', 1)
                    if len(parts) >= 2:
                        session_theme = parts[1]
                        if theme_filter and session_theme != theme_filter:
                            continue
                        
                        # Parsear nombre de sesión
                        session_info = self._parse_session_name(session_dir.name)
                        if not session_info:
                            continue
                        
                        # Analizar contenido de la sesión
                        content_analysis = self._analyze_session_content(session_dir)
                        
                        session_data = {
                            'directory': session_dir,
                            'name': session_dir.name,
                            'date': session_info['date'],
                            'theme': session_info['theme'],
                            'content_analysis': content_analysis,
                            'has_meaningful_content': content_analysis['has_real_content'],
                            'completion_percentage': content_analysis['completion_percentage'],
                            'files_count': content_analysis['files_count'],
                            'templates_count': content_analysis['templates_count']
                        }
                        
                        sessions.append(session_data)
                    session_data = {
                        'directory': session_dir,
                        'name': session_dir.name,
                        'date': session_info['date'],
                        'theme': session_info['theme'],
                        'content_analysis': content_analysis,
                        'has_meaningful_content': content_analysis['has_real_content'],
                        'completion_percentage': content_analysis['completion_percentage'],
                        'files_count': content_analysis['files_count'],
                        'templates_count': content_analysis['templates_count']
                    }
                    
                    sessions.append(session_data)
            
            session_data = {
                'directory': session_dir,
                'name': session_dir.name,
                'date': session_info['date'],
                'theme': session_info['theme'],
                'content_analysis': content_analysis,
                'has_meaningful_content': content_analysis['has_real_content'],
                'completion_percentage': content_analysis['completion_percentage'],
                'files_count': content_analysis['files_count'],
                'templates_count': content_analysis['templates_count']
            }
            
            sessions.append(session_data)
        
        # Ordenar por fecha
        sessions.sort(key=lambda x: x['date'])
        return sessions
    
    def _parse_session_name(self, session_name: str) -> Optional[Dict]:
        """Parsea el nombre de sesión para extraer fecha y tema."""
        try:
            parts = session_name.split('_', 1)
            if len(parts) != 2:
                return None
            
            date_str, theme = parts
            # Validar formato de fecha
            datetime.strptime(date_str, '%Y-%m-%d')
            
            return {
                'date': date_str,
                'theme': theme
            }
        except (ValueError, IndexError):
            return None
    
    def _analyze_session_content(self, session_dir: Path) -> Dict:
        """
        Analiza el contenido de una sesión para determinar calidad y completitud.
        
        Returns:
            Dict con análisis detallado del contenido
        """
        analysis = {
            'has_real_content': False,
            'completion_percentage': 0,
            'files_count': 0,
            'templates_count': 0,
            'meaningful_files': [],
            'template_files': [],
            'assets_count': 0,
            'quality_score': 0
        }
        
        # Analizar archivo principal
        main_files = list(session_dir.glob('pending-tasks-*.md'))
        if main_files:
            main_file = main_files[0]
            try:
                content = main_file.read_text(encoding='utf-8')
                content_quality = self.detector.analyze_content_quality(content)
                
                analysis['files_count'] += 1
                
                if content_quality['type'] != 'template':
                    analysis['has_real_content'] = True
                    analysis['meaningful_files'].append(str(main_file))
                    analysis['completion_percentage'] = content_quality['completion_percentage']
                    analysis['quality_score'] += content_quality['completion_percentage']
                else:
                    analysis['template_files'].append(str(main_file))
                    analysis['templates_count'] += 1
                    
            except Exception as e:
                ColoredOutput.warning(f"Error analizando {main_file}: {e}")
        
        # Analizar support-docs
        support_docs_dir = session_dir / 'support-docs'
        if support_docs_dir.exists():
            for doc_file in support_docs_dir.glob('*.md'):
                try:
                    content = doc_file.read_text(encoding='utf-8')
                    analysis['files_count'] += 1
                    
                    if self.detector.is_template_content(content):
                        analysis['template_files'].append(str(doc_file))
                        analysis['templates_count'] += 1
                    else:
                        analysis['meaningful_files'].append(str(doc_file))
                        analysis['has_real_content'] = True
                        # Calcular score adicional por documentos completados
                        doc_quality = self.detector.analyze_content_quality(content)
                        analysis['quality_score'] += doc_quality['completion_percentage'] * 0.5
                        
                except Exception as e:
                    ColoredOutput.warning(f"Error analizando {doc_file}: {e}")
        
        # Contar assets
        assets_dir = session_dir / 'assets'
        if assets_dir.exists():
            analysis['assets_count'] = len([f for f in assets_dir.rglob('*') if f.is_file()])
            if analysis['assets_count'] > 0:
                analysis['has_real_content'] = True
                analysis['quality_score'] += min(analysis['assets_count'] * 5, 20)  # Max 20 puntos por assets
        
        # Normalizar quality_score (0-100)
        if analysis['files_count'] > 0:
            analysis['quality_score'] = min(analysis['quality_score'] / analysis['files_count'], 100)
        
        return analysis
    
    def validate_sessions_for_consolidation(self, sessions: List[Dict]) -> Dict:
        """
        Valida que las sesiones sean apropiadas para consolidación.
        
        Returns:
            Dict con resultado de validación
        """
        validation = {
            'valid': True,
            'warnings': [],
            'errors': [],
            'recommendations': []
        }
        
        if not sessions:
            validation['valid'] = False
            validation['errors'].append("No hay sesiones para consolidar")
            return validation
        
        # Verificar que haya contenido significativo
        meaningful_sessions = [s for s in sessions if s['has_meaningful_content']]
        if not meaningful_sessions:
            validation['valid'] = False
            validation['errors'].append("Ninguna sesión contiene trabajo significativo")
            validation['recommendations'].append("Completar al menos una sesión antes de consolidar")
            return validation
        
        # Verificar consistencia de temas
        themes = set(s['theme'] for s in sessions)
        if len(themes) > 1:
            validation['warnings'].append(f"Múltiples temas detectados: {', '.join(themes)}")
            validation['recommendations'].append("Considerar consolidar por tema separadamente")
        
        # Verificar duplicación potencial
        duplicate_dates = {}
        for session in sessions:
            date = session['date']
            if date in duplicate_dates:
                duplicate_dates[date].append(session['name'])
            else:
                duplicate_dates[date] = [session['name']]
        
        for date, session_names in duplicate_dates.items():
            if len(session_names) > 1:
                validation['warnings'].append(f"Múltiples sesiones en {date}: {', '.join(session_names)}")
        
        # Verificar calidad promedio
        avg_quality = sum(s['completion_percentage'] for s in meaningful_sessions) / len(meaningful_sessions)
        if avg_quality < 30:
            validation['warnings'].append(f"Calidad promedio baja: {avg_quality:.1f}%")
            validation['recommendations'].append("Completar más contenido antes de consolidar")
        
        return validation
    
    def create_consolidated_playbook(self, sessions: List[Dict], output_name: str) -> Dict:
        """
        Crea un playbook consolidado inteligente evitando duplicación de templates.
        
        Returns:
            Dict con resultado de la consolidación
        """
        result = {
            'success': False,
            'output_file': None,
            'sections_merged': 0,
            'templates_excluded': 0,
            'content_sources': [],
            'warnings': [],
            'errors': []
        }
        
        try:
            # Archivo de salida en docs/ usando tema como nombre único
            theme_name = sessions[0]['theme'] if sessions else output_name
            output_file = self.mission_resumes_dir / 'docs' / f"{theme_name}.md"
            
            # Generar contenido consolidado
            consolidated_content = self._generate_consolidated_content(sessions, output_name)
            
            # Escribir archivo consolidado
            output_file.write_text(consolidated_content, encoding='utf-8')
            result['output_file'] = str(output_file)
            
            # Consolidar todos los assets, charts, web-guides, etc.
            self._consolidate_all_assets(sessions, result)
            
            # Generar log de consolidación en mission-resumes
            self._generate_consolidation_log(sessions, self.mission_resumes_dir, result)
            
            # Actualizar tracking
            self._update_consolidation_tracking(sessions, output_name, result)
            
            result['success'] = True
            
        except Exception as e:
            result['errors'].append(f"Error en consolidación: {e}")
        
        return result
    
    def _generate_consolidated_content(self, sessions: List[Dict], output_name: str) -> str:
        """Genera el contenido consolidado inteligente."""
        
        # Header del documento consolidado
        content_parts = []
        content_parts.append(f"# {output_name} - Resumen Consolidado")
        content_parts.append("")
        content_parts.append(f"**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        content_parts.append(f"**Sesiones consolidadas:** {len(sessions)}")
        content_parts.append("")
        
        # Resumen ejecutivo
        content_parts.append("## 📊 Resumen Ejecutivo")
        content_parts.append("")
        
        meaningful_sessions = [s for s in sessions if s['has_meaningful_content']]
        total_files = sum(s['files_count'] for s in sessions)
        total_templates = sum(s['templates_count'] for s in sessions)
        avg_completion = sum(s['completion_percentage'] for s in meaningful_sessions) / len(meaningful_sessions) if meaningful_sessions else 0
        
        content_parts.append(f"- **Sesiones procesadas:** {len(sessions)}")
        content_parts.append(f"- **Sesiones con contenido:** {len(meaningful_sessions)}")
        content_parts.append(f"- **Archivos totales:** {total_files}")
        content_parts.append(f"- **Templates excluidos:** {total_templates}")
        content_parts.append(f"- **Completitud promedio:** {avg_completion:.1f}%")
        content_parts.append("")
        
        # Índice de sesiones
        content_parts.append("## 📋 Sesiones Incluidas")
        content_parts.append("")
        
        for i, session in enumerate(sessions, 1):
            status_icon = "✅" if session['has_meaningful_content'] else "⚠️"
            content_parts.append(f"{i}. {status_icon} **{session['name']}**")
            content_parts.append(f"   - Fecha: {session['date']}")
            content_parts.append(f"   - Tema: {session['theme']}")
            content_parts.append(f"   - Completitud: {session['completion_percentage']:.1f}%")
            content_parts.append(f"   - Archivos: {session['files_count']} ({session['templates_count']} templates)")
            content_parts.append("")
        
        # Consolidar contenido significativo por sesión
        content_parts.append("## 📝 Contenido Consolidado")
        content_parts.append("")
        
        for session in meaningful_sessions:
            content_parts.append(f"### {session['name']}")
            content_parts.append("")
            
            # Extraer contenido no-template del archivo principal
            main_files = list(session['directory'].glob('pending-tasks-*.md'))
            if main_files:
                try:
                    main_content = main_files[0].read_text(encoding='utf-8')
                    filtered_content = self._extract_meaningful_content(main_content)
                    if filtered_content.strip():
                        content_parts.append(filtered_content)
                        content_parts.append("")
                except Exception as e:
                    content_parts.append(f"⚠️ Error procesando contenido: {e}")
                    content_parts.append("")
            
            # Incluir documentos de apoyo completados
            for meaningful_file in session['content_analysis']['meaningful_files']:
                if 'support-docs' in meaningful_file:
                    try:
                        file_path = Path(meaningful_file)
                        doc_content = file_path.read_text(encoding='utf-8')
                        filtered_doc = self._extract_meaningful_content(doc_content)
                        if filtered_doc.strip():
                            content_parts.append(f"#### {file_path.name}")
                            content_parts.append("")
                            content_parts.append(filtered_doc)
                            content_parts.append("")
                    except Exception as e:
                        content_parts.append(f"⚠️ Error procesando {meaningful_file}: {e}")
                        content_parts.append("")
        
        # Sección de web-guides utilizadas
        web_guides_used = self._extract_web_guides_references(sessions)
        if web_guides_used:
            content_parts.append("## 🌐 Web-Guides Utilizadas")
            content_parts.append("")
            content_parts.append("Las siguientes web-guides fueron creadas durante estas sesiones:")
            content_parts.append("")
            for guide in web_guides_used:
                content_parts.append(f"- **{guide['name']}** - {guide['title']}")
                content_parts.append(f"  - Archivo: `{guide['file_path']}`")
                content_parts.append(f"  - Descripción: {guide['description']}")
                content_parts.append(f"  - Usado en: {', '.join(guide['sessions_used'])}")
                content_parts.append("")
        
        # Sección de guías operacionales utilizadas
        operational_guides_used = self._extract_operational_guides_references(sessions)
        if operational_guides_used:
            content_parts.append("## 🔧 Guías Operacionales Utilizadas")
            content_parts.append("")
            content_parts.append("Las siguientes guías operacionales fueron referenciadas o utilizadas durante estas sesiones:")
            content_parts.append("")
            for guide in operational_guides_used:
                content_parts.append(f"- **{guide['name']}** - {guide['title']}")
                content_parts.append(f"  - Archivo: `operational-guides/{guide['filename']}`")
                content_parts.append(f"  - Tags: {', '.join(guide['tags'])}")
                content_parts.append(f"  - Usado en: {', '.join(guide['sessions'])}")
                content_parts.append("")
        
        # Sección de assets si existen
        total_assets = sum(s['content_analysis']['assets_count'] for s in sessions)
        if total_assets > 0:
            content_parts.append("## 📎 Assets y Evidencias")
            content_parts.append("")
            content_parts.append(f"Se han copiado {total_assets} archivos de assets a este resumen.")
            content_parts.append("Ver directorio `assets/` para capturas, logs y otros archivos de evidencia.")
            content_parts.append("")
        
        # Footer con metadatos
        content_parts.append("---")
        content_parts.append("")
        content_parts.append("## 🔍 Metadatos de Consolidación")
        content_parts.append("")
        content_parts.append(f"- **Herramienta:** Mission Resumer v2.0")
        content_parts.append(f"- **Detección de templates:** Habilitada")
        content_parts.append(f"- **Filtrado inteligente:** Activo")
        content_parts.append(f"- **Sesiones origen:** {', '.join(s['name'] for s in sessions)}")
        content_parts.append("")
        
        return "\n".join(content_parts)
    
    def _extract_meaningful_content(self, content: str) -> str:
        """
        Extrae solo el contenido significativo, filtrando templates y placeholders.
        """
        lines = content.split('\n')
        meaningful_lines = []
        
        for line in lines:
            # Filtrar líneas de template obvias
            if self.detector._is_template_line(line.strip()):
                continue
            
            # Filtrar secciones vacías o de template
            if self.detector._is_placeholder_section(line.strip()):
                continue
            
            meaningful_lines.append(line)
        
        # Limpiar líneas vacías excesivas
        cleaned_content = '\n'.join(meaningful_lines)
        
        # Eliminar bloques de múltiples líneas vacías
        import re
        cleaned_content = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_content)
        
        return cleaned_content.strip()
    
    def _initialize_mission_resumes_structure(self):
        """Pre-carga automáticamente toda la estructura necesaria en mission-resumes/."""
        try:
            # 1. Crear carpetas base
            folders = [
                'assets', 
                'assets/logs', 
                'assets/screenshots', 
                'charts', 
                'web-guides', 
                'support-docs',
                'docs'
            ]
            
            for folder in folders:
                folder_path = self.mission_resumes_dir / folder
                folder_path.mkdir(parents=True, exist_ok=True)
            
            # 2. Copiar templates DOC vacíos desde playbooks/documentation_playbooks/
            doc_templates_dir = self.base_path / 'playbooks' / 'documentation_playbooks'
            
            if doc_templates_dir.exists():
                for doc_file in doc_templates_dir.glob('DOC*.md'):
                    dest_file = self.mission_resumes_dir / doc_file.name
                    if not dest_file.exists():  # Solo si no existe
                        shutil.copy2(doc_file, dest_file)
            
            # 3. Copiar templates DOC adicionales desde playbooks/ (raíz)
            playbooks_dir = self.base_path / 'playbooks'
            if playbooks_dir.exists():
                for doc_file in playbooks_dir.glob('DOC*.md'):
                    dest_file = self.mission_resumes_dir / doc_file.name
                    if not dest_file.exists():  # Solo si no existe
                        shutil.copy2(doc_file, dest_file)
                        
        except Exception as e:
            # No fallar si hay problemas con la inicialización
            pass
    
    def _extract_web_guides_references(self, sessions: List[Dict]) -> List[Dict]:
        """
        Extrae referencias a web-guides de las sesiones.
        
        Returns:
            Lista de web-guides referenciadas con metadatos
        """
        web_guides_used = {}
        
        # Buscar web-guides en cada sesión
        for session in sessions:
            session_name = session['name']
            web_guides_dir = session['directory'] / 'web-guides'
            
            if web_guides_dir.exists():
                for guide_file in web_guides_dir.glob('*.md'):
                    try:
                        content = guide_file.read_text(encoding='utf-8')
                        guide_name = guide_file.stem
                        
                        # Extraer metadatos del contenido
                        lines = content.split('\n')
                        title = guide_name
                        description = ""
                        
                        for line in lines[:10]:  # Buscar en las primeras líneas
                            if line.startswith('# '):
                                title = line[2:].strip()
                            elif line.startswith('**Descripción:**') or line.startswith('**Description:**'):
                                description = line.split(':', 1)[1].strip()
                        
                        web_guides_used[guide_name] = {
                            'name': guide_name,
                            'title': title,
                            'description': description,
                            'file_path': str(guide_file.relative_to(self.base_path)),
                            'sessions_used': [session_name],
                            'size': len(content)
                        }
                        
                    except Exception:
                        pass
        
        return list(web_guides_used.values())
    
    def _extract_operational_guides_references(self, sessions: List[Dict]) -> List[Dict]:
        """
        Extrae referencias a guías operacionales de las sesiones.
        
        Returns:
            Lista de guías operacionales referenciadas con metadatos
        """
        guides_used = {}
        
        # Cargar tracking de guías operacionales
        operational_guides_tracking = self.base_path / 'operational-guides' / '.operational-guides-tracking.json'
        available_guides = {}
        
        if operational_guides_tracking.exists():
            try:
                with open(operational_guides_tracking, 'r', encoding='utf-8') as f:
                    tracking_data = json.load(f)
                    for guide in tracking_data.get('guides', []):
                        available_guides[guide['name']] = guide
            except Exception:
                pass
        
        # Buscar referencias en el contenido de las sesiones
        for session in sessions:
            session_name = session['name']
            
            # Buscar en archivo principal
            main_files = list(session['directory'].glob('pending-tasks-*.md'))
            if main_files:
                try:
                    content = main_files[0].read_text(encoding='utf-8')
                    self._scan_content_for_guides(content, session_name, available_guides, guides_used)
                except Exception:
                    pass
            
            # Buscar en support-docs
            support_docs_dir = session['directory'] / 'support-docs'
            if support_docs_dir.exists():
                for doc_file in support_docs_dir.glob('*.md'):
                    try:
                        content = doc_file.read_text(encoding='utf-8')
                        self._scan_content_for_guides(content, session_name, available_guides, guides_used)
                    except Exception:
                        pass
        
        # Convertir a lista y agregar información de sesiones
        result = []
        for guide_name, guide_info in guides_used.items():
            if guide_name in available_guides:
                guide_data = available_guides[guide_name].copy()
                guide_data['sessions'] = guide_info['sessions']
                result.append(guide_data)
        
        return result
    
    def _consolidate_all_assets(self, sessions: List[Dict], result: Dict):
        """Consolida assets, charts, web-guides de todas las sesiones."""
        assets_consolidated = 0
        
        try:
            for session in sessions:
                session_dir = session['directory']
                session_name = session['name']
                
                # Consolidar assets
                assets_consolidated += self._consolidate_folder(session_dir / 'assets', 'assets', session_name)
                
                # Consolidar charts
                assets_consolidated += self._consolidate_folder(session_dir / 'charts', 'charts', session_name)
                
                # Consolidar web-guides
                assets_consolidated += self._consolidate_folder(session_dir / 'web-guides', 'web-guides', session_name)
                
                # Consolidar support-docs
                assets_consolidated += self._consolidate_folder(session_dir / 'support-docs', 'support-docs', session_name)
            
            if assets_consolidated > 0:
                result['assets_consolidated'] = assets_consolidated
                
        except Exception as e:
            result['warnings'].append(f"Error consolidando assets: {e}")
    
    def _consolidate_folder(self, source_dir: Path, target_folder: str, session_name: str) -> int:
        """Consolida una carpeta específica manteniendo organización."""
        files_copied = 0
        
        if not source_dir.exists():
            return 0
        
        try:
            target_dir = self.mission_resumes_dir / target_folder / session_name
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # Copiar todos los archivos manteniendo estructura
            for file_path in source_dir.rglob('*'):
                if file_path.is_file():
                    try:
                        relative_path = file_path.relative_to(source_dir)
                        dest_path = target_dir / relative_path
                        dest_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # Solo copiar si no existe o es más reciente
                        if not dest_path.exists() or file_path.stat().st_mtime > dest_path.stat().st_mtime:
                            shutil.copy2(file_path, dest_path)
                            files_copied += 1
                            
                    except Exception:
                        continue
                        
        except Exception:
            pass
            
        return files_copied
    
    def _scan_content_for_guides(self, content: str, session_name: str, available_guides: Dict, guides_used: Dict):
        """Escanea contenido buscando referencias a guías operacionales."""
        # Buscar menciones directas de nombres de guías
        for guide_name in available_guides.keys():
            # Buscar por nombre exacto
            if guide_name in content.lower():
                if guide_name not in guides_used:
                    guides_used[guide_name] = {'sessions': []}
                if session_name not in guides_used[guide_name]['sessions']:
                    guides_used[guide_name]['sessions'].append(session_name)
        
        # Buscar patrones de referencias a archivos de guías
        guide_patterns = [
            r'operational-guides/([a-zA-Z0-9-_]+)\.md',
            r'guía\s+([a-zA-Z0-9-_]+)',
            r'guide\s+([a-zA-Z0-9-_]+)',
            r'siguiendo\s+([a-zA-Z0-9-_]+)',
            r'usando\s+([a-zA-Z0-9-_]+)'
        ]
        
        for pattern in guide_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                guide_name = match.lower().replace('_', '-')
                if guide_name in available_guides:
                    if guide_name not in guides_used:
                        guides_used[guide_name] = {'sessions': []}
                    if session_name not in guides_used[guide_name]['sessions']:
                        guides_used[guide_name]['sessions'].append(session_name)
    
    def _copy_relevant_assets(self, sessions: List[Dict], output_dir: Path, result: Dict):
        """Copia assets relevantes de las sesiones al directorio consolidado."""
        # Crear assets directory si hay assets para copiar
        output_assets_dir = output_dir / 'assets'
        assets_copied = 0
        
        for session in sessions:
            session_assets_dir = session['directory'] / 'assets'
            if session_assets_dir.exists():
                output_assets_dir.mkdir(exist_ok=True)
                
                for asset_file in session_assets_dir.rglob('*'):
                    if asset_file.is_file():
                        try:
                            # Crear estructura de directorios en destino con timestamp
                            relative_path = asset_file.relative_to(session_assets_dir)
                            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                            dest_path = output_assets_dir / f"{session['name']}-{timestamp}" / relative_path
                            dest_path.parent.mkdir(parents=True, exist_ok=True)
                            
                            # Copiar archivo
                            shutil.copy2(asset_file, dest_path)
                            assets_copied += 1
                        except Exception as e:
                            result['warnings'].append(f"Error copiando {asset_file}: {e}")
        
        if assets_copied > 0:
            result['assets_copied'] = assets_copied
    
    def _generate_consolidation_log(self, sessions: List[Dict], output_dir: Path, result: Dict):
        """Genera log detallado de la consolidación."""
        log_file = output_dir / f'consolidation-log-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
        
        log_data = {
            'consolidation_timestamp': datetime.now().isoformat(),
            'sessions_processed': len(sessions),
            'sessions_with_content': len([s for s in sessions if s['has_meaningful_content']]),
            'total_files_analyzed': sum(s['files_count'] for s in sessions),
            'templates_excluded': sum(s['templates_count'] for s in sessions),
            'average_completion': sum(s['completion_percentage'] for s in sessions if s['has_meaningful_content']) / len([s for s in sessions if s['has_meaningful_content']]) if any(s['has_meaningful_content'] for s in sessions) else 0,
            'session_details': [
                {
                    'name': s['name'],
                    'date': s['date'],
                    'theme': s['theme'],
                    'has_content': s['has_meaningful_content'],
                    'completion_percentage': s['completion_percentage'],
                    'files_count': s['files_count'],
                    'templates_count': s['templates_count'],
                    'meaningful_files': s['content_analysis']['meaningful_files'],
                    'template_files': s['content_analysis']['template_files']
                }
                for s in sessions
            ],
            'consolidation_result': result
        }
        
        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
            result['log_file'] = str(log_file)
        except Exception as e:
            result['warnings'].append(f"Error generando log: {e}")
    
    def _update_consolidation_tracking(self, sessions: List[Dict], output_name: str, result: Dict):
        """Actualiza el tracking global con información de consolidación."""
        try:
            tracking_file = self.daily_work_dir / '.tracking.json'
            
            # Cargar tracking existente
            if tracking_file.exists():
                with open(tracking_file, 'r', encoding='utf-8') as f:
                    tracking_data = json.load(f)
            else:
                tracking_data = {"processed_dates": [], "consolidations": []}
            
            # Agregar información de consolidación
            if 'consolidations' not in tracking_data:
                tracking_data['consolidations'] = []
            
            consolidation_entry = {
                'name': output_name,
                'timestamp': datetime.now().isoformat(),
                'sessions_included': [s['name'] for s in sessions],
                'sessions_count': len(sessions),
                'meaningful_sessions': len([s for s in sessions if s['has_meaningful_content']]),
                'output_file': result.get('output_file'),
                'success': result['success']
            }
            
            tracking_data['consolidations'].append(consolidation_entry)
            
            # Guardar tracking actualizado
            with open(tracking_file, 'w', encoding='utf-8') as f:
                json.dump(tracking_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            result['warnings'].append(f"Error actualizando tracking: {e}")
    
    def show_consolidation_summary(self, result: Dict, sessions: List[Dict], output_name: str):
        """Muestra resumen de la consolidación realizada."""
        ColoredOutput.header(f"Consolidación Completada: {output_name}")
        
        if result['success']:
            ColoredOutput.success("✅ Consolidación exitosa")
            
            print(f"📄 **Archivo generado:** `{result['output_file']}`")
            print(f"📊 **Sesiones procesadas:** {len(sessions)}")
            
            meaningful_sessions = [s for s in sessions if s['has_meaningful_content']]
            print(f"✅ **Con contenido significativo:** {len(meaningful_sessions)}")
            print(f"⚠️  **Solo templates:** {len(sessions) - len(meaningful_sessions)}")
            
            if 'assets_copied' in result:
                print(f"📎 **Assets copiados:** {result['assets_copied']}")
            
            if 'log_file' in result:
                print(f"📋 **Log detallado:** `{result['log_file']}`")
            
            if result['warnings']:
                ColoredOutput.section("Advertencias")
                for warning in result['warnings']:
                    ColoredOutput.warning(warning)
            
            ColoredOutput.section("Próximos Pasos")
            print("1. Revisar el archivo consolidado generado")
            print("2. Verificar assets copiados si los hay")
            print("3. Considerar ejecutar consistency-checker para validación")
            
        else:
            ColoredOutput.error("❌ Error en consolidación")
            for error in result['errors']:
                ColoredOutput.error(f"  • {error}")
    
    def list_available_sessions(self, theme_filter: Optional[str] = None):
        """Lista todas las sesiones disponibles para consolidación."""
        ColoredOutput.header("Sesiones Disponibles para Consolidación")
        
        sessions = self.scan_available_sessions(theme_filter)
        
        if not sessions:
            ColoredOutput.warning("No se encontraron sesiones disponibles")
            return
        
        # Agrupar por tema
        sessions_by_theme = {}
        for session in sessions:
            theme = session['theme']
            if theme not in sessions_by_theme:
                sessions_by_theme[theme] = []
            sessions_by_theme[theme].append(session)
        
        for theme, theme_sessions in sessions_by_theme.items():
            ColoredOutput.section(f"Tema: {theme}")
            
            meaningful_count = len([s for s in theme_sessions if s['has_meaningful_content']])
            print(f"📊 **Total:** {len(theme_sessions)} sesiones ({meaningful_count} con contenido)")
            print()
            
            for session in theme_sessions:
                status_icon = "✅" if session['has_meaningful_content'] else "⚠️"
                quality_bar = "█" * int(session['completion_percentage'] / 10) + "░" * (10 - int(session['completion_percentage'] / 10))
                
                print(f"{status_icon} **{session['name']}**")
                print(f"   📅 {session['date']} | 📊 {session['completion_percentage']:.1f}% [{quality_bar}]")
                print(f"   📄 {session['files_count']} archivos ({session['templates_count']} templates)")
                print()
        
        print(f"**Total general:** {len(sessions)} sesiones disponibles")