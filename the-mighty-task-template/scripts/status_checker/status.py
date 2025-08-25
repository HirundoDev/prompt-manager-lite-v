"""
Status Checker - Core Module
============================

Verificador de estado del sistema con análisis de calidad y métricas mejoradas.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

# Importar módulos compartidos
sys.path.append(str(Path(__file__).parent.parent))
from shared.template_detector import TemplateDetector
from shared.playbook_registry import PlaybookRegistry
from shared.colored_output import ColoredOutput

class StatusChecker:
    """Verificador de estado con análisis de calidad mejorado."""
    
    def __init__(self, base_path: Optional[Path] = None):
        self.base_path = Path(base_path or Path(__file__).parent.parent.parent)
        self.daily_work_dir = self.base_path / 'daily-work'
        self.mission_resumes_dir = self.base_path / 'mission-resumes'
        
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
    
    def get_system_overview(self) -> Dict:
        """Obtiene vista general del estado del sistema."""
        ColoredOutput.header("Estado del Sistema - The Mighty Task v2.0")
        
        overview = {
            'timestamp': datetime.now().isoformat(),
            'sessions': self.analyze_sessions(),
            'playbooks': self.analyze_playbooks(),
            'mission_resumes': self.analyze_mission_resumes(),
            'quality_metrics': self.calculate_quality_metrics(),
            'recommendations': []
        }
        
        # Generar recomendaciones basadas en análisis
        overview['recommendations'] = self.generate_recommendations(overview)
        
        return overview
    
    def analyze_sessions(self) -> Dict:
        """Analiza todas las sesiones diarias."""
        sessions_data = {
            'total_sessions': 0,
            'meaningful_sessions': 0,
            'template_only_sessions': 0,
            'incomplete_sessions': 0,
            'high_quality_sessions': 0,
            'sessions_by_theme': defaultdict(int),
            'sessions_by_date': {},
            'avg_completion': 0,
            'recent_activity': []
        }
        
        if not self.daily_work_dir.exists():
            return sessions_data
        
        session_completions = []
        recent_sessions = []
        
        for session_dir in self.daily_work_dir.iterdir():
            if not session_dir.is_dir() or session_dir.name.startswith('.'):
                continue
            
            sessions_data['total_sessions'] += 1
            
            # Parsear información de sesión
            session_info = self._parse_session_info(session_dir)
            if session_info:
                sessions_data['sessions_by_theme'][session_info['theme']] += 1
                sessions_data['sessions_by_date'][session_info['date']] = session_info
                recent_sessions.append(session_info)
            
            # Analizar calidad de contenido
            quality_analysis = self._analyze_session_quality(session_dir)
            
            if quality_analysis['is_meaningful']:
                sessions_data['meaningful_sessions'] += 1
            else:
                sessions_data['template_only_sessions'] += 1
            
            if quality_analysis['completion_percentage'] < 30:
                sessions_data['incomplete_sessions'] += 1
            elif quality_analysis['completion_percentage'] > 70:
                sessions_data['high_quality_sessions'] += 1
            
            session_completions.append(quality_analysis['completion_percentage'])
        
        # Calcular promedio de completitud
        if session_completions:
            sessions_data['avg_completion'] = sum(session_completions) / len(session_completions)
        
        # Actividad reciente (últimas 5 sesiones por fecha)
        recent_sessions.sort(key=lambda x: x['date'], reverse=True)
        sessions_data['recent_activity'] = recent_sessions[:5]
        
        return sessions_data
    
    def _parse_session_info(self, session_dir: Path) -> Optional[Dict]:
        """Parsea información básica de una sesión."""
        try:
            parts = session_dir.name.split('_', 1)
            if len(parts) != 2:
                return None
            
            date_str, theme = parts
            datetime.strptime(date_str, '%Y-%m-%d')  # Validar formato
            
            # Obtener información adicional
            main_files = list(session_dir.glob('pending-tasks-*.md'))
            has_main_file = len(main_files) > 0
            
            assets_dir = session_dir / 'assets'
            assets_count = len([f for f in assets_dir.rglob('*') if f.is_file()]) if assets_dir.exists() else 0
            
            return {
                'name': session_dir.name,
                'date': date_str,
                'theme': theme,
                'has_main_file': has_main_file,
                'assets_count': assets_count,
                'directory': str(session_dir)
            }
        except (ValueError, IndexError):
            return None
    
    def _analyze_session_quality(self, session_dir: Path) -> Dict:
        """Analiza la calidad de una sesión específica."""
        analysis = {
            'is_meaningful': False,
            'completion_percentage': 0,
            'quality_score': 0,
            'files_analyzed': 0,
            'content_types': {
                'template': 0,
                'partial': 0,
                'complete': 0
            }
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
                
                content_type = content_analysis['type']
                analysis['content_types'][content_type] += 1
                
                if content_type != 'template':
                    analysis['is_meaningful'] = True
                    
            except Exception:
                pass
        
        # Analizar documentos de apoyo
        support_docs_dir = session_dir / 'support-docs'
        if support_docs_dir.exists():
            for doc_file in support_docs_dir.glob('*.md'):
                try:
                    content = doc_file.read_text(encoding='utf-8')
                    analysis['files_analyzed'] += 1
                    
                    if self.detector.is_template_content(content):
                        analysis['content_types']['template'] += 1
                    else:
                        analysis['is_meaningful'] = True
                        doc_quality = self.detector.analyze_content_quality(content)
                        analysis['quality_score'] += doc_quality['completion_percentage'] * 0.3
                        
                        if doc_quality['completion_percentage'] > 70:
                            analysis['content_types']['complete'] += 1
                        else:
                            analysis['content_types']['partial'] += 1
                        
                except Exception:
                    pass
        
        # Considerar assets como indicador de trabajo real
        assets_dir = session_dir / 'assets'
        if assets_dir.exists():
            assets_count = len([f for f in assets_dir.rglob('*') if f.is_file()])
            if assets_count > 0:
                analysis['is_meaningful'] = True
                analysis['quality_score'] += min(assets_count * 3, 15)
        
        return analysis
    
    def analyze_playbooks(self) -> Dict:
        """Analiza estado de playbooks y temas."""
        playbooks_data = {
            'total_playbooks': 0,
            'available_themes': 0,
            'themes_with_issues': 0,
            'duplicate_templates': 0,
            'theme_details': {},
            'registry_health': 'unknown'
        }
        
        # Obtener información del registry
        all_playbooks = list(self.registry.PLAYBOOK_FILE_MAPPING.keys())
        playbooks_data['total_playbooks'] = len(all_playbooks)
        
        available_themes = [{'name': theme, 'playbooks': playbooks} for theme, playbooks in self.registry.THEME_PLAYBOOK_MAPPING.items()]
        playbooks_data['available_themes'] = len(available_themes)
        
        # Analizar cada tema
        themes_with_issues = 0
        for theme_info in available_themes:
            theme_name = theme_info['name']
            
            playbooks_data['theme_details'][theme_name] = {
                'playbook_count': len(theme_info['playbooks']),
                'existing_playbooks': theme_info['playbooks'],
                'missing_playbooks': [],
                'valid': True,
                'description': f"Tema con {len(theme_info['playbooks'])} playbooks"
            }
        
        playbooks_data['themes_with_issues'] = themes_with_issues
        
        # Detectar duplicados
        duplicates = self.registry.detect_duplicate_templates()
        playbooks_data['duplicate_templates'] = len(duplicates)
        
        # Evaluar salud del registry
        registry_validation = self.registry.validate_registry_integrity()
        playbooks_data['registry_health'] = 'good' if registry_validation['valid'] else 'issues'
        
        return playbooks_data
    
    def analyze_mission_resumes(self) -> Dict:
        """Analiza resúmenes de misión existentes."""
        resumes_data = {
            'total_resumes': 0,
            'recent_resumes': [],
            'resumes_by_size': {'small': 0, 'medium': 0, 'large': 0},
            'avg_sessions_per_resume': 0
        }
        
        if not self.mission_resumes_dir.exists():
            return resumes_data
        
        resume_sessions_counts = []
        recent_resumes = []
        
        for resume_dir in self.mission_resumes_dir.iterdir():
            if not resume_dir.is_dir():
                continue
            
            resumes_data['total_resumes'] += 1
            
            # Analizar contenido del resumen
            consolidated_files = list(resume_dir.glob('*-CONSOLIDATED.md'))
            log_files = list(resume_dir.glob('consolidation-log.json'))
            
            resume_info = {
                'name': resume_dir.name,
                'has_consolidated_file': len(consolidated_files) > 0,
                'has_log': len(log_files) > 0,
                'directory': str(resume_dir)
            }
            
            # Obtener información del log si existe
            if log_files:
                try:
                    with open(log_files[0], 'r', encoding='utf-8') as f:
                        log_data = json.load(f)
                    
                    sessions_count = log_data.get('sessions_processed', 0)
                    resume_info['sessions_count'] = sessions_count
                    resume_info['timestamp'] = log_data.get('consolidation_timestamp')
                    
                    resume_sessions_counts.append(sessions_count)
                    
                    # Clasificar por tamaño
                    if sessions_count <= 2:
                        resumes_data['resumes_by_size']['small'] += 1
                    elif sessions_count <= 5:
                        resumes_data['resumes_by_size']['medium'] += 1
                    else:
                        resumes_data['resumes_by_size']['large'] += 1
                        
                except Exception:
                    pass
            
            recent_resumes.append(resume_info)
        
        # Calcular promedio de sesiones por resumen
        if resume_sessions_counts:
            resumes_data['avg_sessions_per_resume'] = sum(resume_sessions_counts) / len(resume_sessions_counts)
        
        # Ordenar por timestamp si está disponible
        recent_resumes.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        resumes_data['recent_resumes'] = recent_resumes[:3]
        
        return resumes_data
    
    def calculate_quality_metrics(self) -> Dict:
        """Calcula métricas generales de calidad del sistema."""
        metrics = {
            'overall_health_score': 0,
            'productivity_score': 0,
            'consistency_score': 0,
            'completeness_score': 0,
            'recommendations_count': 0
        }
        
        # Obtener datos base
        sessions_data = self.analyze_sessions()
        playbooks_data = self.analyze_playbooks()
        
        # Calcular score de productividad
        if sessions_data['total_sessions'] > 0:
            meaningful_ratio = sessions_data['meaningful_sessions'] / sessions_data['total_sessions']
            quality_ratio = sessions_data['high_quality_sessions'] / sessions_data['total_sessions']
            metrics['productivity_score'] = (meaningful_ratio * 60 + quality_ratio * 40) * 100
        
        # Calcular score de consistencia
        consistency_factors = []
        if playbooks_data['available_themes'] > 0:
            theme_health = (playbooks_data['available_themes'] - playbooks_data['themes_with_issues']) / playbooks_data['available_themes']
            consistency_factors.append(theme_health * 100)
        
        if playbooks_data['registry_health'] == 'good':
            consistency_factors.append(100)
        else:
            consistency_factors.append(60)
        
        if consistency_factors:
            metrics['consistency_score'] = sum(consistency_factors) / len(consistency_factors)
        
        # Calcular score de completitud
        if sessions_data['total_sessions'] > 0:
            metrics['completeness_score'] = sessions_data['avg_completion']
        
        # Score general de salud
        health_factors = [
            metrics['productivity_score'],
            metrics['consistency_score'], 
            metrics['completeness_score']
        ]
        
        valid_factors = [f for f in health_factors if f > 0]
        if valid_factors:
            metrics['overall_health_score'] = sum(valid_factors) / len(valid_factors)
        
        return metrics
    
    def generate_recommendations(self, overview: Dict) -> List[Dict]:
        """Genera recomendaciones basadas en el análisis."""
        recommendations = []
        
        sessions = overview['sessions']
        playbooks = overview['playbooks']
        quality = overview['quality_metrics']
        
        # Recomendaciones basadas en sesiones
        if sessions['total_sessions'] == 0:
            recommendations.append({
                'type': 'action',
                'priority': 'high',
                'message': 'No hay sesiones creadas. Ejecutar generate-daily.py para comenzar.',
                'command': 'python scripts/generate-daily.py --auto'
            })
        elif sessions['template_only_sessions'] > sessions['meaningful_sessions']:
            recommendations.append({
                'type': 'improvement',
                'priority': 'medium',
                'message': f'Alto número de sesiones solo con templates ({sessions["template_only_sessions"]}). Completar contenido.',
                'suggestion': 'Revisar sesiones pendientes y agregar trabajo significativo'
            })
        
        # Recomendaciones basadas en calidad
        if quality['completeness_score'] < 30:
            recommendations.append({
                'type': 'quality',
                'priority': 'medium',
                'message': f'Completitud promedio baja ({quality["completeness_score"]:.1f}%). Mejorar calidad de sesiones.',
                'suggestion': 'Dedicar más tiempo a completar tareas en cada sesión'
            })
        
        # Recomendaciones basadas en playbooks
        if playbooks['themes_with_issues'] > 0:
            recommendations.append({
                'type': 'maintenance',
                'priority': 'low',
                'message': f'{playbooks["themes_with_issues"]} temas tienen playbooks faltantes.',
                'command': 'python scripts/consistency-checker.py --check-playbooks'
            })
        
        if playbooks['duplicate_templates'] > 0:
            recommendations.append({
                'type': 'cleanup',
                'priority': 'low',
                'message': f'{playbooks["duplicate_templates"]} grupos de templates duplicados detectados.',
                'suggestion': 'Revisar y consolidar templates similares'
            })
        
        # Recomendaciones basadas en actividad
        if len(sessions['recent_activity']) > 3 and sessions['meaningful_sessions'] > 2:
            recommendations.append({
                'type': 'consolidation',
                'priority': 'medium',
                'message': 'Múltiples sesiones con contenido. Considerar consolidar en mission-resume.',
                'command': 'python scripts/mission-resumer.py --list-sessions'
            })
        
        return recommendations