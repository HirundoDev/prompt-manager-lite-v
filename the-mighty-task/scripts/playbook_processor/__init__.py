"""
The Mighty Task - Playbook Processor Package
============================================

Paquete modular para procesamiento de playbooks y generación de templates.

Modules:
- processor: Clase principal PlaybookProcessor
- templates: Templates universales organizados por categoría
- utils: Utilidades compartidas
"""

from .processor import PlaybookProcessor
from .utils import ColoredOutput

__version__ = "2.0.0"
__all__ = ["PlaybookProcessor", "ColoredOutput"]
