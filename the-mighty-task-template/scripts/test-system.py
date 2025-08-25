#!/usr/bin/env python3
"""
The Mighty Task - System Testing Suite
======================================

Valida todas las funcionalidades del sistema.

Uso:
    python scripts/test-system.py --full-test
    python scripts/test-system.py --quick-test
    python scripts/test-system.py --smoke-test

Autor: The Mighty Task System
Fecha: 2025-01-22
"""

import os
import sys
import subprocess
import json
import shutil
from datetime import datetime, date
from pathlib import Path

class ColoredOutput:
    """Clase para output con colores en terminal."""
    COLORS = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'END': '\033[0m'
    }
    
    @classmethod
    def print(cls, text, color='WHITE', bold=False, underline=False):
        """Imprime texto con formato."""
        prefix = ""
        if bold:
            prefix += cls.COLORS['BOLD']
        if underline:
            prefix += cls.COLORS['UNDERLINE']
        if color in cls.COLORS:
            prefix += cls.COLORS[color]
        
        print(f"{prefix}{text}{cls.COLORS['END']}")
    
    @classmethod
    def success(cls, text):
        cls.print(f"✅ {text}", 'GREEN', bold=True)
    
    @classmethod
    def error(cls, text):
        cls.print(f"❌ {text}", 'RED', bold=True)
    
    @classmethod
    def warning(cls, text):
        cls.print(f"⚠️  {text}", 'YELLOW', bold=True)
    
    @classmethod
    def info(cls, text):
        cls.print(f"ℹ️  {text}", 'CYAN')
    
    @classmethod
    def header(cls, text):
        cls.print(f"\n{'=' * 60}", 'BLUE')
        cls.print(f"  {text}", 'BLUE', bold=True, underline=True)
        cls.print(f"{'=' * 60}\n", 'BLUE')

class SystemTester:
    """Clase principal para testing del sistema."""
    
    def __init__(self):
        self.base_path = Path(os.getcwd())
        self.scripts_dir = self.base_path / 'scripts'
        self.daily_work_dir = self.base_path / 'daily-work'
        self.test_date = date.today().strftime('%Y-%m-%d')
        self.test_theme = 'BACKEND-API-SETUP'
        
        # Contadores de tests
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.test_results = []
        
        # Verificar estructura básica
        if not any([
            (self.base_path / 'README.md').exists(),
            (self.base_path / 'template-pendingtask.md').exists(),
            (self.base_path / 'scripts').exists()
        ]):
            ColoredOutput.error("No estás en el directorio raíz de The Mighty Task")
            ColoredOutput.info("Ejecuta este script desde el directorio que contiene scripts/ y README.md")
            sys.exit(1)
    
    def run_command(self, cmd, capture_output=True, expect_success=True):
        """Ejecuta un comando y captura su output."""
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=capture_output,
                text=True,
                cwd=self.base_path
            )
            
            if expect_success and result.returncode != 0:
                return False, result.stderr or result.stdout
            
            return result.returncode == 0, result.stdout
        except Exception as e:
            return False, str(e)
    
    def test_case(self, name, test_func):
        """Wrapper para ejecutar un test case."""
        self.tests_run += 1
        ColoredOutput.info(f"Testing: {name}")
        
        try:
            success, message = test_func()
            if success:
                self.tests_passed += 1
                ColoredOutput.success(f"PASS: {name}")
                self.test_results.append({'name': name, 'status': 'PASS', 'message': message})
                return True
            else:
                self.tests_failed += 1
                ColoredOutput.error(f"FAIL: {name} - {message}")
                self.test_results.append({'name': name, 'status': 'FAIL', 'message': message})
                return False
        except Exception as e:
            self.tests_failed += 1
            ColoredOutput.error(f"ERROR: {name} - {str(e)}")
            self.test_results.append({'name': name, 'status': 'ERROR', 'message': str(e)})
            return False
    
    def test_scripts_exist(self):
        """Test: Verificar que todos los scripts principales existen."""
        required_scripts = [
            'generate-daily.py',
            'playbook-processor.py',
            'consistency-checker.py',
            'report-generator.py',
            'mission-resumer.py'
        ]
        
        missing_scripts = []
        for script in required_scripts:
            script_path = self.scripts_dir / script
            if not script_path.exists():
                missing_scripts.append(script)
        
        if missing_scripts:
            return False, f"Scripts faltantes: {', '.join(missing_scripts)}"
        
        return True, f"Todos los {len(required_scripts)} scripts encontrados"
    
    def test_scripts_executable(self):
        """Test: Verificar que los scripts tienen permisos de ejecución."""
        required_scripts = [
            'generate-daily.py',
            'playbook-processor.py', 
            'consistency-checker.py'
        ]
        
        non_executable = []
        for script in required_scripts:
            script_path = self.scripts_dir / script
            if script_path.exists() and not os.access(script_path, os.X_OK):
                non_executable.append(script)
        
        if non_executable:
            return False, f"Scripts sin permisos de ejecución: {', '.join(non_executable)}"
        
        return True, f"Todos los scripts tienen permisos correctos"
    
    def test_generate_daily_help(self):
        """Test: Verificar que generate-daily.py muestra ayuda."""
        success, output = self.run_command("python3 scripts/generate-daily.py --list-themes")
        
        if not success:
            return False, f"Error ejecutando --list-themes: {output}"
        
        if "Temas Disponibles" not in output:
            return False, "Output de --list-themes no contiene 'Temas Disponibles'"
        
        return True, "generate-daily.py --list-themes funciona correctamente"
    
    def test_create_session(self):
        """Test: Crear una sesión de prueba."""
        test_session_dir = self.daily_work_dir / f"{self.test_date}_TEST-SESSION"
        
        # Limpiar sesión anterior si existe
        if test_session_dir.exists():
            shutil.rmtree(test_session_dir)
        
        # Crear nueva sesión
        success, output = self.run_command(
            f'python3 scripts/generate-daily.py --theme "BACKEND-API-SETUP" --date "{self.test_date}"'
        )
        
        if not success:
            return False, f"Error creando sesión: {output}"
        
        # Verificar que se creó la estructura
        session_dir = self.daily_work_dir / f"{self.test_date}_BACKEND-API-SETUP"
        if not session_dir.exists():
            return False, "Directorio de sesión no creado"
        
        # Verificar archivo principal
        main_file = session_dir / f"pending-tasks-{self.test_date}_BACKEND-API-SETUP.md"
        if not main_file.exists():
            return False, "Archivo principal de tareas no creado"
        
        # Verificar subdirectorios
        required_dirs = ['support-docs', 'assets', 'assets/screenshots', 'assets/logs']
        for req_dir in required_dirs:
            if not (session_dir / req_dir).exists():
                return False, f"Directorio requerido no creado: {req_dir}"
        
        return True, f"Sesión creada correctamente: {session_dir}"
    
    def test_playbook_processor_list(self):
        """Test: Verificar que playbook-processor.py lista playbooks."""
        success, output = self.run_command("python3 scripts/playbook-processor.py --list-playbooks")
        
        if not success:
            return False, f"Error ejecutando --list-playbooks: {output}"
        
        if "Playbooks Disponibles" not in output:
            return False, "Output no contiene 'Playbooks Disponibles'"
        
        return True, "playbook-processor.py --list-playbooks funciona correctamente"
    
    def test_consistency_checker_basic(self):
        """Test: Verificar que consistency-checker funciona."""
        success, output = self.run_command(
            "python3 scripts/consistency-checker.py --scan-all",
            expect_success=False  # Puede retornar 1 si hay problemas menores
        )
        
        if "Escaneando Todas las Sesiones" not in output:
            return False, "Output no contiene 'Escaneando Todas las Sesiones'"
        
        return True, "consistency-checker.py --scan-all funciona correctamente"
    
    def test_tracking_file_creation(self):
        """Test: Verificar que se crea el archivo de tracking."""
        tracking_file = self.daily_work_dir / '.tracking.json'
        
        if not tracking_file.exists():
            return False, "Archivo .tracking.json no existe"
        
        try:
            with open(tracking_file, 'r', encoding='utf-8') as f:
                tracking_data = json.load(f)
            
            required_keys = ['processed_dates', 'playbook_usage', 'consistency_checks']
            for key in required_keys:
                if key not in tracking_data:
                    return False, f"Clave requerida '{key}' no encontrada en tracking"
            
            return True, "Archivo .tracking.json válido"
            
        except json.JSONDecodeError:
            return False, "Archivo .tracking.json no es JSON válido"
    
    def test_directory_structure(self):
        """Test: Verificar estructura completa de directorios."""
        required_dirs = [
            'daily-work',
            'reports',
            'mission-resumes',
            'scripts',
            'playbooks/documentation_playbooks'
        ]
        
        missing_dirs = []
        for req_dir in required_dirs:
            dir_path = self.base_path / req_dir
            if not dir_path.exists():
                missing_dirs.append(req_dir)
        
        if missing_dirs:
            return False, f"Directorios faltantes: {', '.join(missing_dirs)}"
        
        return True, f"Estructura de directorios completa ({len(required_dirs)} directorios)"
    
    def test_documentation_files(self):
        """Test: Verificar archivos de documentación."""
        required_docs = [
            'README.md',
            'QUICK_START.md',
            'template-pendingtask.md'
        ]
        
        missing_docs = []
        for doc in required_docs:
            doc_path = self.base_path / doc
            if not doc_path.exists():
                missing_docs.append(doc)
            elif doc_path.stat().st_size < 100:  # Muy pequeño
                missing_docs.append(f"{doc} (muy pequeño)")
        
        if missing_docs:
            return False, f"Documentos faltantes/incompletos: {', '.join(missing_docs)}"
        
        return True, f"Documentación completa ({len(required_docs)} archivos)"
    
    def run_smoke_tests(self):
        """Ejecuta tests básicos de smoke testing."""
        ColoredOutput.header("Smoke Tests - Verificación Básica")
        
        tests = [
            ("Scripts Exist", self.test_scripts_exist),
            ("Documentation Files", self.test_documentation_files),
            ("Directory Structure", self.test_directory_structure),
            ("Generate Daily Help", self.test_generate_daily_help),
        ]
        
        for name, test_func in tests:
            self.test_case(name, test_func)
    
    def run_quick_tests(self):
        """Ejecuta tests rápidos de funcionalidad."""
        ColoredOutput.header("Quick Tests - Funcionalidad Básica")
        
        tests = [
            ("Scripts Executable", self.test_scripts_executable),
            ("Create Session", self.test_create_session),
            ("Playbook Processor List", self.test_playbook_processor_list),
            ("Tracking File Creation", self.test_tracking_file_creation),
        ]
        
        for name, test_func in tests:
            self.test_case(name, test_func)
    
    def run_full_tests(self):
        """Ejecuta suite completo de tests."""
        ColoredOutput.header("Full Test Suite - Verificación Completa")
        
        # Ejecutar smoke tests
        self.run_smoke_tests()
        
        # Ejecutar quick tests
        self.run_quick_tests()
        
        # Tests adicionales para suite completo
        additional_tests = [
            ("Consistency Checker Basic", self.test_consistency_checker_basic),
        ]
        
        ColoredOutput.header("Additional Tests - Verificación Avanzada")
        for name, test_func in additional_tests:
            self.test_case(name, test_func)
    
    def cleanup_test_data(self):
        """Limpia datos de prueba generados."""
        ColoredOutput.info("Limpiando datos de prueba...")
        
        # Limpiar sesiones de prueba
        test_sessions = list(self.daily_work_dir.glob(f"{self.test_date}_*"))
        for session in test_sessions:
            if session.is_dir():
                shutil.rmtree(session)
                ColoredOutput.info(f"Eliminada sesión de prueba: {session.name}")
    
    def show_final_results(self):
        """Muestra resumen final de tests."""
        ColoredOutput.header("Resultados Finales")
        
        print(f"📊 **Tests Ejecutados:** {self.tests_run}")
        print(f"✅ **Tests Exitosos:** {self.tests_passed}")
        print(f"❌ **Tests Fallidos:** {self.tests_failed}")
        
        if self.tests_failed == 0:
            ColoredOutput.success("🎉 ¡Todos los tests pasaron exitosamente!")
            success_rate = 100
        else:
            ColoredOutput.warning(f"⚠️  {self.tests_failed} tests fallaron")
            success_rate = (self.tests_passed / self.tests_run) * 100
        
        print(f"📈 **Tasa de Éxito:** {success_rate:.1f}%")
        
        # Mostrar detalles de tests fallidos
        if self.tests_failed > 0:
            ColoredOutput.header("Tests Fallidos")
            for result in self.test_results:
                if result['status'] in ['FAIL', 'ERROR']:
                    ColoredOutput.error(f"{result['name']}: {result['message']}")
    
    def generate_test_report(self):
        """Genera reporte de testing."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Crear directorio de reportes si no existe
        reports_dir = self.base_path / 'reports'
        reports_dir.mkdir(exist_ok=True)
        
        # Generar contenido del reporte
        report_content = f"""# Test Report - The Mighty Task

**Generated:** {timestamp}  
**System:** The Mighty Task Testing Suite  
**Version:** 1.0

---

## 📊 Summary

| Metric | Value |
|--------|-------|
| **Tests Run** | {self.tests_run} |
| **Tests Passed** | {self.tests_passed} |
| **Tests Failed** | {self.tests_failed} |
| **Success Rate** | {(self.tests_passed / self.tests_run) * 100:.1f}% |

---

## 🔍 Test Results

"""
        
        # Agregar resultados por categoría
        status_groups = {}
        for result in self.test_results:
            status = result['status']
            if status not in status_groups:
                status_groups[status] = []
            status_groups[status].append(result)
        
        for status, results in status_groups.items():
            icon = "✅" if status == "PASS" else "❌"
            report_content += f"### {icon} {status} ({len(results)} tests)\n\n"
            
            for result in results:
                report_content += f"- **{result['name']}**"
                if result['message']:
                    report_content += f": {result['message']}"
                report_content += "\n"
            
            report_content += "\n"
        
        # Guardar reporte
        report_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = reports_dir / f"test-report_{report_timestamp}.md"
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            ColoredOutput.success(f"Reporte de testing generado: {report_file}")
            return str(report_file)
        except Exception as e:
            ColoredOutput.error(f"Error generando reporte: {e}")
            return None

def main():
    """Función principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='The Mighty Task - System Testing Suite',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Suite completo de tests
  python scripts/test-system.py --full-test
  
  # Tests rápidos
  python scripts/test-system.py --quick-test
  
  # Tests básicos (smoke test)
  python scripts/test-system.py --smoke-test
  
  # Generar reporte sin ejecutar tests
  python scripts/test-system.py --report-only

Tipos de test: smoke (básico), quick (funcional), full (completo)
        """
    )
    
    parser.add_argument('--full-test',
                       action='store_true',
                       help='Ejecutar suite completo de tests')
    
    parser.add_argument('--quick-test',
                       action='store_true', 
                       help='Ejecutar tests rápidos de funcionalidad')
    
    parser.add_argument('--smoke-test',
                       action='store_true',
                       help='Ejecutar tests básicos de smoke testing')
    
    parser.add_argument('--cleanup',
                       action='store_true',
                       help='Limpiar datos de prueba después del testing')
    
    parser.add_argument('--no-cleanup',
                       action='store_true',
                       help='No limpiar datos de prueba')
    
    parser.add_argument('--report-only',
                       action='store_true',
                       help='Solo generar reporte (sin ejecutar tests)')
    
    args = parser.parse_args()
    
    # Crear tester
    try:
        tester = SystemTester()
    except SystemExit:
        return 1
    
    # Ejecutar tests según argumentos
    if args.report_only:
        report_file = tester.generate_test_report()
        return 0 if report_file else 1
    
    elif args.full_test:
        tester.run_full_tests()
    
    elif args.quick_test:
        tester.run_quick_tests()
    
    elif args.smoke_test:
        tester.run_smoke_tests()
    
    else:
        # Por defecto, ejecutar smoke tests
        ColoredOutput.info("No se especificó tipo de test, ejecutando smoke tests")
        tester.run_smoke_tests()
    
    # Mostrar resultados
    tester.show_final_results()
    
    # Generar reporte
    tester.generate_test_report()
    
    # Cleanup si se especifica
    if args.cleanup or (not args.no_cleanup and args.full_test):
        tester.cleanup_test_data()
    
    # Return code basado en resultados
    return 0 if tester.tests_failed == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
