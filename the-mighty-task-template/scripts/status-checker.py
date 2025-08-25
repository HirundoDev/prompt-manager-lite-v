#!/usr/bin/env python3
"""
Status Checker - Main Entry Point
=================================

Script principal para verificar estado del sistema con análisis de calidad mejorado.
Mantiene compatibilidad con la interface original mientras usa la nueva arquitectura modular.
"""

import sys
from pathlib import Path

# Agregar el directorio de scripts al path
scripts_dir = Path(__file__).parent
sys.path.insert(0, str(scripts_dir))

# Importar y ejecutar CLI
from status_checker.cli import main

if __name__ == "__main__":
    sys.exit(main())