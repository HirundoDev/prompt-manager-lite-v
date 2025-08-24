#!/usr/bin/env python3
"""
The Mighty Task - Daily Work Generator
=====================================

Genera la estructura de trabajo diaria con templates personalizados.

Uso:
    python scripts/generate-daily.py --theme "BACKEND-API-SETUP" --date "2024-01-15"
    python scripts/generate-daily.py --theme "FRONTEND-COMPONENTS" --date "2024-01-16"
    python scripts/generate-daily.py --auto  # Usa fecha actual y tema default

Autor: The Mighty Task System
Fecha: 2025-01-22
"""

import os
import sys
import json
import argparse
from datetime import datetime, date
from pathlib import Path

# Configuración de temas disponibles y sus descripciones
AVAILABLE_THEMES = {
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
    'DEVOPS-SETUP': 'Configuración de herramientas DevOps'
}

# Mapeo de temas a playbooks
THEME_PLAYBOOK_MAPPING = {
    'FRONTEND-ARCHITECTURE': ['DOC004'],
    'FRONTEND-COMPONENTS': ['DOC003', 'DOC004'],
    'FRONTEND-DEPENDENCIES': ['DOC005'],
    'DESIGN-SYSTEM': ['DOC003'],
    'BACKEND-API-SETUP': ['DOC006', 'DOC007', 'DOC008'],
    'BACKEND-ARCHITECTURE': ['DOC006', 'DOC007'],
    'API-DESIGN': ['DOC008'],
    'DATABASE-SCHEMA': ['DOC009'],
    'DATA-MODELING': ['DOC009'],
    'DEPLOYMENT-CONFIG': ['DOC010'],
    'DEVOPS-SETUP': ['DOC010'],
    'TESTING-STRATEGY': ['DOC011'],
    'CLI-DEVELOPMENT': ['DOC019']
}

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

class DailyWorkGenerator:
    """Generador de estructura de trabajo diario."""
    
    def __init__(self, base_path=None):
        self.base_path = Path(base_path or os.getcwd())
        self.daily_work_dir = self.base_path / 'daily-work'
        self.template_file = self.base_path / 'template-pendingtask.md'
        self.tracking_file = self.daily_work_dir / '.tracking.json'
        
        # Verificar que estemos en el directorio correcto
        if not (self.base_path / 'PLAN-COMPLETO.md').exists():
            ColoredOutput.error("No estás en el directorio raíz de The Mighty Task")
            ColoredOutput.info("Ejecuta este script desde el directorio que contiene PLAN-COMPLETO.md")
            sys.exit(1)
    
    def load_tracking_data(self):
        """Carga los datos de tracking existentes."""
        if self.tracking_file.exists():
            try:
                with open(self.tracking_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                ColoredOutput.warning("Archivo de tracking corrupto, creando uno nuevo")
        
        return {
            "processed_dates": [],
            "playbook_usage": {},
            "consistency_checks": {
                "last_check": None,
                "issues_found": 0,
                "total_files_checked": 0
            },
            "statistics": {
                "total_sessions": 0,
                "most_used_theme": None,
                "created_at": datetime.now().isoformat()
            }
        }
    
    def save_tracking_data(self, data):
        """Guarda los datos de tracking."""
        try:
            # Asegurar que el directorio existe
            self.tracking_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.tracking_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            ColoredOutput.error(f"Error guardando tracking: {e}")
            return False
    
    def validate_inputs(self, theme, date_str):
        """Valida los parámetros de entrada."""
        errors = []
        
        # Validar tema
        if theme not in AVAILABLE_THEMES:
            errors.append(f"Tema '{theme}' no válido")
            ColoredOutput.info("Temas disponibles:")
            for t, desc in AVAILABLE_THEMES.items():
                print(f"  • {t}: {desc}")
        
        # Validar fecha
        try:
            parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            if parsed_date > date.today():
                errors.append("La fecha no puede ser futura")
        except ValueError:
            errors.append(f"Formato de fecha inválido: '{date_str}' (usa YYYY-MM-DD)")
        
        return errors
    
    def check_existing_session(self, theme, date_str):
        """Verifica si ya existe una sesión para esta fecha/tema."""
        tracking_data = self.load_tracking_data()
        
        for session in tracking_data.get('processed_dates', []):
            if session['date'] == date_str and session['theme'] == theme:
                return session
        
        return None
    
    def generate_template_content(self, theme, date_str):
        """Genera el contenido del template personalizado."""
        
        # Intentar cargar template base
        if not self.template_file.exists():
            ColoredOutput.warning("Template base no encontrado, creando uno genérico")
            return self.create_generic_template(theme, date_str)
        
        try:
            with open(self.template_file, 'r', encoding='utf-8') as f:
                base_content = f.read()
        except Exception as e:
            ColoredOutput.error(f"Error leyendo template base: {e}")
            return self.create_generic_template(theme, date_str)
        
        # Personalizar contenido
        personalized_content = base_content.replace(
            '{{DATE}}', date_str
        ).replace(
            '{{THEME}}', theme
        ).replace(
            '{{THEME_DESCRIPTION}}', AVAILABLE_THEMES.get(theme, 'Tema de desarrollo')
        ).replace(
            '{{PLAYBOOKS}}', ', '.join(THEME_PLAYBOOK_MAPPING.get(theme, []))
        ).replace(
            '{{CREATION_TIME}}', datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        
        return personalized_content
    
    def create_generic_template(self, theme, date_str):
        """Crea un template genérico si no existe el base."""
        return f"""# Tareas Pendientes - {date_str} - {theme}

**Fecha de Creación:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Tema Principal:** {theme}  
**Descripción:** {AVAILABLE_THEMES.get(theme, 'Tema de desarrollo')}  
**Playbooks Relacionados:** {', '.join(THEME_PLAYBOOK_MAPPING.get(theme, []))}

---

## 📋 Estado General

- **Estado del Día:** 🟡 En Progreso
- **Prioridad:** Alta
- **Estimación de Tiempo:** 6-8 horas
- **Dependencias:** Ninguna identificada

---

## ✅ Tareas Principales

### 🎯 Tareas de Alta Prioridad

- [ ] **[TASK-001]** Configuración inicial del entorno
  - **Descripción:** Preparar el entorno de desarrollo para {theme.lower()}
  - **Estimación:** 1 hora
  - **Estado:** ⏳ Pendiente
  - **Notas:** Revisar playbooks de referencia

- [ ] **[TASK-002]** Análisis de requerimientos
  - **Descripción:** Revisar y documentar requerimientos específicos
  - **Estimación:** 2 horas
  - **Estado:** ⏳ Pendiente
  - **Notas:** Usar templates de support-docs/

### 🔧 Tareas de Desarrollo

- [ ] **[TASK-003]** Implementación principal
  - **Descripción:** Desarrollo de funcionalidades core
  - **Estimación:** 3-4 horas
  - **Estado:** ⏳ Pendiente
  - **Notas:** Seguir arquitectura definida

- [ ] **[TASK-004]** Testing y validación
  - **Descripción:** Pruebas funcionales y unitarias
  - **Estimación:** 1-2 horas
  - **Estado:** ⏳ Pendiente
  - **Notas:** Usar estrategia de testing definida

### 📝 Tareas de Documentación

- [ ] **[TASK-005]** Documentación técnica
  - **Descripción:** Completar templates de documentación
  - **Estimación:** 1 hora
  - **Estado:** ⏳ Pendiente
  - **Notas:** Usar support-docs como guía

---

## 📊 Progreso del Día

| Hora | Actividad | Estado | Notas |
|------|-----------|---------|-------|
| 09:00 | Inicio del día | ✅ | Revisión de tareas |
| 09:30 | | | |
| 10:00 | | | |
| 11:00 | | | |
| 12:00 | | | |
| 14:00 | | | |
| 15:00 | | | |
| 16:00 | | | |
| 17:00 | | | |
| 18:00 | Fin del día | | Resumen y reporte |

---

## 🔗 Recursos y Referencias

### 📚 Documentación de Apoyo
- Playbooks en `playbooks/documentation_playbooks/`
- Templates generados en `support-docs/`
- Guías de referencia en README.md

### 🛠️ Herramientas Necesarias
- Editor de código (VS Code, Vim, etc.)
- Terminal para scripts de automatización
- Browser para testing y documentación

### 📋 Checklists de Verificación
- [ ] Código sigue estándares del proyecto
- [ ] Tests pasan correctamente
- [ ] Documentación está actualizada
- [ ] No hay errores de lint
- [ ] Performance es aceptable

---

## 📈 Métricas del Día

- **Tareas Completadas:** 0 / 5
- **Tiempo Estimado Total:** 8 horas
- **Tiempo Real Usado:** 0 horas
- **Eficiencia:** N/A
- **Bloqueadores Encontrados:** 0

---

## 💭 Notas y Observaciones

### Decisiones Tomadas
- 

### Problemas Encontrados
- 

### Mejoras Identificadas
- 

### Próximos Pasos
- 

---

## ✅ Checklist Final del Día

- [ ] Todas las tareas principales completadas
- [ ] Documentación actualizada
- [ ] Tests ejecutados exitosamente
- [ ] Código commiteado y pusheado
- [ ] Reporte diario generado
- [ ] Assets y evidencias guardadas
- [ ] Preparación para próxima sesión

---

**Archivo creado automáticamente por The Mighty Task System**  
**Para más información, consultar PLAN-COMPLETO.md**
"""
    
    def create_directory_structure(self, theme, date_str):
        """Crea la estructura de directorios para la sesión."""
        session_name = f"{date_str}_{theme}"
        session_dir = self.daily_work_dir / session_name
        
        # Crear directorios
        directories = [
            session_dir,
            session_dir / 'support-docs',
            session_dir / 'assets',
            session_dir / 'assets' / 'screenshots',
            session_dir / 'assets' / 'logs'
        ]
        
        created_dirs = []
        for directory in directories:
            try:
                directory.mkdir(parents=True, exist_ok=True)
                created_dirs.append(str(directory))
            except Exception as e:
                ColoredOutput.error(f"Error creando directorio {directory}: {e}")
                return None, []
        
        return session_dir, created_dirs
    
    def create_main_task_file(self, session_dir, theme, date_str):
        """Crea el archivo principal de tareas."""
        filename = f"pending-tasks-{date_str}_{theme}.md"
        file_path = session_dir / filename
        
        try:
            content = self.generate_template_content(theme, date_str)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return str(file_path)
        except Exception as e:
            ColoredOutput.error(f"Error creando archivo de tareas: {e}")
            return None
    
    def update_tracking(self, theme, date_str, files_created, session_dir):
        """Actualiza el archivo de tracking."""
        tracking_data = self.load_tracking_data()
        
        # Crear nueva entrada de sesión
        new_session = {
            "date": date_str,
            "theme": theme,
            "playbooks_used": THEME_PLAYBOOK_MAPPING.get(theme, []),
            "files_created": files_created,
            "directories_created": [str(session_dir)],
            "status": "created",
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
        
        # Actualizar datos de tracking
        tracking_data["processed_dates"].append(new_session)
        tracking_data["statistics"]["total_sessions"] += 1
        
        # Actualizar contadores de playbooks
        for playbook in THEME_PLAYBOOK_MAPPING.get(theme, []):
            tracking_data["playbook_usage"][playbook] = tracking_data["playbook_usage"].get(playbook, 0) + 1
        
        return self.save_tracking_data(tracking_data)
    
    def generate_session(self, theme, date_str, force=False):
        """Genera una sesión completa de trabajo diario."""
        
        ColoredOutput.header(f"Generando Sesión de Trabajo: {theme} - {date_str}")
        
        # Validar inputs
        errors = self.validate_inputs(theme, date_str)
        if errors:
            for error in errors:
                ColoredOutput.error(error)
            return False
        
        # Verificar sesión existente
        existing = self.check_existing_session(theme, date_str)
        if existing and not force:
            ColoredOutput.warning(f"Ya existe una sesión para {theme} en {date_str}")
            ColoredOutput.info(f"Estado actual: {existing.get('status', 'unknown')}")
            ColoredOutput.info("Usa --force para sobrescribir")
            return False
        
        # Crear estructura de directorios
        ColoredOutput.info("Creando estructura de directorios...")
        session_dir, created_dirs = self.create_directory_structure(theme, date_str)
        if not session_dir:
            return False
        
        for directory in created_dirs:
            ColoredOutput.success(f"Directorio creado: {directory}")
        
        # Crear archivo principal de tareas
        ColoredOutput.info("Generando archivo principal de tareas...")
        task_file = self.create_main_task_file(session_dir, theme, date_str)
        if not task_file:
            return False
        
        ColoredOutput.success(f"Archivo de tareas creado: {task_file}")
        
        # Crear archivos README para directorios
        self.create_directory_readmes(session_dir)
        
        # Actualizar tracking
        ColoredOutput.info("Actualizando sistema de tracking...")
        all_files = [task_file] + [str(d) + "/README.md" for d in [session_dir / 'support-docs', session_dir / 'assets']]
        
        if self.update_tracking(theme, date_str, all_files, session_dir):
            ColoredOutput.success("Tracking actualizado correctamente")
        else:
            ColoredOutput.warning("Error actualizando tracking, pero la sesión fue creada")
        
        # Mostrar resumen final
        self.show_session_summary(theme, date_str, session_dir)
        
        return True
    
    def create_directory_readmes(self, session_dir):
        """Crea archivos README para subdirectorios."""
        
        # README para support-docs
        support_docs_readme = session_dir / 'support-docs' / 'README.md'
        support_content = """# Support Documentation

Este directorio contiene templates generados automáticamente basados en playbooks.

## Cómo usar estos archivos:

1. **NO modifiques los playbooks originales** en `playbooks/documentation_playbooks/`
2. **SÍ completa estos templates** con información específica de tu trabajo
3. Usa los playbooks originales como **guía y referencia**

## Archivos en este directorio:

Los archivos se generan automáticamente cuando ejecutas:
```bash
python scripts/playbook-processor.py --date=FECHA --theme=TEMA
```

## Estructura típica:

- `DOC###-NombreDelPlaybook.md` - Template para completar
- Headers y secciones ya definidas
- TODOs específicos marcados
- Enlaces a playbooks originales para referencia

---
*Generado automáticamente por The Mighty Task System*
"""
        
        # README para assets
        assets_readme = session_dir / 'assets' / 'README.md'
        assets_content = """# Assets y Evidencias

Este directorio almacena todas las evidencias y archivos de soporte del trabajo diario.

## Estructura:

### `screenshots/`
- Capturas de pantalla del progreso
- Evidencias visuales de funcionalidades
- Comparaciones before/after
- Screenshots de errores o bugs

### `logs/`
- Logs de aplicación
- Output de comandos importantes
- Registros de debugging
- Archivos de configuración temporales

## Nombrado recomendado:

```
screenshots/
├── 001-initial-setup.png
├── 002-feature-implementation.png
└── 003-final-result.png

logs/
├── build-output.log
├── test-results.txt
└── debug-session.log
```

## Buenas prácticas:

- Usa nombres descriptivos
- Incluye timestamps cuando sea relevante
- Agrupa por funcionalidad o fase
- Comprime archivos grandes

---
*Generado automáticamente por The Mighty Task System*
"""
        
        # Escribir archivos
        try:
            with open(support_docs_readme, 'w', encoding='utf-8') as f:
                f.write(support_content)
            
            with open(assets_readme, 'w', encoding='utf-8') as f:
                f.write(assets_content)
            
            ColoredOutput.success("READMEs de directorios creados")
        except Exception as e:
            ColoredOutput.warning(f"Error creando READMEs: {e}")
    
    def show_session_summary(self, theme, date_str, session_dir):
        """Muestra un resumen de la sesión creada."""
        
        ColoredOutput.header("Resumen de Sesión Creada")
        
        print(f"📅 **Fecha:** {date_str}")
        print(f"🎯 **Tema:** {theme}")
        print(f"📁 **Directorio:** {session_dir}")
        print(f"📝 **Descripción:** {AVAILABLE_THEMES.get(theme, 'N/A')}")
        print(f"📚 **Playbooks:** {', '.join(THEME_PLAYBOOK_MAPPING.get(theme, ['N/A']))}")
        
        ColoredOutput.info("\nPróximos pasos recomendados:")
        print("1. Revisar el archivo de tareas creado")
        print("2. Ejecutar playbook-processor.py para generar templates")
        print("3. Comenzar el trabajo siguiendo las tareas definidas")
        print("4. Usar assets/ para evidencias y support-docs/ para documentación")
        
        ColoredOutput.info("\nComandos útiles:")
        print(f"# Generar templates de apoyo:")
        print(f"python scripts/playbook-processor.py --date={date_str} --theme={theme}")
        print(f"")
        print(f"# Verificar consistencia:")
        print(f"python scripts/consistency-checker.py --scan-all")
        print(f"")
        print(f"# Generar reporte al final:")
        print(f"python scripts/report-generator.py --date={date_str} --theme={theme}")

def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='The Mighty Task - Generador de Estructura Diaria',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Crear sesión específica
  python scripts/generate-daily.py --theme "BACKEND-API-SETUP" --date "2024-01-15"
  
  # Crear con fecha actual
  python scripts/generate-daily.py --theme "FRONTEND-COMPONENTS"
  
  # Modo automático (tema default, fecha actual)
  python scripts/generate-daily.py --auto
  
  # Sobrescribir sesión existente
  python scripts/generate-daily.py --theme "API-DESIGN" --date "2024-01-15" --force
  
  # Listar temas disponibles
  python scripts/generate-daily.py --list-themes

Temas disponibles: """ + ", ".join(AVAILABLE_THEMES.keys())
    )
    
    parser.add_argument('--theme', 
                       type=str,
                       help='Tema principal del trabajo (ej: BACKEND-API-SETUP)')
    
    parser.add_argument('--date',
                       type=str,
                       default=date.today().strftime('%Y-%m-%d'),
                       help='Fecha en formato YYYY-MM-DD (default: hoy)')
    
    parser.add_argument('--auto',
                       action='store_true',
                       help='Modo automático: usa fecha actual y tema default')
    
    parser.add_argument('--force',
                       action='store_true',
                       help='Sobrescribir sesión existente si existe')
    
    parser.add_argument('--list-themes',
                       action='store_true',
                       help='Mostrar todos los temas disponibles')
    
    parser.add_argument('--base-path',
                       type=str,
                       help='Ruta base del proyecto (default: directorio actual)')
    
    args = parser.parse_args()
    
    # Mostrar temas disponibles
    if args.list_themes:
        ColoredOutput.header("Temas Disponibles")
        for theme, description in AVAILABLE_THEMES.items():
            playbooks = THEME_PLAYBOOK_MAPPING.get(theme, [])
            print(f"🎯 **{theme}**")
            print(f"   📝 {description}")
            print(f"   📚 Playbooks: {', '.join(playbooks) if playbooks else 'N/A'}")
            print()
        return 0
    
    # Modo automático
    if args.auto:
        theme = 'BACKEND-API-SETUP'  # Tema por defecto
        date_str = date.today().strftime('%Y-%m-%d')
        ColoredOutput.info(f"Modo automático: {theme} - {date_str}")
    else:
        if not args.theme:
            ColoredOutput.error("Debes especificar un tema o usar --auto")
            ColoredOutput.info("Usa --list-themes para ver temas disponibles")
            return 1
        
        theme = args.theme.upper().replace('-', '-')  # Normalizar formato
        date_str = args.date
    
    # Crear generador y ejecutar
    try:
        generator = DailyWorkGenerator(args.base_path)
        success = generator.generate_session(theme, date_str, args.force)
        
        if success:
            ColoredOutput.success("¡Sesión de trabajo creada exitosamente!")
            return 0
        else:
            ColoredOutput.error("Error creando la sesión de trabajo")
            return 1
    
    except KeyboardInterrupt:
        ColoredOutput.warning("\nProceso cancelado por el usuario")
        return 1
    except Exception as e:
        ColoredOutput.error(f"Error inesperado: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
