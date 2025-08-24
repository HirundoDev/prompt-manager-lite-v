"""
Templates Universales para Playbook Processor
==============================================

Este módulo contiene todos los templates universales organizados por categoría.

Templates disponibles:
- frontend: Templates para arquitectura y dependencias frontend
- backend: Templates para arquitectura y dependencias backend  
- data: Templates para modelado de datos y APIs
- infrastructure: Templates para deployment y DevOps
- testing: Templates para estrategias de testing
- cli: Templates para desarrollo de CLI
"""

from .frontend import (
    create_design_system_template,
    create_frontend_architecture_template, 
    create_frontend_dependencies_template
)
from .backend import (
    create_backend_architecture_template,
    create_backend_dependencies_template
)
from .data import (
    create_api_specification_template,
    create_data_model_template
)
from .infrastructure import (
    create_deployment_template
)
from .testing import (
    create_testing_strategy_template
)
from .cli import (
    create_cli_reference_template
)
from .base import create_generic_template

# Registry de templates por tipo
TEMPLATE_REGISTRY = {
    'design_system': create_design_system_template,
    'frontend_architecture': create_frontend_architecture_template,
    'frontend_dependencies': create_frontend_dependencies_template,
    'backend_architecture': create_backend_architecture_template,
    'backend_dependencies': create_backend_dependencies_template,
    'api_specification': create_api_specification_template,
    'data_model': create_data_model_template,
    'deployment': create_deployment_template,
    'testing_strategy': create_testing_strategy_template,
    'cli_reference': create_cli_reference_template,
    'generic': create_generic_template
}

def get_template_function(template_type):
    """
    Obtiene la función de template según el tipo.
    
    Args:
        template_type (str): Tipo de template
        
    Returns:
        function: Función para crear el template
    """
    return TEMPLATE_REGISTRY.get(template_type, create_generic_template)

__all__ = [
    'TEMPLATE_REGISTRY',
    'get_template_function',
    'create_design_system_template',
    'create_frontend_architecture_template', 
    'create_frontend_dependencies_template',
    'create_backend_architecture_template',
    'create_backend_dependencies_template',
    'create_api_specification_template',
    'create_data_model_template',
    'create_deployment_template',
    'create_testing_strategy_template',
    'create_cli_reference_template',
    'create_generic_template'
]
