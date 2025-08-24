#!/usr/bin/env python3
"""
The Mighty Task - Mission Resumer (Fusionador Inteligente de Playbooks)
========================================================================

Script para FUSIONAR múltiples sesiones de trabajo del mismo tema en una sola estructura.
La clave está en la FUSIÓN INTELIGENTE de playbooks del mismo tipo desde diferentes sesiones.

Funcionalidad principal:
1. Busca todas las carpetas daily-work/ que contengan el tema especificado
2. Identifica playbooks comunes (ej: DOC006-BackendArchitecture.md)
3. FUSIONA de manera inteligente los contenidos SIN sobrescribir
4. Consolida assets, charts y support-docs en estructura plana
5. Valida que no existe contenido duplicado antes de agregarlo

Ejemplo:
  daily-work/2025-01-15_BACKEND/support-docs/DOC006-BackendArchitecture.md (50% completado)
  daily-work/2025-01-16_BACKEND/support-docs/DOC006-BackendArchitecture.md (otros 30% completado)
  
  →  mission-resumes/DOC006-BackendArchitecture.md (80% completado, fusionado)

Uso:
    python mission-resumer.py --theme="BACKEND"
"""

import argparse
import shutil
import hashlib
from datetime import datetime
from pathlib import Path
from collections import defaultdict
import json
import re

class PlaybookFuser:
    def __init__(self, base_path=None):
        self.base_path = Path(base_path or Path(__file__).parent.parent)
        self.daily_work_dir = self.base_path / "daily-work"
        self.mission_resumes_dir = self.base_path / "mission-resumes"
        self.mission_resumes_dir.mkdir(exist_ok=True)
        self.copied_files = []
        self.fused_playbooks = []
        self.consolidation_log = []

    def find_theme_sessions(self, theme):
        """Encontrar todas las sesiones de trabajo que coincidan con el tema"""
        pattern = f"*_{theme}*"
        theme_folders = list(self.daily_work_dir.glob(pattern))
        
        if not theme_folders:
            raise FileNotFoundError(f"No se encontraron sesiones para tema: {theme}")
        
        sessions = []
        for folder in sorted(theme_folders):
            # Buscar archivo de tareas dentro de cada carpeta
            task_files = list(folder.glob("pending-tasks-*.md"))
            if task_files:
                sessions.append({
                    'folder': folder,
                    'date': self._extract_date_from_path(folder.name),
                    'theme': self._extract_theme_from_path(folder.name),
                    'task_file': task_files[0],
                    'assets_dir': folder / "assets",
                    'charts_dir': folder / "charts", 
                    'support_docs_dir': folder / "support-docs"
                })
                
        return sessions

    def _extract_date_from_path(self, path_name):
        """Extraer fecha del nombre de la carpeta"""
        match = re.search(r'(\d{4}-\d{2}-\d{2})', path_name)
        return match.group(1) if match else 'Unknown'

    def _extract_theme_from_path(self, path_name):
        """Extraer tema del nombre de la carpeta"""
        match = re.search(r'\d{4}-\d{2}-\d{2}_(.+)', path_name)
        return match.group(1) if match else 'Unknown'

    def consolidate_sessions(self, theme):
        """Consolidar múltiples sesiones fusionando playbooks inteligentemente"""
        print(f"🔄 Consolidando y fusionando sesiones para tema: {theme}")
        
        # Encontrar todas las sesiones del tema
        sessions = self.find_theme_sessions(theme)
        print(f"📁 Sesiones encontradas: {len(sessions)}")
        
        if not sessions:
            print("❌ No se encontraron sesiones para consolidar")
            return None
        
        # Usar directamente mission-resumes/ sin subcarpeta
        consolidated_dir = self.mission_resumes_dir
        
        # Crear subdirectorios para assets, charts, support-docs
        (consolidated_dir / "assets").mkdir(exist_ok=True)
        (consolidated_dir / "charts").mkdir(exist_ok=True)
        (consolidated_dir / "support-docs").mkdir(exist_ok=True)
        
        print(f"📂 Consolidando directamente en: {consolidated_dir}")
        
        # Identificar todos los playbooks a fusionar
        playbook_sessions = self._identify_playbooks_to_fuse(sessions)
        print(f"📚 Playbooks identificados para fusión: {len(playbook_sessions)}")
        
        # Fusionar cada playbook
        for playbook_name, sessions_with_playbook in playbook_sessions.items():
            print(f"\n📖 Fusionando playbook: {playbook_name}")
            self._fuse_playbook(playbook_name, sessions_with_playbook, consolidated_dir)
        
        # Consolidar assets, charts y support-docs (archivos no-playbook)
        self._consolidate_non_playbook_files(sessions, consolidated_dir)
        
        # Generar log de consolidación
        self._generate_consolidation_log(consolidated_dir, sessions)
        
        # Generar resumen final
        resume_file = self._generate_consolidated_resume(sessions, consolidated_dir, "consolidation-resume.md")
        
        return resume_file

    def _identify_playbooks_to_fuse(self, sessions):
        """Identificar qué playbooks existen en múltiples sesiones para fusionar"""
        playbook_sessions = defaultdict(list)
        
        for session in sessions:
            support_docs_dir = session['support_docs_dir']
            if support_docs_dir.exists():
                # Buscar archivos que parecen playbooks (DOCxxx-*.md)
                playbook_files = list(support_docs_dir.glob("DOC*.md"))
                
                for playbook_file in playbook_files:
                    playbook_name = playbook_file.name
                    playbook_sessions[playbook_name].append({
                        'session': session,
                        'file_path': playbook_file
                    })
        
        # Solo retornar playbooks que aparecen en múltiples sesiones O tienen contenido significativo
        filtered_playbooks = {}
        for playbook_name, sessions_list in playbook_sessions.items():
            if len(sessions_list) > 1 or self._has_meaningful_content(sessions_list[0]['file_path']):
                filtered_playbooks[playbook_name] = sessions_list
                print(f"   📋 {playbook_name}: {len(sessions_list)} sesiones")
        
        return filtered_playbooks

    def _has_meaningful_content(self, file_path):
        """Verificar si el archivo tiene contenido real (no solo template)"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Buscar indicadores de contenido completado
            indicators = [
                r'✅', r'☑️', r'COMPLETADO', r'IMPLEMENTADO',
                r'```\w+', r'http[s]?://', r'`[^`]+`',
                r'- \[x\]', r'Estado: COMPLETADO'
            ]
            
            content_indicators = sum(1 for pattern in indicators if re.search(pattern, content))
            lines_with_content = len([line for line in content.split('\n') if line.strip() and not line.strip().startswith('#')])
            
            return content_indicators >= 2 or lines_with_content > 20
            
        except Exception:
            return False

    def _fuse_playbook(self, playbook_name, sessions_with_playbook, consolidated_dir):
        """Fusionar múltiples versiones del mismo playbook por secciones semánticas"""
        
        # Recopilar todo el contenido de todas las versiones
        all_contents = []
        for session_info in sessions_with_playbook:
            try:
                with open(session_info['file_path'], 'r', encoding='utf-8') as f:
                    content = f.read()
                    all_contents.append({
                        'session': session_info['session'],
                        'content': content,
                        'date': session_info['session']['date']
                    })
                print(f"     📄 Cargado desde {session_info['session']['date']}")
            except Exception as e:
                print(f"     ❌ Error cargando {session_info['session']['date']}: {e}")
        
        if not all_contents:
            print(f"     ⚠️  No se pudo cargar contenido para {playbook_name}")
            return
        
        # Ordenar por fecha para procesamiento cronológico
        all_contents.sort(key=lambda x: x['date'])
        
        # Parsear secciones de cada archivo
        all_sections = []
        for content_info in all_contents:
            sections = self._parse_sections(content_info['content'])
            all_sections.append({
                'date': content_info['date'],
                'sections': sections
            })
        
        # Fusionar secciones inteligentemente
        fused_sections = self._merge_sections_semantically(all_sections)
        
        # Regenerar contenido desde secciones fusionadas
        fused_content = self._rebuild_content_from_sections(fused_sections)
        
        # Escribir archivo fusionado directamente en mission-resumes/
        fused_file_path = consolidated_dir / playbook_name
        try:
            with open(fused_file_path, 'w', encoding='utf-8') as f:
                f.write(fused_content)
            
            lines_count = len(fused_content.splitlines())
            self.fused_playbooks.append({
                'playbook': playbook_name,
                'sessions_count': len(sessions_with_playbook),
                'final_lines': lines_count,
                'output_path': fused_file_path
            })
            
            print(f"     ✅ Playbook fusionado: {fused_file_path.name} ({lines_count} líneas) - REEMPLAZADO")
            
        except Exception as e:
            print(f"     ❌ Error escribiendo playbook fusionado: {e}")

    def _parse_sections(self, content):
        """Parsear contenido en secciones por headers"""
        lines = content.split('\n')
        sections = []
        current_section = {'header': '', 'level': 0, 'content': []}
        
        for line in lines:
            stripped = line.strip()
            
            # Detectar headers (## Header, ### Subheader, etc.)
            if stripped.startswith('#'):
                # Guardar sección anterior si tiene contenido
                if current_section['header'] or current_section['content']:
                    sections.append(current_section.copy())
                
                # Iniciar nueva sección
                header_level = 0
                for char in stripped:
                    if char == '#':
                        header_level += 1
                    else:
                        break
                
                current_section = {
                    'header': stripped.lstrip('# ').strip(),
                    'level': header_level,
                    'content': [line]  # Incluir la línea del header
                }
            else:
                # Agregar línea a la sección actual
                current_section['content'].append(line)
        
        # Agregar la última sección
        if current_section['header'] or current_section['content']:
            sections.append(current_section)
        
        return sections
    
    def _merge_sections_semantically(self, all_sections):
        """Fusionar secciones por contenido semántico, evitando duplicados"""
        fused_sections = {}
        
        for content_info in all_sections:
            date = content_info['date']
            sections = content_info['sections']
            
            for section in sections:
                header_key = section['header'].lower().strip()
                
                # Omitir secciones vacías o de template
                if self._is_template_section(section):
                    continue
                
                if header_key not in fused_sections:
                    # Primera vez que vemos esta sección
                    fused_sections[header_key] = {
                        'header': section['header'],
                        'level': section['level'],
                        'content_blocks': [{
                            'date': date,
                            'content': section['content']
                        }],
                        'merged_content': section['content']
                    }
                else:
                    # Ya existe, fusionar contenido
                    existing_section = fused_sections[header_key]
                    new_content = self._merge_section_content(
                        existing_section['merged_content'], 
                        section['content'], 
                        date
                    )
                    
                    existing_section['content_blocks'].append({
                        'date': date,
                        'content': section['content']
                    })
                    existing_section['merged_content'] = new_content
        
        return fused_sections
    
    def _is_template_section(self, section):
        """Detectar si una sección es solo template vacío"""
        content_text = '\n'.join(section['content']).strip()
        
        # Contar indicadores de template vacío
        template_indicators = content_text.count('[TODO]')
        todo_lines = len([line for line in section['content'] if '[TODO]' in line])
        content_lines = len([line for line in section['content'] if line.strip() and not line.strip().startswith('#')])
        
        # Si hay muchos TODOs y poco contenido real, es template
        if todo_lines > 0 and content_lines > 0:
            todo_ratio = todo_lines / content_lines
            return todo_ratio > 0.7  # Más del 70% son TODOs
        
        return False
    
    def _merge_section_content(self, base_content, new_content, source_date):
        """Fusionar contenido de dos secciones evitando duplicados exactos"""
        base_lines = [line.strip() for line in base_content]
        new_lines = [line.strip() for line in new_content]
        
        # Usar líneas exactas para evitar duplicados
        base_set = set(base_lines)
        merged_lines = base_content.copy()
        
        additions = 0
        for i, new_line in enumerate(new_content):
            stripped_new = new_line.strip()
            
            # Omitir líneas vacías, headers duplicados y TODOs genéricos
            if not stripped_new or stripped_new.startswith('#') or stripped_new == '[TODO]':
                continue
            
            # Si la línea es completamente nueva, agregarla
            if stripped_new not in base_set:
                # Buscar punto de inserción inteligente
                insertion_point = self._find_smart_insertion_point(merged_lines, new_line)
                merged_lines.insert(insertion_point, new_line)
                base_set.add(stripped_new)
                additions += 1
        
        if additions > 0:
            print(f"         ➕ {additions} líneas únicas agregadas desde {source_date}")
        
        return merged_lines
    
    def _find_smart_insertion_point(self, existing_lines, new_line):
        """Encontrar el mejor punto para insertar una línea nueva"""
        new_stripped = new_line.strip()
        
        # Si es una lista, insertar cerca de otras listas
        if new_stripped.startswith(('- ', '* ', '+ ', '1. ', '2. ', '3. ')):
            for i in range(len(existing_lines) - 1, -1, -1):
                if existing_lines[i].strip().startswith(('- ', '* ', '+ ')):
                    return i + 1
        
        # Si es código, insertar cerca de otros bloques de código
        if new_stripped.startswith('```') or '`' in new_stripped:
            for i in range(len(existing_lines) - 1, -1, -1):
                if '```' in existing_lines[i] or '`' in existing_lines[i]:
                    return i + 1
        
        # Por defecto, insertar al final antes de líneas vacías
        for i in range(len(existing_lines) - 1, -1, -1):
            if existing_lines[i].strip():
                return i + 1
        
        return len(existing_lines)
    
    def _rebuild_content_from_sections(self, fused_sections):
        """Reconstruir contenido completo desde secciones fusionadas"""
        content_lines = []
        
        # Ordenar secciones por nivel y nombre para consistencia
        sorted_sections = sorted(
            fused_sections.items(),
            key=lambda x: (x[1]['level'], x[0])
        )
        
        for header_key, section_data in sorted_sections:
            # Agregar contenido de la sección
            content_lines.extend(section_data['merged_content'])
            content_lines.append('')  # Línea vacía entre secciones
        
        # Limpiar líneas vacías excesivas al final
        while content_lines and not content_lines[-1].strip():
            content_lines.pop()
        
        return '\n'.join(content_lines)

    def _merge_content_lines(self, base_lines, additional_lines, source_date):
        """Fusionar líneas de contenido evitando duplicados"""
        merged_lines = base_lines.copy()
        base_content_hash = set(hashlib.md5(line.encode()).hexdigest() for line in base_lines if line.strip())
        
        additions = 0
        for line in additional_lines:
            if not line.strip():
                continue
            
            line_hash = hashlib.md5(line.encode()).hexdigest()
            
            # Si la línea no existe, buscar dónde insertarla
            if line_hash not in base_content_hash:
                # Buscar contexto similar para insertar en lugar apropiado
                insertion_point = self._find_best_insertion_point(merged_lines, line)
                merged_lines.insert(insertion_point, line)
                base_content_hash.add(line_hash)
                additions += 1
        
        if additions > 0:
            print(f"       📝 {additions} líneas nuevas agregadas desde {source_date}")
        
        return merged_lines

    def _find_best_insertion_point(self, existing_lines, new_line):
        """Encontrar el mejor punto de inserción para una nueva línea"""
        # Estrategia simple: agregar al final de la sección similar o al final del archivo
        
        # Si es un header (empieza con #), insertarlo en orden
        if new_line.strip().startswith('#'):
            header_level = len(new_line.split()[0])
            for i, existing_line in enumerate(existing_lines):
                if existing_line.strip().startswith('#'):
                    existing_level = len(existing_line.split()[0]) if existing_line.split() else 0
                    if existing_level >= header_level:
                        return i
            return len(existing_lines)
        
        # Si es contenido de lista, insertarlo cerca de listas similares
        if new_line.strip().startswith(('- ', '* ', '1. ')):
            for i in range(len(existing_lines) - 1, -1, -1):
                if existing_lines[i].strip().startswith(('- ', '* ', '1. ')):
                    return i + 1
        
        # Por defecto, insertar al final
        return len(existing_lines)

    def _consolidate_non_playbook_files(self, sessions, consolidated_dir):
        """Consolidar assets, charts y otros archivos que no son playbooks"""
        file_hashes = {}
        
        for session in sessions:
            print(f"\n📁 Consolidando archivos de {session['date']}")
            
            # Consolidar assets - AGREGAR a carpeta
            if session['assets_dir'].exists():
                self._copy_files_to_consolidated(session['assets_dir'], 
                                               consolidated_dir / "assets",
                                               file_hashes, session['date'])
            
            # Consolidar charts - AGREGAR a carpeta
            if session['charts_dir'].exists():
                self._copy_files_to_consolidated(session['charts_dir'], 
                                               consolidated_dir / "charts",
                                               file_hashes, session['date'])
            
            # Consolidar support-docs (solo no-playbooks) - AGREGAR a carpeta
            if session['support_docs_dir'].exists():
                self._copy_non_playbook_support_docs(session['support_docs_dir'], 
                                                   consolidated_dir / "support-docs",
                                                   file_hashes, session['date'])

    def _copy_files_to_consolidated(self, source_dir, dest_dir, file_hashes, prefix):
        """Copiar archivos evitando duplicados"""
        copied = 0
        skipped = 0
        
        for file_path in source_dir.rglob("*"):
            if file_path.is_file():
                file_hash = self._get_file_hash(file_path)
                
                if file_hash and file_hash in file_hashes:
                    skipped += 1
                    continue
                
                # Mantener nombre original - solo agregar si no existe o es diferente
                dest_name = file_path.name  # Usar nombre original
                dest_path = dest_dir / dest_name
                
                # Si existe y es idéntico, omitir
                if dest_path.exists():
                    existing_hash = self._get_file_hash(dest_path)
                    if existing_hash == file_hash:
                        skipped += 1
                        continue
                
                try:
                    shutil.copy2(file_path, dest_path)
                    
                    if file_hash:
                        file_hashes[file_hash] = file_path
                    
                    self.copied_files.append((file_path, dest_path))
                    copied += 1
                    
                except Exception as e:
                    print(f"       ❌ Error copiando {file_path.name}: {e}")
        
        if copied > 0 or skipped > 0:
            print(f"       📂 {copied} archivos copiados, {skipped} duplicados omitidos")

    def _copy_non_playbook_support_docs(self, source_dir, dest_dir, file_hashes, prefix):
        """Copiar solo archivos de support-docs que NO son playbooks"""
        for file_path in source_dir.rglob("*.md"):
            if file_path.is_file() and not file_path.name.startswith("DOC"):
                file_hash = self._get_file_hash(file_path)
                
                if file_hash and file_hash in file_hashes:
                    continue
                
                dest_name = f"{prefix}_{file_path.name}"
                dest_path = dest_dir / dest_name
                
                try:
                    shutil.copy2(file_path, dest_path)
                    
                    if file_hash:
                        file_hashes[file_hash] = file_path
                    
                    self.copied_files.append((file_path, dest_path))
                    
                except Exception as e:
                    print(f"       ❌ Error copiando {file_path.name}: {e}")

    def _get_file_hash(self, file_path):
        """Obtener hash MD5 de un archivo"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception:
            return None

    def _generate_consolidated_resume(self, sessions, consolidated_dir, output_filename):
        """Generar resumen final de la consolidación"""
        resume_path = self.mission_resumes_dir / output_filename
        
        content = f"""# Resumen de Consolidación Inteligente - {sessions[0]['theme'] if sessions else 'Unknown'}

**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Sesiones fusionadas:** {len(sessions)}  
**Directorio consolidado:** `{consolidated_dir.relative_to(self.base_path)}`

---

## 📊 Métricas de Consolidación

| Métrica | Valor |
|---------|-------|
| Sesiones procesadas | {len(sessions)} |
| Playbooks fusionados | {len(self.fused_playbooks)} |
| Archivos copiados | {len(self.copied_files)} |
| Directorio de salida | `{consolidated_dir.name}/` |

---

## 📚 Playbooks Fusionados

"""

        for fused in self.fused_playbooks:
            content += f"""### {fused['playbook']}

- **Sesiones fusionadas:** {fused['sessions_count']}
- **Líneas finales:** {fused['final_lines']}
- **Archivo:** `{fused['output_path'].relative_to(consolidated_dir)}`

"""

        content += f"""---

## 📅 Sesiones Consolidadas

"""

        for session in sessions:
            content += f"""### {session['date']} - {session['theme']}

- **Carpeta original:** `{session['folder'].relative_to(self.base_path)}`
- **Archivo de tareas:** `{session['task_file'].relative_to(self.base_path)}`

"""

        content += f"""---

## 📁 Estructura Final

```
{consolidated_dir.name}/
├── DOCxxx-*.md          # Playbooks fusionados inteligentemente
├── assets/              # Todos los assets consolidados
├── charts/              # Todos los charts consolidados
├── support-docs/        # Documentos de apoyo adicionales
└── consolidation-log.json
```

### Archivos Consolidados ({len(self.copied_files)} total)

"""

        # Listar archivos por tipo
        files_by_type = defaultdict(list)
        for source, dest in self.copied_files:
            if "/assets/" in str(dest):
                files_by_type["Assets"].append(dest.name)
            elif "/charts/" in str(dest):
                files_by_type["Charts"].append(dest.name)
            elif "/support-docs/" in str(dest):
                files_by_type["Documentos"].append(dest.name)

        for file_type, files in files_by_type.items():
            content += f"\n**{file_type}** ({len(files)}):\n"
            for file in sorted(files)[:10]:
                content += f"- `{file}`\n"
            if len(files) > 10:
                content += f"- ... y {len(files) - 10} más\n"

        content += f"""

---

## 💡 Beneficios de la Fusión Inteligente

- ✅ **Playbooks completados progresivamente** desde múltiples sesiones
- ✅ **Sin pérdida de información** - todo el contenido se preserva
- ✅ **Eliminación de duplicados** automática por hash MD5
- ✅ **Estructura plana** fácil de navegar y usar
- ✅ **Historial completo** en log de consolidación

### Usar los playbooks fusionados:

```bash
# Ver todos los playbooks fusionados
ls {consolidated_dir.relative_to(self.base_path)}/DOC*.md

# Ver assets consolidados
ls {consolidated_dir.relative_to(self.base_path)}/assets/

# Ver log de fusión
cat {consolidated_dir.relative_to(self.base_path)}/consolidation-log.json
```

---

*Consolidación inteligente generada por The Mighty Task - Mission Resumer*
"""

        with open(resume_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n✅ Resumen generado: {resume_path}")
        return resume_path

    def _generate_consolidation_log(self, consolidated_dir, sessions):
        """Generar log detallado de la consolidación"""
        log_path = consolidated_dir / "consolidation-log.json"
        
        log_data = {
            'consolidation_date': datetime.now().isoformat(),
            'consolidation_type': 'intelligent_fusion',
            'sessions_processed': len(sessions),
            'playbooks_fused': len(self.fused_playbooks),
            'files_copied': len(self.copied_files),
            'sessions_detail': [
                {
                    'date': session['date'],
                    'theme': session['theme'],
                    'source_folder': str(session['folder'])
                }
                for session in sessions
            ],
            'fused_playbooks': [
                {
                    'name': fused['playbook'],
                    'sessions_count': fused['sessions_count'],
                    'final_lines': fused['final_lines'],
                    'output_path': str(fused['output_path'])
                }
                for fused in self.fused_playbooks
            ],
            'copied_files': [
                {
                    'source': str(source),
                    'destination': str(dest)
                }
                for source, dest in self.copied_files
            ]
        }
        
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)
        
        print(f"📋 Log de consolidación guardado: {log_path}")

def main():
    parser = argparse.ArgumentParser(
        description='Fusionar múltiples sesiones de trabajo con fusión inteligente de playbooks',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python mission-resumer.py --theme="BACKEND"
  python mission-resumer.py --theme="FRONTEND"

El script realiza FUSIÓN INTELIGENTE:
1. Identifica playbooks comunes entre sesiones (ej: DOC006-BackendArchitecture.md)
2. Fusiona contenido sin sobrescribir - solo complementa información nueva
3. Consolida assets, charts y support-docs en estructura plana
4. Genera log detallado de toda la operación de fusión
        """
    )
    
    parser.add_argument(
        '--theme', 
        required=True,
        help='Tema a buscar en nombres de carpetas (ej: BACKEND, FRONTEND, API)'
    )
    
    
    parser.add_argument(
        '--base-path',
        help='Ruta base del proyecto (default: directorio padre del script)'
    )
    
    args = parser.parse_args()
    
    try:
        fuser = PlaybookFuser(args.base_path)
        resume_file = fuser.consolidate_sessions(args.theme)
        
        if resume_file:
            print(f"""
🎉 ¡Fusión inteligente completada exitosamente!

📍 Resumen: {resume_file}
📚 Playbooks fusionados: {len(fuser.fused_playbooks)}
📁 Archivos copiados: {len(fuser.copied_files)}

🎯 La fusión inteligente logró:
- Combinar playbooks del mismo tipo sin sobrescribir
- Preservar todo el contenido de múltiples sesiones  
- Eliminar duplicados automáticamente
- Crear estructura plana fácil de usar

💡 Accede a los playbooks fusionados en:
   mission-resumes/
        """)
        else:
            print("❌ No se pudo completar la fusión")
        
    except Exception as e:
        print(f"❌ Error durante la fusión: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())
