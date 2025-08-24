#!/usr/bin/env python3
"""
The Mighty Task - Report Generator
===================================

Script para generar reportes HTML y Markdown a partir de archivos de tareas diarias.

Uso:
    python report-generator.py --date="2024-01-15" --theme="BACKEND-API-SETUP"
    python report-generator.py --date="2024-01-16" --theme="FRONTEND-COMPONENTS"
"""

import argparse
import re
from datetime import datetime
from pathlib import Path
import json

class TaskReportGenerator:
    def __init__(self, base_path=None):
        self.base_path = Path(base_path or Path(__file__).parent.parent)
        self.daily_work_dir = self.base_path / "daily-work"
        self.reports_dir = self.base_path / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        
    def find_task_file(self, date, theme):
        """Encontrar archivo de tareas para fecha y tema específicos"""
        folder_name = f"{date}_{theme}"
        day_folder = self.daily_work_dir / folder_name
        
        if not day_folder.exists():
            raise FileNotFoundError(f"Carpeta no encontrada: {day_folder}")
            
        filename = f"pending-tasks-{date}_{theme}.md"
        task_file = day_folder / filename
        
        if not task_file.exists():
            raise FileNotFoundError(f"Archivo de tareas no encontrado: {task_file}")
            
        return task_file
    
    def parse_task_file(self, task_file):
        """Parsear archivo de tareas y extraer métricas"""
        with open(task_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metrics = {
            'general_completion': self._extract_completion_percentage(content),
            'current_task': self._extract_current_task(content),
            'completed_tasks': self._extract_completed_tasks(content),
            'pending_tasks': self._extract_pending_tasks(content),
            'history_entries': self._extract_history_entries(content),
            'test_results': self._extract_test_results(content),
            'missions': self._extract_missions(content),
            'bloqueadores': self._extract_blockers(content)
        }
        
        return metrics
    
    def _extract_completion_percentage(self, content):
        """Extraer porcentaje de completitud general"""
        match = re.search(r'\*\*ESTADO GENERAL.*?(\d+)% COMPLETADO\*\*', content, re.DOTALL)
        return int(match.group(1)) if match else 0
    
    def _extract_current_task(self, content):
        """Extraer tarea actual en progreso"""
        current_section = re.search(r'\*\*ACTUALMENTE TRABAJANDO EN:\*\*(.*?)(?=\*\*PRÓXIMO EN COLA:|$)', content, re.DOTALL)
        if not current_section:
            return None
            
        task_info = {}
        lines = current_section.group(1).strip().split('\n')
        
        for line in lines:
            if line.strip().startswith('- **ID:**'):
                task_info['id'] = line.split('**ID:**')[1].strip()
            elif line.strip().startswith('- **Tarea:**'):
                task_info['task'] = line.split('**Tarea:**')[1].strip()
            elif line.strip().startswith('- **Iniciado:**'):
                task_info['started'] = line.split('**Iniciado:**')[1].strip()
                
        return task_info if task_info else None
    
    def _extract_completed_tasks(self, content):
        """Extraer tareas completadas"""
        completed_section = re.search(r'\*\*ÚLTIMOS COMPLETADOS:\*\*(.*?)(?=---|\*\*|$)', content, re.DOTALL)
        if not completed_section:
            return []
            
        completed = []
        lines = completed_section.group(1).strip().split('\n')
        
        for line in lines:
            if '✅' in line:
                # Parse format: - API-XX.X Descripción ✅ (timestamp)
                match = re.search(r'- ([A-Z]+-\d+[A-Z.\d]*) ([^✅]+) ✅ \((.*?)\)', line)
                if match:
                    completed.append({
                        'id': match.group(1),
                        'task': match.group(2).strip(),
                        'completed_at': match.group(3)
                    })
        
        # También buscar en checklists marcados como completados
        checklist_completed_pattern = r'\* \[x\] \*\*\[([A-Z]+-\d+[A-Z.\d]*)\] ([^:]+):\*\* \[Estado: COMPLETADO\]'
        checklist_matches = re.findall(checklist_completed_pattern, content)
        
        for match in checklist_matches:
            completed.append({
                'id': match[0],
                'task': match[1].strip(),
                'completed_at': 'Ver historial para detalles'
            })
                    
        return completed
    
    def _extract_pending_tasks(self, content):
        """Extraer tareas pendientes de checklists"""
        pending = []
        
        # Buscar checklists pendientes con formato específico
        checklist_pattern = r'\* \[ \] \*\*\[([A-Z]+-\d+[A-Z.\d]*)\] ([^:]+):\*\* \[Estado: ([^\]]+)\]'
        matches = re.findall(checklist_pattern, content)
        
        for match in matches:
            if match[2] not in ['COMPLETADO', 'COMPLETED']:
                pending.append({
                    'id': match[0],
                    'task': match[1].strip(),
                    'status': match[2]
                })
        
        # También buscar tareas simples sin estado específico
        simple_checklist_pattern = r'\* \[ \] \*\*\[([A-Z]+-\d+[A-Z.\d]*)\] ([^:]+):\*\*'
        simple_matches = re.findall(simple_checklist_pattern, content)
        
        for match in simple_matches:
            # Evitar duplicados
            existing_ids = [task['id'] for task in pending]
            if match[0] not in existing_ids:
                pending.append({
                    'id': match[0],
                    'task': match[1].strip(),
                    'status': 'PENDIENTE'
                })
                
        return pending
    
    def _extract_history_entries(self, content):
        """Extraer entradas del historial granular"""
        history = []
        
        # Buscar entradas de historial
        history_section = re.search(r'\*\*REGISTRO CRONOLÓGICO.*?\*\*(.*?)(?=---|\*\*FILOSOFÍA|$)', content, re.DOTALL)
        if not history_section:
            return history
            
        entries = re.findall(r'\*\*\[(.*?)\] - (.*?)\*\*(.*?)(?=\*\*\[|\Z)', history_section.group(1), re.DOTALL)
        
        for entry in entries:
            timestamp, action, details = entry
            history.append({
                'timestamp': timestamp.strip(),
                'action': action.strip(),
                'details': details.strip()
            })
            
        return history
    
    def _extract_test_results(self, content):
        """Extraer resultados de pruebas"""
        tests = []
        
        # Buscar pruebas con formato específico
        test_pattern = r'\*\*PRUEBA \d+: (.*?)\*\*(.*?)(?=\*\*PRUEBA|\*\*COMENTARIOS|\Z)'
        matches = re.findall(test_pattern, content, re.DOTALL)
        
        for match in matches:
            test_name = match[0].strip()
            test_content = match[1].strip()
            
            test_info = {'name': test_name}
            
            # Extraer detalles de la prueba
            for line in test_content.split('\n'):
                if '**Comando:**' in line:
                    test_info['command'] = line.split('**Comando:**')[1].strip()
                elif '**Estado:**' in line:
                    status_line = line.split('**Estado:**')[1].strip()
                    test_info['status'] = '✅ PASÓ' if '✅' in status_line else '❌ FALLÓ'
                elif '**Fecha:**' in line:
                    test_info['date'] = line.split('**Fecha:**')[1].strip()
                    
            tests.append(test_info)
            
        return tests
    
    def _extract_missions(self, content):
        """Extraer información de misiones"""
        missions = []
        
        # Buscar misiones con formato específico
        mission_pattern = r'\*\*MISIÓN (\d+): (.*?)\*\*'
        matches = re.findall(mission_pattern, content)
        
        for match in matches:
            missions.append({
                'number': int(match[0]),
                'name': match[1].strip()
            })
            
        return missions
    
    def _extract_blockers(self, content):
        """Extraer bloqueadores identificados"""
        blockers = []
        
        # Buscar bloqueadores en historial
        blocker_pattern = r'Estado.*?BLOQUEADO.*?Contexto:\*\* (.*?)(?=\n|$)'
        matches = re.findall(blocker_pattern, content, re.DOTALL)
        
        for match in matches:
            blockers.append(match.strip())
            
        return blockers
    
    def _detect_project_files(self, date, theme):
        """Detectar archivos creados en assets/ y charts/ para incluir en reportes"""
        folder_name = f"{date}_{theme}"
        day_folder = self.daily_work_dir / folder_name
        
        files_info = {
            'assets': [],
            'charts': [],
            'support_docs': [],
            'total_files': 0
        }
        
        if not day_folder.exists():
            return files_info
        
        # Buscar archivos en assets/
        assets_dir = day_folder / "assets"
        if assets_dir.exists():
            for file_path in assets_dir.rglob("*"):
                if file_path.is_file():
                    relative_path = file_path.relative_to(day_folder)
                    files_info['assets'].append({
                        'name': file_path.name,
                        'path': str(relative_path),
                        'size': file_path.stat().st_size,
                        'type': file_path.suffix or 'Sin extensión'
                    })
        
        # Buscar archivos en charts/
        charts_dir = day_folder / "charts"
        if charts_dir.exists():
            for file_path in charts_dir.rglob("*"):
                if file_path.is_file():
                    relative_path = file_path.relative_to(day_folder)
                    files_info['charts'].append({
                        'name': file_path.name,
                        'path': str(relative_path),
                        'size': file_path.stat().st_size,
                        'type': file_path.suffix or 'Sin extensión'
                    })
        
        # Buscar archivos en support-docs/
        support_dir = day_folder / "support-docs"
        if support_dir.exists():
            for file_path in support_dir.rglob("*"):
                if file_path.is_file():
                    relative_path = file_path.relative_to(day_folder)
                    files_info['support_docs'].append({
                        'name': file_path.name,
                        'path': str(relative_path),
                        'size': file_path.stat().st_size,
                        'type': file_path.suffix or 'Sin extensión'
                    })
        
        files_info['total_files'] = len(files_info['assets']) + len(files_info['charts']) + len(files_info['support_docs'])
        return files_info
    
    def _generate_files_section_html(self, project_files):
        """Generar sección HTML para archivos del proyecto"""
        if project_files['total_files'] == 0:
            return '<div class="no-data">No se detectaron archivos adicionales en assets/, charts/ o support-docs/</div>'
        
        html = f'<p style="margin-bottom: 20px;">Se encontraron <strong>{project_files["total_files"]} archivos</strong> complementarios creados durante esta sesión:</p>'
        
        # Assets
        if project_files['assets']:
            html += f'<h3 style="color: #667eea; margin: 20px 0 10px 0;"><i class="fas fa-images"></i> Assets ({len(project_files["assets"])} archivos)</h3>'
            html += '<div style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 15px;">'
            for file in project_files['assets']:
                size_kb = file['size'] / 1024 if file['size'] > 0 else 0
                html += f'<div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #e9ecef;">'
                html += f'<div><strong>{file["name"]}</strong><br><small style="color: #6c757d;">{file["path"]}</small></div>'
                html += f'<div style="text-align: right;"><span style="background: #17a2b8; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;">{file["type"]}</span><br><small>{size_kb:.1f} KB</small></div>'
                html += '</div>'
            html += '</div>'
        
        # Charts
        if project_files['charts']:
            html += f'<h3 style="color: #667eea; margin: 20px 0 10px 0;"><i class="fas fa-chart-bar"></i> Charts ({len(project_files["charts"])} archivos)</h3>'
            html += '<div style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 15px;">'
            for file in project_files['charts']:
                size_kb = file['size'] / 1024 if file['size'] > 0 else 0
                html += f'<div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #e9ecef;">'
                html += f'<div><strong>{file["name"]}</strong><br><small style="color: #6c757d;">{file["path"]}</small></div>'
                html += f'<div style="text-align: right;"><span style="background: #28a745; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;">{file["type"]}</span><br><small>{size_kb:.1f} KB</small></div>'
                html += '</div>'
            html += '</div>'
        
        # Support Docs
        if project_files['support_docs']:
            html += f'<h3 style="color: #667eea; margin: 20px 0 10px 0;"><i class="fas fa-file-alt"></i> Support Docs ({len(project_files["support_docs"])} archivos)</h3>'
            html += '<div style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 15px;">'
            for file in project_files['support_docs']:
                size_kb = file['size'] / 1024 if file['size'] > 0 else 0
                html += f'<div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #e9ecef;">'
                html += f'<div><strong>{file["name"]}</strong><br><small style="color: #6c757d;">{file["path"]}</small></div>'
                html += f'<div style="text-align: right;"><span style="background: #6f42c1; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;">{file["type"]}</span><br><small>{size_kb:.1f} KB</small></div>'
                html += '</div>'
            html += '</div>'
        
        return html
    
    def generate_html_report(self, metrics, date, theme):
        """Generar reporte HTML"""
        html_template = self._get_html_template()
        
        # Datos para el template
        template_data = {
            'date': date,
            'theme': theme,
            'completion': metrics['general_completion'],
            'current_task': metrics['current_task'],
            'completed_count': len(metrics['completed_tasks']),
            'pending_count': len(metrics['pending_tasks']),
            'tests_passed': len([t for t in metrics['test_results'] if t.get('status') == '✅ PASÓ']),
            'tests_failed': len([t for t in metrics['test_results'] if t.get('status') == '❌ FALLÓ']),
            'history_count': len(metrics['history_entries']),
            'blockers_count': len(metrics['bloqueadores']),
            'completed_tasks': metrics['completed_tasks'],
            'pending_tasks': metrics['pending_tasks'],
            'test_results': metrics['test_results'],
            'history_entries': metrics['history_entries'][:10],  # Últimas 10 entradas
        }
        
        # Reemplazar placeholders en el template
        html_content = html_template
        for key, value in template_data.items():
            placeholder = f"{{{{ {key} }}}}"
            html_content = html_content.replace(placeholder, str(value))
            
        return html_content
    
    def generate_enhanced_html_report(self, metrics, date, theme):
        """Generar reporte HTML mejorado con mejor diseño"""
        # Detectar archivos del proyecto
        project_files = self._detect_project_files(date, theme)
        
        return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📊 Reporte Detallado - {theme}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: #f5f7fa; 
            color: #2c3e50;
            line-height: 1.6;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 20px; }}
        .header {{ 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; padding: 40px; border-radius: 15px; margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .header .meta {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; }}
        .completion-ring {{ 
            position: relative; width: 120px; height: 120px;
            background: conic-gradient(#00ff88 {metrics['general_completion'] * 3.6}deg, rgba(255,255,255,0.2) 0deg);
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
        }}
        .completion-ring::before {{ 
            content: "{metrics['general_completion']}%"; 
            font-size: 1.5em; font-weight: bold; 
            background: #667eea; width: 80px; height: 80px; 
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
        }}
        .metrics-grid {{ 
            display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
            gap: 25px; margin: 30px 0; 
        }}
        .metric-card {{ 
            background: white; padding: 25px; border-radius: 15px; 
            box-shadow: 0 5px 20px rgba(0,0,0,0.1); 
            border-left: 5px solid #667eea; transition: transform 0.3s ease;
        }}
        .metric-card:hover {{ transform: translateY(-5px); }}
        .metric-icon {{ font-size: 2.5em; color: #667eea; margin-bottom: 15px; }}
        .metric-value {{ font-size: 2.5em; font-weight: bold; color: #2c3e50; margin-bottom: 5px; }}
        .metric-label {{ color: #7f8c8d; font-weight: 500; }}
        .section {{ 
            background: white; padding: 30px; margin: 25px 0; 
            border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }}
        .section h2 {{ color: #2c3e50; margin-bottom: 20px; border-bottom: 2px solid #667eea; padding-bottom: 10px; }}
        .task-item {{ 
            padding: 20px; margin: 15px 0; background: #f8f9fa; 
            border-radius: 10px; border-left: 5px solid #28a745;
            transition: all 0.3s ease;
        }}
        .task-item:hover {{ background: #e9ecef; transform: translateX(5px); }}
        .task-id {{ 
            background: #667eea; color: white; padding: 4px 12px; 
            border-radius: 15px; font-size: 0.9em; font-weight: bold;
        }}
        .test-passed {{ color: #28a745; }}
        .test-failed {{ color: #dc3545; }}
        .test-item {{ 
            display: flex; align-items: center; justify-content: space-between;
            padding: 15px; margin: 10px 0; background: #f8f9fa; border-radius: 8px;
        }}
        .timeline {{ position: relative; }}
        .timeline-item {{ 
            position: relative; padding: 20px 0 20px 60px; 
            border-left: 2px solid #667eea; margin-bottom: 20px;
        }}
        .timeline-item::before {{ 
            content: ''; position: absolute; left: -8px; top: 25px;
            width: 15px; height: 15px; background: #667eea; 
            border-radius: 50%; box-shadow: 0 0 0 4px white;
        }}
        .no-data {{ text-align: center; padding: 40px; color: #7f8c8d; font-style: italic; }}
        .progress-bar {{ 
            background: #e9ecef; height: 20px; border-radius: 10px; overflow: hidden;
            margin: 10px 0;
        }}
        .progress-fill {{ 
            background: linear-gradient(90deg, #667eea 0%, #28a745 100%);
            height: 100%; transition: width 0.3s ease;
        }}
        .stats-mini {{ 
            display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px; margin-top: 20px;
        }}
        .stats-mini-item {{ 
            text-align: center; padding: 15px; background: #f8f9fa; 
            border-radius: 10px; border-top: 3px solid #667eea;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="meta">
                <div>
                    <h1><i class="fas fa-chart-line"></i> {theme}</h1>
                    <p><i class="fas fa-calendar"></i> {date} | <i class="fas fa-clock"></i> {datetime.now().strftime('%H:%M:%S')}</p>
                </div>
                <div class="completion-ring"></div>
            </div>
        </div>
        
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-icon"><i class="fas fa-tasks"></i></div>
                <div class="metric-value">{len(metrics['completed_tasks'])}</div>
                <div class="metric-label">Tareas Completadas</div>
            </div>
            <div class="metric-card">
                <div class="metric-icon"><i class="fas fa-clock"></i></div>
                <div class="metric-value">{len(metrics['pending_tasks'])}</div>
                <div class="metric-label">Tareas Pendientes</div>
            </div>
            <div class="metric-card">
                <div class="metric-icon"><i class="fas fa-vial"></i></div>
                <div class="metric-value">{len([t for t in metrics['test_results'] if t.get('status') == '✅ PASÓ'])}</div>
                <div class="metric-label">Tests Exitosos</div>
            </div>
        </div>
        
        <div class="section">
            <h2><i class="fas fa-crosshairs"></i> Tarea Actual</h2>
            {f'<div class="task-item"><span class="task-id">{metrics["current_task"]["id"]}</span> {metrics["current_task"]["task"]}<br><small>Iniciado: {metrics["current_task"]["started"]}</small></div>' if metrics['current_task'] else '<div class="no-data">No hay tarea actualmente en progreso</div>'}
        </div>
        
        <div class="section">
            <h2><i class="fas fa-check-circle"></i> Tareas Completadas</h2>
            {''.join([f'<div class="task-item completed"><span class="task-id">{task["id"]}</span> {task["task"]}<br><small><i class="fas fa-clock"></i> {task["completed_at"]}</small></div>' for task in metrics['completed_tasks']]) if metrics['completed_tasks'] else '<div class="no-data">No hay tareas completadas registradas</div>'}
        </div>
        
        <div class="section">
            <h2><i class="fas fa-list-ul"></i> Tareas Pendientes</h2>
            {''.join([f'<div class="task-item pending"><span class="task-id">{task["id"]}</span> {task["task"]}<br><small>Estado: {task["status"]}</small></div>' for task in metrics['pending_tasks']]) if metrics['pending_tasks'] else '<div class="no-data">No hay tareas pendientes registradas</div>'}
        </div>
        
        <div class="section">
            <h2><i class="fas fa-flask"></i> Resultados de Pruebas</h2>
            {''.join([f'<div class="test-item"><div><strong>{test["name"]}</strong><br><small>{test.get("command", "N/A")}</small></div><div class="{"test-passed" if "✅" in test.get("status", "") else "test-failed"}">{test.get("status", "N/A")}</div></div>' for test in metrics['test_results']]) if metrics['test_results'] else '<div class="no-data">No hay pruebas registradas</div>'}
        </div>
        
        <div class="section">
            <h2><i class="fas fa-history"></i> Historial Reciente</h2>
            <div class="timeline">
                {''.join([f'<div class="timeline-item"><strong>{entry["action"]}</strong><br><small>{entry["timestamp"]}</small><p style="margin-top:10px;">{entry["details"][:200]}...</p></div>' for entry in metrics['history_entries'][:5]]) if metrics['history_entries'] else '<div class="no-data">No hay entradas de historial</div>'}
            </div>
        </div>
        
        <div class="stats-mini">
            <div class="stats-mini-item">
                <div class="metric-value" style="font-size:1.5em;">{len(metrics['history_entries'])}</div>
                <div class="metric-label">Entradas Historial</div>
            </div>
            <div class="stats-mini-item">
                <div class="metric-value" style="font-size:1.5em;">{len(metrics['missions'])}</div>
                <div class="metric-label">Misiones</div>
            </div>
            <div class="stats-mini-item">
                <div class="metric-value" style="font-size:1.5em;">{len(metrics['bloqueadores'])}</div>
                <div class="metric-label">Bloqueadores</div>
            </div>
        </div>
        
        <div class="section">
            <h2><i class="fas fa-folder-open"></i> Archivos del Proyecto</h2>
            {self._generate_files_section_html(project_files)}
        </div>
        
        <footer style="text-align: center; margin-top: 50px; padding: 30px; color: #7f8c8d;">
            <p><i class="fas fa-robot"></i> <em>Reporte generado automáticamente por The Mighty Task</em></p>
            <p style="margin-top: 10px;"><small>Generado el {datetime.now().strftime('%Y-%m-%d a las %H:%M:%S')}</small></p>
        </footer>
    </div>
</body>
</html>"""
    
    def generate_enhanced_markdown_report(self, metrics, date, theme):
        """Generar reporte Markdown mejorado con mejor formato"""
        # Detectar archivos del proyecto
        project_files = self._detect_project_files(date, theme)
        
        tests_passed = len([t for t in metrics['test_results'] if t.get('status') == '✅ PASÓ'])
        tests_total = len(metrics['test_results'])
        
        # Construir el reporte por secciones para evitar f-string complejos
        header = f"# 📊 Reporte de Sesión - {theme}\n\n> **Fecha:** {date}\n> **Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n> **Completitud:** {metrics['general_completion']}%\n\n---\n\n"
        
        # Resumen ejecutivo
        status_completion = '🟢 Excelente' if metrics['general_completion'] >= 80 else '🟡 En progreso' if metrics['general_completion'] >= 50 else '🔴 Requiere atención'
        status_tasks = '🎉 Productivo' if len(metrics['completed_tasks']) >= 3 else '📈 Moderado' if len(metrics['completed_tasks']) >= 1 else '⏳ Iniciando'
        status_pending = '📋 Bien planificado' if len(metrics['pending_tasks']) >= 5 else '📝 Planificación básica'
        status_tests = '✅ Validado' if tests_passed == tests_total and tests_total > 0 else '🔍 En validación'
        
        executive_summary = f"""## 🎯 **Resumen Ejecutivo**

| 📊 **Métrica** | 🔢 **Valor** | 📈 **Estado** |
|---|---|---|
| **Completitud General** | {metrics['general_completion']}% | {status_completion} |
| **Tareas Completadas** | {len(metrics['completed_tasks'])} | {status_tasks} |
| **Tareas Pendientes** | {len(metrics['pending_tasks'])} | {status_pending} |
| **Tests Exitosos** | {tests_passed}/{tests_total} | {status_tests} |

---

"""
        
        # Foco actual
        if metrics['current_task']:
            current_section = f"""## 🎯 **Foco Actual**

### 🎯 En Progreso: {metrics['current_task']['id']}

**Tarea:** {metrics['current_task']['task']}  
**Iniciado:** {metrics['current_task']['started']}  
**Estado:** 🔄 Activo

---

"""
        else:
            current_section = """## 🎯 **Foco Actual**

### ⏸️ Sin Tarea Activa

No hay ninguna tarea actualmente en progreso.

---

"""
        
        # Logros completados
        if metrics['completed_tasks']:
            completed_section = "## ✅ **Logros Completados**\n\n"
            for task in metrics['completed_tasks']:
                completed_section += f"### ✅ {task['id']}\n**Tarea:** {task['task']}\n**Completado:** {task['completed_at']}\n**Estado:** 🎉 Finalizado\n\n"
        else:
            completed_section = """## ✅ **Logros Completados**

> 📝 **No hay tareas completadas aún**  
> Este es un buen momento para completar algunas tareas pendientes.

"""
        
        # Pipeline de trabajo
        if metrics['pending_tasks']:
            pipeline_section = "## 📋 **Pipeline de Trabajo**\n\n"
            for task in metrics['pending_tasks']:
                priority = '🔴 Alta' if 'ALTA' in task.get('status', '') else '🟡 Media' if 'MEDIA' in task.get('status', '') else '🟢 Normal'
                pipeline_section += f"### ⏳ {task['id']}\n**Tarea:** {task['task']}\n**Estado:** {task['status']}\n**Prioridad:** {priority}\n\n"
        else:
            pipeline_section = """## 📋 **Pipeline de Trabajo**

> 🎯 **Pipeline vacío**  
> Todas las tareas han sido completadas o no hay tareas registradas.

"""
        
        # Validaciones
        if metrics['test_results']:
            validation_section = "## 🧪 **Validaciones y Testing**\n\n"
            for test in metrics['test_results']:
                status_icon = "✅" if "✅" in test.get("status", "") else "❌"
                validation_section += f"### {status_icon} {test['name']}\n**Comando:** `{test.get('command', 'N/A')}`\n**Estado:** {test.get('status', 'N/A')}\n**Fecha:** {test.get('date', 'N/A')}\n\n"
        else:
            validation_section = """## 🧪 **Validaciones y Testing**

> 🔍 **Sin pruebas registradas**  
> Considera agregar pruebas para validar el progreso.

"""
        
        # Métricas y recomendaciones
        productivity_section = f"""---

## 📈 **Análisis de Productividad**

### 📊 Métricas Clave
- **Velocity:** {len(metrics['completed_tasks'])} tareas/sesión
- **Tasa de Éxito:** {(tests_passed/tests_total*100) if tests_total > 0 else 0:.1f}% tests exitosos
- **Actividad:** {len(metrics['history_entries'])} entradas en historial
- **Eficiencia:** {(metrics['general_completion']/100 * len(metrics['completed_tasks']) if metrics['completed_tasks'] else 0):.1f} puntos de productividad

"""
        
        # Recomendaciones basadas en métricas
        if metrics['general_completion'] >= 80:
            rec_completion = f"- 🟢 **Mantén el ritmo:** Tu completitud del {metrics['general_completion']}% es excelente"
        elif metrics['general_completion'] >= 50:
            rec_completion = f"- 🟡 **Acelera el progreso:** Con {metrics['general_completion']}% completitud, puedes mejorar"
        else:
            rec_completion = f"- 🔴 **Enfócate en completar:** {metrics['general_completion']}% requiere más dedicación"
        
        if tests_passed == tests_total and tests_total > 0:
            rec_testing = f"- 🎉 **Excelente testing:** {tests_passed}/{tests_total} pruebas exitosas"
        else:
            rec_testing = "- 🔍 **Mejora las validaciones:** Agrega más pruebas para mayor confianza"
        
        if len(metrics['pending_tasks']) >= 3:
            rec_planning = f"- 📋 **Buena planificación:** {len(metrics['pending_tasks'])} tareas en pipeline"
        else:
            rec_planning = "- 📝 **Planifica más:** Considera agregar más tareas al pipeline"
        
        recommendations = f"### 🎯 Recomendaciones\n{rec_completion}\n{rec_testing}\n{rec_planning}\n\n---\n\n"
        
        # Historial
        if metrics['history_entries']:
            history_section = "## 📚 **Historial de Actividad**\n\n"
            for entry in metrics['history_entries'][:5]:
                details_truncated = entry['details'][:150] + ('...' if len(entry['details']) > 150 else '')
                history_section += f"### 📅 {entry['timestamp']}\n**Acción:** {entry['action']}\n**Detalles:** {details_truncated}\n\n"
            if len(metrics['history_entries']) > 5:
                history_section += f"> 📋 **Total de entradas:** {len(metrics['history_entries'])} | [Ver historial completo en archivo de tareas]\n\n"
        else:
            history_section = """## 📚 **Historial de Actividad**

> 📝 **Sin actividad registrada**  
> El historial se construirá a medida que trabajes en tareas.

"""
        
        # Sección de archivos del proyecto
        if project_files['total_files'] > 0:
            files_section = f"""## 📁 **Archivos del Proyecto**

Se encontraron **{project_files['total_files']} archivos** complementarios creados durante esta sesión:

"""
            
            if project_files['assets']:
                files_section += f"### 🖼️ Assets ({len(project_files['assets'])} archivos)\n\n"
                for file in project_files['assets']:
                    size_kb = file['size'] / 1024 if file['size'] > 0 else 0
                    files_section += f"- **{file['name']}** `{file['type']}` ({size_kb:.1f} KB)  \n  📍 `{file['path']}`\n\n"
            
            if project_files['charts']:
                files_section += f"### 📊 Charts ({len(project_files['charts'])} archivos)\n\n"
                for file in project_files['charts']:
                    size_kb = file['size'] / 1024 if file['size'] > 0 else 0
                    files_section += f"- **{file['name']}** `{file['type']}` ({size_kb:.1f} KB)  \n  📍 `{file['path']}`\n\n"
            
            if project_files['support_docs']:
                files_section += f"### 📄 Support Docs ({len(project_files['support_docs'])} archivos)\n\n"
                for file in project_files['support_docs']:
                    size_kb = file['size'] / 1024 if file['size'] > 0 else 0
                    files_section += f"- **{file['name']}** `{file['type']}` ({size_kb:.1f} KB)  \n  📍 `{file['path']}`\n\n"
        else:
            files_section = """## 📁 **Archivos del Proyecto**

> 📂 **No se detectaron archivos adicionales**  
> No hay archivos complementarios en `assets/`, `charts/` o `support-docs/`.

"""
        
        # Información técnica
        technical_info = f"""---

## 🔧 **Información Técnica**

- **📁 Sesión:** `{date}_{theme}`
- **🏗️ Misiones:** {len(metrics['missions'])} registradas
- **⚠️ Bloqueadores:** {len(metrics['bloqueadores'])} identificados
- **📋 Archivos adicionales:** {project_files['total_files']} detectados

---

> 🤖 **Reporte automático de The Mighty Task**  
> 📊 Análisis generado el {datetime.now().strftime('%Y-%m-%d a las %H:%M:%S')}
"""
        
        # Concatenar todas las secciones
        return header + executive_summary + current_section + completed_section + pipeline_section + validation_section + productivity_section + recommendations + history_section + files_section + technical_info
    
    def generate_dashboard_html(self, metrics, date, theme):
        """Generar dashboard HTML interactivo"""
        return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Dashboard - {theme}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .dashboard {{ 
            max-width: 1600px; margin: 0 auto; padding: 20px;
            background: rgba(255,255,255,0.1); border-radius: 20px;
            backdrop-filter: blur(10px); margin-top: 20px;
        }}
        .header {{ 
            text-align: center; color: white; margin-bottom: 40px;
        }}
        .header h1 {{ font-size: 3em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }}
        .kpi-grid {{ 
            display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px; margin-bottom: 40px;
        }}
        .kpi-card {{ 
            background: rgba(255,255,255,0.95); border-radius: 15px;
            padding: 30px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease; border-top: 5px solid #667eea;
        }}
        .kpi-card:hover {{ transform: translateY(-10px); }}
        .kpi-icon {{ font-size: 3em; color: #667eea; margin-bottom: 15px; }}
        .kpi-value {{ 
            font-size: 3.5em; font-weight: bold; color: #2c3e50;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .kpi-label {{ color: #7f8c8d; font-size: 1.1em; margin-top: 10px; }}
        .charts-container {{ 
            display: grid; grid-template-columns: 1fr 1fr;
            gap: 30px; margin-bottom: 30px;
        }}
        .chart-card {{ 
            background: rgba(255,255,255,0.95); border-radius: 15px;
            padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            height: 350px;
        }}
        .chart-card canvas {{
            max-height: 250px !important;
            width: 100% !important;
        }}
        .chart-title {{ 
            font-size: 1.5em; color: #2c3e50; margin-bottom: 20px;
            text-align: center; border-bottom: 2px solid #667eea; padding-bottom: 10px;
        }}
        .status-indicators {{ 
            display: flex; justify-content: space-around; flex-wrap: wrap;
            background: rgba(255,255,255,0.95); border-radius: 15px;
            padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        .status-item {{ 
            text-align: center; padding: 15px; min-width: 120px;
        }}
        .status-icon {{ 
            font-size: 2.5em; margin-bottom: 10px;
        }}
        .status-text {{ font-weight: bold; color: #2c3e50; }}
        @media (max-width: 768px) {{
            .charts-container {{ grid-template-columns: 1fr; }}
            .kpi-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1><i class="fas fa-tachometer-alt"></i> Dashboard de Productividad</h1>
            <p style="font-size: 1.2em; opacity: 0.9;">{theme} | {date}</p>
        </div>
        
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-icon"><i class="fas fa-percentage"></i></div>
                <div class="kpi-value">{metrics['general_completion']}</div>
                <div class="kpi-label">% Completitud</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-icon"><i class="fas fa-check-circle"></i></div>
                <div class="kpi-value">{len(metrics['completed_tasks'])}</div>
                <div class="kpi-label">Tareas Completadas</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-icon"><i class="fas fa-clock"></i></div>
                <div class="kpi-value">{len(metrics['pending_tasks'])}</div>
                <div class="kpi-label">Tareas Pendientes</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-icon"><i class="fas fa-vial"></i></div>
                <div class="kpi-value">{len([t for t in metrics['test_results'] if '✅' in t.get('status', '')])}</div>
                <div class="kpi-label">Tests Exitosos</div>
            </div>
        </div>
        
        <div class="charts-container">
            <div class="chart-card">
                <div class="chart-title"><i class="fas fa-chart-pie"></i> Distribución de Tareas</div>
                <canvas id="tasksChart" width="400" height="200"></canvas>
            </div>
            <div class="chart-card">
                <div class="chart-title"><i class="fas fa-chart-bar"></i> Estado de Tests</div>
                <canvas id="testsChart" width="400" height="200"></canvas>
            </div>
        </div>
        
        <div class="status-indicators">
            <div class="status-item">
                <div class="status-icon" style="color: {'#28a745' if metrics['general_completion'] >= 80 else '#ffc107' if metrics['general_completion'] >= 50 else '#dc3545'};"><i class="fas fa-{'smile' if metrics['general_completion'] >= 80 else 'meh' if metrics['general_completion'] >= 50 else 'frown'}"></i></div>
                <div class="status-text">Estado General</div>
            </div>
            <div class="status-item">
                <div class="status-icon" style="color: {'#28a745' if len(metrics['completed_tasks']) >= 3 else '#ffc107' if len(metrics['completed_tasks']) >= 1 else '#dc3545'};"><i class="fas fa-{'rocket' if len(metrics['completed_tasks']) >= 3 else 'walking' if len(metrics['completed_tasks']) >= 1 else 'pause'}"></i></div>
                <div class="status-text">Productividad</div>
            </div>
            <div class="status-item">
                <div class="status-icon" style="color: {'#28a745' if len([t for t in metrics['test_results'] if '✅' in t.get('status', '')]) == len(metrics['test_results']) and len(metrics['test_results']) > 0 else '#ffc107' if len(metrics['test_results']) > 0 else '#dc3545'};"><i class="fas fa-{'shield-alt' if len([t for t in metrics['test_results'] if '✅' in t.get('status', '')]) == len(metrics['test_results']) and len(metrics['test_results']) > 0 else 'exclamation-triangle'}"></i></div>
                <div class="status-text">Calidad</div>
            </div>
        </div>
    </div>
    
    <script>
        // Gráfico de distribución de tareas
        const tasksCtx = document.getElementById('tasksChart').getContext('2d');
        new Chart(tasksCtx, {{
            type: 'doughnut',
            data: {{
                labels: ['Completadas', 'Pendientes'],
                datasets: [{{
                    data: [{len(metrics['completed_tasks'])}, {len(metrics['pending_tasks'])}],
                    backgroundColor: ['#28a745', '#ffc107'],
                    borderWidth: 3,
                    borderColor: '#fff'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ position: 'bottom' }}
                }}
            }}
        }});
        
        // Gráfico de tests
        const testsCtx = document.getElementById('testsChart').getContext('2d');
        new Chart(testsCtx, {{
            type: 'bar',
            data: {{
                labels: ['Exitosos', 'Fallidos'],
                datasets: [{{
                    label: 'Tests',
                    data: [{len([t for t in metrics['test_results'] if '✅' in t.get('status', '')])}, {len([t for t in metrics['test_results'] if '❌' in t.get('status', '')])or (len(metrics['test_results']) - len([t for t in metrics['test_results'] if '✅' in t.get('status', '')]))}],
                    backgroundColor: ['#28a745', '#dc3545'],
                    borderRadius: 5
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    y: {{ beginAtZero: true }}
                }},
                plugins: {{
                    legend: {{ display: false }}
                }}
            }}
        }});
    </script>
</body>
</html>"""
    
    def generate_markdown_report(self, metrics, date, theme):
        """Generar reporte Markdown"""
        md_content = f"""# Reporte Diario - {theme}

**Fecha:** {date}  
**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 Resumen General

- **Completitud:** {metrics['general_completion']}%
- **Tareas Completadas:** {len(metrics['completed_tasks'])}
- **Tareas Pendientes:** {len(metrics['pending_tasks'])}
- **Pruebas Ejecutadas:** {len(metrics['test_results'])}

---

## 🎯 Tarea Actual

"""
        
        if metrics['current_task']:
            current = metrics['current_task']
            md_content += f"""
**ID:** {current.get('id', 'N/A')}  
**Tarea:** {current.get('task', 'N/A')}  
**Iniciado:** {current.get('started', 'N/A')}
"""
        else:
            md_content += "No hay tarea actualmente en progreso.\n"
            
        md_content += "\n---\n\n## ✅ Tareas Completadas\n\n"
        
        for task in metrics['completed_tasks']:
            md_content += f"- **[{task['id']}]** {task['task']} _(completado: {task['completed_at']})_\n"
            
        md_content += "\n---\n\n## 📋 Tareas Pendientes\n\n"
        
        for task in metrics['pending_tasks']:
            status_emoji = "🔄" if task['status'] == 'EN_PROGRESO' else "⏳"
            md_content += f"- {status_emoji} **[{task['id']}]** {task['task']} _({task['status']})_\n"
            
        md_content += "\n---\n\n## 🧪 Resultados de Pruebas\n\n"
        
        for test in metrics['test_results']:
            status = test.get('status', 'N/A')
            md_content += f"- {status} **{test['name']}** _{test.get('date', 'N/A')}_\n"
            
        if metrics['bloqueadores']:
            md_content += "\n---\n\n## ⚠️ Bloqueadores Identificados\n\n"
            for blocker in metrics['bloqueadores']:
                md_content += f"- {blocker}\n"
                
        md_content += f"""

---

## 📈 Métricas de Productividad

- **Entries en Historial:** {len(metrics['history_entries'])}
- **Tests Pasados/Total:** {len([t for t in metrics['test_results'] if t.get('status') == '✅ PASÓ'])}/{len(metrics['test_results'])}
- **Velocity:** {len(metrics['completed_tasks'])} tareas completadas

---

*Reporte generado automáticamente por The Mighty Task*
"""
        
        return md_content
    
    def _get_html_template(self):
        """Template HTML básico para reportes"""
        return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte Diario - {{ theme }}</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; }
        .metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0; }
        .metric-card { background: #f8f9fa; padding: 20px; border-radius: 8px; text-align: center; border-left: 4px solid #667eea; }
        .metric-value { font-size: 2em; font-weight: bold; color: #667eea; }
        .metric-label { color: #666; margin-top: 5px; }
        .section { background: white; padding: 25px; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .task-item { padding: 15px; margin: 10px 0; background: #f8f9fa; border-radius: 5px; }
        .completed { border-left: 4px solid #28a745; }
        .pending { border-left: 4px solid #ffc107; }
        .test-passed { color: #28a745; }
        .test-failed { color: #dc3545; }
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 Reporte Diario - {{ theme }}</h1>
        <p><strong>Fecha:</strong> {{ date }} | <strong>Completitud:</strong> {{ completion }}%</p>
    </div>
    
    <div class="metrics">
        <div class="metric-card">
            <div class="metric-value">{{ completion }}%</div>
            <div class="metric-label">Completitud</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{{ completed_count }}</div>
            <div class="metric-label">Completadas</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{{ pending_count }}</div>
            <div class="metric-label">Pendientes</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">{{ tests_passed }}/{{ tests_failed }}</div>
            <div class="metric-label">Tests P/F</div>
        </div>
    </div>
    
    <div class="section">
        <h2>🎯 Tarea Actual</h2>
        <p><strong>{{ current_task }}</strong></p>
    </div>
    
    <div class="section">
        <h2>✅ Tareas Completadas</h2>
        <!-- Las tareas completadas se insertarían aquí dinámicamente -->
    </div>
    
    <div class="section">
        <h2>📋 Tareas Pendientes</h2>
        <!-- Las tareas pendientes se insertarían aquí dinámicamente -->
    </div>
    
    <div class="section">
        <h2>🧪 Resultados de Pruebas</h2>
        <!-- Los resultados de pruebas se insertarían aquí dinámicamente -->
    </div>
    
    <footer style="text-align: center; margin-top: 50px; color: #666;">
        <p><em>Reporte generado automáticamente por The Mighty Task</em></p>
    </footer>
</body>
</html>"""
    
    def generate_report(self, date, theme):
        """Generar reporte completo (HTML + MD) en carpeta organizada"""
        print(f"📊 Generando reporte para: {date}_{theme}")
        
        # Crear carpeta específica para la sesión
        session_name = f"{date}_{theme}"
        session_reports_dir = self.reports_dir / session_name
        session_reports_dir.mkdir(exist_ok=True)
        
        # Crear subcarpetas para mejor organización
        (session_reports_dir / "assets").mkdir(exist_ok=True)
        (session_reports_dir / "charts").mkdir(exist_ok=True)
        
        # Encontrar archivo de tareas
        task_file = self.find_task_file(date, theme)
        print(f"📄 Archivo encontrado: {task_file}")
        
        # Parsear métricas
        metrics = self.parse_task_file(task_file)
        print(f"📈 Métricas extraídas: {metrics['general_completion']}% completitud")
        
        # Generar reportes mejorados
        html_content = self.generate_enhanced_html_report(metrics, date, theme)
        md_content = self.generate_enhanced_markdown_report(metrics, date, theme)
        dashboard_content = self.generate_dashboard_html(metrics, date, theme)
        
        # Guardar archivos con nombres descriptivos e identificables
        html_file = session_reports_dir / f"detailed-report-{date}-{theme}.html"
        md_file = session_reports_dir / f"summary-report-{date}-{theme}.md"
        dashboard_file = session_reports_dir / f"dashboard-{date}-{theme}.html"
        metrics_file = session_reports_dir / f"metrics-{date}-{theme}.json"
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        with open(dashboard_file, 'w', encoding='utf-8') as f:
            f.write(dashboard_content)
            
        with open(metrics_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(metrics, indent=2, ensure_ascii=False, default=str))
            
        print(f"✅ Reportes generados en: {session_reports_dir}")
        print(f"   📊 Dashboard: dashboard.html")
        print(f"   📝 Reporte detallado: detailed-report.html")
        print(f"   📄 Resumen: summary-report.md")
        print(f"   📈 Métricas JSON: metrics.json")
        
        return html_file, md_file, dashboard_file

def main():
    parser = argparse.ArgumentParser(
        description='Generar reportes HTML y MD a partir de archivos de tareas diarias',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python report-generator.py --date="2024-01-15" --theme="BACKEND-API-SETUP"
  python report-generator.py --date="2024-01-16" --theme="FRONTEND-COMPONENTS"
        """
    )
    
    parser.add_argument(
        '--date', 
        required=True,
        help='Fecha del archivo de tareas (formato: YYYY-MM-DD)'
    )
    
    parser.add_argument(
        '--theme',
        required=True, 
        help='Tema del archivo de tareas (ej: BACKEND-API-SETUP)'
    )
    
    parser.add_argument(
        '--base-path',
        help='Ruta base del proyecto (default: directorio padre del script)'
    )
    
    args = parser.parse_args()
    
    try:
        generator = TaskReportGenerator(args.base_path)
        html_file, md_file, dashboard_file = generator.generate_report(args.date, args.theme)
        
        print(f"""
🎉 ¡Reportes generados exitosamente!

📍 Ubicaciones:
   - HTML: {html_file}
   - Markdown: {md_file}

💡 Para crear resumen ejecutivo:
   python scripts/mission-resumer.py --theme="{args.theme.split('-')[0]}" --output="combined-{args.theme.split('-')[0].lower()}-missions.md"
        """)
        
    except Exception as e:
        print(f"❌ Error generando reportes: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())
