#!/usr/bin/env python3
"""
Consistency Checker - Main Entry Point
=====================================

Script principal para verificar integridad del sistema con validaciones mejoradas.
Mantiene compatibilidad con la interface original mientras usa la nueva arquitectura modular.
"""

import sys
from pathlib import Path

# Agregar el directorio de scripts al path
scripts_dir = Path(__file__).parent
sys.path.insert(0, str(scripts_dir))

# Importar y ejecutar CLI
from consistency_checker.cli import main

if __name__ == "__main__":
    sys.exit(main())