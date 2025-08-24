"""
Utilidades para el Playbook Processor
=====================================

Contiene clases y funciones de utilidad compartidas.
"""

# Mapeo de temas a playbooks (igual que en generate-daily.py)
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

# Mapeo de códigos DOC a nombres de archivos
PLAYBOOK_FILE_MAPPING = {
    'DOC003': 'DOC003-DesignSystem.md',
    'DOC004': 'DOC004-FrontendArchitecture.md',
    'DOC005': 'DOC005-FrontendDependencies.md',
    'DOC006': 'DOC006-BackendArchitecture.md',
    'DOC007': 'DOC007-BackendDependencies.md',
    'DOC008': 'DOC008-APISpecification.md',
    'DOC009': 'DOC009-DataModel.md',
    'DOC010': 'DOC010-Deployment.md',
    'DOC011': 'DOC011-TestingStrategy.md',
    'DOC019': 'DOC019-CLI-Command-Reference.md'
}

class ColoredOutput:
    """Clase para output con colores en terminal."""
    COLORS = {
        'RED': '\\033[91m',
        'GREEN': '\\033[92m',
        'YELLOW': '\\033[93m',
        'BLUE': '\\033[94m',
        'MAGENTA': '\\033[95m',
        'CYAN': '\\033[96m',
        'WHITE': '\\033[97m',
        'BOLD': '\\033[1m',
        'UNDERLINE': '\\033[4m',
        'END': '\\033[0m'
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
        cls.print(f"\\n{'=' * 60}", 'BLUE')
        cls.print(f"  {text}", 'BLUE', bold=True, underline=True)
        cls.print(f"{'=' * 60}\\n", 'BLUE')
