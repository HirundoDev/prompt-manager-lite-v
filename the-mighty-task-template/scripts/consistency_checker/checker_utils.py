"""
Consistency Checker - Utilities Module
======================================

Utilidades adicionales para verificaciones específicas.
"""

from pathlib import Path
from typing import Dict, List, Optional
import json

class CheckerUtils:
    """Utilidades para verificaciones específicas."""
    
    def check_template_detection(self) -> Dict:
        """Verifica la efectividad de la detección de templates."""
        check_result = {'issues': [], 'warnings': []}
        
        # Casos de prueba para validar detección
        test_cases = [
            ("- [ ] [TODO] Completar esta tarea", True),
            ("## ✅ Tareas Completadas\n\n- [x] Configurar base de datos", False),
            ("**Fecha:** {date}", True),
            ("# Resumen del Día\n\nHoy implementé la funcionalidad de login.", False),
            ("### 🎯 Próximos Pasos\n- [TODO] Definir próximos pasos", True)
        ]
        
        detection_errors = 0
        for test_content, should_be_template in test_cases:
            is_detected_as_template = self.detector.is_template_content(test_content)
            if is_detected_as_template != should_be_template:
                detection_errors += 1
                check_result['warnings'].append({
                    'type': 'template_detection_error',
                    'message': f"Error de detección: contenido {'debería' if should_be_template else 'no debería'} ser template",
                    'content_preview': test_content[:50] + "..." if len(test_content) > 50 else test_content,
                    'expected': should_be_template,
                    'detected': is_detected_as_template
                })
        
        if detection_errors > 0:
            accuracy = ((len(test_cases) - detection_errors) / len(test_cases)) * 100
            check_result['warnings'].append({
                'type': 'detection_accuracy_issue',
                'message': f"Precisión de detección de templates: {accuracy:.1f}%",
                'errors': detection_errors,
                'total_tests': len(test_cases)
            })
        
        return check_result
    
    def check_tracking_consistency(self) -> Dict:
        """Verifica consistencia del sistema de tracking."""
        check_result = {'issues': [], 'warnings': []}
        
        tracking_file = self.daily_work_dir / '.tracking.json'
        
        if not tracking_file.exists():
            check_result['warnings'].append({
                'type': 'missing_tracking',
                'message': "Archivo de tracking no existe",
                'path': str(tracking_file)
            })
            return check_result
        
        try:
            with open(tracking_file, 'r', encoding='utf-8') as f:
                tracking_data = json.load(f)
            
            # Verificar estructura del tracking
            required_keys = ['processed_dates']
            for key in required_keys:
                if key not in tracking_data:
                    check_result['issues'].append({
                        'type': 'invalid_tracking_structure',
                        'severity': 'major',
                        'message': f"Clave requerida faltante en tracking: {key}",
                        'missing_key': key
                    })
            
            # Verificar consistencia con sesiones existentes
            if 'processed_dates' in tracking_data:
                tracked_sessions = set()
                for entry in tracking_data['processed_dates']:
                    if 'session_name' in entry:
                        tracked_sessions.add(entry['session_name'])
                
                # Comparar con sesiones reales
                actual_sessions = set()
                if self.daily_work_dir.exists():
                    for session_dir in self.daily_work_dir.iterdir():
                        if session_dir.is_dir() and not session_dir.name.startswith('.'):
                            actual_sessions.add(session_dir.name)
                
                # Sesiones no trackeadas
                untracked = actual_sessions - tracked_sessions
                for session_name in untracked:
                    check_result['warnings'].append({
                        'type': 'untracked_session',
                        'message': f"Sesión no registrada en tracking: {session_name}",
                        'session': session_name
                    })
                
                # Sesiones trackeadas pero inexistentes
                missing = tracked_sessions - actual_sessions
                for session_name in missing:
                    check_result['warnings'].append({
                        'type': 'orphaned_tracking',
                        'message': f"Sesión en tracking pero directorio no existe: {session_name}",
                        'session': session_name
                    })
            
        except json.JSONDecodeError as e:
            check_result['issues'].append({
                'type': 'corrupted_tracking',
                'severity': 'major',
                'message': f"Archivo de tracking corrupto: {e}",
                'path': str(tracking_file)
            })
        except Exception as e:
            check_result['issues'].append({
                'type': 'tracking_read_error',
                'severity': 'major',
                'message': f"Error leyendo tracking: {e}",
                'path': str(tracking_file)
            })
        
        return check_result
    
    def check_duplicates(self) -> Dict:
        """Detecta duplicados en el sistema."""
        check_result = {'issues': [], 'warnings': []}
        
        # Duplicados en playbooks (usando registry)
        playbook_duplicates = self.registry.detect_duplicate_templates()
        for dup_group in playbook_duplicates:
            check_result['warnings'].append({
                'type': 'duplicate_playbook_templates',
                'message': f"Templates duplicados en playbooks: {len(dup_group['files'])} archivos",
                'files': dup_group['files'],
                'similarity': dup_group['similarity']
            })
        
        # Duplicados en sesiones diarias
        session_duplicates = self._detect_session_duplicates()
        for dup in session_duplicates:
            check_result['warnings'].append({
                'type': 'duplicate_session_content',
                'message': f"Contenido duplicado entre sesiones: {dup['session1']} y {dup['session2']}",
                'sessions': [dup['session1'], dup['session2']],
                'similarity': dup['similarity']
            })
        
        return check_result
    
    def _detect_session_duplicates(self) -> List[Dict]:
        """Detecta duplicados entre sesiones."""
        duplicates = []
        
        if not self.daily_work_dir.exists():
            return duplicates
        
        sessions_content = {}
        
        # Recopilar contenido de sesiones
        for session_dir in self.daily_work_dir.iterdir():
            if not session_dir.is_dir() or session_dir.name.startswith('.'):
                continue
            
            main_files = list(session_dir.glob('pending-tasks-*.md'))
            if main_files:
                try:
                    content = main_files[0].read_text(encoding='utf-8')
                    # Filtrar contenido de template para comparación
                    if hasattr(self.detector, '_extract_meaningful_content'):
                        filtered_content = self.detector._extract_meaningful_content(content)
                    else:
                        # Fallback si el método no existe
                        filtered_content = content
                    
                    if len(filtered_content.strip()) > 100:
                        sessions_content[session_dir.name] = filtered_content
                except Exception:
                    continue
        
        # Comparar sesiones entre sí
        session_names = list(sessions_content.keys())
        for i, session1 in enumerate(session_names):
            for session2 in session_names[i+1:]:
                similarity = self._calculate_content_similarity(
                    sessions_content[session1], 
                    sessions_content[session2]
                )
                
                if similarity > 0.8:  # 80% de similitud
                    duplicates.append({
                        'session1': session1,
                        'session2': session2,
                        'similarity': similarity
                    })
        
        return duplicates
    
    def _calculate_content_similarity(self, content1: str, content2: str) -> float:
        """Calcula similitud entre dos contenidos."""
        words1 = set(content1.lower().split())
        words2 = set(content2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0
    
    def calculate_system_stats(self) -> Dict:
        """Calcula estadísticas generales del sistema."""
        stats = {
            'total_sessions': 0,
            'meaningful_sessions': 0,
            'template_only_sessions': 0,
            'total_playbooks': 0,
            'available_themes': 0,
            'mission_resumes': 0,
            'avg_session_quality': 0,
            'system_completeness': 0
        }
        
        # Estadísticas de sesiones
        if self.daily_work_dir.exists():
            session_qualities = []
            for session_dir in self.daily_work_dir.iterdir():
                if session_dir.is_dir() and not session_dir.name.startswith('.'):
                    stats['total_sessions'] += 1
                    analysis = self._analyze_session_integrity(session_dir)
                    
                    if not analysis['is_template_only']:
                        stats['meaningful_sessions'] += 1
                    else:
                        stats['template_only_sessions'] += 1
                    
                    session_qualities.append(analysis['quality_score'])
            
            if session_qualities:
                stats['avg_session_quality'] = sum(session_qualities) / len(session_qualities)
        
        # Estadísticas de playbooks
        stats['available_themes'] = len(self.registry.THEME_PLAYBOOK_MAPPING)
        stats['total_playbooks'] = len(self.registry.PLAYBOOK_FILE_MAPPING)
        
        # Estadísticas de mission resumes
        if self.mission_resumes_dir.exists():
            stats['mission_resumes'] = len([d for d in self.mission_resumes_dir.iterdir() if d.is_dir()])
        
        # Completitud del sistema
        completeness_factors = []
        
        if stats['total_sessions'] > 0:
            meaningful_ratio = stats['meaningful_sessions'] / stats['total_sessions']
            completeness_factors.append(meaningful_ratio * 100)
        
        completeness_factors.append(stats['avg_session_quality'])
        
        theme_completeness = 0
        for theme in self.registry.THEME_PLAYBOOK_MAPPING:
            validation = self.registry.validate_theme_consistency(theme)
            if validation['valid']:
                theme_completeness += 1
        
        if stats['available_themes'] > 0:
            theme_ratio = (theme_completeness / stats['available_themes']) * 100
            completeness_factors.append(theme_ratio)
        
        if completeness_factors:
            stats['system_completeness'] = sum(completeness_factors) / len(completeness_factors)
        
        return stats