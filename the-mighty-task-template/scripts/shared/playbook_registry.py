"""
Playbook Registry - Shared Module
=================================

Registro central de todos los playbooks y sus templates universales.
Mantiene consistencia en mapeos y detecta duplicaciones.
"""

import json
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from datetime import datetime
import hashlib

class PlaybookRegistry:
    """Registro central de playbooks y templates."""
    
    # Mapeo de temas a playbooks
    THEME_PLAYBOOK_MAPPING = {
        'BACKEND-API-SETUP': ['DOC006', 'DOC007', 'DOC008'],
        'BACKEND-ARCHITECTURE': ['DOC006', 'DOC007'],
        'FRONTEND-COMPONENTS': ['DOC003', 'DOC004', 'DOC005'],
        'FRONTEND-ARCHITECTURE': ['DOC004', 'DOC005'],
        'DATABASE-SCHEMA': ['DOC009'],
        'DEPLOYMENT-CONFIG': ['DOC010'],
        'TESTING-STRATEGY': ['DOC011'],
        'DESIGN-SYSTEM': ['DOC003'],
        'API-DESIGN': ['DOC008'],
        'CLI-DEVELOPMENT': ['DOC019'],
        'DATA-MODELING': ['DOC009'],
        'DEVOPS-SETUP': ['DOC010'],
    }
    
    # Mapeo de códigos a archivos
    PLAYBOOK_FILE_MAPPING = {
        'DOC003': 'DOC003-DesignSystem.md',
        'DOC004': 'DOC004-FrontendArchitecture.md',
        'DOC005': 'DOC005-FrontendDependencies.md',
        'DOC006': 'DOC006-BackendArchitecture.md',
        'DOC007': 'DOC007-BackendDependencies.md',
        'DOC008': 'DOC008-APISpecification.md',
        'DOC009': 'DOC009-DataModel.md',
        'DOC010': 'DOC010-Deployment.md',
        'DOC011': 'DOC011-TestingStrategy.md',
        'DOC019': 'DOC019-CLI-Command-Reference.md',
    }
    
    # Descripción de cada playbook
    PLAYBOOK_DESCRIPTIONS = {
        'DOC003': 'Sistema de diseño y componentes UI',
        'DOC004': 'Arquitectura y estructura frontend',
        'DOC005': 'Dependencias y herramientas frontend',
        'DOC006': 'Arquitectura y estructura backend',
        'DOC007': 'Dependencias y herramientas backend',
        'DOC008': 'Especificación y diseño de APIs',
        'DOC009': 'Modelado y estructura de datos',
        'DOC010': 'Configuración de deployment y DevOps',
        'DOC011': 'Estrategias y implementación de testing',
        'DOC019': 'Referencia de comandos CLI',
    }
    
    def __init__(self, base_path: Optional[Path] = None):
        self.base_path = base_path or Path(__file__).parent.parent.parent
        self.playbooks_dir = self.base_path / 'playbooks' / 'documentation_playbooks'
        self.registry_file = self.base_path / 'scripts' / 'shared' / 'playbook_registry.json'
        self._cache = {}
        
    def scan_all_playbooks(self) -> Dict[str, Dict]:
        """
        Escanea todos los playbooks y genera registro completo.
        
        Returns:
            Dict con información completa de todos los playbooks
        """
        registry = {
            'scan_date': datetime.now().isoformat(),
            'playbooks': {},
            'themes': self.THEME_PLAYBOOK_MAPPING.copy(),
            'file_mapping': self.PLAYBOOK_FILE_MAPPING.copy(),
            'descriptions': self.PLAYBOOK_DESCRIPTIONS.copy(),
            'statistics': {
                'total_playbooks': 0,
                'existing_files': 0,
                'missing_files': 0,
                'total_themes': len(self.THEME_PLAYBOOK_MAPPING)
            }
        }
        
        for playbook_code, filename in self.PLAYBOOK_FILE_MAPPING.items():
            playbook_path = self.playbooks_dir / filename
            
            playbook_info = {
                'code': playbook_code,
                'filename': filename,
                'description': self.PLAYBOOK_DESCRIPTIONS.get(playbook_code, 'Sin descripción'),
                'exists': playbook_path.exists(),
                'path': str(playbook_path),
                'themes_using': [theme for theme, codes in self.THEME_PLAYBOOK_MAPPING.items() if playbook_code in codes]
            }
            
            if playbook_path.exists():
                try:
                    content = playbook_path.read_text(encoding='utf-8')
                    playbook_info.update({
                        'size_bytes': len(content.encode('utf-8')),
                        'lines': len(content.splitlines()),
                        'content_hash': hashlib.md5(content.encode('utf-8')).hexdigest(),
                        'last_modified': datetime.fromtimestamp(playbook_path.stat().st_mtime).isoformat(),
                        'template_structure': self._analyze_template_structure(content)
                    })
                    registry['statistics']['existing_files'] += 1
                except Exception as e:
                    playbook_info['error'] = str(e)
                    registry['statistics']['missing_files'] += 1
            else:
                registry['statistics']['missing_files'] += 1
            
            registry['playbooks'][playbook_code] = playbook_info
            registry['statistics']['total_playbooks'] += 1
        
        return registry
    
    def _analyze_template_structure(self, content: str) -> Dict:
        """Analiza la estructura de template de un playbook."""
        import re
        
        # Extraer headers
        headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        
        # Buscar placeholders universales
        universal_placeholders = re.findall(r'\[([A-Z_]+)\]', content)
        
        # Buscar secciones de decisión
        decision_sections = re.findall(r'\*\*Decisión:\*\*.*?\[([^\]]+)\]', content)
        
        return {
            'headers_count': len(headers),
            'max_header_level': max([len(h[0]) for h in headers]) if headers else 0,
            'universal_placeholders': list(set(universal_placeholders)),
            'decision_sections': list(set(decision_sections)),
            'has_code_blocks': bool(re.search(r'```', content)),
            'has_tables': bool(re.search(r'\|.*\|', content)),
            'has_checkboxes': bool(re.search(r'- \[ \]', content))
        }
    
    def get_playbooks_for_theme(self, theme: str) -> List[Dict]:
        """
        Obtiene información de playbooks para un tema específico.
        
        Args:
            theme: Nombre del tema
            
        Returns:
            Lista de información de playbooks para el tema
        """
        if theme not in self.THEME_PLAYBOOK_MAPPING:
            return []
        
        playbook_codes = self.THEME_PLAYBOOK_MAPPING[theme]
        registry = self.scan_all_playbooks()
        
        return [
            registry['playbooks'][code] 
            for code in playbook_codes 
            if code in registry['playbooks']
        ]
    
    def validate_theme_consistency(self, theme: str) -> Dict[str, any]:
        """
        Valida que todos los playbooks de un tema existan y sean consistentes.
        
        Returns:
            Dict con resultado de validación
        """
        validation = {
            'theme': theme,
            'valid': True,
            'issues': [],
            'playbooks_status': {},
            'summary': {
                'total_playbooks': 0,
                'existing_playbooks': 0,
                'missing_playbooks': 0
            }
        }
        
        if theme not in self.THEME_PLAYBOOK_MAPPING:
            validation['valid'] = False
            validation['issues'].append(f"Tema '{theme}' no existe en mapeo")
            return validation
        
        playbook_codes = self.THEME_PLAYBOOK_MAPPING[theme]
        validation['summary']['total_playbooks'] = len(playbook_codes)
        
        for code in playbook_codes:
            if code not in self.PLAYBOOK_FILE_MAPPING:
                validation['valid'] = False
                validation['issues'].append(f"Playbook {code} no tiene archivo mapeado")
                validation['playbooks_status'][code] = 'unmapped'
                continue
            
            filename = self.PLAYBOOK_FILE_MAPPING[code]
            playbook_path = self.playbooks_dir / filename
            
            if not playbook_path.exists():
                validation['valid'] = False
                validation['issues'].append(f"Archivo faltante: {filename}")
                validation['playbooks_status'][code] = 'missing'
                validation['summary']['missing_playbooks'] += 1
            else:
                validation['playbooks_status'][code] = 'exists'
                validation['summary']['existing_playbooks'] += 1
        
        return validation
    
    def detect_duplicate_templates(self) -> List[Dict]:
        """
        Detecta templates duplicados basado en hash de contenido.
        
        Returns:
            Lista de grupos de duplicados encontrados
        """
        registry = self.scan_all_playbooks()
        hash_groups = {}
        
        # Agrupar por hash de contenido
        for code, info in registry['playbooks'].items():
            if info['exists'] and 'content_hash' in info:
                content_hash = info['content_hash']
                if content_hash not in hash_groups:
                    hash_groups[content_hash] = []
                hash_groups[content_hash].append(info)
        
        # Encontrar grupos con más de un archivo
        duplicates = []
        for content_hash, files in hash_groups.items():
            if len(files) > 1:
                duplicates.append({
                    'content_hash': content_hash,
                    'duplicate_files': files,
                    'count': len(files)
                })
        
        return duplicates
    
    def get_available_themes(self) -> List[Dict]:
        """
        Obtiene lista de todos los temas disponibles con información.
        
        Returns:
            Lista de temas con información detallada
        """
        themes = []
        
        for theme, playbook_codes in self.THEME_PLAYBOOK_MAPPING.items():
            validation = self.validate_theme_consistency(theme)
            
            themes.append({
                'name': theme,
                'playbooks': playbook_codes,
                'playbook_count': len(playbook_codes),
                'valid': validation['valid'],
                'existing_playbooks': validation['summary']['existing_playbooks'],
                'missing_playbooks': validation['summary']['missing_playbooks'],
                'description': self._get_theme_description(theme)
            })
        
        return sorted(themes, key=lambda x: x['name'])
    
    def _get_theme_description(self, theme: str) -> str:
        """Genera descripción para un tema basado en sus playbooks."""
        descriptions = {
            'BACKEND-API-SETUP': 'Configuración y desarrollo de APIs backend',
            'BACKEND-ARCHITECTURE': 'Arquitectura y estructura backend',
            'FRONTEND-COMPONENTS': 'Desarrollo de componentes frontend',
            'FRONTEND-ARCHITECTURE': 'Arquitectura y estructura frontend',
            'DATABASE-SCHEMA': 'Diseño y modelado de base de datos',
            'DEPLOYMENT-CONFIG': 'Configuración de deployment y DevOps',
            'TESTING-STRATEGY': 'Estrategias y implementación de testing',
            'DESIGN-SYSTEM': 'Sistema de diseño y componentes UI',
            'API-DESIGN': 'Diseño y especificación de APIs',
            'CLI-DEVELOPMENT': 'Desarrollo de herramientas CLI',
            'DATA-MODELING': 'Modelado y estructuras de datos',
            'DEVOPS-SETUP': 'Configuración de herramientas DevOps',
        }
        return descriptions.get(theme, 'Tema personalizado')
    
    def save_registry(self) -> bool:
        """
        Guarda el registro completo en archivo JSON.
        
        Returns:
            True si se guardó exitosamente
        """
        try:
            registry = self.scan_all_playbooks()
            
            self.registry_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.registry_file, 'w', encoding='utf-8') as f:
                json.dump(registry, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception:
            return False
    
    def load_registry(self) -> Optional[Dict]:
        """
        Carga el registro desde archivo JSON.
        
        Returns:
            Dict con registro o None si no existe/error
        """
        try:
            if self.registry_file.exists():
                with open(self.registry_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return None
    
    def is_registry_outdated(self, max_age_hours: int = 24) -> bool:
        """
        Verifica si el registro está desactualizado.
        
        Args:
            max_age_hours: Máximo de horas antes de considerar desactualizado
            
        Returns:
            True si está desactualizado o no existe
        """
        registry = self.load_registry()
        if not registry or 'scan_date' not in registry:
            return True
        
        try:
            scan_date = datetime.fromisoformat(registry['scan_date'])
            age_hours = (datetime.now() - scan_date).total_seconds() / 3600
            return age_hours > max_age_hours
        except Exception:
            return True
    
    def validate_registry_integrity(self) -> Dict:
        """
        Valida la integridad del registro de playbooks.
        
        Returns:
            Dict con resultado de validación
        """
        result = {
            'valid': True,
            'issues': [],
            'stats': {
                'total_playbooks': 0,
                'valid_playbooks': 0,
                'missing_files': 0,
                'invalid_mappings': 0
            }
        }
        
        try:
            # Validar archivos de playbooks
            for playbook_id, filename in self.PLAYBOOK_FILE_MAPPING.items():
                result['stats']['total_playbooks'] += 1
                
                playbook_path = self.playbooks_dir / filename
                if not playbook_path.exists():
                    result['valid'] = False
                    result['stats']['missing_files'] += 1
                    result['issues'].append({
                        'type': 'missing_playbook',
                        'severity': 'critical',
                        'message': f"Playbook faltante: {filename}",
                        'path': str(playbook_path)
                    })
                else:
                    result['stats']['valid_playbooks'] += 1
            
            # Validar mapeos tema-playbook
            for theme, playbooks in self.THEME_PLAYBOOK_MAPPING.items():
                for playbook_id in playbooks:
                    if playbook_id not in self.PLAYBOOK_FILE_MAPPING:
                        result['valid'] = False
                        result['stats']['invalid_mappings'] += 1
                        result['issues'].append({
                            'type': 'invalid_mapping',
                            'severity': 'major',
                            'message': f"Tema '{theme}' referencia playbook inexistente: {playbook_id}",
                            'theme': theme,
                            'playbook': playbook_id
                        })
            
        except Exception as e:
            result['valid'] = False
            result['issues'].append({
                'type': 'validation_error',
                'severity': 'critical',
                'message': f"Error durante validación: {str(e)}"
            })
        
        return result