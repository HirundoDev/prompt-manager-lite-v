"""
Consistency Checker - Methods Module
===================================

Métodos específicos de verificación para el ConsistencyChecker.
"""

from pathlib import Path
from typing import Dict, List, Optional
import json

class CheckerMethods:
    """Métodos de verificación para el ConsistencyChecker."""
    
    def check_project_structure(self) -> Dict:
        """Verifica la estructura base del proyecto."""
        check_result = {'issues': [], 'warnings': []}
        
        # Directorios requeridos
        required_dirs = ['daily-work', 'playbooks', 'mission-resumes', 'scripts']
        
        for dir_name in required_dirs:
            dir_path = self.base_path / dir_name
            if not dir_path.exists():
                check_result['issues'].append({
                    'type': 'missing_directory',
                    'severity': 'critical',
                    'message': f"Directorio requerido faltante: {dir_name}",
                    'path': str(dir_path)
                })
        
        # Archivos críticos
        critical_files = ['template-pendingtask.md', 'README.md']
        
        for file_name in critical_files:
            file_path = self.base_path / file_name
            if not file_path.exists():
                check_result['issues'].append({
                    'type': 'missing_critical_file',
                    'severity': 'major',
                    'message': f"Archivo crítico faltante: {file_name}",
                    'path': str(file_path)
                })
        
        # Verificar estructura de scripts modulares
        scripts_structure = {
            'shared': ['template_detector.py', 'playbook_registry.py', 'colored_output.py'],
            'generate_daily': ['__init__.py', 'generator.py', 'cli.py'],
            'mission_resumer': ['__init__.py', 'resumer.py', 'cli.py'],
            'consistency_checker': ['__init__.py', 'checker.py']
        }
        
        scripts_dir = self.base_path / 'scripts'
        if scripts_dir.exists():
            for subdir, expected_files in scripts_structure.items():
                subdir_path = scripts_dir / subdir
                if not subdir_path.exists():
                    check_result['warnings'].append({
                        'type': 'missing_script_module',
                        'message': f"Módulo de script faltante: {subdir}",
                        'path': str(subdir_path)
                    })
                else:
                    for expected_file in expected_files:
                        file_path = subdir_path / expected_file
                        if not file_path.exists():
                            check_result['warnings'].append({
                                'type': 'missing_script_file',
                                'message': f"Archivo de script faltante: {subdir}/{expected_file}",
                                'path': str(file_path)
                            })
        
        return check_result
    
    def check_playbooks_consistency(self) -> Dict:
        """Verifica consistencia de playbooks usando el registro."""
        check_result = {'issues': [], 'warnings': []}
        
        # Verificar integridad del registro
        registry_validation = self.registry.validate_registry_integrity()
        
        if not registry_validation['valid']:
            for issue in registry_validation['issues']:
                check_result['issues'].append({
                    'type': 'registry_inconsistency',
                    'severity': 'major',
                    'message': f"Inconsistencia en registro: {issue}",
                    'source': 'playbook_registry'
                })
        
        # Verificar mapeos de temas
        for theme, playbook_codes in self.registry.THEME_PLAYBOOK_MAPPING.items():
            theme_validation = self.registry.validate_theme_consistency(theme)
            
            if not theme_validation['valid']:
                for issue in theme_validation['issues']:
                    check_result['issues'].append({
                        'type': 'theme_mapping_error',
                        'severity': 'major',
                        'message': f"Error en tema '{theme}': {issue}",
                        'theme': theme
                    })
        
        # Detectar duplicados en playbooks
        duplicates = self.registry.detect_duplicate_templates()
        for duplicate_group in duplicates:
            check_result['warnings'].append({
                'type': 'duplicate_templates',
                'message': f"Templates duplicados detectados: {len(duplicate_group['files'])} archivos",
                'files': duplicate_group['files'],
                'similarity': duplicate_group['similarity']
            })
        
        return check_result
    
    def check_daily_sessions(self) -> Dict:
        """Analiza sesiones diarias con detección de templates."""
        check_result = {'issues': [], 'warnings': []}
        
        if not self.daily_work_dir.exists():
            check_result['issues'].append({
                'type': 'missing_daily_work',
                'severity': 'critical',
                'message': "Directorio daily-work no existe",
                'path': str(self.daily_work_dir)
            })
            return check_result
        
        sessions_analyzed = 0
        template_only_sessions = 0
        
        for session_dir in self.daily_work_dir.iterdir():
            if not session_dir.is_dir() or session_dir.name.startswith('.'):
                continue
            
            sessions_analyzed += 1
            session_analysis = self._analyze_session_integrity(session_dir)
            
            if session_analysis['is_template_only']:
                template_only_sessions += 1
                check_result['warnings'].append({
                    'type': 'template_only_session',
                    'message': f"Sesión contiene solo templates: {session_dir.name}",
                    'session': session_dir.name,
                    'completion': session_analysis['completion_percentage']
                })
            
            # Verificar estructura de sesión
            expected_files = [f"pending-tasks-{session_dir.name}.md"]
            for expected_file in expected_files:
                if not (session_dir / expected_file).exists():
                    check_result['issues'].append({
                        'type': 'missing_session_file',
                        'severity': 'major',
                        'message': f"Archivo principal faltante en {session_dir.name}: {expected_file}",
                        'session': session_dir.name,
                        'file': expected_file
                    })
        
        # Resumen de estadísticas
        if sessions_analyzed > 0:
            template_percentage = (template_only_sessions / sessions_analyzed) * 100
            if template_percentage > 50:
                check_result['warnings'].append({
                    'type': 'high_template_ratio',
                    'message': f"Alto porcentaje de sesiones solo con templates: {template_percentage:.1f}%",
                    'template_sessions': template_only_sessions,
                    'total_sessions': sessions_analyzed
                })
        
        return check_result
    
    def _analyze_session_integrity(self, session_dir: Path) -> Dict:
        """Analiza integridad de una sesión específica."""
        analysis = {
            'is_template_only': True,
            'completion_percentage': 0,
            'quality_score': 0,
            'files_analyzed': 0,
            'meaningful_files': 0
        }
        
        # Analizar archivo principal
        main_files = list(session_dir.glob('pending-tasks-*.md'))
        if main_files:
            main_file = main_files[0]
            try:
                content = main_file.read_text(encoding='utf-8')
                content_analysis = self.detector.analyze_content_quality(content)
                
                analysis['files_analyzed'] += 1
                analysis['completion_percentage'] = content_analysis['completion_percentage']
                analysis['quality_score'] = content_analysis['completion_percentage']
                
                if content_analysis['type'] != 'template':
                    analysis['is_template_only'] = False
                    analysis['meaningful_files'] += 1
                    
            except Exception:
                pass
        
        # Analizar support-docs
        support_docs_dir = session_dir / 'support-docs'
        if support_docs_dir.exists():
            for doc_file in support_docs_dir.glob('*.md'):
                try:
                    content = doc_file.read_text(encoding='utf-8')
                    analysis['files_analyzed'] += 1
                    
                    if not self.detector.is_template_content(content):
                        analysis['is_template_only'] = False
                        analysis['meaningful_files'] += 1
                        doc_quality = self.detector.analyze_content_quality(content)
                        analysis['quality_score'] += doc_quality['completion_percentage'] * 0.3
                        
                except Exception:
                    pass
        
        # Verificar assets
        assets_dir = session_dir / 'assets'
        if assets_dir.exists():
            assets_count = len([f for f in assets_dir.rglob('*') if f.is_file()])
            if assets_count > 0:
                analysis['is_template_only'] = False
                analysis['quality_score'] += min(assets_count * 2, 10)
        
        return analysis