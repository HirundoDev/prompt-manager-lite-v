"""
Playbook Processor - Clase Principal
====================================

Clase principal que maneja el procesamiento de playbooks y generación de templates.
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path

from .utils import ColoredOutput, THEME_PLAYBOOK_MAPPING, PLAYBOOK_FILE_MAPPING
from .templates import get_template_function

class PlaybookProcessor:
    """Procesador de playbooks que genera templates específicos."""
    
    def __init__(self, base_path=None):
        self.base_path = Path(base_path or os.getcwd())
        self.playbooks_dir = self.base_path / 'playbooks' / 'documentation_playbooks'
        self.main_playbooks_dir = self.base_path / 'playbooks'
        self.daily_work_dir = self.base_path / 'daily-work'
        self.tracking_file = self.daily_work_dir / '.tracking.json'
        
        # Verificar estructura del proyecto (buscar archivos indicadores)
        if not any([
            (self.base_path / 'README.md').exists(),
            (self.base_path / 'template-pendingtask.md').exists(),
            (self.base_path / 'scripts').exists()
        ]):
            ColoredOutput.error("No estás en el directorio raíz de The Mighty Task")
            ColoredOutput.info("Ejecuta este script desde el directorio que contiene scripts/ y README.md")
            sys.exit(1)
        
        if not self.playbooks_dir.exists():
            ColoredOutput.error(f"Directorio de playbooks no encontrado: {self.playbooks_dir}")
            sys.exit(1)
    
    def load_tracking_data(self):
        """Carga los datos de tracking existentes."""
        if self.tracking_file.exists():
            try:
                with open(self.tracking_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                ColoredOutput.warning("Archivo de tracking corrupto o no encontrado")
        
        return {"processed_dates": [], "playbook_usage": {}, "consistency_checks": {}}
    
    def save_tracking_data(self, data):
        """Guarda los datos de tracking."""
        try:
            self.tracking_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.tracking_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            ColoredOutput.error(f"Error guardando tracking: {e}")
            return False
    
    def find_session_directory(self, date_str, theme):
        """Encuentra el directorio de sesión basado en fecha y tema."""
        session_name = f"{date_str}_{theme}"
        session_dir = self.daily_work_dir / session_name
        
        if not session_dir.exists():
            ColoredOutput.error(f"Sesión no encontrada: {session_name}")
            ColoredOutput.info("Ejecuta primero: python scripts/generate-daily.py")
            return None
        
        support_docs_dir = session_dir / 'support-docs'
        if not support_docs_dir.exists():
            ColoredOutput.error(f"Directorio support-docs no encontrado en: {session_dir}")
            return None
        
        return session_dir
    
    def get_available_playbooks(self):
        """Obtiene la lista de playbooks disponibles."""
        available = []
        for playbook_code, filename in PLAYBOOK_FILE_MAPPING.items():
            # Buscar primero en documentation_playbooks, luego en playbooks principal
            playbook_path = self.playbooks_dir / filename
            if not playbook_path.exists():
                playbook_path = self.main_playbooks_dir / filename
            
            if playbook_path.exists():
                available.append((playbook_code, filename, playbook_path))
            else:
                ColoredOutput.warning(f"Playbook no encontrado: {filename}")
        
        return available
    
    def load_playbook(self, playbook_path):
        """Carga y parsea un playbook desde archivo."""
        try:
            with open(playbook_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return self.parse_playbook_structure(content, playbook_path.name)
        except Exception as e:
            ColoredOutput.error(f"Error cargando playbook {playbook_path}: {e}")
            return None
    
    def parse_playbook_structure(self, content, filename):
        """Parsea la estructura de un playbook y extrae información relevante."""
        
        # Extraer metadatos del header
        metadata = self.extract_metadata(content)
        
        # Extraer estructura de headers
        headers = self.extract_header_structure(content)
        
        # Extraer secciones principales
        sections = self.extract_sections(content, headers)
        
        return {
            'filename': filename,
            'metadata': metadata,
            'headers': headers,
            'sections': sections,
            'content_length': len(content),
            'parsed_at': datetime.now().isoformat()
        }
    
    def extract_metadata(self, content):
        """Extrae metadatos del header del playbook."""
        metadata = {
            'title': 'Sin título',
            'description': 'Sin descripción',
            'version': '1.0',
            'author': 'The Mighty Task',
            'creation_date': None,
            'last_update': None
        }
        
        # Buscar título (primera línea con #)
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1).strip()
        
        # Buscar descripción en las primeras líneas
        lines = content.split('\n')
        for i, line in enumerate(lines[:20]):  # Solo primeras 20 líneas
            if line.startswith('**Descripción:**') or line.startswith('**Description:**'):
                if i + 1 < len(lines):
                    metadata['description'] = lines[i + 1].strip()
                break
            elif 'descripción' in line.lower() and not line.startswith('#'):
                metadata['description'] = line.strip()
                break
        
        # Buscar versión
        version_match = re.search(r'\*\*Versión:\*\*\s*(.+)', content, re.IGNORECASE)
        if version_match:
            metadata['version'] = version_match.group(1).strip()
        
        return metadata
    
    def extract_header_structure(self, content):
        """Extrae la estructura jerárquica de headers."""
        headers = []
        
        # Patrón para headers de markdown (# ## ### etc.)
        header_pattern = r'^(#{1,6})\s+(.+)$'
        
        for match in re.finditer(header_pattern, content, re.MULTILINE):
            level = len(match.group(1))  # Número de #
            title = match.group(2).strip()
            position = match.start()
            
            headers.append({
                'level': level,
                'title': title,
                'position': position,
                'anchor': self.create_anchor(title)
            })
        
        return headers
    
    def create_anchor(self, title):
        """Crea un anchor para navegación interna."""
        # Convertir a formato anchor de markdown
        anchor = title.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)  # Quitar caracteres especiales
        anchor = re.sub(r'\s+', '-', anchor)  # Espacios a guiones
        return anchor
    
    def extract_sections(self, content, headers):
        """Extrae el contenido de cada sección basado en headers."""
        sections = []
        
        for i, header in enumerate(headers):
            start_pos = header['position']
            
            # Encontrar el final de esta sección (siguiente header del mismo nivel o superior)
            end_pos = len(content)
            for next_header in headers[i + 1:]:
                if next_header['level'] <= header['level']:
                    end_pos = next_header['position']
                    break
            
            # Extraer contenido de la sección
            section_content = content[start_pos:end_pos].strip()
            
            # Analizar tipo de contenido
            content_analysis = self.analyze_section_content(section_content)
            
            sections.append({
                'header': header,
                'content': section_content,
                'length': len(section_content),
                'analysis': content_analysis
            })
        
        return sections
    
    def analyze_section_content(self, section_content):
        """Analiza el tipo de contenido en una sección."""
        analysis = {
            'has_code_blocks': bool(re.search(r'```', section_content)),
            'has_tables': bool(re.search(r'\|.*\|', section_content)),
            'has_lists': bool(re.search(r'^[\*\-\+]\s', section_content, re.MULTILINE)),
            'has_checkboxes': bool(re.search(r'- \[ \]', section_content)),
            'has_links': bool(re.search(r'\[.+\]\(.+\)', section_content)),
            'has_images': bool(re.search(r'!\[.+\]\(.+\)', section_content)),
            'paragraph_count': len([p for p in section_content.split('\n\n') if p.strip()]),
            'content_type': 'mixed'
        }
        
        # Determinar tipo predominante de contenido
        if analysis['has_code_blocks']:
            analysis['content_type'] = 'code-heavy'
        elif analysis['has_tables']:
            analysis['content_type'] = 'table-heavy'
        elif analysis['has_lists'] or analysis['has_checkboxes']:
            analysis['content_type'] = 'list-heavy'
        elif analysis['paragraph_count'] > 3:
            analysis['content_type'] = 'text-heavy'
        
        return analysis
    
    def determine_template_type(self, filename):
        """Determina el tipo de template según el DOC"""
        doc_mapping = {
            'DOC003-DesignSystem.md': 'design_system',
            'DOC004-FrontendArchitecture.md': 'frontend_architecture',
            'DOC005-FrontendDependencies.md': 'frontend_dependencies',
            'DOC006-BackendArchitecture.md': 'backend_architecture',
            'DOC007-BackendDependencies.md': 'backend_dependencies',
            'DOC008-APISpecification.md': 'api_specification',
            'DOC009-DataModel.md': 'data_model',
            'DOC010-Deployment.md': 'deployment',
            'DOC011-TestingStrategy.md': 'testing_strategy',
            'DOC019-CLI-Command-Reference.md': 'cli_reference',
            'DOC035-ErrorTracking.md': 'error_tracking',
            'DOC036-ErrorCodes.md': 'error_codes'
        }
        return doc_mapping.get(filename, 'generic')
    
    def generate_universal_template(self, theme, date_str, filename):
        """Genera un template universal según el tipo"""
        template_type = self.determine_template_type(filename)
        template_func = get_template_function(template_type)
        return template_func(theme, date_str, filename)
    
    def process_theme_playbooks(self, theme, date_str):
        """Procesa todos los playbooks relevantes para un tema."""
        
        ColoredOutput.header(f"Procesando Playbooks para: {theme} - {date_str}")
        
        # Encontrar directorio de sesión
        session_dir = self.find_session_directory(date_str, theme)
        if not session_dir:
            return False
        
        support_docs_dir = session_dir / 'support-docs'
        
        # Obtener playbooks para este tema
        playbooks_to_process = THEME_PLAYBOOK_MAPPING.get(theme, [])
        if not playbooks_to_process:
            ColoredOutput.warning(f"No hay playbooks mapeados para el tema: {theme}")
            return False
        
        ColoredOutput.info(f"Playbooks a procesar: {', '.join(playbooks_to_process)}")
        
        processed_files = []
        failed_files = []
        
        for playbook_code in playbooks_to_process:
            if playbook_code not in PLAYBOOK_FILE_MAPPING:
                ColoredOutput.warning(f"Playbook {playbook_code} no está en el mapeo")
                failed_files.append(playbook_code)
                continue
            
            playbook_filename = PLAYBOOK_FILE_MAPPING[playbook_code]
            playbook_path = self.playbooks_dir / playbook_filename
            
            # Si no existe en documentation_playbooks, buscar en playbooks principal
            if not playbook_path.exists():
                playbook_path = self.main_playbooks_dir / playbook_filename
            
            if not playbook_path.exists():
                ColoredOutput.error(f"Playbook no encontrado: {playbook_path}")
                failed_files.append(playbook_code)
                continue
            
            # Generar template usando el nuevo sistema universal
            ColoredOutput.info(f"Generando template universal para {playbook_code}: {playbook_filename}")
            
            try:
                template_content = self.generate_universal_template(theme, date_str, playbook_filename)
                
                # Guardar template
                template_filename = playbook_filename  # Mantener mismo nombre
                template_path = support_docs_dir / template_filename
                
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(template_content)
                
                processed_files.append(str(template_path))
                ColoredOutput.success(f"Template universal creado: {template_filename}")
                
            except Exception as e:
                ColoredOutput.error(f"Error generando template para {playbook_code}: {e}")
                failed_files.append(playbook_code)
        
        # Actualizar tracking
        self.update_processing_tracking(theme, date_str, processed_files, failed_files)
        
        # Mostrar resumen
        self.show_processing_summary(processed_files, failed_files, theme, date_str)
        
        return len(failed_files) == 0
    
    def update_processing_tracking(self, theme, date_str, processed_files, failed_files):
        """Actualiza el tracking con información de procesamiento."""
        tracking_data = self.load_tracking_data()
        
        # Buscar sesión existente
        session_entry = None
        for session in tracking_data.get('processed_dates', []):
            if session['date'] == date_str and session['theme'] == theme:
                session_entry = session
                break
        
        if session_entry:
            # Actualizar sesión existente
            session_entry['templates_generated'] = processed_files
            session_entry['templates_failed'] = failed_files
            session_entry['template_generation_date'] = datetime.now().isoformat()
            session_entry['template_type'] = 'universal_templates'
            session_entry['status'] = 'universal_templates_generated'
            session_entry['last_updated'] = datetime.now().isoformat()
            
            self.save_tracking_data(tracking_data)
            ColoredOutput.success("Tracking actualizado correctamente")
        else:
            ColoredOutput.warning("No se encontró la sesión en el tracking para actualizar")
    
    def show_processing_summary(self, processed_files, failed_files, theme, date_str):
        """Muestra resumen del procesamiento."""
        
        ColoredOutput.header("Resumen de Procesamiento")
        
        print(f"📅 **Fecha:** {date_str}")
        print(f"🎯 **Tema:** {theme}")
        print(f"✅ **Templates universales generados:** {len(processed_files)}")
        print(f"❌ **Errores:** {len(failed_files)}")
        
        if processed_files:
            ColoredOutput.info("\n📄 Templates universales generados:")
            for file_path in processed_files:
                print(f"  • {Path(file_path).name}")
        
        if failed_files:
            ColoredOutput.warning(f"\n⚠️  Playbooks con errores: {', '.join(failed_files)}")
        
        ColoredOutput.info(f"\n📁 Ubicación: daily-work/{date_str}_{theme}/support-docs/")
        
        if processed_files:
            ColoredOutput.info("\nPróximos pasos:")
            print("1. Revisar los marcos de referencia generados")
            print("2. Completar las decisiones técnicas específicas")
            print("3. Usar los playbooks originales como guía detallada")
            print("4. Documentar las decisiones tomadas durante el desarrollo")
    
    def list_available_playbooks(self):
        """Lista todos los playbooks disponibles."""
        
        ColoredOutput.header("Playbooks Disponibles")
        
        available_playbooks = self.get_available_playbooks()
        
        print("📚 **Playbooks en el sistema:**\n")
        
        for playbook_code, filename, path in available_playbooks:
            # Cargar metadatos básicos
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                metadata = self.extract_metadata(content)
                
                print(f"🎯 **{playbook_code}** - {filename}")
                print(f"   📝 {metadata['title']}")
                print(f"   📄 {metadata['description']}")
                print(f"   📂 {path.relative_to(self.base_path)}")
                print()
                
            except Exception as e:
                print(f"🎯 **{playbook_code}** - {filename}")
                print(f"   ❌ Error leyendo archivo: {e}")
                print()
        
        print(f"**Total playbooks disponibles:** {len(available_playbooks)}")
        
        # Mostrar mapeo de temas
        ColoredOutput.header("Mapeo de Temas a Playbooks")
        
        for theme, playbooks in THEME_PLAYBOOK_MAPPING.items():
            print(f"🎯 **{theme}**")
            print(f"   📚 Playbooks: {', '.join(playbooks)}")
            print()
