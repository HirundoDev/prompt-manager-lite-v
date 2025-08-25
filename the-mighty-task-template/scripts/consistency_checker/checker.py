"""
Consistency Checker - Core Module
=================================

Verificador de integridad del sistema con detección avanzada de templates y validaciones mejoradas.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
from collections import defaultdict

# Importar módulos compartidos
sys.path.append(str(Path(__file__).parent.parent))
from shared.template_detector import TemplateDetector
from shared.playbook_registry import PlaybookRegistry
from shared.colored_output import ColoredOutput

# Importar métodos modulares
from .checker_methods import CheckerMethods
from .checker_utils import CheckerUtils

class ConsistencyChecker(CheckerMethods, CheckerUtils):
    """Verificador de integridad con detección inteligente de templates."""
    
    def __init__(self, base_path: Optional[Path] = None):
        self.base_path = Path(base_path or Path(__file__).parent.parent.parent)
        self.daily_work_dir = self.base_path / 'daily-work'
        self.playbooks_dir = self.base_path / 'playbooks'
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
    
    def run_full_check(self) -> Dict:
        """Ejecuta verificación completa del sistema."""
        ColoredOutput.header("Verificación de Consistencia - The Mighty Task v2.0")
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'checks_performed': [],
            'issues': [],
            'warnings': [],
            'stats': {},
            'overall_health': 'unknown'
        }
        
        # 1. Verificar estructura base
        ColoredOutput.progress("Verificando estructura base del proyecto...")
        structure_check = self.check_project_structure()
        results['checks_performed'].append('project_structure')
        results['issues'].extend(structure_check['issues'])
        results['warnings'].extend(structure_check['warnings'])
        
        # 2. Verificar consistencia de playbooks
        ColoredOutput.progress("Verificando consistencia de playbooks...")
        playbooks_check = self.check_playbooks_consistency()
        results['checks_performed'].append('playbooks_consistency')
        results['issues'].extend(playbooks_check['issues'])
        results['warnings'].extend(playbooks_check['warnings'])
        
        # 3. Verificar sesiones diarias
        ColoredOutput.progress("Analizando sesiones diarias...")
        sessions_check = self.check_daily_sessions()
        results['checks_performed'].append('daily_sessions')
        results['issues'].extend(sessions_check['issues'])
        results['warnings'].extend(sessions_check['warnings'])
        
        # 4. Verificar detección de templates
        ColoredOutput.progress("Verificando detección de templates...")
        templates_check = self.check_template_detection()
        results['checks_performed'].append('template_detection')
        results['issues'].extend(templates_check['issues'])
        results['warnings'].extend(templates_check['warnings'])
        
        # 5. Verificar tracking y metadatos
        ColoredOutput.progress("Verificando sistema de tracking...")
        tracking_check = self.check_tracking_consistency()
        results['checks_performed'].append('tracking_consistency')
        results['issues'].extend(tracking_check['issues'])
        results['warnings'].extend(tracking_check['warnings'])
        
        # 6. Verificar duplicados
        ColoredOutput.progress("Detectando duplicados...")
        duplicates_check = self.check_duplicates()
        results['checks_performed'].append('duplicates_detection')
        results['issues'].extend(duplicates_check['issues'])
        results['warnings'].extend(duplicates_check['warnings'])
        
        # Calcular estadísticas finales
        results['stats'] = self.calculate_system_stats()
        
        # Determinar salud general
        critical_issues = len([i for i in results['issues'] if i.get('severity') == 'critical'])
        major_issues = len([i for i in results['issues'] if i.get('severity') == 'major'])
        
        if critical_issues > 0:
            results['overall_health'] = 'critical'
        elif major_issues > 3:
            results['overall_health'] = 'poor'
        elif major_issues > 0 or len(results['warnings']) > 5:
            results['overall_health'] = 'fair'
        else:
            results['overall_health'] = 'good'
        
        return results