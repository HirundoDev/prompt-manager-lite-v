"""
Template Detector - Shared Module
=================================

Detecta si el contenido es template vacío vs contenido real completado.
Usado por todos los scripts para asegurar consistencia en la detección.
"""

import re
from typing import Dict, List, Tuple, Optional
from pathlib import Path

class TemplateDetector:
    """Detector inteligente de templates vs contenido real."""
    
    # Patrones que indican contenido de template
    TEMPLATE_PATTERNS = [
        r'\[TODO\]',
        r'\[TECNOLOGÍA_ESPECÍFICA\]',
        r'\[FRAMEWORK_ELEGIDO\]',
        r'\[DECISIÓN:\]',
        r'\[HERRAMIENTA_ELEGIDA\]',
        r'\[ARQUITECTURA_ELEGIDA\]',
        r'\[PATRÓN_ELEGIDO\]',
        r'\[ESTRATEGIA_ELEGIDA\]',
        r'\[METODOLOGÍA_ELEGIDA\]',
        r'\*\*Decisión:\*\* \[',
        r'\*\*Herramienta:\*\* \[',
        r'\*\*Framework:\*\* \[',
        r'```\s*\[',  # Bloques de código con placeholders
        r'- \[ \] \[TODO\]',
        r'- \[ \] Definir',
        r'- \[ \] Elegir',
        r'- \[ \] Implementar',
        r'- \[ \] Configurar',
        r'Estado: \[PENDIENTE\]',
        r'Estado: \[TODO\]',
    ]
    
    # Patrones que indican contenido real completado
    COMPLETED_PATTERNS = [
        r'✅.*implementado',
        r'✅.*completado',
        r'✅.*configurado',
        r'Estado: COMPLETADO',
        r'Estado: IMPLEMENTADO',
        r'Estado: CONFIGURADO',
        r'```\w+\n[^`\[]+```',  # Código real (no placeholders)
        r'http[s]?://\S+',      # URLs reales
        r'- \[x\] [^[\]]+',     # Tareas completadas
        r'☑️',
        r'✅',
        r'npm install \w+',     # Comandos reales
        r'pip install \w+',
        r'yarn add \w+',
        r'import \w+ from',     # Imports reales
        r'from \w+ import',
        r'const \w+ = ',        # Código JavaScript real
        r'function \w+\(',      # Funciones reales
        r'class \w+[:\(]',      # Clases reales
    ]
    
    # Patrones de headers de template
    TEMPLATE_HEADERS = [
        r'# .* - Marco Universal',
        r'## Propósito del Documento',
        r'### Frameworks considerados:',
        r'### Herramientas evaluadas:',
        r'### Opciones consideradas:',
    ]
    
    @classmethod
    def is_template_content(cls, content: str) -> bool:
        """
        Determina si el contenido es principalmente template.
        
        Args:
            content: Contenido del archivo a analizar
            
        Returns:
            True si es template, False si es contenido real
        """
        if not content or len(content.strip()) < 50:
            return True
        
        # Contar indicadores de template
        template_count = sum(
            len(re.findall(pattern, content, re.IGNORECASE | re.MULTILINE))
            for pattern in cls.TEMPLATE_PATTERNS
        )
        
        # Contar indicadores de contenido completado
        completed_count = sum(
            len(re.findall(pattern, content, re.IGNORECASE | re.MULTILINE))
            for pattern in cls.COMPLETED_PATTERNS
        )
        
        # Contar líneas con contenido real (no vacías, no headers, no placeholders)
        lines = content.split('\n')
        content_lines = [
            line for line in lines 
            if line.strip() 
            and not line.strip().startswith('#')
            and not re.search(r'\[.*\]', line)
            and len(line.strip()) > 10
        ]
        
        total_lines = len([line for line in lines if line.strip()])
        
        # Lógica de decisión
        if total_lines == 0:
            return True
        
        # Si hay muchos placeholders y poco contenido real
        template_ratio = template_count / max(total_lines, 1)
        completed_ratio = completed_count / max(total_lines, 1)
        content_ratio = len(content_lines) / max(total_lines, 1)
        
        # Es template si:
        # - Más del 40% son placeholders de template
        # - Menos del 20% es contenido completado
        # - Menos del 30% son líneas con contenido real
        is_template = (
            template_ratio > 0.4 or
            (completed_ratio < 0.2 and content_ratio < 0.3) or
            (template_count > 5 and completed_count == 0)
        )
        
        return is_template
    
    @classmethod
    def analyze_content_quality(cls, content: str) -> Dict[str, any]:
        """
        Analiza la calidad y completitud del contenido.
        
        Returns:
            Dict con análisis detallado del contenido
        """
        if not content:
            return {
                'type': 'empty',
                'completeness': 0.0,
                'template_indicators': 0,
                'completed_indicators': 0,
                'quality_score': 0.0
            }
        
        template_count = sum(
            len(re.findall(pattern, content, re.IGNORECASE | re.MULTILINE))
            for pattern in cls.TEMPLATE_PATTERNS
        )
        
        completed_count = sum(
            len(re.findall(pattern, content, re.IGNORECASE | re.MULTILINE))
            for pattern in cls.COMPLETED_PATTERNS
        )
        
        lines = content.split('\n')
        total_lines = len([line for line in lines if line.strip()])
        
        # Calcular completitud
        if template_count + completed_count == 0:
            completeness = 0.5  # Contenido neutro
        else:
            completeness = completed_count / (template_count + completed_count)
        
        # Determinar tipo
        if cls.is_template_content(content):
            content_type = 'template'
        elif completeness > 0.8:
            content_type = 'completed'
        elif completeness > 0.3:
            content_type = 'partial'
        else:
            content_type = 'minimal'
        
        # Calcular score de calidad (0-1)
        quality_score = min(1.0, (
            completeness * 0.6 +
            min(1.0, len(content) / 1000) * 0.2 +  # Longitud
            min(1.0, total_lines / 50) * 0.2       # Número de líneas
        ))
        
        return {
            'type': content_type,
            'completeness': completeness,
            'template_indicators': template_count,
            'completed_indicators': completed_count,
            'quality_score': quality_score,
            'total_lines': total_lines,
            'content_length': len(content)
        }
    
    @classmethod
    def is_meaningful_content(cls, file_path: Path) -> bool:
        """
        Determina si un archivo tiene contenido significativo para fusión.
        
        Args:
            file_path: Ruta al archivo a analizar
            
        Returns:
            True si tiene contenido significativo
        """
        try:
            content = file_path.read_text(encoding='utf-8')
            analysis = cls.analyze_content_quality(content)
            
            # Es significativo si:
            # - No es template Y tiene buena completitud
            # - O tiene score de calidad alto
            return (
                analysis['type'] != 'template' and analysis['completeness'] > 0.3
            ) or analysis['quality_score'] > 0.6
            
        except Exception:
            return False
    
    @classmethod
    def should_include_in_fusion(cls, content: str) -> bool:
        """
        Determina si el contenido debe incluirse en fusión de playbooks.
        
        Args:
            content: Contenido a evaluar
            
        Returns:
            True si debe incluirse en fusión
        """
        if cls.is_template_content(content):
            return False
        
        analysis = cls.analyze_content_quality(content)
        
        # Incluir si tiene contenido real significativo
        return (
            analysis['completed_indicators'] > 2 or
            analysis['quality_score'] > 0.4 or
            analysis['completeness'] > 0.3
        )
    
    @classmethod
    def extract_template_placeholders(cls, content: str) -> List[str]:
        """
        Extrae todos los placeholders de template encontrados.
        
        Returns:
            Lista de placeholders únicos encontrados
        """
        placeholders = set()
        
        for pattern in cls.TEMPLATE_PATTERNS:
            matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE)
            placeholders.update(matches)
        
        return sorted(list(placeholders))
    
    @classmethod
    def get_completion_suggestions(cls, content: str) -> List[str]:
        """
        Genera sugerencias para completar un template.
        
        Returns:
            Lista de sugerencias de completitud
        """
        suggestions = []
        placeholders = cls.extract_template_placeholders(content)
        
        if '[TECNOLOGÍA_ESPECÍFICA]' in placeholders:
            suggestions.append("Definir tecnología específica a usar")
        
        if '[FRAMEWORK_ELEGIDO]' in placeholders:
            suggestions.append("Seleccionar framework principal")
        
        if '[TODO]' in placeholders:
            suggestions.append("Completar elementos marcados como TODO")
        
        if '[ ]' in content:
            suggestions.append("Marcar tareas completadas con [x]")
        
        analysis = cls.analyze_content_quality(content)
        if analysis['completeness'] < 0.3:
            suggestions.append("Agregar más contenido específico del proyecto")
        
        return suggestions