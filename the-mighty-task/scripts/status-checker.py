#!/usr/bin/env python3

"""
STATUS CHECKER - The Mighty Task System
========================================

Script de verificación rápida del estado del sistema:
- Lista todas las sesiones diarias creadas
- Muestra reportes generados
- Estado de consolidaciones en mission-resumes
- Pendientes y TODOs rápidos
- Recordatorios de tareas incompletas

Uso:
    python3 scripts/status-checker.py              # Estado completo
    python3 scripts/status-checker.py --daily      # Solo sesiones diarias  
    python3 scripts/status-checker.py --reports    # Solo reportes
    python3 scripts/status-checker.py --resumes    # Solo mission-resumes
    python3 scripts/status-checker.py --pending    # Solo pendientes
"""

import argparse
import json
import os
import re
from datetime import datetime, date
from pathlib import Path
from collections import defaultdict

def get_base_dir():
    """Obtener directorio base del proyecto"""
    return Path(__file__).parent.parent

def scan_daily_work():
    """Escanear carpeta daily-work y extraer información"""
    daily_work_path = get_base_dir() / "daily-work"
    
    if not daily_work_path.exists():
        return []
    
    sessions = []
    for session_dir in daily_work_path.iterdir():
        if session_dir.is_dir() and not session_dir.name.startswith('.'):
            # Parsear nombre: 2024-01-15_BACKEND-API-SETUP
            parts = session_dir.name.split('_', 1)
            if len(parts) == 2:
                session_date, theme = parts
                
                # Encontrar archivo principal
                main_file = session_dir / f"pending-tasks-{session_dir.name}.md"
                
                # Contar archivos en subcarpetas
                support_docs = len(list((session_dir / "support-docs").glob("*.md"))) if (session_dir / "support-docs").exists() else 0
                assets_count = len(list((session_dir / "assets").rglob("*"))) if (session_dir / "assets").exists() else 0
                charts_count = len(list((session_dir / "charts").rglob("*"))) if (session_dir / "charts").exists() else 0
                
                # Analizar estado del archivo principal
                completion_status = "❌ No encontrado"
                pending_tasks = 0
                
                if main_file.exists():
                    try:
                        content = main_file.read_text(encoding='utf-8')
                        
                        # Contar TODOs y tareas pendientes
                        todo_count = len(re.findall(r'\[TODO\]|\[ \]', content, re.IGNORECASE))
                        completed_count = len(re.findall(r'\[x\]|\[X\]', content, re.IGNORECASE))
                        
                        total_tasks = todo_count + completed_count
                        if total_tasks > 0:
                            completion_pct = (completed_count / total_tasks) * 100
                            completion_status = f"📈 {completion_pct:.0f}% ({completed_count}/{total_tasks})"
                        else:
                            completion_status = "📄 Sin tareas marcadas"
                            
                        pending_tasks = todo_count
                        
                    except Exception as e:
                        completion_status = f"⚠️ Error: {str(e)}"
                
                sessions.append({
                    'date': session_date,
                    'theme': theme,
                    'folder': session_dir.name,
                    'main_file_exists': main_file.exists(),
                    'completion_status': completion_status,
                    'pending_tasks': pending_tasks,
                    'support_docs': support_docs,
                    'assets': assets_count,
                    'charts': charts_count,
                    'path': str(session_dir)
                })
    
    # Ordenar por fecha (más reciente primero)
    sessions.sort(key=lambda x: x['date'], reverse=True)
    return sessions

def scan_reports():
    """Escanear carpeta reports"""
    reports_path = get_base_dir() / "reports"
    
    if not reports_path.exists():
        return []
    
    reports = []
    for item in reports_path.rglob("*"):
        if item.is_file() and item.suffix in ['.html', '.md', '.json']:
            # Obtener info del archivo
            stat = item.stat()
            modified_time = datetime.fromtimestamp(stat.st_mtime)
            size_kb = stat.st_size / 1024
            
            reports.append({
                'name': item.name,
                'path': str(item.relative_to(get_base_dir())),
                'type': item.suffix[1:].upper(),
                'size_kb': size_kb,
                'modified': modified_time.strftime('%Y-%m-%d %H:%M'),
                'relative_path': str(item.relative_to(reports_path))
            })
    
    # Ordenar por fecha de modificación (más reciente primero)
    reports.sort(key=lambda x: x['modified'], reverse=True)
    return reports

def scan_mission_resumes():
    """Escanear carpeta mission-resumes"""
    resumes_path = get_base_dir() / "mission-resumes"
    
    if not resumes_path.exists():
        return {'exists': False}
    
    # Contar playbooks fusionados (DOCxxx)
    playbooks = []
    for item in resumes_path.glob("DOC*.md"):
        stat = item.stat()
        size_kb = stat.st_size / 1024
        lines = len(item.read_text(encoding='utf-8').splitlines())
        
        playbooks.append({
            'name': item.name,
            'size_kb': size_kb,
            'lines': lines,
            'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')
        })
    
    # Contar archivos en subcarpetas
    assets_count = len(list((resumes_path / "assets").rglob("*"))) if (resumes_path / "assets").exists() else 0
    charts_count = len(list((resumes_path / "charts").rglob("*"))) if (resumes_path / "charts").exists() else 0
    support_docs_count = len(list((resumes_path / "support-docs").rglob("*"))) if (resumes_path / "support-docs").exists() else 0
    
    # Leer logs si existen
    log_file = resumes_path / "consolidation-log.json"
    last_consolidation = None
    if log_file.exists():
        try:
            log_data = json.loads(log_file.read_text(encoding='utf-8'))
            last_consolidation = log_data.get('timestamp', 'Desconocido')
        except:
            last_consolidation = "Error al leer log"
    
    return {
        'exists': True,
        'playbooks': playbooks,
        'assets_count': assets_count,
        'charts_count': charts_count,
        'support_docs_count': support_docs_count,
        'last_consolidation': last_consolidation
    }

def get_pending_summary():
    """Obtener resumen de tareas pendientes del sistema"""
    sessions = scan_daily_work()
    
    total_pending = sum(s['pending_tasks'] for s in sessions)
    sessions_with_pending = [s for s in sessions if s['pending_tasks'] > 0]
    
    # Buscar sesiones sin reportes
    reports = scan_reports()
    report_names = {r['name'].replace('-report.html', '').replace('-report.md', '').replace('dashboard-', '').replace('detailed-report-', '').replace('summary-report-', '').replace('metrics-', '').replace('.json', '').replace('.html', '').replace('.md', '') for r in reports}
    
    sessions_without_reports = []
    for session in sessions:
        session_key = session['folder']
        if not any(session_key in name for name in report_names):
            sessions_without_reports.append(session)
    
    return {
        'total_pending_tasks': total_pending,
        'sessions_with_pending': len(sessions_with_pending),
        'sessions_without_reports': len(sessions_without_reports),
        'pending_sessions': sessions_with_pending[:5],  # Top 5
        'missing_reports': sessions_without_reports[:5]  # Top 5
    }

def print_daily_work(sessions):
    """Imprimir estado de daily-work"""
    print("🗂️  SESIONES DIARIAS (daily-work/)")
    print("=" * 60)
    
    if not sessions:
        print("❌ No se encontraron sesiones de trabajo")
        return
    
    for session in sessions:
        print(f"\n📁 {session['folder']}")
        print(f"   📅 Fecha: {session['date']}")
        print(f"   🎯 Tema: {session['theme']}")
        print(f"   📝 Archivo principal: {'✅' if session['main_file_exists'] else '❌'}")
        print(f"   📊 Estado: {session['completion_status']}")
        if session['pending_tasks'] > 0:
            print(f"   ⚠️  Pendientes: {session['pending_tasks']} tareas")
        
        if session['support_docs'] > 0 or session['assets'] > 0 or session['charts'] > 0:
            print(f"   📂 Archivos: {session['support_docs']} docs, {session['assets']} assets, {session['charts']} charts")

def print_reports(reports):
    """Imprimir estado de reportes"""
    print("\n📊 REPORTES GENERADOS (reports/)")
    print("=" * 60)
    
    if not reports:
        print("❌ No se encontraron reportes generados")
        return
    
    # Agrupar por sesión
    by_session = defaultdict(list)
    for report in reports:
        # Extraer sesión del nombre del archivo
        session_name = report['name']
        for pattern in ['-report.html', '-report.md', 'dashboard-', 'detailed-report-', 'summary-report-', 'metrics-']:
            session_name = session_name.replace(pattern, '')
        session_name = session_name.replace('.html', '').replace('.md', '').replace('.json', '')
        
        by_session[session_name].append(report)
    
    for session_name, session_reports in by_session.items():
        print(f"\n📁 Sesión: {session_name}")
        for report in session_reports:
            print(f"   📄 {report['name']} ({report['type']}, {report['size_kb']:.1f}KB) - {report['modified']}")

def print_mission_resumes(resumes_data):
    """Imprimir estado de mission-resumes"""
    print("\n🎯 CONSOLIDACIONES (mission-resumes/)")
    print("=" * 60)
    
    if not resumes_data['exists']:
        print("❌ No se encontró carpeta mission-resumes/")
        return
    
    if resumes_data['last_consolidation']:
        print(f"📅 Última consolidación: {resumes_data['last_consolidation']}")
    
    if resumes_data['playbooks']:
        print(f"\n📚 Playbooks fusionados ({len(resumes_data['playbooks'])}):")
        for playbook in resumes_data['playbooks']:
            print(f"   📖 {playbook['name']} ({playbook['lines']} líneas, {playbook['size_kb']:.1f}KB)")
    else:
        print("❌ No se encontraron playbooks fusionados")
    
    print(f"\n📂 Archivos consolidados:")
    print(f"   🖼️  Assets: {resumes_data['assets_count']} archivos")
    print(f"   📈 Charts: {resumes_data['charts_count']} archivos") 
    print(f"   📑 Support-docs: {resumes_data['support_docs_count']} archivos")

def print_pending_summary(pending_data):
    """Imprimir resumen de pendientes"""
    print("\n⚠️  RESUMEN DE PENDIENTES")
    print("=" * 60)
    
    print(f"📊 Total tareas pendientes: {pending_data['total_pending_tasks']}")
    print(f"🗂️  Sesiones con pendientes: {pending_data['sessions_with_pending']}")
    print(f"📊 Sesiones sin reportes: {pending_data['sessions_without_reports']}")
    
    if pending_data['pending_sessions']:
        print(f"\n🔥 TOP SESIONES CON MÁS PENDIENTES:")
        for session in pending_data['pending_sessions']:
            print(f"   ⚠️  {session['folder']} - {session['pending_tasks']} pendientes")
    
    if pending_data['missing_reports']:
        print(f"\n📊 SESIONES SIN REPORTES:")
        for session in pending_data['missing_reports']:
            print(f"   📝 {session['folder']} - {session['completion_status']}")

def print_system_summary():
    """Imprimir resumen ejecutivo del sistema"""
    sessions = scan_daily_work()
    reports = scan_reports()
    resumes = scan_mission_resumes()
    pending = get_pending_summary()
    
    print("🚀 THE MIGHTY TASK - ESTADO DEL SISTEMA")
    print("=" * 60)
    print(f"📅 Revisión: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print(f"\n📊 RESUMEN EJECUTIVO:")
    print(f"   🗂️  Sesiones diarias: {len(sessions)}")
    print(f"   📊 Reportes generados: {len(reports)}")
    print(f"   🎯 Playbooks fusionados: {len(resumes['playbooks']) if resumes['exists'] else 0}")
    print(f"   ⚠️  Tareas pendientes: {pending['total_pending_tasks']}")
    
    if pending['total_pending_tasks'] > 0:
        print(f"\n🔔 RECORDATORIOS:")
        print(f"   • Hay {pending['total_pending_tasks']} tareas pendientes en {pending['sessions_with_pending']} sesiones")
        if pending['sessions_without_reports']:
            print(f"   • {pending['sessions_without_reports']} sesiones necesitan reportes")

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description="Verificador rápido del estado de The Mighty Task System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python3 scripts/status-checker.py              # Estado completo
  python3 scripts/status-checker.py --daily      # Solo sesiones diarias
  python3 scripts/status-checker.py --reports    # Solo reportes  
  python3 scripts/status-checker.py --resumes    # Solo consolidaciones
  python3 scripts/status-checker.py --pending    # Solo pendientes
        """
    )
    
    parser.add_argument('--daily', action='store_true', help='Solo mostrar sesiones diarias')
    parser.add_argument('--reports', action='store_true', help='Solo mostrar reportes')
    parser.add_argument('--resumes', action='store_true', help='Solo mostrar mission-resumes')
    parser.add_argument('--pending', action='store_true', help='Solo mostrar pendientes')
    
    args = parser.parse_args()
    
    # Si no se especifica ninguna opción, mostrar todo
    show_all = not any([args.daily, args.reports, args.resumes, args.pending])
    
    if show_all:
        print_system_summary()
    
    if show_all or args.daily:
        sessions = scan_daily_work()
        print_daily_work(sessions)
    
    if show_all or args.reports:
        reports = scan_reports()
        print_reports(reports)
    
    if show_all or args.resumes:
        resumes = scan_mission_resumes()
        print_mission_resumes(resumes)
    
    if show_all or args.pending:
        pending = get_pending_summary()
        print_pending_summary(pending)
    
    if show_all:
        print(f"\n💡 Tip: Usa --daily, --reports, --resumes o --pending para ver secciones específicas")

if __name__ == "__main__":
    main()
