"""
Colored Output - Shared Module
==============================

Utilidad compartida para output colorido en terminal.
Usado por todos los scripts para consistencia visual.
"""

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
    
    @classmethod
    def section(cls, text):
        cls.print(f"\n--- {text} ---", 'MAGENTA', bold=True)
    
    @classmethod
    def progress(cls, text):
        cls.print(f"🔄 {text}", 'CYAN')
    
    @classmethod
    def debug(cls, text):
        cls.print(f"🐛 {text}", 'WHITE')